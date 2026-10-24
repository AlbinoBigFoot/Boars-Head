#!/usr/bin/env python3
"""Generate the Perspective reference pages of the BH wiki (docs/perspective/reference/**).

Reads the BH Perspective project straight from the gateway bind mount and writes one page per view plus
index pages: page-config routes, the nav tree, session properties, common binding patterns, style classes,
the stylesheet section index, themes and icons.

    python -I wiki/tools/gen_perspective.py            # from the repo root (or call main(repo_root))

Stdlib only, UTF-8, idempotent. It rewrites ONLY wiki/docs/perspective/reference/** and
nothing else. Source hashes for check_docs.py are recorded by gen_all.py from SOURCES.
"""
import hashlib
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

PERSP_REL = "gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
SCRIPTS_REL = "gateways/standard/data/projects/BH/ignition/script-python"
NQ_REL = "gateways/standard/data/projects/BH/ignition/named-query"
CORE_REL = "gateways/standard/data/config/resources/core/com.inductiveautomation.perspective"
DOCS_REL = "wiki/docs"
OUT_REL = "wiki/docs/perspective/reference"
HASHES_REL = "wiki/tools/.gen_perspective_sources.json"   # legacy file, removed on each run

# What this reference tool reads; gen_all.py hashes these into wiki/tools/manifest/sources.json for check_docs.py.
SOURCES = [
    PERSP_REL + "/**/*",
    CORE_REL + "/**/*",
    SCRIPTS_REL + "/**/code.py",
]

BANNER = ":::note\nThis reference page is generated from the project files.\n:::\n"
COMMON_MIN_VIEWS = 20      # a binding / handler repeated in this many views is shown once on common-patterns
MAX_EXPR = 3000            # characters of an expression shown before truncating
MAX_SCRIPT_LINES = 40      # lines of a transform / handler shown before truncating
MAX_EVENT_LINES = 25       # lines of an event script shown ("first lines")
MAX_TREE = 250             # component tree lines
DETAILS_OVER = 12          # wrap a list in <details> above this many entries

# --------------------------------------------------------------------------------------------- markdown helpers


def esc(text):
    """Escape plain text for MDX (outside code)."""
    s = str(text)
    s = s.replace("\\", "\\\\")
    for ch in "`*_[]{}|#":
        s = s.replace(ch, "\\" + ch)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace("\n", " ")


def code(text, table=False):
    """Inline code span (safe in MDX; pipes escaped inside tables)."""
    s = str(text).replace("\r", "").replace("\n", " ").strip()
    if not s:
        return "`''`"
    run = max((len(m) for m in re.findall(r"`+", s)), default=0)
    tick = "`" * (run + 1)
    if table:
        s = s.replace("|", "\\|")
    pad = " " if s.startswith("`") or s.endswith("`") else ""
    return tick + pad + s + pad + tick


def fence(text, lang=""):
    s = str(text).replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")
    run = max((len(m) for m in re.findall(r"`{3,}", s)), default=0)
    tick = "`" * max(3, run + 1)
    return "%s%s\n%s\n%s\n" % (tick, lang, s, tick)


def details(summary, body, open_=False):
    return "<details%s>\n<summary>%s</summary>\n\n%s\n\n</details>\n" % (" open" if open_ else "", esc(summary),
                                                                       body.rstrip("\n"))


def maybe_details(summary, body, count):
    if count > DETAILS_OVER:
        return details(summary, body)
    return body


def front(title, description, extra=None):
    lines = ["---", "title: %s" % json.dumps(title), "sidebar_label: %s" % json.dumps(title),
             "description: %s" % json.dumps(description[:300]), "generated: true"]
    for k, v in (extra or {}).items():
        lines.append("%s: %s" % (k, json.dumps(v)))
    lines.append("---")
    return "\n".join(lines) + "\n\n" + BANNER + "\n"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) if c not in (None, "") else " " for c in r) + " |")
    return "\n".join(out) + "\n"


def short_json(v, n=80):
    s = json.dumps(v, ensure_ascii=False, sort_keys=True)
    return s if len(s) <= n else s[: n - 3] + "..."


def clip_lines(text, n):
    lines = str(text).replace("\r\n", "\n").split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    # strip the common tab indent Perspective adds to function bodies
    ind = min((len(l) - len(l.lstrip("\t")) for l in lines if l.strip()), default=0)
    lines = [l[ind:] if l[:ind] == "\t" * ind else l for l in lines]
    while lines and not lines[-1].strip():
        lines.pop()
    more = len(lines) - n
    body = "\n".join(lines[:n]).replace("\t", "    ")
    if more > 0:
        body += "\n# ... %d more line(s): see the view.json" % more
    return body


def clip_expr(text):
    s = str(text).replace("\r\n", "\n")
    if len(s) > MAX_EXPR:
        return s[:MAX_EXPR] + "\n// ... truncated (%d characters in total): see the view.json" % len(s)
    return s


def slug(part):
    s = part.replace("&", "and")
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s or "x"


# --------------------------------------------------------------------------------------------- project model


class View:
    def __init__(self, rel, data, resource):
        self.rel = rel                        # 00_Pages/00_Docked/Header
        self.data = data
        self.resource = resource or {}
        self.name = rel.split("/")[-1]
        self.folder = "/".join(rel.split("/")[:-1])
        self.bindings = []                    # dicts
        self.changes = []                     # property change scripts
        self.events = []
        self.handlers = []                    # message handlers
        self.methods = []                     # custom methods
        self.components = []                  # (depth, path, type, comp)
        self.embeds = []                      # (component path, view path, kind)
        self.dynamic_embeds = []              # component paths whose view path is bound
        self.refs = set()                     # view paths mentioned anywhere (popups, scripts, expressions)
        self.classes = Counter()              # static style classes
        self.bound_classes = set()
        self.tags = set()
        self.members = set()
        self.calls = set()
        self.queries = set()
        self.routes = []
        self.docks = []
        self.embedded_in = set()
        self.referenced_by = set()
        self.nav_items = []
        self.script_refs = set()


def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def iter_components(comp, path, depth=0):
    name = (comp.get("meta") or {}).get("name") or "?"
    here = name if not path else path + "/" + name
    yield depth, here, comp
    for ch in comp.get("children") or []:
        yield from iter_components(ch, here, depth + 1)


TAG_RE = re.compile(r"\[(?:default|System|RCP1|Sim|~)\][^\"'{}\\\n]*")
MEMBER_RE = re.compile(r"\+\s*(?:\\?[\"'])(/[A-Za-z0-9_. /-]{2,80}|\.[A-Za-z][A-Za-z0-9_]{1,60})(?:\\?[\"'])")
STRLIT_RE = re.compile(r"'([^'\\\n]{1,120})'|\"([^\"\\\n]{1,120})\"")


def scan_text_refs(view, text, libs_re):
    for m in TAG_RE.finditer(text):
        t = m.group(0).rstrip(" .,;)")
        if len(t) > 9:
            view.tags.add(t)
    for m in MEMBER_RE.finditer(text):
        view.members.add(m.group(1))
    if libs_re:
        for m in libs_re.finditer(text):
            view.calls.add(m.group(0))


def collect_binding(view, owner, prop, cfg, libs_re, known_classes):
    b = cfg.get("binding")
    if b:
        rec = {"owner": owner, "prop": prop, "type": b.get("type"), "config": b.get("config") or {},
               "transforms": b.get("transforms") or [], "bidirectional": bool((b.get("config") or {}).get(
                   "bidirectional"))}
        view.bindings.append(rec)
        text = json.dumps(b, ensure_ascii=False)
        scan_text_refs(view, text, libs_re)
        if rec["type"] == "tag":
            tp = rec["config"].get("tagPath")
            if tp:
                view.tags.add(str(tp))
        if rec["type"] == "query":
            qp = rec["config"].get("queryPath")
            if qp:
                view.queries.add(qp)
        if prop.endswith("style.classes") or prop.endswith(".classes"):
            for m in STRLIT_RE.finditer(text):
                for tok in (m.group(1) or m.group(2) or "").split():
                    if tok in known_classes:
                        view.bound_classes.add(tok)
    if cfg.get("onChange"):
        oc = cfg["onChange"]
        script = oc.get("script") or ""
        view.changes.append({"owner": owner, "prop": prop, "script": script,
                             "enabled": oc.get("enabled", True)})
        scan_text_refs(view, script, libs_re)


def analyse(view, libs_re, known_classes):
    d = view.data
    for prop, cfg in (d.get("propConfig") or {}).items():
        collect_binding(view, "(view)", prop, cfg, libs_re, known_classes)
    root = d.get("root") or {}
    for depth, path, comp in iter_components(root, ""):
        ctype = comp.get("type", "?")
        view.components.append((depth, path, ctype, comp))
        for prop, cfg in (comp.get("propConfig") or {}).items():
            collect_binding(view, path, prop, cfg, libs_re, known_classes)
        props = comp.get("props") or {}
        style = props.get("style") or {}
        cls = style.get("classes") if isinstance(style, dict) else None
        if isinstance(cls, str):
            for tok in cls.split():
                view.classes[tok] += 1
        if ctype in ("ia.display.view", "ia.display.flex-repeater"):
            pc = comp.get("propConfig") or {}
            p = props.get("path")
            if "props.path" in pc and pc["props.path"].get("binding"):
                view.dynamic_embeds.append(path)
            elif isinstance(p, str) and p:
                view.embeds.append((path, p, "repeater" if ctype.endswith("repeater") else "embed"))
        for etype, evs in (comp.get("events") or {}).items():
            for ename, handlers in (evs or {}).items():
                for h in handlers if isinstance(handlers, list) else [handlers]:
                    if not isinstance(h, dict):
                        continue
                    view.events.append({"owner": path, "event": "%s.%s" % (etype, ename), "type": h.get("type"),
                                        "scope": h.get("scope"), "config": h.get("config") or {},
                                        "enabled": h.get("enabled", True)})
                    scan_text_refs(view, json.dumps(h, ensure_ascii=False), libs_re)
        scripts = comp.get("scripts") or {}
        for mh in scripts.get("messageHandlers") or []:
            view.handlers.append({"owner": path, **mh})
            scan_text_refs(view, mh.get("script") or "", libs_re)
        for cm in scripts.get("customMethods") or []:
            view.methods.append({"owner": path, **cm})
            scan_text_refs(view, cm.get("script") or "", libs_re)


# --------------------------------------------------------------------------------------------- formatting


def binding_body(rec):
    t, c = rec["type"], rec["config"]
    out = []
    if t == "expr":
        out.append(fence(clip_expr(c.get("expression", "")), "js"))
    elif t == "expr-struct":
        lines = []
        for k, v in (c.get("struct") or {}).items():
            lines.append("%s: %s" % (k, str(v).replace("\n", "\n    ")))
        out.append(fence(clip_expr("\n".join(lines)), "js"))
        if "waitOnAll" in c:
            out.append("waitOnAll: %s\n" % code(c.get("waitOnAll")))
    elif t == "property":
        pass
    elif t == "tag":
        refs = c.get("references") or {}
        out.append("Mode %s, tag path %s%s%s\n" % (
            code(c.get("mode", "direct")), code(c.get("tagPath", "")),
            (", references " + ", ".join("%s = %s" % (code(k), code(v)) for k, v in refs.items())) if refs else "",
            (", fallback delay %s s" % c.get("fallbackDelay")) if c.get("fallbackDelay") is not None else ""))
    elif t == "query":
        out.append("Named query %s, return format %s%s\n" % (
            code(c.get("queryPath", "")), code(c.get("returnFormat", "auto")),
            (", polling " + code(short_json(c.get("polling"), 60))) if c.get("polling") else ""))
        params = c.get("parameters") or {}
        if params:
            out.append(fence("\n".join("%s: %s" % (k, v) for k, v in params.items()), "js"))
    else:
        out.append(fence(json.dumps(c, indent=1, ensure_ascii=False)[:MAX_EXPR], "json"))
    for i, tr in enumerate(rec["transforms"], 1):
        tt = tr.get("type")
        if tt == "script":
            out.append("Transform %d, script:\n\n%s" % (i, fence(clip_lines(tr.get("code", ""), MAX_SCRIPT_LINES),
                                                                  "python")))
        elif tt == "expression":
            out.append("Transform %d, expression:\n\n%s" % (i, fence(clip_expr(tr.get("expression", "")), "js")))
        elif tt == "map":
            maps = tr.get("mappings") or []
            rows = ["%s -> %s" % (short_json(m.get("input"), 50), short_json(m.get("output"), 60)) for m in maps[:20]]
            if len(maps) > 20:
                rows.append("... %d more" % (len(maps) - 20))
            rows.append("fallback -> %s" % short_json(tr.get("fallback"), 60))
            out.append("Transform %d, map (%s to %s):\n\n%s" % (i, tr.get("inputType"), tr.get("outputType"),
                                                               fence("\n".join(rows))))
        elif tt == "format":
            out.append("Transform %d, format %s %s\n" % (i, code(tr.get("formatType", "")),
                                                         code(tr.get("formatValue", ""))))
        else:
            out.append("Transform %d, %s:\n\n%s" % (i, tt, fence(short_json(tr, 400), "json")))
    return "\n".join(out)


def binding_head(rec):
    t, c = rec["type"], rec["config"]
    label = {"expr": "expression", "expr-struct": "structured expression (expr-struct)", "property": "property",
             "tag": "tag", "query": "named query", "tag-history": "tag history"}.get(t, t)
    extra = ""
    if t == "property":
        extra = " " + code(c.get("path", "")) + (" (bidirectional)" if c.get("bidirectional") else "")
    elif t == "tag" and c.get("bidirectional"):
        extra = " (bidirectional)"
    tr = rec["transforms"]
    if tr:
        extra += ", then " + " + ".join(x.get("type", "?") for x in tr) + " transform"
    return "%s: %s%s" % (code(rec["prop"]), label, extra)


def binding_key(rec):
    return json.dumps({"p": rec["prop"], "t": rec["type"], "c": rec["config"], "x": rec["transforms"]},
                      sort_keys=True, ensure_ascii=False)


def handler_key(h):
    return json.dumps({"m": h.get("messageType"), "s": h.get("script")}, sort_keys=True, ensure_ascii=False)


def event_key(e):
    return json.dumps({"e": e["event"], "t": e["type"], "c": e["config"]}, sort_keys=True, ensure_ascii=False)


# --------------------------------------------------------------------------------------------- main


class Gen:
    def __init__(self, repo):
        self.repo = Path(repo).resolve()
        self.persp = self.repo / PERSP_REL
        self.out = self.repo / OUT_REL
        self.views = {}
        self.sources = {}
        self.page_paths = {}                  # view rel -> doc path (posix, relative to docs root, no .md)
        self.common = {}                      # key -> pattern dict
        self.script_pages = {}                # "shared.Alerts" -> doc path

    # ---- helpers
    def rel_link(self, from_doc, to_doc):
        """Relative markdown link from one doc (path under docs/, no .md) to another."""
        a = os.path.dirname(from_doc)
        r = os.path.relpath(to_doc + ".md", a or ".").replace("\\", "/")
        return r if r.startswith(".") else "./" + r

    def view_link(self, from_doc, rel, label=None):
        if rel in self.page_paths:
            return "[%s](%s)" % (esc(label or rel), self.rel_link(from_doc, self.page_paths[rel]))
        return code(rel)

    def hash_source(self, p):
        rel = p.relative_to(self.repo).as_posix()
        with open(p, "rb") as f:
            self.sources[rel] = hashlib.sha256(f.read()).hexdigest()

    def write(self, doc, text):
        p = self.repo / DOCS_REL / (doc + ".md")
        p.parent.mkdir(parents=True, exist_ok=True)
        # no plant IP addresses in the wiki (same rule as gen_tags)
        text = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", "x.x.x.x", text)
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(text.rstrip("\n") + "\n")
        self.written += 1

    def write_category(self, folder_doc, label, position=None, description=None, collapsed=True):
        p = self.repo / DOCS_REL / folder_doc / "_category_.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        cat = {"label": label, "collapsed": collapsed}
        if position is not None:
            cat["position"] = position
        cat["link"] = {"type": "generated-index", "description": description or ("Generated pages for " + label)}
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            json.dump(cat, f, indent=2, ensure_ascii=False)
            f.write("\n")

    # ---- load
    def load(self):
        libs = []
        sp = self.repo / SCRIPTS_REL
        if sp.is_dir():
            libs = sorted(x.name for x in sp.iterdir() if x.is_dir())
        self.libs_re = re.compile(r"\b(?:%s)\.[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?" % "|".join(map(re.escape, libs))) \
            if libs else None
        self.style_classes = {}
        sc_root = self.persp / "style-classes"
        for p in sorted(sc_root.rglob("style.json")):
            name = p.parent.relative_to(sc_root).as_posix()
            self.style_classes[name] = load_json(p)
            self.hash_source(p)
        css_p = self.persp / "stylesheet" / "stylesheet.css"
        self.css = css_p.read_text(encoding="utf-8") if css_p.exists() else ""
        if css_p.exists():
            self.hash_source(css_p)
        self.css_classes = set(m.replace("\\/", "/") for m in re.findall(r"\.psc-((?:[A-Za-z0-9_-]|\\/)+)", self.css))
        known = set(self.style_classes) | self.css_classes
        vroot = self.persp / "views"
        for p in sorted(vroot.rglob("view.json")):
            rel = p.parent.relative_to(vroot).as_posix()
            res_p = p.parent / "resource.json"
            v = View(rel, load_json(p), load_json(res_p) if res_p.exists() else {})
            self.hash_source(p)
            analyse(v, self.libs_re, known)
            v.text = p.read_text(encoding="utf-8")
            self.views[rel] = v
        pc_p = self.persp / "page-config" / "config.json"
        self.page_config = load_json(pc_p) if pc_p.exists() else {"pages": {}}
        if pc_p.exists():
            self.hash_source(pc_p)
        sp_p = self.persp / "session-props" / "props.json"
        self.session_props = load_json(sp_p) if sp_p.exists() else {}
        if sp_p.exists():
            self.hash_source(sp_p)
        perm_p = self.persp / "session-permissions" / "data.bin"
        try:
            self.session_perm = load_json(perm_p)
            self.hash_source(perm_p)
        except Exception:
            self.session_perm = None
        # view references inside other views / project scripts
        paths = sorted(self.views, key=len, reverse=True)
        self.path_re = re.compile(r"(?<=['\"])(%s)(?=\\?['\"])" % "|".join(map(re.escape, paths)))
        self.by_leaf = defaultdict(list)
        for rel in self.views:
            self.by_leaf[rel.split("/")[-1]].append(rel)
        for v in self.views.values():
            for m in self.path_re.finditer(v.text):
                if m.group(1) != v.rel:
                    v.refs.add(m.group(1))
        self.script_files = {}
        if sp.is_dir():
            for p in sorted(sp.rglob("code.py")):
                mod = ".".join(p.parent.relative_to(sp).parts)
                txt = p.read_text(encoding="utf-8", errors="replace")
                self.script_files[mod] = txt
                for m in self.path_re.finditer(txt):
                    if m.group(1) in self.views:
                        self.views[m.group(1)].script_refs.add(mod)
        self.find_script_pages()

    def find_script_pages(self):
        """Map script modules to SCRIPTING's generated pages, if they exist (by title/heading)."""
        sroot = self.repo / DOCS_REL / "scripting"
        if not sroot.is_dir():
            return
        mods = set(self.script_files)
        for p in sroot.rglob("*.md*"):
            try:
                head = p.read_text(encoding="utf-8", errors="replace")[:1500]
            except OSError:
                continue
            doc = p.relative_to(self.repo / DOCS_REL).with_suffix("").as_posix()
            for m in re.finditer(r"^(?:title:\s*\"?|#\s+)`?([A-Za-z_][\w.]+)`?", head, re.M):
                name = m.group(1)
                if name in mods and name not in self.script_pages:
                    self.script_pages[name] = doc

    # ---- cross references
    def cross(self):
        pages = self.page_config.get("pages") or {}
        for url, pg in pages.items():
            vp = pg.get("viewPath")
            if vp in self.views:
                self.views[vp].routes.append((url, pg.get("title", "")))
            for side, docks in (pg.get("docks") or {}).items():
                for dk in docks or []:
                    if dk.get("viewPath") in self.views:
                        self.views[dk["viewPath"]].docks.append("%s dock %s on %s" % (side, dk.get("id"), url))
        for side, docks in (self.page_config.get("sharedDocks") or {}).items():
            if not isinstance(docks, list):
                continue
            for dk in docks:
                if dk.get("viewPath") in self.views:
                    self.views[dk["viewPath"]].docks.append("shared %s dock %s (%s)" % (side, dk.get("id"),
                                                                                         dk.get("show")))
        for v in self.views.values():
            for _, target, _ in v.embeds:
                if target in self.views:
                    self.views[target].embedded_in.add(v.rel)
            for target in v.refs:
                if target in self.views and v.rel not in self.views[target].embedded_in:
                    self.views[target].referenced_by.add(v.rel)
        # nav tree items that open a view as a faceplate
        nav = self.views.get("00_Pages/00_Docked/Navigation")
        self.nav_items = (nav.data.get("custom") or {}).get("items") or [] if nav else []

        def walk(items, trail):
            for it in items or []:
                d = it.get("data") or {}
                t = trail + [str(it.get("label"))]
                if d.get("viewPath") in self.views and d.get("action") == "faceplate":
                    self.views[d["viewPath"]].nav_items.append(" > ".join(t))
                walk(it.get("items"), t)
        walk(self.nav_items, [])
        # common bindings / handlers / events
        bcount, hcount, ecount = defaultdict(set), defaultdict(set), defaultdict(set)
        for v in self.views.values():
            for b in v.bindings:
                bcount[binding_key(b)].add(v.rel)
            for h in v.handlers:
                hcount[handler_key(h)].add(v.rel)
            for e in v.events:
                ecount[event_key(e)].add(v.rel)
        n = 0
        for kind, counter in (("binding", bcount), ("message handler", hcount), ("event", ecount)):
            for key, vs in sorted(counter.items(), key=lambda kv: -len(kv[1])):
                if len(vs) >= COMMON_MIN_VIEWS:
                    n += 1
                    self.common[(kind, key)] = {"id": "pattern-%d" % n, "kind": kind, "views": vs}

    # ---- doc paths
    def assign_paths(self):
        used = {}
        for rel in sorted(self.views):
            parts = [slug(p) for p in rel.split("/")]
            doc = "perspective/reference/views/" + "/".join(parts)
            while doc in used:
                doc += "-2"
            used[doc] = rel
            self.page_paths[rel] = doc

    # ---- writers
    def kind(self, v):
        if v.docks:
            return "Docked view"
        if v.routes:
            return "Page"
        top = v.rel.split("/")[0]
        if "/_Assets/" in "/" + v.rel + "/":
            return "Asset (embedded piece)"
        return {"00_Pages": "Page piece (not routed)", "01_Popups": "Popup / faceplate", "02_Components":
                "Reusable component", "03_Elements": "Element (small reusable part)",
                "98_Configuration": "Configuration / tool view"}.get(top, "View")

    def calls_md(self, doc, calls):
        out = []
        for c in sorted(calls):
            mod = c
            if mod not in self.script_pages:
                mod = ".".join(c.split(".")[:-1]) if c.count(".") >= 1 else c
            if mod in self.script_pages:
                out.append("[%s](%s)" % (esc(c), self.rel_link(doc, self.script_pages[mod])))
            else:
                out.append(code(c))
        return ", ".join(out)

    def view_page(self, v):
        doc = self.page_paths[v.rel]
        root = v.data.get("root") or {}
        props = v.data.get("props") or {}
        desc = "Perspective view %s (%s): %d components, %d bindings, %d event scripts." % (
            v.rel, self.kind(v), len(v.components), len(v.bindings), len(v.events) + len(v.changes))
        md = [front(v.name, desc, {"keywords": [v.rel, v.name] + [r for r, _ in v.routes]})]
        md.append("**%s**: %s.\n" % (esc(self.kind(v)), code(v.rel)))
        rows = [("View path", code(v.rel, True)),
                ("File", code("%s/views/%s/view.json" % (PERSP_REL, v.rel), True)),
                ("Designer", esc("Project Browser > Perspective > Views > " + " > ".join(v.rel.split("/"))))]
        if v.routes:
            rows.append(("Routes", "<br/>".join("%s (%s)" % (code(u, True), esc(t)) for u, t in v.routes)))
        if v.docks:
            rows.append(("Docked", "<br/>".join(esc(d) for d in v.docks)))
        if v.nav_items:
            shown = v.nav_items[:6]
            more = len(v.nav_items) - len(shown)
            rows.append(("Opened from the nav tree", "<br/>".join(esc(x) for x in shown) +
                         ("<br/>... and %d more nav items" % more if more > 0 else "")))
        rows.append(("Root", "%s, %s" % (code(root.get("type", "?"), True),
                                          esc(", ".join("%s %s" % (k, short_json(val, 40)) for k, val in
                                                        (props.get("defaultSize") or {}).items())) or "no default size")))
        rows.append(("Size", "%d components, %d bindings, %d event handlers, %d change scripts, %d message handlers"
                     % (len(v.components), len(v.bindings), len(v.events), len(v.changes), len(v.handlers))))
        lm = (v.resource.get("attributes") or {}).get("lastModification") or {}
        if lm:
            actor = lm.get("actor", "?")
            if actor.lower() not in ("admin", "administrator", "djones", "?"):
                actor = "the Designer"
            rows.append(("Last saved", esc("%s by %s" % (lm.get("timestamp", "?"), actor))))
        md.append(table(["", ""], rows))

        # params / custom
        pconf = v.data.get("propConfig") or {}
        for section, key in (("Params", "params"), ("Custom properties", "custom")):
            vals = v.data.get(key) or {}
            if not vals:
                continue
            rws = []
            for name, val in vals.items():
                pc = pconf.get("%s.%s" % (key, name)) or {}
                notes = []
                if pc.get("paramDirection"):
                    notes.append(pc["paramDirection"])
                if pc.get("binding"):
                    notes.append("bound (%s)" % pc["binding"].get("type"))
                if pc.get("onChange"):
                    notes.append("change script")
                if pc.get("persistent") is False:
                    notes.append("not persistent")
                rws.append((code(name, True), code(short_json(val, 70), True), esc(", ".join(notes))))
            body = table(["Name", "Default", "Notes"], rws)
            md.append("## %s\n\n%s" % (section, maybe_details("%d %s" % (len(rws), section.lower()), body, len(rws))))

        # component tree
        tree = []
        counts = Counter(t for _, _, t, _ in v.components)
        bcount = Counter(b["owner"] for b in v.bindings)
        ecount = Counter(e["owner"] for e in v.events)
        for depth, path, ctype, comp in v.components[:MAX_TREE]:
            name = path.split("/")[-1]
            bits = []
            if bcount.get(path):
                bits.append("%d binding%s" % (bcount[path], "s" if bcount[path] > 1 else ""))
            if ecount.get(path):
                bits.append("%d event%s" % (ecount[path], "s" if ecount[path] > 1 else ""))
            if ctype in ("ia.display.view", "ia.display.flex-repeater"):
                p = (comp.get("props") or {}).get("path")
                bits.append("view: " + (p if p and path not in v.dynamic_embeds else "(bound)"))
            tree.append("%s%s  %s%s" % ("  " * depth, name, ctype, ("  [" + "; ".join(bits) + "]") if bits else ""))
        if len(v.components) > MAX_TREE:
            tree.append("... %d more components (see the Designer)" % (len(v.components) - MAX_TREE))
        md.append("## Component Tree\n")
        md.append("Component types: %s.\n" % esc(", ".join("%s x%d" % (t, n) for t, n in counts.most_common())))
        md.append(maybe_details("Component tree (%d components)" % len(v.components), fence("\n".join(tree), "text"),
                                len(v.components)))

        # bindings
        if v.bindings:
            md.append("## Bindings\n")
            tcount = Counter(b["type"] for b in v.bindings)
            md.append("%d bindings: %s.\n" % (len(v.bindings), esc(", ".join("%s %d" % kv for kv in tcount.most_common()))))
            groups = defaultdict(list)
            for b in v.bindings:
                groups[b["owner"]].append(b)
            body = []
            for owner, bs in groups.items():
                body.append("**%s**\n" % code(owner))
                for b in bs:
                    pat = self.common.get(("binding", binding_key(b)))
                    if pat:
                        body.append("- %s. Common pattern, see [%s](%s).\n" % (
                            binding_head(b), pat["id"], self.rel_link(doc, "perspective/reference/common-patterns") +
                            "#" + pat["id"]))
                        continue
                    body.append("- %s\n" % binding_head(b))
                    inner = binding_body(b)
                    if inner.strip():
                        body.append(inner + "\n")
            text = "\n".join(body)
            md.append(maybe_details("All %d bindings, grouped by component" % len(v.bindings), text, len(v.bindings)))

        # events
        ev_lines = []
        for e in v.events:
            pat = self.common.get(("event", event_key(e)))
            head = "- **%s** %s, %s action%s" % (code(e["owner"]), code(e["event"]), esc(e["type"] or "?"),
                                                (", scope " + code(e["scope"])) if e.get("scope") else "")
            if e.get("enabled") is False:
                head += " (disabled)"
            if pat:
                ev_lines.append(head + ". Common pattern, see [%s](%s).\n" % (
                    pat["id"], self.rel_link(doc, "perspective/reference/common-patterns") + "#" + pat["id"]))
                continue
            c = e["config"]
            if e["type"] == "script":
                ev_lines.append(head + "\n\n" + fence(clip_lines(c.get("script", ""), MAX_EVENT_LINES), "python"))
            elif e["type"] == "popup":
                ev_lines.append(head + ": %s popup %s, view %s\n" % (esc(c.get("type", "open")), code(c.get("id", "")),
                                                                     self.view_link(doc, c.get("viewPath", ""))))
            elif e["type"] == "nav":
                tgt = c.get("page") or c.get("url") or c.get("view") or ""
                ev_lines.append(head + ": navigate to %s\n" % code(tgt))
            else:
                ev_lines.append(head + "\n\n" + fence(short_json(c, 600), "json"))
        for ch in v.changes:
            ev_lines.append("- **%s** change script on %s%s\n\n%s" % (
                code(ch["owner"]), code(ch["prop"]), " (disabled)" if ch.get("enabled") is False else "",
                fence(clip_lines(ch["script"], MAX_EVENT_LINES), "python")))
        for h in v.handlers:
            pat = self.common.get(("message handler", handler_key(h)))
            scopes = [s for s in ("page", "session", "view") if h.get(s + "Scope")]
            head = "- **%s** message handler %s (scope: %s)" % (code(h["owner"]), code(h.get("messageType", "")),
                                                                 esc(", ".join(scopes) or "none"))
            if pat:
                ev_lines.append(head + ". Common pattern, see [%s](%s).\n" % (
                    pat["id"], self.rel_link(doc, "perspective/reference/common-patterns") + "#" + pat["id"]))
            else:
                ev_lines.append(head + "\n\n" + fence(clip_lines(h.get("script", ""), MAX_EVENT_LINES), "python"))
        for cm in v.methods:
            ev_lines.append("- **%s** custom method %s(%s)\n\n%s" % (
                code(cm["owner"]), code(cm.get("name", "")), esc(", ".join(cm.get("params") or [])),
                fence(clip_lines(cm.get("script", ""), MAX_EVENT_LINES), "python")))
        if ev_lines:
            md.append("## Event Scripts And Handlers\n")
            n = len(v.events) + len(v.changes) + len(v.handlers) + len(v.methods)
            md.append(maybe_details("All %d event actions, change scripts and handlers" % n, "\n".join(ev_lines), n))
        if v.calls:
            md.append("Project script calls: %s.\n" % self.calls_md(doc, v.calls))
            if not self.script_pages:
                md.append("Script modules are documented under [Scripting](%s).\n" % self.rel_link(doc, "scripting/index"))

        # view relationships
        rel_lines = []
        if v.embeds:
            items = sorted(set((p, k) for _, p, k in v.embeds))
            rel_lines.append("**Embeds** (%d): %s\n" % (len(items), ", ".join(
                self.view_link(doc, p) + (" (flex repeater)" if k == "repeater" else "") for p, k in items)))
        if v.dynamic_embeds:
            rel_lines.append("**Bound embeds** (view path set by a binding): %s\n" % ", ".join(
                code(x) for x in v.dynamic_embeds[:20]))
        other = sorted(v.refs - set(p for _, p, _ in v.embeds))
        if other:
            rel_lines.append("**Opens or names** (popups, scripts, expressions): %s\n" % ", ".join(
                self.view_link(doc, p) for p in other))
        if v.embedded_in:
            rel_lines.append("**Embedded in** (%d): %s\n" % (len(v.embedded_in), ", ".join(
                self.view_link(doc, p) for p in sorted(v.embedded_in))))
        if v.referenced_by:
            rel_lines.append("**Opened or named by** (%d): %s\n" % (len(v.referenced_by), ", ".join(
                self.view_link(doc, p) for p in sorted(v.referenced_by))))
        if v.script_refs:
            rel_lines.append("**Named in project scripts**: %s\n" % self.calls_md(doc, v.script_refs))
        if rel_lines:
            md.append("## Related Views\n")
            md.append("\n".join(rel_lines))

        # style classes
        if v.classes or v.bound_classes:
            md.append("## Style Classes\n")
            sc = self.rel_link(doc, "perspective/reference/style-classes")
            parts = []
            for c, n in sorted(v.classes.items()):
                kind = "style class" if c in self.style_classes else ("stylesheet" if c in self.css_classes else
                                                                      "no rule found")
                parts.append((code(c, True), str(n), kind))
            for c in sorted(v.bound_classes - set(v.classes)):
                parts.append((code(c, True), "bound", "style class" if c in self.style_classes else "stylesheet"))
            md.append(maybe_details("%d classes" % len(parts), table(["Class", "Uses", "Defined in"], parts),
                                    len(parts)))
            md.append("See the [style class catalog](%s) and the [stylesheet index](%s).\n" % (
                sc, self.rel_link(doc, "perspective/reference/stylesheet")))

        # tags
        if v.tags or v.members or v.queries:
            md.append("## Tags And Data\n")
            if v.queries:
                md.append("Named queries: %s.\n" % ", ".join(code(q) for q in sorted(v.queries)))
            if v.tags:
                tl = sorted(v.tags)
                md.append(maybe_details("%d literal tag paths" % len(tl), "\n".join("- " + code(t) for t in tl) + "\n",
                                        len(tl)))
            if v.members:
                ml = sorted(v.members)
                md.append("Member paths appended to a base path in expressions (relative):\n")
                md.append(maybe_details("%d relative member paths" % len(ml), ", ".join(code(m) for m in ml) + "\n",
                                        len(ml)))
            md.append("Tag folders and UDTs are documented under [Tags](%s).\n" % self.rel_link(doc, "tags/index"))
        self.write(doc, "\n".join(md))

    def folder_indexes(self):
        """_category_.json for every generated folder (labels keep the Designer names)."""
        seen = set()
        for rel in self.views:
            parts = rel.split("/")[:-1]
            for i in range(1, len(parts) + 1):
                folder = "/".join(parts[:i])
                if folder in seen:
                    continue
                seen.add(folder)
                doc_folder = "perspective/reference/views/" + "/".join(slug(p) for p in parts[:i])
                n = sum(1 for r in self.views if r.startswith(folder + "/"))
                self.write_category(doc_folder, parts[i - 1], description="%d views under %s (Designer: Perspective > "
                                    "Views > %s)." % (n, folder, " > ".join(parts[:i])))
        self.write_category("perspective/reference/views", "Views", 1,
                            "One generated page per Perspective view, grouped like the Designer's Project Browser.")

    def views_index(self):
        doc = "perspective/reference/views-index"
        md = [front("All Views", "Every Perspective view in the BH project, grouped by Designer folder, with kind, "
                    "routes and size.", {"sidebar_position": 2})]
        md.append("All %d views of the BH project, grouped by their top Designer folder. Click a name for its page. "
                  "\n" % len(self.views))
        groups = defaultdict(list)
        for rel in sorted(self.views):
            groups[rel.split("/")[0]].append(rel)
        for top, rels in groups.items():
            rows = []
            for rel in rels:
                v = self.views[rel]
                rows.append((self.view_link(doc, rel, rel[len(top) + 1:]), esc(self.kind(v)),
                             "<br/>".join(code(u, True) for u, _ in v.routes[:3]) + (" ..." if len(v.routes) > 3 else ""),
                             str(len(v.bindings))))
            md.append("## %s\n" % esc(top))
            md.append(details("%d views in %s" % (len(rels), top),
                              table(["View", "Kind", "Routes", "Bindings"], rows), open_=len(rels) <= 40))
        self.write(doc, "\n".join(md))

    def routes_page(self):
        doc = "perspective/reference/routes"
        pages = self.page_config.get("pages") or {}
        md = [front("Page Routes", "Every page-config route (URL) of the BH project with its title, view and docks.",
                    {"sidebar_position": 3})]
        md.append("Source: %s (Designer: Project Browser > Perspective > Page Configuration). %d routes. A route "
                  "like %s takes a URL parameter that the view reads from %s.\n" % (
                      code(PERSP_REL + "/page-config/config.json"), len(pages), code("/operations/plcs/:plc"),
                      code("page.props.path") + " / view params"))
        rows = []
        for url in sorted(pages):
            pg = pages[url]
            docks = []
            for side, ds in (pg.get("docks") or {}).items():
                for dk in ds or []:
                    docks.append("%s: %s" % (side, dk.get("id")))
            rows.append((code(url, True), esc(pg.get("title", "")), self.view_link(doc, pg.get("viewPath", "")),
                         esc(", ".join(docks))))
        md.append(table(["URL", "Title", "View", "Page docks"], rows))
        md.append("## Shared Docks\n\nShared docks appear on every page unless a page overrides that side.\n")
        rows = []
        for side, ds in (self.page_config.get("sharedDocks") or {}).items():
            if not isinstance(ds, list):
                continue
            for dk in ds:
                rows.append((esc(side), code(dk.get("id", ""), True), self.view_link(doc, dk.get("viewPath", "")),
                             esc(dk.get("show", "")), esc(dk.get("content", "")), str(dk.get("size", "")),
                             str(dk.get("autoBreakpoint", ""))))
        md.append(table(["Side", "Dock id", "View", "Show", "Content", "Size px", "Auto breakpoint px"], rows))
        if self.page_config.get("sharedDocks", {}).get("cornerPriority"):
            md.append("Corner priority: %s.\n" % code(self.page_config["sharedDocks"]["cornerPriority"]))
        self.write(doc, "\n".join(md))

    def nav_page(self):
        doc = "perspective/reference/nav-tree"
        md = [front("Nav Tree Items", "The full navigation tree (00_Docked/Navigation view.custom.items) with pages, "
                    "views, faceplates and flags.", {"sidebar_position": 4})]
        md.append("Source: %s on the view %s (mirrored in the tag %s). Flags: hidden (kept, not shown), demo (shown "
                  "in enterprise mode), flattenLocal (lifted into its parent in local mode), permission (Roles & "
                  "Permissions row), adminOnly. Faceplate items open a device popup instead of a page.\n" % (
                      code("custom.items"), self.view_link(doc, "00_Pages/00_Docked/Navigation"),
                      code("[default]_Config/Navigation")))
        lines, n = [], [0]
        flag_keys = ("hidden", "demo", "flattenLocal", "adminOnly", "permission", "demoPage", "localPage", "localIcon",
                     "parkedPage")

        def walk(items, depth):
            for it in items or []:
                n[0] += 1
                d = it.get("data") or {}
                bits = []
                if d.get("page"):
                    bits.append("page " + d["page"])
                if d.get("action") == "faceplate":
                    bits.append("faceplate " + str(d.get("viewPath", "")).split("/")[-1] + " on " + str(d.get("tagPath")))
                for k in flag_keys:
                    if d.get(k) not in (None, "", False):
                        bits.append("%s=%s" % (k, d[k]) if d[k] is not True else k)
                icon = (it.get("icon") or {}).get("path")
                lines.append("%s%s%s%s" % ("  " * depth, it.get("label"), ("  (" + icon + ")") if icon else "",
                                           ("  -> " + "; ".join(bits)) if bits else ""))
                walk(it.get("items"), depth + 1)
        walk(self.nav_items, 0)
        md.append("%d nav items in total.\n" % n[0])
        md.append(details("Full nav tree (%d items)" % n[0], fence("\n".join(lines), "text"), open_=False))
        self.write(doc, "\n".join(md))

    def session_page(self):
        doc = "perspective/reference/session-properties"
        sp = self.session_props
        md = [front("Session Properties", "BH session props and session custom properties, with their bindings.",
                    {"sidebar_position": 5})]
        md.append("Source: %s (Designer: Project Browser > Perspective > Session Properties). Session custom "
                  "properties are read in views as %s.\n" % (code(PERSP_REL + "/session-props/props.json"),
                                                             code("{session.custom.<name>}")))
        if self.session_perm:
            md.append("Session permissions (%s): %s, levels %s. A session needs a login before it opens.\n" % (
                code("session-permissions/data.bin"), code(self.session_perm.get("type")),
                ", ".join(code(l.get("name")) for l in self.session_perm.get("securityLevels") or [])))
        md.append("## Session Props\n")
        md.append(table(["Prop", "Value"], [(code(k, True), code(short_json(v, 90), True)) for k, v in
                                            (sp.get("props") or {}).items()]))
        md.append("## Session Custom Properties\n")
        pcs = sp.get("propConfig") or {}
        names = list((sp.get("custom") or {}).keys()) + [k[7:] for k in pcs if k.startswith("custom.") and
                                                          k[7:] not in (sp.get("custom") or {})]
        for name in names:
            pc = pcs.get("custom." + name) or {}
            val = (sp.get("custom") or {}).get(name)
            md.append("### %s\n" % esc(name))
            line = "Access %s." % code(pc.get("access", "default"))
            if val is not None:
                line += " Default %s." % code(short_json(val, 120))
            md.append(line + "\n")
            b = pc.get("binding")
            if b:
                rec = {"prop": "custom." + name, "type": b.get("type"), "config": b.get("config") or {},
                       "transforms": b.get("transforms") or []}
                md.append("Binding " + binding_head(rec) + "\n\n" + binding_body(rec) + "\n")
            users = [rel for rel, v in sorted(self.views.items()) if ("session.custom." + name) in v.text]
            if users:
                md.append(maybe_details("Read by %d views" % len(users), ", ".join(self.view_link(doc, u) for u in users)
                                        + "\n", len(users)))
        other = sorted(k for k in pcs if not k.startswith("custom."))
        if other:
            md.append("## System Prop Access\n")
            md.append(table(["Prop", "Access", "Persistent"], [(code(k, True), code(pcs[k].get("access", ""), True),
                                                                 str(pcs[k].get("persistent", ""))) for k in other]))
        self.write(doc, "\n".join(md))

    def common_page(self):
        doc = "perspective/reference/common-patterns"
        md = [front("Common Binding Patterns", "Bindings, events and message handlers repeated in many views, shown "
                    "once.", {"sidebar_position": 6})]
        md.append("These bindings, event actions and message handlers are identical in %d or more views. The view pages "
                  "link here instead of repeating them. For example the Ticket Logger right-click menu.\n" % COMMON_MIN_VIEWS)
        for (kind, key), pat in sorted(self.common.items(), key=lambda kv: int(kv[1]["id"].split("-")[1])):
            data = json.loads(key)
            md.append("## %s: %s \\{#%s\\}\n" % (pat["id"].replace("-", " ").title(), esc(kind).title(), pat["id"]))
            if kind == "binding":
                rec = {"prop": data["p"], "type": data["t"], "config": data["c"], "transforms": data["x"]}
                md.append("- " + binding_head(rec) + "\n\n" + binding_body(rec) + "\n")
            elif kind == "event":
                md.append("Event %s, %s action.\n" % (code(data["e"]), esc(data["t"])))
                c = data["c"]
                if data["t"] == "script":
                    md.append(fence(clip_lines(c.get("script", ""), 80), "python"))
                else:
                    md.append(fence(json.dumps(c, indent=1, ensure_ascii=False)[:2000], "json"))
            else:
                md.append("Message type %s.\n\n%s" % (code(data["m"]), fence(clip_lines(data["s"] or "", 80), "python")))
            vs = sorted(pat["views"])
            md.append(details("Used in %d views" % len(vs), ", ".join(self.view_link(doc, x) for x in vs) + "\n"))
        self.write(doc, "\n".join(md))

    def style_page(self):
        doc = "perspective/reference/style-classes"
        md = [front("Style Class Catalog", "Every project style class (style-classes/) with its CSS and the views that "
                    "use it.", {"sidebar_position": 7})]
        md.append("Source: %s (Designer: Project Browser > Perspective > Styles). %d style classes. Perspective emits "
                  "each as %s after the stylesheet, sorted by name. A view uses one by putting its name in %s.\n" % (
                      code(PERSP_REL + "/style-classes/<name>/style.json"), len(self.style_classes), code(".psc-<name>"),
                      code("props.style.classes")))
        users = defaultdict(set)
        for rel, v in self.views.items():
            for c in set(v.classes) | v.bound_classes:
                users[c].add(rel)
        groups = defaultdict(list)
        for name in sorted(self.style_classes, key=str.lower):
            groups[re.split(r"[-/]", name)[0]].append(name)
        for g, names in sorted(groups.items(), key=lambda kv: kv[0].lower()):
            md.append("## %s\n" % esc(g))
            for name in names:
                sc = self.style_classes[name]
                css = []
                for state, block in sc.items():
                    style = (block or {}).get("style") if isinstance(block, dict) else None
                    decl = "\n".join("  %s: %s;" % (re.sub(r"([A-Z])", lambda m: "-" + m.group(1).lower(), k), v)
                                     for k, v in (style or {}).items())
                    sel = ".psc-%s%s" % (name.replace("/", "\\/"), "" if state == "base" else "  /* " + state + " */")
                    css.append("%s {\n%s\n}" % (sel, decl))
                    extra = {k: v for k, v in (block or {}).items() if k != "style"} if isinstance(block, dict) else {}
                    if extra:
                        css.append("/* %s */" % short_json(extra, 200))
                us = sorted(users.get(name, ()))
                md.append("### %s\n" % esc(name))
                md.append(fence("\n".join(css), "css"))
                if us:
                    md.append(maybe_details("Used in %d views" % len(us), ", ".join(self.view_link(doc, u) for u in us)
                                            + "\n", len(us)))
                else:
                    md.append("Not used in any view's static classes (may be set by a binding or a script).\n")
        self.write(doc, "\n".join(md))

    def stylesheet_page(self):
        doc = "perspective/reference/stylesheet"
        lines = self.css.split("\n")
        md = [front("Stylesheet Index", "Section index of the BH Advanced Stylesheet (stylesheet.css): every comment "
                    "block, its line range and the classes it defines.", {"sidebar_position": 8})]
        md.append("Source: %s (Designer: Project Browser > Perspective > Styles > Advanced Stylesheet). %d lines, "
                  "%d %s classes. Sections start at a comment in column 1. Selectors use %s for project classes "
                  "(%s becomes %s).\n" % (code(PERSP_REL + "/stylesheet/stylesheet.css"), len(lines),
                                          len(self.css_classes), code(".psc-*"), code(".psc-<class>"),
                                          code("Fonts/Label"), code(".psc-Fonts\\/Label")))
        starts = [i for i, l in enumerate(lines) if l.startswith("/*")]
        rows = []
        class_lines = defaultdict(list)
        for i, l in enumerate(lines):
            if l.lstrip().startswith("/*") or l.lstrip().startswith("*"):
                continue
            for m in re.finditer(r"\.psc-((?:[A-Za-z0-9_-]|\\/)+)", l):
                class_lines[m.group(1).replace("\\/", "/")].append(i + 1)
        for k, s in enumerate(starts):
            e = (starts[k + 1] if k + 1 < len(starts) else len(lines)) - 1
            head = lines[s].strip()[2:].strip(" *-=").replace("*/", "").strip()
            j = s
            while not head and j < e and j < s + 4:
                j += 1
                head = lines[j].strip(" *-=/").strip()
            seg = "\n".join(l for l in lines[s:e + 1] if not l.lstrip().startswith(("/*", "*")))
            cls = sorted(set(m.replace("\\/", "/") for m in re.findall(r"\.psc-((?:[A-Za-z0-9_-]|\\/)+)", seg)))
            rules = seg.count("{")
            rows.append(("%d-%d" % (s + 1, e + 1), esc(head[:110]), str(rules),
                         esc(", ".join(cls[:12]) + (" ... +%d" % (len(cls) - 12) if len(cls) > 12 else ""))))
        md.append("## Sections\n")
        md.append(table(["Lines", "Section comment", "Rules", "Classes"], rows))
        md.append("## Class To Line Index\n")
        body = table(["Class", "Lines", "Also a style class"], [
            (code(c, True), esc(", ".join(map(str, sorted(set(ls))[:12])) + (" ..." if len(set(ls)) > 12 else "")),
             "yes" if c in self.style_classes else "") for c, ls in sorted(class_lines.items(), key=lambda kv: kv[0].lower())])
        md.append(details("%d classes referenced in selectors" % len(class_lines), body))
        roots = re.findall(r"^\s*(--[A-Za-z0-9-]+)\s*:\s*([^;]+);", self.css, re.M)
        if roots:
            md.append("## Custom Properties (CSS Variables)\n")
            seen = {}
            for k, val in roots:
                seen.setdefault(k, val.strip())
            md.append(details("%d variables defined in the stylesheet" % len(seen), table(
                ["Variable", "First value"], [(code(k, True), code(v[:80], True)) for k, v in sorted(seen.items())])))
        self.write(doc, "\n".join(md))

    def themes_page(self):
        doc = "perspective/reference/themes-and-icons"
        core = self.repo / CORE_REL
        md = [front("Themes And Icons", "Gateway Perspective themes (folders, imports, neutral scale) and the icon "
                    "libraries.", {"sidebar_position": 9})]
        md.append("Themes and icon libraries are **gateway** config resources under %s, not part of the project. "
                  "%s picks the theme folder.\n" % (code(CORE_REL), code("session.props.theme")))
        troot = core / "themes"
        if troot.is_dir():
            md.append("## Themes\n")
            for t in sorted(x for x in troot.iterdir() if x.is_dir()):
                files = sorted(p.relative_to(t).as_posix() for p in t.rglob("*") if p.is_file())
                idx = t / "index.css"
                imports = re.findall(r"@import\s+[\"']([^\"']+)", idx.read_text(encoding="utf-8")) if idx.exists() else []
                var_p = t / "variables.css"
                neutrals = []
                if var_p.exists():
                    self.hash_source(var_p)
                    vt = var_p.read_text(encoding="utf-8")
                    neutrals = re.findall(r"(--neutral-\d+)\s*:\s*([^;]+);", vt)
                    base = re.findall(r"@import\s+[\"']([^\"']+)", vt)
                else:
                    base = []
                if idx.exists():
                    self.hash_source(idx)
                md.append("### %s\n" % esc(t.name))
                md.append("%d files (%s). index.css imports: %s.%s\n" % (
                    len(files), "full base" if len(files) > 8 else "thin variant",
                    ", ".join(code(i) for i in imports) or "none",
                    (" variables.css imports " + ", ".join(code(b) for b in base) + ".") if base else ""))
                if neutrals:
                    md.append(table(["Neutral", "Value"], [(code(k, True), code(v.strip(), True)) for k, v in neutrals]))
        iroot = core / "icons"
        if iroot.is_dir():
            md.append("## Icon Libraries\n")
            md.append("Use an icon in a view as %s (the Icon component %s, or a nav item icon). %s icons come with "
                      "Ignition.\n" % (code("<library>/<id>"), code("props.path"), code("material/*")))
            for lib in sorted(x for x in iroot.iterdir() if x.is_dir()):
                for svg in sorted(lib.glob("*.svg")):
                    self.hash_source(svg)
                    txt = svg.read_text(encoding="utf-8")
                    ids = re.findall(r"<!--\s*([^>]*?)\s*-->\s*<svg[^>]*>\s*<g[^>]*id=\"([^\"]+)\"", txt)
                    allids = re.findall(r"<g[^>]*class=\"icon\"[^>]*id=\"([^\"]+)\"|<g[^>]*id=\"([^\"]+)\"[^>]*class=\"icon\"", txt)
                    labels = {i: lab for lab, i in ids}
                    rows = []
                    for a, b in allids:
                        i = a or b
                        token = "%s/%s" % (lib.name, i)
                        uses = sum(1 for v in self.views.values() if token in v.text)
                        rows.append((code(token, True), esc(labels.get(i, "")), str(uses)))
                    md.append("### %s\n" % esc(lib.name))
                    md.append("File %s, %d icons.\n" % (code(svg.relative_to(self.repo).as_posix()), len(rows)))
                    md.append(table(["Icon path", "Label", "Views using it"], rows))
        mat = Counter()
        for v in self.views.values():
            for m in re.findall(r"\"(material/[a-z0-9_]+)\"", v.text):
                mat[m] += 1
        if mat:
            md.append("## Material Icons In Use\n")
            md.append(details("%d material icons referenced in views" % len(mat), table(
                ["Icon path", "References"], [(code(k, True), str(n)) for k, n in mat.most_common()])))
        self.write(doc, "\n".join(md))

    def index_page(self):
        doc = "perspective/reference/index"
        nb = sum(len(v.bindings) for v in self.views.values())
        ne = sum(len(v.events) + len(v.changes) + len(v.handlers) for v in self.views.values())
        tc = Counter(b["type"] for v in self.views.values() for b in v.bindings)
        md = [front("Perspective Reference", "Generated reference for the BH Perspective project: views, routes, nav, "
                    "session, styles.", {"sidebar_position": 1})]
        md.append("Generated straight from the project files by %s. Hand-written guides are one level up in "
                  "[Perspective](%s).\n" % (code("wiki/tools/gen_perspective.py"), self.rel_link(doc, "perspective/index")))
        md.append(table(["What", "Count"], [
            ("Views", str(len(self.views))),
            ("Bindings", "%d (%s)" % (nb, esc(", ".join("%s %d" % kv for kv in tc.most_common())))),
            ("Event actions, change scripts, message handlers", str(ne)),
            ("Page routes", str(len(self.page_config.get("pages") or {}))),
            ("Style classes", str(len(self.style_classes))),
            ("Stylesheet classes (.psc-*)", str(len(self.css_classes))),
            ("Common patterns", str(len(self.common)))]))
        md.append("## Pages\n")
        for d, t in (("views-index", "All Views"), ("routes", "Page Routes"), ("nav-tree", "Nav Tree Items"),
                     ("session-properties", "Session Properties"), ("common-patterns", "Common Binding Patterns"),
                     ("style-classes", "Style Class Catalog"), ("stylesheet", "Stylesheet Index"),
                     ("themes-and-icons", "Themes And Icons")):
            md.append("- [%s](%s)" % (t, self.rel_link(doc, "perspective/reference/" + d)))
        md.append("\nEach view page lists its path, Designer location and routes, params and custom properties, a "
                  "component tree, every binding (with expressions and transforms), every event script, the views it "
                  "embeds and the views that embed it, its style classes and the tag paths it names.\n")
        md.append("To regenerate after a project change: %s (or %s for this area only).\n" % (
            code("python -I wiki/tools/gen_all.py"), code("python -I wiki/tools/gen_perspective.py")))
        self.write(doc, "\n".join(md))

    def run(self):
        self.written = 0
        self.load()
        self.cross()
        self.assign_paths()
        if self.out.exists():
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True)
        cat = {"label": "Reference (Generated)", "position": 99, "collapsed": True,
               "link": {"type": "doc", "id": "perspective/reference/index"}}
        with open(self.out / "_category_.json", "w", encoding="utf-8", newline="\n") as f:
            json.dump(cat, f, indent=2)
            f.write("\n")
        self.index_page()
        self.views_index()
        self.routes_page()
        self.nav_page()
        self.session_page()
        self.common_page()
        self.style_page()
        self.stylesheet_page()
        self.themes_page()
        self.folder_indexes()
        for rel in sorted(self.views):
            self.view_page(self.views[rel])
        legacy = self.repo / HASHES_REL           # superseded by gen_all.py's manifest
        if legacy.exists():
            legacy.unlink()
        nb = sum(len(v.bindings) for v in self.views.values())
        stats = {"views": len(self.views), "bindings": nb, "routes": len(self.page_config.get("pages") or {}),
                 "style_classes": len(self.style_classes), "pages_written": self.written}
        print("gen_perspective: " + ", ".join("%s %s" % kv for kv in stats.items()))
        return stats


def main(repo_root=None):
    repo = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    return Gen(repo).run()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
