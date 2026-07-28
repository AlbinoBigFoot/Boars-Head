# -*- coding: utf-8 -*-
"""Structural checks for Adhoc Trend multi-plot views."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BH = ROOT / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
TREND = BH / "views/98_Configuration/AdhocTrend/Trend/view.json"
PLOT = BH / "views/98_Configuration/AdhocTrend/_Assets/Plot/view.json"
PENPLOT = BH / "views/98_Configuration/AdhocTrend/_Assets/PenPlot/view.json"
CSS = BH / "stylesheet/stylesheet.css"


def find(node, name):
	if isinstance(node, dict):
		if node.get("meta", {}).get("name") == name:
			return node
		for c in node.get("children") or []:
			r = find(c, name)
			if r:
				return r
	return None


def assert_true(cond, msg):
	if not cond:
		raise AssertionError(msg)


def no_cr(obj, path="$"):
	if isinstance(obj, dict):
		for k, v in obj.items():
			if k in ("code", "script", "expression") and isinstance(v, str):
				assert_true("\r" not in v, "%s.%s has CR" % (path, k))
			else:
				no_cr(v, path + "." + k)
	elif isinstance(obj, list):
		for i, v in enumerate(obj):
			no_cr(v, "%s[%d]" % (path, i))


def tab_scripts(obj):
	if isinstance(obj, dict):
		for k, v in obj.items():
			if k in ("code", "script") and isinstance(v, str) and v.strip():
				for line in v.split("\n"):
					if not line:
						continue
					assert_true(line.startswith("\t") or line.startswith("#"), "non-tab script line: %r" % line[:40])
			else:
				tab_scripts(v)
	elif isinstance(obj, list):
		for v in obj:
			tab_scripts(v)


def main():
	trend = json.loads(TREND.read_text(encoding="utf-8"))
	plot = json.loads(PLOT.read_text(encoding="utf-8"))
	penplot = json.loads(PENPLOT.read_text(encoding="utf-8"))
	css = CSS.read_text(encoding="utf-8")

	no_cr(trend)
	no_cr(plot)
	no_cr(penplot)
	tab_scripts(trend)
	tab_scripts(plot)
	tab_scripts(penplot)

	t = find(trend["root"], "Trend")
	assert_true(t and t.get("type") == "ia.container.flex", "Trend not flex")
	assert_true((t.get("props") or {}).get("direction") == "column", "Trend not column")
	assert_true(find(t, "apexchart") is None, "apexchart still on Trend")
	tb = find(t, "PlotToolbar")
	assert_true(tb is not None, "PlotToolbar missing")
	assert_true((tb.get("position") or {}).get("basis") == "48px", "toolbar not 48px")
	icons = find(t, "Icons")
	buttons = find(t, "Buttons")
	assert_true(not ((icons.get("propConfig") or {}).get("position.height")), "Icons still % height")
	assert_true(not ((buttons.get("propConfig") or {}).get("position.height")), "Buttons still % height")
	kids = buttons.get("children") or []
	assert_true(kids and kids[0].get("meta", {}).get("name") == "AddPlot", "AddPlot not first")
	add = kids[0]
	assert_true((add.get("props") or {}).get("text") == "", "AddPlot has text")
	assert_true(
		((add.get("props") or {}).get("image") or {}).get("icon", {}).get("path") == "material/add",
		"AddPlot icon",
	)
	plots = find(t, "Plots")
	assert_true(plots.get("type") == "ia.display.flex-repeater", "Plots not repeater")
	assert_true((plots.get("props") or {}).get("path", "").endswith("_Assets/Plot"), "Plots path")
	assert_true(((plots.get("props") or {}).get("elementPosition") or {}).get("grow") == 1, "elementPosition")

	pc = trend.get("propConfig") or {}
	for k in ("custom.key", "custom.dataset", "custom.realTimeDataset", "custom.historicalDataset"):
		assert_true(k not in pc, "leftover %s" % k)

	table = find(trend["root"], "Table")
	fields = [c.get("field") for c in ((table.get("props") or {}).get("columns") or [])]
	assert_true("plotId" in fields, "plotId column missing")

	# Plot ticket logger
	assert_true("ticketLog" in json.dumps(plot.get("handlers") or plot), "Plot ticketLog")
	assert_true("ticketLog" in json.dumps(penplot.get("handlers") or penplot), "PenPlot ticketLog")

	assert_true(".psc-adhoc-trend-plots" in css, "css plots")
	assert_true("min-height: 0" in css, "css min-height")
	assert_true(".psc-adhoc-trend-add-plot-btn" in css, "css add btn")

	print("views OK")


if __name__ == "__main__":
	main()
