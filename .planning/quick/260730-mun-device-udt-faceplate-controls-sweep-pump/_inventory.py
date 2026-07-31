"""One-shot inventory for RESEARCH-sim-overviews.md"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\dylan.jones\Documents\Bors")
TAG_DEF = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-definition/default"
PAGES = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages"
)
FACEPLATES = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates"
)
CONTROLS = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Templates/Devices"
)
CSV_PATH = ROOT / "sim/bh-plant-sim.csv"
BUILD = ROOT / "sim/build_plant_sim.py"


def udt_instances(folder: str) -> list[tuple[str, str]]:
    """Return [(name, typeId)] for top-level UDT instances in folder udts.json."""
    path = TAG_DEF / folder / "udts.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    # Ignition 8.3 tag-definition: top-level is a list OR {"tags":[...]}
    tags = data if isinstance(data, list) else (data.get("tags") or [])
    out = []
    for t in tags:
        if t.get("tagType") == "UdtInstance":
            out.append((t["name"], t.get("typeId", "")))
        elif t.get("tagType") == "Folder":
            for c in t.get("tags") or []:
                if c.get("tagType") == "UdtInstance":
                    out.append((f"{t['name']}/{c['name']}", c.get("typeId", "")))
    return out


def _csv_rows():
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        # Headers have leading spaces: " Browse Path"
        fieldmap = {k.strip(): k for k in (reader.fieldnames or [])}
        for row in reader:
            yield {sk: row[rk] for sk, rk in fieldmap.items()}


def csv_instances() -> dict[str, set[str]]:
    instances: dict[str, set[str]] = {}
    for row in _csv_rows():
        bp = row["Browse Path"]
        segs = bp.split("/")
        if len(segs) >= 2:
            instances.setdefault(segs[0], set()).add(segs[1])
    return instances


def csv_leaf_sample(prefix: str, device: str, limit: int = 40):
    leaves = []
    for row in _csv_rows():
        bp = row["Browse Path"]
        if bp.startswith(f"{prefix}/{device}/"):
            rel = bp[len(f"{prefix}/{device}/") :]
            leaves.append(rel)
    return leaves[:limit], len(leaves)


def overview_tag_paths(family: str) -> list[str]:
    view = PAGES / family / "Overview" / "view.json"
    if not view.exists():
        return []
    text = view.read_text(encoding="utf-8")
    return sorted(set(re.findall(r'"tagPath":\s*"(\[default\][^"]+)"', text)))


def find_device_type_in_view(view_path: Path) -> list[str]:
    """Find deviceType props / params in a view.json tree."""
    if not view_path.exists():
        return []
    text = view_path.read_text(encoding="utf-8")
    hits = []
    for m in re.finditer(r'"deviceType"\s*:\s*"([^"]*)"', text):
        hits.append(m.group(1))
    # also params.deviceType binding patterns
    for m in re.finditer(r'"params\.deviceType"[^}]*?"binding"[^}]*?"path"\s*:\s*"([^"]*)"', text):
        hits.append(f"bound:{m.group(1)}")
    return hits


def scan_overview_faceplate_wiring(family: str) -> dict:
    view = PAGES / family / "Overview" / "view.json"
    result = {
        "exists": view.exists(),
        "embedded_paths": [],
        "deviceTypes": [],
        "showAlert": False,
        "openFaceplate": False,
        "onActionPerformed_snippets": [],
    }
    if not view.exists():
        return result
    data = json.loads(view.read_text(encoding="utf-8"))
    text = view.read_text(encoding="utf-8")
    result["deviceTypes"] = find_device_type_in_view(view)
    result["showAlert"] = "showAlert" in text or "Alerts.showAlert" in text
    result["openFaceplate"] = "openFaceplate" in text or "Faceplate.open" in text
    # embedded view paths
    result["embedded_paths"] = sorted(set(re.findall(r'"path":\s*"(01_[^"]+|[^"]*Devices/[^"]+|[^"]*Faceplate[^"]*)"', text)))
    # event scripts mentioning faceplate / deviceType
    for m in re.finditer(r'"script":\s*"((?:[^"\\]|\\.)*)"', text):
        s = m.group(1).encode().decode("unicode_escape") if "\\u" in m.group(1) else m.group(1).replace("\\n", "\n").replace("\\t", "\t")
        if any(k in s for k in ("deviceType", "Faceplate", "showAlert", "openFaceplate", "faceplate")):
            result["onActionPerformed_snippets"].append(s[:500])
    return result


def faceplate_dirs() -> list[str]:
    if not FACEPLATES.exists():
        return []
    return sorted(p.name for p in FACEPLATES.iterdir() if p.is_dir())


def device_template_dirs() -> list[str]:
    if not CONTROLS.exists():
        return []
    return sorted(p.name for p in CONTROLS.iterdir() if p.is_dir())


def build_folders() -> list[str]:
    text = BUILD.read_text(encoding="utf-8")
    m = re.search(r'FOLDERS\s*=\s*\[([^\]]+)\]', text)
    if not m:
        return []
    return re.findall(r'"([^"]+)"', m.group(1))


def main() -> None:
    folders = [
        "Compressors",
        "Pumps",
        "Valves",
        "Tanks",
        "Sensors",
        "ExhaustFans",
        "Evaporators",
        "CoolingTowers",
    ]
    csv_inst = csv_instances()
    print("=== BUILD FOLDERS ===")
    print(build_folders())
    print("=== FACEPLATE DIRS ===")
    print(faceplate_dirs())
    print("=== DEVICE TEMPLATE DIRS ===")
    print(device_template_dirs())
    print()
    for folder in folders:
        print(f"=== {folder} ===")
        inst = udt_instances(folder)
        print(f"  UDT instances ({len(inst)}):")
        for name, tid in inst:
            print(f"    {name}  typeId={tid}")
        csv_names = sorted(csv_inst.get(folder, set()))
        print(f"  CSV devices ({len(csv_names)}): {csv_names}")
        ov_path = PAGES / folder / "Overview"
        print(f"  Overview exists: {ov_path.exists()}")
        tags = overview_tag_paths(folder)
        print(f"  Overview tagPaths ({len(tags)}): {tags}")
        wiring = scan_overview_faceplate_wiring(folder)
        print(f"  deviceTypes: {wiring['deviceTypes']}")
        print(f"  embedded: {wiring['embedded_paths']}")
        print(f"  showAlert={wiring['showAlert']} openFaceplate={wiring['openFaceplate']}")
        if wiring["onActionPerformed_snippets"]:
            for sn in wiring["onActionPerformed_snippets"][:3]:
                print(f"  SCRIPT:\n{sn}\n")
        print()

    # CSV leaf counts per folder
    print("=== CSV LEAF COUNTS BY DEVICE ===")
    counts: dict[str, dict[str, int]] = {}
    for row in _csv_rows():
        segs = row["Browse Path"].split("/")
        if len(segs) >= 2:
            counts.setdefault(segs[0], {})
            counts[segs[0]][segs[1]] = counts[segs[0]].get(segs[1], 0) + 1
    for folder in sorted(counts):
        for dev, n in sorted(counts[folder].items()):
            print(f"  {folder}/{dev}: {n} leaves")

    # Sample COMP-01 and PMP-01 leaves
    print("\n=== SAMPLE LEAVES COMP-01 ===")
    leaves, total = csv_leaf_sample("Compressors", "COMP-01", 80)
    print(f"total={total}")
    for L in leaves:
        print(f"  {L}")
    print("\n=== SAMPLE LEAVES PMP-01 ===")
    leaves, total = csv_leaf_sample("Pumps", "PMP-01", 40)
    print(f"total={total}")
    for L in leaves:
        print(f"  {L}")

    # Overview faceplate params
    print("\n=== OVERVIEW FACEPLATE PARAMS ===")
    for family in folders:
        view = PAGES / family / "Overview" / "view.json"
        if not view.exists():
            print(f"  {family}: MISSING Overview")
            continue
        text = view.read_text(encoding="utf-8")
        fps = sorted(set(re.findall(r'"faceplate":\s*"([^"]*)"', text)))
        paths = sorted(set(re.findall(r'"path":\s*"(02_Components/01_Devices/[^"]+)"', text)))
        print(f"  {family}: faceplate={fps} component={paths}")

    # Device click open target summary
    print("\n=== DEVICE COMPONENT OPEN TARGET ===")
    devices_dir = (
        ROOT
        / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices"
    )
    for d in sorted(devices_dir.iterdir()):
        v = d / "view.json"
        if not v.exists():
            continue
        text = v.read_text(encoding="utf-8")
        uses_unified = "01_Popups/00_Faceplates/Faceplate" in text and "deviceType" in text
        uses_legacy = "01_Popups/00_Faceplates/' + str(faceplate)" in text or '01_Popups/00_Faceplates/" + str(faceplate)' in text
        # simpler detect
        if "deviceType" in text and "Faceplate'" in text.replace('"', "'"):
            mode = "UNIFIED Faceplate + deviceType"
        elif "openPopup" in text:
            mode = "LEGACY openPopup -> 01_Popups/00_Faceplates/<faceplate>"
        else:
            mode = "NO open handler?"
        print(f"  {d.name}: {mode}")

    # Other CSVs
    print("\n=== OTHER CSV FILES ===")
    for p in ROOT.rglob("*.csv"):
        if "node_modules" in str(p) or ".git" in str(p):
            continue
        print(f"  {p.relative_to(ROOT)}")

    displays = ROOT / "Displays"
    if displays.exists():
        csvs = list(displays.rglob("*.csv"))
        print(f"  csv count under Displays/: {len(csvs)}")

    docs = ROOT / "docs"
    for p in docs.rglob("*"):
        if p.suffix.lower() in (".csv", ".xlsx", ".jsonl") and (
            "ft-display" in str(p).lower() or "Display" in p.parts
        ):
            print(f"  docs related: {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
