# List alarm-configured leaves under a device for Faceplate Alarm Configuration.
# Prefer explicit Alm_*/Value candidates — recursive browse often skips nested Digitals.

logger = system.util.getLogger("shared.AlarmConfig")

_EXPLICIT_ALMS = (
	"Alm_IOFault",
	"Alm_FullStall",
	"Alm_TransitStall",
	"Alm_IntlkTrip",
	"Alm_FailToStart",
	"Alm",
	"Failed",
	"Comm",
	"Cutout",
)

_ALM_LABELS = {
	"Alm_IOFault": "I/O Fault",
	"Alm_FullStall": "Full Stall",
	"Alm_TransitStall": "Transit Stall",
	"Alm_IntlkTrip": "Interlock Trip",
	"Alm_FailToStart": "Fail to Start",
	"Failed": "Failed",
	"Comm": "Communications",
	"Cutout": "Cutout",
	"Alm": "Alarm",
}

_GENERIC_ALARM_NAMES = set(["Alarm", "Value", "Alm", ""])

_SETPOINT_MODES = set([
	"AboveSetpoint", "BelowSetpoint", "BetweenSetpoints", "OutsideSetpoints",
	"AboveOrEqualSetpoint", "BelowOrEqualSetpoint",
])
_DIGITAL_MODES = set([
	"Equality", "Inequality", "AnyChange", "Bit", "OnChange",
	"WhenTrue", "WhenFalse",
])


def _parseHidden(text):
	hidden_set = set()
	try:
		t = str(text or "")
		if t:
			t = t.replace(";", ",")
			for item in t.split(","):
				item = item.strip()
				if item:
					hidden_set.add(item)
	except Exception:
		pass
	return hidden_set


def _isHidden(fullPath, hidden_set):
	if not hidden_set:
		return False
	stripped = fullPath.split("]", 1)[-1] if "]" in fullPath else fullPath
	norm = stripped.replace(chr(92), "/")
	if fullPath in hidden_set or stripped in hidden_set or norm in hidden_set:
		return True
	norm_slash = "/" + norm.strip("/") + "/"
	for h in hidden_set:
		hh = str(h).replace(chr(92), "/")
		if hh.endswith("/"):
			seg = hh.strip("/")
			if not seg:
				continue
			if ("/" + seg + "/") in norm_slash:
				return True
			if norm.strip("/") == seg or norm.strip("/").startswith(seg + "/"):
				return True
		else:
			if norm.endswith("/" + hh) or norm.split("/")[-1] == hh:
				return True
	return False


def _isNoise(fullPath):
	parts = [p for p in str(fullPath).replace("\\", "/").split("/") if p]
	for p in parts:
		if p in ("_Alarms", "SummaryInstances"):
			return True
	return False


def _modeName(mode):
	if mode is None:
		return "Equality"
	try:
		if hasattr(mode, "name"):
			return str(mode.name())
	except Exception:
		pass
	s = str(mode)
	if "." in s:
		s = s.split(".")[-1]
	return s or "Equality"


def _dataTypeName(dt):
	if dt is None:
		return ""
	try:
		if hasattr(dt, "name"):
			return str(dt.name())
	except Exception:
		pass
	return str(dt)


def _browseCandidates(root_path):
	"""Return candidate tag paths under root (browse + explicit Alm_* leaves)."""
	candidates = []
	seen = set()

	def add(path):
		p = str(path or "").strip()
		if not p or p in seen or _isNoise(p):
			return
		seen.add(p)
		candidates.append(p)

	try:
		raw = system.tag.browse(root_path, {"recursive": True})
		try:
			rows = raw.getResults()
		except Exception:
			rows = list(raw) if raw is not None else []
		for tag in rows or []:
			try:
				tt = str(tag["tagType"])
			except Exception:
				continue
			# Only atomic leaves from browse — UDT instances are covered by explicit Alm_* paths
			if tt != "AtomicTag":
				continue
			try:
				add(tag["fullPath"])
			except Exception:
				pass
	except Exception as e:
		logger.warn("browse failed for %s: %s" % (root_path, str(e)))

	add(root_path)
	for alm in _EXPLICIT_ALMS:
		add(root_path + "/" + alm + "/Value")
		add(root_path + "/" + alm)
	return candidates


def _alarmsOn(path):
	"""Return (resolvedPath, nodeCfg, alarmsList) or (None, None, None).

	Only real getConfiguration alarm definitions — do not invent rows from
	AlarmEvalEnabled (that property is True for many non-alarmed leaves).
	"""
	full_path = str(path)
	try:
		cfg = system.tag.getConfiguration(full_path, False)
	except Exception:
		return None, None, None
	if not cfg or len(cfg) == 0:
		return None, None, None
	node = cfg[0]
	if node.get("enabled", True) is False:
		return None, None, None
	alarms = node.get("alarms")
	if not alarms and not full_path.endswith("/Value"):
		try:
			cfgv = system.tag.getConfiguration(full_path + "/Value", False)
			if cfgv and (cfgv[0].get("alarms") or []):
				full_path = full_path + "/Value"
				node = cfgv[0]
				alarms = node.get("alarms")
		except Exception:
			pass
	if not alarms:
		return None, None, None
	return full_path, node, alarms


def _folderName(full_path):
	parts = [p for p in str(full_path).replace("\\", "/").split("/") if p]
	if parts and parts[-1] == "Value" and len(parts) >= 2:
		name = parts[-2]
	elif parts:
		name = parts[-1]
	else:
		name = str(full_path)
	if "]" in name:
		name = name.split("]", 1)[-1]
	return name


def _humanize(token):
	key = str(token or "").strip()
	if key in _ALM_LABELS:
		return _ALM_LABELS[key]
	s = key
	if s.startswith("Alm_"):
		s = s[4:]
	out = []
	for i, ch in enumerate(s):
		if i and ch.isupper() and (s[i - 1].islower() or (i + 1 < len(s) and s[i + 1].islower())):
			out.append(" ")
		if ch == "_":
			out.append(" ")
		else:
			out.append(ch)
	pretty = "".join(out).replace("  ", " ").strip()
	pretty = pretty.replace("IO ", "I/O ").replace("Intlk ", "Interlock ")
	return pretty or key


def _labelFor(full_path, node, root_path):
	label_base = ""
	try:
		md = node.get("metadata") or {}
		label_base = str(md.get("shortDescription") or "").strip()
	except Exception:
		label_base = ""
	if not label_base:
		try:
			parent = full_path.rsplit("/", 1)[0]
			pcfg = system.tag.getConfiguration(parent, False)
			if pcfg:
				pmd = pcfg[0].get("metadata") or {}
				label_base = str(pmd.get("shortDescription") or "").strip()
		except Exception:
			pass
	if not label_base:
		label_base = _humanize(_folderName(full_path))
	else:
		label_base = _humanize(label_base)
	return label_base


def listAlarms(tagPath, hiddenTags=""):
	"""
	Return rows for Alarm Configuration flex-repeater:
	[{tagPath, alarmName, label, isDigital, hasSetpoint, mode}, ...]
	"""
	result = []
	root_path = str(tagPath or "").strip()
	if not root_path:
		return result

	hidden_set = _parseHidden(hiddenTags)
	seen_keys = set()

	for cand in _browseCandidates(root_path):
		if _isHidden(cand, hidden_set):
			continue
		full_path, node, alarms = _alarmsOn(cand)
		if not full_path or not alarms:
			continue
		if _isHidden(full_path, hidden_set):
			continue

		dt = _dataTypeName(node.get("dataType"))
		label_base = _labelFor(full_path, node, root_path)

		for alarm in alarms:
			try:
				alarm_name = str(alarm.get("name") or "Alarm")
			except Exception:
				alarm_name = "Alarm"
			mode = _modeName(alarm.get("mode") if hasattr(alarm, "get") else None)
			try:
				if not hasattr(alarm, "get") and hasattr(alarm, "getName"):
					alarm_name = str(alarm.getName() or "Alarm")
			except Exception:
				pass

			is_digital = (mode in _DIGITAL_MODES) or (dt in ("Boolean", "Bool", "Int1"))
			has_setpoint = mode in _SETPOINT_MODES
			if not has_setpoint and not is_digital and mode not in _DIGITAL_MODES:
				has_setpoint = True
				is_digital = False

			folder = _folderName(full_path)
			try:
				notes = str(alarm.get("notes") or "").strip()
			except Exception:
				notes = ""
			if not notes and folder.startswith("Alm_"):
				notes = folder

			label = label_base
			if alarm_name and alarm_name not in _GENERIC_ALARM_NAMES:
				# Alarm object already has a plain-English name — use it as the title.
				label = _humanize(alarm_name)
			elif folder.startswith("Alm_"):
				label = _humanize(folder)

			key = full_path + "|" + alarm_name
			if key in seen_keys:
				continue
			seen_keys.add(key)
			inst = full_path
			if inst.endswith("/Value"):
				inst = inst[:-6]
			result.append({
				"tagPath": full_path,
				"instancePath": inst,
				"alarmName": alarm_name,
				"label": label,
				"notes": notes,
				"isDigital": bool(is_digital and not has_setpoint),
				"hasSetpoint": bool(has_setpoint),
				"mode": mode,
			})

	result.sort(key=lambda x: (str(x.get("label") or ""), str(x.get("alarmName") or "")))
	logger.info("listAlarms(%s) -> %d" % (root_path, len(result)))
	return result


def applyOverride(tagPath, alarmName, priority=None, mode=None, viewName=None):
	"""Merge priority/mode onto the instance alarm (UDT instance override).

	Boolean alarms use WhenTrue / WhenFalse (not Equality).
	Successful changes are written to OpsAudit.
	"""
	tag_path = str(tagPath or "").strip()
	alarm_name = str(alarmName or "").strip()
	if not tag_path or not alarm_name:
		raise ValueError("tagPath and alarmName are required")

	parent, _, leaf = tag_path.rpartition("/")
	if not parent or not leaf:
		raise ValueError("invalid tagPath: %s" % tag_path)

	old_priority = None
	old_mode = None
	try:
		cfg = system.tag.getConfiguration(tag_path, False)[0]
		existing = cfg.get("alarms") or []
		if existing:
			names = []
			for a in existing:
				try:
					names.append(str(a.get("name") or ""))
				except Exception:
					pass
			if alarm_name not in names:
				# Inherited UDT alarm name may differ from the faceplate label.
				if len(names) == 1 and names[0]:
					alarm_name = names[0]
			for a in existing:
				try:
					if str(a.get("name") or "") == alarm_name:
						old_priority = a.get("priority")
						old_mode = a.get("mode")
						break
				except Exception:
					pass
	except Exception as e:
		logger.warn("applyOverride getConfiguration %s: %s" % (tag_path, e))

	alarm = {"name": alarm_name}
	if priority not in (None, ""):
		alarm["priority"] = str(priority)
	if mode not in (None, ""):
		m = str(mode)
		if m in ("1", "1.0", "True", "true", "WhenTrue"):
			m = "WhenTrue"
		elif m in ("0", "0.0", "False", "false", "WhenFalse"):
			m = "WhenFalse"
		alarm["mode"] = m

	payload = {"name": leaf, "alarms": [alarm]}
	q = system.tag.configure(parent, [payload], "m")
	ok = True
	try:
		if q:
			item = q[0] if hasattr(q, "__getitem__") else q
			if hasattr(item, "isGood"):
				ok = bool(item.isGood())
			else:
				s = str(item)
				if s and s.upper().find("GOOD") < 0 and s not in ("192", "None"):
					ok = False
					logger.warn("applyOverride quality %s %s" % (tag_path, s))
	except Exception:
		pass
	logger.info("applyOverride %s %s %s ok=%s" % (tag_path, alarm_name, alarm, ok))
	if ok:
		try:
			parts = [p for p in tag_path.replace("\\", "/").split("/") if p]
			base = " ".join(parts[-3:]) if len(parts) >= 2 else tag_path
			if priority not in (None, ""):
				shared.Audit.logEvent(
					"alarm config",
					"%s %s priority" % (base, alarm_name),
					"%s -> %s" % (old_priority if old_priority not in (None, "") else "—", alarm.get("priority")),
					tagPath=tag_path,
					viewName=viewName,
				)
			if mode not in (None, ""):
				shared.Audit.logEvent(
					"alarm config",
					"%s %s trigger" % (base, alarm_name),
					"%s -> %s" % (old_mode if old_mode not in (None, "") else "—", alarm.get("mode")),
					tagPath=tag_path,
					viewName=viewName,
				)
		except Exception as ex:
			logger.warn("applyOverride audit %s: %s" % (tag_path, ex))
	return {"ok": ok, "tagPath": tag_path, "alarmName": alarm_name, "alarm": alarm}
