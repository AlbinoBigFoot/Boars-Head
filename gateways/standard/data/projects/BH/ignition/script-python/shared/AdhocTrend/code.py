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
	"""A fresh session/config starts with a single analog plot titled Default."""
	return [{"id": "p0", "title": "Default", "kind": "analog"}]


def _default_plot_title(index):
	"""Fallback title when a plot entry has no title. First plot is Default."""
	if index == 0:
		return "Default"
	return "Plot %d" % (index + 1)


try:
	_STRING_TYPES = (basestring,)  # Jython 2.7
except NameError:
	_STRING_TYPES = (str, bytes)


def _is_string(value):
	return isinstance(value, _STRING_TYPES)


def _as_list(value):
	"""Best-effort coercion to a plain python list (tolerates Perspective wrappers).

	Never call list() on a plain string — list(\"#008FFB\") yields characters and
	collapses every pen onto junk / the same Apex default color.
	Prefer index access for Perspective ArrayWrappers when available.
	"""
	if value is None:
		return []
	if _is_string(value):
		return [value] if value != "" else []
	if isinstance(value, list):
		return list(value)
	if isinstance(value, tuple):
		return list(value)
	if isinstance(value, dict):
		return []
	# Perspective ArrayWrapper / Java List: prefer indexed reads
	try:
		n = len(value)
		if n == 0:
			return []
		out = []
		for i in range(n):
			try:
				out.append(value[i])
			except Exception:
				break
		if len(out) == n:
			return out
	except Exception:
		pass
	try:
		return list(value)
	except Exception:
		return [value]


def palette_colors(colors):
	"""Plain list of usable pen hex/rgb colors; never a single shared color.

	Falls back to DEFAULT_COLORS when the input is missing, a lone hex string,
	character-sploded junk from list(string), or otherwise unusable.
	"""
	# JSON-encoded array accidentally stored as a string
	if _is_string(colors):
		s = str(colors).strip()
		if s.startswith("["):
			try:
				decoded = system.util.jsonDecode(s)
				return palette_colors(decoded)
			except Exception:
				pass
		# A single hex is not a palette — keep cycling the defaults
		return list(DEFAULT_COLORS)

	raw = _as_list(colors)
	out = []
	for c in raw:
		if c in (None, ""):
			continue
		s = str(c).strip()
		if s.startswith("#") and len(s) >= 4:
			out.append(s)
		elif s.lower().startswith("rgb"):
			out.append(s)
		elif s.startswith("var("):
			out.append(s)
	# list(\"#008FFB\") style junk → many 1-char tokens
	if out and len(out) > 3 and all(len(c) <= 2 for c in out):
		return list(DEFAULT_COLORS)
	if len(out) < 1:
		return list(DEFAULT_COLORS)
	return out


def color_for_index(colors, index):
	"""Palette color for pen index (cycles; never collapses to one color)."""
	palette = palette_colors(colors)
	if not palette:
		palette = list(DEFAULT_COLORS)
	i = int(index) if index is not None else 0
	if i < 0:
		i = 0
	return palette[i % len(palette)]


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
		# Migrate legacy primary title "Plot 1" / "Analog" → Default
		if i == 0 and title in ("Plot 1", "Analog"):
			title = "Default"
		out.append({
			"id": str(pid) if pid not in (None, "") else ("p%d" % i),
			"title": str(title) if title not in (None, "") else _default_plot_title(i),
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


def plain_disabled_pens(cfg):
	"""Plain dict[alias -> True] for pens the operator unchecked (On = off).

	Accepts a full cfg, a bare dict of aliases, or a list of aliases.
	"""
	raw = _cfg_get(cfg, "disabledPens", None)
	if raw is None and isinstance(cfg, (dict, list, tuple)):
		# Caller passed the disabled map/list directly
		if isinstance(cfg, (list, tuple)) or (hasattr(cfg, "items") and "disabledPens" not in cfg and "plots" not in cfg and "tags" not in cfg):
			raw = cfg
	out = {}
	if raw is None:
		return out
	if isinstance(raw, (list, tuple)):
		for k in raw:
			if k not in (None, ""):
				out[str(k)] = True
		return out
	try:
		items = list(raw.items()) if hasattr(raw, "items") else []
	except Exception:
		items = []
	for k, v in items:
		if k in (None, ""):
			continue
		# Treat missing/falsey as enabled (omit); truthy = disabled
		if v in (False, 0, "0", "false", "False", None, ""):
			continue
		out[str(k)] = True
	return out


def is_pen_enabled(disabled_pens, alias, tag_path=None):
	"""True unless alias (or tag_path) is listed in disabledPens."""
	if disabled_pens is None:
		return True
	# Prefer plain map when caller already normalized
	if isinstance(disabled_pens, dict) and "disabledPens" not in disabled_pens and "plots" not in disabled_pens and "tags" not in disabled_pens:
		dp = {}
		for k, v in disabled_pens.items():
			if k in (None, ""):
				continue
			if v not in (False, 0, "0", "false", "False", None, ""):
				dp[str(k)] = True
	else:
		dp = plain_disabled_pens(disabled_pens)
	if alias not in (None, "") and str(alias) in dp:
		return False
	if tag_path not in (None, "") and str(tag_path) in dp:
		return False
	return True


def toggle_pen_enabled(cfg, alias_or_path):
	"""Flip On/off for a pen. Returns plain disabledPens for session reassignment."""
	normalize_config(cfg)
	key = str(alias_or_path or "")
	if "/" in key or "]" in key:
		al = alias_for(key)
		if al not in (None, ""):
			key = al
	dp = plain_disabled_pens(cfg)
	if key in dp:
		del dp[key]
	elif key:
		dp[key] = True
	_cfg_set(cfg, "disabledPens", dp)
	return dp


def normalize_config(cfg):
	"""Ensure cfg has plots, penPlots, disabledPens, and a usable colors palette."""
	if cfg is None:
		return cfg
	_cfg_set(cfg, "plots", plain_plots(cfg))
	_cfg_set(cfg, "penPlots", plain_pen_plots(cfg))
	_cfg_set(cfg, "disabledPens", plain_disabled_pens(cfg))
	# Repair a corrupted / single-color palette so pens stay distinct
	_cfg_set(cfg, "colors", palette_colors(_cfg_get(cfg, "colors", None)))
	return cfg


# Trailing path leaves that are generic PLC/UDT property names, not the member.
_GENERIC_LEAF_NAMES = set(["value", "cmd", "status"])


def _path_segments(tag_path):
	"""[provider]Folder/Instance/Member/Value -> ["Folder", "Instance", "Member"].

	Strips the provider bracket and any trailing generic leaves
	(Value / CMD / status, case-insensitive).
	"""
	if tag_path in (None, ""):
		return []
	path = str(tag_path)
	if "]" in path:
		path = path.split("]", 1)[1]
	path = path.strip("/")
	segments = [s for s in path.split("/") if s != ""]
	while segments and segments[-1].lower() in _GENERIC_LEAF_NAMES:
		segments.pop()
	return segments


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
	"""Parent UDT instance + child member pen name.

	.../<Folder>/<Instance>/<Member>/<Value> -> "<Instance> <Member>"
	Uses the two segments immediately above any stripped generic leaf
	(Value/CMD/status). Shallower paths fall back to the remaining leaf.
	"""
	segments = _path_segments(tag_path)
	if not segments:
		return str(tag_path) if tag_path is not None else ""
	if len(segments) >= 2:
		return "%s %s" % (segments[-2], segments[-1])
	return segments[-1]


def pen_labels(tag_paths):
	"""pen_label() for each path (instance + member already included)."""
	return [pen_label(p) for p in (tag_paths or [])]


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


def build_pens(tags, colors, pen_plots=None, plots=None, disabled_pens=None):
	"""Pens Dataset for the trend legend/table.

	Optional pen_plots/plots fill the plotId column for the table dropdown.
	pens_for_plot() still resolves membership live from penPlots.
	disabled_pens (alias -> True) drives the On checkbox / chart visibility.
	"""
	rows = []
	tags = _as_list(tags)
	palette = palette_colors(colors)
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
	dp = {}
	if disabled_pens is not None:
		if isinstance(disabled_pens, dict) and (
			"disabledPens" in disabled_pens or "plots" in disabled_pens or "tags" in disabled_pens or "penPlots" in disabled_pens
		):
			dp = plain_disabled_pens(disabled_pens)
		else:
			dp = plain_disabled_pens({"disabledPens": disabled_pens})

	# Stable pen index among non-empty tags (skip blanks without shifting colors)
	pen_index = 0
	for tag in tags:
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
		# Always derive display name from path so Clear+re-add and live rebuild match
		pen_name = pen_label(tag)
		alias = alias_for(tag)
		pen_color = color_for_index(palette, pen_index)
		assigned = first_id
		if pp:
			if alias in pp:
				assigned = pp[alias]
			elif tag in pp:
				assigned = pp[tag]
			elif hist_path in pp:
				assigned = pp[hist_path]
		enabled = is_pen_enabled(dp, alias, hist_path)
		rows.append([enabled, hist_path, pen_name, alias, eng_unit, pen_color, assigned, ""])
		pen_index += 1
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


def series_color_list(pens):
	"""Hex list for ApexCharts options.colors (parallel to enabled series order)."""
	out = []
	if pens is None:
		return out
	try:
		if pens.getRowCount() <= 0:
			return out
	except Exception:
		return out
	for pen in system.dataset.toPyDataSet(pens):
		try:
			if not pen["penEnabled"]:
				continue
		except Exception:
			continue
		try:
			color = pen["penColor"]
		except Exception:
			color = None
		if color in (None, ""):
			color = color_for_index(DEFAULT_COLORS, len(out))
		else:
			color = str(color)
		out.append(color)
	return out


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

	series_i = 0
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
			name = pen["penName"]
		except Exception:
			name = None
		if name in (None, ""):
			try:
				name = pen_label(pen["tagPath"])
			except Exception:
				name = None
		if name in (None, ""):
			name = alias
		try:
			color = pen["penColor"]
		except Exception:
			color = None
		if color in (None, ""):
			color = color_for_index(DEFAULT_COLORS, series_i)
		else:
			color = str(color)
		try:
			data = system.dataset.filterColumns(dataset, cols)
		except Exception:
			continue
		series.append({"name": str(name), "color": color, "data": data})
		series_i += 1
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
	name = str(title).strip() if title not in (None, "") else ""
	plots.append({
		"id": pid,
		"title": name or ("Plot %d" % n),
		"kind": kind or "analog",
	})
	_cfg_set(cfg, "plots", plots)
	return pid


def apply_add_plot(cfg, title=None, kind="analog"):
	"""add_plot() then return the plain plots list for session reassignment."""
	add_plot(cfg, title=title, kind=kind)
	return plain_plots(cfg)


POPUP_NAME_PLOT = "AdhocTrendNamePlot"
VIEW_NAME_PLOT = "98_Configuration/AdhocTrend/_Assets/NamePlot"
POPUP_REMOVE_PLOT = "AdhocTrendRemovePlot"
VIEW_REMOVE_PLOT = "98_Configuration/AdhocTrend/_Assets/RemovePlot"
DEFAULT_PLOT_ID = "p0"


def prompt_add_plot():
	"""Open the NamePlot popup; Confirm creates the plot, Cancel does nothing."""
	system.perspective.openPopup(
		id=POPUP_NAME_PLOT,
		view=VIEW_NAME_PLOT,
		params={},
		size={"width": 360, "height": 200},
		draggable=True,
		resizable=False,
		showCloseIcon=False,
		modal=True,
		overlayDismiss=False,
		viewportBound=True,
	)


def confirm_add_plot(cfg, title):
	"""Create an empty named plot after NamePlot Confirm.

	Returns (ok, message, plots). On failure plots is the current plain list
	(unchanged). On success plots is the updated plain list for session reassignment.
	"""
	name = str(title).strip() if title not in (None, "") else ""
	if not name:
		return False, "Enter a plot name.", plain_plots(cfg)
	plots = apply_add_plot(cfg, title=name)
	return True, "", plots


def close_name_plot_popup():
	"""Close the NamePlot popup if open."""
	try:
		system.perspective.closePopup(POPUP_NAME_PLOT)
	except Exception:
		pass


def removable_plots(cfg):
	"""Non-Default plots (everything except id p0). Default is never removable."""
	out = []
	for p in plain_plots(cfg):
		if str(p.get("id")) == DEFAULT_PLOT_ID:
			continue
		out.append(p)
	return out


def remove_plot(cfg, plot_id):
	"""Remove a non-Default plot; move its pens to Default.

	Returns (ok, message, plots, penPlots). Never removes p0/Default.
	"""
	normalize_config(cfg)
	plot_id = str(plot_id or "")
	plots = plain_plots(cfg)
	pen_plots = plain_pen_plots(cfg)
	if plot_id == DEFAULT_PLOT_ID:
		return False, "Cannot remove the Default plot.", plots, pen_plots
	if not any(str(p.get("id")) == plot_id for p in plots):
		return False, "Plot not found.", plots, pen_plots
	# Reassign pens that lived on the removed plot to Default
	for k, v in list(pen_plots.items()):
		if str(v) == plot_id:
			pen_plots[k] = DEFAULT_PLOT_ID
	plots = [p for p in plots if str(p.get("id")) != plot_id]
	if not plots:
		plots = default_plots()
	# Ensure Default still exists
	if not any(str(p.get("id")) == DEFAULT_PLOT_ID for p in plots):
		plots = default_plots() + plots
	_cfg_set(cfg, "plots", plots)
	_cfg_set(cfg, "penPlots", pen_plots)
	return True, "", plots, pen_plots


def prompt_remove_plot(cfg):
	"""Toolbar minus: auto-remove sole non-Default plot, or open picker.

	Returns (action, message, plots, penPlots) where action is one of:
	  'none'    — only Default exists (soft no-op)
	  'removed' — auto-removed the only removable plot
	  'prompt'  — opened RemovePlot popup for the operator to choose
	  'error'   — remove failed
	"""
	normalize_config(cfg)
	removable = removable_plots(cfg)
	plots = plain_plots(cfg)
	pen_plots = plain_pen_plots(cfg)
	if len(removable) == 0:
		return "none", "No removable plots. Default cannot be removed.", plots, pen_plots
	if len(removable) == 1:
		ok, msg, plots, pen_plots = remove_plot(cfg, removable[0]["id"])
		return ("removed" if ok else "error"), msg, plots, pen_plots
	system.perspective.openPopup(
		id=POPUP_REMOVE_PLOT,
		view=VIEW_REMOVE_PLOT,
		params={},
		size={"width": 360, "height": 220},
		draggable=True,
		resizable=False,
		showCloseIcon=False,
		modal=True,
		overlayDismiss=False,
		viewportBound=True,
	)
	return "prompt", "", plots, pen_plots


def confirm_remove_plot(cfg, plot_id):
	"""Remove the chosen plot after RemovePlot Confirm.

	Returns (ok, message, plots, penPlots).
	"""
	return remove_plot(cfg, plot_id)


def close_remove_plot_popup():
	"""Close the RemovePlot popup if open."""
	try:
		system.perspective.closePopup(POPUP_REMOVE_PLOT)
	except Exception:
		pass


def remove_plot_dropdown_options(cfg):
	"""Dropdown options for RemovePlot popup (non-Default only)."""
	return plot_dropdown_options(removable_plots(cfg))


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


# Layout chrome used to compute ApexCharts pixel height when Pens collapses.
# CSS flex alone fails: Plot defaultSize (480) caps the embed max-height, and
# ApexCharts keeps a fixed canvas px height until chart.height is a new number.
_FACEPLATE_TOTAL = 780
_FACEPLATE_HEADER = 40
_FACEPLATE_PAD = 8
_PAGE_HEADER = 48
_TREND_TOOLBAR = 58
_PENS_COLLAPSED = 32
_PENS_EXPANDED_FACEPLATE = 200
_PENS_EXPANDED_PAGE = 188
_PLOT_TITLE_ROW = 22


def plot_chart_height(faceplate_mode=False, pens_collapsed=False, plot_count=1, viewport_height=None):
	"""Pixel height for one plot's ApexCharts canvas.

	Pens collapse frees ~156–168px above the docked header; without an explicit
	pixel chart.height ApexCharts stays at its initial canvas size and leaves a
	gray band. Returns an int so Perspective/ApexCharts remounts on toggle.
	"""
	n = max(1, int(plot_count or 1))
	collapsed = bool(pens_collapsed)
	if faceplate_mode:
		body = _FACEPLATE_TOTAL - _FACEPLATE_HEADER - _FACEPLATE_PAD
		pens = _PENS_COLLAPSED if collapsed else _PENS_EXPANDED_FACEPLATE
	else:
		try:
			vh = int(viewport_height) if viewport_height not in (None, "") else 900
		except Exception:
			vh = 900
		if vh < 400:
			vh = 900
		body = vh - _PAGE_HEADER
		pens = _PENS_COLLAPSED if collapsed else _PENS_EXPANDED_PAGE
	plots_area = max(120, body - _TREND_TOOLBAR - pens)
	per = plots_area // n
	return max(120, int(per - _PLOT_TITLE_ROW))
