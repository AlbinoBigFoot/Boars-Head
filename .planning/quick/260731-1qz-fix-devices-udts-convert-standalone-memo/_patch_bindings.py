#!/usr/bin/env python3
"""Wrap FACEPLATE_DEFAULTS keys with /Value and patch faceplate view bindings."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\dylan.jones\Documents\Bors")
SIM = ROOT / "sim" / "build_plant_sim.py"
FACEPLATES = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates"
)

# Members that were AtomicTag and are now _Root/*/Value
BARE_MEMBERS = [
    # modes / cmds
    "OPER",
    "MAINT",
    "PROG",
    "AutoEN",
    "HMIEnable",
    "Cleanup",
    "Cmd_Start",
    "Cmd_Stop",
    "Cmd_Auto",
    "Cmd_Manual",
    "Cmd_Remote",
    "Cmd_Reset",
    "Cmd_Open",
    "Cmd_Close",
    "Cmd_StartDefrost",
    "Cmd_StopDefrost",
    # KPIs / config
    "RuntimeHours",
    "MotorStarts",
    "Fail_Timer_PRE",
    "MaxRunTimePerStart",
    "Min_Runtime_Set",
    "HiHiLim",
    "HiLim",
    "LoLim",
    "LoLoLim",
    "Cfg_PumpOut",
    "Cfg_SoftHotGas",
    "Cfg_MainHotGas",
    "Cfg_Bleed",
    "Cfg_FanDelay",
    "Cfg_CoolingTime",
    "Cfg_ZoneAirTempDB",
    # Interlock children (also now Root)
    "Sts_IntlkOK",
    "Sts_NBIntlkOK",
    "Sts_BypActive",
    "Sts_FirstOut",
    "Sts_Intlk",
    "Cfg_Bypassable",
    "OCmd_Reset",
    "Rdy_Reset",
]

# CondTxt00-15 and MSet_Bypass00-15
for i in range(16):
    BARE_MEMBERS.append(f"Cfg_CondTxt{i:02d}")
    BARE_MEMBERS.append(f"MSet_Bypass{i:02d}")

# Sort longest first to avoid partial replacements
BARE_MEMBERS = sorted(set(BARE_MEMBERS), key=len, reverse=True)


def wrap_faceplate_defaults_in_sim() -> None:
    """Rewrite FACEPLATE_DEFAULTS dict literals so bare keys become key/Value."""
    text = SIM.read_text(encoding="utf-8")

    # After each FACEPLATE_DEFAULTS block (including for-loops), wrap keys that lack /Value.
    # Safer approach: inject a normalize call after all defaults are built.
    marker = "def _faceplate_emit_specs()"
    if "_normalize_faceplate_value_keys" not in text:
        helper = '''
def _normalize_faceplate_value_keys(d: dict[str, tuple[str, str]]) -> dict[str, tuple[str, str]]:
    """Ensure every faceplate demo leaf path ends with /Value (Devices _Root bases)."""
    out: dict[str, tuple[str, str]] = {}
    for k, v in d.items():
        if k.endswith("/Value") or k.endswith("/SP"):
            out[k] = v
        else:
            out[f"{k}/Value"] = v
    return out


'''
        text = text.replace(marker, helper + marker)

    # Wrap the dicts in _faceplate_emit_specs
    old = """def _faceplate_emit_specs() -> list[tuple[str, dict[str, dict[str, str]], dict[str, tuple[str, str]], dict[str, dict[str, str]] | None]]:
    \"\"\"(folder, device_profiles, faceplate_defaults, optional_overlay_profiles).\"\"\"
    return [
        ("Compressors", COMP_PROFILES, COMP_FACEPLATE_DEFAULTS, None),
        ("Pumps", PMP_PROFILES, PUMP_FACEPLATE_DEFAULTS, None),
        ("ExhaustFans", EFAN_PROFILES, EXHAUSTFAN_FACEPLATE_DEFAULTS, None),
        ("CoolingTowers", CT_PROFILES, CT_FACEPLATE_DEFAULTS, None),
        ("Evaporators", EV_PROFILES, EV_FACEPLATE_DEFAULTS, EV_CONTROLS_PROFILES),
        ("Valves", VALVE_PROFILES, VALVE_FACEPLATE_DEFAULTS, None),
        ("Tanks", TANK_PROFILES, TANK_FACEPLATE_DEFAULTS, None),
        ("Sensors", SENSOR_PROFILES, SENSOR_FACEPLATE_DEFAULTS, None),
    ]
"""
    new = """def _faceplate_emit_specs() -> list[tuple[str, dict[str, dict[str, str]], dict[str, tuple[str, str]], dict[str, dict[str, str]] | None]]:
    \"\"\"(folder, device_profiles, faceplate_defaults, optional_overlay_profiles).\"\"\"
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
"""
    if old not in text:
        raise SystemExit("Could not find _faceplate_emit_specs block to patch")
    text = text.replace(old, new)
    SIM.write_text(text, encoding="utf-8")
    print("Updated sim/build_plant_sim.py normalize wrapper")


def patch_string_paths(s: str) -> tuple[str, int]:
    """Append /Value to known bare member path suffixes in scripts/expressions."""
    n = 0
    # Patterns covering common faceplate constructions
    replacements = []

    # 1) '/Member' or "/Member" not already followed by /Value
    for mem in BARE_MEMBERS:
        # expression: + '/OPER'  or + "/OPER"
        for quote in ("'", '"'):
            bare = f"{quote}/{mem}{quote}"
            good = f"{quote}/{mem}/Value{quote}"
            if bare in s and good not in s.replace(bare, good):  # rough
                pass
            # Replace bare only when not already /Value
            pattern = re.compile(
                rf"({re.escape(quote)}/{re.escape(mem)})(?!/Value)({re.escape(quote)})"
            )

            def repl(m, _good=None):
                return m.group(1) + "/Value" + m.group(2)

            s2, c = pattern.subn(repl, s)
            if c:
                s = s2
                n += c

        # script: base + '/OPER' already covered
        # script: path + '/Sts_Intlk' covered
        # script: path + '/Cfg_CondTxt' + nn  → need /Value after nn
        # Indirect: '/MSet_Bypass' + nn → '/MSet_Bypass' + nn + '/Value'

    # Special: CondTxt / MSet_Bypass concatenated with nn variable
    # path + '/Cfg_CondTxt' + nn  → path + '/Cfg_CondTxt' + nn + '/Value'
    for prefix in ("Cfg_CondTxt", "MSet_Bypass"):
        # script form
        pat = re.compile(
            rf"(path \+ '/{prefix}' \+ nn)(?! \+ '/Value')"
        )
        s2, c = pat.subn(r"\1 + '/Value'", s)
        s, n = s2, n + c
        # expression: '/Cfg_CondTxt' + {view.custom.nn}
        pat2 = re.compile(
            rf"('/{prefix}' \+ \{{view\.custom\.nn\}})(?! \+ '/Value')"
        )
        s2, c = pat2.subn(r"\1 + '/Value'", s)
        s, n = s2, n + c
        # tag path reference: '/MSet_Bypass' + {view.custom.nn}
        pat3 = re.compile(
            rf"(\{{view\.params\.interlockPath\}} \+ '/{prefix}' \+ \{{view\.custom\.nn\}})(?! \+ '/Value')"
        )
        s2, c = pat3.subn(r"\1 + '/Value'", s)
        s, n = s2, n + c

    return s, n


def patch_faceplates() -> None:
    total = 0
    files = 0
    for path in FACEPLATES.rglob("view.json"):
        text = path.read_text(encoding="utf-8")
        new, n = patch_string_paths(text)
        if n:
            path.write_text(new, encoding="utf-8")
            print(f"  {path.relative_to(ROOT)}: {n} replacements")
            total += n
            files += 1
    print(f"Faceplate files patched: {files}, replacements: {total}")


def patch_overview_if_needed() -> None:
    overview = ROOT / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views"
    total = 0
    for path in overview.rglob("view.json"):
        text = path.read_text(encoding="utf-8")
        if "RuntimeHours" not in text and "MotorStarts" not in text:
            continue
        # Only patch bare RuntimeHours/MotorStarts path suffixes
        new = text
        n = 0
        for mem in ("RuntimeHours", "MotorStarts"):
            pat = re.compile(rf"(/{mem})(?!/Value)")
            new2, c = pat.subn(rf"\1/Value", new)
            new, n = new2, n + c
        if n and new != text:
            path.write_text(new, encoding="utf-8")
            print(f"  overview-ish {path.relative_to(ROOT)}: {n}")
            total += n
    print(f"Overview RuntimeHours/MotorStarts patches: {total}")


def main():
    wrap_faceplate_defaults_in_sim()
    print("Patching faceplates...")
    patch_faceplates()
    print("Patching overview RuntimeHours...")
    patch_overview_if_needed()


if __name__ == "__main__":
    main()
