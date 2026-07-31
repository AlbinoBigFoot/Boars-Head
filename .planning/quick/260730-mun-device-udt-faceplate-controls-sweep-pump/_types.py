"""List Devices/* and PLC/* UDT type names; sample Pump vs Compressor leaves."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(r"C:\Users\dylan.jones\Documents\Bors")
TT = ROOT / "gateways/standard/data/config/resources/core/ignition/tag-type-definition/default"


def type_names(folder: str) -> list[str]:
    p = TT / folder / "udts.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    tags = data if isinstance(data, list) else data.get("tags", [])
    out = []
    for t in tags:
        if t.get("tagType") == "UdtType":
            out.append(t.get("name", "?"))
    return out


def top_leaves(type_path_parts: list[str], type_name: str, max_depth: int = 2) -> list[str]:
    """Find a UdtType by name and list child names (shallow)."""
    # Devices/udts.json may nest types
    p = TT.joinpath(*type_path_parts) / "udts.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    tags = data if isinstance(data, list) else data.get("tags", [])

    def find(nodes, name):
        for n in nodes or []:
            if n.get("name") == name and n.get("tagType") == "UdtType":
                return n
            found = find(n.get("tags"), name)
            if found:
                return found
        return None

    udt = find(tags, type_name)
    if not udt:
        return []
    names = []
    for c in udt.get("tags") or []:
        names.append(f"{c.get('name')} ({c.get('tagType')})")
    return names


print("Devices types:", type_names("Devices"))
print("PLC types:", type_names("PLC"))
print("\nDevices/Compressor children:")
for n in top_leaves(["Devices"], "Compressor"):
    print(" ", n)
print("\nDevices/Pump children:")
for n in top_leaves(["Devices"], "Pump"):
    print(" ", n)
print("\nDevices/Valve children:")
for n in top_leaves(["Devices"], "Valve"):
    print(" ", n)
print("\nDevices/Tank children:")
for n in top_leaves(["Devices"], "Tank"):
    print(" ", n)
print("\nDevices/Sensor children:")
for n in top_leaves(["Devices"], "Sensor"):
    print(" ", n)
print("\nDevices/ExhaustFan children:")
for n in top_leaves(["Devices"], "ExhaustFan"):
    print(" ", n)
print("\nDevices/Evaporator children:")
for n in top_leaves(["Devices"], "Evaporator"):
    print(" ", n)
print("\nDevices/CoolingTower children:")
for n in top_leaves(["Devices"], "CoolingTower"):
    print(" ", n)

# Compressors component open script via json walk of events key variations
comp = ROOT / (
    "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/"
    "02_Components/01_Devices/Compressor/view.json"
)
text = comp.read_text(encoding="utf-8")
idx = text.find("deviceType")
# find script containing deviceType
import re
for m in re.finditer(r'"script"\s*:\s*"((?:[^"\\]|\\.)*)"', text):
    raw = m.group(1)
    if "deviceType" in raw:
        s = raw.encode("utf-8").decode("unicode_escape")
        print("\n=== COMPRESSOR OPEN SCRIPT ===")
        print(s)
        break
