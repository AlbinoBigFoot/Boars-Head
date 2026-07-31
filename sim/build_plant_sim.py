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

FOLDERS = [
    "Evaporators",
    "Compressors",
    "Pumps",
    "ExhaustFans",
    "CoolingTowers",
    "Valves",
    "Tanks",
    "Sensors",
]

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


# Per-EV plant profiles â€” status wall for Overview demo.
# Evaporator Status enum: 0 Off, 1 Cooling, 2 Defrost, 3 Fault, 4 Manual (not shown), 5 Idle,
# 6 1.PD (Pump Down), 7 2.HG (Hot Gas), 8 3.BLD (Bleed), 9 3.FD (Fan Delay).
# Stages 6-9 display as DFT + stage line on StatusIndicator.
# Comm Loss is NOT a Status int â€” EV-01 Status/Value has enabled=false (Bad quality) in
# tag-definition Evaporators/udts.json. Do not set enabled=false on the UDT type.
# Temp/SP is now _Root/Analog under device Temp (path Temp/SP/Value). Defaults: Evap 35F, CT 85F,
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
    # EV-02: Cooling + PV > SP (40 > 35) â†’ AnalogValue red
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
    # EV-14: Defrost stage 3.BLD (Bleed) â€” EV-16 uses 3.FD
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
    # EV-16: Defrost stage 3.FD (Fan Delay) â€” fault demo stays on EV-06/EV-11
    "EV-16": {
        "Status": "9",
        "Temp": "realistic(31.0, 0.7, 0.04, 0.18, true)",
        "Pressure": "ramp(18.0, 28.0, 95, true)",
        "SPD_FBK": "0.0",
        "CMD": "false",
        "Fault": "false",
    },
}



# --- EVAPORATOR ---
# Controls-grade defaults for Devices/Evaporator (CG_RL_Evap enable/defrost/ZAT/Interlock).
# Status wall remains EV_PROFILES above. A-merge wires FOLDERS + CSV emission for these leaves.
# HMI Status stays simplified; PLC Sts_State 0-10 maps in Devices/Evaporator Status metadata.
# Analog/Digital Controls leaves use Member/Value browse paths (OPC Sim style).
EV_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "HMIEnable": ("true", "Boolean"),
    "Cmd_StartDefrost": ("false", "Boolean"),
    "Cmd_StopDefrost": ("false", "Boolean"),
    "Cleanup": ("false", "Boolean"),
    "TooHot/Value": ("false", "Boolean"),
    "TooCold/Value": ("false", "Boolean"),
    "IntlkOK/Value": ("true", "Boolean"),
    "PermOK/Value": ("true", "Boolean"),
    "Off/Value": ("false", "Boolean"),
    "TimeLeft/Value": ("12.0", "Float"),
    "Cfg_PumpOut": ("3.0", "Float"),
    "Cfg_SoftHotGas": ("2.0", "Float"),
    "Cfg_MainHotGas": ("8.0", "Float"),
    "Cfg_Bleed": ("2.0", "Float"),
    "Cfg_FanDelay": ("1.0", "Float"),
    "Cfg_CoolingTime": ("45.0", "Float"),
    "Cfg_ZoneAirTempDB": ("2.0", "Float"),
    "Temp/SP": ("35.0", "Float"),
    "Pressure/SP": ("30.0", "Float"),
    "Interlock/Sts_IntlkOK": ("true", "Boolean"),
    "Interlock/Sts_NBIntlkOK": ("true", "Boolean"),
    "Interlock/Sts_BypActive": ("false", "Boolean"),
    "Interlock/Sts_FirstOut": ("false", "Boolean"),
    "Interlock/Sts_Intlk": ("0", "Int32"),
    "Interlock/Cfg_Bypassable": ("7", "Int32"),
    "Interlock/OCmd_Reset": ("false", "Boolean"),
    "Interlock/Rdy_Reset": ("true", "Boolean"),
    "Interlock/Cfg_CondTxt00": ("Zone Air Temp HiHi", "String"),
    "Interlock/Cfg_CondTxt01": ("Defrost Timeout", "String"),
    "Interlock/Cfg_CondTxt02": ("Fan Fault", "String"),
    "Interlock/Cfg_CondTxt03": ("Permissive Not OK", "String"),
}
for _i in range(4, 16):
    EV_FACEPLATE_DEFAULTS[f"Interlock/Cfg_CondTxt{_i:02d}"] = ("", "String")
for _i in range(16):
    EV_FACEPLATE_DEFAULTS[f"Interlock/MSet_Bypass{_i:02d}"] = ("false", "Boolean")

# EV Controls demo seed (beyond Status/Temp/Pressure/Fans wall profile).
# Keys match FACEPLATE_DEFAULTS relative paths (Value-wrapped for Analog/Digital).
EV_CONTROLS_PROFILES: dict[str, dict[str, str]] = {
    "EV-02": {
        "HMIEnable": "true",
        "TimeLeft/Value": "8.5",
        "TooHot/Value": "true",
        "IntlkOK/Value": "true",
        "PermOK/Value": "true",
        "Cmd_StartDefrost": "false",
        "Cmd_StopDefrost": "false",
    },
    "EV-04": {
        "HMIEnable": "true",
        "TimeLeft/Value": "4.0",
        "Cmd_StartDefrost": "true",
    },
    "EV-06": {
        "HMIEnable": "true",
        "IntlkOK/Value": "false",
        "TimeLeft/Value": "0.0",
    },
}
# --- END EVAPORATOR ---

# --- COOLINGTOWER ---
# Non-EV Status enum: 0 Off, 1 Run, 2 Fault, 3 Manual (not shown), 4 Idle.
# Four Overview slots → Run / Idle / Fault / Off (no Manual; Comm Loss only on EV-01).
# Fan/pump spin graphics use Status==1 (Run).
# Controls-grade defaults (Devices/CoolingTower flat + Interlock/) — A-merge wires CSV.
CT_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "OPER": ("true", "Boolean"),
    "MAINT": ("false", "Boolean"),
    "PROG": ("false", "Boolean"),
    "Cmd_Start": ("false", "Boolean"),
    "Cmd_Stop": ("false", "Boolean"),
    "Cmd_Auto": ("false", "Boolean"),
    "Cmd_Manual": ("false", "Boolean"),
    "RuntimeHours": ("2145.0", "Float"),
    "MotorStarts": ("512", "Int32"),
    "Failed": ("false", "Boolean"),
    "Alm": ("false", "Boolean"),
    "Comm": ("false", "Boolean"),
    "Temp/SP": ("85.0", "Float"),
    "Interlock/Sts_IntlkOK": ("false", "Boolean"),
    "Interlock/Sts_NBIntlkOK": ("true", "Boolean"),
    "Interlock/Sts_BypActive": ("false", "Boolean"),
    "Interlock/Sts_FirstOut": ("false", "Boolean"),
    "Interlock/Sts_Intlk": ("6", "Int32"),
    "Interlock/Cfg_Bypassable": ("7", "Int32"),
    "Interlock/OCmd_Reset": ("false", "Boolean"),
    "Interlock/Rdy_Reset": ("true", "Boolean"),
    "Interlock/Cfg_CondTxt00": ("Basin Level Low", "String"),
    "Interlock/Cfg_CondTxt01": ("Fan VFD Fault", "String"),
    "Interlock/Cfg_CondTxt02": ("Vibration High", "String"),
    "Interlock/Cfg_CondTxt03": ("Emergency Stop", "String"),
}
for _i in range(4, 16):
    CT_FACEPLATE_DEFAULTS[f"Interlock/Cfg_CondTxt{_i:02d}"] = ("", "String")
for _i in range(16):
    CT_FACEPLATE_DEFAULTS[f"Interlock/MSet_Bypass{_i:02d}"] = ("false", "Boolean")

CT_PROFILES: dict[str, dict[str, str]] = {
    # CT-01: Run + PV > SP (90 > 85) → AnalogValue red; Controls demo seed
    "CT-01": {
        "Status": "1",
        "Temp": "90.0",
        "SPD_FBK": "48.0",
        "Failed": "false",
        "Alm": "false",
        "Comm": "false",
        "OPER": "true",
        "MAINT": "false",
        "PROG": "false",
    },
    "CT-02": {
        "Status": "4",
        "Temp": "realistic(72.0, 0.6, 0.03, 0.15, true)",
        "SPD_FBK": "realistic(30.0, 1.5, 0.04, 0.18, true)",
    },
    "CT-03": {
        "Status": "2",
        "Temp": "realistic(80.0, 1.0, 0.05, 0.2, true)",
        "SPD_FBK": "realistic(12.0, 1.0, 0.05, 0.2, true)",
        "Failed": "true",
        "Alm": "true",
    },
    "CT-04": {
        "Status": "0",
        "Temp": "realistic(68.0, 0.5, 0.03, 0.14, true)",
        "SPD_FBK": "realistic(0.5, 0.2, 0.03, 0.14, true)",
    },
}
# --- END COOLINGTOWER ---

# --- PUMP ---
# P_Motor Val_Sts: 0=UNK, 1=STOPPED, 2=RUNNING, 7=STOPPING, 8=STARTING, 33=DISABLED.
PUMP_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "OPER": ("true", "Boolean"),
    "MAINT": ("false", "Boolean"),
    "PROG": ("false", "Boolean"),
    "Cmd_Start": ("false", "Boolean"),
    "Cmd_Stop": ("false", "Boolean"),
    "Cmd_Auto": ("false", "Boolean"),
    "Cmd_Manual": ("false", "Boolean"),
    "Cmd_Reset": ("false", "Boolean"),
    "RuntimeHours": ("412.5", "Float"),
    "MotorStarts": ("96", "Int32"),
    "AutoEN": ("true", "Boolean"),
    "Fail_Timer_PRE": ("30.0", "Float"),
    "Failed": ("false", "Boolean"),
    "Alm": ("false", "Boolean"),
    "Started": ("true", "Boolean"),
    "Comm": ("false", "Boolean"),
    "Flow/SP": ("50.0", "Float"),
    "Interlock/Sts_IntlkOK": ("false", "Boolean"),
    "Interlock/Sts_NBIntlkOK": ("true", "Boolean"),
    "Interlock/Sts_BypActive": ("false", "Boolean"),
    "Interlock/Sts_FirstOut": ("false", "Boolean"),
    "Interlock/Sts_Intlk": ("6", "Int32"),
    "Interlock/Cfg_Bypassable": ("7", "Int32"),
    "Interlock/OCmd_Reset": ("false", "Boolean"),
    "Interlock/Rdy_Reset": ("true", "Boolean"),
    "Interlock/Cfg_CondTxt00": ("Seal Water", "String"),
    "Interlock/Cfg_CondTxt01": ("Discharge Pressure", "String"),
    "Interlock/Cfg_CondTxt02": ("Motor OL", "String"),
    "Interlock/Cfg_CondTxt03": ("Emergency Stop", "String"),
}
for _i in range(4, 16):
    PUMP_FACEPLATE_DEFAULTS[f"Interlock/Cfg_CondTxt{_i:02d}"] = ("", "String")
for _i in range(16):
    PUMP_FACEPLATE_DEFAULTS[f"Interlock/MSet_Bypass{_i:02d}"] = ("false", "Boolean")

PMP_PROFILES: dict[str, dict[str, str]] = {
    "PMP-01": {
        "Status": "2",
        "Flow": "60.0",
        "Failed": "false",
        "Alm": "false",
        "Started": "true",
        "Comm": "false",
        "OPER": "true",
        "MAINT": "false",
        "PROG": "false",
    },
    "PMP-02": {
        "Status": "1",
        "Flow": "realistic(40.0, 1.0, 0.05, 0.2, true)",
        "Started": "false",
    },
    "PMP-03": {
        "Status": "1",
        "Flow": "realistic(35.0, 1.2, 0.06, 0.22, true)",
        "Failed": "true",
        "Alm": "true",
        "Started": "false",
    },
    "PMP-04": {
        "Status": "0",
        "Flow": "realistic(20.0, 0.8, 0.04, 0.18, true)",
        "Started": "false",
    },
}
# --- END PUMP ---

# --- EXHAUSTFAN ---
EXHAUSTFAN_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "OPER": ("true", "Boolean"),
    "MAINT": ("false", "Boolean"),
    "PROG": ("false", "Boolean"),
    "Cmd_Start": ("false", "Boolean"),
    "Cmd_Stop": ("false", "Boolean"),
    "Cmd_Auto": ("false", "Boolean"),
    "Cmd_Manual": ("false", "Boolean"),
    "Cmd_Reset": ("false", "Boolean"),
    "RuntimeHours": ("865.0", "Float"),
    "MotorStarts": ("210", "Int32"),
    "AutoEN": ("true", "Boolean"),
    "Fail_Timer_PRE": ("30.0", "Float"),
    "Failed": ("false", "Boolean"),
    "Alm": ("false", "Boolean"),
    "Started": ("true", "Boolean"),
    "Comm": ("false", "Boolean"),
    "Airflow/SP": ("1000.0", "Float"),
    "Interlock/Sts_IntlkOK": ("false", "Boolean"),
    "Interlock/Sts_NBIntlkOK": ("true", "Boolean"),
    "Interlock/Sts_BypActive": ("false", "Boolean"),
    "Interlock/Sts_FirstOut": ("false", "Boolean"),
    "Interlock/Sts_Intlk": ("6", "Int32"),
    "Interlock/Cfg_Bypassable": ("7", "Int32"),
    "Interlock/OCmd_Reset": ("false", "Boolean"),
    "Interlock/Rdy_Reset": ("true", "Boolean"),
    "Interlock/Cfg_CondTxt00": ("Damper Closed", "String"),
    "Interlock/Cfg_CondTxt01": ("High Temp", "String"),
    "Interlock/Cfg_CondTxt02": ("Motor OL", "String"),
    "Interlock/Cfg_CondTxt03": ("Emergency Stop", "String"),
}
for _i in range(4, 16):
    EXHAUSTFAN_FACEPLATE_DEFAULTS[f"Interlock/Cfg_CondTxt{_i:02d}"] = ("", "String")
for _i in range(16):
    EXHAUSTFAN_FACEPLATE_DEFAULTS[f"Interlock/MSet_Bypass{_i:02d}"] = ("false", "Boolean")

EFAN_PROFILES: dict[str, dict[str, str]] = {
    "EFAN-01": {
        "Status": "2",
        "Airflow": "1200.0",
        "Failed": "false",
        "Alm": "false",
        "Started": "true",
        "Comm": "false",
        "OPER": "true",
        "MAINT": "false",
        "PROG": "false",
    },
    "EFAN-02": {
        "Status": "1",
        "Airflow": "realistic(800.0, 20.0, 0.05, 0.2, true)",
        "Started": "false",
    },
    "EFAN-03": {
        "Status": "1",
        "Airflow": "realistic(750.0, 25.0, 0.06, 0.22, true)",
        "Failed": "true",
        "Alm": "true",
        "Started": "false",
    },
    "EFAN-04": {
        "Status": "0",
        "Airflow": "realistic(100.0, 10.0, 0.04, 0.18, true)",
        "Started": "false",
    },
}
# --- END EXHAUSTFAN ---

# --- VALVE ---
# P_ValveSO Status wall + Controls/Interlock defaults (A-merge wires FOLDERS + CSV).
# Val_Sts: 1=CLOSED, 2=OPEN, 5=CLOSING, 6=OPENING, 33=DISABLED.
VALVE_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "OPER": ("true", "Boolean"),
    "MAINT": ("false", "Boolean"),
    "PROG": ("false", "Boolean"),
    "Cmd_Open": ("false", "Boolean"),
    "Cmd_Close": ("false", "Boolean"),
    "Cmd_Reset": ("false", "Boolean"),
    "OpenLS": ("false", "Boolean"),
    "ClosedLS": ("true", "Boolean"),
    "Failed": ("false", "Boolean"),
    "Comm": ("false", "Boolean"),
    "TravelTime": ("2.5", "Float"),
    "Interlock/Sts_IntlkOK": ("true", "Boolean"),
    "Interlock/Sts_NBIntlkOK": ("true", "Boolean"),
    "Interlock/Sts_BypActive": ("false", "Boolean"),
    "Interlock/Sts_FirstOut": ("false", "Boolean"),
    "Interlock/Sts_Intlk": ("0", "Int32"),
    "Interlock/Cfg_Bypassable": ("3", "Int32"),
    "Interlock/OCmd_Reset": ("false", "Boolean"),
    "Interlock/Rdy_Reset": ("true", "Boolean"),
    "Interlock/Cfg_CondTxt00": ("Open Limit Switch", "String"),
    "Interlock/Cfg_CondTxt01": ("Closed Limit Switch", "String"),
    "Interlock/Cfg_CondTxt02": ("Transit Stall", "String"),
    "Interlock/Cfg_CondTxt03": ("IO Fault", "String"),
}
for _i in range(4, 16):
    VALVE_FACEPLATE_DEFAULTS[f"Interlock/Cfg_CondTxt{_i:02d}"] = ("", "String")
for _i in range(16):
    VALVE_FACEPLATE_DEFAULTS[f"Interlock/MSet_Bypass{_i:02d}"] = ("false", "Boolean")

VALVE_PROFILES: dict[str, dict[str, str]] = {
    # HPRL-ISO: Open + OpenLS
    "HPRL-ISO": {
        "Status": "2",
        "OpenLS": "true",
        "ClosedLS": "false",
        "Failed": "false",
        "TravelTime": "2.5",
    },
    # LTR-SV: Closed + ClosedLS
    "LTR-SV": {
        "Status": "1",
        "OpenLS": "false",
        "ClosedLS": "true",
        "Failed": "false",
        "TravelTime": "2.0",
    },
    # MAIN-LIQ-SV: Fault demo (Failed + intlk not OK)
    "MAIN-LIQ-SV": {
        "Status": "1",
        "OpenLS": "false",
        "ClosedLS": "false",
        "Failed": "true",
        "TravelTime": "3.0",
        "Interlock/Sts_IntlkOK": "false",
        "Interlock/Cfg_CondTxt00": "Main Liquid Permissive",
    },
    # HTR-SV: Opening transit
    "HTR-SV": {
        "Status": "6",
        "OpenLS": "false",
        "ClosedLS": "false",
        "Failed": "false",
        "TravelTime": "2.8",
    },
}
# --- END VALVE ---



# --- SENSOR ---
# Status: 0=OK, 1=HI, 2=LO, 3=HIHI, 4=LOLO, 5=FAIL, 6=BAD (P_AIn aggregate)
# A-merge: add Sensors to FOLDERS and wire these defaults into CSV regen.
SENSOR_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "Cmd_Reset": ("false", "Boolean"),
    "HiHiLim": ("100.0", "Float"),
    "HiLim": ("80.0", "Float"),
    "LoLim": ("20.0", "Float"),
    "LoLoLim": ("5.0", "Float"),
    "HiHi": ("false", "Boolean"),
    "Hi": ("false", "Boolean"),
    "Lo": ("false", "Boolean"),
    "LoLo": ("false", "Boolean"),
    "Fail": ("false", "Boolean"),
}

SENSOR_PROFILES: dict[str, dict[str, str]] = {
    "LSS-PT": {
        "Status": "0",
        "Value": "realistic(28.5, 0.8, 0.04, 0.18, true)",
        "Hi": "false",
        "Lo": "false",
        "Fail": "false",
        "HiLim": "45.0",
        "LoLim": "15.0",
    },
    "HSS-PT": {
        "Status": "1",
        "Value": "52.0",
        "Hi": "true",
        "Lo": "false",
        "Fail": "false",
        "HiLim": "50.0",
        "LoLim": "20.0",
    },
    "HPR-PT": {
        "Status": "2",
        "Value": "12.0",
        "Hi": "false",
        "Lo": "true",
        "Fail": "false",
        "HiLim": "150.0",
        "LoLim": "25.0",
    },
    "OIL-TT": {
        "Status": "5",
        "Value": "0.0",
        "Hi": "false",
        "Lo": "false",
        "Fail": "true",
        "HiLim": "140.0",
        "LoLim": "60.0",
        "HiHiLim": "180.0",
        "LoLoLim": "40.0",
    },
}
# --- END SENSOR ---

# --- TANK ---
# Controls-grade sim profiles for Devices/Tank (A-merge wires FOLDERS + CSV).
TANK_FACEPLATE_DEFAULTS: dict[str, tuple[str, str]] = {
    "Level/SP": ("50.0", "Float"),
    "HH/SP": ("95.0", "Float"),
    "H/SP": ("80.0", "Float"),
    "L/SP": ("20.0", "Float"),
    "LL/SP": ("5.0", "Float"),
    "Pressure/Value": ("18.0", "Float"),
    "Interlock/Sts_IntlkOK": ("true", "Boolean"),
    "Interlock/OCmd_Reset": ("false", "Boolean"),
    "Interlock/Rdy_Reset": ("true", "Boolean"),
    "Interlock/Cfg_CondTxt00": ("Low Level Cutout", "String"),
    "Interlock/Cfg_CondTxt01": ("High Level Cutout", "String"),
    "Interlock/Cfg_CondTxt02": ("Level Transmitter", "String"),
    "Interlock/Cfg_CondTxt03": ("Vessel Pressure", "String"),
}

TANK_PROFILES: dict[str, dict[str, str]] = {
    # LTR-01: OK mid-level — Overview normal
    "LTR-01": {
        "Status": "0",
        "Level": "55.0",
        "Pressure": "18.5",
        "LSH": "false",
        "LSL": "false",
        "HH": "false",
        "H": "false",
        "L": "false",
        "LL": "false",
    },
    # LTR-02: HIGH — LSH + H
    "LTR-02": {
        "Status": "2",
        "Level": "82.0",
        "Pressure": "19.0",
        "LSH": "true",
        "LSL": "false",
        "H": "true",
        "HH": "false",
        "L": "false",
        "LL": "false",
    },
    # LTR-03: LOW — LSL + L
    "LTR-03": {
        "Status": "1",
        "Level": "18.0",
        "Pressure": "17.0",
        "LSH": "false",
        "LSL": "true",
        "L": "true",
        "LL": "false",
        "H": "false",
        "HH": "false",
    },
    # LTR-04: HIHI critical — HH + LL
    "LTR-04": {
        "Status": "4",
        "Level": "96.0",
        "Pressure": "20.0",
        "LSH": "true",
        "LSL": "true",
        "HH": "true",
        "LL": "true",
        "H": "true",
        "L": "true",
    },
    "LTR": {
        "Status": "3",
        "Level": "12.0",
        "Pressure": "16.0",
        "LL": "true",
        "L": "true",
    },
    "HPR": {
        "Status": "2",
        "Level": "78.0",
        "Pressure": "145.0",
        "H": "true",
    },
    "HTR": {
        "Status": "4",
        "Level": "96.0",
        "Pressure": "95.0",
        "HH": "true",
        "H": "true",
    },
}
# --- END TANK ---

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
    "DisP/SP": ("25.0", "Float"),
    "FLA/SP": ("70.0", "Float"),
    "SVP/SP": ("50.0", "Float"),
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
    # COMP-01: Run; CP Auto / SV Manual â€” FLA > SP (70)
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
    # COMP-02: Idle; CP Manual / SV Auto â€” SVP stays under SP; mild Amps
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
    # COMP-03: Fault; CP/SV Remote â€” Alm + Failed; Cutout color
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
    # COMP-04: Off; CP Auto / SV Manual â€” low but nonzero FLA/SVP
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
    # COMP-05: Manual; CP Remote / SV Manual â€” AntiRec / Starting demo
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


def _valve_id(path: str) -> str | None:
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "Valves":
        return parts[1]
    return None


def _tank_id(path: str) -> str | None:
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "Tanks":
        return parts[1]
    return None


def _sensor_id(path: str) -> str | None:
    parts = path.split("/")
    if len(parts) >= 2 and parts[0] == "Sensors":
        return parts[1]
    return None


def _profile_lookup(path: str, profiles: dict[str, dict[str, str]], device_id: str) -> str | None:
    """Match Value-leaf browse path against profile keys (leaf parent or relative path)."""
    profile = profiles.get(device_id) or {}
    # Strip folder/device prefix → relative under device
    parts = path.split("/")
    if len(parts) < 3:
        return None
    rel = "/".join(parts[2:])  # e.g. Status/Value, Interlock/Sts_IntlkOK, Value/Value
    if rel in profile:
        return profile[rel]
    # FACEPLATE-style Value wrap: TooHot/Value ← profile TooHot/Value or TooHot
    if rel.endswith("/Value"):
        parent = rel[: -len("/Value")]
        if parent in profile:
            return profile[parent]
        if f"{parent}/Value" in profile:
            return profile[f"{parent}/Value"]
    leaf_parent = parts[-2]
    if leaf_parent in profile:
        return profile[leaf_parent]
    return None


def value_source(path: str, sim_dtype: str) -> str:
    for getter, profiles in (
        (_ev_id, EV_PROFILES),
        (_ct_id, CT_PROFILES),
        (_pmp_id, PMP_PROFILES),
        (_efan_id, EFAN_PROFILES),
        (_comp_id, COMP_PROFILES),
        (_valve_id, VALVE_PROFILES),
        (_tank_id, TANK_PROFILES),
        (_sensor_id, SENSOR_PROFILES),
    ):
        device_id = getter(path)
        if device_id:
            hit = _profile_lookup(path, profiles, device_id)
            if hit is not None:
                return hit
            # Evaporator Controls overlays (TimeLeft/TooHot/…) when present on leaves
            if getter is _ev_id:
                hit = _profile_lookup(path, EV_CONTROLS_PROFILES, device_id)
                if hit is not None:
                    return hit

    leaf_parent = path.split("/")[-2]
    if leaf_parent == "Status":
        if path.startswith("Evaporators/"):
            return "list(0, 1, 2, 3, 5, true)"
        if path.startswith("Valves/"):
            return "list(1, 2, 5, 6, true)"
        if path.startswith("Tanks/") or path.startswith("Sensors/"):
            return "0"
        return "list(0, 1, 2, 4, true)"
    if leaf_parent in ("CP_Mode", "SV_Mode"):
        return "2"
    if leaf_parent == "Rung":
        return "0"
    if leaf_parent == "Color":
        return "0"
    if leaf_parent == "Temp":
        return "realistic(20.0, 1.2, 0.06, 0.25, true)"
    if leaf_parent == "Flow":
        return "realistic(35.0, 1.2, 0.06, 0.25, true)"
    if leaf_parent == "Airflow":
        return "realistic(800.0, 20.0, 0.05, 0.2, true)"
    if leaf_parent == "Level":
        return "realistic(50.0, 2.0, 0.05, 0.2, true)"
    if leaf_parent == "TravelTime":
        return "2.5"
    if leaf_parent == "TimeLeft":
        return "12.0"
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
    # Sensor PV is Sensors/<id>/Value/Value — leaf_parent is the Analog member name "Value"
    if leaf_parent == "Value" and path.startswith("Sensors/"):
        return "realistic(30.0, 1.0, 0.05, 0.2, true)"
    if leaf_parent == "SP":
        return "0.0"
    if leaf_parent in (
        "CMD",
        "Fault",
        "Alm",
        "Cutout",
        "Failed",
        "Started",
        "Comm",
        "OpenLS",
        "ClosedLS",
        "HiHi",
        "Hi",
        "Lo",
        "LoLo",
        "Fail",
        "LSH",
        "LSL",
        "HH",
        "H",
        "L",
        "LL",
        "TooHot",
        "TooCold",
        "IntlkOK",
        "PermOK",
        "Off",
    ):
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



def _normalize_faceplate_value_keys(d: dict[str, tuple[str, str]]) -> dict[str, tuple[str, str]]:
    """Ensure every faceplate demo leaf path ends with /Value (Devices _Root bases)."""
    out: dict[str, tuple[str, str]] = {}
    for k, v in d.items():
        if k.endswith("/Value"):
            out[k] = v
        else:
            out[f"{k}/Value"] = v
    return out


def _faceplate_emit_specs() -> list[tuple[str, dict[str, dict[str, str]], dict[str, tuple[str, str]], dict[str, dict[str, str]] | None]]:
    """(folder, device_profiles, faceplate_defaults, optional_overlay_profiles)."""
    return [
        ("Compressors", COMP_PROFILES, _normalize_faceplate_value_keys(COMP_FACEPLATE_DEFAULTS), None),
        ("Pumps", PMP_PROFILES, _normalize_faceplate_value_keys(PUMP_FACEPLATE_DEFAULTS), None),
        ("ExhaustFans", EFAN_PROFILES, _normalize_faceplate_value_keys(EXHAUSTFAN_FACEPLATE_DEFAULTS), None),
        ("CoolingTowers", CT_PROFILES, _normalize_faceplate_value_keys(CT_FACEPLATE_DEFAULTS), None),
        ("Evaporators", EV_PROFILES, _normalize_faceplate_value_keys(EV_FACEPLATE_DEFAULTS), EV_CONTROLS_PROFILES),
        ("Valves", VALVE_PROFILES, _normalize_faceplate_value_keys(VALVE_FACEPLATE_DEFAULTS), None),
        ("Tanks", TANK_PROFILES, _normalize_faceplate_value_keys(TANK_FACEPLATE_DEFAULTS), None),
        ("Sensors", SENSOR_PROFILES, _normalize_faceplate_value_keys(SENSOR_FACEPLATE_DEFAULTS), None),
    ]


def _faceplate_source(
    rel: str,
    default_val: str,
    profile: dict[str, str],
    overlay: dict[str, str] | None,
) -> str:
    for src in (overlay or {}, profile):
        if rel in src:
            return src[rel]
        # Allow profile leaf keys (Failed) to override Failed/Value faceplate rows
        if rel.endswith("/Value"):
            parent = rel[: -len("/Value")]
            if parent in src:
                return src[parent]
    return default_val


def emit_faceplate_rows(rows: list[dict]) -> None:
    """Emit Controls/Config/Interlock demo tags (memory AtomicTags + Value-wrapped Analogs)."""
    for folder, profiles, defaults, overlay_profiles in _faceplate_emit_specs():
        for device_id in sorted(profiles):
            profile = profiles.get(device_id) or {}
            overlay = (overlay_profiles or {}).get(device_id) if overlay_profiles else None
            for rel, (val, dtype) in defaults.items():
                rows.append(
                    {
                        "Time Interval": "0",
                        "Browse Path": f"{folder}/{device_id}/{rel}",
                        "Value Source": _faceplate_source(rel, val, profile, overlay),
                        "Data Type": dtype,
                    }
                )


def emit_faceplate_sim_tags(tree: dict, sim_dtype_map: dict[str, str]) -> None:
    for folder, profiles, defaults, _overlay in _faceplate_emit_specs():
        for device_id in sorted(profiles):
            for rel, (_val, dtype) in defaults.items():
                path = f"{folder}/{device_id}/{rel}"
                parts = path.split("/")
                parent = ensure_folder(tree, parts[:-1])
                parent["tags"].append(
                    {
                        "name": parts[-1],
                        "tagType": "AtomicTag",
                        "valueSource": "opc",
                        "opcServer": "Ignition OPC UA Server",
                        "opcItemPath": "ns=1;s=[Sim]" + "/".join(parts),
                        "dataType": sim_dtype_map.get(dtype, "Float4"),
                    }
                )


def main() -> None:
    leaves: list[tuple[str, dict]] = []
    folder_data: dict[str, list] = {}
    for f in FOLDERS:
        udts_path = TAG_DEF / f / "udts.json"
        if not udts_path.exists():
            print(f"Skip missing plant folder {f}/udts.json (faceplate emit still covers demo paths)")
            continue
        data = json.loads(udts_path.read_text(encoding="utf-8"))
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

    # Flat faceplate demo tags live on Devices/* types (memory) and are often
    # not present as Value leaves on instances — emit Sim rows so lab CSV covers
    # Controls/Config/Interlocks paths for every family.
    emit_faceplate_rows(rows)

    # Deduplicate browse paths (instance Value leaf wins over faceplate emit).
    seen: set[str] = set()
    deduped: list[dict] = []
    for r in sorted(rows, key=lambda x: x["Browse Path"]):
        bp = r["Browse Path"]
        if bp in seen:
            continue
        seen.add(bp)
        deduped.append(r)
    rows = deduped

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
    emit_faceplate_sim_tags(tree, SIM_DTYPE)

    sim_udts = folder_to_json(tree)
    sim_dir = TAG_DEF / "_Sim_"
    # Prefer an existing unary-resource template before wiping _Sim_
    for candidate in (
        TAG_DEF / "Evaporators" / "unary-resource.json",
        TAG_DEF / "Plant" / "Machine Room" / "unary-resource.json",
        sim_dir / "unary-resource.json",
    ):
        if candidate.exists():
            ur = json.loads(candidate.read_text(encoding="utf-8"))
            break
    else:
        ur = {"scope": "G", "version": 1, "restricted": False, "overridable": True, "files": ["udts.json"], "attributes": {"config": {}}}
    ur["files"] = ["udts.json"]

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
