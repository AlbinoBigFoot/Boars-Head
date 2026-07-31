#!/usr/bin/env python3
import json
import re
from pathlib import Path

root = Path(
    r"C:\Users\dylan.jones\Documents\Bors\gateways\standard\data\config\resources\core\ignition\tag-definition\default"
)
keys = (
    "OPER",
    "MAINT",
    "PROG",
    "Cmd_",
    "RuntimeHours",
    "MotorStarts",
    "AutoEN",
    "HMIEnable",
    "Cleanup",
    "Fail_Timer",
    "HiHiLim",
    "HiLim",
    "LoLim",
    "LoLoLim",
    "Interlock",
)
for f in root.rglob("udts.json"):
    if f.parent.name == "_Sim_":
        continue
    data = json.loads(f.read_text(encoding="utf-8"))

    def walk(tags, path=""):
        for m in tags or []:
            n = m.get("name", "")
            p = f"{path}/{n}" if path else n
            opc = m.get("opcItemPath")
            if opc and any(k in opc for k in keys):
                leaf = opc.rstrip("/").split("/")[-1]
                if leaf != "Value" and not opc.endswith("/SP"):
                    print(f.parent.name, p, opc)
            if m.get("tags"):
                walk(m["tags"], p)

    for inst in data:
        walk(inst.get("tags"), inst.get("name", ""))
print("done")
