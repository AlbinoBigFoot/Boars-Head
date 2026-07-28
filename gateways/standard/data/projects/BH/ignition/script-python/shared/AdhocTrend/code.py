"""Adhoc Trend multi-plot helpers.

Explicit, user-driven plots: the operator adds empty plots and moves pens
between them freely. Routing by tag datatype only (float -> analog,
boolean/integer status -> discrete) -- no magnitude/scale auto-splitting.

`system` (Ignition scripting API) is referenced only inside function bodies,
never at import time, so this module can be imported outside the gateway
(see scripts/_verify_adhoc_helpers.py).
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

PEN_HEADERS = ["penEnabled", "tagPath", "penName", "alias", "engUnit", "penColor", "plotId", "penAction"]

_DISCRETE_DATATYPES = set(["boolean", "int1", "int2", "int4", "int8"])
_ANALOG_DATATYPES = set(["float4", "float8", "double"])


def default_plots():
	"""A fresh session/config starts with a single analog plot."""
	return [{"id": "p0", "title": "Plot 1", "kind": "analog"}]


def _as_list(value):
	"""Best-effort coercion to a plain python list (tolerates Perspective wrappers)."""
	if value is None:
		return []
	if isinstance(value, list):
		return list(value)
	if isinstance(value, tuple):
		return list(value)
	if isinstance(value, dict):
		return []
	try:
		return list(value)
	except Exception:
		return [value]


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
		v = getattr(cfg, key)
		if v is not None:
			return v
	except Exception:
		pass
	return default


def _cfg_set(cfg, key, value):
	"""Write cfg key; prefer attribute set (Perspective session custom), else dict-set."""
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
	"""Read a field off a plot entry that may be a plain dict or a Perspective wrapper."""
	try:
		if hasattr(p, "get"):
			v = p.get(key)
			if v is not None:
				return v
	except Exception:
		pass
	try:
		v = getattr(p, key)
		if v is not None:
			return v
	except Exception:
		pass
	return default


def plain_plots(cfg_or_plots):
	"""Plain list[dict] for session.custom.AdhocTrend.plots reassignment.

	Accepts either a full config (dict-like with a "plots" key) or a bare
	list of plot entries. Reassigning the returned plain list is what makes
	Perspective bindings re-evaluate -- mutating in place is a silent no-op.
	"""
	if cfg_or_plots is None:
		return default_plots()
	plots = cfg_or_plots
	try:
		if hasattr(cfg_or_plots, "plots"):
			plots = _cfg_get(cfg_or_plots, "plots", [])
		elif hasattr(cfg_or_plots, "get"):
			plots = cfg_or_plots.get("plots")
	except Exception:
		pass
	out = []
	for i, p in enumerate(_as_list(plots)):
		pid = _plot_field(p, "id")
		title = _plot_field(p, "title")
		kind = _plot_field(p, "kind")
		out.append({
			"id": str(pid) if pid not in (None, "") else ("p%d" % i),
			"title": str(title) if title not in (None, "") else ("Plot %d" % (i + 1)),
			"kind": str(kind) if kind not in (None, "") else "analog",
		})
	return out or default_plots()


def plain_pen_plots(cfg):
	"""Plain dict[alias -> plotId] for session.custom.AdhocTrend.penPlots reassignment."""
	raw = _cfg_get(cfg, "penPlots", {})
	out = {}
	try:
		items = list(raw.items()) if hasattr(raw, "items") else []
	except Exception:
		items = []
	for k, v in items:
		try:
			out[str(k)] = str(v)
		except Exception:
			pass
	return out


def normalize_config(cfg):
	"""Ensure cfg has a non-empty plots list and a penPlots dict. Safe to call repeatedly."""
	if cfg is None:
		return cfg
	_cfg_set(cfg, "plots", plain_plots(cfg))
	_cfg_set(cfg, "penPlots", plain_pen_plots(cfg))
	return cfg


def _path_segments(tag_path):
	"""[provider]Folder/Instance/Member/Value -> ["Folder", "Instance", "Member"]."""
	if tag_path in (None, ""):
		return []
	path = str(tag_path)
	if "]" in path:
		path = path.split("]", 1)[1]
	if path.endswith("/Value"):
		path = path[: -len("/Value")]
	path = path.strip("/")
	return [s for s in path.split("/") if s != ""]


def alias_for(tag_path):
	"""Dataset/session alias: drop trailing /Value, strip provider, / -> -, space -> _."""
	if tag_path in (None, ""):
		return ""
	path = str(tag_path)
	if path.endswith("/Value"):
		path = path[: -len("/Value")]
	parts = path.split("]")
	tail = parts[1] if len(parts) > 1 else path
	return tail.replace("/", "-").replace(" ", "_")


def pen_label(tag_path):
	"""UDT-instance pen name.

	.../<Type>/<Instance>/<Member>/Value -> <Instance> (three or more path
	segments once the provider prefix and trailing /Value are stripped).
	Shallower paths (a plain tag, or a tag with no Type folder above it)
	have no separate instance folder, so the tag's own leaf name is used.
	"""
	segments = _path_segments(tag_path)
	if not segments:
		return str(tag_path) if tag_path is not None else ""
	if len(segments) >= 3:
		return segments[-2]
	return segments[-1]


def _member_segment(tag_path):
	segments = _path_segments(tag_path)
	if not segments:
		return ""
	return segments[-1]


def pen_labels(tag_paths):
	"""pen_label() for each path, disambiguating duplicates with the member name."""
	paths = list(tag_paths or [])
	labels = [pen_label(p) for p in paths]
	counts = {}
	for label in labels:
		counts[label] = counts.get(label, 0) + 1
	out = []
	for path, label in zip(paths, labels):
		if counts.get(label, 0) > 1:
			member = _member_segment(path)
			out.append(("%s %s" % (label, member)) if member else label)
		else:
			out.append(label)
	return out


def tag_kind(tag_path):
	"""'analog' or 'discrete' from the tag's DataType. Unreadable/unknown -> 'analog'."""
	try:
		path = str(tag_path)
		value_path = path if path.endswith("/Value") else (path + "/Value")
		qv = system.tag.readBlocking([value_path + ".DataType"])[0]
		dt = str(qv.value).strip().lower() if qv.value not in (None, "") else ""
	except Exception:
		return "analog"
	if dt in _DISCRETE_DATATYPES:
		return "discrete"
	if dt in _ANALOG_DATATYPES:
		return "analog"
	return "analog"


def build_pens(tags, colors, pen_plots=None, plots=None):
	"""Pens Dataset for the trend legend/table.

	Optional pen_plots/plots fill the plotId column for the table dropdown.
	pens_for_plot() still resolves membership live from penPlots.
	"""
	rows = []
	tags = _as_list(tags)
	colors = _as_list(colors) or list(DEFAULT_COLORS)
	if not tags:
		return system.dataset.toDataSet(PEN_HEADERS, rows)

	plot_list = plain_plots(plots) if plots is not None else default_plots()
	first_id = plot_list[0]["id"] if plot_list else "p0"
	pp = {}
	if pen_plots is not None:
		pp = plain_pen_plots({"penPlots": pen_plots})
	elif plots is not None:
		# allow callers to pass a full cfg as pen_plots mistakenly — ignore
		pp = {}

	paths = [str(t) for t in tags if t not in (None, "")]
	labels = pen_labels(paths)
	label_by_path = dict(zip(paths, labels))

	for i, tag in enumerate(tags):
		if tag in (None, ""):
			continue
		tag = str(tag)
		hist_path = tag if tag.endswith("/Value") else (tag + "/Value")
		eng_unit = ""
		try:
			qv = system.tag.readBlocking([hist_path + ".EngUnit"])[0]
			eng_unit = qv.value if qv.value not in (None, "") else ""
		except Exception:
			eng_unit = ""
		pen_name = label_by_path.get(tag, pen_label(tag))
		alias = alias_for(tag)
		pen_color = colors[i] if i < len(colors) else colors[0]
		assigned = first_id
		if pp:
			if alias in pp:
				assigned = pp[alias]
			elif tag in pp:
				assigned = pp[tag]
			elif hist_path in pp:
				assigned = pp[hist_path]
		rows.append([True, hist_path, pen_name, alias, eng_unit, pen_color, assigned, ""])
	return system.dataset.toDataSet(PEN_HEADERS, rows)


def pens_for_plot(pens, pen_plots, plot_id, first_plot_id):
	"""Enabled pens from `pens` currently assigned to plot_id.

	Assignment is resolved live from pen_plots (alias -> plotId); pens with
	no entry fall through to first_plot_id. Independent of whatever the
	dataset's own "plotId" column happens to hold.
	"""
	if pens is None:
		return system.dataset.toDataSet(PEN_HEADERS, [])
	try:
		if pens.getRowCount() <= 0:
			return system.dataset.toDataSet(PEN_HEADERS, [])
	except Exception:
		return system.dataset.toDataSet(PEN_HEADERS, [])

	pen_plots = pen_plots or {}
	first_plot_id = str(first_plot_id) if first_plot_id not in (None, "") else str(plot_id)
	plot_id = str(plot_id) if plot_id not in (None, "") else first_plot_id

	cols = list(pens.getColumnNames())
	rows = []
	# Tolerate dict-like or list-of-pairs pen_plots
	try:
		pp = plain_pen_plots({"penPlots": pen_plots})
	except Exception:
		pp = pen_plots if isinstance(pen_plots, dict) else {}

	for py_row in system.dataset.toPyDataSet(pens):
		try:
			enabled = py_row["penEnabled"]
		except Exception:
			enabled = False
		if not enabled:
			continue
		try:
			alias = py_row["alias"]
		except Exception:
			alias = None
		try:
			tag_path = py_row["tagPath"]
		except Exception:
			tag_path = None
		assigned = None
		if alias not in (None, "") and alias in pp:
			assigned = pp[alias]
		elif tag_path not in (None, "") and tag_path in pp:
			assigned = pp[tag_path]
		elif alias not in (None, ""):
			try:
				assigned = pp.get(alias, first_plot_id)
			except Exception:
				assigned = first_plot_id
		else:
			assigned = first_plot_id
		if assigned in (None, ""):
			assigned = first_plot_id
		if str(assigned) != plot_id:
			continue
		rows.append([py_row[c] for c in cols])
	return system.dataset.toDataSet(cols, rows)


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


def build_series(dataset, pens):
	"""Kyvis ApexCharts series list for a single plot's enabled pens."""
	series = []
	if dataset is None or pens is None:
		return series
	try:
		if dataset.getRowCount() <= 0 or pens.getRowCount() <= 0:
			return series
	except Exception:
		return series

	for pen in system.dataset.toPyDataSet(pens):
		try:
			if not pen["penEnabled"]:
				continue
		except Exception:
			continue
		try:
			alias = pen["alias"]
		except Exception:
			continue
		if alias in (None, ""):
			continue
		col = resolve_column(dataset, alias)
		if col is None:
			continue
		cols = ["t_stamp", col]
		try:
			name = pen["penName"] or pen["alias"]
		except Exception:
			name = alias
		try:
			color = pen["penColor"]
		except Exception:
			color = None
		try:
			data = system.dataset.filterColumns(dataset, cols)
		except Exception:
			continue
		series.append({"name": name, "color": color, "data": data})
	return series


def build_key(pens, aggregate):
	"""[{"aggregate","alias","path"}] list the tag-history binding consumes."""
	key = []
	if pens is None:
		return key
	try:
		if pens.getRowCount() <= 0:
			return key
	except Exception:
		return key
	aggregate = aggregate or ""
	if not aggregate:
		return key
	for pen in system.dataset.toPyDataSet(pens):
		try:
			if pen["penEnabled"]:
				key.append({"aggregate": aggregate, "alias": pen["alias"], "path": pen["tagPath"]})
		except Exception:
			continue
	return key


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


def add_plot(cfg, title=None, kind="analog"):
	"""Append an empty plot. Returns the new plot id."""
	normalize_config(cfg)
	plots = plain_plots(cfg)
	pid = _new_plot_id(plots)
	n = len(plots) + 1
	plots.append({
		"id": pid,
		"title": title or ("Plot %d" % n),
		"kind": kind or "analog",
	})
	_cfg_set(cfg, "plots", plots)
	return pid


def apply_add_plot(cfg, title=None, kind="analog"):
	"""add_plot() then return the plain plots list for session reassignment."""
	add_plot(cfg, title=title, kind=kind)
	return plain_plots(cfg)


def remove_plot(cfg, plot_id):
	"""Remove an empty plot. Returns (ok, message)."""
	normalize_config(cfg)
	plots = plain_plots(cfg)
	if len(plots) <= 1:
		return False, "Keep at least one plot."
	plot_id = str(plot_id)
	pen_plots = plain_pen_plots(cfg)
	if plot_id in pen_plots.values():
		return False, "Move or remove pens from this plot before deleting it."
	plots = [p for p in plots if str(p.get("id")) != plot_id]
	if not plots:
		plots = default_plots()
	_cfg_set(cfg, "plots", plots)
	return True, ""


def move_pen(cfg, tag_or_alias, plot_id):
	"""Assign a pen to an existing plot (cross-type OK). Returns plain penPlots.

	Unknown plot ids are ignored (T-260727-01). Keys are stored under alias.
	"""
	normalize_config(cfg)
	plots = plain_plots(cfg)
	ids = set([str(p.get("id")) for p in plots if p.get("id") not in (None, "")])
	target = str(plot_id or "")
	if target not in ids:
		return plain_pen_plots(cfg)
	key = str(tag_or_alias or "")
	# Normalize tagPath -> alias so pens_for_plot lookups stay consistent
	al = alias_for(key) if ("/" in key or "]" in key) else key
	if al in (None, ""):
		al = key
	pen_plots = plain_pen_plots(cfg)
	pen_plots[str(al)] = target
	_cfg_set(cfg, "penPlots", pen_plots)
	return pen_plots


def route_new_tag(cfg, tag_path, data_type=None):
	"""Route a newly-added tag to a plot by datatype. Returns (plotId, plots, penPlots).

	Floats land on the first analog plot. Booleans/integer status tags land
	on the first discrete plot, creating one (titled "Status") if none
	exists yet. No magnitude/scale-based splitting.
	"""
	normalize_config(cfg)
	# Optional data_type override (Perspective may already know the datatype)
	if data_type not in (None, ""):
		dt = str(data_type).strip().lower()
		if dt in _DISCRETE_DATATYPES or dt in ("bool", "boolean", "integer", "short", "long", "byte"):
			kind = "discrete"
		elif dt in _ANALOG_DATATYPES or dt in ("float", "real", "double"):
			kind = "analog"
		else:
			kind = tag_kind(tag_path)
	else:
		kind = tag_kind(tag_path)
	plots = plain_plots(cfg)
	target = None
	for p in plots:
		if p.get("kind") == kind:
			target = p
			break
	if target is None:
		title = "Status" if kind == "discrete" else ("Plot %d" % (len(plots) + 1))
		pid = add_plot(cfg, title=title, kind=kind)
		plots = plain_plots(cfg)
		target = next((p for p in plots if p["id"] == pid), plots[-1])

	alias = alias_for(tag_path)
	pen_plots = plain_pen_plots(cfg)
	pen_plots[alias] = target["id"]
	# Also key by raw tagPath so UI handlers that pass session tags still resolve
	tp = str(tag_path or "")
	if tp and tp != alias:
		pen_plots[tp] = target["id"]
	_cfg_set(cfg, "plots", plots)
	_cfg_set(cfg, "penPlots", pen_plots)
	return target["id"], plots, pen_plots


def route_new_pen(cfg, tag_path, data_type=None):
	"""Alias for route_new_tag (D-02 / plan naming)."""
	return route_new_tag(cfg, tag_path, data_type)


def plot_dropdown_options(plots):
	"""Dropdown options [{value, label}] for pen move UI."""
	out = []
	for p in plain_plots(plots):
		out.append({"value": p["id"], "label": p["title"]})
	return out


def plot_options_overrides(kind):
	"""Small ApexCharts option overrides so status/discrete pens don't render as ramps."""
	if kind == "discrete":
		return {"stroke": {"curve": "stepline"}, "yaxis": {"decimalsInFloat": 0}}
	return {}
