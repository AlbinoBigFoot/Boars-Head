"""Adhoc Trend multi-plot helpers (operator-controlled N plots).

Type-based default routing only — no magnitude / engUnit auto-split.
"""

DEFAULT_COLORS = [
	"#008FFB",
	"#34C759",
	"#FFA726",
	"#FF4560",
	"#775DD0",
	"#1C4E80",
	"#008080",
	"#26C6DA",
	"#4F4F4F",
	"#6C757D",
]

_LEAF_MEMBERS = set(
	[
		"value",
		"status",
		"cmd",
		"mode",
		"auto",
		"manual",
		"pressure",
		"temperature",
		"temp",
		"level",
		"flow",
		"speed",
		"amps",
		"current",
		"voltage",
		"power",
		"position",
		"setpoint",
		"sp",
		"pv",
		"cv",
		"fault",
		"alarm",
		"running",
		"enabled",
		"state",
	]
)


def default_plots():
	"""One analog plot matching the original single-chart feel."""
	return [{"id": "p0", "title": "Plot 1", "kind": "analog"}]


def _as_list(value):
	if value is None:
		return []
	try:
		if isinstance(value, (list, tuple)):
			return list(value)
	except Exception:
		pass
	try:
		return list(value)
	except Exception:
		return []


def _as_bool(value):
	if value in (True, "true", "True", "TRUE", 1, "1"):
		return True
	return False


def _cfg_get(cfg, key, default=None):
	"""Read cfg key from dict-like or Perspective session custom object."""
	if cfg is None:
		return default
	try:
		if hasattr(cfg, "get"):
			v = cfg.get(key)
			if v is not None:
				return v
	except Exception:
		pass
	try:
		return getattr(cfg, key)
	except Exception:
		return default


def _cfg_set(cfg, key, value):
	"""Write cfg key; prefer attribute set (Perspective session custom)."""
	if cfg is None:
		return False
	try:
		setattr(cfg, key, value)
		return True
	except Exception:
		pass
	try:
		cfg[key] = value
		return True
	except Exception:
		return False


def _plot_field(p, key, default=None):
	try:
		if hasattr(p, "get"):
			v = p.get(key)
			if v is not None:
				return v
	except Exception:
		pass
	try:
		return getattr(p, key)
	except Exception:
		return default


def plain_plots(cfg_or_plots):
	"""Plain list[dict] for session.custom.AdhocTrend.plots reassignment."""
	if cfg_or_plots is None:
		return default_plots()
	plots = cfg_or_plots
	try:
		if hasattr(cfg_or_plots, "plots") or (
			hasattr(cfg_or_plots, "get") and cfg_or_plots.get("plots") is not None
		):
			plots = _cfg_get(cfg_or_plots, "plots")
	except Exception:
		pass
	out = []
	for i, p in enumerate(_as_list(plots)):
		pid = _plot_field(p, "id")
		title = _plot_field(p, "title")
		kind = _plot_field(p, "kind")
		out.append(
			{
				"id": str(pid or ("p%d" % i)),
				"title": str(title or ("Plot %d" % (i + 1))),
				"kind": str(kind or "analog"),
			}
		)
	return out or default_plots()


def plain_pen_plots(cfg):
	"""Plain dict tagPath/alias -> plotId."""
	raw = _cfg_get(cfg, "penPlots", {})
	out = {}
	if raw is None:
		return out
	# dict-like
	try:
		if hasattr(raw, "keys") and not isinstance(raw, (list, tuple, str)):
			for k in list(raw.keys()):
				try:
					v = raw[k] if not hasattr(raw, "get") else raw.get(k)
				except Exception:
					v = None
				if k in (None, "") or v in (None, ""):
					continue
				out[str(k)] = str(v)
			return out
	except Exception:
		pass
	# list of pairs / {tagPath, plotId} objects
	for item in _as_list(raw):
		try:
			if isinstance(item, (list, tuple)) and len(item) >= 2:
				out[str(item[0])] = str(item[1])
				continue
		except Exception:
			pass
		tp = _plot_field(item, "tagPath")
		if tp in (None, ""):
			tp = _plot_field(item, "alias")
		pid = _plot_field(item, "plotId")
		if tp not in (None, "") and pid not in (None, ""):
			out[str(tp)] = str(pid)
	return out


def normalize_config(cfg):
	"""Ensure plots / penPlots exist; return cfg."""
	if cfg is None:
		return cfg
	plots = plain_plots(cfg)
	pen_plots = plain_pen_plots(cfg)
	_cfg_set(cfg, "plots", plots)
	_cfg_set(cfg, "penPlots", pen_plots)
	return cfg


def _new_plot_id(plots):
	used = set()
	for p in plots or []:
		pid = _plot_field(p, "id")
		if pid not in (None, ""):
			used.add(str(pid))
	i = 0
	while ("p%d" % i) in used:
		i += 1
	return "p%d" % i


def _strip_provider(tag_path):
	s = str(tag_path or "")
	if "]" in s:
		s = s.split("]", 1)[1]
	return s.strip("/")


def alias_for(tag_path):
	"""Historian-style alias used by existing Adhoc Trend pens."""
	base = str(tag_path or "")
	if base.endswith("/Value"):
		base = base[:-6]
	part = base.split("]")[1] if "]" in base else base
	alias = str(part).replace("/", "-").replace(" ", "_")
	return alias


def pen_label(tag_path):
	"""UDT instance name holding the tag (e.g. EV-01), not leaf Value/Pressure."""
	path = _strip_provider(tag_path)
	if path.endswith("/Value"):
		path = path[:-6]
	segs = [s for s in path.split("/") if s]
	if not segs:
		return str(tag_path or "")
	if len(segs) == 1:
		return segs[0]
	# Prefer second-to-last when last looks like a member/leaf
	leaf = segs[-1]
	candidate = segs[-2]
	if leaf.lower() in _LEAF_MEMBERS or leaf.lower() == "value":
		return candidate
	# Evaporators/EV-01/Pressure/Value already stripped Value → Pressure is leaf
	if len(segs) >= 2 and leaf.lower() in _LEAF_MEMBERS:
		return candidate
	# Default: UDT instance is second-to-last (folder/member under instance)
	return candidate


def pen_labels(tag_paths):
	"""Labels with duplicate UDT instances disambiguated by member name."""
	paths = _as_list(tag_paths)
	raw = [pen_label(tp) for tp in paths]
	counts = {}
	for lab in raw:
		counts[lab] = counts.get(lab, 0) + 1
	out = []
	for i, tp in enumerate(paths):
		lab = raw[i]
		if counts.get(lab, 0) <= 1:
			out.append(lab)
			continue
		path = _strip_provider(tp)
		if path.endswith("/Value"):
			path = path[:-6]
		segs = [s for s in path.split("/") if s]
		member = segs[-1] if segs else ""
		if member and member != lab:
			out.append("%s %s" % (lab, member))
		else:
			out.append(lab)
	return out


def tag_kind(tag_path, data_type=None):
	"""Return 'analog' or 'discrete' from datatype (floats→analog; bool/int→discrete)."""
	dt = data_type
	if dt in (None, ""):
		try:
			tp = str(tag_path or "")
			hist = tp if tp.endswith("/Value") else (tp + "/Value")
			reads = system.tag.readBlocking([hist + ".DataType", tp + ".DataType"])
			for qv in reads:
				if qv.value not in (None, ""):
					dt = qv.value
					break
		except Exception:
			dt = None
	s = str(dt or "").strip().lower()
	if s in ("boolean", "bool", "int1", "int2", "int4", "int8", "short", "long", "byte", "integer"):
		return "discrete"
	if s in ("float4", "float8", "double", "float", "real"):
		return "analog"
	return "analog"


def _plot_ids(plots):
	ids = set()
	for p in plots or []:
		pid = _plot_field(p, "id")
		if pid not in (None, ""):
			ids.add(str(pid))
	return ids


def _first_plot_id(plots, kind=None):
	for p in plots or []:
		if kind is not None and str(_plot_field(p, "kind") or "") != str(kind):
			continue
		pid = _plot_field(p, "id")
		if pid not in (None, ""):
			return str(pid)
	if plots:
		pid = _plot_field(plots[0], "id")
		return str(pid or "p0")
	return "p0"


def _lookup_pen_plot(pen_plots, tag_path, alias=None):
	if not pen_plots:
		return None
	tp = str(tag_path or "")
	if tp in pen_plots:
		return str(pen_plots[tp])
	al = alias or alias_for(tp)
	if al in pen_plots:
		return str(pen_plots[al])
	# try with/without /Value
	if tp.endswith("/Value"):
		base = tp[:-6]
		if base in pen_plots:
			return str(pen_plots[base])
	else:
		alt = tp + "/Value"
		if alt in pen_plots:
			return str(pen_plots[alt])
	return None


def add_plot(cfg, title=None, kind="analog"):
	"""Append an empty plot. Returns new plot id."""
	normalize_config(cfg)
	plots = plain_plots(cfg)
	pid = _new_plot_id(plots)
	n = len(plots) + 1
	plots.append(
		{
			"id": pid,
			"title": title or ("Plot %d" % n),
			"kind": kind or "analog",
		}
	)
	_cfg_set(cfg, "plots", plots)
	return pid


def apply_add_plot(cfg, title=None, kind="analog"):
	"""Append plot and return plain plots list for session.custom reassignment."""
	add_plot(cfg, title=title, kind=kind)
	plots = plain_plots(cfg)
	_cfg_set(cfg, "plots", plots)
	return plots


def remove_plot(cfg, plot_id):
	"""Remove an empty plot. Returns (ok, message)."""
	normalize_config(cfg)
	plots = plain_plots(cfg)
	if len(plots) <= 1:
		return False, "Keep at least one plot."
	plot_id = str(plot_id)
	pen_plots = plain_pen_plots(cfg)
	if plot_id in [str(v) for v in pen_plots.values()]:
		return False, "Move or remove pens from this plot before deleting it."
	plots = [p for p in plots if str(p.get("id")) != plot_id]
	if not plots:
		plots = default_plots()
	_cfg_set(cfg, "plots", plots)
	return True, ""


def move_pen(cfg, tag_path, target_plot_id):
	"""Assign pen to an existing plot (cross-type OK). Returns plain penPlots dict."""
	normalize_config(cfg)
	plots = plain_plots(cfg)
	ids = _plot_ids(plots)
	target = str(target_plot_id or "")
	if target not in ids:
		# ignore unknown ids (T-260727-01)
		return plain_pen_plots(cfg)
	key = str(tag_path or "")
	# Prefer the raw session tag key; also store under alias for lookups
	pen_plots = plain_pen_plots(cfg)
	pen_plots[key] = target
	al = alias_for(key)
	if al and al != key:
		# Keep a single canonical key when possible: prefer tagPath if already present
		# Drop stale alias-only entries that would duplicate
		pass
	_cfg_set(cfg, "penPlots", pen_plots)
	return pen_plots


def route_new_pen(cfg, tag_path, data_type=None):
	"""Default-route a new pen by datatype; create discrete plot if needed.

	Returns (plot_id, plain_plots, plain_pen_plots).
	"""
	normalize_config(cfg)
	plots = plain_plots(cfg)
	pen_plots = plain_pen_plots(cfg)
	kind = tag_kind(tag_path, data_type)
	pid = _first_plot_id(plots, kind=kind)
	# If discrete requested but no discrete plot, create Status plot
	if kind == "discrete":
		found = None
		for p in plots:
			if str(_plot_field(p, "kind") or "") == "discrete":
				found = str(_plot_field(p, "id"))
				break
		if found is None:
			pid = add_plot(cfg, title="Status", kind="discrete")
			plots = plain_plots(cfg)
		else:
			pid = found
	else:
		found = None
		for p in plots:
			if str(_plot_field(p, "kind") or "") == "analog":
				found = str(_plot_field(p, "id"))
				break
		if found is None:
			pid = add_plot(cfg, title="Analog", kind="analog")
			plots = plain_plots(cfg)
		else:
			pid = found
	key = str(tag_path or "")
	pen_plots[key] = str(pid)
	_cfg_set(cfg, "plots", plots)
	_cfg_set(cfg, "penPlots", pen_plots)
	return str(pid), plots, pen_plots


# Alias used by some call sites / sibling plans
def route_new_tag(cfg, tag_path, data_type=None):
	return route_new_pen(cfg, tag_path, data_type)


def plot_dropdown_options(plots):
	"""Dropdown options [{value, label}] for pen move UI."""
	out = []
	for p in plain_plots(plots):
		out.append({"value": p["id"], "label": p["title"]})
	return out


def plot_options_overrides(kind):
	if str(kind or "") == "discrete":
		return {"stroke": {"curve": "stepline"}, "yaxis": {"decimalsInFloat": 0}}
	return {}


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


def build_series(dataset, pens):
	"""Build Kyvis ApexCharts series list for pens already filtered to one plot."""
	series = []
	if dataset is None or pens is None:
		return series
	try:
		if dataset.getRowCount() <= 0:
			return series
	except Exception:
		return series

	filter_columns = ["t_stamp"]
	for pen in _enabled_pens(pens):
		try:
			alias = pen["alias"]
		except Exception:
			continue
		use = resolve_column(dataset, alias)
		if use is None:
			continue
		try:
			filter_columns.append(use)
			try:
				name = pen["penName"] or pen["alias"]
			except Exception:
				name = alias
			try:
				color = pen["penColor"]
			except Exception:
				color = "#008FFB"
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


def build_key(pens, aggregate):
	"""Tag-history key list for enabled pens."""
	key = []
	if pens is None or aggregate in (None, ""):
		return key
	try:
		if pens.getRowCount() <= 0:
			return key
	except Exception:
		return key
	for pen in system.dataset.toPyDataSet(pens):
		try:
			if not _as_bool(pen["penEnabled"]):
				continue
			key.append(
				{
					"aggregate": aggregate,
					"alias": pen["alias"],
					"path": pen["tagPath"],
				}
			)
		except Exception:
			continue
	return key


def build_pens(tags, colors, pen_plots=None, plots=None):
	"""Dataset of pens with UDT-instance penName and plotId assignment."""
	headers = [
		"penEnabled",
		"tagPath",
		"penName",
		"alias",
		"engUnit",
		"penColor",
		"plotId",
		"penAction",
	]
	rows = []
	tag_list = _as_list(tags)
	color_list = _as_list(colors) or list(DEFAULT_COLORS)
	plot_list = plain_plots(plots) if plots is not None else default_plots()
	first_id = _first_plot_id(plot_list)
	pp = {}
	if pen_plots is not None:
		if isinstance(pen_plots, dict) or hasattr(pen_plots, "keys"):
			pp = plain_pen_plots({"penPlots": pen_plots})
		else:
			pp = plain_pen_plots({"penPlots": pen_plots})
	labels = pen_labels(tag_list)
	for i, tag in enumerate(tag_list):
		if tag in (None, ""):
			continue
		tag = str(tag)
		hist_path = tag if tag.endswith("/Value") else (tag + "/Value")
		base = tag[:-6] if tag.endswith("/Value") else tag
		eng = ""
		try:
			reads = system.tag.readBlocking([hist_path + ".EngUnit", base + ".EngUnit"])
			for qv in reads:
				if qv.value not in (None, ""):
					eng = qv.value
					break
		except Exception:
			eng = ""
		alias = alias_for(tag)
		name = labels[i] if i < len(labels) else pen_label(tag)
		color = color_list[i] if i < len(color_list) else color_list[0]
		pid = _lookup_pen_plot(pp, tag, alias) or first_id
		rows.append([True, hist_path, name, alias, eng, color, pid, ""])
	return system.dataset.toDataSet(headers, rows)


def pens_for_plot(pens, pen_plots, plot_id, first_plot_id=None):
	"""Filter pens dataset to those assigned to plot_id."""
	headers = [
		"penEnabled",
		"tagPath",
		"penName",
		"alias",
		"engUnit",
		"penColor",
		"plotId",
		"penAction",
	]
	rows = []
	if pens is None:
		return system.dataset.toDataSet(headers, rows)
	try:
		if pens.getRowCount() <= 0:
			return system.dataset.toDataSet(headers, rows)
	except Exception:
		return system.dataset.toDataSet(headers, rows)

	target = str(plot_id or "")
	fallback = str(first_plot_id or "p0")
	pp = plain_pen_plots({"penPlots": pen_plots}) if pen_plots is not None else {}

	# Detect column names
	try:
		cols = list(pens.getColumnNames())
	except Exception:
		cols = headers

	has_plot_col = "plotId" in cols
	for pen in system.dataset.toPyDataSet(pens):
		try:
			alias = pen["alias"]
		except Exception:
			alias = ""
		try:
			tag_path = pen["tagPath"]
		except Exception:
			tag_path = ""
		assigned = None
		if has_plot_col:
			try:
				assigned = pen["plotId"]
			except Exception:
				assigned = None
		if assigned in (None, ""):
			assigned = _lookup_pen_plot(pp, tag_path, alias)
		if assigned in (None, ""):
			assigned = fallback
		if str(assigned) != target:
			continue
		row = []
		for h in headers:
			try:
				row.append(pen[h] if h != "plotId" else assigned)
			except Exception:
				if h == "plotId":
					row.append(assigned)
				elif h == "penEnabled":
					row.append(True)
				elif h == "penAction":
					row.append("")
				else:
					row.append("")
		rows.append(row)
	return system.dataset.toDataSet(headers, rows)
