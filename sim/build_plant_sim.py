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

FOLDERS = ["Evaporators", "Compressors", "Pumps", "ExhaustFans"]

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


def value_source(path: str, sim_dtype: str) -> str:
    leaf_parent = path.split("/")[-2]
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

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["Time Interval", "Browse Path", "Value Source", "Data Type"],
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(rows)

    shutil.copy2(OUT_CSV, DEVICE_SIM / "instructions.csv")
    print(f"Wrote {OUT_CSV} ({len(rows)} instructions)")
    print(f"Copied to {DEVICE_SIM / 'instructions.csv'}")

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

    total = 0
    for f, data in folder_data.items():
        n = patch_tags(data, f)
        total += n
        (TAG_DEF / f / "udts.json").write_text(
            json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
        print(f"Patched {f}: {n} reference tags")
    print(f"Total reference conversions: {total}")
    print("Sample CSV:")
    for r in rows[:5]:
        print(r)


if __name__ == "__main__":
    main()
