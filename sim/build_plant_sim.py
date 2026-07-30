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
    if parent in ("CMD", "Fault", "Alm", "Cutout", "Failed", "Started", "Comm"):
        return "Boolean", "Boolean"
    if parent in ("Status", "CP_Mode", "SV_Mode", "Rung", "Color"):
        return "Int32", "Int4"
    return "Float", "Float4"


# Per-EV plant profiles — status wall for Overview demo.
# Evaporator Status enum: 0 Off, 1 Cooling, 2 Defrost, 3 Fault, 4 Manual (not shown), 5 Idle,
# 6 1.PD (Pump Down), 7 2.HG (Hot Gas), 8 3.BLD (Bleed), 9 3.FD (Fan Delay).
# Stages 6-9 display as DFT + stage line on StatusIndicator.
# Comm Loss is NOT a Status int — EV-01 Status/Value has enabled=false (Bad quality) in
# tag-definition Evaporators/udts.json. Do not set enabled=false on the UDT type.
# Temp/SP lives only on device Temp (not _Root/Analog). Defaults: Evap 35°F, CT 85°F,
# Pump 50 gpm, ExhaustFan 1000 cfm, Compressor DisP 25 psi.
# Over-SP AnalogValue red demos: EV-02, CT-01, PMP-01, EFAN-01.
# Compressors demo Status/FLA%/SVP%/CP/SV + DisP/Amps/Rung/Color/bools (PLC-aligned).
# Over-SP AnalogValue red demos: COMP-01 FLA (>70 SP), COMP-02 SVP (>50 SP).
EV_PROFILES: dict[str, dict[str, str]] = {
    # EV-01: Comm Loss via tag enabled=false (sim value unused while disabled)
    "EV-01": {
        "Status": "0",
        "Temp": "realistic(30.0, 0.5, 0.03, 0.15, true)",
        "Pressure": "ramp(22.0, 32.0, 90, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    # EV-02: Cooling + PV > SP (40 > 35) → AnalogValue red
    "EV-02": {
        "Status": "1",
        "Temp": "40.0",
        "Pressure": "ramp(40.0, 55.0, 70, true)",
        "SPD_FBK": "ramp(45.0, 60.0, 50, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-03": {
        "Status": "5",
        "Temp": "realistic(28.0, 0.6, 0.04, 0.18, true)",
        "Pressure": "ramp(24.0, 34.0, 85, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    # EV-04: Defrost stage 1.PD (Pump Down)
    "EV-04": {
        "Status": "6",
        "Temp": "realistic(32.0, 0.8, 0.05, 0.2, true)",
        "Pressure": "ramp(30.0, 40.0, 80, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-05": {
        "Status": "0",
        "Temp": "realistic(29.0, 0.5, 0.03, 0.16, true)",
        "Pressure": "ramp(20.0, 30.0, 92, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-06": {
        "Status": "3",
        "Temp": "realistic(31.0, 0.7, 0.04, 0.18, true)",
        "Pressure": "ramp(18.0, 28.0, 95, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "true",
    },
    # Repeat wall EV-07..11
    "EV-07": {
        "Status": "1",
        "Temp": "realistic(22.0, 1.0, 0.06, 0.25, true)",
        "Pressure": "ramp(42.0, 58.0, 65, true)",
        "SPD_FBK": "ramp(48.0, 62.0, 48, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-08": {
        "Status": "5",
        "Temp": "realistic(27.0, 0.6, 0.04, 0.18, true)",
        "Pressure": "ramp(26.0, 36.0, 88, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    # EV-09: Defrost stage 2.HG (Hot Gas)
    "EV-09": {
        "Status": "7",
        "Temp": "realistic(33.0, 0.8, 0.05, 0.2, true)",
        "Pressure": "ramp(28.0, 38.0, 78, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-10": {
        "Status": "0",
        "Temp": "realistic(30.0, 0.5, 0.03, 0.15, true)",
        "Pressure": "ramp(20.0, 30.0, 90, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-11": {
        "Status": "3",
        "Temp": "realistic(32.0, 0.7, 0.04, 0.18, true)",
        "Pressure": "ramp(16.0, 26.0, 100, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "true",
    },
    # Repeat wall EV-12..16
    "EV-12": {
        "Status": "1",
        "Temp": "realistic(18.0, 1.0, 0.05, 0.24, true)",
        "Pressure": "ramp(44.0, 60.0, 72, true)",
        "SPD_FBK": "ramp(50.0, 65.0, 45, true)",
        "CMD": "true",
        "Fault": "false",
    },
    "EV-13": {
        "Status": "5",
        "Temp": "realistic(26.0, 0.6, 0.04, 0.18, true)",
        "Pressure": "ramp(24.0, 34.0, 85, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    # EV-14: Defrost stage 3.BLD (Bleed) — EV-16 uses 3.FD
    "EV-14": {
        "Status": "8",
        "Temp": "realistic(34.0, 0.8, 0.05, 0.2, true)",
        "Pressure": "ramp(30.0, 40.0, 80, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    "EV-15": {
        "Status": "0",
        "Temp": "realistic(28.0, 0.5, 0.03, 0.15, true)",
        "Pressure": "ramp(22.0, 32.0, 90, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
    # EV-16: Defrost stage 3.FD (Fan Delay) — fault demo stays on EV-06/EV-11
    "EV-16": {
        "Status": "9",
        "Temp": "realistic(31.0, 0.7, 0.04, 0.18, true)",
        "Pressure": "ramp(18.0, 28.0, 95, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
}


# Non-EV Status enum: 0 Off, 1 Run, 2 Fault, 3 Manual (not shown), 4 Idle.
# Four Overview slots → Run / Idle / Fault / Off (no Manual; Comm Loss only on EV-01).
# Fan/pump spin graphics use Status==1 (Run).
CT_PROFILES: dict[str, dict[str, str]] = {
    # CT-01: Run + PV > SP (90 > 85) → AnalogValue red
    "CT-01": {
        "Status": "1",
        "Temp": "90.0",
    },
    "CT-02": {
        "Status": "4",
        "Temp": "realistic(72.0, 0.6, 0.03, 0.15, true)",
    },
    "CT-03": {
        "Status": "2",
        "Temp": "realistic(80.0, 1.0, 0.05, 0.2, true)",
    },
    "CT-04": {
        "Status": "0",
        "Temp": "realistic(68.0, 0.5, 0.03, 0.14, true)",
    },
}

PMP_PROFILES: dict[str, dict[str, str]] = {
    # PMP-01: Run + flow > SP (60 > 50) → AnalogValue red
    "PMP-01": {"Status": "1", "Temp": "60.0"},
    "PMP-02": {"Status": "4", "Temp": "realistic(40.0, 1.0, 0.05, 0.2, true)"},
    "PMP-03": {"Status": "2", "Temp": "realistic(35.0, 1.2, 0.06, 0.22, true)"},
    "PMP-04": {"Status": "0", "Temp": "realistic(20.0, 0.8, 0.04, 0.18, true)"},
}

EFAN_PROFILES: dict[str, dict[str, str]] = {
    # EFAN-01: Run + airflow > SP (1200 > 1000) → AnalogValue red
    "EFAN-01": {"Status": "1", "Temp": "1200.0"},
    "EFAN-02": {"Status": "4", "Temp": "realistic(800.0, 20.0, 0.05, 0.2, true)"},
    "EFAN-03": {"Status": "2", "Temp": "realistic(750.0, 25.0, 0.06, 0.22, true)"},
    "EFAN-04": {"Status": "0", "Temp": "realistic(100.0, 10.0, 0.04, 0.18, true)"},
}

# Faceplate Controls/Config/Interlocks demo leaves (Devices/Compressor flat + Interlock/).
# Keys are relative paths under Compressors/COMP-##/ (not Value-parent names).
COMP_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "OPER": ("true", "Boolean"),
    "MAINT": ("false", "Boolean"),
    "PROG": ("false", "Boolean"),
    "Cmd_Start": ("false", "Boolean"),
    "Cmd_Stop": ("false", "Boolean"),
    "Cmd_Auto": ("false", "Boolean"),
    "Cmd_Manual": ("false", "Boolean"),
    "Cmd_Remote": ("false", "Boolean"),
    "RuntimeHours": ("1247.5", "Float"),
    "MotorStarts": ("382", "Int32"),
    "MaxRunTimePerStart": ("18.5", "Float"),
    "AutoEN": ("true", "Boolean"),
    "Min_Runtime_Set": ("120.0", "Float"),
    "Fail_Timer_PRE": ("30.0", "Float"),
    "Interlock/Sts_IntlkOK": ("false", "Boolean"),
    "Interlock/Sts_NBIntlkOK": ("true", "Boolean"),
    "Interlock/Sts_BypActive": ("false", "Boolean"),
    "Interlock/Sts_FirstOut": ("false", "Boolean"),
    "Interlock/Sts_Intlk": ("6", "Int32"),
    "Interlock/Cfg_Bypassable": ("7", "Int32"),
    "Interlock/OCmd_Reset": ("false", "Boolean"),
    "Interlock/Rdy_Reset": ("true", "Boolean"),
    "Interlock/Cfg_CondTxt00": ("Oil Pressure", "String"),
    "Interlock/Cfg_CondTxt01": ("Discharge Temp", "String"),
    "Interlock/Cfg_CondTxt02": ("Motor OL", "String"),
    "Interlock/Cfg_CondTxt03": ("Emergency Stop", "String"),
}
for _i in range(4, 16):
    COMP_FACEPLATE_DEFAULTS[f"Interlock/Cfg_CondTxt{_i:02d}"] = ("", "String")
for _i in range(16):
    COMP_FACEPLATE_DEFAULTS[f"Interlock/MSet_Bypass{_i:02d}"] = ("false", "Boolean")

COMP_PROFILES: dict[str, dict[str, str]] = {
    # COMP-01: Run; CP Auto / SV Manual — FLA > SP (70)
    "COMP-01": {
        "Status": "1",
        "DisP": "35.0",
        "Amps": "realistic(185.0, 5.0, 0.04, 0.18, true)",
        "FLA": "realistic(78.0, 3.0, 0.05, 0.2, true)",
        "SVP": "realistic(62.0, 4.0, 0.06, 0.22, true)",
        "CP_Mode": "2",
        "SV_Mode": "3",
        "Rung": "1",
        "Color": "1",
        "Alm": "false",
        "Cutout": "false",
        "Failed": "false",
        "Started": "true",
        "Comm": "false",
    },
    # COMP-02: Idle; CP Manual / SV Auto — SVP stays under SP; mild Amps
    "COMP-02": {
        "Status": "4",
        "DisP": "realistic(18.0, 1.0, 0.05, 0.2, true)",
        "Amps": "realistic(42.0, 3.0, 0.04, 0.18, true)",
        "FLA": "realistic(42.0, 3.0, 0.04, 0.18, true)",
        "SVP": "realistic(55.0, 2.0, 0.04, 0.18, true)",
        "CP_Mode": "3",
        "SV_Mode": "2",
        "Rung": "0",
        "Color": "0",
        "Alm": "false",
        "Cutout": "false",
        "Failed": "false",
        "Started": "false",
        "Comm": "false",
    },
    # COMP-03: Fault; CP/SV Remote — Alm + Failed; Cutout color
    "COMP-03": {
        "Status": "2",
        "DisP": "realistic(20.0, 1.2, 0.06, 0.22, true)",
        "Amps": "realistic(12.0, 2.0, 0.05, 0.2, true)",
        "FLA": "realistic(28.0, 2.5, 0.04, 0.18, true)",
        "SVP": "realistic(18.0, 2.0, 0.05, 0.2, true)",
        "CP_Mode": "1",
        "SV_Mode": "1",
        "Rung": "0",
        "Color": "3",
        "Alm": "true",
        "Cutout": "true",
        "Failed": "true",
        "Started": "false",
        "Comm": "false",
    },
    # COMP-04: Off; CP Auto / SV Manual — low but nonzero FLA/SVP
    "COMP-04": {
        "Status": "0",
        "DisP": "realistic(15.0, 0.8, 0.04, 0.18, true)",
        "Amps": "realistic(5.0, 1.0, 0.04, 0.18, true)",
        "FLA": "realistic(8.0, 1.5, 0.04, 0.18, true)",
        "SVP": "realistic(12.0, 2.0, 0.05, 0.2, true)",
        "CP_Mode": "2",
        "SV_Mode": "3",
        "Rung": "0",
        "Color": "0",
        "Alm": "false",
        "Cutout": "false",
        "Failed": "false",
        "Started": "false",
        "Comm": "false",
    },
    # COMP-05: Manual; CP Remote / SV Manual — AntiRec / Starting demo
    "COMP-05": {
        "Status": "3",
        "DisP": "realistic(28.0, 1.0, 0.05, 0.2, true)",
        "Amps": "realistic(95.0, 4.0, 0.05, 0.2, true)",
        "FLA": "realistic(55.0, 3.0, 0.05, 0.2, true)",
        "SVP": "realistic(40.0, 3.0, 0.05, 0.2, true)",
        "CP_Mode": "1",
        "SV_Mode": "3",
        "Rung": "2",
        "Color": "2",
        "Alm": "false",
        "Cutout": "false",
        "Failed": "false",
        "Started": "true",
        "Comm": "false",
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


def _pmp_id(path: str) -> str | None:
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "Pumps" and parts[1].startswith("PMP-"):
        return parts[1]
    return None


def _efan_id(path: str) -> str | None:
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "ExhaustFans" and parts[1].startswith("EFAN-"):
        return parts[1]
    return None


def _comp_id(path: str) -> str | None:
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "Compressors" and parts[1].startswith("COMP-"):
        return parts[1]
    return None


def value_source(path: str, sim_dtype: str) -> str:
    leaf_parent = path.split("/")[-2]
    for getter, profiles in (
        (_ev_id, EV_PROFILES),
        (_ct_id, CT_PROFILES),
        (_pmp_id, PMP_PROFILES),
        (_efan_id, EFAN_PROFILES),
        (_comp_id, COMP_PROFILES),
    ):
        device_id = getter(path)
        if device_id and device_id in profiles:
            profile = profiles[device_id]
            if leaf_parent in profile:
                return profile[leaf_parent]

    if leaf_parent == "Status":
        if path.startswith("Evaporators/"):
            return "list(0, 1, 2, 3, 5, true)"
        return "list(0, 1, 2, 4, true)"
    if leaf_parent in ("CP_Mode", "SV_Mode"):
        return "2"
    if leaf_parent == "Rung":
        return "0"
    if leaf_parent == "Color":
        return "0"
    if leaf_parent == "Temp":
        return "realistic(20.0, 1.2, 0.06, 0.25, true)"
    if leaf_parent == "DisP":
        return "realistic(22.0, 1.2, 0.06, 0.25, true)"
    if leaf_parent == "Amps":
        return "realistic(80.0, 5.0, 0.05, 0.2, true)"
    if leaf_parent == "FLA":
        return "realistic(55.0, 5.0, 0.05, 0.2, true)"
    if leaf_parent == "SVP":
        return "realistic(40.0, 5.0, 0.05, 0.2, true)"
    if leaf_parent == "Pressure":
        return "ramp(20.0, 80.0, 60, true)"
    if leaf_parent == "SPD_FBK":
        return "ramp(0.0, 60.0, 40, true)"
    if leaf_parent in ("CMD", "Fault", "Alm", "Cutout", "Failed", "Started", "Comm"):
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

    # Flat faceplate demo tags live on Devices/Compressor type (memory) and are
    # not present as Value leaves on Compressors instances — emit Sim rows so
    # lab CSV covers Controls/Config/Interlocks paths.
    for comp_id in sorted(COMP_PROFILES):
        for rel, (val, dtype) in COMP_FACEPLATE_DEFAULTS.items():
            rows.append(
                {
                    "Time Interval": "0",
                    "Browse Path": f"Compressors/{comp_id}/{rel}",
                    "Value Source": val,
                    "Data Type": dtype,
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

    SIM_DTYPE = {
        "Boolean": "Boolean",
        "Float": "Float4",
        "Int32": "Int4",
        "Int16": "Int2",
        "String": "String",
    }
    for comp_id in sorted(COMP_PROFILES):
        for rel, (_val, dtype) in COMP_FACEPLATE_DEFAULTS.items():
            path = f"Compressors/{comp_id}/{rel}"
            parts = path.split("/")
            parent = ensure_folder(tree, parts[:-1])
            parent["tags"].append(
                {
                    "name": parts[-1],
                    "tagType": "AtomicTag",
                    "valueSource": "opc",
                    "opcServer": "Ignition OPC UA Server",
                    "opcItemPath": "ns=1;s=[Sim]" + "/".join(parts),
                    "dataType": SIM_DTYPE.get(dtype, "Float4"),
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
