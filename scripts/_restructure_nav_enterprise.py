# -*- coding: utf-8 -*-
"""Restructure BH Navigation for enterprise → plant hierarchy."""
from __future__ import annotations

import copy
import json
from pathlib import Path

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

ICON = {
	"color": "",
	"path": "material/location_on",
	"style": {"classes": "", "height": "18px", "width": "18px"},
}
ICON_DOMAIN = {
	"color": "",
	"path": "material/domain",
	"style": {"classes": "", "height": "18px", "width": "18px"},
}
ICON_BUILD = {
	"color": "",
	"path": "material/build",
	"style": {"classes": "", "height": "18px", "width": "18px"},
}
ICON_ALARM = {
	"color": "",
	"path": "material/notifications_active",
	"style": {"classes": "", "height": "18px", "width": "18px"},
}
ICON_TREND = {
	"color": "",
	"path": "material/show_chart",
	"style": {"classes": "", "height": "18px", "width": "18px"},
}


def node(label, *, page="", action="", view_path="", tag_path="", icon=None, expanded=False, items=None, admin_only=None):
	data = {
		"action": action,
		"page": page,
		"viewPath": view_path,
		"tagPath": tag_path,
	}
	if admin_only is not None:
		data["adminOnly"] = admin_only
	return {
		"label": label,
		"expanded": expanded,
		"icon": copy.deepcopy(icon or ICON),
		"data": data,
		"items": items if items is not None else [],
	}


def find_label(items, label):
	for it in items:
		if it.get("label") == label:
			return it
	return None


def enterprise_ops():
	return node(
		"Enterprise Operations",
		action="",
		page="",
		icon=ICON_BUILD,
		expanded=False,
		items=[
			node("Alarm Status", action="page", page="/alarms", icon=ICON_ALARM),
			node("Alarm Journal", action="page", page="/alarms/journal", icon=ICON_ALARM),
			node("AdHoc Trend", action="page", page="/trending", icon=ICON_TREND),
		],
	)


def placeholder_plant(label):
	return node(label, action="", page="", icon=ICON_DOMAIN, expanded=False, items=[])


def build_tree(old_items):
	plant = find_label(old_items, "Plant")
	ops = find_label(old_items, "Operations")
	if not plant:
		raise SystemExit("Plant node missing from current Navigation")
	if not ops:
		raise SystemExit("Operations node missing from current Navigation")

	# Plant children (areas) stay under Groveport; Operations moves under Groveport as plant ops.
	plant_children = copy.deepcopy(plant.get("items") or [])
	plant_ops = copy.deepcopy(ops)
	plant_ops["label"] = "Operations"
	# Keep full plant ops list as-is (alarms, journal, trending, saved, audit, L5K)

	groveport = node(
		"Groveport",
		action="page",
		page="/machine-room",
		view_path="00_Pages/Machine Room/Overview",
		icon=ICON_DOMAIN,
		expanded=True,
		items=plant_children + [plant_ops],
	)

	return [
		node(
			"Boars Head",
			action="page",
			page="/",
			icon=ICON,
			expanded=True,
			items=[
				groveport,
				placeholder_plant("New Castle"),
				placeholder_plant("Forrest City"),
				placeholder_plant("Petersburg"),
				placeholder_plant("Holland"),
				enterprise_ops(),
			],
		)
	]


BRAND_CODE = (
	"\tpath = ''\n"
	"\ttry:\n"
	"\t\tpath = str(value)\n"
	"\texcept:\n"
	"\t\tpath = ''\n"
	"\tif path == '/' or path == '':\n"
	"\t\treturn 'Boars Head International'\n"
	"\treturn 'Groveport'\n"
)


def update_brand(view):
	"""Bind Brand label text to page path."""
	# Find Brand component under root children
	root = view.get("root") or {}
	children = root.get("children") or []
	brand = None
	for c in children:
		if (c.get("meta") or {}).get("name") == "Brand":
			brand = c
			break
	if brand is None:
		raise SystemExit("Brand component not found in Navigation view")

	brand.setdefault("propConfig", {})
	brand["propConfig"]["props.text"] = {
		"binding": {
			"config": {"path": "page.props.path"},
			"transforms": [{"code": BRAND_CODE.rstrip("\n"), "type": "script"}],
			"type": "property",
		}
	}
	# Keep a sensible default for Designer
	brand.setdefault("props", {})["text"] = "Boars Head International"


def write_nav_items(items):
	tags = json.loads(TAGS.read_text(encoding="utf-8"))
	for t in tags:
		if t.get("name") == "Navigation":
			t["defaultValue"] = {"items": items}
			break
	else:
		raise SystemExit("Navigation tag missing")
	TAGS.write_text(json.dumps(tags, indent=2) + "\n", encoding="utf-8", newline="\n")
	print("updated", TAGS)

	for path in (NAV_VIEW, TEMP_NAV):
		if not path.exists():
			print("skip missing", path)
			continue
		view = json.loads(path.read_text(encoding="utf-8"))
		view.setdefault("custom", {})["items"] = items
		# Clear any stale props.items snapshot — binding rebuilds from custom.items
		tree = None
		for c in (view.get("root") or {}).get("children") or []:
			if (c.get("meta") or {}).get("name") in ("Tree", "NavTree", "NavigationTree"):
				tree = c
				break
			# nested search one level
			for cc in c.get("children") or []:
				if (cc.get("meta") or {}).get("name") in ("Tree", "NavTree", "NavigationTree"):
					tree = cc
					break
		# Also search by type
		if tree is None:
			def find_tree(nodes):
				for n in nodes or []:
					if n.get("type") == "ia.display.tree":
						return n
					found = find_tree(n.get("children"))
					if found:
						return found
				return None

			tree = find_tree((view.get("root") or {}).get("children"))

		if path == NAV_VIEW:
			update_brand(view)

		path.write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8", newline="\n")
		print("updated", path)


def main():
	tags = json.loads(TAGS.read_text(encoding="utf-8"))
	nav = next(t for t in tags if t.get("name") == "Navigation")
	old = nav["defaultValue"]["items"]
	# If already restructured, rebuild from Groveport children if possible
	boars = find_label(old, "Boars Head")
	if boars:
		print("already has Boars Head root — rebuilding from current tree")
		grove = find_label(boars.get("items") or [], "Groveport")
		if grove:
			# Reconstruct fake Plant/Ops for rebuild
			g_items = grove.get("items") or []
			ops = find_label(g_items, "Operations")
			areas = [i for i in g_items if i.get("label") != "Operations"]
			old = [
				{"label": "Plant", "items": areas, "data": {}, "icon": ICON, "expanded": True},
				ops
				or find_label(boars.get("items") or [], "Enterprise Operations")
				or {"label": "Operations", "items": [], "data": {}, "icon": ICON_BUILD},
			]
			if old[1].get("label") == "Enterprise Operations":
				# Prefer plant ops under grove if present; else keep empty ops shell
				pass

	new_items = build_tree(old)
	write_nav_items(new_items)

	def walk(nodes, indent=0):
		for n in nodes:
			d = n.get("data") or {}
			print(
				"  " * indent
				+ n.get("label", "?")
				+ " | %s %s" % (d.get("action"), d.get("page"))
			)
			walk(n.get("items") or [], indent + 1)

	print("--- new tree ---")
	walk(new_items)


if __name__ == "__main__":
	main()
