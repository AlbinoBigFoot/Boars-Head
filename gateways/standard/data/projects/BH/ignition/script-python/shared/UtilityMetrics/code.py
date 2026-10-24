# Utility Overview (OverviewKpis) metrics from the REAL plant data only: live reads for status / counts,
# historian for the averages and dwell hours. No history for a CG / range -> None / 0 (the view shows No Data).
# Written by .cursor/tasks/utility-overview-metrics/build.py - edit the builder source, not this copy.
#   zone temp   : CG ZAT/Val (P_AIn, historized)  -> time-weighted average of the raw samples (Good time only)
#   dwell hours : CG CG/Sts_State (historized from 2026-10-24) -> raw samples, hours held per state (Good only)
# History is cached in the gateway (system.util.getGlobals) for CACHE_MS: ONE batched queryTagHistory per refresh,
# shared by every client. Live values are a single readBlocking per call.

SECTIONS = [('Freezer', ['A1', 'A2']), ('SuperChill', ['B1', 'B2']), ('Club', ['C1']), ('Palletizing', ['D1']),
	('East PH', ['E1', 'E2', 'E3', 'E4']), ('West PH', ['F1', 'F2', 'F3', 'F4']),
	('Dock', ['G1', 'G2', 'G3', 'G4', 'G5'])]
STATUS_KEYS = ['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']
DWELL_KEYS = ['CLG', 'DFT', 'DFT PD', 'DFT HG', 'DFT BLD', 'DFT FD', 'IDLE', 'STOP', 'FLT']
MAIN_KEYS = ['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']
DFT_KEYS = ['DFT', 'DFT PD', 'DFT HG', 'DFT BLD', 'DFT FD']
CACHE_MS = 180000
# PLC CG_RL_Evap Sts_State -> HmiStatus code (same map as the Evaporator UDT HmiStatus expression)
STATE_TO_HMI = {0: 0, 1: 6, 2: 7, 3: 7, 4: 8, 5: 9, 6: 1, 7: 5, 8: 2, 9: 5, 10: 3}
HMI_TO_DWELL = {0: 'STOP', 1: 'CLG', 2: 'DFT', 3: 'FLT', 5: 'IDLE', 6: 'DFT PD', 7: 'DFT HG', 8: 'DFT BLD', 9: 'DFT FD'}


def _base(area, short):
	return '[default]Boars_Head/GrovePort/%s/Utility/CG-%s' % (area, short)


def _coarse(h):
	if h is None:
		return None
	if h == 1:
		return 'CLG'
	if h in (2, 6, 7, 8, 9):
		return 'DFT'
	if h == 3:
		return 'FLT'
	if h == 5:
		return 'IDLE'
	return 'STOP'


def _k(path):
	"""Dataset paths come back without the [provider] prefix."""
	p = str(path)
	return (p.split(']', 1)[1] if p.startswith('[') else p).lower()


def _is_good(q):
	try:
		return int(q) >= 192
	except:
		return str(q).lower().startswith('good')


def _raw(paths, start, end):
	"""ONE queryTagHistory for every path (temps + states): path -> [(ms, value, good)] sorted by time. A path with
	no rows has no history. Bounding values give the value in force at the start of the range."""
	rows = {}
	try:
		ds = system.tag.queryTagHistory(paths=paths, startDate=start, endDate=end, returnSize=-1,
			aggregationMode='LastValue', returnFormat='Tall', includeBoundingValues=True)
	except:
		system.util.getLogger('UtilityMetrics').warn('queryTagHistory failed')
		return rows
	for r in range(ds.getRowCount()):
		rows.setdefault(_k(ds.getValueAt(r, 0)), []).append(
			(system.date.toMillis(ds.getValueAt(r, 3)), ds.getValueAt(r, 1), _is_good(ds.getValueAt(r, 2))))
	for k in rows:
		rows[k].sort(key=lambda x: x[0])
	return rows


def _avg_temp(pts, s_ms, e_ms):
	"""Time-weighted average of the zone temp over the time it has Good samples (linear between neighbouring Good
	samples, the last Good sample held to the end of the range). Gaps (link outage, bad quality) are not counted.
	None = no Good data in the range."""
	area = 0.0
	covered = 0.0
	for i in range(len(pts)):
		t0, v0, g0 = pts[i]
		if not g0 or v0 is None:
			continue
		if i + 1 < len(pts):
			t1, v1, g1 = pts[i + 1]
			if not g1 or v1 is None:
				continue
		else:
			t1, v1 = e_ms, v0
		lo = max(t0, s_ms)
		hi = min(t1, e_ms)
		if hi <= lo:
			continue
		f = float(v1 - v0) / float(t1 - t0) if t1 > t0 else 0.0
		area += ((v0 + f * (lo - t0)) + (v0 + f * (hi - t0))) / 2.0 * (hi - lo)
		covered += hi - lo
	return None if covered <= 0 else area / covered


def _dwell_hours(pts, s_ms, e_ms):
	"""{dwell key: hours} the CG held each state (Good samples only); None = no Good state history in the range."""
	hrs = None
	for i in range(len(pts)):
		t0, v, g = pts[i]
		t1 = pts[i + 1][0] if i + 1 < len(pts) else e_ms
		t0 = max(t0, s_ms)
		t1 = min(t1, e_ms)
		if t1 <= t0 or v is None or not g:
			continue
		code = HMI_TO_DWELL.get(STATE_TO_HMI.get(int(v)))
		if code is None:
			continue
		if hrs is None:
			hrs = dict((k, 0.0) for k in DWELL_KEYS)
		hrs[code] += (t1 - t0) / 3600000.0
	return hrs


def _history(hours):
	"""Cached historian block for the last `hours` hours: {'temp': {path: avg}, 'dwell': {path: hrs}}."""
	g = system.util.getGlobals()
	cache = g.get('bhUtilityMetricsCache')
	if cache is None:
		cache = {}
		g['bhUtilityMetricsCache'] = cache
	now_ms = system.date.toMillis(system.date.now())
	hit = cache.get(hours)
	if hit is not None and now_ms - hit['at'] < CACHE_MS:
		return hit
	end = system.date.now()
	start = system.date.addHours(end, -hours)
	temp_paths = []
	state_paths = []
	for area, shorts in SECTIONS:
		for s in shorts:
			temp_paths.append(_base(area, s) + '/ZAT/Val')
			state_paths.append(_base(area, s) + '/CG/Sts_State')
	raw = _raw(temp_paths + state_paths, start, end)
	s_ms = system.date.toMillis(start)
	e_ms = system.date.toMillis(end)
	temp = {}
	dwell = {}
	for p in temp_paths:
		temp[p] = _avg_temp(raw.get(_k(p)) or [], s_ms, e_ms)
	for p in state_paths:
		dwell[p] = _dwell_hours(raw.get(_k(p)) or [], s_ms, e_ms)
	hit = {'at': now_ms, 'temp': temp, 'dwell': dwell}
	cache[hours] = hit
	return hit


def get(hours=24):
	hist = _history(hours)
	paths = []
	for area, shorts in SECTIONS:
		for s in shorts:
			paths.append(_base(area, s) + '/ZAT/Val')
			paths.append(_base(area, s) + '/HmiStatus')
	live = system.tag.readBlocking(paths)
	cats = []
	temps = []
	cgs = []
	sections = []
	counts = dict((k, 0) for k in STATUS_KEYS)
	acc = dict((k, 0.0) for k in DWELL_KEYS)
	n_dwell = 0
	i = 0
	for area, shorts in SECTIONS:
		sc = dict((k, 0) for k in STATUS_KEYS)
		stemps = []
		scats = []
		for s in shorts:
			base = _base(area, s)
			qt = live[i]
			qs = live[i + 1]
			i += 2
			t = None
			st = None
			try:
				if qt.quality.isGood() and qt.value is not None:
					t = float(qt.value)
				if qs.quality.isGood() and qs.value is not None:
					st = int(qs.value)
			except:
				pass
			a = hist['temp'].get(base + '/ZAT/Val')
			a = None if a is None else round(a, 1)
			code = _coarse(st)
			cats.append(s)
			temps.append(a)
			scats.append(s)
			stemps.append(a)
			if code is not None:
				sc[code] += 1
				counts[code] += 1
			d = hist['dwell'].get(base + '/CG/Sts_State')
			if d is not None:
				n_dwell += 1
				for k in DWELL_KEYS:
					acc[k] += d[k]
			cgs.append({'cg': 'CG-' + s, 'area': area, 'temp24': a, 'tempLive': None if t is None else round(t, 1),
				'tempTagPath': base + '/ZAT', 'status': code, 'statusRaw': st, 'navPage': '/cg-' + s.lower()})
		good = [x for x in stemps if x is not None]
		sections.append({'area': area, 'cgs': len(shorts), 'avgTemp': round(sum(good) / len(good), 1) if good else None,
			'cooling': sc['CLG'], 'defrost': sc['DFT'], 'idle': sc['IDLE'], 'stop': sc['STOP'], 'fault': sc['FLT'],
			'categories': scats, 'temps24': stemps})
	# average hours per CG that has Good state history (all zero = No Data in the view)
	dwell = dict((k, round(acc[k] / float(n_dwell), 1) if n_dwell else 0.0) for k in DWELL_KEYS)
	main = {'CLG': dwell['CLG'], 'DFT': round(sum(dwell[k] for k in DFT_KEYS), 1), 'IDLE': dwell['IDLE'],
		'STOP': dwell['STOP'], 'FLT': dwell['FLT']}
	good = [x for x in temps if x is not None]
	return {
		'categories': cats, 'temps24': temps, 'counts': counts,
		'avgTemp': (sum(good) / float(len(good))) if good else None,
		'cooling': counts['CLG'], 'defrost': counts['DFT'], 'idle': counts['IDLE'], 'stop': counts['STOP'],
		'fault': counts['FLT'],
		'statusHrsMainCategories': list(MAIN_KEYS), 'statusHrsMain': [main[k] for k in MAIN_KEYS],
		'statusHrsDftCategories': list(DFT_KEYS), 'statusHrsDft': [dwell[k] for k in DFT_KEYS],
		'statusHrsCategories': list(MAIN_KEYS), 'statusHrs': [main[k] for k in MAIN_KEYS],
		'statusHrsByKey': dwell, 'dwellCgs': n_dwell, 'hours': hours,
		'total': len(cgs), 'sections': sections, 'cgs': cgs,
		'sectionAvgs': [s['avgTemp'] for s in sections],
		'sectionNames': [s['area'] for s in sections],
		'sectionStatusSeries': [
			{'name': 'CLG', 'data': [s['cooling'] for s in sections]},
			{'name': 'DFT', 'data': [s['defrost'] for s in sections]},
			{'name': 'IDLE', 'data': [s['idle'] for s in sections]},
			{'name': 'STOP', 'data': [s['stop'] for s in sections]},
			{'name': 'FLT', 'data': [s['fault'] for s in sections]}],
	}


def _segments(pts, s_ms, e_ms):
	"""[(hmi_code, start_ms, end_ms)] of Good Sts_State samples, consecutive equal HMI codes merged."""
	segs = []
	for i in range(len(pts)):
		t0, v, g = pts[i]
		t1 = pts[i + 1][0] if i + 1 < len(pts) else e_ms
		t0 = max(t0, s_ms)
		t1 = min(t1, e_ms)
		if t1 <= t0 or v is None or not g:
			continue
		code = STATE_TO_HMI.get(int(v))
		if code is None:
			continue
		if segs and segs[-1][0] == code and segs[-1][2] == t0:
			segs[-1] = (code, segs[-1][1], t1)
		else:
			segs.append((code, t0, t1))
	return segs


def _clock(ms):
	return system.date.format(system.date.fromMillis(long(ms)), 'HH:mm')


def _dur(ms):
	sec = int(max(0, ms) / 1000)
	h = sec / 3600
	m = (sec % 3600) / 60
	if h > 0:
		return '%dh %dm' % (h, m)
	if m > 0:
		return '%dm' % m
	return '%ds' % sec


HMI_NAMES = {0: 'Off', 1: 'Cooling', 2: 'Defrost', 3: 'Fault', 5: 'Idle', 6: 'Pump Down', 7: 'Hot Gas', 8: 'Bleed',
	9: 'Fan Delay'}


def cg(tagPath, hours=12):
	"""CG History view payload (AhuEvapHistory): REAL historian data of ONE CG, cached 3 minutes per CG.
	series = Good ZAT/Val samples averaged into <= 90 time buckets (empty bucket = no point); status hours / rows =
	Good CG/Sts_State samples. No history -> empty series / zero hours / no rows (the view shows No Data)."""
	out = {'series': [], 'statusHrsMainCategories': list(MAIN_KEYS), 'statusHrsMain': [0.0] * len(MAIN_KEYS),
		'statusHrsDftCategories': list(DFT_KEYS), 'statusHrsDft': [0.0] * len(DFT_KEYS), 'rows': [], 'hours': hours}
	base = str(tagPath or '').strip()
	if not base:
		return out
	if not base.startswith('['):
		base = '[default]' + base
	cache = system.util.getGlobals().setdefault('bhUtilityMetricsCgCache', {})
	key = '%s|%s' % (_k(base), hours)
	now_ms = system.date.toMillis(system.date.now())
	hit = cache.get(key)
	if hit is not None and now_ms - hit['at'] < CACHE_MS:
		return hit['out']
	end = system.date.now()
	start = system.date.addHours(end, -hours)
	s_ms = system.date.toMillis(start)
	e_ms = system.date.toMillis(end)
	tp = base + '/ZAT/Val'
	sp = base + '/CG/Sts_State'
	raw = _raw([tp, sp], start, end)
	nb = 90
	width = float(e_ms - s_ms) / nb
	sums = [0.0] * nb
	cnt = [0] * nb
	for t, v, g in raw.get(_k(tp)) or []:
		if g and v is not None and s_ms <= t <= e_ms:
			b = min(nb - 1, int((t - s_ms) / width))
			sums[b] += float(v)
			cnt[b] += 1
	pts = [[int(s_ms + width * (b + 0.5)), round(sums[b] / cnt[b], 2)] for b in range(nb) if cnt[b]]
	if pts:
		out['series'] = [{'name': 'Zone Air Temp', 'data': pts}]
	state_pts = raw.get(_k(sp)) or []
	d = _dwell_hours(state_pts, s_ms, e_ms)
	if d is not None:
		d = dict((k, round(v, 2)) for k, v in d.items())
		out['statusHrsMain'] = [d['CLG'], round(sum(d[k] for k in DFT_KEYS), 2), d['IDLE'], d['STOP'], d['FLT']]
		out['statusHrsDft'] = [d[k] for k in DFT_KEYS]
	segs = _segments(state_pts, s_ms, e_ms)
	rows = []
	for i in range(len(segs)):
		code, a, b = segs[i]
		rows.append({'State': HMI_NAMES.get(code, 'Unknown'), 'Started': _clock(a),
			'Ended': 'Now' if (i == len(segs) - 1 and e_ms - b < 120000) else _clock(b), 'Duration': _dur(b - a)})
	rows.reverse()
	out['rows'] = rows
	cache[key] = {'at': now_ms, 'out': out}
	return out
