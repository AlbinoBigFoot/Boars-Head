# -*- coding: utf-8 -*-
"""Point Groveport nav/marker at plant overview, not Machine Room."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
TAGS = ROOT / (
	"gateways/standard/data/config/resources/core/"
	"ignition/tag-definition/default/_Config/tags.json"
)
NAV_VIEW = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/00_Pages/00_Docked/Navigation/view.json"
)
TEMP_NAV = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/00_Pages/00_Docked/TempNav/view.json"
)
PAGE_CONFIG = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/page-config/config.json"
)
SCAN_CFG = ROOT / "docs/cloud-agent/ignition-scan.json"
WIRE_SCRIPT = ROOT / "scripts/_wire_globe_nav_click.py"

GROVEPORT_PAGE = "/plants/groveport"
GROVEPORT_VIEW = "00_Pages/LandingPage/PlantPlaceholder"
MACHINE_ROOM_PAGE = "/machine-room"
MACHINE_ROOM_VIEW = "00_Pages/Machine Room/Overview"


def find_label(items, label):
	for it in items or []:
		if it.get("label") == label:
			return it
	return None


def load_scan_env():
	port = "19088"
	token = ""
	if SCAN_CFG.exists():
		cfg = json.loads(SCAN_CFG.read_text(encoding="utf-8"))
		port = str(cfg.get("standardHttpPort") or port)
		token = cfg.get("apiToken") or token
	env_path = ROOT / ".env"
	if env_path.exists():
		for line in env_path.read_text(encoding="utf-8").splitlines():
			line = line.strip()
			if not line or line.startswith("#") or "=" not in line:
				continue
			k, v = line.split("=", 1)
			k, v = k.strip(), v.strip().strip('"').strip("'")
			if k == "STANDARD_HTTP_PORT":
				port = v
			elif k == "IGNITION_API_TOKEN":
				token = v
	return port, token


def main():
	tags = json.loads(TAGS.read_text(encoding="utf-8"))
	nav = next(t for t in tags if t.get("name") == "Navigation")
	items = nav["defaultValue"]["items"]
	boars = find_label(items, "Boars Head")
	grove = find_label(boars.get("items"), "Groveport")
	if not grove:
		raise SystemExit("Groveport node missing")

	grove["data"] = {
		"action": "page",
		"page": GROVEPORT_PAGE,
		"viewPath": GROVEPORT_VIEW,
		"tagPath": "",
	}

	machine = find_label(grove.get("items"), "Machine Room")
	if not machine:
		raise SystemExit("Machine Room child missing under Groveport")
	machine.setdefault("data", {})
	machine["data"]["action"] = "page"
	machine["data"]["page"] = MACHINE_ROOM_PAGE
	machine["data"]["viewPath"] = MACHINE_ROOM_VIEW
	print("Groveport ->", GROVEPORT_PAGE)
	print("Machine Room ->", MACHINE_ROOM_PAGE)

	geo = next(t for t in tags if t.get("name") == "MapMarkerGeoJson")
	for f in geo["defaultValue"]["features"]:
		props = f.get("properties") or {}
		if props.get("label") == "Groveport" or props.get("name") == "Groveport OH":
			props["page"] = GROVEPORT_PAGE
			props["action"] = "page"
			props["viewPath"] = GROVEPORT_VIEW
			props["tagPath"] = ""
			props["label"] = "Groveport"
			f["properties"] = props
			print("MapMarkerGeoJson Groveport ->", GROVEPORT_PAGE)

	TAGS.write_text(json.dumps(tags, indent=2) + "\n", encoding="utf-8", newline="\n")

	for path in (NAV_VIEW, TEMP_NAV):
		view = json.loads(path.read_text(encoding="utf-8"))
		view.setdefault("custom", {})["items"] = items
		path.write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8", newline="\n")
		print("synced", path.name)

	cfg = json.loads(PAGE_CONFIG.read_text(encoding="utf-8"))
	cfg.setdefault("pages", {})[GROVEPORT_PAGE] = {
		"title": "Groveport",
		"viewPath": GROVEPORT_VIEW,
		"viewParams": {"plantName": "Groveport"},
	}
	PAGE_CONFIG.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("page-config", GROVEPORT_PAGE)

	# Keep wire script plant list consistent for future re-runs
	if WIRE_SCRIPT.exists():
		text = WIRE_SCRIPT.read_text(encoding="utf-8")
		old = (
			'\t\t"label": "Groveport",\n'
			'\t\t"name": "Groveport OH",\n'
			'\t\t"page": "/machine-room",\n'
			'\t\t"viewPath": "00_Pages/Machine Room/Overview",\n'
			'\t\t"tagPath": "[default]Plant/Machine Room",\n'
			'\t\t"coords": [-82.943375287534, 39.83741622205],\n'
			'\t\t"placeholder": False,\n'
		)
		new = (
			'\t\t"label": "Groveport",\n'
			'\t\t"name": "Groveport OH",\n'
			'\t\t"page": "/plants/groveport",\n'
			'\t\t"viewPath": "00_Pages/LandingPage/PlantPlaceholder",\n'
			'\t\t"tagPath": "",\n'
			'\t\t"coords": [-82.943375287534, 39.83741622205],\n'
			'\t\t"placeholder": True,\n'
		)
		if old in text:
			WIRE_SCRIPT.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
			print("updated _wire_globe_nav_click.py PLANTS Groveport")
		elif '"page": "/plants/groveport"' in text:
			print("_wire_globe_nav_click.py already has Groveport overview page")
		else:
			print("warn: could not patch _wire_globe_nav_click.py PLANTS block")

	port, token = load_scan_env()
	base = f"http://127.0.0.1:{port}"
	headers = {"X-Ignition-API-Token": token, "Content-Type": "application/json"}

	markers = geo["defaultValue"]
	r = requests.post(
		f"{base}/system/webdev/BH/globe/mapMarkers",
		headers=headers,
		json=markers,
		timeout=60,
	)
	print("POST markers", r.status_code, (r.text or "")[:200])
	r = requests.post(
		f"{base}/system/webdev/BH/globe/mapMarkers",
		headers=headers,
		json={"__nav": True, "items": items},
		timeout=60,
	)
	print("POST nav", r.status_code, (r.text or "")[:200])

	import subprocess

	subprocess.check_call(
		[sys.executable, str(ROOT / "scripts" / "repair-resource-signatures.py")],
		cwd=str(ROOT),
	)
	for endpoint in ("/data/api/v1/scan/config", "/data/api/v1/scan/projects"):
		r = requests.post(f"{base}{endpoint}", headers=headers, timeout=120)
		print("scan", endpoint, r.status_code)

	print("Done.")


if __name__ == "__main__":
	main()
