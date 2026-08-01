# -*- coding: utf-8 -*-
"""Wire globe marker clicks to plant pages + nav tree expansion."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAGS = ROOT / (
	"gateways/standard/data/config/resources/core/"
	"ignition/tag-definition/default/_Config/tags.json"
)
GLOBE_VIEW = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/00_Pages/LandingPage/Globe/view.json"
)
PLACEHOLDER_DIR = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
	"/views/00_Pages/LandingPage/PlantPlaceholder"
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
GLOBE_INDEX = ROOT / (
	"gateways/standard/data/projects/BH/com.inductiveautomation.webdev"
	"/resources/globe/index/config.json"
)

PLANTS = [
	{
		"label": "Groveport",
		"name": "Groveport OH",
		"page": "/plants/groveport",
		"viewPath": "00_Pages/LandingPage/PlantPlaceholder",
		"tagPath": "",
		"coords": [-82.943375287534, 39.83741622205],
		"placeholder": True,
	},
	{
		"label": "New Castle",
		"name": "New Castle IN",
		"page": "/plants/new-castle",
		"viewPath": "00_Pages/LandingPage/PlantPlaceholder",
		"tagPath": "",
		"coords": [-85.385006308166, 39.873372394315],
		"placeholder": True,
	},
	{
		"label": "Forrest City",
		"name": "Forrest City AR",
		"page": "/plants/forrest-city",
		"viewPath": "00_Pages/LandingPage/PlantPlaceholder",
		"tagPath": "",
		"coords": [-90.811739063343, 34.995907752639],
		"placeholder": True,
	},
	{
		"label": "Petersburg",
		"name": "Petersburg VA",
		"page": "/plants/petersburg",
		"viewPath": "00_Pages/LandingPage/PlantPlaceholder",
		"tagPath": "",
		"coords": [-77.414445481263, 37.176357413569],
		"placeholder": True,
	},
	{
		"label": "Holland",
		"name": "Holland MI",
		"page": "/plants/holland",
		"viewPath": "00_Pages/LandingPage/PlantPlaceholder",
		"tagPath": "",
		"coords": [-86.096160011663, 42.80339475283],
		"placeholder": True,
	},
]

NAV_ONCHANGE = (
	"\tvalue = currentValue.value\n"
	"\tdata = {}\n"
	"\tif value is None or value == '' or value == {}:\n"
	"\t\treturn\n"
	"\ttry:\n"
	"\t\t# Document tags may expose nested QualifiedValues\n"
	"\t\tfor k in value:\n"
	"\t\t\tv = value[k]\n"
	"\t\t\ttry:\n"
	"\t\t\t\tdata[k] = v.value\n"
	"\t\t\texcept:\n"
	"\t\t\t\tdata[k] = v\n"
	"\texcept:\n"
	"\t\ttry:\n"
	"\t\t\tdata = system.util.jsonDecode(system.util.jsonEncode(value))\n"
	"\t\texcept:\n"
	"\t\t\treturn\n"
	"\tif not data:\n"
	"\t\treturn\n"
	"\t# Ensure page navigation even if action omitted\n"
	"\tif data.get('page') and not data.get('action'):\n"
	"\t\tdata['action'] = 'page'\n"
	"\tNavigation.Nav.navigate(data)\n"
	"\tsystem.tag.writeAsync(['[default]_Config/MapMarkerNavigation'], [{}])\n"
)

TICKET_ITEMS = None  # keep existing


def geojson_features():
	feats = []
	for p in PLANTS:
		feats.append(
			{
				"type": "Feature",
				"geometry": {"coordinates": list(p["coords"]), "type": "Point"},
				"properties": {
					"color": "#114599",
					"name": p["name"],
					"label": p["label"],
					"page": p["page"],
					"action": "page",
					"viewPath": p["viewPath"],
					"tagPath": p["tagPath"],
				},
			}
		)
	return {"type": "FeatureCollection", "features": feats}


def update_tags():
	tags = json.loads(TAGS.read_text(encoding="utf-8"))
	nav = next(t for t in tags if t.get("name") == "Navigation")
	items = nav["defaultValue"]["items"]
	boars = items[0]
	assert boars.get("label") == "Boars Head"
	by_label = {c.get("label"): c for c in boars.get("items") or []}
	for p in PLANTS:
		node = by_label.get(p["label"])
		if not node:
			raise SystemExit("missing nav node %s" % p["label"])
		node["data"] = {
			"action": "page",
			"page": p["page"],
			"viewPath": p["viewPath"],
			"tagPath": p["tagPath"],
		}
	for t in tags:
		if t.get("name") == "MapMarkerGeoJson":
			t["defaultValue"] = geojson_features()
			break
	TAGS.write_text(json.dumps(tags, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("updated tags Navigation + MapMarkerGeoJson")
	return nav["defaultValue"]["items"]


def sync_nav_views(items):
	for path in (NAV_VIEW, TEMP_NAV):
		view = json.loads(path.read_text(encoding="utf-8"))
		view["custom"]["items"] = items
		path.write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8", newline="\n")
		print("synced", path.relative_to(ROOT))


def write_placeholder_view():
	PLACEHOLDER_DIR.mkdir(parents=True, exist_ok=True)
	view = {
		"custom": {},
		"params": {"plantName": ""},
		"propConfig": {
			"params.plantName": {"paramDirection": "input", "persistent": True}
		},
		"props": {"defaultSize": {"height": 400, "width": 800}},
		"root": {
			"children": [
				{
					"meta": {"name": "Title"},
					"position": {"shrink": 0},
					"propConfig": {
						"props.text": {
							"binding": {
								"config": {
									"struct": {
										"name": "{view.params.plantName}",
										"path": "{page.props.path}",
									},
									"waitOnAll": True,
								},
								"transforms": [
									{
										"code": (
											"\tname = value['name'] or ''\n"
											"\tif name:\n"
											"\t\treturn str(name)\n"
											"\tpath = str(value['path'] or '')\n"
											"\treturn path.split('/')[-1].replace('-', ' ').title() or 'Plant'\n"
										).rstrip("\n"),
										"type": "script",
									}
								],
								"type": "expr-struct",
							}
						}
					},
					"props": {
						"text": "Plant",
						"style": {
							"classes": "font-title",
							"fontSize": "22px",
							"fontWeight": "700",
							"marginBottom": "8px",
						},
					},
					"type": "ia.display.label",
				},
				{
					"meta": {"name": "Body"},
					"position": {"shrink": 0},
					"props": {
						"text": "Plant overview coming soon.",
						"style": {"classes": "font-label", "fontSize": "14px"},
					},
					"type": "ia.display.label",
				},
			],
			"meta": {"name": "root", "contextMenu": {}},
			"props": {
				"direction": "column",
				"style": {
					"classes": "bg-page",
					"height": "100%",
					"padding": "24px",
					"width": "100%",
				},
			},
			"type": "ia.container.flex",
			"propConfig": {
				"meta.contextMenu.items": {
					"binding": {
						"config": {
							"struct": {"tagPath": '"No TagPath: "'},
							"waitOnAll": True,
						},
						"transforms": [
							{
								"code": (
									"\ttagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]\n"
									"\titems = [{\n"
									'\t\t"text": "Ticket Logger",\n'
									'\t\t"icon": {"path": "material/info", "color": "--neutral-80", "style": {}},\n'
									'\t\t"style": {"classes": "bg-component font-value", "height": 24, "width": 120},\n'
									'\t\t"type": "message",\n'
									'\t\t"children": [],\n'
									'\t\t"link": {"url": "", "target": "self"},\n'
									'\t\t"method": {"name": "", "params": {}},\n'
									'\t\t"message": {\n'
									'\t\t\t"type": "ticketLog",\n'
									'\t\t\t"payload": {"tagPath": tagPath, "viewName": self.view.id.split(\'@\')[0]},\n'
									'\t\t\t"scope": "page"\n'
									"\t\t}\n"
									"\t}]\n"
									"\treturn items"
								),
								"type": "script",
							}
						],
						"type": "expr-struct",
					}
				},
				"meta.contextMenu.enabled": {
					"binding": {
						"config": {
							"struct": {
								"items": "{this.meta.contextMenu.items}",
								"permission": "{session.custom.TicketLogAccess}",
							},
							"waitOnAll": True,
						},
						"transforms": [
							{
								"expression": "len({value}['items']) > 0 && {value}['permission']",
								"type": "expression",
							}
						],
						"type": "expr-struct",
					}
				},
			},
			"scripts": {
				"customMethods": [],
				"extensionFunctions": None,
				"messageHandlers": [
					{
						"messageType": "ticketLog",
						"pageScope": True,
						"script": (
							"\tshared.Alerts.contextMenuTicketLog("
							"payload['tagPath'], payload['viewName'])"
						),
						"sessionScope": False,
						"viewScope": False,
					}
				],
			},
		},
	}
	(PLACEHOLDER_DIR / "view.json").write_text(
		json.dumps(view, indent=2) + "\n", encoding="utf-8", newline="\n"
	)
	(PLACEHOLDER_DIR / "resource.json").write_text(
		json.dumps(
			{
				"scope": "G",
				"version": 1,
				"restricted": False,
				"overridable": True,
				"files": ["view.json"],
				"attributes": {
					"lastModificationSignature": "0" * 64,
					"lastModification": {
						"actor": "cursor",
						"timestamp": "2026-08-01T19:10:00Z",
					},
				},
			},
			indent=2,
		)
		+ "\n",
		encoding="utf-8",
		newline="\n",
	)
	print("wrote PlantPlaceholder view")


def update_page_config():
	cfg = json.loads(PAGE_CONFIG.read_text(encoding="utf-8"))
	for p in PLANTS:
		if not p["placeholder"]:
			continue
		cfg["pages"][p["page"]] = {
			"title": p["label"],
			"viewPath": "00_Pages/LandingPage/PlantPlaceholder",
			"viewParams": {"plantName": p["label"]},
		}
	PAGE_CONFIG.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("updated page-config plant routes")


def patch_globe_js():
	cfg = json.loads(GLOBE_INDEX.read_text(encoding="utf-8"))
	html = cfg["text"].replace("\r\n", "\n").replace("\r", "\n")

	# rowFromFeature — include page/action
	old_row = (
		"    return {\n"
		"      id:  f.properties.name,\n"
		"      fill: f.properties.color,\n"
		"      name: f.properties && f.properties.name ? f.properties.name : \"\",\n"
		"      lat, lng,\n"
		"      viewPath: f.properties.viewPath,\n"
		"      tagPath:  f.properties.tagPath\n"
		"    };"
	)
	new_row = (
		"    return {\n"
		"      id:  f.properties.name,\n"
		"      fill: f.properties.color,\n"
		"      name: f.properties && f.properties.name ? f.properties.name : \"\",\n"
		"      lat, lng,\n"
		"      viewPath: f.properties.viewPath,\n"
		"      tagPath:  f.properties.tagPath,\n"
		"      page: f.properties.page || \"\",\n"
		"      action: f.properties.action || \"page\"\n"
		"    };"
	)
	if old_row not in html:
		raise SystemExit("rowFromFeature block not found")
	html = html.replace(old_row, new_row, 1)

	# click POST body
	old_body = 'body: JSON.stringify({viewPath: dc.viewPath, tagPath: dc.tagPath})'
	new_body = (
		"body: JSON.stringify({"
		"viewPath: dc.viewPath, tagPath: dc.tagPath, "
		"page: dc.page || \"\", action: dc.action || \"page\""
		"})"
	)
	if old_body not in html:
		raise SystemExit("click POST body not found")
	html = html.replace(old_body, new_body, 1)

	# store page/action on sprite
	old_set = "    g.setAll({\n      viewPath: dc.viewPath,\n      tagPath:  dc.tagPath\n    });"
	new_set = (
		"    g.setAll({\n"
		"      viewPath: dc.viewPath,\n"
		"      tagPath:  dc.tagPath,\n"
		"      page: dc.page,\n"
		"      action: dc.action\n"
		"    });"
	)
	if old_set in html:
		html = html.replace(old_set, new_set, 1)
	else:
		print("warn: sprite setAll block not found (optional)")

	cfg["text"] = html
	GLOBE_INDEX.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("patched globe index JS")


def wire_globe_view():
	view = json.loads(GLOBE_VIEW.read_text(encoding="utf-8"))
	view.setdefault("custom", {})["navData"] = {}
	view.setdefault("propConfig", {})
	view["propConfig"]["custom.navData"] = {
		"binding": {
			"config": {
				"fallbackDelay": 2.5,
				"mode": "direct",
				"tagPath": "[default]_Config/MapMarkerNavigation",
			},
			"transforms": [
				{
					"expression": 'if(isNull({value}),\n\t"",{value})',
					"type": "expression",
				}
			],
			"type": "tag",
		},
		"onChange": {"enabled": None, "script": NAV_ONCHANGE.rstrip("\n")},
		"persistent": True,
	}
	GLOBE_VIEW.write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("wired Globe view MapMarkerNavigation handler")


def main():
	items = update_tags()
	sync_nav_views(items)
	write_placeholder_view()
	update_page_config()
	patch_globe_js()
	wire_globe_view()
	# payloads for live tag writes
	Path(".tmp-mapmarkers.json").write_text(
		json.dumps(geojson_features()), encoding="utf-8"
	)
	Path(".tmp-nav-write.json").write_text(
		json.dumps({"__nav": True, "items": items}), encoding="utf-8"
	)
	print("wrote .tmp-mapmarkers.json and .tmp-nav-write.json")


if __name__ == "__main__":
	main()
