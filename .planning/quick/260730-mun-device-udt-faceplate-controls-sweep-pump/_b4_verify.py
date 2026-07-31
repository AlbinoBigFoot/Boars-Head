# -*- coding: utf-8 -*-
from pathlib import Path

fp = Path(
    "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/"
    "01_Popups/00_Faceplates/Faceplate/view.json"
).read_text(encoding="utf-8")
for dt in ["Pump", "ExhaustFan", "Valve", "Tank", "Sensor", "Evaporator", "CoolingTower"]:
    assert dt in fp, dt
assert "hasControlsAsset" in fp and "CoolingTower" in fp
# Web GUI header remains compressor-only (escaped or raw quotes in JSON)
assert "Compressor" in fp and "coalesce({view.params.webGuiUrl}" in fp
assert "len(coalesce({view.params.webGuiUrl}" in fp
web_ok = (
    "{view.params.deviceType} = 'Compressor' && len(coalesce({view.params.webGuiUrl}, '')) > 0" in fp
    or "{view.params.deviceType} = \\'Compressor\\' && len(coalesce({view.params.webGuiUrl}, '')) > 0" in fp
)
assert web_ok, "Web GUI compressor-only expression missing"

pump = Path(
    "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/"
    "02_Components/01_Devices/Pump/view.json"
).read_text(encoding="utf-8")
assert "deviceType" in pump and "Faceplate" in pump

sv = Path(
    "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/"
    "02_Components/01_Devices/SolenoidValve/view.json"
).read_text(encoding="utf-8")
assert "'deviceType': 'Valve'" in sv

# Controls paths exist
root = Path(
    "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/"
    "01_Popups/00_Faceplates/_Assets"
)
for d in ["Pump", "ExhaustFan", "Valve", "Tank", "Sensor", "Evaporator", "CoolingTower"]:
    assert (root / d / "Controls" / "view.json").is_file(), d

# thin wrappers embed Faceplate
for name, dtype in [
    ("Pump", "Pump"),
    ("SolenoidValve", "Valve"),
    ("Evaporator", "Evaporator"),
]:
    w = Path(
        "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/"
        f"01_Popups/00_Faceplates/{name}/view.json"
    ).read_text(encoding="utf-8")
    assert "01_Popups/00_Faceplates/Faceplate" in w
    assert f'"deviceType": "{dtype}"' in w

print("B4-ok")
