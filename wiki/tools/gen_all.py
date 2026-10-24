"""Regenerate every generated reference page in the wiki, then record what the reference tools read.

    python -I wiki/tools/gen_all.py            # run every gen_<area>.py that exists
    python -I wiki/tools/gen_all.py tags       # run only some areas

Each wiki/tools/gen_<area>.py exposes main(repo_root) and rewrites only its own docs/<area>/reference/**
pages. A reference tool may define SOURCES (a list of repo-relative glob patterns it reads); otherwise the default
patterns below are used. After the run, the source hashes go to wiki/tools/manifest/sources.json, which
check_docs.py compares against the working tree to tell you when the reference is stale.

Stdlib only, UTF-8.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import time
import traceback
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
WIKI = TOOLS.parent
REPO = WIKI.parent
DOCS = WIKI / "docs"
MANIFEST = TOOLS / "manifest" / "sources.json"

GW = "gateways/standard/data"
PROJ = f"{GW}/projects/BH"
CORE = f"{GW}/config/resources/core"

# area -> (module name, default source globs when the module defines no SOURCES)
AREAS: dict[str, tuple[str, list[str]]] = {
    "tags": ("gen_tags", [
        f"{CORE}/ignition/tag-definition/**/*.json",
        f"{CORE}/ignition/tag-type-definition/**/*.json",
        f"{CORE}/ignition/tag-group/**/*.json",
        f"{CORE}/ignition/tag-provider/**/*.json",
    ]),
    "perspective": ("gen_perspective", [
        f"{PROJ}/com.inductiveautomation.perspective/**/*",
        f"{CORE}/com.inductiveautomation.perspective/**/*",
    ]),
    "scripting": ("gen_scripting", [
        f"{PROJ}/ignition/**/*",
        f"{PROJ}/com.inductiveautomation.reporting/**/*",
        f"{PROJ}/com.inductiveautomation.webdev/**/*",
        "sql/**/*.sql",
    ]),
}

SKIP_PARTS = {".resources", "node_modules", "__pycache__", ".git"}


def _expand(patterns: list[str]) -> list[Path]:
    seen: set[Path] = set()
    for pat in patterns:
        for p in REPO.glob(pat):
            if p.is_file() and not (SKIP_PARTS & set(p.relative_to(REPO).parts)):
                seen.add(p)
    return sorted(seen)


def hash_sources(patterns: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for p in _expand(patterns):
        h = hashlib.sha1()
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        out[p.relative_to(REPO).as_posix()] = h.hexdigest()
    return out


def _load(module: str):
    path = TOOLS / f"{module}.py"
    if not path.exists():
        return None
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    spec = importlib.util.spec_from_file_location(module, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def count_generated() -> dict[str, int]:
    counts: dict[str, int] = {}
    for p in DOCS.rglob("*.md*"):
        try:
            head = p.read_text(encoding="utf-8")[:600]
        except OSError:
            continue
        if head.startswith("---") and "\ngenerated: true" in head.split("\n---", 1)[0]:
            area = p.relative_to(DOCS).parts[0]
            counts[area] = counts.get(area, 0) + 1
    return counts


def scrub_generated() -> None:
    """Drop authoring notes from generated pages (see scrub.py)."""
    scrub = _load("scrub").scrub
    for p in DOCS.rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        if text.startswith("---") and "generated: true" in text[:800]:
            new = scrub(text)
            if new != text:
                p.write_text(new, encoding="utf-8", newline=chr(10))


def main(argv: list[str]) -> int:
    wanted = argv or list(AREAS)
    manifest = {}
    if MANIFEST.exists():
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rc = 0
    for area in wanted:
        if area not in AREAS:
            print(f"[skip] unknown area {area!r}; known: {', '.join(AREAS)}")
            continue
        module, default_sources = AREAS[area]
        mod = _load(module)
        if mod is None:
            print(f"[skip] {area}: tools/{module}.py not found")
            continue
        t0 = time.time()
        try:
            result = mod.main(REPO)
        except Exception:  # keep the other reference tools running
            traceback.print_exc()
            print(f"[FAIL] {area}: {module}.main raised")
            rc = 1
            continue
        sources = list(getattr(mod, "SOURCES", None) or default_sources)
        manifest[area] = {
            "module": module,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "patterns": sources,
            "files": hash_sources(sources),
        }
        extra = f" -> {result}" if result not in (None, 0) else ""
        print(f"[ok]   {area}: {module}.main done in {time.time() - t0:.1f}s, "
              f"{len(manifest[area]['files'])} source files hashed{extra}")
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    scrub_generated()
    counts = count_generated()
    total = sum(counts.values())
    print("\nGenerated pages (front matter generated: true):")
    for area in sorted(counts):
        print(f"  {area:<16}{counts[area]:>6}")
    print(f"  {'total':<16}{total:>6}")
    print(f"\nManifest: {MANIFEST.relative_to(REPO).as_posix()}  Next: python -I wiki/tools/check_docs.py; cd wiki; npm run build")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
