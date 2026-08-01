# -*- coding: utf-8 -*-
"""Wire BH globe: fix HTML, add markers tags, create home Perspective view, page-config."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BH = ROOT / "gateways/standard/data/projects/BH"
GLOBE_INDEX = BH / "com.inductiveautomation.webdev/resources/globe/index/config.json"
TAGS = ROOT / (
	"gateways/standard/data/config/resources/core/"
	"ignition/tag-definition/default/_Config/tags.json"
)
PAGE_CONFIG = BH / "com.inductiveautomation.perspective/page-config/config.json"
VIEW_DIR = BH / "com.inductiveautomation.perspective/views/00_Pages/LandingPage/Globe"

TICKET_ITEMS_CODE = (
	"\ttagPath = ''\n"
	"\ttry:\n"
	"\t\ttagPath = self.view.params.tagPath\n"
	"\texcept:\n"
	"\t\tpass\n"
	"\tif tagPath is None or str(tagPath).strip() == '':\n"
	"\t\ttagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]\n"
	"\titems = [\n"
	"\t\t\t  {\n"
	'\t\t\t    "text": "Ticket Logger",\n'
	'\t\t\t    "icon": {\n'
	'\t\t\t      "path": "material/info",\n'
	'\t\t\t      "color": "--neutral-80",\n'
	'\t\t\t      "style": {}\n'
	"\t\t\t    },\n"
	'\t\t\t    "style": {\n'
	'\t\t\t      "classes": "bg-component font-value",\n'
	'\t\t\t      "height": 24,\n'
	'\t\t\t      "width": 120\n'
	"\t\t\t    },\n"
	'\t\t\t    "type": "message",\n'
	'\t\t\t    "children": [],\n'
	'\t\t\t    "link": {\n'
	'\t\t\t      "url": "",\n'
	'\t\t\t      "target": "self"\n'
	"\t\t\t    },\n"
	'\t\t\t    "method": {\n'
	'\t\t\t      "name": "",\n'
	'\t\t\t      "params": {}\n'
	"\t\t\t    },\n"
	'\t\t\t    "message": {\n'
	'\t\t\t      "type": "ticketLog",\n'
	'\t\t\t      "payload": {\n'
	'\t\t\t        "tagPath": tagPath,\n'
	"\t\t\t        \"viewName\": self.view.id.split('@')[0]\n"
	"\t\t\t      },\n"
	'\t\t\t      "scope": "page"\n'
	"\t\t\t    }\n"
	"\t\t\t  }\n"
	"\t\t\t]\n"
	"\treturn items"
)

IFRAME_SRC_CODE = (
	"\ttheme = str(value['theme'] or 'light-cool').lower()\n"
	"\t# Match ChangeTheme aliases so globe CSS includes BH tokens (--ct-water, etc.).\n"
	"\tif theme == 'light':\n"
	"\t\ttheme = 'light-cool'\n"
	"\telif theme == 'dark':\n"
	"\t\ttheme = 'dark-cool'\n"
	"\treturn '/system/webdev/BH/globe/index?theme=' + theme + '#NoAlarms'\n"
)

NESTED_APPLY_THEME = """  function applyTheme(theme) {
    const t = (theme || 'light').toLowerCase();
    document.getElementById('vars-light').disabled       = (t !== 'light');
    document.getElementById('vars-light-warm').disabled  = (t !== 'light-warm');
    document.getElementById('vars-light-cool').disabled  = (t !== 'light-cool');
    document.getElementById('vars-dark').disabled        = (t !== 'dark');
    document.getElementById('vars-dark-warm').disabled   = (t !== 'dark-warm');
    document.getElementById('vars-dark-cool').disabled   = (t !== 'dark-cool');
    document.documentElement.dataset.theme = t;
  }"""


def fix_globe_index() -> None:
	cfg = json.loads(GLOBE_INDEX.read_text(encoding="utf-8"))
	html = cfg["text"].replace("\r\n", "\n").replace("\r", "\n")

	# Replace incomplete nested applyTheme inside am5.ready
	old_nested = re.compile(
		r"  function applyTheme\(theme\) \{\n"
		r"    const t = theme\.toLowerCase\(\);\n"
		r"    document\.getElementById\('vars-light'\)\.disabled = \(t !== 'light'\);\n"
		r"    document\.getElementById\('vars-dark'\)\.disabled  = \(t !== 'dark'\);\n"
		r"    document\.getElementById\('vars-dark-warm'\)\.disabled  = \(t !== 'dark-warm'\);\n"
		r"    document\.getElementById\('vars-light-warm'\)\.disabled  = \(t !== 'light-warm'\);\n"
		r"    document\.documentElement\.dataset\.theme = t;\n"
		r"  \}"
	)
	html2, n = old_nested.subn(NESTED_APPLY_THEME, html, count=1)
	if n != 1:
		# already fixed or format drifted — try looser replace of first incomplete block
		if "vars-light-cool" not in html.split("am5.ready")[1][:800]:
			raise SystemExit("could not patch nested applyTheme (%d matches)" % n)
		html2 = html

	# Theme-aware tooltip chrome
	replacements = [
		(
			"fill: am5.color(0xFFFFFF),\n    stroke: cssVar('--globe-land-stroke', '#4D5358'),",
			"fill: cssVar('--neutral-10', '#FFFFFF'),\n    stroke: cssVar('--globe-land-stroke', '#4D5358'),",
		),
		(
			"fill: am5.color(0x555555),\n      fillOpacity: 1,\n      cornerRadiusTL: 6, cornerRadiusTR: 6, cornerRadiusBL: 0, cornerRadiusBR: 0",
			"fill: cssVar('--neutral-80', '#343A3F'),\n      fillOpacity: 1,\n      cornerRadiusTL: 6, cornerRadiusTR: 6, cornerRadiusBL: 0, cornerRadiusBR: 0",
		),
		(
			"fill: am5.color(0x000000),\n      fillOpacity: 1,\n      cornerRadiusBL: 6, cornerRadiusBR: 6, cornerRadiusTL: 0, cornerRadiusTR: 0",
			"fill: cssVar('--neutral-90', '#21272A'),\n      fillOpacity: 1,\n      cornerRadiusBL: 6, cornerRadiusBR: 6, cornerRadiusTL: 0, cornerRadiusTR: 0",
		),
		(
			'fill: am5.color(0xffffff),\n    position: "relative"\n  });\n\n  let nameLabel',
			'fill: cssVar(\'--neutral-10\', \'#FFFFFF\'),\n    position: "relative"\n  });\n\n  let nameLabel',
		),
		(
			'fill: am5.color(0xffffff),\n    paddingTop: 0,\n    paddingLeft: 6,',
			'fill: cssVar(\'--neutral-10\', \'#FFFFFF\'),\n    paddingTop: 0,\n    paddingLeft: 6,',
		),
		(
			'fill: am5.color(0xffffff),\n    position: "relative",\n    centerY: am5.percent(50),\n    y: am5.percent(50)\n  });\n\n\n  let row1_status',
			'fill: cssVar(\'--neutral-10\', \'#FFFFFF\'),\n    position: "relative",\n    centerY: am5.percent(50),\n    y: am5.percent(50)\n  });\n\n\n  let row1_status',
		),
		(
			"fill: am5.color(0x008FFB),",
			"fill: cssVar('--globe-marker', '#114599'),",
		),
		(
			"return am5.color(0x000000);",
			"return cssVar('--globe-marker', '#114599');",
		),
	]
	for a, b in replacements:
		if a not in html2:
			print("warn: skip replace missing:", a[:60].replace("\n", " "))
			continue
		html2 = html2.replace(a, b, 1)

	cfg["text"] = html2
	GLOBE_INDEX.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("fixed", GLOBE_INDEX)


SAMPLE_GEOJSON = {
	"type": "FeatureCollection",
	"features": [
		{
			"type": "Feature",
			"geometry": {
				"coordinates": [-82.943375287534, 39.83741622205],
				"type": "Point",
			},
			"properties": {
				"color": "#114599",
				"viewPath": "00_Pages/Machine Room/Overview",
				"tagPath": "[default]Plant/Machine Room",
				"name": "Groveport OH",
			},
		},
		{
			"type": "Feature",
			"geometry": {
				"coordinates": [-85.385006308166, 39.873372394315],
				"type": "Point",
			},
			"properties": {
				"color": "#114599",
				"viewPath": "00_Pages/Machine Room/Overview",
				"tagPath": "[default]Plant/Machine Room",
				"name": "New Castle IN",
			},
		},
		{
			"type": "Feature",
			"geometry": {
				"coordinates": [-90.811739063343, 34.995907752639],
				"type": "Point",
			},
			"properties": {
				"color": "#114599",
				"viewPath": "00_Pages/Machine Room/Overview",
				"tagPath": "[default]Plant/Machine Room",
				"name": "Forrest City AR",
			},
		},
		{
			"type": "Feature",
			"geometry": {
				"coordinates": [-77.414445481263, 37.176357413569],
				"type": "Point",
			},
			"properties": {
				"color": "#114599",
				"viewPath": "00_Pages/Machine Room/Overview",
				"tagPath": "[default]Plant/Machine Room",
				"name": "Petersburg VA",
			},
		},
		{
			"type": "Feature",
			"geometry": {
				"coordinates": [-86.096160011663, 42.80339475283],
				"type": "Point",
			},
			"properties": {
				"color": "#114599",
				"viewPath": "00_Pages/Machine Room/Overview",
				"tagPath": "[default]Plant/Machine Room",
				"name": "Holland MI",
			},
		},
	],
}


def ensure_marker_tags() -> None:
	tags = json.loads(TAGS.read_text(encoding="utf-8"))
	names = {t.get("name") for t in tags}
	changed = False
	if "MapMarkerNavigation" not in names:
		tags.append(
			{
				"valueSource": "memory",
				"dataType": "Document",
				"name": "MapMarkerNavigation",
				"defaultValue": {},
				"tagType": "AtomicTag",
			}
		)
		changed = True
	if "MapMarkerGeoJson" not in names:
		tags.append(
			{
				"valueSource": "memory",
				"dataType": "Document",
				"name": "MapMarkerGeoJson",
				"defaultValue": SAMPLE_GEOJSON,
				"tagType": "AtomicTag",
			}
		)
		changed = True
	else:
		for t in tags:
			if t.get("name") == "MapMarkerGeoJson":
				t["defaultValue"] = SAMPLE_GEOJSON
				changed = True
				break
	if changed:
		TAGS.write_text(json.dumps(tags, indent=2) + "\n", encoding="utf-8", newline="\n")
		print("updated", TAGS)
	else:
		print("tags already present")


def write_globe_view() -> None:
	VIEW_DIR.mkdir(parents=True, exist_ok=True)
	view = {
		"custom": {
			"theme": "",
		},
		"params": {},
		"propConfig": {
			"custom.theme": {
				"binding": {
					"config": {
						"path": "session.props.theme",
					},
					"type": "property",
				},
				"persistent": True,
			}
		},
		"props": {
			"defaultSize": {
				"height": 900,
				"width": 1600,
			}
		},
		"root": {
			"children": [
				{
					"meta": {"name": "IFrame"},
					"position": {"grow": 1},
					"propConfig": {
						"props.src": {
							"binding": {
								"config": {
									"struct": {
										"theme": "{view.custom.theme}",
									},
									"waitOnAll": True,
								},
								"transforms": [
									{
										"code": IFRAME_SRC_CODE.rstrip("\n"),
										"type": "script",
									}
								],
								"type": "expr-struct",
							}
						}
					},
					"props": {
						"allowFullScreen": True,
						"style": {
							"height": "100%",
							"width": "100%",
						},
					},
					"type": "ia.display.iframe",
				}
			],
			"meta": {
				"name": "root",
				"contextMenu": {},
			},
			"props": {
				"direction": "column",
				"style": {
					"classes": "bg-page",
					"height": "100%",
					"overflow": "hidden",
					"width": "100%",
				},
			},
			"type": "ia.container.flex",
			"propConfig": {
				"meta.contextMenu.items": {
					"binding": {
						"config": {
							"struct": {
								"tagPath": '"No TagPath: "',
							},
							"waitOnAll": True,
						},
						"transforms": [
							{
								"code": TICKET_ITEMS_CODE,
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
							"\t# Ticket Logger context-menu opener\n"
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
	(VIEW_DIR / "view.json").write_text(
		json.dumps(view, indent=2) + "\n", encoding="utf-8", newline="\n"
	)
	(VIEW_DIR / "resource.json").write_text(
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
						"timestamp": "2026-08-01T18:45:00Z",
					},
				},
			},
			indent=2,
		)
		+ "\n",
		encoding="utf-8",
		newline="\n",
	)
	print("wrote", VIEW_DIR)


def update_page_config() -> None:
	cfg = json.loads(PAGE_CONFIG.read_text(encoding="utf-8"))
	cfg["pages"]["/"] = {
		"title": "Home",
		"viewPath": "00_Pages/LandingPage/Globe",
	}
	# Keep a direct plant entry if Plant view appears later; Machine Room already at /machine-room
	PAGE_CONFIG.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("updated", PAGE_CONFIG)


def main() -> None:
	fix_globe_index()
	ensure_marker_tags()
	write_globe_view()
	update_page_config()


if __name__ == "__main__":
	main()
