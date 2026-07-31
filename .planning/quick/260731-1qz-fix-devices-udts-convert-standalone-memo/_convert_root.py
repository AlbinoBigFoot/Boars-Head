#!/usr/bin/env python3
"""Convert Devices UDT standalone AtomicTag memory leaves to _Root bases."""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\dylan.jones\Documents\Bors")
DEVICES_UDT = (
    ROOT
    / "gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json"
)
TAG_DEF = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-definition/default"

OFF_ON_STATES = [
    {"label": "Off", "value": 0},
    {"label": "On", "value": 1},
]

# Keep nested AtomicTags that already live under a _Root UdtInstance (Value/SP/Metadata)
NESTED_LEAF_NAMES = {"Value", "SP", "Metadata"}

TARGET_TYPES = {
    "Compressor",
    "Pump",
    "ExhaustFan",
    "Valve",
    "Tank",
    "Sensor",
    "Evaporator",
    "CoolingTower",
}


def make_digital(atomic: dict) -> dict:
    meta = copy.deepcopy(atomic.get("metadata") or {})
    meta.setdefault("shortDescription", atomic.get("name", ""))
    meta.setdefault("longDescription", meta.get("shortDescription", ""))
    meta["states"] = copy.deepcopy(OFF_ON_STATES)
    value_tag: dict = {
        "valueSource": atomic.get("valueSource", "memory"),
        "metadata": meta,
        "dataType": "Boolean",
        "name": "Value",
        "tagType": "AtomicTag",
    }
    if "value" in atomic:
        value_tag["value"] = atomic["value"]
    if "alarms" in atomic:
        value_tag["alarms"] = copy.deepcopy(atomic["alarms"])
    # history props commonly on Digital Value
    for k in (
        "historyEnabled",
        "historyProvider",
        "historicalDeadbandMode",
        "historicalDeadbandStyle",
        "historicalDeadband",
        "sampleMode",
    ):
        if k in atomic:
            value_tag[k] = atomic[k]
    out: dict = {
        "name": atomic["name"],
        "typeId": "_Root/Digital",
        "tagType": "UdtInstance",
        "tags": [value_tag],
    }
    if atomic.get("metadata"):
        out["metadata"] = {
            "shortDescription": meta.get("shortDescription", ""),
            "longDescription": meta.get("longDescription", ""),
        }
    return out


def make_analog(atomic: dict) -> dict:
    meta = copy.deepcopy(atomic.get("metadata") or {})
    meta.setdefault("shortDescription", atomic.get("name", ""))
    meta.setdefault("longDescription", meta.get("shortDescription", ""))
    value_tag: dict = {
        "name": "Value",
        "dataType": atomic.get("dataType", "Float4"),
        "valueSource": atomic.get("valueSource", "memory"),
        "tagType": "AtomicTag",
        "metadata": {
            "shortDescription": meta.get("shortDescription", "value"),
            "longDescription": meta.get("longDescription", "value"),
        },
        "historyEnabled": True,
        "historyProvider": "historian",
        "historicalDeadband": 0.01 if atomic.get("dataType") != "Int4" else 0.0,
        "historicalDeadbandMode": "Absolute",
        "historicalDeadbandStyle": "Discrete",
        "sampleMode": "OnChange",
    }
    if "value" in atomic:
        value_tag["value"] = atomic["value"]
    if "engUnit" in atomic:
        value_tag["engUnit"] = atomic["engUnit"]
    if "formatString" in atomic:
        value_tag["formatString"] = atomic["formatString"]
    elif atomic.get("dataType") == "Int4":
        value_tag["formatString"] = "#0"
    else:
        value_tag["formatString"] = "#0.0"
    if "alarms" in atomic:
        value_tag["alarms"] = copy.deepcopy(atomic["alarms"])
    out: dict = {
        "name": atomic["name"],
        "typeId": "_Root/Analog",
        "tagType": "UdtInstance",
        "tags": [value_tag],
    }
    if atomic.get("metadata"):
        out["metadata"] = {
            "shortDescription": meta.get("shortDescription", ""),
            "longDescription": meta.get("longDescription", ""),
        }
    return out


def make_document(atomic: dict) -> dict:
    """String CondTxt → Document with String-typed Value override."""
    meta = copy.deepcopy(atomic.get("metadata") or {})
    meta.setdefault("shortDescription", atomic.get("name", ""))
    meta.setdefault("longDescription", meta.get("shortDescription", ""))
    value_tag: dict = {
        "valueSource": atomic.get("valueSource", "memory"),
        "metadata": {
            "shortDescription": meta.get("shortDescription", "value"),
            "longDescription": meta.get("longDescription", "value"),
        },
        "dataType": "String",
        "name": "Value",
        "tagType": "AtomicTag",
    }
    if "value" in atomic:
        value_tag["value"] = atomic["value"]
    out: dict = {
        "name": atomic["name"],
        "typeId": "_Root/Document",
        "tagType": "UdtInstance",
        "tags": [value_tag],
    }
    if atomic.get("metadata"):
        out["metadata"] = {
            "shortDescription": meta.get("shortDescription", ""),
            "longDescription": meta.get("longDescription", ""),
        }
    return out


def classify(atomic: dict) -> str | None:
    """Return target base name or None to skip."""
    if atomic.get("tagType") != "AtomicTag":
        return None
    # Already has a typeId somehow
    if atomic.get("typeId"):
        return None
    dt = atomic.get("dataType")
    if dt == "Boolean":
        return "Digital"
    if dt in ("Float4", "Float8", "Int1", "Int2", "Int4", "Int8", "Long", "Short", "Byte"):
        return "Analog"
    if dt == "String":
        return "Document"
    # Document-typed standalone rare — skip
    return None


def convert_tags_list(tags: list, stats: dict, under_root_instance: bool = False) -> list:
    out = []
    for m in tags or []:
        tt = m.get("tagType")
        name = m.get("name", "")

        # Folders: convert children only
        if tt == "Folder":
            nm = copy.deepcopy(m)
            nm["tags"] = convert_tags_list(m.get("tags") or [], stats, under_root_instance=False)
            out.append(nm)
            continue

        # Existing UdtInstance — recurse into children but do not convert nested Value/SP/Metadata
        if tt == "UdtInstance":
            nm = copy.deepcopy(m)
            type_id = m.get("typeId") or ""
            is_root = type_id.startswith("_Root/")
            # Keep SummaryInstances / _Alarms as-is structurally; still walk for safety
            if type_id in ("_Root/Expression", "Config/_Alarms") or name == "SummaryInstances":
                # still convert? no — leave Expression/Alarms alone; their children are Value/Metadata
                out.append(nm)
                continue
            if is_root:
                # Do not convert Value/SP/Metadata; leave other unexpected AtomicTags alone under root
                out.append(nm)
                continue
            # Nested device UDT (e.g. Fan → Devices/VFD) — leave as-is (VFD already root-based)
            if m.get("tags"):
                nm["tags"] = convert_tags_list(m.get("tags") or [], stats, under_root_instance=False)
            out.append(nm)
            continue

        if tt == "AtomicTag":
            # Nested leaf under something we already kept? Only convert standalone.
            target = classify(m)
            if target is None:
                out.append(copy.deepcopy(m))
                continue
            if target == "Digital":
                out.append(make_digital(m))
                stats["Digital"] += 1
            elif target == "Analog":
                out.append(make_analog(m))
                stats["Analog"] += 1
            elif target == "Document":
                out.append(make_document(m))
                stats["Document"] += 1
            stats["converted"] += 1
            stats["by_name"][name] = stats["by_name"].get(name, 0) + 1
            continue

        # UdtType or other — deep copy with recursive convert of tags
        nm = copy.deepcopy(m)
        if m.get("tags"):
            nm["tags"] = convert_tags_list(m.get("tags") or [], stats, under_root_instance=False)
        out.append(nm)
    return out


def convert_devices_udt() -> dict:
    data = json.loads(DEVICES_UDT.read_text(encoding="utf-8"))
    stats = {"converted": 0, "Digital": 0, "Analog": 0, "Document": 0, "by_name": {}, "by_type": {}}
    new_types = []
    for t in data:
        name = t.get("name")
        if name not in TARGET_TYPES:
            new_types.append(t)
            continue
        before = stats["converted"]
        nt = copy.deepcopy(t)
        nt["tags"] = convert_tags_list(t.get("tags") or [], stats)
        stats["by_type"][name] = stats["converted"] - before
        new_types.append(nt)
    DEVICES_UDT.write_text(json.dumps(new_types, indent=2) + "\n", encoding="utf-8")
    return stats


def fix_alarms_instance(member: dict) -> dict:
    """Rewrite malformed _Alarms AtomicTag → UdtInstance Config/_Alarms."""
    if member.get("name") != "_Alarms":
        return member
    if member.get("typeId") == "Config/_Alarms" and member.get("tagType") == "UdtInstance":
        # Drop nested memory overrides so type defaults apply
        return {"typeId": "Config/_Alarms", "name": "_Alarms", "tagType": "UdtInstance"}
    if member.get("typeId") == "Config/_Alarms":
        return {"typeId": "Config/_Alarms", "name": "_Alarms", "tagType": "UdtInstance"}
    return member


def convert_instance_atomic(atomic: dict) -> dict:
    """Convert flat AtomicTag override to UdtInstance with Value child."""
    target = classify(atomic)
    if target == "Digital":
        return make_digital(atomic)
    if target == "Analog":
        return make_analog(atomic)
    if target == "Document":
        return make_document(atomic)
    return atomic


LIMIT_NAMES = {"HiHiLim", "HiLim", "LoLim", "LoLoLim"}
KPI_NAMES = {
    "RuntimeHours",
    "MotorStarts",
    "Fail_Timer_PRE",
    "MaxRunTimePerStart",
    "Min_Runtime_Set",
}


def fix_instance_tags(tags: list, stats: dict) -> list:
    out = []
    for m in tags or []:
        name = m.get("name", "")
        if name == "_Alarms":
            fixed = fix_alarms_instance(m)
            if fixed.get("tagType") == "UdtInstance" and m.get("tagType") != "UdtInstance":
                stats["alarms_fixed"] += 1
            out.append(fixed)
            continue

        # Flat Sensor limits / KPI memory overrides → Analog UdtInstance
        if m.get("tagType") == "AtomicTag" and not m.get("typeId"):
            if name in LIMIT_NAMES or name in KPI_NAMES or classify(m):
                # For Sensor limits: user asked to remove flat overrides (inherit UDT)
                if name in LIMIT_NAMES:
                    stats["limits_removed"] += 1
                    continue  # inherit from UDT
                # KPI overrides: convert to nested Analog
                converted = convert_instance_atomic(m)
                if converted is not m:
                    stats["instance_converted"] += 1
                out.append(converted)
                continue

        # Recurse into UdtInstance / Folder children (OPC Value paths stay)
        if m.get("tags") and m.get("tagType") in ("UdtInstance", "Folder"):
            nm = copy.deepcopy(m)
            # Do not recurse into nested device types deeply for Atomic conversion except Value leaves
            nm["tags"] = fix_instance_tags(m.get("tags") or [], stats)
            out.append(nm)
            continue

        out.append(copy.deepcopy(m))
    return out


def fix_tag_definitions() -> dict:
    stats = {"alarms_fixed": 0, "limits_removed": 0, "instance_converted": 0, "files": []}
    for folder in (
        "Pumps",
        "ExhaustFans",
        "Valves",
        "Tanks",
        "Sensors",
        "Evaporators",
        "CoolingTowers",
        "Compressors",
    ):
        path = TAG_DEF / folder / "udts.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        new = []
        for inst in data:
            ni = copy.deepcopy(inst)
            if inst.get("tags"):
                ni["tags"] = fix_instance_tags(inst.get("tags") or [], stats)
            new.append(ni)
        path.write_text(json.dumps(new, indent=2) + "\n", encoding="utf-8")
        stats["files"].append(folder)
    return stats


def verify_devices() -> list[str]:
    """Assert no standalone AtomicTag Float4/Int4/Boolean/String remain (except under _Root Value)."""
    data = json.loads(DEVICES_UDT.read_text(encoding="utf-8"))
    leftovers = []

    def walk(tags, path, under_root_value_parent: bool):
        for m in tags or []:
            name = m.get("name", "")
            p = f"{path}/{name}" if path else name
            tt = m.get("tagType")
            type_id = m.get("typeId") or ""
            if tt == "AtomicTag":
                # Allowed: Value/SP/Metadata under a _Root instance (parent path ends with root member)
                # We pass under_root_value_parent when parent is UdtInstance _Root/*
                if under_root_value_parent and name in NESTED_LEAF_NAMES:
                    continue
                # Also allow Expression Metadata/Value — parent type Expression
                leftovers.append(
                    f"{p} AtomicTag {m.get('dataType')} {m.get('valueSource')} typeId={type_id!r}"
                )
            is_root = type_id.startswith("_Root/")
            # SummaryInstances Expression — children OK
            if type_id == "_Root/Expression" or name == "SummaryInstances":
                continue
            if type_id == "Config/_Alarms":
                continue
            if m.get("tags"):
                walk(m["tags"], p, under_root_value_parent=is_root)

    for t in data:
        if t.get("name") not in TARGET_TYPES:
            continue
        walk(t.get("tags"), t["name"], False)
    return leftovers


def main():
    print("=== Converting Devices UDTs ===")
    stats = convert_devices_udt()
    print(f"Converted members: {stats['converted']}")
    print(f"  Digital: {stats['Digital']}, Analog: {stats['Analog']}, Document: {stats['Document']}")
    print("By type:")
    for k, v in stats["by_type"].items():
        print(f"  {k}: {v}")

    print("\n=== Fixing tag-definition instances ===")
    istats = fix_tag_definitions()
    print(
        f"Alarms fixed: {istats['alarms_fixed']}, "
        f"limits removed: {istats['limits_removed']}, "
        f"instance converted: {istats['instance_converted']}"
    )

    print("\n=== Verify ===")
    leftovers = verify_devices()
    if leftovers:
        print(f"FAIL: {len(leftovers)} leftover AtomicTags:")
        for line in leftovers[:50]:
            print(" ", line)
        if len(leftovers) > 50:
            print(f"  ... +{len(leftovers) - 50} more")
    else:
        print("PASS: zero standalone AtomicTag memory leaves in Devices target types")

    # Write stats for parent
    out_path = DEVICES_UDT.parent / "_convert_stats.json"
    # store next to planning
    out_path = Path(__file__).with_name("CONVERT-STATS.json")
    out_path.write_text(
        json.dumps({"udt": stats, "instances": istats, "leftovers": leftovers}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\nStats written to {out_path}")


if __name__ == "__main__":
    main()
