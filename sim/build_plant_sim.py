"""Build Programmable Device Simulator CSV + wire plant tags to [default]_Sim_."""
from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAG_DEF = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-definition/default"
DEVICE_SIM = (
    ROOT
    / "gateways/standard/data/config/resources/core/com.inductiveautomation.opcua/device/Sim"
)
OUT_CSV = ROOT / "sim/bh-plant-sim.csv"

FOLDERS = ["Evaporators", "Compressors", "Pumps", "ExhaustFans", "CoolingTowers"]

DTYPE_MAP = {
    "Boolean": "Boolean",
    "Float4": "Float",
    "Float8": "Double",
    "Int4": "Int32",
    "Int2": "Int16",
    "Int8": "Int64",
}


def infer_dtype(path: str, dt: str | None) -> tuple[str, str]:
    if dt and dt in DTYPE_MAP:
        return DTYPE_MAP[dt], dt
    parent = path.split("/")[-2] if "/" in path else ""
    if parent in ("CMD", "Fault"):
        return "Boolean", "Boolean"
    if parent == "Status":
        return "Int32", "Int4"
    return "Float", "Float4"


# Per-EV plant profiles so Overview units look distinct (Status 0–5:
# STOP / CLG / DFT / FLT / MAN / IDLE).
EV_PROFILES: dict[str, dict[str, str]] = {
    # 01–02 STOP/IDLE, fans off, cool room temps
    "EV-01": {
        "Status": "0",
        "Temp": "realistic(38.0, 0.8, 0.04, 0.2, true)",
        "Pressure": "ramp(22.0, 32.0, 90, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-02": {
        "Status": "5",
        "Temp": "realistic(36.0, 0.9, 0.05, 0.22, true)",
        "Pressure": "ramp(24.0, 34.0, 85, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    # 03–06 CLG, fans spinning, colder
    "EV-03": {
        "Status": "1",
        "Temp": "realistic(22.0, 1.0, 0.06, 0.25, true)",
        "Pressure": "ramp(40.0, 55.0, 70, true)",
        "SPD_FBK": "ramp(45.0, 60.0, 50, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-04": {
        "Status": "1",
        "Temp": "realistic(20.0, 1.1, 0.06, 0.25, true)",
        "Pressure": "ramp(42.0, 58.0, 65, true)",
        "SPD_FBK": "ramp(48.0, 62.0, 48, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-05": {
        "Status": "1",
        "Temp": "realistic(18.0, 1.0, 0.05, 0.24, true)",
        "Pressure": "ramp(44.0, 60.0, 72, true)",
        "SPD_FBK": "ramp(50.0, 65.0, 45, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-06": {
        "Status": "1",
        "Temp": "realistic(16.0, 0.9, 0.05, 0.23, true)",
        "Pressure": "ramp(46.0, 62.0, 68, true)",
        "SPD_FBK": "ramp(52.0, 68.0, 42, true)",
        "CMD": "true",
        "Fault": "false",
    },
    # 07–08 DFT, fans off, rising temp
    "EV-07": {
        "Status": "2",
        "Temp": "realistic(42.0, 1.5, 0.08, 0.3, true)",
        "Pressure": "ramp(30.0, 40.0, 80, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-08": {
        "Status": "2",
        "Temp": "realistic(45.0, 1.6, 0.09, 0.32, true)",
        "Pressure": "ramp(28.0, 38.0, 78, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    # 09–10 FLT
    "EV-09": {
        "Status": "3",
        "Temp": "realistic(40.0, 1.2, 0.07, 0.28, true)",
        "Pressure": "ramp(18.0, 28.0, 95, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "true",
    },
    "EV-10": {
        "Status": "3",
        "Temp": "realistic(41.0, 1.3, 0.07, 0.28, true)",
        "Pressure": "ramp(16.0, 26.0, 100, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "true",
    },
    # 11–12 MAN, fans on, mid temps
    "EV-11": {
        "Status": "4",
        "Temp": "realistic(28.0, 1.0, 0.06, 0.25, true)",
        "Pressure": "ramp(35.0, 48.0, 75, true)",
        "SPD_FBK": "ramp(30.0, 50.0, 55, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-12": {
        "Status": "4",
        "Temp": "realistic(30.0, 1.1, 0.06, 0.26, true)",
        "Pressure": "ramp(36.0, 50.0, 73, true)",
        "SPD_FBK": "ramp(35.0, 55.0, 52, true)",
        "CMD": "true",
        "Fault": "false",
    },
    # 13–16 mixed / staggered cycles
    "EV-13": {
        "Status": "list(1, 1, 5, 1, true)",
        "Temp": "realistic(24.0, 1.2, 0.06, 0.25, true)",
        "Pressure": "ramp(38.0, 56.0, 60, true)",
        "SPD_FBK": "ramp(40.0, 58.0, 47, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-14": {
        "Status": "list(5, 0, 5, 1, true)",
        "Temp": "realistic(34.0, 1.0, 0.05, 0.22, true)",
        "Pressure": "ramp(26.0, 36.0, 88, true)",
        "SPD_FBK": "list(0.0, 0.0, 20.0, 0.0, true)",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-15": {
        "Status": "list(0, 5, 0, 1, true)",
        "Temp": "realistic(37.0, 0.9, 0.04, 0.2, true)",
        "Pressure": "ramp(20.0, 30.0, 92, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-16": {
        "Status": "list(1, 2, 1, 1, true)",
        "Temp": "realistic(19.0, 1.4, 0.07, 0.27, true)",
        "Pressure": "ramp(48.0, 68.0, 58, true)",
        "SPD_FBK": "ramp(55.0, 72.0, 40, true)",
        "CMD": "true",
        "Fault": "false",
    },
}


# Per-CT profiles matching Overview copy: CT-01 Run · CT-02 Off · CT-03 Fault.
# Status 0–4: Off / Run / Fault / Manual / Idle. Fan spin on graphic uses Status==1.
CT_PROFILES: dict[str, dict[str, str]] = {
    "CT-01": {
        "Status": "1",
        "Temp": "realistic(78.5, 1.0, 0.05, 0.22, true)",
    },
    "CT-02": {
        "Status": "0",
        "Temp": "realistic(70.0, 0.6, 0.03, 0.15, true)",
    },
    "CT-03": {
        "Status": "2",
        "Temp": "realistic(92.0, 1.4, 0.08, 0.3, true)",
    },
}


def _ev_id(path: str) -> str | None:
    """Return EV-## from Evaporators/EV-##/... browse path."""
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "Evaporators" and parts[1].startswith("EV-"):
        return parts[1]
    return None


def _ct_id(path: str) -> str | None:
    """Return CT-## from CoolingTowers/CT-##/... browse path."""
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "CoolingTowers" and parts[1].startswith("CT-"):
        return parts[1]
    return None


def value_source(path: str, sim_dtype: str) -> str:
    leaf_parent = path.split("/")[-2]
    ev = _ev_id(path)
    if ev and ev in EV_PROFILES:
        profile = EV_PROFILES[ev]
        if leaf_parent in profile:
            return profile[leaf_parent]
    ct = _ct_id(path)
    if ct and ct in CT_PROFILES:
        profile = CT_PROFILES[ct]
        if leaf_parent in profile:
            return profile[leaf_parent]

    if leaf_parent == "Status":
        if path.startswith("Evaporators/"):
            return "list(0, 1, 2, 3, 4, 5, true)"
        return "list(0, 1, 2, true)"
    if leaf_parent == "Temp":
        return "realistic(20.0, 1.2, 0.06, 0.25, true)"
    if leaf_parent == "Pressure":
        return "ramp(20.0, 80.0, 60, true)"
    if leaf_parent == "SPD_FBK":
        return "ramp(0.0, 60.0, 40, true)"
    if leaf_parent in ("CMD", "Fault"):
        return "false"
    if sim_dtype == "Boolean":
        return "false"
    if sim_dtype == "Int32":
        return "0"
    return "0.0"


def collect_leaves(tags, prefix: str, out: list) -> None:
    for t in tags or []:
        name = t["name"]
        path = f"{prefix}/{name}" if prefix else name
        segs = path.split("/")
        if name in ("Overview", "SummaryInstances", "Metadata") or "SummaryInstances" in segs:
            continue
        if t.get("tags"):
            collect_leaves(t.get("tags"), path, out)
        if name == "Value" and t.get("tagType") == "AtomicTag":
            out.append((path, t))


def ensure_folder(tree: dict, parts: list[str]) -> dict:
    node = tree
    for p in parts:
        children = node["children"]
        if p not in children:
            children[p] = {"name": p, "children": {}, "tags": []}
        node = children[p]
    return node


def folder_to_json(node: dict) -> list:
    items = []
    for cname in sorted(node["children"]):
        child = node["children"][cname]
        items.append(
            {
                "name": child["name"],
                "tagType": "Folder",
                "tags": folder_to_json(child) + child["tags"],
            }
        )
    return items


def patch_tags(tags, prefix: str) -> int:
    changed = 0
    for t in tags or []:
        name = t["name"]
        path = f"{prefix}/{name}" if prefix else name
        segs = path.split("/")
        if name in ("Overview", "SummaryInstances", "Metadata") or "SummaryInstances" in segs:
            continue
        if t.get("tags"):
            changed += patch_tags(t["tags"], path)
        if name == "Value" and t.get("tagType") == "AtomicTag":
            t["valueSource"] = "reference"
            t["sourceTagPath"] = f"[default]_Sim_/{path}"
            t.pop("value", None)
            if not t.get("dataType"):
                _, ign_dt = infer_dtype(path, None)
                t["dataType"] = ign_dt
            changed += 1
    return changed


def main() -> None:
    leaves: list[tuple[str, dict]] = []
    folder_data: dict[str, list] = {}
    for f in FOLDERS:
        data = json.loads((TAG_DEF / f / "udts.json").read_text(encoding="utf-8"))
        folder_data[f] = data
        collect_leaves(data, f, leaves)

    print(f"Collected {len(leaves)} leaves")

    rows = []
    for path, tag in leaves:
        sim_dt, _ = infer_dtype(path, tag.get("dataType"))
        rows.append(
            {
                "Time Interval": "0",
                "Browse Path": path,
                "Value Source": value_source(path, sim_dt),
                "Data Type": sim_dt,
            }
        )
    rows.sort(key=lambda r: r["Browse Path"])

    fieldnames = ["Time Interval", "Browse Path", "Value Source", "Data Type"]
    # Gateway Sim device historically uses spaced unquoted headers.
    header_line = "Time Interval, Browse Path, Value Source, Data Type\n"

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        fh.write(header_line)
        writer = csv.DictWriter(fh, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)

    dest = DEVICE_SIM / "instructions.csv"
    shutil.copy2(OUT_CSV, dest)
    print(f"Wrote {OUT_CSV} ({len(rows)} instructions)")
    print(f"Copied to {dest}")

    tree = {"name": "_Sim_", "children": {}, "tags": []}
    for path, tag in leaves:
        parts = path.split("/")
        parent = ensure_folder(tree, parts[:-1])
        _, ign_dt = infer_dtype(path, tag.get("dataType"))
        parent["tags"].append(
            {
                "name": parts[-1],
                "tagType": "AtomicTag",
                "valueSource": "opc",
                "opcServer": "Ignition OPC UA Server",
                "opcItemPath": "ns=1;s=[Sim]" + "/".join(parts),
                "dataType": ign_dt,
            }
        )

    sim_udts = folder_to_json(tree)
    sim_dir = TAG_DEF / "_Sim_"
    if sim_dir.exists():
        for child in list(sim_dir.iterdir()):
            if child.name == "unary-resource.json":
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    else:
        sim_dir.mkdir(parents=True)

    (sim_dir / "udts.json").write_text(
        json.dumps(sim_udts, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    existing_ur = TAG_DEF / "Evaporators" / "unary-resource.json"
    ur = json.loads(existing_ur.read_text(encoding="utf-8"))
    (sim_dir / "unary-resource.json").write_text(
        json.dumps(ur, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(f"Wrote _Sim_/udts.json top folders: {[x['name'] for x in sim_udts]}")

    # Plant tags stay OPC → ns=1;s=[Sim]<path> (live wiring). _Sim_ mirror
    # above is for optional reference browse; do not rewrite plant Value leaves.
    print("Skipped plant tag reference patch (preserving OPC wiring)")
    print("Sample CSV:")
    for r in rows[:8]:
        print(r)


if __name__ == "__main__":
    main()
