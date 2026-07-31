#!/usr/bin/env python3
"""Final verify: zero standalone AtomicTag memory in Devices target types."""
from __future__ import annotations

import json
from pathlib import Path

DEVICES = Path(
    r"C:\Users\dylan.jones\Documents\Bors\gateways\standard\data\config\resources\core\ignition\tag-type-definition\default\Devices\udts.json"
)
TARGET = {
    "Compressor",
    "Pump",
    "ExhaustFan",
    "Valve",
    "Tank",
    "Sensor",
    "Evaporator",
    "CoolingTower",
}
NESTED = {"Value", "SP", "Metadata"}


def main():
    data = json.loads(DEVICES.read_text(encoding="utf-8"))
    leftovers = []
    counts = {t: {"Digital": 0, "Analog": 0, "Document": 0, "other_root": 0} for t in TARGET}

    def walk(tags, path, under_root: bool):
        for m in tags or []:
            name = m.get("name", "")
            p = f"{path}/{name}" if path else name
            tt = m.get("tagType")
            type_id = m.get("typeId") or ""
            if tt == "AtomicTag":
                if under_root and name in NESTED:
                    continue
                leftovers.append(f"{p} {m.get('dataType')} {m.get('valueSource')}")
                continue
            if type_id == "_Root/Expression" or name == "SummaryInstances":
                continue
            if type_id == "Config/_Alarms":
                continue
            is_root = type_id.startswith("_Root/")
            if is_root:
                base = type_id.split("/", 1)[-1]
                # count at member level using path's device type
                dtype = path.split("/")[0]
                if dtype in counts:
                    if base in counts[dtype]:
                        counts[dtype][base] += 1
                    else:
                        counts[dtype]["other_root"] += 1
            if m.get("tags"):
                walk(m["tags"], p, under_root=is_root)

    for t in data:
        if t["name"] not in TARGET:
            continue
        walk(t.get("tags"), t["name"], False)

    print("=== Root member counts (UdtInstance _Root/*) ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")

    # Count AtomicTags that would have been convertible — should be 0
    print(f"\nLeftover standalone AtomicTags: {len(leftovers)}")
    for line in leftovers[:30]:
        print(" ", line)

    # Instance alarms check
    tag_def = Path(
        r"C:\Users\dylan.jones\Documents\Bors\gateways\standard\data\config\resources\core\ignition\tag-definition\default"
    )
    bad_alarms = []
    flat_limits = []
    for folder in tag_def.iterdir():
        f = folder / "udts.json"
        if not f.exists():
            continue
        data = json.loads(f.read_text(encoding="utf-8"))
        for inst in data:
            if not str(inst.get("typeId", "")).startswith("Devices/"):
                continue
            for m in inst.get("tags") or []:
                if m.get("name") == "_Alarms" and m.get("tagType") != "UdtInstance":
                    bad_alarms.append(f"{folder.name}/{inst['name']}")
                if m.get("name") in ("HiHiLim", "HiLim", "LoLim", "LoLoLim") and m.get("tagType") == "AtomicTag":
                    flat_limits.append(f"{folder.name}/{inst['name']}/{m['name']}")
    print(f"Bad _Alarms AtomicTag: {len(bad_alarms)}")
    print(f"Flat Sensor limits: {len(flat_limits)}")
    if leftovers or bad_alarms or flat_limits:
        raise SystemExit(1)
    print("PASS")


if __name__ == "__main__":
    main()
