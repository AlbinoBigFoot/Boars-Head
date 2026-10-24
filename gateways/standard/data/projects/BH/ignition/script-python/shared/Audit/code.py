"""OPS Audit helpers for Perspective writable values.

Central write path for AnalogValue / Control Numeric (and later any
writable view field). Records into the OpsAudit profile table
ops_audit_events with every configured column populated.
"""

OPS_AUDIT_PROFILE = "OpsAudit"
REBUILD_TAG = "[default]_Config/Rebuild"   # shared.Overview tag-change trigger

import threading
import time

_writeLock = threading.Lock()
_recentWrites = {}
_DEDUPE_MS = 1000


def _value_key(value):
	if value is None:
		return "None"
	if isinstance(value, bool):
		return "B:%s" % value
	try:
		return "N:%s" % float(value)
	except Exception:
		return "S:%s" % value


def _status_code(quality):
	try:
		return int(quality.getCode())
	except Exception:
		try:
			return int(quality)
		except Exception:
			return 0


def valuesEqual(a, b):
	"""True when two tag values should be treated as the same (no write / no audit)."""
	if a is None and b is None:
		return True
	if a is None or b is None:
		return False
	if isinstance(a, bool) or isinstance(b, bool):
		try:
			return bool(a) == bool(b)
		except Exception:
			return False
	try:
		return float(a) == float(b)
	except Exception:
		return str(a) == str(b)


def _describe(tagPath, value):
	try:
		return shared.Enums.describe(tagPath, value)
	except Exception:
		return "%s" % (value,)


def _target_from_tag_path(tagPath):
	"""Build a short target label from a tag path, e.g. EV-01 Temp SP."""
	path = str(tagPath or "").strip()
	if not path:
		return ""
	# Strip [provider] prefix
	if path.startswith("["):
		close = path.find("]")
		if close >= 0:
			path = path[close + 1 :]
	parts = [p for p in path.split("/") if p]
	if not parts:
		return path
	# Prefer device + folder + leaf (EV-01 Temp SP)
	if len(parts) >= 3:
		return " ".join(parts[-3:])
	return " ".join(parts)


def _sessionMayWrite(tagPath):
	"""security-tiers: server-side write gate for Perspective sessions (gateway scripts pass).

	Writes need Faceplates/Operate; Out Of Service (<device>.Enabled) needs OutOfService/Set. Ticket Logger
	integration settings (_Config/Integrations) are gated by session.custom.IntegrationAccess at the caller.
	"""
	p = str(tagPath or '')
	if '_Config/Integrations/' in p:
		return True
	if p.endswith('.Enabled'):
		# oos-log: Out Of Service only through shared.OutOfService (required memo, Out Of Service log, audit);
		# a session may not flip <device>.Enabled directly (the old confirmApplyWrite path). Gateway scripts pass.
		if shared.Security._currentSession() is not None:
			system.util.getLogger('shared.Audit').info('Refused direct %s write - use shared.OutOfService' % p)
			return False
		return True
	# device-perms: Faceplates/Operate AND the device-type row (Pump/Command, Evaporator/Setpoint, ...)
	return shared.Security.requireWrite(p)


def _plcWriteBlocked(tagPath):
	"""plc-write-lock: True when shared.PlcWriteLock refuses the write (an error blocks only paths naming RCP1)."""
	try:
		return not shared.PlcWriteLock.writeAllowed(tagPath)
	except Exception as e:
		system.util.getLogger('shared.Audit').warn('PlcWriteLock check failed for %s: %s' % (tagPath, e))
		p = str(tagPath or '')
		return '_RCP1_' in p or '[RCP1]' in p


def writeTag(tagPath, value, label=None, viewName=None):
	"""Write a tag and log the change to OpsAudit.

	Parameters
	----------
	tagPath : str
		Full tag path to write.
	value : any
		New value.
	label : str, optional
		Unused for audit target (kept for call-site compatibility /
		confirm dialogs). Target is derived from the tag path.
	viewName : str, optional
		Perspective view path for originating_system context.

	Returns
	-------
	dict
		{ok, oldValue, newValue, quality, statusCode}
	"""
	tagPath = str(tagPath or "").strip()
	if not tagPath:
		raise ValueError("tagPath is required")
	if not _sessionMayWrite(tagPath):
		return {"ok": False, "skipped": True, "denied": True, "oldValue": None, "newValue": value,
			"quality": None, "statusCode": 0}
	# plc-write-lock (.cursor/tasks/plc-write-lock): no HMI write reaches the RCP1 controller (an [RCP1] OPC item,
	# through references too) while PLC writes are locked, or outside the one unlocked scope
	if _plcWriteBlocked(tagPath):
		return {"ok": False, "skipped": True, "denied": True, "plcLocked": True, "oldValue": None,
			"newValue": value, "quality": None, "statusCode": 0}

	# Prefer OPC/Memory source when Digitals leaf is a reference.
	# Do not follow references for UDT params (Instance.almPriority) or alarm props.
	writePath = tagPath
	leaf = tagPath.replace("\\", "/").split("/")[-1]
	if "." not in leaf:
		try:
			cfg = system.tag.getConfiguration(tagPath, False)[0]
			src = cfg.get("sourceTagPath") or cfg.get("sourceTagPath")
			if src:
				writePath = str(src)
		except Exception:
			pass

	old_qv = system.tag.readBlocking([writePath])[0]
	old_value = old_qv.value
	skipped = {
		"ok": True,
		"skipped": True,
		"oldValue": old_value,
		"newValue": value,
		"quality": getattr(old_qv, "quality", None),
		"statusCode": 0,
	}
	if valuesEqual(old_value, value):
		return skipped

	now_ms = int(time.time() * 1000)
	claim_key = writePath
	claim_val = _value_key(value)
	with _writeLock:
		if len(_recentWrites) > 200:
			_recentWrites.clear()
		prev = _recentWrites.get(claim_key)
		if prev and prev[0] == claim_val and (now_ms - prev[1]) < _DEDUPE_MS:
			return skipped
		_recentWrites[claim_key] = (claim_val, now_ms)

	qualities = system.tag.writeBlocking([writePath], [value])
	quality = qualities[0] if qualities else None
	ok = False
	try:
		ok = bool(quality.isGood())
	except Exception:
		ok = str(quality) in ("Good", "192")

	after_qv = system.tag.readBlocking([writePath])[0]
	after_value = after_qv.value
	if (not ok) or valuesEqual(after_value, old_value):
		return {
			"ok": ok,
			"skipped": True,
			"oldValue": old_value,
			"newValue": after_value,
			"quality": quality,
			"statusCode": _status_code(quality) if quality is not None else 0,
		}

	status = _status_code(quality) if quality is not None else 0
	leaf = tagPath.split("/")[-1]
	target = _target_from_tag_path(tagPath) or (label if label not in (None, "") else tagPath)
	# enum-backed members log words: 'Time Of Day (0) -> Runtime (2)' (shared.Enums); others / any error: raw values
	action_value = "%s -> %s" % (_describe(tagPath, old_value), _describe(tagPath, after_value))

	origin = ["tagPath", tagPath, "tagName", leaf]
	if viewName:
		origin.extend(["view", str(viewName)])

	try:
		system.util.audit(
			action="tag write",
			actionTarget=str(target),
			actionValue=str(action_value),
			auditProfile=OPS_AUDIT_PROFILE,
			originatingSystem=origin,
			originatingContext=4,
			statusCode=status,
		)
	except Exception as ex:
		system.util.getLogger("shared.Audit").warn(
			"OpsAudit write failed for %s: %s" % (tagPath, ex)
		)

	# Out Of Service / Return To Service flips a device instance's Enabled: rebuild the Overview tables (and the
	# auto-built nav) right away so the device drops out / comes back without Designer (user 2026-10-01)
	if tagPath.endswith(".Enabled"):
		try:
			system.tag.writeBlocking([REBUILD_TAG], [True])
		except Exception as ex:
			system.util.getLogger("shared.Audit").warn("Rebuild trigger failed after %s: %s" % (tagPath, ex))

	return {
		"ok": ok,
		"skipped": False,
		"oldValue": old_value,
		"newValue": after_value,
		"quality": quality,
		"statusCode": status,
	}


def logEvent(action, actionTarget, actionValue, tagPath=None, viewName=None, statusCode=0):
	"""Record an operator action in OpsAudit without writing a tag.

	Used for alarm config (system.tag.configure) and ack/reset (multi-tag pulse).
	"""
	target = actionTarget
	if not target and tagPath:
		target = _target_from_tag_path(tagPath) or tagPath
	now_ms = int(time.time() * 1000)
	claim_key = "evt:%s|%s|%s" % (action, target, actionValue)
	with _writeLock:
		if len(_recentWrites) > 200:
			_recentWrites.clear()
		prev = _recentWrites.get(claim_key)
		if prev and (now_ms - prev[1]) < _DEDUPE_MS:
			return
		_recentWrites[claim_key] = ("1", now_ms)
	origin = []
	path = str(tagPath or "").strip()
	if path:
		origin.extend(["tagPath", path, "tagName", path.split("/")[-1]])
	if viewName:
		origin.extend(["view", str(viewName)])
	if not origin:
		origin = ["script", "shared.Audit"]
	try:
		system.util.audit(
			action=str(action or "event"),
			actionTarget=str(target or ""),
			actionValue="" if actionValue is None else str(actionValue),
			auditProfile=OPS_AUDIT_PROFILE,
			originatingSystem=origin,
			originatingContext=4,
			statusCode=int(statusCode or 0),
		)
	except Exception as ex:
		system.util.getLogger("shared.Audit").warn(
			"OpsAudit logEvent failed for %s: %s" % (target, ex)
		)


# Call-site aliases used by some Perspective views
writeTag = writeTag
valuesEqual = valuesEqual
logEvent = logEvent
