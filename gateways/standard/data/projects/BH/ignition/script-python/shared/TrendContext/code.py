"""Trend context menu + session trend basket (2026-10-23). See docs/trending.md.

Every historized value in the HMI calls menu() from its right-click (events.dom.onContextMenu, wired by
.cursor/tasks/trend-context/build.py):

	shared.TrendContext.menu(self, event, '{view.params.tagPath}/ZAT/Val')

The third argument is a path template: {view.params.x}, {view.custom.x}, {this.custom.x}, {session.custom.x},
{page.props.x} and {../Sibling.props.x} references are resolved against the component at click time.

Basket = session.custom.AdhocTrend.tags (what the Trending page, the faceplate trend and Saved Trends /
dbo.adhoc_trend_configs already use). session.custom.trend {pens, count, key} is a read-only summary bound from
it (session props), for the header badge and other readers. Pens are stored as full atomic history paths.

Historized check = shared.TrendHistorized (generated from the UDT definitions + tag config, no tag reads); paths
outside a known UDT instance fall back to one cached '.HistoryEnabled' property read per path.

The menu never writes tags: it only changes the session basket, navigates, and opens popups.
"""

import re

POPUP_MENU = "TrendContextMenu"
VIEW_MENU = "01_Popups/TrendContext/Menu"
POPUP_QUICK = "TrendQuickHistory"
VIEW_QUICK = "01_Popups/TrendContext/QuickHistory"
POPUP_TOAST = "TrendToast"
VIEW_TOAST = "01_Popups/TrendContext/Toast"
POPUP_COPY = "TrendCopyPath"
VIEW_COPY = "01_Popups/TrendContext/CopyPath"
TREND_PAGE = "/trending"
MAX_PENS = 10
MENU_W = 236
ROW_H = 30
HEAD_H = 53   # header 44 + first separator 9
SEP_H = 9

_hist_cache = {}
_unit_cache = {}
_REF = re.compile(r"\{([^{}]+)\}")


def _H():
	return shared.TrendHistorized


# ---------------------------------------------------------------- paths / historized lookup

def _split(path):
	"""'[prov]a/b' -> ('prov', 'a/b'); bare paths are [default]."""
	s = str(path or "").strip()
	if s.startswith("["):
		i = s.find("]")
		if i > 0:
			return s[1:i], s[i + 1:].strip("/")
	return "default", s.strip("/")


def full(path):
	prov, rel = _split(path)
	return ("[%s]%s" % (prov, rel)) if rel else ""


def owner(path):
	"""(instancePath, typeId, memberPath) when path is under a known top-level UDT instance, else (None, None, None)."""
	prov, rel = _split(path)
	if prov != "default" or not rel:
		return None, None, None
	parts = rel.split("/")
	inst = _H().INSTANCES
	for i in range(len(parts) - 1, 0, -1):
		p = "/".join(parts[:i])
		tid = inst.get(p)
		if tid:
			return p, tid, "/".join(parts[i:])
	return None, None, None


def is_historized(path):
	"""True when the atomic tag at path has history enabled (no getConfiguration; see module doc)."""
	prov, rel = _split(path)
	if not rel:
		return False
	if prov == "default":
		H = _H()
		if rel in H.tags():
			return True
		ov = H.OVERRIDES.get(rel)
		if ov is not None:
			return ov
		inst, tid, member = owner(path)
		if tid:
			return member in H.members(tid)
	key = full(path)
	hit = _hist_cache.get(key)
	if hit is None:
		try:
			qv = system.tag.readBlocking([key + ".HistoryEnabled"])[0]
			hit = bool(qv.quality.isGood() and qv.value)
		except:
			hit = False
		if len(_hist_cache) > 5000:
			_hist_cache.clear()
		_hist_cache[key] = hit
	return hit


def _legacy(tid, member):
	"""Pre-PAX member (saved trends) -> PlantPAx member of the same device, else None."""
	H = _H()
	new = H.LEGACY.get(tid, {}).get(member)
	if new and new in H.members(tid):
		return new
	leaf = member[:-6] if member.endswith("/Value") else member
	hits = [m for m in H.members(tid) if m.endswith("/" + leaf) and m.count("/") == 1]
	return hits[0] if len(hits) == 1 else None


def history_path(path):
	"""Full atomic path the historian stores: the path itself, or path + '/Value' for legacy _Root/* instances."""
	p = full(path)
	if not p:
		return ""
	inst, tid, member = owner(p)
	if tid and member not in _H().members(tid):
		new = _legacy(tid, member)
		if new:
			return "[default]%s/%s" % (inst, new)
	if p.endswith("/Value") or is_historized(p):
		return p
	if is_historized(p + "/Value"):
		return p + "/Value"
	return p


def label(path):
	"""Operator pen label: '<Device> <Member>' (e.g. 'CG-E4 Zone Temp', 'Comp 4 Discharge Pressure')."""
	hp = history_path(path)
	prov, rel = _split(hp)
	inst, tid, member = owner(hp)
	H = _H()
	if inst:
		device = inst.split("/")[-1]
		parts = [s for s in member.split("/") if s]
		words = []
		for i, seg in enumerate(parts):
			table = H.MEMBER_LABELS if i == len(parts) - 1 else H.NESTED_LABELS
			w = table.get(seg)
			if w is None:
				w = seg.replace("_", " ")
			if w and w not in words:
				words.append(w)
		return " ".join([device] + words)
	segs = [s for s in rel.split("/") if s]
	while len(segs) > 1 and segs[-1].lower() == "value":
		segs.pop()
	return " ".join(segs[-2:]) if segs else hp


def units(path):
	"""Engineering unit: static UDT engUnit when known, else one cached '.EngUnit' read."""
	hp = history_path(path)
	leaf = hp.split("/")[-1]
	u = _H().UNITS.get(leaf)
	if u:
		return u
	if hp in _unit_cache:
		return _unit_cache[hp]
	try:
		qv = system.tag.readBlocking([hp + ".EngUnit"])[0]
		u = qv.value if qv.quality.isGood() and qv.value not in (None, "") else ""
	except:
		u = ""
	u = unicode(u).replace(unichr(0xFFFD), u"°")   # U+FFFD in some UDT engUnits -> degree sign
	if len(_unit_cache) > 5000:
		_unit_cache.clear()
	_unit_cache[hp] = u
	return u


def all_paths():
	"""Every historized atomic tag the index knows (Trending page tag browser), full paths, sorted."""
	H = _H()
	out = []
	for inst in sorted(H.INSTANCES.keys()):
		for m in sorted(H.members(H.INSTANCES[inst])):
			if H.OVERRIDES.get(inst + "/" + m) is False:
				continue
			out.append("[default]%s/%s" % (inst, m))
	out.extend(["[default]" + t for t in sorted(H.tags())])
	return out


# ---------------------------------------------------------------- template resolution

def _walk(obj, dotted):
	for part in [p for p in dotted.split(".") if p]:
		if obj is None:
			return None
		nxt = None
		try:
			nxt = getattr(obj, part)
		except:
			try:
				nxt = obj[part]
			except:
				return None
		obj = nxt
	return obj


def _ref(component, ref):
	ref = ref.strip()
	try:
		if ref.startswith("view."):
			return _walk(component.view, ref[5:])
		if ref.startswith("this."):
			return _walk(component, ref[5:])
		if ref.startswith("session."):
			return _walk(component.session, ref[8:])
		if ref.startswith("page."):
			return _walk(component.page, ref[5:])
		if ref.startswith("parent."):
			return _walk(component.parent, ref[7:])
		if ref.startswith("../"):
			name, rest = (ref[3:].split(".", 1) + [""])[:2]
			return _walk(component.getSibling(name), rest)
	except:
		return None
	return None


def resolve(component, template):
	"""Substitute {...} property references in a path template; '' when any reference is empty."""
	t = str(template or "")
	empty = [False]

	def sub(m):
		v = _ref(component, m.group(1))
		if v in (None, ""):
			empty[0] = True
			return ""
		return unicode(v)

	out = _REF.sub(sub, t).strip()
	if empty[0]:
		return ""
	if out.startswith("pax:"):
		out = out[4:]
	return out


# ---------------------------------------------------------------- basket (session.custom.AdhocTrend)

def _cfg(session):
	try:
		return session.custom.AdhocTrend
	except:
		return None


def _tags(session):
	cfg = _cfg(session)
	try:
		raw = cfg.tags if cfg is not None else []
	except:
		raw = []
	return [unicode(t) for t in (raw or []) if t not in (None, "")]


def in_trend(session, path):
	hp = history_path(path)
	return bool(hp) and any(history_path(t) == hp for t in _tags(session))


def add(session, path, name=None):
	"""Add a historized tag to the session trend. Returns (ok, message)."""
	hp = history_path(path)
	name = name or label(hp)
	if not hp or not is_historized(hp):
		return False, "%s Is Not Historized" % name
	cfg = _cfg(session)
	if cfg is None:
		return False, "Trend Is Not Available In This Session"
	tags = _tags(session)
	if any(history_path(t) == hp for t in tags):
		return True, "%s Is Already In The Trend" % name
	if len(tags) >= MAX_PENS:
		return False, "Trend Is Full (%d Pens). Remove A Pen First." % MAX_PENS
	tags.append(hp)
	cfg.tags = tags
	cfg.colors = shared.AdhocTrend.palette_colors(cfg.colors)
	_pid, plots, penPlots = shared.AdhocTrend.route_new_pen(cfg, hp)
	cfg.plots = plots
	cfg.penPlots = penPlots
	return True, "Added %s To Trend" % name


def remove(session, path, name=None):
	"""Remove a tag (any stored form of it) from the session trend. Returns (ok, message)."""
	hp = history_path(path)
	name = name or label(hp)
	cfg = _cfg(session)
	if cfg is None:
		return False, "Trend Is Not Available In This Session"
	tags = _tags(session)
	keep = [t for t in tags if history_path(t) != hp]
	if len(keep) == len(tags):
		return True, "%s Is Not In The Trend" % name
	gone = set([t for t in tags if history_path(t) == hp] + [hp])
	aliases = set([shared.AdhocTrend.alias_for(t) for t in gone])
	pp = shared.AdhocTrend.plain_pen_plots(cfg)
	for k in list(pp.keys()):
		if k in gone or k in aliases:
			del pp[k]
	dp = shared.AdhocTrend.plain_disabled_pens(cfg)
	for k in list(dp.keys()):
		if k in gone or k in aliases:
			del dp[k]
	cfg.tags = keep
	cfg.penPlots = pp
	cfg.disabledPens = dp
	return True, "Removed %s From Trend" % name


def toggle(session, path, name=None):
	if in_trend(session, path):
		return remove(session, path, name)
	return add(session, path, name)


def summary(cfg):
	"""session.custom.trend from session.custom.AdhocTrend: {pens: [{tagPath, label, units, color, axis, plot}],
	count, key: '|path|path|'} (read-only; written by the session-props binding)."""
	tags = []
	try:
		tags = [unicode(t) for t in (shared.AdhocTrend._cfg_get(cfg, "tags", []) or []) if t not in (None, "")]
	except:
		tags = []
	plots = shared.AdhocTrend.plain_plots(cfg)
	titles = dict([(p["id"], p["title"]) for p in plots])
	first = plots[0]["id"] if plots else "p0"
	pp = shared.AdhocTrend.plain_pen_plots(cfg)
	colors = shared.AdhocTrend.palette_colors(shared.AdhocTrend._cfg_get(cfg, "colors", None))
	pens = []
	for i, t in enumerate(tags):
		hp = history_path(t)
		alias = shared.AdhocTrend.alias_for(hp)
		axis = pp.get(alias) or pp.get(t) or pp.get(hp) or first
		pens.append({"tagPath": hp, "label": label(hp), "units": units(hp),
			"color": shared.AdhocTrend.color_for_index(colors, i), "axis": axis, "plot": titles.get(axis, "")})
	return {"pens": pens, "count": len(pens), "key": "|" + "|".join([p["tagPath"] for p in pens]) + "|"}


# ---------------------------------------------------------------- popups

def _num(event, key):
	for getter in (lambda: getattr(event, key), lambda: event[key]):
		try:
			v = getter()
			if v is not None:
				return float(v)
		except:
			pass
	return None


def _viewport(component):
	try:
		d = component.page.props.dimensions.viewport
		return float(d.width or 0), float(d.height or 0)
	except:
		return 0.0, 0.0


def menu(component, event, template="", name=None):
	"""Right-click handler: open the trend context menu at the cursor (never a write action)."""
	path = resolve(component, template)
	if not path:
		return
	hp = history_path(path)
	hist = is_historized(hp)
	session = component.session
	try:
		ticket = bool(session.custom.TicketLogAccess)
	except:
		ticket = False
	try:
		view_name = component.view.id.split("@")[0]
	except:
		view_name = ""
	rows = (4 if hist else 2) + (1 if ticket else 0)
	height = HEAD_H + rows * ROW_H + SEP_H + 10   # + card padding 8 + border 2
	x = _num(event, "clientX")
	y = _num(event, "clientY")
	if x is None or y is None:
		x, y = _num(event, "pageX") or 200.0, _num(event, "pageY") or 200.0
	vw, vh = _viewport(component)
	left, top = x + 2, y + 2
	if vw and left + MENU_W > vw - 4:
		left = max(4, x - MENU_W - 2)
	if vh and top + height > vh - 4:
		top = max(4, vh - height - 4)
	params = {"tagPath": hp, "label": name or label(hp), "historized": hist,
		"inTrend": in_trend(session, hp) if hist else False, "ticketLog": ticket, "viewName": view_name}
	# no closePopup first: close + open of one id in a single script races on the client (menu flickers shut)
	system.perspective.openPopup(id=POPUP_MENU, view=VIEW_MENU, params=params,
		position={"left": int(left), "top": int(top), "width": MENU_W, "height": int(height)},
		showCloseIcon=False, draggable=False, resizable=False, modal=True, overlayDismiss=True, viewportBound=True)


def close_menu():
	try:
		system.perspective.closePopup(POPUP_MENU)
	except:
		pass


def menu_action(component, action):
	"""Menu row click (01_Popups/TrendContext/Menu). action: add | remove | open | quick | copy | ticket."""
	p = component.view.params
	path = unicode(p.tagPath or "")
	name = unicode(p.label or "") or None
	session = component.session
	close_menu()
	if not path:
		return
	if action in ("add", "remove", "toggle"):
		fn = {"add": add, "remove": remove, "toggle": toggle}[action]
		ok, msg = fn(session, path, name)
		toast(msg, "ok" if ok else "warn")
	elif action == "open":
		open_trend()
	elif action == "quick":
		quick_history(path, name)
	elif action == "copy":
		copy_path(path)
	elif action == "ticket":
		shared.Alerts.contextMenuTicketLog(path, unicode(p.viewName or ""))


def open_trend():
	system.perspective.navigate(page=TREND_PAGE)


def quick_history(path, name=None, hours=8):
	hp = history_path(path)
	system.perspective.openPopup(id=POPUP_QUICK, view=VIEW_QUICK,
		params={"tagPath": hp, "label": name or label(hp), "units": units(hp), "hours": hours},
		position={"width": 780, "height": 520}, showCloseIcon=False, draggable=True, resizable=True,
		modal=False, overlayDismiss=False, viewportBound=True)


def copy_path(path):
	system.perspective.openPopup(id=POPUP_COPY, view=VIEW_COPY, params={"tagPath": full(path)},
		position={"width": 520, "height": 150}, showCloseIcon=False, draggable=True, resizable=False,
		modal=True, overlayDismiss=True, viewportBound=True)


def toast(text, kind="ok"):
	system.perspective.openPopup(id=POPUP_TOAST, view=VIEW_TOAST,
		params={"text": unicode(text), "kind": kind, "openedAt": system.date.now()},
		position={"top": 56, "right": 16, "width": 420, "height": 44}, showCloseIcon=False, draggable=False,
		resizable=False, modal=False, overlayDismiss=False, viewportBound=True)


def copy_markdown(path):
	"""Markdown source for the CopyPath popup: a Copy button + one automatic copy attempt (client JS)."""
	p = unicode(path or "")
	attr = p.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
	js = ("var b=this.tagName=='BUTTON'?this:document.getElementById('tc-copy-btn');var t=b.getAttribute('data-p');"
		"var ok=function(){b.textContent='Copied';};"
		"var fb=function(){var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();"
		"try{document.execCommand('copy');ok();}catch(e){}document.body.removeChild(a);};"
		"if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(ok,fb);}else{fb();}")
	return (u'<button id="tc-copy-btn" class="tc-copy-btn" data-p="%s" onclick="%s">Copy</button>'
		u'<img src="data:image/png;base64,AAAA" style="display:none" onerror="%s">') % (attr, js, js)


# ---------------------------------------------------------------- Quick History chart helpers

def quick_key(path, aggregate="Average"):
	hp = history_path(path)
	if not hp:
		return []
	return [{"aggregate": aggregate or "Average", "alias": "pen", "path": hp}]


def quick_series(dataset, name, color=None):
	"""Single-pen ApexCharts series from a Wide history dataset (t_stamp + 'pen')."""
	if dataset is None:
		return []
	try:
		if dataset.getRowCount() <= 0:
			return []
		cols = columns(dataset)
	except:
		return []
	col = "pen" if "pen" in cols else ([c for c in cols if c != "t_stamp"] or [None])[0]
	if col is None:
		return []
	return [{"name": unicode(name or col), "color": color or "#008FFB", "data": points(dataset, col)}]


def is_tall(dataset):
	"""Tall history dataset (path, value, quality, timestamp): the only format that carries quality."""
	try:
		return "quality" in list(dataset.getColumnNames())
	except:
		return False


def columns(dataset):
	"""Pen columns: Wide = the column names; Tall = 't_stamp' + the distinct path / alias values."""
	try:
		cols = list(dataset.getColumnNames())
	except:
		return []
	if "quality" not in cols:
		return cols
	out = ["t_stamp"]
	pi = dataset.getColumnIndex("path")
	for r in range(dataset.getRowCount()):
		v = unicode(dataset.getValueAt(r, pi))
		if v not in out:
			out.append(v)
	return out


def _good(q):
	"""Quality code from a Tall row: bad / error codes are negative (Good = 192, Uncertain kept)."""
	try:
		return int(q) >= 0
	except:
		try:
			return bool(q.isGood()) or not bool(q.isBad())
		except:
			return True


def points(dataset, col):
	"""[[epochMs, value|None], ...] for one pen. The historian returns 0.0 for windows with bad quality (comm loss)
	or no data (before the first sample), so Tall rows with a bad quality become None: ApexCharts leaves a gap
	instead of drawing a false zero. Wide datasets carry no quality: only real nulls / NaN become gaps."""
	out = []
	try:
		tall = is_tall(dataset)
		ti = dataset.getColumnIndex("timestamp" if tall else "t_stamp")
		ci = dataset.getColumnIndex("value" if tall else col)
		pi = dataset.getColumnIndex("path") if tall else -1
		qi = dataset.getColumnIndex("quality") if tall else -1
		n = dataset.getRowCount()
	except:
		return out
	for r in range(n):
		if tall and unicode(dataset.getValueAt(r, pi)) != unicode(col):
			continue
		t = dataset.getValueAt(r, ti)
		try:
			ms = long(t.getTime())
		except:
			continue
		v = dataset.getValueAt(r, ci)
		if tall and not _good(dataset.getValueAt(r, qi)):
			v = None
		if v is not None:
			try:
				v = float(v)
				if v != v:
					v = None
			except:
				v = None
		out.append([ms, v])
	return out


# ---- chart tools on a single chart (faceplate Trend tab, Quick History): zoom state on the view ----------------------
# view.custom.zoomMin / zoomMax (epoch ms) drive the chart's xaxis.min / max and the "Zoomed: ..." chip; Reset Zoom /
# the chip / a double-click clear them and resetSeries() drops a value (Zoom Area) zoom. docs/trending.md


def _ev(obj, key):
	for get in (lambda: getattr(obj, key), lambda: obj[key]):
		try:
			v = get()
			if v is not None:
				return v
		except:
			pass
	return None


def _ms(v):
	if v is None:
		return None
	try:
		return long(v.getTime())
	except:
		pass
	try:
		return long(float(v))
	except:
		return None


def chart_zoomed(view, event, pause=False, chart=None):
	"""zoomedHandler / scrolledHandler: remember the window (and pause a live Quick History). Zoom Area: kyvis passes
	no yaxis and any options update re-applies the yaxis config, so the chart binds its x options to the values they
	had (zoomHoldMin / Max) and ApexCharts keeps the box."""
	now = system.date.toMillis(system.date.now())
	reset_at = _ms(view.custom.zoomResetAt)
	if reset_at and now - reset_at < 2000:
		return   # the zoomed callback ApexCharts fires right after its own reset
	x = _ev(event, "xaxis")
	lo = _ms(_ev(x, "min")) if x is not None else None
	hi = _ms(_ev(x, "max")) if x is not None else None
	area = view.custom.dragMode == "area" and chart is not None
	if area:
		view.custom.zoomHoldMin = chart.props.options.xaxis.min
		view.custom.zoomHoldMax = chart.props.options.xaxis.max
	view.custom.zoomKind = "area" if area else "time"
	if pause and view.custom.live:
		view.custom.pausedAt = system.date.now()
		view.custom.live = False
	if lo is not None and hi is not None and hi > lo:
		view.custom.zoomMin = lo
		view.custom.zoomMax = hi


def chart_reset(view, names):
	"""Reset Zoom / the zoomed chip / double-click: full range again on the chart(s) named (root children)."""
	view.custom.zoomMin = None
	view.custom.zoomMax = None
	view.custom.zoomKind = None
	view.custom.zoomResetAt = system.date.toMillis(system.date.now())
	for name in names:
		try:
			view.rootContainer.getChild(name).resetSeries(True, True)
		except:
			pass
