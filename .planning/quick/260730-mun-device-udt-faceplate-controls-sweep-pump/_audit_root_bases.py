"""Audit Devices UDTs for standalone memory tags vs _Root/* instances."""
from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Users\dylan.jones\Documents\Bors")
DEVICES = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json"
TAG_DEF = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-definition/default"
TARGET_TYPES = {
    "Pump", "ExhaustFan", "Valve", "Tank", "Sensor",
    "Evaporator", "CoolingTower", "Compressor",
}
IGNORE_FOLDER_NAMES = {"Interlock", "Interlocks", "Config"}
IGNORE_LEAF_NAMES = {"_Alarms", "SummaryInstances"}
ROOT_BASES = {"_Root/Analog", "_Root/Digital", "_Root/Multistate", "_Root/Expression", "_Root/Document"}


def suggest_base(node: dict, path: str) -> tuple[str, str]:
    """Return (required_base, suggested_states_or_engUnit)."""
    dt = (node.get("dataType") or "").lower()
    name = node.get("name", "")
    meta = node.get("metadata") or {}
    states = meta.get("states")
    eng = node.get("engUnit") or meta.get("engUnit") or ""
    vs = (node.get("valueSource") or "").lower()

    # Naming heuristics
    nlow = name.lower()
    pl = path.lower()

    if vs == "expr" or "expression" in pl:
        return "_Root/Expression", "keep expr; wrap as Expression instance"

    if dt in ("boolean", "bool"):
        if states:
            labels = ", ".join(f"{s.get('label')}={s.get('value')}" for s in states)
            return "_Root/Digital", f"states: {labels}"
        return "_Root/Digital", "states: Off=0, On=1 (default)"

    if dt in ("int1", "int2", "int4", "int8", "uint2", "uint4"):
        # Status / mode style ints -> Multistate
        if states or any(k in nlow for k in ("status", "sts", "mode", "state", "cmd", "select")):
            if states:
                labels = ", ".join(f"{s.get('label')}={s.get('value')}" for s in states)
                return "_Root/Multistate", f"states: {labels}"
            return "_Root/Multistate", "define states from PLC/metadata"
        # numeric int without states — still usually Multistate or Analog
        if any(k in nlow for k in ("count", "runtime", "hours", "sp", "setpoint", "limit", "pv", "cv")):
            eu = eng or "TBD"
            return "_Root/Analog", f"engUnit: {eu}; dataType Int4"
        return "_Root/Multistate", "likely discrete enum; define states"

    if dt in ("float4", "float8", "double"):
        eu = eng or "TBD"
        return "_Root/Analog", f"engUnit: {eu}"

    if dt == "string":
        return "_Root/Document or keep AtomicTag", "string leaf — often OK as AtomicTag under Config; or Document"

    if dt == "document":
        return "_Root/Document", "document value"

    return f"_Root/? (dataType={dt or 'missing'})", "manual review"


def is_ignored_path(parts: list[str]) -> bool:
    # Ignore Interlock/ folder containers and members under them for structure notes,
    # but still list AtomicTags that are wrong if they're process leaves?
    # User said: Ignore folder containers (Interlock/), `_Alarms` if Config/_Alarms pattern,
    # SummaryInstances if already Expression.
    if not parts:
        return False
    if parts[0] in IGNORE_FOLDER_NAMES and len(parts) == 1:
        return True  # the folder itself
    if "_Alarms" in parts:
        # Config/_Alarms pattern
        return True
    if parts[-1] == "SummaryInstances":
        return True
    return False


def walk_members(tags: list, path_prefix: str = "", parent_type_id: str | None = None):
    """Yield findings for standalone atomic / wrong-shaped members.

    When parent is already a _Root UdtInstance, child Value/SP/etc overrides are expected
    (memory leaves inside the instance) — do NOT flag those as findings.
    """
    for node in tags or []:
        name = node.get("name", "?")
        path = f"{path_prefix}/{name}" if path_prefix else name
        parts = path.split("/")
        tt = node.get("tagType")
        tid = node.get("typeId")
        vs = (node.get("valueSource") or "").lower()
        children = node.get("tags") or []

        # Folder container: recurse, don't flag the folder itself
        if tt == "Folder":
            if name in IGNORE_FOLDER_NAMES or name == "Interlock":
                # still recurse to catch bad leaves inside? User said ignore Interlock/ containers
                # — skip entire Interlock tree
                continue
            yield from walk_members(children, path, parent_type_id=None)
            continue

        # UdtInstance of _Root — correct pattern; overrides of Value inside are OK
        if tt == "UdtInstance":
            if tid and tid.startswith("_Root/"):
                # recurse only to note nested non-_Root? Usually children are Value overrides.
                # Flag if nested child is itself a standalone AtomicTag sibling misuse? No.
                # But flag nested Folder/Atomic that aren't part of base?
                # For Expression SummaryInstances — ignore if Expression
                if name == "SummaryInstances" and tid == "_Root/Expression":
                    continue
                # Optionally scan children for unexpected sibling AtomicTags that aren't Value/Metadata/SP
                known_override_names = {
                    "Value", "Metadata", "SP", "Hi", "Lo", "HiHi", "LoLo",
                    "RawHigh", "RawLow", "ScaledHigh", "ScaledLow",
                    "Deadband", "EU", "EngUnit",
                }
                for child in children:
                    cn = child.get("name", "")
                    ctt = child.get("tagType")
                    # Nested UdtInstance under _Root is unusual
                    if ctt == "UdtInstance":
                        yield {
                            "path": f"{path}/{cn}",
                            "kind": "nested_udt_under_root",
                            "current": f"UdtInstance typeId={child.get('typeId')}",
                            "node": child,
                        }
                    elif ctt == "AtomicTag" and cn not in known_override_names:
                        # Extra atomic under _Root instance — might be OK (SP on Analog) — SP is known
                        # Flag only if it's a process leaf that looks like sibling status
                        pass
                    elif ctt == "Folder":
                        yield from walk_members(child.get("tags") or [], f"{path}/{cn}", parent_type_id=tid)
                continue
            else:
                # UdtInstance of some other type (Devices/X, PLC/X) — note but not primary finding
                yield {
                    "path": path,
                    "kind": "non_root_udt_instance",
                    "current": f"UdtInstance typeId={tid}",
                    "node": node,
                }
                yield from walk_members(children, path, parent_type_id=tid)
                continue

        if tt == "UdtType":
            continue

        if tt == "AtomicTag":
            if is_ignored_path(parts):
                continue
            # SummaryInstances already Expression handled above
            if name == "SummaryInstances":
                continue
            # Standalone memory (or opc/expr) leaf without being inside _Root instance
            if parent_type_id and str(parent_type_id).startswith("_Root/"):
                continue  # shouldn't reach here
            base, suggestion = suggest_base(node, path)
            yield {
                "path": path,
                "kind": "standalone_atomic",
                "current": (
                    f"AtomicTag valueSource={node.get('valueSource') or 'unset'} "
                    f"dataType={node.get('dataType') or 'unset'} "
                    f"engUnit={node.get('engUnit') or '-'} "
                    f"typeId={tid or 'none'}"
                ),
                "required_base": base,
                "suggestion": suggestion,
                "node": node,
            }
            continue

        # Unknown tagType with children
        if children:
            yield from walk_members(children, path, parent_type_id=tid)


def classify_udt(udt: dict):
    name = udt["name"]
    findings = list(walk_members(udt.get("tags") or []))
    # Also inventory correct _Root usage for context
    correct = []

    def inv(tags, prefix=""):
        for n in tags or []:
            p = f"{prefix}/{n['name']}" if prefix else n["name"]
            if n.get("tagType") == "UdtInstance" and (n.get("typeId") or "").startswith("_Root/"):
                correct.append({"path": p, "typeId": n["typeId"]})
            if n.get("tagType") == "Folder" and n.get("name") not in IGNORE_FOLDER_NAMES:
                inv(n.get("tags"), p)
            elif n.get("tagType") == "UdtInstance":
                # don't inventory inside
                pass
            elif n.get("tags"):
                inv(n.get("tags"), p)

    inv(udt.get("tags"))
    return findings, correct


def scan_instance_overrides():
    """Find tag-definition instances that hardcode memory AtomicTags conflicting with UDT shape."""
    issues = []
    for folder in TAG_DEF.iterdir():
        if not folder.is_dir():
            continue
        udts = folder / "udts.json"
        if not udts.exists():
            continue
        data = json.loads(udts.read_text(encoding="utf-8"))
        for inst in data if isinstance(data, list) else [data]:
            type_id = inst.get("typeId", "")
            iname = inst.get("name", "?")
            # Look for AtomicTag overrides at top of instance that duplicate members
            # that should be UdtInstances
            def scan(tags, prefix=""):
                for n in tags or []:
                    p = f"{prefix}/{n['name']}" if prefix else n["name"]
                    tt = n.get("tagType")
                    tid = n.get("typeId")
                    if tt == "AtomicTag":
                        vs = (n.get("valueSource") or "memory").lower()
                        # Instance override of a leaf that looks like it should be a folder/_Root
                        # Heuristic: top-level or mid-level Atomic with Bool/Int/Float and no parent typeId
                        issues.append({
                            "provider_folder": folder.name,
                            "instance": iname,
                            "typeId": type_id,
                            "path": p,
                            "current": (
                                f"AtomicTag valueSource={n.get('valueSource')} "
                                f"dataType={n.get('dataType')} "
                                f"(instance override)"
                            ),
                        })
                    elif tt == "Folder":
                        scan(n.get("tags"), p)
                    elif tt == "UdtInstance":
                        # Overrides inside _Root instance (Value) are OK — note only if
                        # the override replaces entire member with Atomic incorrectly — already Atomic case
                        # Nested children under UdtInstance are Value overrides — skip deep Value
                        for c in n.get("tags") or []:
                            if c.get("tagType") == "AtomicTag" and c.get("name") == "Value":
                                continue  # normal
                            if c.get("tagType") == "AtomicTag":
                                # SP etc OK
                                if c.get("name") in ("SP", "Metadata"):
                                    continue
                                issues.append({
                                    "provider_folder": folder.name,
                                    "instance": iname,
                                    "typeId": type_id,
                                    "path": f"{p}/{c.get('name')}",
                                    "current": (
                                        f"AtomicTag under UdtInstance "
                                        f"valueSource={c.get('valueSource')} dataType={c.get('dataType')}"
                                    ),
                                })
                            elif c.get("tagType") == "Folder":
                                scan(c.get("tags"), f"{p}/{c.get('name')}")

            scan(inst.get("tags"))
    return issues


def main():
    devices = json.loads(DEVICES.read_text(encoding="utf-8"))
    by_name = {u["name"]: u for u in devices}

    report = {
        "types": {},
        "compressor_correct_inventory": [],
        "instance_overrides": [],
    }

    for tname in sorted(TARGET_TYPES):
        udt = by_name.get(tname)
        if not udt:
            report["types"][tname] = {"error": "NOT FOUND in Devices/udts.json"}
            continue
        findings, correct = classify_udt(udt)
        report["types"][tname] = {
            "correct_root_count": len(correct),
            "correct_root": correct,
            "findings": findings,
            "finding_count": len(findings),
        }
        if tname == "Compressor":
            report["compressor_correct_inventory"] = correct

    # Instance overrides — only for Devices-related folders
    all_issues = scan_instance_overrides()
    # Filter to interesting: AtomicTags that are NOT under a path ending with /Value
    # and whose parent member looks like status/analog
    filtered = []
    for i in all_issues:
        p = i["path"]
        # Skip Value overrides under _Root instances — those come from UdtInstance path
        # Our scanner already skips Value under UdtInstance; top-level Atomic is the conflict
        if "/Value" in p and p.endswith("/Value"):
            # could still be wrong if parent isn't UdtInstance — keep if path is Single segment? 
            pass
        filtered.append(i)

    # Cross-check: for each Devices type, which instance Atomic paths match UDT member names
    # that are UdtInstance in the type definition
    udt_root_members = {}
    for tname, udt in by_name.items():
        if tname not in TARGET_TYPES:
            continue
        members = {}

        def collect(tags, prefix=""):
            for n in tags or []:
                p = f"{prefix}/{n['name']}" if prefix else n["name"]
                members[p] = {
                    "tagType": n.get("tagType"),
                    "typeId": n.get("typeId"),
                    "dataType": n.get("dataType"),
                    "valueSource": n.get("valueSource"),
                }
                if n.get("tagType") == "Folder" and n.get("name") not in IGNORE_FOLDER_NAMES:
                    collect(n.get("tags"), p)
                # Don't descend into UdtInstance

        collect(udt.get("tags"))
        udt_root_members[tname] = members

    conflicting = []
    for i in filtered:
        # Map typeId Devices/Pump -> Pump
        tid = i.get("typeId") or ""
        short = tid.split("/")[-1] if tid else ""
        members = udt_root_members.get(short) or {}
        # Check if any UDT member path is prefix of instance path and is UdtInstance,
        # but instance flattened to Atomic at that member
        path = i["path"]
        top = path.split("/")[0]
        um = members.get(top)
        if um and um.get("tagType") == "UdtInstance" and (um.get("typeId") or "").startswith("_Root/"):
            # Instance has AtomicTag at top member name — CONFLICT (replaced UdtInstance with Atomic)
            if path == top or (i["current"].startswith("AtomicTag") and "/" not in path):
                conflicting.append({**i, "udt_expects": f"{um['tagType']} {um.get('typeId')}"})
            elif path == top:
                conflicting.append({**i, "udt_expects": f"{um['tagType']} {um.get('typeId')}"})
        # Also: instance Atomic at path that UDT says should be UdtInstance
        if path in members:
            um2 = members[path]
            if um2.get("tagType") == "UdtInstance" and i["current"].startswith("AtomicTag"):
                conflicting.append({**i, "udt_expects": f"{um2['tagType']} {um2.get('typeId')}"})
        # Instance Atomic for a path whose UDT counterpart is also Atomic (standalone) — note as amplify
        if path in members and members[path].get("tagType") == "AtomicTag":
            conflicting.append({**i, "udt_expects": "AtomicTag (UDT also standalone — fix UDT first)", "note": "amplifies_udt_defect"})

    report["instance_conflicts"] = conflicting
    report["instance_override_raw_count"] = len(filtered)

    # Also dump full member inventory for each type for the markdown
    inventories = {}
    for tname in sorted(TARGET_TYPES):
        udt = by_name.get(tname)
        if not udt:
            continue
        inv = []

        def full(tags, prefix=""):
            for n in tags or []:
                p = f"{prefix}/{n['name']}" if prefix else n["name"]
                entry = {
                    "path": p,
                    "tagType": n.get("tagType"),
                    "typeId": n.get("typeId"),
                    "dataType": n.get("dataType"),
                    "valueSource": n.get("valueSource"),
                    "engUnit": n.get("engUnit"),
                    "states": (n.get("metadata") or {}).get("states"),
                }
                inv.append(entry)
                if n.get("tagType") == "Folder":
                    full(n.get("tags"), p)
                elif n.get("tagType") == "UdtInstance":
                    # list override children briefly
                    for c in n.get("tags") or []:
                        inv.append({
                            "path": f"{p}/{c.get('name')}",
                            "tagType": c.get("tagType"),
                            "typeId": c.get("typeId"),
                            "dataType": c.get("dataType"),
                            "valueSource": c.get("valueSource"),
                            "engUnit": c.get("engUnit"),
                            "states": (c.get("metadata") or {}).get("states"),
                            "note": "override_under_root_instance",
                        })

        full(udt.get("tags"))
        inventories[tname] = inv

    out = ROOT / ".planning/quick/260730-mun-device-udt-faceplate-controls-sweep-pump/_audit_root_bases.json"
    # Strip heavy node blobs from findings for JSON
    slim = json.loads(json.dumps(report, default=str))
    for tname, tdata in slim.get("types", {}).items():
        for f in tdata.get("findings") or []:
            f.pop("node", None)
    out.write_text(json.dumps({"report": slim, "inventories": inventories}, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    for tname in sorted(TARGET_TYPES):
        t = slim["types"].get(tname, {})
        print(f"{tname}: findings={t.get('finding_count')} correct_root={t.get('correct_root_count')}")
    print(f"instance_conflicts={len(conflicting)} raw_overrides={len(filtered)}")


if __name__ == "__main__":
    main()
