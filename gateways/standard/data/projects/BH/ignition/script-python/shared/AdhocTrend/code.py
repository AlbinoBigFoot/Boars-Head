"""Adhoc trend helpers — multi-plot scaling for ApexCharts.

When enabled pens use incompatible scales (different eng units, or value
ranges that would squash smaller series), split pens across two plots so the
chart stays readable.
"""

import math


RANGE_RATIO_THRESHOLD = 10.0


def _as_bool(value):
	if value in (True, "true", "True", "TRUE", 1, "1"):
		return True
	return False


def resolve_column(dataset, alias):
	"""Map a pen alias to a dataset column name (BH historian aliases vary)."""
	if dataset is None or alias in (None, ""):
		return None
	try:
		cols = list(dataset.getColumnNames())
	except Exception:
		return None
	if alias in cols:
		return alias
	leaf = str(alias).split("-")[-1]
	for c in cols:
		if c == "t_stamp":
			continue
		if c == leaf or str(c).endswith(leaf) or (leaf and leaf in str(c)):
			return c
	return None


def _column_extent(dataset, column):
	"""Return (min, max) for numeric values in column, or None."""
	try:
		rows = dataset.getRowCount()
		col_idx = list(dataset.getColumnNames()).index(column)
	except Exception:
		return None
	lo = None
	hi = None
	for r in range(rows):
		try:
			v = dataset.getValueAt(r, col_idx)
		except Exception:
			continue
		if v is None:
			continue
		try:
			f = float(v)
		except Exception:
			continue
		if lo is None or f < lo:
			lo = f
		if hi is None or f > hi:
			hi = f
	if lo is None or hi is None:
		return None
	return (lo, hi)


def _magnitude_bucket(extent):
	if not extent:
		return "m:na"
	lo, hi = extent
	span = max(abs(lo), abs(hi), abs(hi - lo), 1e-9)
	try:
		return "m:%d" % int(math.floor(math.log10(span)))
	except Exception:
		return "m:na"


def _pen_scale_key(pen, dataset):
	eu = ""
	try:
		eu = pen["engUnit"]
	except Exception:
		eu = ""
	if eu is None:
		eu = ""
	eu = str(eu).strip()
	if eu:
		return "u:%s" % eu.lower()

	alias = None
	try:
		alias = pen["alias"]
	except Exception:
		alias = None
	col = resolve_column(dataset, alias)
	if col is None:
		return "u:"
	return _magnitude_bucket(_column_extent(dataset, col))


def _enabled_pens(pens):
	if pens is None:
		return []
	try:
		if pens.getRowCount() <= 0:
			return []
	except Exception:
		return []
	out = []
	for pen in system.dataset.toPyDataSet(pens):
		try:
			enabled = pen["penEnabled"]
		except Exception:
			enabled = False
		if _as_bool(enabled):
			out.append(pen)
	return out


def scale_groups(dataset, pens):
	"""Ordered list of (scale_key, [pen, ...]) for enabled pens with data cols."""
	groups = []
	index = {}
	for pen in _enabled_pens(pens):
		try:
			alias = pen["alias"]
		except Exception:
			alias = None
		if alias in (None, ""):
			continue
		if resolve_column(dataset, alias) is None:
			continue
		key = _pen_scale_key(pen, dataset)
		if key not in index:
			index[key] = len(groups)
			groups.append((key, [pen]))
		else:
			groups[index[key]][1].append(pen)
	return groups


def needs_dual_plot(dataset, pens):
	"""True when pens should be split across two stacked plots."""
	if dataset is None or pens is None:
		return False
	try:
		if dataset.getRowCount() <= 0:
			return False
	except Exception:
		return False

	groups = scale_groups(dataset, pens)
	if len(groups) >= 2:
		return True

	# Same eng-unit / bucket but wildly different spans → still split.
	extents = []
	for pen in _enabled_pens(pens):
		try:
			alias = pen["alias"]
		except Exception:
			continue
		col = resolve_column(dataset, alias)
		if col is None:
			continue
		ext = _column_extent(dataset, col)
		if ext is not None:
			span = abs(ext[1] - ext[0])
			if span <= 0:
				span = max(abs(ext[0]), abs(ext[1]), 1e-9)
			extents.append(span)
	if len(extents) < 2:
		return False
	lo = min(extents)
	hi = max(extents)
	if lo <= 0:
		return hi > 0
	return (hi / lo) >= RANGE_RATIO_THRESHOLD


def pens_for_plot(dataset, pens, plot_index):
	"""Return the pens dataset rows that belong on plot 0 or 1.

	Plot 0 = first scale group (or largest-span pen when ratio-splitting).
	Plot 1 = remaining enabled pens. When dual plot is not needed, plot 0
	gets all pens and plot 1 is empty.
	"""
	plot_index = int(plot_index) if plot_index is not None else 0
	enabled = _enabled_pens(pens)
	if not enabled:
		return []

	dual = needs_dual_plot(dataset, pens)
	if not dual:
		return enabled if plot_index == 0 else []

	groups = scale_groups(dataset, pens)
	if len(groups) >= 2:
		if plot_index == 0:
			return groups[0][1]
		out = []
		for _key, pens_in_group in groups[1:]:
			out.extend(pens_in_group)
		return out

	# Ratio split within one scale key: put widest-span pen on plot 0 alone
	# if that isolates the busy scale; otherwise first pen vs rest.
	ranked = []
	for pen in enabled:
		try:
			alias = pen["alias"]
		except Exception:
			continue
		col = resolve_column(dataset, alias)
		ext = _column_extent(dataset, col) if col else None
		span = 0.0
		if ext is not None:
			span = abs(ext[1] - ext[0])
			if span <= 0:
				span = max(abs(ext[0]), abs(ext[1]), 0.0)
		ranked.append((span, pen))
	ranked.sort(key=lambda item: item[0], reverse=True)
	if plot_index == 0:
		return [ranked[0][1]] if ranked else []
	return [p for _s, p in ranked[1:]]


def build_series(dataset, pens, plot_index=0):
	"""Build Kyvis ApexCharts series list for one plot."""
	series = []
	if dataset is None or pens is None:
		return series
	try:
		if dataset.getRowCount() <= 0:
			return series
	except Exception:
		return series

	plot_pens = pens_for_plot(dataset, pens, plot_index)
	filter_columns = ["t_stamp"]
	for pen in plot_pens:
		try:
			alias = pen["alias"]
		except Exception:
			continue
		use = resolve_column(dataset, alias)
		if use is None:
			continue
		try:
			filter_columns.append(use)
			name = pen["penName"] or pen["alias"]
			color = pen["penColor"]
			series.append(
				{
					"name": name,
					"color": color,
					"data": system.dataset.filterColumns(dataset, filter_columns),
				}
			)
			filter_columns.remove(use)
		except Exception:
			try:
				if use in filter_columns:
					filter_columns.remove(use)
			except Exception:
				pass
	return series
