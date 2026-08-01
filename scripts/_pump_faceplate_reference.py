# -*- coding: utf-8 -*-
"""Spin up Pump as the shell + typed-Controls reference.

1) Machine Room pumps: faceplate = Pump
2) Device opener: unify popup id to comp-fp-* (matches Faceplate Close / showFaceplate)
3) Faceplate Close: also close pump-fp-* (legacy)
4) Pump Controls: add Faults strip + Fail timer / Min runtime KPI rows
5) CSS for fault status codes
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
MR = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/00_Pages/Machine Room/Overview/view.json"
)
PUMP_DEV = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/02_Components/01_Devices/Pump/view.json"
)
FACEPLATE = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/01_Popups/00_Faceplates/Faceplate/view.json"
)
CONTROLS = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/01_Popups/00_Faceplates/_Assets/Pump/Controls/view.json"
)
CSS = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/stylesheet/stylesheet.css"
)
SCAN_CFG = ROOT / "docs/cloud-agent/ignition-scan.json"

PUMP_OPENER = (
	"\tfaceplate = self.view.params.faceplate\n"
	"\tif faceplate is None or str(faceplate).strip() == '':\n"
	"\t\treturn\n"
	"\ttagPath = str(self.view.params.tagPath or '')\n"
	"\ttitle = str(self.view.custom.label or '')\n"
	"\tif title in (None, '', 'nn'):\n"
	"\t\ttitle = tagPath.split('/')[-1] if tagPath else self.view.name\n"
	"\t# Shell + typed Controls. Prefer shared.Alerts.showFaceplate (comp-fp id).\n"
	"\tshared.Alerts.showFaceplate(\n"
	"\t\ttagPath=tagPath,\n"
	"\t\tdeviceType='Pump',\n"
	"\t\ttitle=title,\n"
	"\t\twebGuiUrl='',\n"
	"\t\tshowControls=True,\n"
	"\t\tshowConfiguration=True,\n"
	"\t\tshowInterlocks=True,\n"
	"\t\tshowTrend=True,\n"
	"\t\tshowAlarmConfiguration=True,\n"
	"\t\tshowAlarms=True,\n"
	"\t\twidth=560,\n"
	"\t\theight=640\n"
	"\t)\n"
)

CLOSE_SCRIPT = (
	"\ttagPath = str(self.view.params.tagPath or '')\n"
	"\tlabel = str(self.view.custom.label or '')\n"
	"\tkey = tagPath or label\n"
	"\tfor pid in [\n"
	"\t\t'comp-fp-%s' % key,\n"
	"\t\t'fp-%s' % key,\n"
	"\t\t'pump-fp-%s' % key,\n"
	"\t]:\n"
	"\t\ttry:\n"
	"\t\t\tsystem.perspective.closePopup(pid)\n"
	"\t\texcept:\n"
	"\t\t\tpass\n"
)


def fault_chip(name: str, code: str, tag_suffix: str) -> dict:
	"""Text status chip: OK / ACTIVE with sts class (not color-only)."""
	return {
		"type": "ia.container.flex",
		"meta": {"name": name},
		"position": {"basis": "120px", "shrink": 0},
		"props": {
			"direction": "column",
			"style": {"classes": "faceplate-fault-chip", "gap": "2px"},
		},
		"children": [
			{
				"type": "ia.display.label",
				"meta": {"name": "Code"},
				"props": {
					"text": code,
					"style": {"classes": "faceplate-fault-code font-label"},
				},
			},
			{
				"type": "ia.display.label",
				"meta": {"name": "State"},
				"propConfig": {
					"props.text": {
						"binding": {
							"config": {
								"expression": (
									"if({view.params.tagPath} = '', '—',\n"
									"\tif(coalesce(tag({view.params.tagPath} + '/%s'), false),\n"
									"\t\t'ACTIVE', 'OK'))" % tag_suffix
								)
							},
							"type": "expr",
						}
					},
					"props.style.classes": {
						"binding": {
							"config": {
								"expression": (
									"if({view.params.tagPath} = '', 'faceplate-fault-state',\n"
									"\tif(coalesce(tag({view.params.tagPath} + '/%s'), false),\n"
									"\t\t'faceplate-fault-state faceplate-fault-active',\n"
									"\t\t'faceplate-fault-state faceplate-fault-ok'))" % tag_suffix
								)
							},
							"type": "expr",
						}
					},
				},
				"props": {
					"text": "OK",
					"style": {"classes": "faceplate-fault-state faceplate-fault-ok"},
				},
			},
		],
	}


def faults_section() -> dict:
	return {
		"type": "ia.container.flex",
		"meta": {"name": "FaultsSection"},
		"position": {"shrink": 0},
		"propConfig": {
			"position.display": {
				"binding": {
					"config": {
						"expression": (
							"qualityOf(tag({view.params.tagPath} + '/Alm_FailToStart/Value')) = 'Good' || "
							"qualityOf(tag({view.params.tagPath} + '/Alm_IOFault/Value')) = 'Good' || "
							"qualityOf(tag({view.params.tagPath} + '/Sts_FailToStart/Value')) = 'Good'"
						)
					},
					"type": "expr",
				}
			}
		},
		"props": {
			"direction": "column",
			"style": {"classes": "faceplate-section faceplate-section-card"},
		},
		"children": [
			{
				"type": "ia.display.label",
				"meta": {"name": "FaultsTitle"},
				"props": {
					"text": "Faults",
					"style": {"classes": "faceplate-section-title font-label"},
				},
			},
			{
				"type": "ia.container.flex",
				"meta": {"name": "FaultChips"},
				"props": {
					"direction": "row",
					"style": {"gap": "8px", "flexWrap": "wrap"},
				},
				"children": [
					fault_chip("FailToStartAlm", "FTS", "Alm_FailToStart/Value"),
					fault_chip("IOFault", "IOF", "Alm_IOFault/Value"),
					fault_chip("FailToStartSts", "FTS-STS", "Sts_FailToStart/Value"),
				],
			},
		],
	}


def kpi_row(name: str, label: str, expr: str) -> dict:
	return {
		"type": "ia.container.flex",
		"meta": {"name": name},
		"position": {"shrink": 0},
		"props": {
			"direction": "row",
			"alignItems": "center",
			"style": {"classes": "faceplate-kpi-row"},
		},
		"children": [
			{
				"type": "ia.display.label",
				"meta": {"name": name + "Lbl"},
				"position": {"basis": "140px", "shrink": 0},
				"props": {
					"text": label,
					"style": {"classes": "faceplate-kpi-label font-label"},
				},
			},
			{
				"type": "ia.display.label",
				"meta": {"name": name + "Val"},
				"position": {"grow": 1},
				"propConfig": {
					"props.text": {
						"binding": {"config": {"expression": expr}, "type": "expr"}
					}
				},
				"props": {"style": {"classes": "font-value"}, "text": ""},
			},
		],
	}


def wire_machine_room():
	doc = json.loads(MR.read_text(encoding="utf-8"))

	def walk(nodes):
		n = 0
		for node in nodes or []:
			meta = (node.get("meta") or {}).get("name", "")
			path = (node.get("props") or {}).get("path", "")
			if path == "02_Components/01_Devices/Pump" or "Pump" in meta:
				params = node.setdefault("props", {}).setdefault("params", {})
				if "faceplate" in params or path.endswith("/Pump"):
					params["faceplate"] = "Pump"
					n += 1
			n += walk(node.get("children"))
		return n

	# Overview root children
	count = walk(doc.get("root", {}).get("children"))
	MR.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("Machine Room Pump faceplate params set:", count)


def wire_pump_opener():
	doc = json.loads(PUMP_DEV.read_text(encoding="utf-8"))
	script = doc["root"]["events"]["dom"]["onClick"]["config"]["script"]
	if "shared.Alerts.showFaceplate" in script:
		print("Pump opener already uses showFaceplate")
	else:
		doc["root"]["events"]["dom"]["onClick"]["config"]["script"] = PUMP_OPENER
		PUMP_DEV.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8", newline="\n")
		print("Pump opener -> shared.Alerts.showFaceplate (comp-fp)")


def wire_close():
	doc = json.loads(FACEPLATE.read_text(encoding="utf-8"))

	def find_close(node):
		if (node.get("meta") or {}).get("name") == "Close":
			return node
		for ch in node.get("children") or []:
			found = find_close(ch)
			if found:
				return found
		return None

	close = find_close(doc["root"])
	if not close:
		raise SystemExit("Faceplate Close button not found")
	close["events"]["component"]["onActionPerformed"]["config"]["script"] = CLOSE_SCRIPT
	FACEPLATE.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("Faceplate Close closes comp-fp / fp / pump-fp")


def wire_controls():
	doc = json.loads(CONTROLS.read_text(encoding="utf-8"))
	children = doc["root"]["children"]
	# Remove prior FaultsSection if re-run
	children = [c for c in children if (c.get("meta") or {}).get("name") != "FaultsSection"]

	# Insert Faults after ModeSection (or at start)
	insert_at = 0
	for i, c in enumerate(children):
		if (c.get("meta") or {}).get("name") == "ModeSection":
			insert_at = i + 1
			break
	children.insert(insert_at, faults_section())

	# Append KPI rows for fail timer / min runtime inside KpiSection
	for c in children:
		if (c.get("meta") or {}).get("name") != "KpiSection":
			continue
		kpi_kids = c.setdefault("children", [])
		names = {(k.get("meta") or {}).get("name") for k in kpi_kids}
		if "FailTimer" not in names:
			kpi_kids.append(
				kpi_row(
					"FailTimer",
					"Fail-to-start timer",
					"if({view.params.tagPath} = '', '', numberFormat(toFloat(tag({view.params.tagPath} + '/Fail_Timer_PRE/Value')), '#0.0'))",
				)
			)
		if "MinRuntime" not in names:
			kpi_kids.append(
				kpi_row(
					"MinRuntime",
					"Min runtime set",
					"if({view.params.tagPath} = '', '', numberFormat(toFloat(tag({view.params.tagPath} + '/Min_Runtime_Set/Value')), '#0.0'))",
				)
			)
		break

	doc["root"]["children"] = children
	CONTROLS.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("Pump Controls: Faults + FailTimer/MinRuntime KPI")


def wire_css():
	text = CSS.read_text(encoding="utf-8")
	block = """
/* Pump / motor faceplate fault status codes (text + class, not color-only) */
.psc-faceplate-fault-chip {
	min-width: 88px;
	padding: 4px 6px;
	border: 1px solid var(--border);
	border-radius: 4px;
	background: var(--surface-container);
}
.psc-faceplate-fault-code {
	font-size: 11px;
	font-weight: 700;
	letter-spacing: 0.04em;
	color: var(--text-muted);
}
.psc-faceplate-fault-state {
	font-size: 12px;
	font-weight: 600;
}
.psc-faceplate-fault-ok {
	color: var(--text-muted);
}
.psc-faceplate-fault-active {
	color: var(--sts-fault);
	font-weight: 700;
}
"""
	if "faceplate-fault-chip" in text:
		print("CSS fault chips already present")
		return
	CSS.write_text(text.rstrip() + "\n" + block + "\n", encoding="utf-8", newline="\n")
	print("CSS: faceplate fault chips")


def repair_and_scan():
	import subprocess

	paths = [
		MR.parent / "resource.json",
		PUMP_DEV.parent / "resource.json",
		FACEPLATE.parent / "resource.json",
		CONTROLS.parent / "resource.json",
		CSS.parent / "resource.json",
	]
	for p in paths:
		subprocess.check_call(
			[sys.executable, str(ROOT / "scripts" / "repair-resource-signatures.py"), "--path", str(p)],
			cwd=str(ROOT),
		)
	cfg = json.loads(SCAN_CFG.read_text(encoding="utf-8"))
	base = "http://127.0.0.1:%s" % cfg["standardHttpPort"]
	headers = {"X-Ignition-API-Token": cfg["apiToken"]}
	for ep in ("/data/api/v1/scan/config", "/data/api/v1/scan/projects"):
		r = requests.post(base + ep, headers=headers, timeout=120)
		print("scan", ep, r.status_code)


def main():
	wire_machine_room()
	wire_pump_opener()
	wire_close()
	wire_controls()
	wire_css()
	repair_and_scan()
	print("Done. Test: /machine-room → HTLR-Pump 1 → Controls → Close")


if __name__ == "__main__":
	main()
