"""Generate the scripting / database reference pages of the BH wiki.

    python -I wiki/tools/gen_scripting.py          # or: python -I wiki/tools/gen_all.py scripting

Writes ONLY these generated pages (front matter `generated: true`):
    wiki/docs/scripting/reference/**   project script library (one page per module, every function with its
                                       signature, docstring and callers), gateway events, tag event scripts,
                                       Perspective messages, named queries (SQL, parameters, callers), WebDev,
                                       Reporting resources, loggers
    wiki/docs/database/reference/**    the tables created by sql/*.sql (columns, types, comments, indexes)

Everything is read from files on disk (the project files and sql/). Nothing talks to
the gateway or the database. Stdlib only, UTF-8, Python 3.9+. main(repo_root) returns a summary dict.
Source hashes: wiki/tools/gen_all.py hashes SOURCES into wiki/tools/manifest/sources.json (check_docs.py).
"""
from __future__ import annotations

import ast
import io
import json
import re
import sys
import warnings
from pathlib import Path

GW = "gateways/standard/data"
PROJ = GW + "/projects/BH"
CORE = GW + "/config/resources/core"
VIEWS = PROJ + "/com.inductiveautomation.perspective/views"

# repo-relative globs this reference tool reads (gen_all.py hashes them for check_docs.py)
SOURCES = [
    PROJ + "/ignition/**/*",
    PROJ + "/com.inductiveautomation.reporting/**/*",
    PROJ + "/com.inductiveautomation.webdev/**/*",
    PROJ + "/com.inductiveautomation.perspective/views/**/view.json",
    PROJ + "/com.inductiveautomation.perspective/session-props/props.json",
    CORE + "/ignition/tag-definition/default/_Config/**/*.json",
    CORE + "/ignition/tag-type-definition/**/*.json",
    "sql/**/*.sql",
]

BANNER = ":::note\nThis reference page is generated from the project files.\n:::\n"
SQLTYPES = {0: "Int1", 1: "Int2", 2: "Int4", 3: "Int8", 4: "Float4", 5: "Float8", 6: "Boolean", 7: "String",
            8: "DateTime", 9: "Text"}
CALL_RE = re.compile(r"\b(shared|Navigation|L5K)\.([A-Za-z_]\w*)\.([A-Za-z_]\w*)")
LOGGER_RE = re.compile(r"getLogger\(\s*['\"]([^'\"]+)['\"]")
API_RE = re.compile(r"\bsystem\.([a-z]+)\.")
SEND_RE = re.compile(r"sendMessage\(\s*(?:messageType\s*=\s*)?['\"]([\w.\-]+)['\"]([^\n]*)")
MENU_MSG_RE = re.compile(r"['\"]message['\"]\s*:\s*\{\s*['\"]type['\"]\s*:\s*['\"]([\w.\-]+)['\"]")
SCOPE_RE = re.compile(r"scope\s*=\s*['\"](\w+)['\"]")
MENU_ITEM_RE = re.compile(r"(?<![\w.])item\(\s*['\"][^'\"]*['\"]\s*,\s*['\"][^'\"]*['\"]\s*,\s*['\"]([\w.\-]+)['\"]")
ALERT_BTN_RE = re.compile(r"btnAction(?:Primary|Secondary)\s*[=:]\s*['\"]([A-Za-z][\w.\-]*)['\"]")


# ---------------------------------------------------------------------------------------------- text helpers
def esc(text) -> str:
    """Plain markdown text safe for MDX (no JSX braces / tags)."""
    s = "" if text is None else str(text)
    return (s.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")
            .replace("<", "&lt;").replace(">", "&gt;").replace("*", "\\*").replace("_", "\\_"))


def code(text) -> str:
    """Inline code span, safe inside a GFM table cell."""
    s = ("" if text is None else str(text)).replace("\r", " ").replace("\n", " ").replace("|", "\\|")
    if not s:
        return ""
    if "`" in s:
        return "`` " + s + " ``"
    return "`" + s + "`"


def cell(text) -> str:
    return demojibake(esc(text).replace("|", "\\|").replace("\n", " "))


_U = "\\" + "u00"          # built at run time to avoid literal mojibake in this file
MOJIBAKE = [(chr(0xE2) + chr(0x20AC), "(mojibake)"), (chr(0xC2), "(A-circumflex)"), (chr(0xC3), "(A-tilde)"),
            (_U + "c2", "U+00C2"), (_U + "c3", "U+00C3"), (chr(0xFFFD), "(U+FFFD)"), (chr(0xFEFF), "")]


def demojibake(s: str) -> str:
    """Docstrings that describe mojibake must not trip the encoding check on the wiki."""
    for a, b in MOJIBAKE:
        s = s.replace(a, b)
    return s


def fence(text, lang="text") -> str:
    s = demojibake(("" if text is None else str(text)).replace("\r\n", "\n").replace("```", "'''").rstrip())
    return "```" + lang + "\n" + s + "\n```\n"


def slug(text) -> str:
    return re.sub(r"[^a-z0-9_]+", "-", str(text).lower()).strip("-") or "x"


def heading(level, text, anchor) -> str:
    return "%s %s {#%s}\n\n" % ("#" * level, esc(text), slug(anchor))


def front(title, desc, label=None, pos=None) -> str:
    lines = ["---", "title: " + json.dumps(title, ensure_ascii=False)]
    if label:
        lines.append("sidebar_label: " + json.dumps(label, ensure_ascii=False))
    if pos is not None:
        lines.append("sidebar_position: %d" % pos)
    lines += ["description: " + json.dumps(desc, ensure_ascii=False), "generated: true",
              "custom_edit_url: null", "---", ""]
    return "\n".join(lines) + "\n"


def read(p: Path) -> str:
    return io.open(p, encoding="utf-8", errors="replace").read()


def rel(repo: Path, p: Path) -> str:
    return p.relative_to(repo).as_posix()


def details(summary, body) -> str:
    return "<details>\n<summary>%s</summary>\n\n%s\n</details>\n" % (esc(summary), body.rstrip())


def write(path: Path, text: str, written: list):
    path.parent.mkdir(parents=True, exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text.rstrip() + "\n")
    written.append(path)


def category(path: Path, label, pos, doc_id, written):
    write(path / "_category_.json", json.dumps({"label": label, "position": pos,
                                                "link": {"type": "doc", "id": doc_id}}, indent=2), written)


# ---------------------------------------------------------------------------------------------- python parsing
def parse_py(src):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            return ast.parse(src)
        except SyntaxError:
            return None


def signature(fn) -> str:
    a = fn.args
    out = []
    pos = list(a.posonlyargs) + list(a.args)
    defaults = [None] * (len(pos) - len(a.defaults)) + list(a.defaults)
    for arg, d in zip(pos, defaults):
        out.append(arg.arg + ("=" + _src(d) if d is not None else ""))
    if a.vararg:
        out.append("*" + a.vararg.arg)
    for arg, d in zip(a.kwonlyargs, a.kw_defaults):
        out.append(arg.arg + ("=" + _src(d) if d is not None else ""))
    if a.kwarg:
        out.append("**" + a.kwarg.arg)
    return "%s(%s)" % (fn.name, ", ".join(out))


def _src(node) -> str:
    try:
        s = ast.unparse(node)
    except Exception:
        s = "..."
    return s if len(s) <= 60 else s[:57] + "..."


def leading_comment(src_lines, lineno) -> str:
    """Comment block right above a def (used when there is no docstring)."""
    out = []
    i = lineno - 2
    while i >= 0 and src_lines[i].strip().startswith("#"):
        out.insert(0, src_lines[i].strip().lstrip("#").strip())
        i -= 1
    return "\n".join(out)


def module_header(src, tree) -> str:
    doc = ast.get_docstring(tree) if tree is not None else None
    if doc:
        return doc
    lines = []
    for line in src.splitlines():
        if line.startswith("#"):
            lines.append(line.lstrip("#").strip())
        elif line.strip() == "" and lines:
            break
        elif line.strip() == "":
            continue
        else:
            break
    return "\n".join(lines)


class Module:
    def __init__(self, repo, path, pkg, name):
        self.path = path
        self.rel = rel(repo, path)
        self.pkg, self.name = pkg, name
        self.full = pkg + "." + name
        self.src = read(path)
        self.tree = parse_py(self.src)
        self.header = module_header(self.src, self.tree)
        self.functions = []      # dicts: name, sig, doc, line, end, kind
        self.constants = []      # (name, short value)
        self.prefixes = []       # module-level string constants ending with '/'
        self.loggers = sorted(set(LOGGER_RE.findall(self.src)))
        self.apis = sorted(set(API_RE.findall(self.src)))
        lines = self.src.splitlines()
        if self.tree is None:
            for m in re.finditer(r"^def\s+(\w+)\s*\(([^)]*)\)", self.src, re.M):
                ln = self.src[:m.start()].count("\n") + 1
                self.functions.append({"name": m.group(1), "sig": "%s(%s)" % (m.group(1), m.group(2)),
                                       "doc": leading_comment(lines, ln), "line": ln, "end": ln, "kind": "def"})
            self.funcnames = set(f["name"] for f in self.functions)
            return
        for node in self.tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.functions.append({"name": node.name, "sig": signature(node),
                                       "doc": ast.get_docstring(node) or leading_comment(lines, node.lineno),
                                       "line": node.lineno, "end": getattr(node, "end_lineno", node.lineno),
                                       "kind": "def"})
            elif isinstance(node, ast.ClassDef):
                self.functions.append({"name": node.name, "sig": "class " + node.name,
                                       "doc": ast.get_docstring(node) or leading_comment(lines, node.lineno),
                                       "line": node.lineno, "end": getattr(node, "end_lineno", node.lineno),
                                       "kind": "class"})
            elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                nm = node.targets[0].id
                if nm.isupper() or (nm[:1] == "_" and nm[1:2].isupper()):
                    v = _src(node.value)
                    self.constants.append((nm, v))
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) \
                            and node.value.value.endswith("/"):
                        self.prefixes.append(node.value.value)
        self.funcnames = set(f["name"] for f in self.functions)

    def func_at(self, line):
        for f in self.functions:
            if f["line"] <= line <= f["end"]:
                return f["name"]
        return "(module level)"

    def strings(self):
        """(value, line) of every string literal."""
        if self.tree is None:
            return [(m.group(2), self.src[:m.start()].count("\n") + 1)
                    for m in re.finditer(r"(['\"])([^'\"\n]{2,200})\1", self.src)]
        out = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                out.append((node.value, getattr(node, "lineno", 0)))
        return out


# ---------------------------------------------------------------------------------------------- view walking
def _where(keys, label):
    if label:
        return label
    ks = [k for k in keys if isinstance(k, str)]
    if not ks:
        return ""
    if ks[0] == "events":
        return "event " + ".".join(ks[1:3])
    if ks[0] == "propConfig":
        return ("binding " + ks[1]) if len(ks) > 1 else "propConfig"
    if ks[0] in ("props", "custom", "params", "meta", "position"):
        return ".".join(ks[:2])
    return ks[0]


def walk_strings(obj, comp="", keys=(), label=""):
    """Yield (component path, location, string) for every string leaf of a Perspective view / props JSON."""
    if isinstance(obj, dict):
        meta = obj.get("meta")
        if isinstance(meta, dict) and isinstance(meta.get("name"), str) and "type" in obj:
            comp = (comp + "/" if comp else "") + meta["name"]
            keys, label = (), ""
        for k, v in obj.items():
            if k == "children":
                yield from walk_strings(v, comp, (), "")
                continue
            if k in ("messageHandlers", "customMethods", "extensionFunctions") and isinstance(v, list):
                kind = {"messageHandlers": "message handler", "customMethods": "custom method",
                        "extensionFunctions": "extension function"}[k]
                for item in v:
                    nm = item.get("messageType") or item.get("name") or "" if isinstance(item, dict) else ""
                    yield from walk_strings(item, comp, keys + (k,), ("%s %s" % (kind, nm)).strip())
                continue
            if isinstance(v, str):
                yield comp, _where(keys + (k,), label), v
            else:
                yield from walk_strings(v, comp, keys + (k,), label)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v, comp, keys, label)


def message_handlers(obj, comp=""):
    """(component, messageType, scopes) of every Perspective message handler."""
    if isinstance(obj, dict):
        meta = obj.get("meta")
        if isinstance(meta, dict) and isinstance(meta.get("name"), str) and "type" in obj:
            comp = (comp + "/" if comp else "") + meta["name"]
        scripts = obj.get("scripts")
        if isinstance(scripts, dict):
            for h in scripts.get("messageHandlers") or []:
                if isinstance(h, dict):
                    scopes = [s for s in ("viewScope", "pageScope", "sessionScope") if h.get(s)]
                    yield comp or "(view)", h.get("messageType", ""), [s.replace("Scope", "") for s in scopes]
        for k, v in obj.items():
            if k != "scripts":
                yield from message_handlers(v, comp)
    elif isinstance(obj, list):
        for v in obj:
            yield from message_handlers(v, comp)


# ---------------------------------------------------------------------------------------------- collection
class Index:
    def __init__(self, repo: Path):
        self.repo = repo
        self.modules = {}
        self.calls = {}          # full module.func -> list of (caller kind, caller, location)
        self.nq_callers = {}     # nq path -> list of (kind, caller, location)
        self.msg_send = {}       # message type -> list of (source, location, scope)
        self.msg_handle = {}     # message type -> list of (view, component, scopes)
        self.view_texts = []     # (view path, [(comp, where, string)])
        self.queries = {}
        self.warnings = []

    # -------- script library
    def load_modules(self):
        base = self.repo / PROJ / "ignition" / "script-python"
        for p in sorted(base.glob("*/*/code.py")):
            pkg, name = p.parent.parent.name, p.parent.name
            m = Module(self.repo, p, pkg, name)
            self.modules[m.full] = m
        for p in sorted(base.glob("*/code.py")):   # top-level module (none today)
            m = Module(self.repo, p, "", p.parent.name)
            m.full = p.parent.name
            self.modules[m.full] = m

    def add_call(self, target, kind, caller, where):
        lst = self.calls.setdefault(target, [])
        key = (kind, caller, where)
        if key not in lst:
            lst.append(key)

    def scan_text(self, kind, caller, items):
        """items: iterable of (location, text)."""
        for where, text in items:
            for m in CALL_RE.finditer(text):
                full = m.group(1) + "." + m.group(2)
                if full in self.modules and m.group(3) in self.modules[full].funcnames:
                    self.add_call(full + "." + m.group(3), kind, caller, where)
            for m in SEND_RE.finditer(text):
                sc = SCOPE_RE.search(m.group(2) or "")
                self.msg_send.setdefault(m.group(1), []).append((kind + " " + caller, where,
                                                                 sc.group(1) if sc else "default"))
            for m in MENU_MSG_RE.finditer(text):
                self.msg_send.setdefault(m.group(1), []).append((kind + " " + caller, where, "menu item"))
            for m in MENU_ITEM_RE.finditer(text):
                self.msg_send.setdefault(m.group(1), []).append((kind + " " + caller, where, "menu item"))
            for m in ALERT_BTN_RE.finditer(text):
                self.msg_send.setdefault(m.group(1), []).append((kind + " " + caller, where,
                                                                 "Alert popup button (page)"))

    def scan_modules(self):
        for full, mod in self.modules.items():
            if mod.tree is not None:
                for node in ast.walk(mod.tree):
                    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Attribute) \
                            and isinstance(node.value.value, ast.Name):
                        tgt = node.value.value.id + "." + node.value.attr
                        if tgt in self.modules and node.attr in self.modules[tgt].funcnames and tgt != full:
                            self.add_call(tgt + "." + node.attr, "script", full + "." + mod.func_at(node.lineno), "")
                    elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                            and node.func.id in mod.funcnames:
                        caller = mod.func_at(node.lineno)
                        if caller != node.func.id:
                            self.add_call(full + "." + node.func.id, "same module", full + "." + caller, "")
            for rx, sc_label in ((MENU_ITEM_RE, "menu item"), (ALERT_BTN_RE, "Alert popup button (page)")):
                for m in rx.finditer(mod.src):
                    ln = mod.src[:m.start()].count("\n") + 1
                    self.msg_send.setdefault(m.group(1), []).append(("script " + full + "." + mod.func_at(ln), "",
                                                                     sc_label))
            for m in SEND_RE.finditer(mod.src):
                sc = SCOPE_RE.search(m.group(2) or "")
                ln = mod.src[:m.start()].count("\n") + 1
                self.msg_send.setdefault(m.group(1), []).append(("script " + full + "." + mod.func_at(ln), "",
                                                                 sc.group(1) if sc else "default"))

    # -------- views / other scripts
    def scan_views(self):
        base = self.repo / VIEWS
        for p in sorted(base.rglob("view.json")):
            vpath = p.parent.relative_to(base).as_posix()
            try:
                data = json.loads(read(p))
            except ValueError:
                self.warnings.append("unreadable view " + vpath)
                continue
            leaves = list(walk_strings(data))
            self.view_texts.append((vpath, leaves))
            self.scan_text("view", vpath, ((("%s %s" % (c, w)).strip(), s) for c, w, s in leaves))
            for comp, mtype, scopes in message_handlers(data):
                self.msg_handle.setdefault(mtype, []).append((vpath, comp, scopes))
        props = self.repo / PROJ / "com.inductiveautomation.perspective" / "session-props" / "props.json"
        if props.exists():
            leaves = list(walk_strings(json.loads(read(props))))
            self.view_texts.append(("(session props)", leaves))
            self.scan_text("session props", "session-props", ((w, s) for c, w, s in leaves))

    def gateway_scripts(self):
        """[(kind, name, resource dict, {file: code})] for timers, tag change, message, startup ... events."""
        out = []
        ign = self.repo / PROJ / "ignition"
        skip = {"script-python", "named-query", "global-props"}
        for d in sorted(x for x in ign.iterdir() if x.is_dir() and x.name not in skip):
            for res in sorted(d.rglob("resource.json")):
                folder = res.parent
                try:
                    meta = json.loads(read(res))
                except ValueError:
                    meta = {}
                files = {}
                for f in meta.get("files", []):
                    fp = folder / f
                    if fp.exists() and fp.suffix == ".py":
                        files[f] = read(fp)
                out.append((d.name, folder.relative_to(d).as_posix(), meta, files))
        for kind, name, meta, files in out:
            self.scan_text("gateway " + kind, name, ((f, s) for f, s in files.items()))
        return out

    def webdev(self):
        out = []
        base = self.repo / PROJ / "com.inductiveautomation.webdev" / "resources"
        if not base.exists():
            return out
        for res in sorted(base.rglob("resource.json")):
            folder = res.parent
            name = folder.relative_to(base).as_posix()
            cfg = {}
            if (folder / "config.json").exists():
                try:
                    cfg = json.loads(read(folder / "config.json"))
                except ValueError:
                    cfg = {}
            methods = {}
            for f in sorted(folder.glob("do*.py")):
                methods[f.stem] = read(f)
            out.append((name, cfg, methods))
            self.scan_text("webdev", name, ((m, s) for m, s in methods.items()))
        return out

    def reports(self):
        out = []
        base = self.repo / PROJ / "com.inductiveautomation.reporting" / "reports"
        if not base.exists():
            return out
        for data in sorted(base.rglob("data.bin")):
            name = data.parent.relative_to(base).as_posix()
            raw = data.read_bytes()
            info = {"name": name, "xml": raw.lstrip().startswith(b"<?xml"), "size": len(raw),
                    "params": [], "sources": [], "description": ""}
            if info["xml"]:
                s = raw.decode("utf-8", "replace")
                for m in re.finditer(r"ReportParameter\">(.*?)</o>", s, re.S):
                    blk = m.group(1)
                    nm = re.search(r'm="setName"[^>]*><str>(.*?)</str>', blk, re.S)
                    tp = re.search(r"<class>(.*?)</class>", blk)
                    dv = re.search(r'm="setDefaultValue"[^>]*><str>(.*?)</str>', blk, re.S)
                    info["params"].append((nm.group(1) if nm else "?", (tp.group(1) if tp else "").split(".")[-1],
                                           dv.group(1) if dv else ""))
                for m in re.finditer(r'cls="([\w.]+ReportDataObject)">(.*?)</o>', s, re.S):
                    blk = m.group(2)
                    nm = re.search(r'm="setName"[^>]*><str>(.*?)</str>', blk, re.S)
                    sc = re.search(r'm="setScript"[^>]*><str>(.*?)</str>', blk, re.S)
                    script = _xml_unescape(sc.group(1)) if sc else ""
                    info["sources"].append((m.group(1).split(".")[-1], nm.group(1) if nm else "?", script))
                    self.scan_text("report", name, [("data source", script)])
                d = re.search(r'm="setDescription"[^>]*><str>(.*?)</str>', s, re.S)
                info["description"] = _xml_unescape(d.group(1)) if d else ""
            out.append(info)
        return out

    # -------- named queries
    def load_queries(self):
        base = self.repo / PROJ / "ignition" / "named-query"
        for res in sorted(base.rglob("resource.json")):
            folder = res.parent
            qpath = folder.relative_to(base).as_posix()
            try:
                meta = json.loads(read(res))
            except ValueError:
                meta = {}
            sql = read(folder / "query.sql") if (folder / "query.sql").exists() else ""
            self.queries[qpath] = {"meta": meta.get("attributes", {}), "scope": meta.get("scope", ""), "sql": sql}

    def scan_query_callers(self, gw_scripts, webdev, reports):
        paths = set(self.queries)

        def add(q, kind, caller, where):
            lst = self.nq_callers.setdefault(q, [])
            if (kind, caller, where) not in lst:
                lst.append((kind, caller, where))
        for full, mod in self.modules.items():
            for s, line in mod.strings():
                cands = [s] + [p + s for p in mod.prefixes]
                for c in cands:
                    if c in paths:
                        add(c, "script", full + "." + mod.func_at(line), "")
        quoted = {q: re.compile(r"['\"]" + re.escape(q) + r"['\"]") for q in paths}
        for vpath, leaves in self.view_texts:
            for comp, where, s in leaves:
                if s in paths:
                    add(s, "view", vpath, ("%s %s" % (comp, where)).strip())
                elif "/" in s and len(s) > 20:
                    for q, rx in quoted.items():
                        if rx.search(s):
                            add(q, "view", vpath, ("%s %s" % (comp, where)).strip())
        for kind, name, meta, files in gw_scripts:
            for f, s in files.items():
                for q, rx in quoted.items():
                    if rx.search(s):
                        add(q, "gateway " + kind, name, f)
        for name, cfg, methods in webdev:
            for mname, s in methods.items():
                for q, rx in quoted.items():
                    if rx.search(s):
                        add(q, "webdev", name, mname)


def _xml_unescape(s):
    return (s.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'")
            .replace("&#13;", "").replace("&amp;", "&"))


# ---------------------------------------------------------------------------------------------- tag event scripts
def tag_event_scripts(repo: Path):
    out = []
    roots = [repo / CORE / "ignition" / "tag-definition", repo / CORE / "ignition" / "tag-type-definition"]
    for root in roots:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.json")):
            if "_RCP1_" in p.parts or p.name.lower().startswith("lightspeeddefault"):
                continue
            txt = read(p)
            if "eventScripts" not in txt:
                continue
            try:
                data = json.loads(txt)
            except ValueError:
                continue
            base = p.parent.relative_to(root).as_posix()

            def walk(o, path):
                if isinstance(o, dict):
                    nm = o.get("name")
                    here = path + "/" + nm if isinstance(nm, str) else path
                    for e in o.get("eventScripts") or []:
                        if isinstance(e, dict):
                            out.append((root.name, here.strip("/"), e.get("eventid", ""), e.get("script", "")))
                    for k, v in o.items():
                        if k == "tags":
                            walk(v, here)
                elif isinstance(o, list):
                    for x in o:
                        walk(x, path)
            walk(data, base)
    return out


# ---------------------------------------------------------------------------------------------- sql schema
def sql_tables(repo: Path):
    tables = []
    base = repo / "sql"
    if not base.exists():
        return tables
    for p in sorted(base.glob("*.sql")):
        src = read(p)
        head = []
        for line in src.splitlines():
            if line.startswith("--"):
                head.append(line[2:].strip())
            elif line.strip():
                break
        for m in re.finditer(r"CREATE\s+TABLE\s+([\w.\[\]]+)\s*\((.*?)\n\s*\);", src, re.S | re.I):
            name = m.group(1).replace("[", "").replace("]", "")
            cols, cons = [], []
            pending = None
            for raw in m.group(2).splitlines():
                line = raw.rstrip()
                if not line.strip():
                    continue
                comment = ""
                if "--" in line:
                    line, comment = line.split("--", 1)
                    comment = comment.strip()
                s = line.strip().rstrip(",")
                if not s:
                    if pending is not None and comment:
                        pending["comment"] = (pending["comment"] + " " + comment).strip()
                    continue
                cm = re.match(r"^([a-z_][\w]*)\s+([A-Z][A-Z0-9]*(?:\s*\([^)]*\))?)(.*)$", s)
                if cm and cm.group(1).upper() != "CONSTRAINT":
                    rest = cm.group(3)
                    pending = {"name": cm.group(1), "type": cm.group(2).replace(" ", ""),
                               "null": "NULL" if re.search(r"\bNOT\s+NULL\b", rest, re.I) is None and
                               re.search(r"\bNULL\b", rest, re.I) else ("NOT NULL" if "NOT NULL" in rest.upper() else ""),
                               "extra": [], "comment": comment}
                    if "IDENTITY" in rest.upper():
                        pending["extra"].append("identity")
                    if "PRIMARY KEY" in rest.upper():
                        pending["extra"].append("PK")
                    cols.append(pending)
                elif s.upper().startswith("CONSTRAINT") and pending is not None and not re.search(
                        r"\b(UNIQUE|FOREIGN|PRIMARY\s+KEY\s*\()", s, re.I):
                    d = re.search(r"DEFAULT\s*\((.*)\)\s*$", s, re.I)
                    if d:
                        pending["extra"].append("default " + d.group(1))
                    if re.search(r"PRIMARY KEY", s, re.I):
                        pending["extra"].append("PK")
                    r = re.search(r"REFERENCES\s+([\w.]+)\s*\(([^)]*)\)(.*)", s, re.I)
                    if r:
                        pending["extra"].append("FK -> %s(%s)%s" % (r.group(1), r.group(2),
                                                                    " cascade" if "CASCADE" in r.group(3).upper() else ""))
                    if comment:
                        pending["comment"] = (pending["comment"] + " " + comment).strip()
                elif s.upper().startswith("CONSTRAINT") or s.upper().startswith("UNIQUE"):
                    cons.append(s)
                elif pending is not None and re.match(r"^(REFERENCES|DEFAULT|NOT NULL|NULL)", s, re.I):
                    pending["extra"].append(s)
            # comment line(s) right above the CREATE TABLE / IF OBJECT_ID block
            before = src[:m.start()].rstrip().splitlines()
            desc = []
            for line in reversed(before):
                t = line.strip()
                if t.startswith("--"):
                    t = t.lstrip("-").strip().lstrip("-").strip()
                    if t:
                        desc.insert(0, t)
                elif t.upper().startswith(("IF OBJECT_ID", "BEGIN")) or not t:
                    if desc:
                        break
                    continue
                else:
                    break
            tables.append({"name": name, "file": rel(repo, p), "cols": cols, "cons": cons, "desc": " ".join(desc)})
        idx = re.findall(r"CREATE\s+(UNIQUE\s+)?(?:NONCLUSTERED\s+)?INDEX\s+(\w+)\s+ON\s+([\w.]+)\s*\(([^)]*)\)"
                         r"(\s*WHERE[^;\n]*)?", src, re.I)
        for uniq, iname, tbl, cols, where in idx:
            for t in tables:
                if t["name"] == tbl:
                    t["cons"].append("%sINDEX %s (%s)%s" % ("UNIQUE " if uniq else "", iname, cols.strip(),
                                                           (" " + where.strip()) if where else ""))
        for am in re.finditer(r"ALTER\s+TABLE\s+([\w.]+)\s+ADD\s+(\w+)\s+([A-Z][A-Z0-9]*(?:\([^)]*\))?)(.*?)(?:;|\nGO)",
                              src, re.S | re.I):
            for t in tables:
                if t["name"] == am.group(1):
                    rest = am.group(4)
                    d = re.search(r"DEFAULT\s*\((.*?)\)", rest, re.I)
                    t["cols"].append({"name": am.group(2), "type": am.group(3), "comment": "added by ALTER TABLE",
                                      "null": "NOT NULL" if "NOT NULL" in rest.upper() else "NULL",
                                      "extra": ["default " + d.group(1)] if d else []})
        tables_file_head = " ".join(head)
        for t in tables:
            if t["file"] == rel(repo, p):
                t["file_head"] = tables_file_head
    return tables


# ---------------------------------------------------------------------------------------------- rendering
def caller_rows(callers, limit=None):
    rows = ["| Caller | Kind | Where |", "|---|---|---|"]
    for kind, caller, where in sorted(callers, key=lambda x: (x[0] != "view", x[1], x[2])):
        rows.append("| %s | %s | %s |" % (code(caller), cell(kind), code(where) if where else ""))
    return "\n".join(rows) + "\n"


def module_slug(full):
    return slug(full)


def render_module(idx: Index, mod: Module) -> str:
    title = mod.full
    out = [front(title, "Script module %s: every function, its docstring and its callers." % mod.full,
                 label=mod.full, pos=None), BANNER, "\n"]
    out.append("**Source:** %s  \n" % code(mod.rel))
    out.append("**Lines:** %d. **Functions:** %d. **Called as:** %s\n\n" % (
        len(mod.src.splitlines()), sum(1 for f in mod.functions if f["kind"] == "def"),
        code(mod.full + ".<function>(...)")))
    if mod.header:
        out.append("## What the source says\n\n" + fence(mod.header) + "\n")
    meta = []
    if mod.apis:
        meta.append("| Ignition APIs used | %s |" % ", ".join(code("system." + a) for a in mod.apis))
    if mod.loggers:
        meta.append("| Logger names | %s |" % ", ".join(code(l) for l in mod.loggers))
    uses = sorted(set(c.split(".")[0] + "." + c.split(".")[1] for c in
                      [m.group(1) + "." + m.group(2) for m in CALL_RE.finditer(mod.src)]
                      if c in idx.modules and c != mod.full))
    if uses:
        meta.append("| Calls modules | %s |" % ", ".join("[%s](./%s.md)" % (u, module_slug(u)) for u in uses))
    used_by = sorted(set(c[1].rsplit(".", 1)[0] for f in mod.functions
                         for c in idx.calls.get(mod.full + "." + f["name"], []) if c[0] == "script"))
    if used_by:
        meta.append("| Called by modules | %s |" % ", ".join(
            "[%s](./%s.md)" % (u, module_slug(u)) if u in idx.modules else code(u) for u in used_by))
    if meta:
        out.append("## At a glance\n\n| | |\n|---|---|\n" + "\n".join(meta) + "\n\n")
    if mod.constants:
        rows = "\n".join("| %s | %s |" % (code(n), code(v)) for n, v in mod.constants)
        out.append(details("Module constants (%d)" % len(mod.constants), "| Name | Value |\n|---|---|\n" + rows + "\n")
                   + "\n")
    # summary table
    out.append("## Functions\n\n| Function | Summary | Callers outside the module |\n|---|---|---|\n")
    for f in mod.functions:
        callers = [c for c in idx.calls.get(mod.full + "." + f["name"], []) if c[0] != "same module"]
        first = (f["doc"] or "").strip().split("\n")[0]
        priv = " (internal)" if f["name"].startswith("_") else ""
        out.append("| [%s](#%s)%s | %s | %d |\n" % (code(f["name"]), slug(f["name"]), priv, cell(first[:160]),
                                                   len(callers)))
    out.append("\n")
    for f in mod.functions:
        out.append(heading(3, f["name"], f["name"]))
        out.append(fence(("def " if f["kind"] == "def" else "") + f["sig"], "python"))
        out.append("Line %d of %s.\n\n" % (f["line"], code(mod.rel)))
        if f["doc"]:
            out.append(fence(f["doc"]) + "\n")
        else:
            out.append("_No docstring._\n\n")
        callers = idx.calls.get(mod.full + "." + f["name"], [])
        ext = [c for c in callers if c[0] != "same module"]
        same = [c for c in callers if c[0] == "same module"]
        if ext:
            body = caller_rows(ext)
            out.append(details("Called from %d place(s) outside the module" % len(ext), body) + "\n"
                       if len(ext) > 8 else "**Callers:**\n\n" + body + "\n")
        elif not f["name"].startswith("_"):
            out.append("_No caller found in views, scripts, events, WebDev or reports (it may be called by "
                       "name from the Designer script console or a dynamic string)._\n\n")
        if same:
            out.append("Used inside the module by: %s\n\n" % ", ".join(sorted(set(code(c[1].rsplit(".", 1)[1])
                                                                                for c in same))))
    return "".join(out)


def render_modules_index(idx: Index) -> str:
    out = [front("Script Library Reference", "Every project script module of the BH project, generated from "
                 "ignition/script-python.", label="Script Modules", pos=2), BANNER, "\n"]
    out.append("All project library modules (Designer: **Project Browser > Scripting > Project Library**). "
               "Path on disk: %s.\n\n" % code(PROJ + "/ignition/script-python/<package>/<Module>/code.py"))
    out.append("| Module | Lines | Functions | External callers | Summary |\n|---|---|---|---|---|\n")
    for full in sorted(idx.modules):
        m = idx.modules[full]
        ncall = sum(len([c for c in idx.calls.get(full + "." + f["name"], []) if c[0] != "same module"])
                    for f in m.functions)
        first = (m.header or "").strip().split("\n")[0]
        out.append("| [%s](./%s.md) | %d | %d | %d | %s |\n" % (full, module_slug(full), len(m.src.splitlines()),
                                                              sum(1 for f in m.functions if f["kind"] == "def"),
                                                              ncall, cell(first[:150])))
    return "".join(out)


def render_gateway(gw, tag_events) -> str:
    out = [front("Gateway Events Reference", "Gateway timer, tag change, message and startup event scripts of the "
                 "BH project, plus tag event scripts.", label="Gateway Events", pos=3), BANNER, "\n"]
    out.append("Designer: **Project Browser > Scripting > Gateway Events** (8.3 stores each event as its own "
               "resource under %s). These scripts run in the **gateway scope**: no Perspective session, no "
               "`self`, `system.perspective` only through session ids.\n\n" % code(PROJ + "/ignition/<kind>/<name>"))
    kinds = {}
    for kind, name, meta, files in gw:
        kinds.setdefault(kind, []).append((name, meta, files))
    for kind in ("startup", "shutdown", "timer", "tag-change", "message", "scheduled"):
        kinds.setdefault(kind, [])
    for kind in sorted(kinds):
        items = kinds[kind]
        out.append("## %s (%d)\n\n" % (esc(kind), len(items)))
        if not items:
            out.append("_None in the project._\n\n")
            continue
        for name, meta, files in items:
            attrs = meta.get("attributes", {})
            out.append("### %s\n\n" % esc(name))
            rows = ["| Setting | Value |", "|---|---|", "| Scope | %s |" % code(meta.get("scope", "")),
                    "| Enabled | %s |" % code(attrs.get("enabled"))]
            for k in ("delay", "fixedDelay", "sharedThread", "changeTypes"):
                if k in attrs:
                    rows.append("| %s | %s |" % (esc(k), code(json.dumps(attrs[k]))))
            if attrs.get("paths"):
                rows.append("| Tag paths | %s |" % "<br/>".join(code(p) for p in attrs["paths"]))
            lm = attrs.get("lastModification", {})
            if lm:
                rows.append("| Last modified | %s by %s |" % (code(lm.get("timestamp")), code(lm.get("actor"))))
            out.append("\n".join(rows) + "\n\n")
            for f, src in files.items():
                out.append("%s:\n\n" % code(f) + fence(src, "python") + "\n")
    out.append("## Tag event scripts (%d)\n\n" % len(tag_events))
    out.append("Scripts on tags or UDT members (Tag Editor > **Events > Value Changed** etc.), found in the "
               "tag-definition / tag-type-definition files (the browsed %s tree is skipped: it has none).\n\n"
               % code("_RCP1_"))
    for root, path, ev, src in tag_events:
        out.append("### %s\n\n| | |\n|---|---|\n| Store | %s |\n| Event | %s |\n\n" % (esc(path), code(root),
                                                                                      code(ev)))
        out.append(fence(src, "python") + "\n")
    return "".join(out)


def render_messages(idx: Index) -> str:
    out = [front("Perspective Messages Reference", "Every Perspective message type: who sends it and which views "
                 "handle it.", label="Perspective Messages", pos=4), BANNER, "\n"]
    out.append("A Perspective **message** is sent with `system.perspective.sendMessage(type, payload, scope)` "
               "(or a menu item / message action) and received by a **message handler** on a view or component "
               "(Designer: select the component > **Configure Scripts > Message Handlers**). Scopes: `view`, "
               "`page`, `session`. Handlers listen on the scopes ticked below.\n\n")
    types = sorted(set(idx.msg_send) | set(idx.msg_handle))
    out.append("| Message type | Senders | Handlers |\n|---|---|---|\n")
    for t in types:
        out.append("| [%s](#%s) | %d | %d |\n" % (code(t), slug(t), len(idx.msg_send.get(t, [])),
                                                 len(idx.msg_handle.get(t, []))))
    out.append("\n")
    for t in types:
        out.append(heading(2, t, t))
        snd = idx.msg_send.get(t, [])
        hnd = idx.msg_handle.get(t, [])
        if snd:
            rows = ["| Sender | Where | Scope |", "|---|---|---|"]
            seen = set()
            for s, w, sc in snd:
                if (s, w, sc) in seen:
                    continue
                seen.add((s, w, sc))
                rows.append("| %s | %s | %s |" % (code(s), code(w) if w else "", code(sc)))
            body = "\n".join(rows) + "\n"
            out.append(details("Senders (%d)" % len(seen), body) + "\n" if len(seen) > 10 else "**Senders:**\n\n" + body + "\n")
        else:
            out.append("_No sender found by the scan (sent from a binding-built menu or a dynamic name)._\n\n")
        if hnd:
            rows = ["| View | Component | Listens on |", "|---|---|---|"]
            for v, c, sc in sorted(hnd):
                rows.append("| %s | %s | %s |" % (code(v), code(c), cell(", ".join(sc) or "none ticked")))
            body = "\n".join(rows) + "\n"
            out.append(details("Handlers (%d)" % len(hnd), body) + "\n" if len(hnd) > 10 else "**Handlers:**\n\n" + body + "\n")
        else:
            out.append("_No handler in the project (a gateway message handler, or a leftover sender)._\n\n")
    return "".join(out)


def render_queries(idx: Index, folder, names) -> str:
    out = [front("Named Queries: %s" % folder, "Named queries under %s/: SQL, parameters and callers." % folder,
                 label=folder), BANNER, "\n"]
    out.append("Designer: **Project Browser > Data > Named Queries > %s**. Files: %s.\n\n" % (
        esc(folder), code(PROJ + "/ignition/named-query/" + folder + "/<Query>/query.sql + resource.json")))
    out.append("| Query | Type | Parameters | Callers |\n|---|---|---|---|\n")
    for q in names:
        a = idx.queries[q]["meta"]
        params = ", ".join(p.get("identifier", "") for p in a.get("parameters", []))
        out.append("| [%s](#%s) | %s | %s | %d |\n" % (code(q), slug(q), code(a.get("type")), code(params),
                                                     len(idx.nq_callers.get(q, []))))
    out.append("\n")
    for q in names:
        info = idx.queries[q]
        a = info["meta"]
        out.append(heading(2, q, q))
        rows = ["| Setting | Value |", "|---|---|",
                "| Path (what callers pass) | %s |" % code(q),
                "| Type | %s |" % code(a.get("type")),
                "| Database | %s |" % code(a.get("database") or "(project default)"),
                "| Enabled | %s |" % code(a.get("enabled")),
                "| Scope | %s |" % code(info["scope"]),
                "| Cache | %s |" % code("%s %s" % (a.get("cacheAmount"), a.get("cacheUnit")) if a.get("cacheEnabled")
                                      else "off"),
                "| Max rows | %s |" % code(a.get("maxReturnSize") if a.get("useMaxReturnSize") else "unlimited")]
        perms = [p for p in a.get("permissions", []) if p.get("role") or p.get("zone")]
        rows.append("| Security | %s |" % (", ".join(code("%s %s" % (p.get("zone"), p.get("role"))) for p in perms)
                                           if perms else "no role / zone restriction (the SQL and the callers check)"))
        out.append("\n".join(rows) + "\n\n")
        ps = a.get("parameters", [])
        if ps:
            out.append("| Parameter | Mode | SQL type |\n|---|---|---|\n")
            for p in ps:
                st = p.get("sqlType")
                out.append("| %s | %s | %s |\n" % (code(":" + p.get("identifier", "")), cell(p.get("type")),
                                                   code(SQLTYPES.get(st, st))))
            out.append("\n")
        out.append(fence(info["sql"], "sql") + "\n")
        callers = idx.nq_callers.get(q, [])
        if callers:
            out.append("**Callers:**\n\n" + caller_rows(callers) + "\n")
        else:
            out.append("_No caller found by the scan._\n\n")
    return "".join(out)


def render_nq_index(idx: Index, folders) -> str:
    out = [front("Named Queries Reference", "All named queries of the BH project, by folder.", label="Named Queries",
                 pos=5), BANNER, "\n"]
    out.append("%d named queries. Every one runs on the database connection `ignition` (MSSQL, see the "
               "Database section).\n\n" % len(idx.queries))
    out.append("| Folder | Queries | Page |\n|---|---|---|\n")
    for f, names in folders.items():
        out.append("| %s | %d | [%s](./%s.md) |\n" % (code(f), len(names), esc(f), slug(f)))
    out.append("\n| Query | Type | Parameters | Callers |\n|---|---|---|---|\n")
    for q in sorted(idx.queries):
        a = idx.queries[q]["meta"]
        out.append("| [%s](./%s.md#%s) | %s | %s | %d |\n" % (code(q), slug(q.split("/")[0]), slug(q),
                                                              code(a.get("type")),
                                                              code(", ".join(p.get("identifier", "")
                                                                             for p in a.get("parameters", []))),
                                                              len(idx.nq_callers.get(q, []))))
    return "".join(out)


def render_webdev(wd) -> str:
    out = [front("WebDev Resources Reference", "WebDev (HTTP endpoint) resources in the BH project.",
                 label="WebDev Resources", pos=6), BANNER, "\n"]
    out.append("WebDev resources are HTTP endpoints served at `/system/webdev/BH/<path>` (Designer: **Project "
               "Browser > Web Dev**). Files: %s.\n\n" % code(PROJ + "/com.inductiveautomation.webdev/resources"))
    out.append("| Resource | Type | Enabled methods | Auth required |\n|---|---|---|---|\n")
    for name, cfg, methods in wd:
        kind = cfg.get("resource-type", "file / folder")
        en = [m for m in sorted(cfg) if isinstance(cfg[m], dict) and cfg[m].get("enabled")]
        auth = [m for m in en if cfg[m].get("require-auth")]
        out.append("| %s | %s | %s | %s |\n" % (code(name), code(kind), ", ".join(code(m) for m in en) or "-",
                                               ", ".join(code(m) for m in auth) or "none"))
    out.append("\n")
    for name, cfg, methods in wd:
        out.append("## %s\n\n" % esc(name))
        out.append("URL: %s\n\n" % code("/system/webdev/BH/" + name))
        en = [m for m in sorted(cfg) if isinstance(cfg[m], dict) and cfg[m].get("enabled")]
        for m in en:
            src = methods.get(m, "")
            if src.strip():
                out.append("%s (require-auth %s, roles %s):\n\n" % (code(m), code(cfg[m].get("require-auth")),
                                                                    code(cfg[m].get("required-roles") or "-"))
                           + fence(src, "python") + "\n")
        if "_probe" in name or "probe" in name.lower():
            out.append(":::warning\nThis looks like a temporary test endpoint. Remove it once it is no longer needed.\n:::\n\n")
    return "".join(out)


def render_reports(reps) -> str:
    out = [front("Reporting Resources Reference", "Reporting module resources (PDF layouts) in the BH project.",
                 label="Reporting Resources", pos=7), BANNER, "\n"]
    out.append("Reports live in %s (Designer: **Project Browser > Reports**). Each `data.bin` is the Ignition "
               "XML serialization of the report (parameters, data sources, layout).\n\n"
               % code(PROJ + "/com.inductiveautomation.reporting/reports"))
    out.append("| Report | Parameters | Data sources | Format |\n|---|---|---|---|\n")
    for r in reps:
        out.append("| %s | %s | %s | %s |\n" % (code(r["name"]), ", ".join(code(p[0]) for p in r["params"]) or "-",
                                               ", ".join(code(s[1]) for s in r["sources"]) or "-",
                                               "XML" if r["xml"] else "binary (Designer-saved)"))
    out.append("\n")
    for r in reps:
        out.append("## %s\n\n" % esc(r["name"]))
        if r["description"]:
            out.append(esc(r["description"]) + "\n\n")
        if not r["xml"]:
            out.append("Saved by the Designer in the binary format: not parsed here.\n\n")
            continue
        if r["params"]:
            out.append("| Parameter | Type | Default |\n|---|---|---|\n" + "".join(
                "| %s | %s | %s |\n" % (code(n), code(t), code(d)) for n, t, d in r["params"]) + "\n")
        for kind, nm, script in r["sources"]:
            out.append("Data source %s (%s):\n\n" % (code(nm), esc(kind)) + fence(script, "python") + "\n")
    return "".join(out)


def render_loggers(idx: Index) -> str:
    out = [front("Logger Names Reference", "Logger names used by the BH scripts (filter the gateway log by these).",
                 label="Logger Names", pos=8), BANNER, "\n"]
    out.append("Filter **Gateway > Status > Diagnostics > Logs** (8.3: **Diagnostics > Logs**) by these names, or "
               "set their level under **Logging Levels**.\n\n| Logger | Module |\n|---|---|\n")
    rows = []
    for full, m in idx.modules.items():
        for l in m.loggers:
            rows.append((l, full))
    for l, full in sorted(rows):
        out.append("| %s | [%s](./modules/%s.md) |\n" % (code(l), full, module_slug(full)))
    return "".join(out)


def render_sql(tables) -> str:
    out = [front("SQL Schema Files Reference", "Tables created by the repo's sql/*.sql scripts, parsed from the "
                 "CREATE TABLE statements.", label="SQL Schema Files", pos=1), BANNER, "\n"]
    out.append("These are the tables the BH project owns in the MSSQL database `ignition`. Each `sql/*.sql` file is "
               "idempotent (`IF OBJECT_ID(...) IS NULL`), so it can be re-applied safely. Tables created by "
               "Ignition itself (historian, alarm journal, audit profiles) are described on the hand-written "
               "pages.\n\n| Table | File | Columns | Purpose |\n|---|---|---|---|\n")
    for t in tables:
        out.append("| [%s](#%s) | %s | %d | %s |\n" % (code(t["name"]), slug(t["name"]), code(t["file"]),
                                                     len(t["cols"]), cell(t["desc"][:150])))
    out.append("\n")
    for t in tables:
        out.append(heading(2, t["name"], t["name"]))
        out.append("Created by %s. %s\n\n" % (code(t["file"]), esc(t["desc"])))
        out.append("| Column | Type | Null | Keys / defaults | Comment |\n|---|---|---|---|---|\n")
        for c in t["cols"]:
            out.append("| %s | %s | %s | %s | %s |\n" % (code(c["name"]), code(c["type"]), cell(c["null"]),
                                                         cell(", ".join(c["extra"])), cell(c["comment"])))
        if t["cons"]:
            out.append("\nConstraints and indexes:\n\n" + "".join("- %s\n" % code(x) for x in t["cons"]))
        out.append("\n")
    return "".join(out)


def render_ref_index(idx, counts) -> str:
    out = [front("Scripting Reference", "Generated reference for the BH scripting layer: modules, gateway events, "
                 "messages, named queries, WebDev, reports.", label="Reference (Generated)", pos=1), BANNER, "\n"]
    out.append("Built from the project files by `wiki/tools/gen_scripting.py`. Use the hand-written pages one level "
               "up to learn how things fit together; use these pages to look up exact names, signatures and "
               "callers.\n\n| Page | Contents |\n|---|---|\n")
    out.append("| [Script Modules](./modules/index.md) | %d modules, %d functions (signature, docstring, callers) |\n"
               % (counts["modules"], counts["functions"]))
    out.append("| [Gateway Events](./gateway-events.md) | %d gateway event scripts, %d tag event scripts |\n"
               % (counts["gateway_events"], counts["tag_events"]))
    out.append("| [Perspective Messages](./messages.md) | %d message types (senders and handlers) |\n"
               % counts["message_types"])
    out.append("| [Named Queries](./named-queries/index.md) | %d named queries (SQL, parameters, callers) |\n"
               % counts["named_queries"])
    out.append("| [WebDev Resources](./webdev.md) | %d WebDev resources |\n" % counts["webdev"])
    out.append("| [Reporting Resources](./reporting.md) | %d report resources |\n" % counts["reports"])
    out.append("| [Logger Names](./loggers.md) | %d logger names |\n" % counts["loggers"])
    out.append("| [SQL Schema Files](../../database/reference/sql-schema.md) | %d tables from sql/*.sql |\n"
               % counts["tables"])
    return "".join(out)


# ---------------------------------------------------------------------------------------------- main
def _clean(dirpath: Path):
    if not dirpath.exists():
        return
    for p in sorted(dirpath.rglob("*"), reverse=True):
        if p.is_file() and (p.suffix in (".md", ".mdx") or p.name == "_category_.json"):
            p.unlink()
        elif p.is_dir() and not any(p.iterdir()):
            p.rmdir()


def main(repo_root=None):
    repo = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
    docs = repo / "wiki" / "docs"
    sref = docs / "scripting" / "reference"
    dref = docs / "database" / "reference"
    for d in (sref, dref):
        _clean(d)
    written = []

    idx = Index(repo)
    idx.load_modules()
    idx.scan_modules()
    idx.scan_views()
    gw = idx.gateway_scripts()
    wd = idx.webdev()
    reps = idx.reports()
    idx.load_queries()
    idx.scan_query_callers(gw, wd, reps)
    tev = tag_event_scripts(repo)
    tables = sql_tables(repo)

    category(sref, "Reference (Generated)", 99, "scripting/reference/index", written)
    category(sref / "modules", "Script Modules", 2, "scripting/reference/modules/index", written)
    write(sref / "modules" / "index.md", render_modules_index(idx), written)
    for full in sorted(idx.modules):
        write(sref / "modules" / (module_slug(full) + ".md"), render_module(idx, idx.modules[full]), written)
    write(sref / "gateway-events.md", render_gateway(gw, tev), written)
    write(sref / "messages.md", render_messages(idx), written)
    folders = {}
    for q in sorted(idx.queries):
        folders.setdefault(q.split("/")[0], []).append(q)
    category(sref / "named-queries", "Named Queries", 5, "scripting/reference/named-queries/index", written)
    write(sref / "named-queries" / "index.md", render_nq_index(idx, folders), written)
    for f, names in folders.items():
        write(sref / "named-queries" / (slug(f) + ".md"), render_queries(idx, f, names), written)
    write(sref / "webdev.md", render_webdev(wd), written)
    write(sref / "reporting.md", render_reports(reps), written)
    write(sref / "loggers.md", render_loggers(idx), written)

    category(dref, "Reference (Generated)", 99, "database/reference/sql-schema", written)
    write(dref / "sql-schema.md", render_sql(tables), written)

    counts = {
        "modules": len(idx.modules),
        "functions": sum(1 for m in idx.modules.values() for f in m.functions if f["kind"] == "def"),
        "gateway_events": len(gw), "tag_events": len(tev),
        "message_types": len(set(idx.msg_send) | set(idx.msg_handle)),
        "named_queries": len(idx.queries), "webdev": len(wd), "reports": len(reps),
        "loggers": len(set(l for m in idx.modules.values() for l in m.loggers)),
        "tables": len(tables), "views_scanned": len(idx.view_texts), "pages": len([p for p in written
                                                                                  if p.suffix == ".md"]),
    }
    write(sref / "index.md", render_ref_index(idx, counts), written)
    counts["pages"] += 1
    for w in idx.warnings:
        print("warning:", w)
    return counts


if __name__ == "__main__":
    print(main(sys.argv[1] if len(sys.argv) > 1 else None))
