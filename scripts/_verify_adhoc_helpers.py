# -*- coding: utf-8 -*-
"""Verify shared.AdhocTrend helpers without a live Ignition gateway."""
from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py"


class _DS:
	def __init__(self, headers, rows):
		self._headers = list(headers)
		self._rows = [list(r) for r in rows]

	def getRowCount(self):
		return len(self._rows)

	def getColumnNames(self):
		return list(self._headers)

	def getValueAt(self, r, c):
		if isinstance(c, str):
			c = self._headers.index(c)
		return self._rows[r][c]


class _PyRow(dict):
	pass


def _install_system():
	system = types.ModuleType("system")
	tag = types.ModuleType("system.tag")
	dataset = types.ModuleType("system.dataset")

	def readBlocking(paths):
		out = []
		for p in paths:
			val = None
			ps = str(p)
			if ps.endswith(".DataType"):
				if "Status" in ps or "CMD" in ps or "Fault" in ps:
					val = "Boolean"
				elif "Pressure" in ps or "Temp" in ps or "SPD" in ps:
					val = "Float4"
				else:
					val = "Float4"
			elif ps.endswith(".EngUnit"):
				val = "psi" if "Pressure" in ps else ""
			out.append(types.SimpleNamespace(value=val))
		return out

	def toDataSet(headers, rows):
		return _DS(headers, rows)

	def toPyDataSet(ds):
		rows = []
		for r in range(ds.getRowCount()):
			row = _PyRow()
			for h in ds.getColumnNames():
				row[h] = ds.getValueAt(r, h)
			rows.append(row)
		return rows

	def filterColumns(ds, cols):
		idxs = [ds.getColumnNames().index(c) for c in cols]
		rows = [[ds.getValueAt(r, i) for i in idxs] for r in range(ds.getRowCount())]
		return _DS(cols, rows)

	tag.readBlocking = readBlocking
	dataset.toDataSet = toDataSet
	dataset.toPyDataSet = toPyDataSet
	dataset.filterColumns = filterColumns
	system.tag = tag
	system.dataset = dataset
	sys.modules["system"] = system
	sys.modules["system.tag"] = tag
	sys.modules["system.dataset"] = dataset


def _load():
	_install_system()
	spec = importlib.util.spec_from_file_location("AdhocTrend", CODE)
	mod = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(mod)
	return mod


def assert_eq(a, b, msg):
	if a != b:
		raise AssertionError("%s: %r != %r" % (msg, a, b))


def main():
	m = _load()
	assert_eq(m.pen_label("[default]Evaporators/EV-01/Pressure/Value"), "EV-01", "pressure value")
	assert_eq(m.pen_label("[default]Evaporators/EV-01/Pressure"), "EV-01", "pressure")
	assert_eq(m.pen_label("[default]Compressors/AU5-C1/Suction/Value"), "AU5-C1", "suction")
	assert_eq(m.pen_label("[default]Misc/SomeTag/Value"), "SomeTag", "shallow")
	assert_eq(m.pen_label("[default]LoneTag"), "LoneTag", "lone")
	labels = m.pen_labels([
		"[default]Evaporators/EV-01/Pressure/Value",
		"[default]Evaporators/EV-01/Temp/Value",
	])
	assert_eq(labels, ["EV-01 Pressure", "EV-01 Temp"], "disambiguate")

	cfg = {"plots": m.default_plots(), "penPlots": {}}
	pid = m.add_plot(cfg)
	assert_eq(pid, "p1", "new plot id")
	assert_eq(len(m.plain_plots(cfg)), 2, "two plots")
	plots = m.apply_add_plot(cfg)
	assert_eq(len(plots), 3, "apply_add_plot")
	assert isinstance(plots[0], dict), "plain dict"

	pp = m.move_pen(cfg, "Evaporators-EV_01-Pressure", "p1")
	assert_eq(pp.get("Evaporators-EV_01-Pressure"), "p1", "move_pen")

	ok, msg = m.remove_plot(cfg, "p1")
	assert_eq(ok, False, "refuse remove plot with pens")
	if "Move or remove" not in msg:
		raise AssertionError("remove message: %r" % msg)

	cfg2 = {
		"plots": [
			{"id": "p0", "title": "Plot 1", "kind": "analog"},
			{"id": "p1", "title": "Plot 2", "kind": "analog"},
		],
		"penPlots": {},
	}
	ok, _ = m.remove_plot(cfg2, "p1")
	assert_eq(ok, True, "remove empty")
	ok, _ = m.remove_plot(cfg2, "p0")
	assert_eq(ok, False, "keep one")

	cfg3 = {"plots": m.default_plots(), "penPlots": {}}
	_, plots, penPlots = m.route_new_tag(cfg3, "[default]X/EV-01/Status/Value", data_type="Boolean")
	assert any(p["kind"] == "discrete" for p in plots), "status plot created"
	assert penPlots, "pen assigned"

	# no magnitude APIs
	for bad in ("needs_dual_plot", "scale_groups", "RANGE_RATIO_THRESHOLD", "_magnitude_bucket"):
		if hasattr(m, bad):
			raise AssertionError("magnitude API present: %s" % bad)

	print("helpers OK")


if __name__ == "__main__":
	main()
