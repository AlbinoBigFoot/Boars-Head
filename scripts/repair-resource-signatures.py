#!/usr/bin/env python3
"""Repair Ignition project resource.json signatures + CAS digests.

Matches Ignition 8.3 Resource.calculateContentDigest / LastModification.calculateSignature.

Failure mode this prevents
--------------------------
Agent/disk edits that change view.json / code.py / stylesheet.css / etc. without updating
`attributes.lastModificationSignature` (or without copying content digests into
`projects/.resources/`) cause Designer pull / gateway load to hit Optional.get() empty →
ProtoSerializationException / ImmutableResourceSerializer "No value present".

Usage
-----
  python scripts/repair-resource-signatures.py           # repair missing/invalid/CAS gaps
  python scripts/repair-resource-signatures.py --all     # recompute every BH resource
  python scripts/repair-resource-signatures.py --check   # report only (exit 1 if issues)
  python scripts/repair-resource-signatures.py --path gateways/standard/data/projects/BH/.../resource.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BH = ROOT / "gateways/standard/data/projects/BH"
RESOURCES_CAS = ROOT / "gateways/standard/data/projects/.resources"
SCOPE_CHAR = {"G": 1, "D": 2, "C": 4, "A": 7, "N": 0}
ZERO_SIG = "0" * 64


def _ints(i: int) -> bytes:
    return struct.pack(">i", i)


def scope_int(scope: str) -> int:
    """Ignition ResourceScope flags — single letter or combined (e.g. DG = Designer|Gateway)."""
    if len(scope) == 1 and scope in SCOPE_CHAR:
        return SCOPE_CHAR[scope]
    value = 0
    for ch in scope:
        if ch not in SCOPE_CHAR:
            raise KeyError(ch)
        value |= SCOPE_CHAR[ch]
    return value


def calculate_signature(resource_dir: Path, rj: dict, *, unary: bool = False) -> str:
    scope = scope_int(rj["scope"])
    version = int(rj["version"])
    restricted = bool(rj.get("restricted", False))
    overridable = bool(rj.get("overridable", True))
    documentation = rj.get("documentation")
    if documentation is None:
        documentation = rj.get("description")

    h = hashlib.sha256()
    h.update(_ints(scope))
    if documentation is not None:
        h.update(str(documentation).encode("utf-8"))
    h.update(_ints(version))
    h.update(b"\x01" if unary else b"\x00")
    h.update(b"\x01" if restricted else b"\x00")
    h.update(b"\x01" if overridable else b"\x00")

    for key in sorted(rj.get("files") or []):
        digest = hashlib.sha256((resource_dir / key).read_bytes()).hexdigest()
        h.update(key.encode("utf-8"))
        h.update(digest.encode("utf-8"))

    attrs = dict(rj.get("attributes") or {})
    for key in sorted(k for k in attrs if k != "lastModificationSignature"):
        h.update(key.encode("utf-8"))
        val = attrs[key]
        if isinstance(val, dict) and "actor" in val and "timestamp" in val:
            s = '{"actor":"%s","timestamp":"%s"}' % (val["actor"], val["timestamp"])
        elif isinstance(val, str):
            s = json.dumps(val, ensure_ascii=False)
        elif isinstance(val, bool):
            s = "true" if val else "false"
        elif val is None:
            s = "null"
        else:
            s = json.dumps(val, separators=(",", ":"), ensure_ascii=False)
        h.update(s.encode("utf-8"))

    return h.hexdigest()


def ensure_cas(resource_dir: Path, files: list[str]) -> list[str]:
    added = []
    RESOURCES_CAS.mkdir(parents=True, exist_ok=True)
    for name in files:
        src = resource_dir / name
        if not src.is_file():
            raise FileNotFoundError(src)
        digest = hashlib.sha256(src.read_bytes()).hexdigest()
        dest = RESOURCES_CAS / digest
        if not dest.exists():
            shutil.copy2(src, dest)
            added.append(digest)
    return added


def cas_missing(resource_dir: Path, files: list[str]) -> list[str]:
    missing = []
    for name in files:
        src = resource_dir / name
        if not src.is_file():
            missing.append(f"missing-file:{name}")
            continue
        digest = hashlib.sha256(src.read_bytes()).hexdigest()
        if not (RESOURCES_CAS / digest).exists():
            missing.append(f"cas:{name}={digest[:16]}")
    return missing


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def needs_repair(resource_json: Path, rj: dict | None = None) -> tuple[bool, list[str]]:
    """Return (needs_repair, reasons)."""
    if rj is None:
        rj = _read_json(resource_json)
    reasons: list[str] = []
    attrs = rj.get("attributes") or {}
    sig = attrs.get("lastModificationSignature")
    files = list(rj.get("files") or [])

    if not sig:
        reasons.append("missing-signature")
    elif sig == ZERO_SIG:
        reasons.append("zero-signature")
    else:
        try:
            expected = calculate_signature(resource_json.parent, rj, unary=False)
            if sig != expected:
                reasons.append(f"stale-signature:{sig[:12]}!={expected[:12]}")
        except Exception as exc:  # noqa: BLE001 — report and repair
            reasons.append(f"calc-error:{exc}")

    miss = cas_missing(resource_json.parent, files)
    reasons.extend(miss)
    return (bool(reasons), reasons)


def repair(resource_json: Path) -> str:
    resource_dir = resource_json.parent
    rj = _read_json(resource_json)
    attrs = rj.setdefault("attributes", {})
    if "lastModification" not in attrs:
        attrs["lastModification"] = {
            "actor": "external",
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
    files = list(rj.get("files") or [])
    cas_added = ensure_cas(resource_dir, files)
    sig = calculate_signature(resource_dir, rj, unary=False)
    attrs["lastModificationSignature"] = sig
    # Keep key order similar to healthy siblings: signature then lastModification
    ordered = {}
    if "lastModificationSignature" in attrs:
        ordered["lastModificationSignature"] = attrs["lastModificationSignature"]
    if "lastModification" in attrs:
        ordered["lastModification"] = attrs["lastModification"]
    for k, v in attrs.items():
        if k not in ordered:
            ordered[k] = v
    rj["attributes"] = ordered
    resource_json.write_text(json.dumps(rj, indent=2) + "\n", encoding="utf-8")
    return f"sig={sig[:12]}... cas+={len(cas_added)}"


def iter_targets(path: Path | None) -> list[Path]:
    if path is not None:
        p = path if path.is_absolute() else ROOT / path
        if p.name != "resource.json":
            raise SystemExit(f"expected a resource.json path, got: {p}")
        return [p]
    return sorted(BH.rglob("resource.json"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--all", action="store_true", help="recompute every BH resource.json")
    ap.add_argument("--check", action="store_true", help="report issues only; exit 1 if any")
    ap.add_argument("--path", type=Path, help="single resource.json to repair/check")
    args = ap.parse_args()

    targets = iter_targets(args.path)
    issues: list[tuple[Path, list[str]]] = []
    fixed: list[str] = []

    for rj_path in targets:
        rj = _read_json(rj_path)
        dirty, reasons = needs_repair(rj_path, rj)
        if args.all:
            dirty = True
            if not reasons:
                reasons = ["forced"]
        if not dirty:
            continue
        rel = rj_path.relative_to(ROOT).as_posix()
        issues.append((rj_path, reasons))
        if args.check:
            print(f"ISSUE {rel}: {', '.join(reasons)}")
            continue
        info = repair(rj_path)
        fixed.append(f"{rel} ({info})")
        print(f"fixed {rel} ({info}) [{', '.join(reasons)}]")

    if args.check:
        print(f"check: {len(issues)} issue(s) of {len(targets)} resource(s)")
        return 1 if issues else 0

    print(f"done: repaired {len(fixed)} resource(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
