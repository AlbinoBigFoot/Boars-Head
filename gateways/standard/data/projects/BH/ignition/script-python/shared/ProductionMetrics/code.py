# Groveport FCM Chipotle Chicken line KPIs (deterministic demo generator + memory KPI tag overrides).
# Written by scripts/_build_groveport_production_overview.py (_METRICS_L1/L2/L3) - edit the builder, not this
# copy. value = the metrics expr-struct of the Production views (Level1/Overview, Level2/Kpis, Level3/Kpis):
#   l1: {sel, day, shift, dtRe, L_*/Z_*/U_* live tag values}; l2: {zone, Z_*, U_*}; l3: {unitId, U_*}.
# shared.Reports (custom report builder) calls l1 per day / shift / unit for the Production demo data.



def l1(value):
	# Synthetic FCM Chipotle Chicken line + device KPIs (deterministic demo).
	sel = str((value or {}).get('sel') or '')
	try:
		day_off = int((value or {}).get('day') or 0)
	except:
		day_off = 0
	shift_sel = str((value or {}).get('shift') or '')
	if shift_sel not in ('A', 'B', 'C'):
		shift_sel = ''
	dt_re = str((value or {}).get('dtRe') or '')
	now_ms = int(system.date.toMillis(system.date.now()))
	day_bucket = (now_ms // 86400000) - day_off
	# Scramble the day+shift into a well-mixed token. Java String.hashCode() is
	# sequential, so appending a raw day number changes the hash by ~1 between
	# consecutive days (metrics barely move). Mixing first spreads each day/shift
	# across the full range.
	shift_tok = shift_sel if shift_sel != '' else 'ALL'
	day_tok = str((day_bucket * 2654435761 + 1013904223) & 2147483647) + '_' + shift_tok
	day_start_ms = day_bucket * 86400000
	# Shift schedule (8h each): A 07:00-15:00, B 15:00-23:00, C 23:00-07:00.
	is_shift = shift_sel != ''
	shift_start_hr = {'A': 7, 'B': 15, 'C': 23}.get(shift_sel, 0)
	# Time-of-day awareness (only meaningful for TODAY / day_off == 0): a shift that
	# has not started yet has NO data; one in progress shows partial (elapsed) data.
	now_dt = system.date.now()
	cur_frac = system.date.getHour24(now_dt) + system.date.getMinute(now_dt) / 60.0
	shift_state = 'complete'   # complete | active | pending
	elapsed = 8.0
	if is_shift:
		if day_off != 0:
			shift_state = 'complete'
			elapsed = 8.0
		elif shift_sel == 'C':
			# C wraps midnight: 23:00 -> 07:00 next day
			if cur_frac >= 23.0:
				shift_state = 'active'; elapsed = cur_frac - 23.0
			elif cur_frac < 7.0:
				shift_state = 'active'; elapsed = cur_frac + 1.0
			else:
				shift_state = 'pending'
		else:
			s_end = shift_start_hr + 8
			if cur_frac < shift_start_hr:
				shift_state = 'pending'
			elif cur_frac >= s_end:
				shift_state = 'complete'
			else:
				shift_state = 'active'; elapsed = cur_frac - shift_start_hr
	shift_pending = (shift_state == 'pending')
	# Volume scaling + time window: full day = 24h; complete shift = 8h; active = elapsed.
	if not is_shift:
		win = 24.0; vol_factor = 1.0
	elif shift_state == 'pending':
		win = 0.0; vol_factor = 0.0
	elif shift_state == 'active':
		win = max(0.1, elapsed); vol_factor = elapsed / 24.0
	else:
		win = 8.0; vol_factor = 8.0 / 24.0
	shift_start_txt = {'A': '7:00 AM', 'B': '3:00 PM', 'C': '11:00 PM'}.get(shift_sel, '')
	shift_note = ('Shift ' + shift_sel + ' has not started yet \u2014 begins ' + shift_start_txt) if shift_pending else ''

	units_cfg = [('VD', 'Vat Dumper', 'Prep'), ('HOP', 'Hopper', 'Prep'), ('HND', 'Handtman', 'Forming'), ('LDR', 'Loaders', 'Forming'), ('RSM', 'Roll Stock', 'Packaging'), ('ST', 'Shrink Tunnel', 'Packaging'), ('LS', 'Lazy Susan', 'Packaging')]

	def synth(key, lo, hi):
		seed = abs(hash(str(key) + '#' + day_tok)) % 10007
		return lo + (float(seed % 1000) / 1000.0) * (hi - lo)

	# --- Line-level throughput / OEE ---
	line_rate = int(round(synth('line_rate', 820, 980), 0))
	line_target = 950
	rate_vs_target = round((float(line_rate) / float(line_target) - 1.0) * 100.0, 1)
	attainment = round(float(line_rate) / float(line_target) * 100.0, 1)

	availability = round(synth('avail', 80, 98), 1)
	performance = round(synth('perf', 70, 96), 1)
	quality = round(synth('qual', 92, 99.5), 1)
	oee = round(availability * performance * quality / 10000.0, 1)

	cases = int(round(synth('cases_today', 4200, 5100) * vol_factor, 0))
	yield_pct = round(synth('yield', 92, 98.5), 1)
	reject = round(synth('reject_pct', 0.8, 2.4), 2)
	dt_min = int(round(synth('downtime', 12, 45) * vol_factor, 0))
	uptime = round(synth('uptime', 91, 98), 1)
	run_hrs = synth('run_time', win * 0.55, win * 0.95)
	run_time = '%dh %02dm' % (int(run_hrs), int((run_hrs - int(run_hrs)) * 60))
	shift = shift_sel if is_shift else 'All'

	# --- Downtime Pareto (minutes, sorted desc) ---
	dt_reasons = ['Changeover', 'Mechanical', 'Sanitation', 'Material', 'Minor Stops']
	dt_pairs = []
	for rn in dt_reasons:
		dt_pairs.append((rn, int(round(synth('dt_' + rn, 2, 20) * vol_factor, 0))))
	dt_pairs = sorted(dt_pairs, key=lambda p: -p[1])
	dt_labels = [p[0] for p in dt_pairs]
	dt_values = [p[1] for p in dt_pairs]

	# --- Downtime time-series (minutes per hour, over the window) ---
	n_pts = int(win)
	dt_ts = []
	for h in range(n_pts):
		dt_ts.append([day_start_ms + (shift_start_hr + h) * 3600000,
		              int(round(synth('dtts_' + str(h), 0, 8), 0))])

	# --- Line rate time-series (lb/hr per hour, over the window) ---
	rate_ts = []
	for h in range(n_pts):
		rate_ts.append([day_start_ms + (shift_start_hr + h) * 3600000,
		               int(round(synth('ratets_' + str(h), line_rate * 0.82, line_rate * 1.08), 0))])

	# --- Time in state (window hours) ---
	st_run = round(synth('tis_run', win * 0.72, win * 0.9), 1)
	st_change = round(synth('tis_chg', win * 0.03, win * 0.11), 1)
	st_idle = round(synth('tis_idle', win * 0.02, win * 0.09), 1)
	st_fault = round(max(0.0, win - st_run - st_change - st_idle), 1)
	tis_labels = ['Running', 'Changeover', 'Idle', 'Fault']
	tis_values = [st_run, st_change, st_idle, st_fault]

	# --- Per-unit rows ---
	unit_rows = []
	active_alarms = 0
	units_running = 0
	for uid, uname, uz in units_cfg:
		st_roll = synth(uid + '_run', 0, 1)
		status = 'Running' if st_roll > 0.10 else ('Fault' if st_roll < 0.02 else 'Idle')
		if status == 'Running':
			units_running += 1
		alm = int(round(synth(uid + '_alm', 0, 1.35), 0))
		active_alarms += alm
		unit_rows.append({
			'Unit': uname,
			'UnitId': uid,
			'Zone': uz,
			'Status': status,
			'Rate': int(round(synth(uid + '_rate', 80, 145), 0)),
			'OEE': round(synth(uid + '_oee', 68, 96), 1),
			'Reject': round(synth(uid + '_reject', 0.5, 3.2), 2),
			'Alarms': alm,
		})

	# --- Memory KPI tags (Today / All Shifts): Boars_Head/GrovePort/Production/FCM line, zone, unit ---
	# struct keys L_* / Z_<zone>_* / U_<unit>_* (l1_live_struct); a missing / bad tag keeps the synthetic value
	def lv(k):
		try:
			v = (value or {}).get(k)
			return None if v is None else float(v)
		except:
			return None
	live = day_off == 0 and not is_shift and lv('L_Rate') is not None
	st_names = {1: 'Running', 3: 'Fault', 5: 'Idle'}
	if live:
		units_running = 0
		for r in unit_rows:
			uid = str(r['UnitId'])
			if lv('U_' + uid + '_Status') is not None:
				r['Status'] = st_names.get(int(lv('U_' + uid + '_Status')), 'Idle')
			if lv('U_' + uid + '_OEE') is not None:
				r['OEE'] = round(lv('U_' + uid + '_OEE'), 1)
			if lv('U_' + uid + '_Reject') is not None:
				r['Reject'] = round(lv('U_' + uid + '_Reject'), 2)
			if r['Status'] == 'Running':
				units_running += 1
		line_rate = int(round(lv('L_Rate'), 0))
		rate_vs_target = round((float(line_rate) / float(line_target) - 1.0) * 100.0, 1)
		attainment = round(float(line_rate) / float(line_target) * 100.0, 1)
		if lv('L_Availability') is not None:
			availability = round(lv('L_Availability'), 1)
		if lv('L_Performance') is not None:
			performance = round(lv('L_Performance'), 1)
		if lv('L_Quality') is not None:
			quality = round(lv('L_Quality'), 1)
		oee = round(availability * performance * quality / 10000.0, 1)
		if lv('L_Cases') is not None:
			cases = int(round(lv('L_Cases'), 0))
		if lv('L_Yield') is not None:
			yield_pct = round(lv('L_Yield'), 1)
		if lv('L_Reject') is not None:
			reject = round(lv('L_Reject'), 2)
		if lv('L_Uptime') is not None:
			uptime = round(lv('L_Uptime'), 1)

	# --- Zone rollups ---
	zone_rows = []
	zone_labels = []
	zone_rate_series = []
	zone_oee_series = []
	for zid in ['Prep', 'Forming', 'Packaging']:
		z_units = [r for r in unit_rows if str(r.get('Zone')) == zid]
		z_running = len([r for r in z_units if str(r.get('Status')) == 'Running'])
		z_alarms = sum(int(r.get('Alarms') or 0) for r in z_units)
		z_fault = any(str(r.get('Status')) == 'Fault' for r in z_units)
		z_status = 'Fault' if z_fault else ('Running' if z_running == len(z_units) and z_units else 'Idle')
		z_rate = int(round(synth('z_' + zid + '_rate', 780, 960), 0))
		z_oee = round(synth('z_' + zid + '_oee', 70, 93), 1)
		zone_labels.append(zid)
		zone_rate_series.append(z_rate)
		zone_oee_series.append(z_oee)
		zone_rows.append({
			'Zone': zid,
			'Status': z_status,
			'Rate': z_rate,
			'OEE': z_oee,
			'Downtime': int(round(synth('z_' + zid + '_dt', 4, 22), 0)),
			'Running': '%d/%d' % (z_running, len(z_units)),
			'Alarms': z_alarms,
		})

	if live:
		for zi in range(len(zone_rows)):
			zid = str(zone_rows[zi]['Zone'])
			if lv('Z_' + zid + '_Rate') is not None:
				zone_rows[zi]['Rate'] = int(round(lv('Z_' + zid + '_Rate'), 0))
				zone_rate_series[zi] = zone_rows[zi]['Rate']
			if lv('Z_' + zid + '_OEE') is not None:
				zone_rows[zi]['OEE'] = round(lv('Z_' + zid + '_OEE'), 1)
				zone_oee_series[zi] = zone_rows[zi]['OEE']

	# --- Active alarm feed (always 2-4 items, day/shift-aware) ---
	alarm_msgs = {
		'VD': 'Vat low level',
		'HOP': 'Hopper level high',
		'HND': 'Portioner over-torque',
		'LDR': 'Loader jam detected',
		'RSM': 'Film supply low',
		'ST': 'Tunnel temp deviation',
		'LS': 'Tree table full',
	}
	alarm_pool = [
		('HND', 'High', 'Portioner over-torque'),
		('ST', 'High', 'Tunnel temp deviation'),
		('LDR', 'Medium', 'Loader jam detected'),
		('RSM', 'Medium', 'Film supply low'),
		('HOP', 'Low', 'Hopper level high'),
		('VD', 'Low', 'Vat low level'),
		('LS', 'Medium', 'Tree table full'),
	]
	uid_to_name = dict((str(u[0]), u[1]) for u in units_cfg)
	n_active = 2 + int(round(synth('n_active', 0, 2.4), 0))  # 2..4
	alarm_rows = []
	used_idx = []
	for i in range(n_active):
		idx = abs(hash('ap_' + str(i) + '#' + day_tok)) % len(alarm_pool)
		if idx in used_idx:
			idx = (idx + 1) % len(alarm_pool)
		used_idx.append(idx)
		p_uid, p_pri, p_msg = alarm_pool[idx]
		mm = int(round(synth('am_' + str(i), 1, 180), 0))
		alarm_rows.append({'Age': str(mm) + 'm', 'Unit': uid_to_name.get(p_uid, p_uid),
		                   'Priority': p_pri, 'Message': p_msg})
	alarm_rows = sorted(alarm_rows, key=lambda a: {'High': 0, 'Medium': 1, 'Low': 2}.get(a['Priority'], 3))

	# --- Line alarm summary (for previous-day rollups) ---
	la_reasons = ['Changeover', 'Mechanical', 'Sanitation', 'Material', 'Sensor Fault', 'Temp Deviation']
	la_counts = [(rn, int(round(synth('la_c_' + rn, 1, 11) * vol_factor, 0))) for rn in la_reasons]
	la_sorted = sorted(la_counts, key=lambda p: -p[1])
	la_top = la_sorted[0]
	la_total = sum(c for _, c in la_counts)
	la_dur = int(round(synth('la_dur', 60, 240) * vol_factor, 0))
	la_avg = round(float(la_dur) / float(max(1, la_total)), 1)
	la_high = int(round(synth('la_high', 0, 5), 0))
	la_long = int(round(synth('la_long', 10, 45), 0))
	alarm_summary = [
		{'Metric': 'Total Alarms', 'Value': str(la_total)},
		{'Metric': 'Most Frequent', 'Value': la_top[0] + ' (' + str(la_top[1]) + ')'},
		{'Metric': 'High Priority', 'Value': str(la_high)},
		{'Metric': 'Total Duration', 'Value': str(la_dur) + ' min'},
		{'Metric': 'Avg Duration', 'Value': str(la_avg) + ' min'},
		{'Metric': 'Longest Alarm', 'Value': str(la_long) + ' min'},
	]

	# --- Scope-neutral outputs (line by default; overridden per-device below) ---
	line_state = 'Warning' if len([a for a in alarm_rows if a['Priority'] == 'High']) > 0 else 'Running'
	o_state = line_state
	o_rate = line_rate
	o_target = line_target
	o_vs = rate_vs_target
	o_oee = oee
	o_avail = availability
	o_perf = performance
	o_qual = quality
	o_oeecomp = [availability, performance, quality]
	o_tput = 'Cases ' + str(cases)
	o_yield = yield_pct
	o_reject = reject
	o_uptime = uptime
	o_alarms = len(alarm_rows)
	o_runtime = run_time
	o_dtlabels = dt_labels
	o_dtvalues = dt_values
	o_dtts = dt_ts
	o_ratets = rate_ts
	o_tis = tis_values
	scope_name = 'FCM Chipotle Chicken Line'

	# --- Device-scope tables (empty unless a device is selected) ---
	d_signals = []
	d_shifts = []
	d_alarms = []
	if sel != '':
		uname_sel = sel
		uz_sel = 'Prep'
		for cfg_id, cfg_name, cfg_zone in units_cfg:
			if str(cfg_id) == sel:
				uname_sel = cfg_name
				uz_sel = cfg_zone
				break
		scope_name = uname_sel
		d_st_roll = synth(sel + '_run', 0, 1)
		o_state = 'Running' if d_st_roll > 0.08 else 'Idle'
		d_rate = int(round(synth(sel + '_rate', 80, 145), 0))
		d_target = 130
		o_rate = d_rate
		o_target = d_target
		o_vs = round((float(d_rate) / float(d_target) - 1.0) * 100.0, 1)
		o_avail = round(synth(sel + '_avail', 80, 98), 1)
		o_perf = round(synth(sel + '_perf', 70, 96), 1)
		o_qual = round(synth(sel + '_qual', 92, 99.6), 1)
		o_oee = round(o_avail * o_perf * o_qual / 10000.0, 1)
		o_oeecomp = [o_avail, o_perf, o_qual]
		o_yield = round(synth(sel + '_yield', 92, 99), 1)
		o_reject = round(synth(sel + '_reject', 0.3, 2.6), 2)
		o_uptime = round(synth(sel + '_uptime', 90, 99), 1)
		d_run_hrs = synth(sel + '_runhrs', win * 0.5, win * 0.95)
		o_runtime = '%dh %02dm' % (int(d_run_hrs), int((d_run_hrs - int(d_run_hrs)) * 60))
		o_tput = 'Units ' + str(int(round(synth(sel + '_units', 900, 2400) * vol_factor, 0)))
		d_reasons = ['Changeover', 'Mechanical', 'Sanitation', 'Startup', 'Minor Stops']
		d_pairs = []
		for rn in d_reasons:
			d_pairs.append((rn, int(round(synth(sel + '_dt_' + rn, 1, 16) * vol_factor, 0))))
		d_pairs = sorted(d_pairs, key=lambda p: -p[1])
		o_dtlabels = [p[0] for p in d_pairs]
		o_dtvalues = [p[1] for p in d_pairs]
		d_dtts = []
		d_ratets = []
		for h in range(int(win)):
			d_dtts.append([day_start_ms + (shift_start_hr + h) * 3600000,
			              int(round(synth(sel + '_dtts_' + str(h), 0, 6), 0))])
			d_ratets.append([day_start_ms + (shift_start_hr + h) * 3600000,
			               int(round(synth(sel + '_ratets_' + str(h), d_rate * 0.8, d_rate * 1.1), 0))])
		o_dtts = d_dtts
		o_ratets = d_ratets
		d_run = round(synth(sel + '_tis_run', win * 0.74, win * 0.9), 1)
		d_chg = round(synth(sel + '_tis_chg', win * 0.03, win * 0.1), 1)
		d_idle = round(synth(sel + '_tis_idle', win * 0.01, win * 0.08), 1)
		d_flt = round(max(0.0, win - d_run - d_chg - d_idle), 1)
		o_tis = [d_run, d_chg, d_idle, d_flt]
		if live:
			if lv('U_' + sel + '_Status') is not None:
				o_state = st_names.get(int(lv('U_' + sel + '_Status')), 'Idle')
			if lv('U_' + sel + '_OEE') is not None:
				o_oee = round(lv('U_' + sel + '_OEE'), 1)
				# keep Availability x Performance x Quality = OEE
				o_perf = round(min(100.0, o_oee * 10000.0 / max(1.0, o_avail * o_qual)), 1)
				o_oeecomp = [o_avail, o_perf, o_qual]
			if lv('U_' + sel + '_Reject') is not None:
				o_reject = round(lv('U_' + sel + '_Reject'), 2)

		def okpi(v, tgt):
			return 'OK' if v >= tgt else 'Low'
		d_signals = [
			{'Metric': 'Rate (lb/hr)', 'Value': str(d_rate), 'Target': str(d_target), 'Status': okpi(d_rate, d_target)},
			{'Metric': 'OEE (%)', 'Value': str(o_oee), 'Target': '85.0', 'Status': okpi(o_oee, 85.0)},
			{'Metric': 'Availability (%)', 'Value': str(o_avail), 'Target': '90.0', 'Status': okpi(o_avail, 90.0)},
			{'Metric': 'Performance (%)', 'Value': str(o_perf), 'Target': '88.0', 'Status': okpi(o_perf, 88.0)},
			{'Metric': 'Quality (%)', 'Value': str(o_qual), 'Target': '98.0', 'Status': okpi(o_qual, 98.0)},
			{'Metric': 'Reject (%)', 'Value': str(o_reject), 'Target': '2.00', 'Status': 'OK' if o_reject <= 2.0 else 'High'},
			{'Metric': 'Uptime (%)', 'Value': str(o_uptime), 'Target': '95.0', 'Status': okpi(o_uptime, 95.0)},
		]
		for sh in ['A', 'B', 'C']:
			d_shifts.append({
				'Shift': sh,
				'Rate': int(round(synth(sel + '_sh_' + sh + '_rate', 80, 145), 0)),
				'OEE': round(synth(sel + '_sh_' + sh + '_oee', 68, 96), 1),
				'Downtime': int(round(synth(sel + '_sh_' + sh + '_dt', 3, 24), 0)),
				'Alarms': int(round(synth(sel + '_sh_' + sh + '_alm', 0, 2.4), 0)),
			})
		d_amsg = ['High discharge temp', 'Low supply pressure', 'Sensor fault', 'Speed deviation', 'Maintenance due']
		d_ncount = int(round(synth(sel + '_almcount', 0, 2.4), 0))
		for ai in range(d_ncount):
			d_pri = 'High' if synth(sel + '_apri_' + str(ai), 0, 1) > 0.7 else ('Medium' if synth(sel + '_apri2_' + str(ai), 0, 1) > 0.5 else 'Low')
			d_alarms.append({
				'Priority': d_pri,
				'Message': d_amsg[abs(hash(sel + str(ai) + str(day_bucket))) % len(d_amsg)],
				'Age': str(int(round(synth(sel + '_aage_' + str(ai), 1, 220), 0))) + 'm',
			})
		d_alarms = sorted(d_alarms, key=lambda a: {'High': 0, 'Medium': 1, 'Low': 2}.get(a['Priority'], 3))
		o_alarms = len(d_alarms)
		da_reasons = ['High Temp', 'Low Pressure', 'Sensor Fault', 'Speed Dev', 'Maint Due']
		da_counts = [(rn, int(round(synth(sel + '_da_' + rn, 0, 8), 0))) for rn in da_reasons]
		da_sorted = sorted(da_counts, key=lambda p: -p[1])
		da_top = da_sorted[0]
		da_total = sum(c for _, c in da_counts)
		da_dur = int(round(synth(sel + '_da_dur', 20, 150), 0))
		da_avg = round(float(da_dur) / float(max(1, da_total)), 1)
		da_high = int(round(synth(sel + '_da_high', 0, 4), 0))
		da_long = int(round(synth(sel + '_da_long', 6, 35), 0))
		alarm_summary = [
			{'Metric': 'Total Alarms', 'Value': str(da_total)},
			{'Metric': 'Most Frequent', 'Value': da_top[0] + ' (' + str(da_top[1]) + ')'},
			{'Metric': 'High Priority', 'Value': str(da_high)},
			{'Metric': 'Total Duration', 'Value': str(da_dur) + ' min'},
			{'Metric': 'Avg Duration', 'Value': str(da_avg) + ' min'},
			{'Metric': 'Longest Alarm', 'Value': str(da_long) + ' min'},
		]

	# --- Downtime detail events (Start / Stop / Duration) for a drilled reason ---
	# Split that reason's Pareto total into 1-3 events across the window so the
	# detail rows reconcile with the bar the user clicked.
	dt_events = []
	if dt_re != '' and not shift_pending:
		tgt = 0
		for _li in range(len(o_dtlabels)):
			if str(o_dtlabels[_li]) == dt_re:
				tgt = int(o_dtvalues[_li])
				break
		if tgt > 0:
			n_ev = 1 + int(round(synth('deN_' + dt_re, 0, 2.4), 0))  # 1..3
			parts = []
			remaining = tgt
			for i in range(n_ev):
				if i == n_ev - 1:
					parts.append(remaining)
				else:
					floor = n_ev - 1 - i
					mx = max(1, remaining - floor)
					p = 1 + int(round(synth('deP_' + dt_re + str(i), 0, max(0, mx - 1)), 0))
					if p > remaining - floor:
						p = remaining - floor
					parts.append(p)
					remaining -= p
			base_hr = shift_start_hr if is_shift else 6
			span = (win if is_shift else 16.0)
			if span < 1.0:
				span = 1.0
			for i in range(n_ev):
				start_off = synth('deS_' + dt_re + str(i), 0, span)
				dur_min = parts[i]
				start_ms = day_start_ms + int((base_hr + start_off) * 3600000)
				stop_ms = start_ms + dur_min * 60000
				dt_events.append({
					'Start': system.date.format(system.date.fromMillis(start_ms), 'MM/dd HH:mm'),
					'Stop': system.date.format(system.date.fromMillis(stop_ms), 'MM/dd HH:mm'),
					'Duration': str(dur_min) + ' min',
					'_s': start_ms,
				})
			dt_events = sorted(dt_events, key=lambda e: e['_s'])
			for e in dt_events:
				del e['_s']

	# --- Pending shift (today, not started yet): no data anywhere ---
	if shift_pending:
		o_rate = 0; o_vs = 0.0; o_oee = 0.0; o_avail = 0.0; o_perf = 0.0; o_qual = 0.0
		o_oeecomp = [0, 0, 0]; cases = 0; o_tput = 'No Data'; o_yield = 0.0; o_reject = 0.0
		dt_min = 0; o_uptime = 0.0; o_runtime = '0h 00m'; o_alarms = 0; o_state = 'Not Started'
		o_dtlabels = []; o_dtvalues = []; o_dtts = []; o_ratets = []; o_tis = [0, 0, 0, 0]
		zone_rows = []; zone_labels = []; zone_rate_series = []; zone_oee_series = []
		unit_rows = []; units_running = 0; alarm_rows = []
		d_signals = []; d_shifts = []; d_alarms = []; dt_events = []
		alarm_summary = [
			{'Metric': 'Total Alarms', 'Value': '0'},
			{'Metric': 'Most Frequent', 'Value': '--'},
			{'Metric': 'High Priority', 'Value': '0'},
			{'Metric': 'Total Duration', 'Value': '0 min'},
			{'Metric': 'Avg Duration', 'Value': '0 min'},
			{'Metric': 'Longest Alarm', 'Value': '0 min'},
		]

	# --- Downtime event count over the window (1-3 events per reason, as in the drill-down detail) ---
	dt_event_count = 0
	for _ri in range(len(o_dtlabels)):
		if int(o_dtvalues[_ri]) > 0:
			dt_event_count += 1 + int(round(synth('deN_' + str(o_dtlabels[_ri]), 0, 2.4), 0))

	return {
		'scope': 'unit' if sel != '' else 'line',
		'scopeName': scope_name,
		'lineRate': o_rate,
		'lineTarget': o_target,
		'rateVsTarget': o_vs,
		'attainmentPct': round(float(o_rate) / float(o_target) * 100.0, 1),
		'oee': o_oee,
		'availability': o_avail,
		'performance': o_perf,
		'quality': o_qual,
		'oeeComponents': o_oeecomp,
		'oeeComponentLabels': ['Availability', 'Performance', 'Quality'],
		'casesToday': cases,
		'throughputLabel': o_tput,
		'yieldPct': o_yield,
		'rejectPct': o_reject,
		'downtimeMin': dt_min,
		'uptimePct': o_uptime,
		'runTime': o_runtime,
		'shift': shift,
		'lineState': o_state,
		'activeAlarms': o_alarms,
		'unitsRunning': units_running,
		'unitsRunningLabel': str(units_running) + ' / ' + str(len(unit_rows)),
		'unitsTotal': len(unit_rows),
		'dtLabels': o_dtlabels,
		'dtValues': o_dtvalues,
		'dtSeries': ([{'name': 'Downtime (min)', 'data': o_dtts}] if o_dtts else []),
		'rateSeries': ([{'name': 'lb/hr', 'data': o_ratets}] if o_ratets else []),
		'dtEvents': dt_events,
		'dtEventCount': dt_event_count,
		'dtDetailReason': dt_re,
		'windowHours': int(win),
		'shiftLabel': ('Shift ' + shift_sel) if is_shift else 'All Shifts',
		'shiftState': shift_state if is_shift else 'na',
		'shiftPending': shift_pending,
		'shiftNote': shift_note,
		'tisLabels': tis_labels,
		'tisValues': o_tis,
		'zoneLabels': zone_labels,
		'zoneRateSeries': zone_rate_series,
		'zoneOeeSeries': zone_oee_series,
		'zones': zone_rows,
		'units': unit_rows,
		'unitById': dict((str(r['UnitId']), r) for r in unit_rows),
		'alarms': alarm_rows,
		'dSignals': d_signals,
		'dShifts': d_shifts,
		'dAlarms': d_alarms,
		'alarmSummary': alarm_summary,
	}


def l2(value):
	zone = str(value.get('zone') or 'Prep')
	now_ms = int(system.date.toMillis(system.date.now()))
	hour_bucket = now_ms // 3600000
	units_cfg = [('VD', 'Vat Dumper', 'Prep'), ('HOP', 'Hopper', 'Prep'), ('HND', 'Handtman', 'Forming'), ('LDR', 'Loaders', 'Forming'), ('RSM', 'Roll Stock', 'Packaging'), ('ST', 'Shrink Tunnel', 'Packaging'), ('LS', 'Lazy Susan', 'Packaging')]

	def synth(key, lo, hi):
		seed = abs(hash(str(key) + str(hour_bucket))) % 10007
		return lo + (float(seed % 1000) / 1000.0) * (hi - lo)

	zone_rate = round(synth('z_'+zone+'_rate', 780, 960), 0)
	zone_oee = round(synth('z_'+zone+'_oee', 70, 93), 1)
	zone_dt = int(round(synth('z_'+zone+'_dt', 4, 22), 0))

	unit_rows = []
	for uid, uname, uz in units_cfg:
		if str(uz) != zone:
			continue
		st_roll = synth(uid+'_run', 0, 1)
		status = 'Running' if st_roll > 0.12 else ('Fault' if st_roll < 0.04 else 'Idle')
		unit_rows.append({
			'Unit': uname,
			'UnitId': uid,
			'Status': status,
			'Rate': round(synth(uid+'_rate', 80, 145), 0),
			'OEE': round(synth(uid+'_oee', 68, 96), 1),
			'Alarms': int(round(synth(uid+'_alm', 0, 3), 0)),
		})

	# Memory KPI tags (l2_live_struct): zone Rate / OEE, unit Status / OEE; missing tag -> synthetic
	def lv(k):
		try:
			v = (value or {}).get(k)
			return None if v is None else float(v)
		except:
			return None
	if lv('Z_Rate') is not None:
		zone_rate = round(lv('Z_Rate'), 0)
	if lv('Z_OEE') is not None:
		zone_oee = round(lv('Z_OEE'), 1)
	for r in unit_rows:
		uid = str(r['UnitId'])
		if lv('U_' + uid + '_Status') is not None:
			r['Status'] = {1: 'Running', 3: 'Fault', 5: 'Idle'}.get(int(lv('U_' + uid + '_Status')), 'Idle')
		if lv('U_' + uid + '_OEE') is not None:
			r['OEE'] = round(lv('U_' + uid + '_OEE'), 1)

	return {
		'zone': zone,
		'zoneRate': zone_rate,
		'zoneOee': zone_oee,
		'zoneDowntime': zone_dt,
		'units': unit_rows,
	}


def l3(value):
	uid = str(value.get('unitId') or 'VD')
	now_ms = int(system.date.toMillis(system.date.now()))
	hour_bucket = now_ms // 3600000
	units_cfg = [('VD', 'Vat Dumper', 'Prep'), ('HOP', 'Hopper', 'Prep'), ('HND', 'Handtman', 'Forming'), ('LDR', 'Loaders', 'Forming'), ('RSM', 'Roll Stock', 'Packaging'), ('ST', 'Shrink Tunnel', 'Packaging'), ('LS', 'Lazy Susan', 'Packaging')]

	def synth(key, lo, hi):
		seed = abs(hash(str(key) + str(hour_bucket))) % 10007
		return lo + (float(seed % 1000) / 1000.0) * (hi - lo)

	uname = uid
	uz = 'Prep'
	for cfg_id, cfg_name, cfg_zone in units_cfg:
		if str(cfg_id) == uid:
			uname = cfg_name
			uz = cfg_zone
			break

	st_roll = synth(uid+'_run', 0, 1)
	status = 'Running' if st_roll > 0.12 else ('Fault' if st_roll < 0.04 else 'Idle')
	rate = round(synth(uid+'_rate', 80, 145), 0)
	oee = round(synth(uid+'_oee', 68, 96), 1)
	alarms = int(round(synth(uid+'_alm', 0, 3), 0))
	reject = round(synth(uid+'_reject', 0.5, 3.2), 2)
	run_hrs = round(synth(uid+'_runhrs', 4.5, 11.5), 1)

	trend = []
	for i in range(12):
		seed = abs(hash(uid+'_ut' + str(i) + str(hour_bucket))) % 100
		trend.append(round(rate * (0.88 + 0.2 * (float(seed) / 100.0)), 0))

	# Memory KPI tags (l3_live_struct): Rate (also the trend's 'Now' point), OEE, Reject, Status
	def lv(k):
		try:
			v = (value or {}).get(k)
			return None if v is None else float(v)
		except:
			return None
	if lv('U_Rate') is not None:
		rate = round(lv('U_Rate'), 0)
		trend[-1] = rate
	if lv('U_OEE') is not None:
		oee = round(lv('U_OEE'), 1)
	if lv('U_Reject') is not None:
		reject = round(lv('U_Reject'), 2)
	if lv('U_Status') is not None:
		status = {1: 'Running', 3: 'Fault', 5: 'Idle'}.get(int(lv('U_Status')), 'Idle')

	return {
		'unitId': uid,
		'unitName': uname,
		'zone': uz,
		'runStatus': status,
		'rate': rate,
		'oee': oee,
		'alarms': alarms,
		'rejectPct': reject,
		'runHours': run_hrs,
		'unitTrend': trend,
		'unitTrendLabels': ['-11h','-10h','-9h','-8h','-7h','-6h','-5h','-4h','-3h','-2h','-1h','Now'],
	}
