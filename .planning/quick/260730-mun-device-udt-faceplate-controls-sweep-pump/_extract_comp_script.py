"""Extract Compressor faceplate open script."""
from pathlib import Path
import json

p = Path(
    r"C:\Users\dylan.jones\Documents\Bors\gateways\standard\data\projects\BH"
    r"\com.inductiveautomation.perspective\views\02_Components\01_Devices\Compressor\view.json"
)
data = json.loads(p.read_text(encoding="utf-8"))


def walk(node, out):
    if isinstance(node, dict):
        ev = node.get("events")
        if isinstance(ev, dict):
            for scope in ev.values():
                if isinstance(scope, dict):
                    for handlers in scope.values():
                        if isinstance(handlers, list):
                            for h in handlers:
                                if isinstance(h, dict) and h.get("type") == "script":
                                    s = h.get("script", "")
                                    if "faceplate" in s or "deviceType" in s:
                                        out.append(s)
        for v in node.values():
            walk(v, out)
    elif isinstance(node, list):
        for i in node:
            walk(i, out)


scripts = []
walk(data, scripts)
for s in scripts:
    print("---SCRIPT---")
    print(s)
    print()
