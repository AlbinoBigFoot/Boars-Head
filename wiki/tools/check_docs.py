"""Wiki staleness check: what needs updating after a project change?

    python -I wiki/tools/check_docs.py            # report
    python -I wiki/tools/check_docs.py --strict   # exit 1 when anything is stale (for scripts / pre-commit)
    python -I wiki/tools/check_docs.py --all      # also list hand-written pages that are up to date

Three checks:
1. Generated reference. gen_all.py records a SHA-1 of every source file each reference tool read
   (wiki/tools/manifest/sources.json). Files changed, added or removed since then mean that area's
   reference pages are stale: rerun `python -I wiki/tools/gen_all.py`.
2. Hand-written pages. Each guide page lists the repo files it describes in front matter:

       sources:
         - gateways/standard/data/config/resources/core/ignition/tag-group/**/*.json
         - docs/plc-write-lock.md
       last_verified: 2026-10-23

   A page is stale when any source changed after last_verified. The change time of a file is its last
   commit date when the file is tracked and clean, otherwise its modification time (uncommitted edits or
   untracked files).
3. Hygiene. Hand-written pages without sources / last_verified, and sources that match no file.

Stdlib only, UTF-8. Read only: it never edits a page.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
WIKI = TOOLS.parent
REPO = WIKI.parent
DOCS = WIKI / "docs"
MANIFEST = TOOLS / "manifest" / "sources.json"
SKIP_PARTS = {".resources", "node_modules", "__pycache__", ".git"}


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", check=False).stdout
    except OSError:
        return ""


def sha1(p: Path) -> str:
    h = hashlib.sha1()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def expand(pattern: str) -> list[Path]:
    pattern = pattern.strip().lstrip("/")
    if not any(c in pattern for c in "*?["):
        p = REPO / pattern
        return [p] if p.is_file() else (sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else [])
    return sorted(p for p in REPO.glob(pattern)
                  if p.is_file() and not (SKIP_PARTS & set(p.relative_to(REPO).parts)))


# ---------------------------------------------------------------- front matter
def front_matter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    data: dict = {}
    key = None
    for line in text[3:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                data[key] = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
            elif val == "":
                data[key] = []
            else:
                data[key] = val.strip("'\"")
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(m.group(1).strip().strip("'\""))
    return data


def parse_when(val: str) -> dt.datetime | None:
    val = (val or "").strip()
    try:
        d = dt.datetime.fromisoformat(val)
    except ValueError:
        return None
    if d.tzinfo is not None:
        d = d.astimezone().replace(tzinfo=None)
    if len(val) == 10:  # a bare date covers the whole day
        d = d.replace(hour=23, minute=59, second=59)
    return d


# ---------------------------------------------------------------- change times
class ChangeTimes:
    def __init__(self) -> None:
        self.tracked = set(git("ls-files", "-z").split("\0"))
        self.dirty: set[str] = set()
        for entry in git("status", "--porcelain", "-z", "--untracked-files=all").split("\0"):
            if len(entry) > 3:
                self.dirty.add(entry[3:])
        self._commit: dict[str, dt.datetime | None] = {}

    def commit_time(self, rel: str) -> dt.datetime | None:
        if rel not in self._commit:
            out = git("log", "-1", "--format=%cI", "--", rel).strip()
            self._commit[rel] = (dt.datetime.fromisoformat(out).astimezone().replace(tzinfo=None)
                                 if out else None)
        return self._commit[rel]

    def changed(self, p: Path) -> tuple[dt.datetime, str]:
        rel = p.relative_to(REPO).as_posix()
        if rel in self.tracked and rel not in self.dirty:
            t = self.commit_time(rel)
            if t:
                return t, "commit"
        return dt.datetime.fromtimestamp(p.stat().st_mtime), "mtime"


# ---------------------------------------------------------------- checks
def check_generated() -> list[str]:
    out: list[str] = []
    if not MANIFEST.exists():
        return ["  (no manifest yet: run python -I wiki/tools/gen_all.py)"]
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not manifest:
        return ["  (manifest empty: no gen_<area>.py has run yet)"]
    for area, rec in sorted(manifest.items()):
        old: dict[str, str] = rec.get("files", {})
        now: dict[str, Path] = {}
        for pat in rec.get("patterns", []):
            for p in expand(pat):
                now[p.relative_to(REPO).as_posix()] = p
        changed = [r for r, p in now.items() if r in old and sha1(p) != old[r]]
        added = [r for r in now if r not in old]
        removed = [r for r in old if r not in now]
        if not (changed or added or removed):
            out.append(f"  [ok]    {area}: {len(old)} sources unchanged since {rec.get('generated_at')}")
            continue
        out.append(f"  [STALE] {area}: {len(changed)} changed, {len(added)} added, {len(removed)} removed "
                   f"since {rec.get('generated_at')} -> rerun gen_all.py {area}")
        for label, rows in (("changed", changed), ("added", added), ("removed", removed)):
            for r in sorted(rows)[:15]:
                out.append(f"            {label}: {r}")
            if len(rows) > 15:
                out.append(f"            ... {len(rows) - 15} more {label}")
    return out


def main(argv: list[str]) -> int:
    strict, show_all = "--strict" in argv, "--all" in argv
    stale_count = 0

    print("== Generated reference (wiki/tools/manifest/sources.json) ==")
    gen = check_generated()
    print("\n".join(gen))
    stale_count += sum(1 for line in gen if "[STALE]" in line)

    ct = ChangeTimes()
    stale, fresh, missing, unmatched = [], [], [], []
    for page in sorted(DOCS.rglob("*.md*")):
        rel = page.relative_to(WIKI).as_posix()
        fm = front_matter(page.read_text(encoding="utf-8")) or {}
        if str(fm.get("generated", "")).lower() == "true":
            continue
        sources = fm.get("sources") or []
        if isinstance(sources, str):
            sources = [sources]
        verified = parse_when(str(fm.get("last_verified", "")))
        if not sources or verified is None:
            missing.append(f"  {rel}: " + ", ".join(
                x for x, bad in (("sources", not sources), ("last_verified", verified is None)) if bad))
            continue
        newer = []
        for pat in sources:
            files = expand(pat)
            if not files:
                unmatched.append(f"  {rel}: {pat}")
                continue
            for f in files:
                when, how = ct.changed(f)
                if when > verified:
                    newer.append((when, how, f.relative_to(REPO).as_posix()))
        if newer:
            newer.sort(reverse=True)
            lines = [f"  {rel} (last_verified {fm.get('last_verified')}): {len(newer)} source file(s) newer"]
            for when, how, f in newer[:8]:
                lines.append(f"      {when:%Y-%m-%d %H:%M} ({how}) {f}")
            if len(newer) > 8:
                lines.append(f"      ... {len(newer) - 8} more")
            stale.append("\n".join(lines))
        else:
            fresh.append(f"  {rel} (last_verified {fm.get('last_verified')})")

    print("\n== Hand-written pages whose sources changed since last_verified ==")
    print("\n".join(stale) if stale else "  none")
    stale_count += len(stale)
    if show_all:
        print("\n== Up-to-date hand-written pages ==")
        print("\n".join(fresh) if fresh else "  none")
    print("\n== Pages missing sources / last_verified front matter ==")
    print("\n".join(missing) if missing else "  none")
    print("\n== sources entries that match no file ==")
    print("\n".join(unmatched) if unmatched else "  none")

    print(f"\nSummary: {len(stale)} stale page(s), {len(fresh)} current, {len(missing)} without sources, "
          f"{len(unmatched)} dead source pattern(s).")
    if stale_count:
        print("Fix: update the stale pages (then bump last_verified), rerun python -I wiki/tools/gen_all.py, "
              "then cd wiki; npm run build.")
    return 1 if (strict and (stale_count or unmatched)) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
