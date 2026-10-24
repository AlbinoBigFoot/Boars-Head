"""Generate the tag reference pages of the wiki (docs/tags/reference/**) from the gateway files on disk.

    python -I wiki/tools/gen_tags.py          # or: python -I wiki/tools/gen_all.py tags

Reads (never writes) the Ignition 8.3 tag configuration under gateways/standard/data/config/resources/core/ignition:
tag-type-definition (UDT definitions), tag-definition (instances, _Config, the _RCP1_ browse mirror), tag-group,
tag-provider, plus the BH project (views / scripts, for "read by" cross references) and .gitignore (tracked or not).

Writes ONLY docs/tags/reference/**: one page per UDT definition, one page per device instance folder under
[default]Boars_Head, the tag group table, the _Config tag list, the _RCP1_ mirror summary, an alarm index and a
history index. Every page carries `generated: true` in its front matter.

Safety: tag VALUES are never printed for _Config / instance tags (some hold credentials); UDT default values are
shown only when short and not credential-like, and IPv4 addresses are masked.

Stdlib only, UTF-8.
"""
from __future__ import annotations

import bisect
import json
import os
import re

import subprocess
import sys
import urllib.parse
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

GW = "gateways/standard/data"
CORE = f"{GW}/config/resources/core"
IGN = f"{CORE}/ignition"
PROJ = f"{GW}/projects/BH"

# What this reference tool reads (repo-relative globs); gen_all.py hashes them into wiki/tools/manifest/sources.json.
SOURCES = [
    f"{IGN}/tag-definition/**/*.json",
    f"{IGN}/tag-type-definition/**/*.json",
    f"{IGN}/tag-group/**/*.json",
    f"{IGN}/tag-provider/**/*.json",
    f"{CORE}/com.inductiveautomation.historian/**/*.json",
    f"{IGN}/alarm-journal/**/*.json",
    f"{PROJ}/com.inductiveautomation.perspective/views/**/view.json",
    f"{PROJ}/com.inductiveautomation.perspective/page-config/*.json",
    f"{PROJ}/com.inductiveautomation.perspective/session-props/*.json",
    f"{PROJ}/com.inductiveautomation.perspective/session-permissions/*.json",
    f"{PROJ}/com.inductiveautomation.webdev/resources/**/*.py",
    f"{PROJ}/ignition/**/*.py",
    f"{PROJ}/ignition/**/*.json",
    ".gitignore",
]
BANNER = ":::note\nThis reference page is generated from the project files.\n:::\n"

SECRET_NAME = re.compile(r"token|password|passwd|secret|api.?key|credential", re.I)
IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


# ----------------------------------------------------------------------------------------------------------------
# Markdown / MDX helpers
# ----------------------------------------------------------------------------------------------------------------
def esc(text, limit=None) -> str:
    """Plain text safe for MDX tables and paragraphs."""
    if text is None:
        return ""
    s = str(text).replace("\r", " ").replace("\n", " ").replace("\t", " ")
    s = re.sub(r"\s{2,}", " ", s).strip()
    s = IPV4.sub("x.x.x.x", s)
    if limit and len(s) > limit:
        s = s[: limit - 1].rstrip() + "…"
    s = s.replace("\\", "\\\\")
    for a, b in (("&", "&amp;"), ("<", "&lt;"), (">", "&gt;"), ("{", "\\{"), ("}", "\\}"),
                 ("|", "\\|"), ("*", "\\*"), ("`", "\\`"), ("[", "\\["), ("]", "\\]"), ("_", "\\_")):
        s = s.replace(a, b)
    return s


def code(text, limit=None) -> str:
    """Inline code span, safe inside a GFM table cell."""
    if text is None or text == "":
        return ""
    s = str(text).replace("\r", "").replace("\n", " ").replace("\t", " ")
    s = IPV4.sub("x.x.x.x", s)
    if limit and len(s) > limit:
        s = s[: limit - 1].rstrip() + "…"
    s = s.replace("|", "\\|")
    if "`" in s:
        return "`` " + s + " ``"
    return "`" + s + "`"


def block(text, lang="") -> str:
    s = IPV4.sub("x.x.x.x", str(text).replace("\r\n", "\n").replace("\r", "\n"))
    fence = "````" if "```" in s else "```"
    return f"{fence}{lang}\n{s}\n{fence}\n"


def table(headers, rows) -> str:
    if not rows:
        return "_None._\n"
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(("" if c is None else str(c)) for c in r) + " |")
    return "\n".join(out) + "\n"


def details(summary, body) -> str:
    return f"<details>\n<summary>{esc(summary)}</summary>\n\n{body}\n</details>\n"


def front(title, label=None, description=None, position=None, slug=None) -> str:
    def q(s):
        return json.dumps(str(s), ensure_ascii=False)
    lines = ["---", f"title: {q(title)}"]
    if label:
        lines.append(f"sidebar_label: {q(label)}")
    if position is not None:
        lines.append(f"sidebar_position: {position}")
    if description:
        lines.append(f"description: {q(IPV4.sub('x.x.x.x', description)[:300])}")
    if slug:
        lines.append(f"slug: {q(slug)}")
    lines.append("generated: true")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def slugify(s) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", str(s)).strip("-").lower()
    s = s or "x"
    if s[0].isdigit():
        s = "type-" + s
    return s


def category(path: Path, label, position, link_doc=None, collapsed=True, description=None, slug=None):
    cat = {"label": label, "position": position, "collapsed": collapsed}
    if link_doc:
        cat["link"] = {"type": "doc", "id": link_doc}
    elif description:
        cat["link"] = {"type": "generated-index", "description": description}
        if slug:
            cat["link"]["slug"] = slug
    path.mkdir(parents=True, exist_ok=True)
    (path / "_category_.json").write_text(json.dumps(cat, indent=2) + "\n", encoding="utf-8")


# ----------------------------------------------------------------------------------------------------------------
# Loading
# ----------------------------------------------------------------------------------------------------------------
def load_json(p: Path):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def resource_files(folder: Path):
    """The tag files a tag resource folder actually uses (unary-resource.json 'files'); stale extras are ignored."""
    ur = folder / "unary-resource.json"
    if ur.exists():
        try:
            files = load_json(ur).get("files") or []
            return [folder / f for f in files if (folder / f).exists()]
        except Exception:
            pass
    return [folder / f for f in ("tags.json", "udts.json") if (folder / f).exists()]


class Types:
    """UDT definitions: key 'Folder/Sub/Name' -> definition dict (+ file)."""

    def __init__(self, root: Path, repo: Path):
        self.root = root
        self.repo = repo
        self.defs: "OrderedDict[str, dict]" = OrderedDict()
        self.file: dict[str, str] = {}
        self.folder: dict[str, str] = {}
        if not root.exists():
            return
        for dp, dn, fn in sorted(os.walk(root)):
            dn.sort()
            d = Path(dp)
            for f in resource_files(d):
                if f.name != "udts.json":
                    continue
                rel = d.relative_to(root).as_posix()
                rel = "" if rel == "." else rel
                for u in load_json(f):
                    if u.get("tagType") != "UdtType":
                        continue
                    key = (rel + "/" if rel else "") + u["name"]
                    self.defs[key] = u
                    self.file[key] = f.relative_to(repo).as_posix()
                    self.folder[key] = rel or "(root)"

    def get(self, key):
        return self.defs.get(key)

    def chain(self, key):
        """[key, parent, grandparent ...]"""
        out, seen = [], set()
        while key and key in self.defs and key not in seen:
            out.append(key)
            seen.add(key)
            key = self.defs[key].get("typeId")
        return out

    def params(self, key):
        """Effective parameter defaults (parent first)."""
        out = OrderedDict()
        for k in reversed(self.chain(key)):
            for n, p in (self.defs[k].get("parameters") or {}).items():
                out[n] = p
        return out

    def members(self, key):
        """Effective top-level members (parent first, child overrides by name) with their origin type."""
        out = OrderedDict()
        for k in reversed(self.chain(key)):
            for m in self.defs[k].get("tags") or []:
                out[m["name"]] = (m, k)
        return out


def walk_members(tags, prefix=""):
    for t in tags or []:
        path = prefix + t["name"]
        yield path, t
        if t.get("tagType") == "Folder":
            yield from walk_members(t.get("tags"), path + "/")


def binding_text(v):
    if isinstance(v, dict):
        if "binding" in v:
            return v["binding"]
        if "value" in v and isinstance(v.get("value"), str):
            return v["value"]
        return json.dumps(v, ensure_ascii=False)
    return v


def substitute(s, env):
    if not isinstance(s, str):
        return s

    def rep(m):
        k = m.group(1)
        if k in env and env[k] not in (None,):
            return str(env[k])
        return m.group(0)
    return re.sub(r"\{([A-Za-z0-9_]+)\}", rep, s)


def param_value(p):
    """A parameter entry -> its raw value or binding text."""
    if isinstance(p, dict):
        v = p.get("value")
        if isinstance(v, dict):
            return binding_text(v)
        return v
    return p


# ----------------------------------------------------------------------------------------------------------------
# Instance tree (tag-definition)
# ----------------------------------------------------------------------------------------------------------------
class Node:
    __slots__ = ("path", "data", "file")

    def __init__(self, path, data, file):
        self.path, self.data, self.file = path, data, file


def load_provider(root: Path, repo: Path, skip_top=()):
    """All nodes of a provider tree: list of Node (path like 'Boars_Head/GrovePort/...')."""
    nodes: "OrderedDict[str, Node]" = OrderedDict()
    if not root.exists():
        return nodes
    for dp, dn, fn in os.walk(root):
        dn.sort()
        d = Path(dp)
        rel = d.relative_to(root).as_posix()
        rel = "" if rel == "." else urllib.parse.unquote(rel)
        top = rel.split("/")[0] if rel else ""
        if top in skip_top:
            dn[:] = []
            continue
        for f in resource_files(d):
            try:
                data = load_json(f)
            except Exception:
                continue
            frel = f.relative_to(repo).as_posix()

            def walk(ts, prefix):
                for t in ts or []:
                    p = (prefix + "/" if prefix else "") + t["name"]
                    nodes[p] = Node(p, t, frel)
                    if t.get("tagType") == "Folder":
                        walk(t.get("tags"), p)
            walk(data if isinstance(data, list) else [], rel)
    return nodes


# ----------------------------------------------------------------------------------------------------------------
# Rendering helpers for members
# ----------------------------------------------------------------------------------------------------------------
def source_of(t):
    vs = t.get("valueSource")
    tt = t.get("tagType")
    if tt == "UdtInstance":
        return "UDT", t.get("typeId") or ""
    if tt == "Folder":
        return "folder", ""
    if vs == "opc":
        return "opc", binding_text(t.get("opcItemPath")) or ""
    if vs == "expr":
        return "expr", binding_text(t.get("expression")) or ""
    if vs == "reference":
        return "reference", binding_text(t.get("sourceTagPath")) or ""
    if vs == "memory":
        return "memory", ""
    if vs == "derived":
        return "derived", binding_text(t.get("sourceTagPath")) or ""
    if vs == "query":
        return "query", binding_text(t.get("query")) or ""
    return (vs or ""), ""


def short_opc(s):
    s = str(s)
    for pre in ("ns=1;s=[{DeviceName}]", "ns=1;s=[{PlcDevice}]"):
        if s.startswith(pre):
            return s[len(pre):]
    return s


def history_of(t):
    if not t.get("historyEnabled"):
        return ""
    parts = [t.get("historyProvider") or "?", t.get("sampleMode") or ""]
    if t.get("sampleMode") == "Periodic" and t.get("historySampleRate"):
        parts.append(f"{t.get('historySampleRate')} {t.get('historySampleRateUnits') or ''}".strip())
    if "historicalDeadband" in t:
        parts.append(f"db {t.get('historicalDeadband')} {t.get('historicalDeadbandMode') or ''}"
                     f" ({t.get('historicalDeadbandStyle') or 'Auto'})")
    return ", ".join(p for p in parts if p)


def units_of(t):
    bits = []
    eu = t.get("engUnit")
    if eu:
        bits.append(binding_text(eu))
    fs = t.get("formatString")
    if fs:
        bits.append("fmt " + str(fs))
    return " ".join(str(b) for b in bits)


def doc_of(t):
    d = t.get("documentation") or ""
    md = t.get("metadata") or {}
    if isinstance(md, dict) and not d:
        d = md.get("longDescription") or md.get("shortDescription") or ""
    return d


def alarm_enabled_text(a):
    e = a.get("enabled", True)
    if isinstance(e, dict):
        return e.get("value") or e.get("binding") or json.dumps(e)
    return "true" if e in (True, None) else str(e)


def safe_value(name, v, limit=60):
    if v is None:
        return ""
    if SECRET_NAME.search(name or ""):
        return "(hidden)"
    if isinstance(v, (bool, int, float)):
        return str(v)
    if isinstance(v, str):
        if len(v) > limit:
            return f"(text, {len(v)} chars)"
        return v
    if isinstance(v, (dict, list)):
        return f"(document, {len(json.dumps(v))} chars)"
    return ""


# ----------------------------------------------------------------------------------------------------------------
# Reference tool
# ----------------------------------------------------------------------------------------------------------------
class Gen:
    def __init__(self, repo: Path):
        self.repo = repo
        self.ign = repo / IGN
        self.out = repo / "wiki" / "docs" / "tags" / "reference"
        self.types = Types(self.ign / "tag-type-definition" / "default", repo)
        self.system_types = Types(self.ign / "tag-type-definition" / "System", repo)
        self.tags = load_provider(self.ign / "tag-definition" / "default", repo, skip_top=("_RCP1_",))
        self.rcp1_root = self.ign / "tag-definition" / "default" / "_RCP1_"
        self.page_of_type: dict[str, str] = {}      # type key -> reference-relative md path
        self.page_of_group: dict[str, str] = {}     # instance folder -> reference-relative md path
        self.warnings: list[str] = []
        self.counts = Counter()
        self._git_ignored = None
        self._corpus = None

    # ---------------- generic helpers ----------------
    def link_type(self, key, from_dir: str):
        p = self.page_of_type.get(key)
        if not p:
            return code(key)
        return f"[{esc(key)}]({os.path.relpath(p, from_dir).replace(os.sep, '/')})"

    def link_group(self, folder, from_dir: str, label=None):
        p = self.page_of_group.get(folder)
        if not p:
            return code(label or folder)
        return f"[{esc(label or folder)}]({os.path.relpath(p, from_dir).replace(os.sep, '/')})"

    def git_ignored(self, rel_paths):
        """repo-relative paths -> set of the ones .gitignore ignores (None if git is unavailable)."""
        try:
            inp = "\n".join(rel_paths) + "\n"
            r = subprocess.run(["git", "-C", str(self.repo), "check-ignore", "--no-index", "--stdin"],
                               input=inp.encode("utf-8"), capture_output=True, timeout=60)
            if r.returncode not in (0, 1):
                return None
            return set(x.strip() for x in r.stdout.decode("utf-8", "replace").splitlines() if x.strip())
        except Exception:
            return None

    def corpus(self):
        """(label, text) of project resources and tag files, for 'read by' lookups."""
        if self._corpus is not None:
            return self._corpus
        out = []
        proj = self.repo / PROJ
        views = proj / "com.inductiveautomation.perspective" / "views"
        if views.exists():
            for p in sorted(views.rglob("view.json")):
                out.append(("view " + p.parent.relative_to(views).as_posix(), p.read_text(encoding="utf-8", errors="replace")))
        persp = proj / "com.inductiveautomation.perspective"
        for sub, label in (("page-config", "page-config"), ("session-props", "session props"),
                           ("session-permissions", "session permissions")):
            for p in sorted((persp / sub).glob("*.json")) if (persp / sub).exists() else []:
                if p.name != "resource.json":
                    out.append((label, p.read_text(encoding="utf-8", errors="replace")))
        webdev = proj / "com.inductiveautomation.webdev" / "resources"
        if webdev.exists():
            for p in sorted(webdev.rglob("*.py")):
                out.append(("webdev " + p.parent.relative_to(webdev).as_posix(),
                            p.read_text(encoding="utf-8", errors="replace")))
        ign = proj / "ignition"
        if ign.exists():
            for p in sorted(ign.rglob("*")):
                if not p.is_file() or p.suffix not in (".py", ".json") or p.name == "resource.json":
                    continue
                rel = p.parent.relative_to(ign).as_posix()
                if rel.startswith("script-python/"):
                    label = "script " + rel[len("script-python/"):].replace("/", ".")
                else:
                    label = rel.replace("/", " ")
                text = p.read_text(encoding="utf-8", errors="replace")
                if p.name == "resource.json":
                    continue
                out.append((label, text))
            # gateway event resources list their trigger paths in resource.json
            for p in sorted((ign / "tag-change").glob("*/resource.json")) if (ign / "tag-change").exists() else []:
                out.append(("tag-change " + p.parent.name + " (trigger)", p.read_text(encoding="utf-8", errors="replace")))
        ttd = self.ign / "tag-type-definition" / "default"
        for key, u in self.types.defs.items():
            out.append(("UDT " + key, json.dumps(u, ensure_ascii=False)))
        self._corpus = out
        return out

    def read_by(self, tagpath):
        """Resources whose text mentions tagpath (path under the provider, e.g. '_Config/Navigation')."""
        hits = []
        pat = re.compile(re.escape(tagpath) + r"(?![A-Za-z0-9_])")
        for label, text in self.corpus():
            if label not in hits and tagpath in text and pat.search(text):
                hits.append(label)
        return hits

    # ---------------- run ----------------
    def run(self):
        self.clean_out()
        self.load_rcp1()
        self.plan_pages()
        self.collect_usage()
        category(self.out, "Reference (Generated)", 90, link_doc="tags/reference/index")
        self.write_udt_pages()
        self.write_device_pages()
        self.write_tag_groups()
        self.write_config_tags()
        self.write_rcp1()
        self.write_alarm_index()
        self.write_history_index()
        self.write_other_tags()
        self.write_index()
        return self.counts

    def clean_out(self):
        """Remove the previous generated pages (files only; folders are reused, a locked folder is no problem)."""
        if self.out.exists():
            for p in sorted(self.out.rglob("*"), reverse=True):
                try:
                    if p.is_file() and (p.suffix in (".md", ".mdx") or p.name == "_category_.json"):
                        p.unlink()
                    elif p.is_dir() and not any(p.iterdir()):
                        p.rmdir()
                except OSError:
                    pass
        self.out.mkdir(parents=True, exist_ok=True)

    # ---------------- _RCP1_ mirror ----------------
    def load_rcp1(self):
        self.rcp1_items: list[str] = []          # sorted opcItemPaths
        self.rcp1_stats = Counter()
        self.rcp1_by = defaultdict(Counter)
        self.rcp1_objects = Counter()            # top object (Controller:Global/<obj> or Program:x) -> tags
        self.rcp1_present = self.rcp1_root.exists()
        if not self.rcp1_present:
            return
        items = []
        for dp, dn, fn in os.walk(self.rcp1_root):
            d = Path(dp)
            rel = urllib.parse.unquote(d.relative_to(self.rcp1_root).as_posix())
            for f in resource_files(d):
                try:
                    data = load_json(f)
                except Exception:
                    continue

                def walk(ts, prefix):
                    for t in ts or []:
                        p = (prefix + "/" if prefix else "") + t["name"]
                        if t.get("tagType") == "Folder":
                            walk(t.get("tags"), p)
                            continue
                        if t.get("tagType") != "AtomicTag":
                            continue
                        self.rcp1_stats["tags"] += 1
                        self.rcp1_by["dataType"][t.get("dataType") or "?"] += 1
                        self.rcp1_by["tagGroup"][t.get("tagGroup") or "Default"] += 1
                        self.rcp1_by["readOnly"]["read only" if t.get("readOnly") else "WRITABLE"] += 1
                        self.rcp1_by["valueSource"][t.get("valueSource") or "?"] += 1
                        if "value" in t:
                            self.rcp1_stats["value_keys"] += 1
                        parts = p.split("/")
                        top = parts[0]
                        if top == "Controller:Global" and len(parts) > 1:
                            obj = parts[1]
                        else:
                            obj = top
                        self.rcp1_by["top"][top] += 1
                        self.rcp1_objects[(top, obj)] += 1
                        op = t.get("opcItemPath")
                        if isinstance(op, str):
                            items.append(op)
                walk(data if isinstance(data, list) else [], rel)
        self.rcp1_items = sorted(items)

    def rcp1_count(self, device, prefix):
        if not self.rcp1_present or not device or not prefix or "{" in str(prefix):
            return None
        base = f"ns=1;s=[{device}]{prefix}"
        n = 0
        i = bisect.bisect_left(self.rcp1_items, base)
        while i < len(self.rcp1_items):
            s = self.rcp1_items[i]
            if s == base or s.startswith(base + ".") or s.startswith(base + "["):
                n += 1
                i += 1
            elif s.startswith(base):
                i += 1
            else:
                break
        return n

    # ---------------- page plan ----------------
    def plan_pages(self):
        used = set()
        for key in self.types.defs:
            folder = self.types.folder[key]
            fslug = slugify(folder.replace("/", "-")) if folder != "(root)" else "root"
            name = key.rsplit("/", 1)[-1]
            s = slugify(name)
            p = f"udts/{fslug}/{s}.md"
            k = 2
            while p in used:
                p = f"udts/{fslug}/{s}-{k}.md"
                k += 1
            used.add(p)
            self.page_of_type[key] = p
        # device groups = parent folders of UDT instances under Boars_Head
        self.groups: "OrderedDict[str, list]" = OrderedDict()
        for path, node in self.tags.items():
            if not path.startswith("Boars_Head/"):
                continue
            if node.data.get("tagType") != "UdtInstance":
                continue
            parent = path.rsplit("/", 1)[0]
            if self._inside_instance(path):     # overrides inside another instance
                continue
            self.groups.setdefault(parent, []).append(node)
        for g in self.groups:
            rel = g.split("/", 2)[2] if g.count("/") >= 2 else g
            self.page_of_group[g] = f"devices/{slugify(rel)}.md"

    def _inside_instance(self, path):
        parts = path.split("/")
        for i in range(1, len(parts)):
            anc = "/".join(parts[:i])
            n = self.tags.get(anc)
            if n is not None and n.data.get("tagType") == "UdtInstance":
                return True
        return False

    # ---------------- usage ----------------
    def collect_usage(self):
        self.nested_in = defaultdict(list)       # type -> [(container type, member path)]
        self.children_of = defaultdict(list)     # type -> [child types that inherit it]
        for key, u in self.types.defs.items():
            if u.get("typeId"):
                self.children_of[u["typeId"]].append(key)
            for path, t in walk_members(u.get("tags")):
                if t.get("tagType") == "UdtInstance" and t.get("typeId"):
                    self.nested_in[t["typeId"]].append((key, path))
        self.instances_of = defaultdict(list)    # type -> [instance path]
        for path, node in self.tags.items():
            if node.data.get("tagType") == "UdtInstance" and node.data.get("typeId") and not self._inside_instance(path):
                self.instances_of[node.data["typeId"]].append(path)
        # transitive: instances that contain this type somewhere (through nesting)
        self.contained_count = Counter()
        memo = {}

        def containers(t, seen=()):
            if t in memo:
                return memo[t]
            out = set([t])
            for (c, _) in self.nested_in.get(t, []):
                if c not in seen:
                    out |= containers(c, seen + (t,))
            for ch in self.children_of.get(t, []):
                if ch not in seen:
                    out |= containers(ch, seen + (t,))
            memo[t] = out
            return out
        self.containers = {t: containers(t) for t in self.types.defs}

    # ---------------- UDT pages ----------------
    def write_udt_pages(self):
        folders = OrderedDict()
        for key in self.types.defs:
            folders.setdefault(self.types.folder[key], []).append(key)
        udir = self.out / "udts"
        category(udir, "UDT Definitions", 1, link_doc="tags/reference/udts/index")
        pos = 0
        for folder, keys in folders.items():
            pos += 1
            fslug = slugify(folder.replace("/", "-")) if folder != "(root)" else "root"
            category(udir / fslug, folder, pos, collapsed=True,
                     description=f"Generated pages for the {len(keys)} UDT definitions in the `{folder}` folder "
                                 f"of the default tag provider (Tag Browser > default > Data Types > {folder}).",
                     slug=f"/tags/reference/udts/{fslug}")
            for key in keys:
                self.write_udt(key)
        # index
        lines = [front("UDT Definitions (Generated)", "All UDT Definitions",
                       "Every UDT definition in the default tag provider, grouped by folder, with member, alarm, "
                       "history and instance counts."), BANNER,
                 "Every UDT (User Defined Type) definition in the `default` tag provider. In the Designer they are "
                 "under **Tag Browser > default > Data Types**; on disk under "
                 f"`{IGN}/tag-type-definition/default/<folder>/udts.json`.\n\n"
                 "The hand-written guides explain the design: see [UDTs](../../udts/index.md).\n"]
        for folder, keys in folders.items():
            lines.append(f"\n## {esc(folder)}\n")
            rows = []
            for key in keys:
                u = self.types.defs[key]
                mem = list(walk_members(u.get("tags")))
                atom = sum(1 for _, t in mem if t.get("tagType") == "AtomicTag")
                nested = sum(1 for _, t in mem if t.get("tagType") == "UdtInstance")
                alarms = sum(len(t.get("alarms") or []) for _, t in mem)
                hist = sum(1 for _, t in mem if t.get("historyEnabled"))
                inst = len(self.instances_of.get(key, []))
                status = self.type_status(key)
                rows.append([self.link_type(key, "udts"), esc((u.get("metadata") or {}).get("shortDescription")
                                                             or u.get("documentation") or "", 90),
                             atom, nested, alarms, hist, inst, esc(status)])
            lines.append(table(["UDT", "Description", "Atomic", "Nested UDTs", "Alarms", "Historized",
                                "Direct instances", "Status"], rows))
        (udir / "index.md").write_text("".join(lines), encoding="utf-8")

    def type_status(self, key):
        cont = self.containers.get(key, {key})
        n_inst = sum(len(self.instances_of.get(c, [])) for c in cont)
        if n_inst:
            return "in use"
        if key.startswith("PLC/") and key.count("/") == 1:
            return "unused (raw L5K import)"
        return "no instances"

    def write_udt(self, key):
        u = self.types.defs[key]
        page = self.page_of_type[key]
        pdir = os.path.dirname(page)
        name = key.rsplit("/", 1)[-1]
        md = u.get("metadata") or {}
        desc = md.get("shortDescription") or u.get("documentation") or ""
        long = md.get("longDescription") or ""
        out = [front(key, name, f"UDT definition {key}: {desc}" if desc else f"UDT definition {key}"), BANNER]
        out.append(f"# UDT `{key}`\n\n")
        if desc or long:
            out.append(esc(desc) + ("\n\n" + esc(long) if long and long != desc else "") + "\n\n")
        if u.get("documentation") and u.get("documentation") not in (desc, long):
            out.append(esc(u["documentation"]) + "\n\n")
        mem = list(walk_members(u.get("tags")))
        chain = self.types.chain(key)
        status = self.type_status(key)
        summary = [
            ["Designer location", esc("Tag Browser > default > Data Types > " + key.replace("/", " > "))],
            ["Tag path", code("[default]_types_/" + key)],
            ["File", code(self.types.file[key])],
            ["Inherits from", " > ".join(self.link_type(k, pdir) for k in chain[1:]) or "-"],
            ["Inherited by", ", ".join(self.link_type(k, pdir) for k in self.children_of.get(key, [])) or "-"],
            ["Own members", f"{len(mem)} ({sum(1 for _, t in mem if t.get('tagType') == 'AtomicTag')} atomic, "
                            f"{sum(1 for _, t in mem if t.get('tagType') == 'UdtInstance')} nested UDT, "
                            f"{sum(1 for _, t in mem if t.get('tagType') == 'Folder')} folders)"],
            ["Status", esc(status)],
        ]
        out.append(table(["", ""], summary) + "\n")
        self.counts["udt_pages"] += 1

        # parameters
        params = self.types.params(key)
        out.append("## Parameters\n\n")
        if params:
            rows = []
            own = u.get("parameters") or {}
            for n, p in params.items():
                rows.append([code(n), esc(p.get("dataType") if isinstance(p, dict) else ""),
                             code(safe_value(n, param_value(p))) or "-",
                             "own" if n in own else "inherited"])
            out.append(table(["Parameter", "Data type", "Default", "Defined"], rows))
            out.append("\nParameters are referenced in member settings as `{Name}` and are set per instance "
                       "(Designer: right-click the instance > Edit Tag > Parameters).\n\n")
        else:
            out.append("_No parameters._\n\n")

        # OPC pattern
        opc = [binding_text(t.get("opcItemPath")) for _, t in mem if t.get("valueSource") == "opc"]
        if opc:
            pref = os.path.commonprefix([str(o) for o in opc])
            uni = ""
            if "{TagPrefix}" in pref:
                uni = pref.split("{TagPrefix}")[0] + "{TagPrefix}.<member>"
            out.append("## OPC Item Path\n\n")
            out.append(f"{len(opc)} members read OPC through the server `"
                       f"{esc(next((t.get('opcServer') for _, t in mem if t.get('opcServer')), 'Ignition OPC UA Server'))}`. ")
            if uni:
                out.append(f"Pattern: {code(uni)}, so an instance with `DeviceName = RCP1` and "
                           f"`TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part "
                           f"after `[{{DeviceName}}]`.\n\n")
            else:
                out.append(f"Common prefix: {code(pref)}. The Source column shows the part after the device.\n\n")

        # inheritance / nesting diagram
        nested = [(p, t) for p, t in mem if t.get("tagType") == "UdtInstance"]
        if chain[1:] or nested or self.children_of.get(key):
            out.append("## Structure\n\n```mermaid\nflowchart LR\n")
            ids = {}

            def nid(k):
                if k not in ids:
                    ids[k] = f"n{len(ids)}"
                return ids[k]
            me = nid(key)
            out.append(f'  {me}["{key}"]\n  style {me} stroke-width:3px\n')
            for a, b in zip(chain, chain[1:]):
                out.append(f'  {nid(a)}["{a}"] -- inherits --> {nid(b)}["{b}"]\n')
            for ch in self.children_of.get(key, [])[:12]:
                out.append(f'  {nid(ch)}["{ch}"] -- inherits --> {me}\n')
            seen = set()
            for p, t in nested[:30]:
                tid = t.get("typeId") or "?"
                lbl = p.replace('"', "'")
                out.append(f'  {me} -- "{lbl}" --> {nid(tid + "#" + p)}["{tid}"]\n')
            out.append("```\n\n")

        # members
        out.append("## Members\n\n")
        inh = []
        for k in chain[1:]:
            pm = [p for p, t in walk_members(self.types.defs[k].get("tags"))]
            inh.append(f"{len(pm)} from {self.link_type(k, pdir)}")
        if inh:
            out.append("Inherited members (listed on the parent page): " + ", ".join(inh) + ".\n\n")
        rows, longexpr, states = [], [], []
        for p, t in mem:
            kind, src = source_of(t)
            tt = t.get("tagType")
            if tt == "Folder":
                rows.append([code(p + "/"), "Folder", "", "", "", "", "", "", ""])
                continue
            if tt == "UdtInstance":
                rows.append([code(p), "UDT", "nested " + self.link_type(t.get("typeId"), pdir), "", "",
                             "", "", "", esc(doc_of(t), 160)])
                continue
            if kind == "opc":
                srcs = "OPC " + code(short_opc(src), 90)
            elif kind in ("expr", "reference", "derived", "query"):
                if len(str(src)) > 90:
                    longexpr.append((p, kind, src))
                    srcs = kind + " " + code(str(src), 70) + " (full below)"
                else:
                    srcs = kind + " " + code(src)
            elif kind == "memory":
                v = safe_value(p, t.get("value"))
                srcs = "memory" + (" = " + code(v) if v not in ("", None) else "")
            else:
                srcs = esc(kind)
            ro = "yes" if t.get("readOnly") else ""
            al = len(t.get("alarms") or [])
            md2 = t.get("metadata") or {}
            if isinstance(md2, dict) and isinstance(md2.get("states"), list) and md2["states"]:
                states.append((p, md2["states"]))
            rows.append([code(p), esc(t.get("dataType") or ""), srcs, esc(t.get("tagGroup") or ""), ro,
                         esc(history_of(t)), esc(units_of(t)), str(al) if al else "", esc(doc_of(t), 160)])
        out.append(table(["Member", "Data type", "Source", "Tag group", "Read only", "History", "Units / format",
                          "Alarms", "Documentation"], rows))
        if longexpr:
            body = "".join(f"**{code(p)}** ({kind})\n\n" + block(src, "") + "\n" for p, kind, src in longexpr)
            out.append("\n" + details(f"Full expressions / references ({len(longexpr)})", body))
        if states:
            body = table(["Member", "States (value = label)"],
                         [[code(p), esc(", ".join(f"{s.get('value')} = {s.get('label')}" for s in st
                                                 if isinstance(s, dict)), 400)] for p, st in states])
            out.append("\n" + details(f"State labels ({len(states)} members)", body))

        # nested parts
        if nested:
            out.append("\n## Nested UDTs\n\n")
            rows = []
            for p, t in nested:
                pb = []
                for n, pv in (t.get("parameters") or {}).items():
                    pb.append(f"{n} = {binding_text(pv.get('value') if isinstance(pv, dict) else pv)}")
                en = t.get("enabled", True)
                rows.append([code(p), self.link_type(t.get("typeId"), pdir), code("; ".join(pb), 160) or "-",
                             "enabled" if en in (True, None) else ("disabled" if en is False else code(binding_text(en)))])
            out.append(table(["Member", "Type", "Parameter bindings", "Default state"], rows))
            out.append("\n`disabled` parts subscribe nothing until an instance enables them (instance override "
                       "`enabled: true`). See the device instance pages for which instances enable which part.\n")

        # alarms
        al_rows = []
        for p, t in mem:
            for a in t.get("alarms") or []:
                al_rows.append([code(p), esc(a.get("name")), esc(a.get("priority")), esc(a.get("mode")),
                                code(alarm_enabled_text(a), 80), esc(binding_text(a.get("displayPath")) or ""),
                                esc(a.get("notes"), 100)])
        out.append("\n## Alarms\n\n")
        if al_rows:
            out.append(table(["Member", "Alarm", "Priority", "Mode", "Enabled", "Display path", "Notes"], al_rows))
            out.append("\nAssociated data `Site` / `Area` / `Device` come from the tag path "
                       "(`split({PathToTag}, '/')` segments 1 / 2 / 4). Alarms are defined only here, on the UDT, "
                       "never on instances: see [Alarms](../../../alarms.md).\n")
        else:
            out.append("_No alarms defined on this type._\n")

        # used by
        out.append("\n## Used By\n\n")
        ni = self.nested_in.get(key, [])
        if ni:
            out.append("Nested in: " + ", ".join(f"{self.link_type(c, pdir)} (as {code(m)})" for c, m in ni) + "\n\n")
        insts = self.instances_of.get(key, [])
        if insts:
            rows = []
            for ip in insts:
                g = ip.rsplit("/", 1)[0]
                rows.append([code("[default]" + ip), self.link_group(g, pdir, g.split("/", 2)[-1])])
            body = table(["Instance", "Instance page"], rows)
            if len(rows) > 15:
                out.append(f"{len(rows)} direct instances.\n\n" + details(f"Show the {len(rows)} instances", body))
            else:
                out.append(f"{len(rows)} direct instance(s):\n\n" + body)
        total = sum(len(self.instances_of.get(c, [])) for c in self.containers.get(key, {key}))
        if not ni and not insts:
            out.append("Not used by any instance or other UDT"
                       + (" (raw L5K import kept for reference)." if status.startswith("unused") else ".") + "\n")
        elif total and not insts:
            out.append(f"Reached through nesting by {total} top-level instance(s).\n")
        (self.out / page).parent.mkdir(parents=True, exist_ok=True)
        (self.out / page).write_text("".join(out), encoding="utf-8")

    # ---------------- device instance pages ----------------
    def resolve(self, type_key, env, overrides, prefix="", parent_enabled=True, depth=0):
        """Rows describing the nested UDTs / PLC atomics / references of one instance."""
        rows = []
        if depth > 6 or type_key not in self.types.defs:
            return rows
        members = self.types.members(type_key)
        ov_index = {o["name"]: o for o in (overrides or []) if isinstance(o, dict) and "name" in o}

        def walk(items, ovs, pre):
            for name, (m, origin) in items:
                path = pre + name
                ov = ovs.get(name, {})
                tt = m.get("tagType")
                if tt == "Folder":
                    sub = OrderedDict((c["name"], (c, origin)) for c in m.get("tags") or [])
                    subov = {o["name"]: o for o in (ov.get("tags") or []) if isinstance(o, dict) and "name" in o}
                    walk(sub.items(), subov, path + "/")
                    continue
                if tt == "UdtInstance":
                    tid = m.get("typeId")
                    nenv = OrderedDict()
                    for n, p in self.types.params(tid).items():
                        nenv[n] = param_value(p)
                    for n, p in (m.get("parameters") or {}).items():
                        nenv[n] = substitute(param_value(p), env)
                    for n, p in (ov.get("parameters") or {}).items():
                        nenv[n] = param_value(p)
                    en = m.get("enabled", True)
                    if "enabled" in ov:
                        en = ov.get("enabled")
                    en = (en is not False) and parent_enabled
                    rows.append({"path": path, "kind": "udt", "type": tid, "env": nenv, "enabled": en})
                    if tid and tid.startswith(("Devices/", "Units/")):
                        rows.extend(self.resolve(tid, nenv, ov.get("tags"), path + "/", en, depth + 1))
                    continue
                if tt == "AtomicTag":
                    kind, src = source_of(m)
                    if "opcItemPath" in ov:
                        kind, src = "opc", binding_text(ov["opcItemPath"])
                    if "sourceTagPath" in ov:
                        kind, src = "reference", binding_text(ov["sourceTagPath"])
                    if kind in ("opc", "reference"):
                        rows.append({"path": path, "kind": kind, "src": substitute(src, env),
                                     "enabled": parent_enabled})
        walk(members.items(), ov_index, prefix)
        return rows

    def write_device_pages(self):
        ddir = self.out / "devices"
        category(ddir, "Device Instances", 2, link_doc="tags/reference/devices/index")
        index_rows = []
        for g, nodes in self.groups.items():
            page = self.page_of_group[g]
            rel = g.split("/", 2)[2] if g.count("/") >= 2 else g
            types = Counter(n.data.get("typeId") for n in nodes)
            title = rel.replace("/", " / ")
            out = [front(f"{title} (Instances)", title,
                         f"Device instances in [default]{g}: types, parameters and the resolved PLC objects."), BANNER]
            out.append(f"# `{g}`\n\n")
            out.append(f"Tag Browser: **default > {esc(g.replace('/', ' > '))}**. File: "
                       f"{code(nodes[0].file)}. {len(nodes)} UDT instance(s): "
                       + ", ".join(f"{c} x {self.link_type(t, 'devices')}" for t, c in types.items()) + ".\n\n")
            for n in nodes:
                d = n.data
                tid = d.get("typeId")
                md = d.get("metadata") or {}
                out.append(f"## {esc(d['name'])}\n\n")
                info = [["Tag path", code("[default]" + n.path)], ["Type", self.link_type(tid, "devices")]]
                if md.get("shortDescription"):
                    info.append(["Label", esc(md.get("shortDescription"))])
                if md.get("longDescription"):
                    info.append(["Description", esc(md.get("longDescription"), 400)])
                if d.get("enabled") is False:
                    info.append(["Enabled", "**false** (Out Of Service or disabled)"])
                out.append(table(["", ""], info) + "\n")
                params = d.get("parameters") or {}
                env = OrderedDict((k, param_value(v)) for k, v in self.types.params(tid).items()) if tid else OrderedDict()
                for k, v in params.items():
                    env[k] = param_value(v)
                if params:
                    out.append(table(["Parameter", "Value"],
                                     [[code(k), code(safe_value(k, param_value(v), 240))] for k, v in params.items()]) + "\n")
                rows = self.resolve(tid, env, d.get("tags")) if tid else []
                prow = []
                for r in rows:
                    if r["kind"] == "udt":
                        e = r["env"]
                        dev = e.get("DeviceName")
                        tp = e.get("TagPrefix")
                        if "TagPrefix" in e or "DeviceName" in e:
                            obj = f"[{dev}]{tp}" if tp else "(no PLC object)"
                            cnt = self.rcp1_count(dev, tp) if tp else None
                            mirror = "" if cnt is None else (f"{cnt} tags" if cnt else "not in mirror")
                            prow.append([code(r["path"]), self.link_type(r["type"], "devices"),
                                         "yes" if r["enabled"] else "no", code(obj) if tp else esc(obj),
                                         esc(mirror)])
                        elif "Source" in e:
                            prow.append([code(r["path"]), self.link_type(r["type"], "devices"),
                                         "yes" if r["enabled"] else "no", "reference to " + code(e.get("Source") or "(empty)"), ""])
                        elif r["type"] and r["type"].startswith("PLC/"):
                            ps = ", ".join(f"{k}={v}" for k, v in e.items() if k not in ("Description",) and v not in (None, ""))
                            prow.append([code(r["path"]), self.link_type(r["type"], "devices"),
                                         "yes" if r["enabled"] else "no", code(ps, 80), ""])
                    elif r["kind"] == "opc":
                        src = str(r["src"])
                        m = re.match(r"ns=1;s=\[([^\]]+)\](.*)", src)
                        cnt = self.rcp1_count(m.group(1), m.group(2)) if m else None
                        prow.append([code(r["path"]), "OPC atomic", "yes" if r["enabled"] else "no", code(src, 90),
                                     "" if cnt is None else (f"{cnt} tags" if cnt else "not in mirror")])
                    elif r["kind"] == "reference":
                        prow.append([code(r["path"]), "reference", "yes" if r["enabled"] else "no",
                                     code(r["src"], 110), ""])
                if prow:
                    out.append(table(["Member", "Part type", "Enabled", "Reads (resolved)", "In `_RCP1_` mirror"],
                                     prow) + "\n")
                    self.counts["parts"] += len(prow)
                self.counts["instances"] += 1
                index_rows.append([code(d["name"]), self.link_type(tid, "devices"),
                                   self.link_group(g, "devices", rel),
                                   esc(", ".join(f"{k}={param_value(v)}" for k, v in params.items()
                                                 if k != "PlcDevice"), 120)])
            (self.out / page).write_text("".join(out), encoding="utf-8")
            self.counts["device_pages"] += 1
        lines = [front("Device Instances (Generated)", "All Device Instances",
                       "Every UDT instance under [default]Boars_Head with its type, parameters and page."), BANNER,
                 "Every UDT instance in the device tree `[default]Boars_Head/<Site>/<Area>/<Type>/<Device>`. Each "
                 "page lists the instance parameters and the PLC object every nested part reads once the "
                 "parameters are substituted (`[DeviceName]TagPrefix`). The **In `_RCP1_` mirror** column counts the "
                 "tags of that object in the pruned browse mirror `[default]_RCP1_` (evidence that the object "
                 "exists in the controller; empty when the mirror is not on this machine).\n\n"
                 "How the values get there: [PAX Mapping](../../pax-mapping/index.md).\n\n"]
        lines.append(table(["Instance", "Type", "Folder", "Parameters"], index_rows))
        (ddir / "index.md").write_text("".join(lines), encoding="utf-8")

    # ---------------- tag groups ----------------
    def write_tag_groups(self):
        tg = self.ign / "tag-group"
        rows = []
        use = defaultdict(Counter)
        for key, u in self.types.defs.items():
            for p, t in walk_members(u.get("tags")):
                if t.get("tagType") == "AtomicTag" and t.get("valueSource") == "opc":
                    use[t.get("tagGroup") or "Default"]["UDT OPC members"] += 1
        for path, node in self.tags.items():
            t = node.data
            if t.get("tagType") == "AtomicTag" and t.get("valueSource") == "opc":
                use[t.get("tagGroup") or "Default"]["instance OPC tags"] += 1
        for g, c in self.rcp1_by.get("tagGroup", {}).items():
            use[g]["`_RCP1_` tags"] += c
        ignored = self.git_ignored([f"{IGN}/tag-group/{p.parent.parent.name}/{p.parent.name}/config.json"
                                    for p in tg.glob("*/*/config.json")]) if tg.exists() else None
        for p in sorted(tg.glob("*/*/config.json")) if tg.exists() else []:
            prov, name = p.parent.parent.name, p.parent.name
            cfg = load_json(p).get("config", {})
            relp = f"{IGN}/tag-group/{prov}/{name}/config.json"
            tracked = "?" if ignored is None else ("no" if relp in ignored else "yes")
            u = use.get(name, {}) if prov == "default" else {}
            rows.append([esc(prov), code(name), esc(cfg.get("mode")), esc(cfg.get("rate")), esc(cfg.get("leasedRate", "")),
                         esc(cfg.get("opcDataMode", "")), esc(", ".join(f"{v} {k}" for k, v in u.items())), tracked])
        out = [front("Tag Groups (Generated)", "Tag Groups",
                     "Every tag group with its mode, rates and how many tags use it."), BANNER,
               "Tag groups decide how often OPC tags are polled. **Direct** = always polled at `rate` (ms). "
               "**Leased** = polled at `leasedRate` while something (a view, a binding) subscribes to the tag, "
               "otherwise at `rate` (0 = not at all). Designer: **Tag Browser > (gear) Edit Tag Groups**; Gateway "
               "web UI: **Config > Tags > Tag Groups**; on disk "
               f"`{IGN}/tag-group/<provider>/<group>/config.json`.\n\n"
               "Why the groups are set this way: [History And Polling](../history.md).\n\n"]
        out.append(table(["Provider", "Group", "Mode", "Rate (ms)", "Leased rate (ms)", "OPC data mode",
                          "Used by (OPC tags)", "In git"], rows))
        out.append("\nA member without a `tagGroup` uses the `Default` group.\n")
        (self.out / "tag-groups.md").write_text("".join(out), encoding="utf-8")
        self.counts["tag_groups"] = len(rows)

    # ---------------- _Config ----------------
    def write_config_tags(self):
        cfg = [(p, n) for p, n in self.tags.items() if p == "_Config" or p.startswith("_Config/")]
        folders = sorted(set(n.file.rsplit("/", 1)[0] for _, n in cfg))
        ignored = self.git_ignored([f + "/unary-resource.json" for f in folders])
        rows = []
        for p, n in cfg:
            t = n.data
            if t.get("tagType") == "Folder":
                continue
            folder = n.file.rsplit("/", 1)[0]
            tracked = "?" if ignored is None else ("no" if folder + "/unary-resource.json" in ignored else "yes")
            kind = t.get("tagType")
            if kind == "UdtInstance":
                dtype = "UDT " + (t.get("typeId") or "")
            else:
                dtype = t.get("dataType") or ""
            vs = t.get("valueSource") or ("instance" if kind == "UdtInstance" else "")
            extra = ""
            if vs == "expr":
                extra = " " + code(binding_text(t.get("expression")), 80)
            if vs == "reference":
                extra = " " + code(binding_text(t.get("sourceTagPath")), 80)
            hits = self.read_by(p)
            rb = ", ".join(code(h) for h in hits[:8]) + (f" +{len(hits) - 8} more" if len(hits) > 8 else "")
            rows.append([code("[default]" + p), esc(dtype), esc(vs) + extra, esc(doc_of(t), 220), rb or "-", tracked])
        out = [front("_Config Tags (Generated)", "_Config Tags",
                     "Every tag under [default]_Config with its type, documentation and the resources that read it."),
               BANNER,
               "Every tag under `[default]_Config` (configuration tags the HMI reads at runtime). **Values are not "
               "shown on purpose** (some hold credentials); read them in the Designer Tag Browser. **Read by** lists "
               "the project resources whose source mentions the full tag path (views, project scripts, gateway "
               "events, UDTs); scripts that build a path at runtime (for example `shared.Enums` with "
               "`_Config/Enums/` + a name) only show up on the parent folder.\n\n"
               "What each one is for: [_Config Tags](../config-tags.md). **In git** = the folder is whitelisted in "
               "`.gitignore` (untracked folders exist only on this gateway).\n\n"]
        out.append(table(["Tag", "Type", "Value source", "Documentation", "Read by", "In git"], rows))
        (self.out / "config-tags.md").write_text("".join(out), encoding="utf-8")
        self.counts["config_tags"] = len(rows)

    # ---------------- _RCP1_ ----------------
    def write_rcp1(self):
        out = [front("_RCP1_ Mirror (Generated)", "_RCP1_ Mirror",
                     "Counts and objects of the pruned, read-only browse mirror [default]_RCP1_ of the RCP1 PLC."),
               BANNER]
        out.append("`[default]_RCP1_` is a browse of the production controller `[RCP1]`, pruned to the PlantPAx "
                   "members the HMI and FactoryTalk use, with every tag `readOnly`. The HMI reads the PLC through the "
                   "device UDTs, not through this folder (exceptions: the SAFETYS `Digitals` references). It is "
                   "git-ignored, so it exists only on this gateway. Background: [PAX Mapping](../pax-mapping/index.md), "
                   "[PLC Write Lock](../plc-write-lock.md).\n\n")
        if not self.rcp1_present:
            out.append(":::caution\nThe `_RCP1_` folder is not on this machine, so no counts were generated.\n:::\n")
            (self.out / "rcp1-mirror.md").write_text("".join(out), encoding="utf-8")
            return
        st = self.rcp1_stats
        ro = self.rcp1_by["readOnly"]
        out.append(table(["Check", "Result"], [
            ["Atomic tags", st["tags"]],
            ["Read only", f"{ro.get('read only', 0)} of {st['tags']}" + ("" if not ro.get("WRITABLE") else
                                                                         f" (**{ro['WRITABLE']} writable**)")],
            ["Tags carrying a `value` key (must be 0)", st.get("value_keys", 0)],
            ["Distinct OPC items", len(set(self.rcp1_items))],
        ]) + "\n")
        for k, label in (("top", "Top folder"), ("tagGroup", "Tag group"), ("dataType", "Data type"),
                         ("valueSource", "Value source")):
            out.append(f"### By {label.lower()}\n\n")
            out.append(table([label, "Tags"], [[code(a), b] for a, b in self.rcp1_by[k].most_common()]) + "\n")
        # used by
        users = defaultdict(set)
        for g, nodes in self.groups.items():
            for n in nodes:
                tid = n.data.get("typeId")
                if not tid:
                    continue
                env = OrderedDict((k, param_value(v)) for k, v in self.types.params(tid).items())
                for k, v in (n.data.get("parameters") or {}).items():
                    env[k] = param_value(v)
                for r in self.resolve(tid, env, n.data.get("tags")):
                    tp = None
                    if r["kind"] == "udt":
                        tp = r["env"].get("TagPrefix")
                    elif r["kind"] == "opc":
                        m = re.match(r"ns=1;s=\[[^\]]+\](.*)", str(r["src"]))
                        tp = m.group(1) if m else None
                    elif r["kind"] == "reference" and "_RCP1_/" in str(r["src"]):
                        s = str(r["src"]).split("_RCP1_/", 1)[1].split("/")
                        tp = s[1] if s[0] == "Controller:Global" and len(s) > 1 else s[0]
                    if tp and r.get("enabled", True):
                        obj = re.split(r"[\[.]", str(tp))[0]
                        users[obj].add(n.path.split("/", 2)[-1])
        rows = []
        for (top, obj), c in sorted(self.rcp1_objects.items(), key=lambda x: (x[0][0] != "Controller:Global", x[0])):
            us = sorted(users.get(obj, []))
            rows.append([code(top), code(obj), c, esc(", ".join(us[:6]) + (f" +{len(us) - 6}" if len(us) > 6 else ""))])
        out.append("## Objects\n\nOne row per controller object (array or single tag) in the mirror, with the "
                   "device instances whose parts read it.\n\n")
        out.append(table(["Folder", "Object", "Tags", "Read by device instances"], rows))
        (self.out / "rcp1-mirror.md").write_text("".join(out), encoding="utf-8")
        self.counts["rcp1_tags"] = st["tags"]

    # ---------------- alarm index ----------------
    def write_alarm_index(self):
        rows, inst_rows = [], []
        for key, u in self.types.defs.items():
            for p, t in walk_members(u.get("tags")):
                for a in t.get("alarms") or []:
                    rows.append([self.link_type(key, "."), code(p), esc(a.get("name")), esc(a.get("priority")),
                                 esc(a.get("mode")), code(alarm_enabled_text(a), 70), esc(a.get("notes"), 90)])
        for path, node in self.tags.items():
            for a in node.data.get("alarms") or []:
                inst_rows.append([code("[default]" + path), esc(a.get("name")), esc(a.get("priority"))])
        pri = Counter(r[3] for r in rows)
        out = [front("Alarm Index (Generated)", "Alarm Index",
                     "Every Ignition alarm defined on a UDT member, with priority and enable condition."), BANNER,
               "Every Ignition alarm configured in the tag configuration. The rule is that alarms live on UDT "
               "definition members only ([Alarms](../alarms.md)); the second table lists any alarm found on an "
               "instance or plain tag (it should be empty).\n\n",
               f"**{len(rows)} alarm definitions** on UDT members: "
               + ", ".join(f"{c} {esc(k)}" for k, c in pri.most_common()) + ".\n\n"]
        out.append(table(["UDT", "Member", "Alarm", "Priority", "Mode", "Enabled", "Notes"], rows))
        out.append("\n## Alarms On Instances Or Plain Tags\n\n")
        out.append(table(["Tag", "Alarm", "Priority"], inst_rows))
        (self.out / "alarm-index.md").write_text("".join(out), encoding="utf-8")
        self.counts["alarm_defs"] = len(rows)
        if inst_rows:
            self.warnings.append(f"{len(inst_rows)} alarms on instances / plain tags")

    # ---------------- history index ----------------
    def write_history_index(self):
        rows = []
        for key, u in self.types.defs.items():
            for p, t in walk_members(u.get("tags")):
                if t.get("tagType") == "AtomicTag" and t.get("historyEnabled"):
                    n_inst = sum(len(self.instances_of.get(c, [])) for c in self.containers.get(key, {key}))
                    rows.append([self.link_type(key, "."), code(p), esc(t.get("dataType")), esc(t.get("tagGroup") or "Default"),
                                 esc(history_of(t)), n_inst or ""])
        inst = []
        for path, node in self.tags.items():
            t = node.data
            if t.get("tagType") == "AtomicTag" and t.get("historyEnabled"):
                inst.append([code("[default]" + path), esc(t.get("dataType")), esc(history_of(t))])
        out = [front("History Index (Generated)", "History Index",
                     "Every historized UDT member and tag, with provider, sample mode and deadband."), BANNER,
               "Every member with **History Enabled** in a UDT definition (applies to every instance that reaches "
               "it), then tags historized directly in the instance tree. Explained in "
               "[History And Polling](../history.md).\n\n"]
        out.append(f"## On UDT Members ({len(rows)})\n\n")
        out.append("**Instances** = top-level instances that contain the type (through nesting); 0 / empty means the "
                   "type is not used.\n\n")
        out.append(table(["UDT", "Member", "Data type", "Tag group", "History", "Instances"], rows))
        out.append(f"\n## On Instance / Plain Tags ({len(inst)})\n\n")
        out.append(table(["Tag", "Data type", "History"], inst))
        (self.out / "history-index.md").write_text("".join(out), encoding="utf-8")
        self.counts["history_members"] = len(rows)

    # ---------------- other tags ----------------
    def write_other_tags(self):
        tops = Counter()
        for p, n in self.tags.items():
            tops[(p.split("/")[0], n.data.get("tagType"))] += 1
        rows = []
        for path, node in self.tags.items():
            t = node.data
            if not path.startswith("Boars_Head/") or t.get("tagType") != "AtomicTag" or self._inside_instance(path):
                continue
            kind, src = source_of(t)
            rows.append([code("[default]" + path), esc(t.get("dataType")), esc(kind) + (" " + code(src, 70) if src else ""),
                         esc(history_of(t)), esc(doc_of(t), 120)])
        ignored = self.git_ignored(sorted(set(n.file for n in self.tags.values())))
        top_rows = []
        files_by_top = defaultdict(set)
        for n in self.tags.values():
            files_by_top[n.path.split("/")[0]].add(n.file)
        for top in sorted(set(k for k, _ in tops)):
            fs = files_by_top[top]
            tr = "?" if ignored is None else f"{sum(1 for f in fs if f not in ignored)} of {len(fs)} files"
            top_rows.append([code("[default]" + top), tops[(top, "AtomicTag")], tops[(top, "UdtInstance")],
                             tops[(top, "Folder")], tr])
        if self.rcp1_present:
            top_rows.append([code("[default]_RCP1_"), self.rcp1_stats["tags"], 0, "", "no (git-ignored)"])
        out = [front("Tag Tree Inventory (Generated)", "Tag Tree Inventory",
                     "Top-level folders of the default tag provider and the plain tags under Boars_Head."), BANNER,
               "## Top-Level Folders Of `[default]`\n\n",
               table(["Folder", "Atomic tags", "UDT instances", "Folders", "Tracked in git"], top_rows),
               "\nCounts include nested folders; instance members are not counted (they come from the UDT).\n\n",
               f"## Plain (Non-UDT) Tags Under `Boars_Head` ({len(rows)})\n\n",
               "Atomic tags in the device tree that are not part of a UDT instance (for example the Production / FCM "
               "line KPI memory placeholders).\n\n", table(["Tag", "Data type", "Source", "History", "Documentation"], rows)]
        (self.out / "tag-tree.md").write_text("".join(out), encoding="utf-8")

    # ---------------- index ----------------
    def write_index(self):
        c = self.counts
        out = [front("Tag Reference (Generated)", "Overview",
                     "Generated reference of the BH tag configuration: UDTs, instances, tag groups, _Config, _RCP1_."),
               BANNER,
               "These pages are generated from the gateway tag files in the repo "
               f"(`{IGN}/...`). They reflect the project files as of the last wiki update. For explanations start at "
               "[Tags](../index.md).\n\n",
               table(["Page", "What", "Count"], [
                   ["[UDT Definitions](udts/index.md)", "one page per UDT definition", c["udt_pages"]],
                   ["[Device Instances](devices/index.md)", "one page per device folder under `Boars_Head`; "
                    "instances / resolved parts", f"{c['device_pages']} pages, {c['instances']} instances, "
                                                  f"{c['parts']} parts"],
                   ["[Tag Groups](tag-groups.md)", "polling groups", c["tag_groups"]],
                   ["[_Config Tags](config-tags.md)", "runtime configuration tags", c["config_tags"]],
                   ["[_RCP1_ Mirror](rcp1-mirror.md)", "pruned PLC browse", c.get("rcp1_tags", 0)],
                   ["[Alarm Index](alarm-index.md)", "alarm definitions on UDT members", c["alarm_defs"]],
                   ["[History Index](history-index.md)", "historized UDT members", c["history_members"]],
                   ["[Tag Tree Inventory](tag-tree.md)", "top-level folders, plain tags", ""],
               ]),
               "\nRegenerate: `python -I wiki/tools/gen_all.py tags` (or all areas without an argument), then "
               "`cd wiki; npm run build`.\n"]
        (self.out / "index.md").write_text("".join(out), encoding="utf-8")


def main(repo_root=None):
    repo = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    g = Gen(repo)
    counts = g.run()
    summary = (f"{counts['udt_pages']} UDTs, {counts['device_pages']} device pages ({counts['instances']} instances, "
               f"{counts['parts']} parts), {counts['tag_groups']} tag groups, {counts['config_tags']} _Config tags, "
               f"{counts.get('rcp1_tags', 0)} _RCP1_ tags, {counts['alarm_defs']} alarms, "
               f"{counts['history_members']} historized members")
    for w in g.warnings:
        print("[warn] " + w)
    return summary


if __name__ == "__main__":
    print(main(sys.argv[1] if len(sys.argv) > 1 else None))
