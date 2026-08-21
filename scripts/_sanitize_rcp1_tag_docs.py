#!/usr/bin/env python3
"""Sanitize RCP1 tags.json documentation fields bloated by encoding garbage.

Keeps a short usable prefix (#OPC line + ASCII PLC summary). Deletes *.tmp
siblings. Run: python scripts/_sanitize_rcp1_tag_docs.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RCP1 = (
    ROOT
    / "gateways/standard/data/config/resources/core/ignition/tag-definition/default/RCP1"
)

# Documentation longer than this is treated as corrupt / worth rewriting.
MAX_KEEP = 240


def _ascii_prefix(s: str) -> str:
    out = []
    for ch in s:
        o = ord(ch)
        if ch in "\t\n\r":
            out.append(ch)
            continue
        if o < 32 or o > 126:
            break
        out.append(ch)
    return "".join(out).rstrip(" -–—\t")


def clean_documentation(doc: str | None) -> str | None:
    if doc is None:
        return None
    if not isinstance(doc, str):
        return doc
    if len(doc) <= MAX_KEEP and all(ord(c) < 128 for c in doc):
        return doc

    lines = doc.splitlines()
    kept: list[str] = []
    if lines and lines[0].startswith("#OPC:"):
        kept.append(lines[0].strip())
        if len(lines) > 1 and lines[1].lstrip().startswith("PLC "):
            plc = _ascii_prefix(lines[1])
            if plc:
                kept.append(plc)
    elif lines:
        # No OPC header — keep a short ASCII prefix of the whole string
        prefix = _ascii_prefix(doc)
        if prefix:
            kept.append(prefix[:MAX_KEEP])

    # Preserve trailing Devices/… note if present and clean
    for line in reversed(lines[2:] if len(lines) > 2 else []):
        if "Devices " in line and all(ord(c) < 128 for c in line):
            kept.append(line.strip())
            break

    cleaned = "\n".join(kept).strip()
    return cleaned if cleaned else None


def sanitize_file(path: Path) -> tuple[bool, str]:
    before = path.stat().st_size
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        return False, f"skip non-list {path}"

    changed = False
    for tag in data:
        if not isinstance(tag, dict) or "documentation" not in tag:
            continue
        old = tag.get("documentation")
        new = clean_documentation(old if isinstance(old, str) else None)
        if new != old:
            if new is None:
                tag.pop("documentation", None)
            else:
                tag["documentation"] = new
            changed = True

    if not changed:
        return False, f"ok {path.relative_to(ROOT)} ({before} bytes)"

    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    after = path.stat().st_size
    return True, f"fixed {path.relative_to(ROOT)} {before} -> {after} bytes"


def main() -> None:
    if not RCP1.is_dir():
        raise SystemExit(f"missing {RCP1}")

    fixed = 0
    for path in sorted(RCP1.rglob("tags.json")):
        did, msg = sanitize_file(path)
        print(msg)
        if did:
            fixed += 1

    removed_tmp = 0
    for tmp in sorted(RCP1.rglob("*.tmp")):
        print(f"remove {tmp.relative_to(ROOT)} ({tmp.stat().st_size} bytes)")
        tmp.unlink()
        removed_tmp += 1

    print(f"done: fixed {fixed} tags.json, removed {removed_tmp} .tmp")


if __name__ == "__main__":
    main()
