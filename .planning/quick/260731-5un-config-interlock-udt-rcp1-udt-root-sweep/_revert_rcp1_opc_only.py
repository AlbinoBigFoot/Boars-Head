# Revert HTR Folder+Value mimic to flat OPC AtomicTags; fix Units sourceTagPaths.
import json
from pathlib import Path

htr_path = Path(
    r"gateways/standard/data/config/resources/core/ignition/tag-definition/default/RCP1/HTR/udts.json"
)
units_path = Path(
    r"gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Units/udts.json"
)

htr = json.loads(htr_path.read_text(encoding="utf-8"))
flat = []
for item in htr:
    if item.get("tagType") == "Folder":
        name = item["name"]
        for child in item.get("tags") or []:
            cname = child["name"]
            leaf = dict(child)
            if cname == "Value":
                leaf["name"] = name
            elif cname == "SP":
                leaf["name"] = f"{name}_SP"
            else:
                leaf["name"] = f"{name}_{cname}"
            flat.append(leaf)
    else:
        flat.append(item)

htr_path.write_text(
    json.dumps(flat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print("HTR leaves:", [t["name"] for t in flat])

units = json.loads(units_path.read_text(encoding="utf-8"))

replacements = {
    "[default]RCP1/HTR/HH/Value": "[default]RCP1/HTR/HH",
    "[default]RCP1/HTR/HH/SP": "[default]RCP1/HTR/HH_SP",
    "[default]RCP1/HTR/H/Value": "[default]RCP1/HTR/H",
    "[default]RCP1/HTR/H/SP": "[default]RCP1/HTR/H_SP",
    "[default]RCP1/HTR/L/Value": "[default]RCP1/HTR/L",
    "[default]RCP1/HTR/L/SP": "[default]RCP1/HTR/L_SP",
    "[default]RCP1/HTR/LL/Value": "[default]RCP1/HTR/LL",
    "[default]RCP1/HTR/LL/SP": "[default]RCP1/HTR/LL_SP",
    "[default]RCP1/HTR/Level/Value": "[default]RCP1/HTR/Level",
    "[default]RCP1/HTR/Level/SP": "[default]RCP1/HTR/Level_SP",
    "[default]RCP1/HTR/HH/SP/Value": "[default]RCP1/HTR/HH_SP",
    "[default]RCP1/HTR/H/SP/Value": "[default]RCP1/HTR/H_SP",
    "[default]RCP1/HTR/L/SP/Value": "[default]RCP1/HTR/L_SP",
    "[default]RCP1/HTR/LL/SP/Value": "[default]RCP1/HTR/LL_SP",
    "[default]RCP1/HTR/Level/SP/Value": "[default]RCP1/HTR/Level_SP",
}

changed = [0]


def walk(obj):
    if isinstance(obj, dict):
        if "sourceTagPath" in obj and isinstance(obj["sourceTagPath"], str):
            p = obj["sourceTagPath"]
            if p in replacements:
                obj["sourceTagPath"] = replacements[p]
                changed[0] += 1
            elif p.startswith("[default]RCP1/") and p.endswith("/Value"):
                # Legitimate leaf named Value (Sensor process value):
                # [default]RCP1/HSS-Pumps Pressure/Value
                parts = p[len("[default]") :].strip("/").split("/")
                # parts like RCP1, HSS-Pumps Pressure, Value
                if len(parts) >= 3 and parts[-1] == "Value" and parts[-2] != "Value":
                    # .../member/Value — strip mistaken _Root Value suffix
                    # EXCEPT when member IS the leaf named Value at device folder root
                    # i.e. exactly 3 parts: RCP1 / folder / Value
                    if len(parts) == 3 and parts[2] == "Value":
                        pass  # keep HSS-Pumps Pressure/Value
                    else:
                        obj["sourceTagPath"] = p[: -len("/Value")]
                        changed[0] += 1
                elif p.endswith("/Value/Value"):
                    obj["sourceTagPath"] = p[: -len("/Value")]
                    changed[0] += 1
        for v in obj.values():
            walk(v)
    elif isinstance(obj, list):
        for v in obj:
            walk(v)


walk(units)

left = []


def collect(obj):
    if isinstance(obj, dict):
        p = obj.get("sourceTagPath")
        if isinstance(p, str) and p.startswith("[default]RCP1/") and "Value" in p:
            left.append(p)
        for v in obj.values():
            collect(v)
    elif isinstance(obj, list):
        for v in obj:
            collect(v)


collect(units)
units_path.write_text(
    json.dumps(units, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print("Units sourceTagPath changes:", changed[0])
print("Remaining RCP1 paths containing Value:")
for p in sorted(set(left)):
    print(" ", p)

# Final RCP1 audit
import glob

base = r"gateways/standard/data/config/resources/core/ignition/tag-definition/default/RCP1"
for p in glob.glob(base + "/**/udts.json", recursive=True):
    data = json.load(open(p, encoding="utf-8"))
    s = json.dumps(data)
    print(
        p.split("RCP1")[-1],
        "typeId=",
        "typeId" in s,
        "_Root=",
        "_Root" in s,
        "UdtInstance=",
        "UdtInstance" in s,
        "Folder=",
        '"tagType": "Folder"' in s or '"tagType":"Folder"' in s,
    )
