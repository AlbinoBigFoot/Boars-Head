# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GL = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views"
    / "00_Pages/LandingPage/Globe/view.json"
)
CSS = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet"
    / "stylesheet.css"
)

g = json.loads(GL.read_text(encoding="utf-8"))


def bump_embeds(node):
    if isinstance(node, dict):
        if node.get("props", {}).get("path") == "02_Components/02_Widgets/SiteCard":
            node["position"] = {"basis": "270px", "shrink": 0}
            node["props"]["style"] = {
                "height": "270px",
                "minHeight": "260px",
                "overflow": "visible",
                "width": "100%",
            }
        for val in node.values():
            bump_embeds(val)
    elif isinstance(node, list):
        for item in node:
            bump_embeds(item)


bump_embeds(g)
GL.write_text(json.dumps(g, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Globe embeds sized up")

text = CSS.read_text(encoding="utf-8")
block = """/* Lightspeed-inspired site picker + overview cards */
.psc-site-card {
	min-height: 260px;
	overflow: visible;
	padding-bottom: 18px;
	transition: box-shadow 120ms ease, border-color 120ms ease;
}
.psc-site-card:hover {
	border-color: var(--callToAction, #0C7BB3);
	box-shadow: var(--boxShadow2, 0 4px 14px rgba(0,0,0,0.18));
}
.psc-overview-card {
	box-sizing: border-box;
	min-width: 0;
}
"""
marker = "/* Lightspeed-inspired site picker + overview cards */"
if marker in text:
    start = text.index(marker)
    rest = text[start:]
    end_rel = rest.find(".psc-overview-card")
    if end_rel >= 0:
        sub = rest[end_rel:]
        brace = sub.find("}")
        end = start + end_rel + brace + 1
        text = text[:start].rstrip() + "\n\n" + block + text[end:].lstrip("\n")
    else:
        text = text[:start].rstrip() + "\n\n" + block
else:
    text = text.rstrip() + "\n\n" + block
CSS.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
print("CSS updated")
