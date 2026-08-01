# -*- coding: utf-8 -*-
"""Update Legend dock alarm rows to Critical/High/Medium/Low NotificationIcons."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
LEGEND = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/00_Pages/00_Docked/Legend/view.json"
)
SCAN_CFG = ROOT / "docs/cloud-agent/ignition-scan.json"

ALARMS = [
	{
		"name": "Critical",
		"path": "03_Elements/01_Status/NotificationIcons/Alarms/Critical",
		"text": "Critical Alarm",
		"tooltip": "A critical-priority alarm is active",
		"container": "FlexContainer_Critical",
	},
	{
		"name": "High",
		"path": "03_Elements/01_Status/NotificationIcons/Alarms/High",
		"text": "High Alarm",
		"tooltip": "A high-priority alarm is active",
		"container": "FlexContainer_High",
	},
	{
		"name": "Medium",
		"path": "03_Elements/01_Status/NotificationIcons/Alarms/Medium",
		"text": "Medium Alarm",
		"tooltip": "A medium-priority alarm is active",
		"container": "FlexContainer_Medium",
	},
	{
		"name": "Low",
		"path": "03_Elements/01_Status/NotificationIcons/Alarms/Low",
		"text": "Low Alarm",
		"tooltip": "A low-priority alarm is active",
		"container": "FlexContainer_Low",
	},
]

TOOLTIP_STYLE = {
	"background": "var(--neutral-70)",
	"borderRadius": "10px",
	"fontSize": "1rem",
	"padding": "10px 20px",
}


def spacer(name: str) -> dict:
	return {
		"meta": {"name": name},
		"position": {"basis": "15px", "shrink": 0},
		"type": "ia.display.label",
	}


def alarm_row(spec: dict) -> dict:
	return {
		"children": [
			{
				"meta": {"name": spec["name"]},
				"position": {"basis": "30px", "shrink": 0},
				"props": {"path": spec["path"]},
				"type": "ia.display.view",
			},
			{
				"meta": {"name": "Label"},
				"position": {"grow": 1},
				"props": {
					"style": {
						"classes": "font-label",
						"marginRight": "10px",
						"textAlign": "right",
					},
					"text": spec["text"],
				},
				"type": "ia.display.label",
			},
		],
		"meta": {
			"name": spec["container"],
			"tooltip": {
				"enabled": True,
				"location": "center-left",
				"style": dict(TOOLTIP_STYLE),
				"text": spec["tooltip"],
				"width": "400px",
			},
		},
		"position": {"basis": "30px", "shrink": 0},
		"props": {"style": {"cursor": "help", "overflow": "visible"}},
		"type": "ia.container.flex",
	}


def is_alarm_section(node: dict) -> bool:
	"""True for old High/Medium/Low rows or their spacer labels."""
	name = (node.get("meta") or {}).get("name", "")
	if name in {
		"FlexContainer_5",
		"FlexContainer_6",
		"FlexContainer_7",
		"FlexContainer_Critical",
		"FlexContainer_High",
		"FlexContainer_Medium",
		"FlexContainer_Low",
		"Label_7",
		"Label_4",
		"Label_5",
		"Label_AlarmGap0",
		"Label_AlarmGap1",
		"Label_AlarmGap2",
		"Label_AlarmGap3",
	}:
		return True
	# detect by icon path
	for child in node.get("children") or []:
		path = (child.get("props") or {}).get("path", "")
		if "Alarms/" in path or "Alarms\\" in path:
			return True
	return False


def main():
	doc = json.loads(LEGEND.read_text(encoding="utf-8"))
	children = doc["root"]["children"]
	kept = [c for c in children if not is_alarm_section(c)]

	# Ensure a spacer before alarm block if last kept item isn't already a spacer label
	alarm_block = []
	for i, spec in enumerate(ALARMS):
		alarm_block.append(spacer("Label_AlarmGap%d" % i))
		alarm_block.append(alarm_row(spec))

	doc["root"]["children"] = kept + alarm_block
	LEGEND.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("Legend alarms -> Critical/High/Medium/Low NotificationIcons")

	import subprocess

	subprocess.check_call(
		[
			sys.executable,
			str(ROOT / "scripts" / "repair-resource-signatures.py"),
			"--path",
			str(
				ROOT
				/ "gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
				"/views/00_Pages/00_Docked/Legend/resource.json"
			),
		],
		cwd=str(ROOT),
	)

	cfg = json.loads(SCAN_CFG.read_text(encoding="utf-8"))
	base = "http://127.0.0.1:%s" % cfg["standardHttpPort"]
	headers = {"X-Ignition-API-Token": cfg["apiToken"]}
	r = requests.post(base + "/data/api/v1/scan/projects", headers=headers, timeout=120)
	print("scan projects", r.status_code)


if __name__ == "__main__":
	main()
