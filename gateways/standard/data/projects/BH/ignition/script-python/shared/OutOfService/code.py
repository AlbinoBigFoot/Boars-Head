# HMI Out Of Service log (2026-10-10, .cursor/tasks/oos-log - this file is the source of the BH project library
# shared.OutOfService; the builder copies it to ignition/script-python/shared/OutOfService/code.py). Docs:
# docs/out-of-service.md.
#
# Every Take Out Of Service / Return To Service / comment goes through here, on the gateway:
#   permission  shared.Security (Roles & Permissions OutOfService/Set, OutOfService/Comment) from the calling session
#   memo        at least MIN_TEXT characters after trimming (the dialog checks too; this is the real check)
#   who / when  session.props.auth.user + the gateway clock (never client-supplied params)
#   log         dbo.oos_record / dbo.oos_comment (sql/out_of_service_log.sql) through named queries OutOfService/*
#   tag         <device>.Enabled (the UDT instance's enabled property = the out-of-service flag)
#   audit       shared.Audit.logEvent -> OpsAudit (ops_audit_events) with old/new value, reason and memo
# Order: the DB row is written inside a transaction, then the tag; the transaction commits only when the tag write
# read back as written, otherwise it rolls back (and a written tag is put back), so the log and the tag agree.

DB = "ignition"
NQ = "OutOfService/"
MIN_TEXT = 10
MAX_TEXT = 2000
REASONS = ["Maintenance", "Repair", "Awaiting Parts", "Seasonal", "Safety Lockout", "Other"]
COMMENT_STATUSES = ["In Progress", "Awaiting Parts", "On Hold", "Ready To Return"]
OPEN_STATUS = "Out Of Service"
RETURNED_STATUS = "Returned"
BACKFILL_USER = "system"
BACKFILL_NAME = "Unknown (Before Logging)"
BACKFILL_MEMO = "Taken out of service before the Out Of Service log existed - no memo was recorded."
POPUP_ID = "oosDialog"
POPUP_VIEW = "01_Popups/00_Faceplates/Alerts/OutOfService"
LOG_ROUTE = "/operations/out-of-service"
_log = system.util.getLogger("shared.OutOfService")


class _Refused(Exception):
	"""A request the user can fix (shown in the dialog), not a fault."""
	pass


def _text(v):
	if v is None:
		return u""
	try:
		return unicode(v).strip()
	except Exception:
		return u""


def _user(session):
	"""(username, display name) of the session's logged-in user; ('', '') when not logged in."""
	try:
		u = session.props.auth.user
	except Exception:
		return ("", "")
	name = first = last = u""
	try:
		name = _text(u.userName)
	except Exception:
		pass
	try:
		first = _text(u.firstName)
		last = _text(u.lastName)
	except Exception:
		pass
	display = (first + u" " + last).strip() or name
	return (name, display)


def _device(tagPath):
	"""{tagPath, name, type, site, area} for a device UDT instance (typeId Devices/*), else None."""
	tp = _text(tagPath)
	if not tp:
		return None
	try:
		cfg = system.tag.getConfiguration(tp, False)[0]
		kind = str(cfg.get("tagType") or "")
		typeId = str(cfg.get("typeId") or "")
	except Exception:
		return None
	if kind != "UdtInstance" or not typeId.startswith("Devices/"):
		return None
	if not tp.startswith("["):
		tp = "[default]" + tp
	parts = [p for p in tp.split("]", 1)[-1].split("/") if p]
	site = area = u""
	if len(parts) >= 3 and parts[0] == "Boars_Head":
		site = parts[1]
		area = parts[2] if len(parts) >= 4 else u""
	elif len(parts) >= 2:
		area = parts[-2]
	return {"tagPath": tp, "name": parts[-1], "type": typeId.split("/")[-1], "site": site, "area": area}


def _enabled(tp):
	qv = system.tag.readBlocking([tp + ".Enabled"])[0]
	return True if qv.value is None else bool(qv.value)


def _setEnabled(tp, value):
	"""Write <device>.Enabled and read it back; raises when it did not take."""
	q = system.tag.writeBlocking([tp + ".Enabled"], [bool(value)])[0]
	good = False
	try:
		good = bool(q.isGood())
	except Exception:
		good = str(q) in ("Good", "192")
	if not good or _enabled(tp) != bool(value):
		raise Exception("write %s.Enabled = %s failed (%s)" % (tp, value, q))


def _query(name, params, tx=None):
	if tx is None:
		return system.db.runNamedQuery(NQ + name, params)
	return system.db.runNamedQuery(NQ + name, params, tx)


def _openRecordId(tp, tx=None):
	ds = _query("OpenRecordId", {"tagPath": tp}, tx)
	return int(ds.getValueAt(0, 0)) if ds is not None and ds.getRowCount() else None


def _insertRecord(dev, user, display, now, reason, memo, backfill, tx):
	ds = _query("InsertRecord", {
		"tagPath": dev["tagPath"], "deviceName": dev["name"], "deviceType": dev["type"], "site": dev["site"],
		"area": dev["area"], "takenBy": user, "takenName": display, "takenAt": now, "reason": reason,
		"memo": memo, "status": OPEN_STATUS, "isBackfill": 1 if backfill else 0}, tx)
	return int(ds.getValueAt(0, 0))


def _closeRecord(recordId, user, display, now, memo, tx):
	n = _query("CloseRecord", {"id": recordId, "returnedBy": user, "returnedName": display, "returnedAt": now,
		"returnMemo": memo, "status": RETURNED_STATUS}, tx)
	if not n:
		raise Exception("record %s was not open" % recordId)


def _target(tp):
	try:
		return shared.Audit._target_from_tag_path(tp + ".Enabled")
	except Exception:
		return tp + ".Enabled"


def _audit(action, tp, value, viewName):
	try:
		shared.Audit.logEvent(action, _target(tp), value, tagPath=tp + ".Enabled", viewName=viewName)
	except Exception as e:
		_log.warn("OpsAudit %s failed for %s: %s" % (action, tp, e))


def _notify(payload):
	"""Refresh the log page / header badge in this session (other sessions poll)."""
	try:
		system.perspective.sendMessage("oosChanged", payload=payload, scope="session")
	except Exception:
		pass


def _rebuild():
	"""Device tables drop / regain the device right away (shared.Overview via _Config/Rebuild)."""
	try:
		system.tag.writeBlocking([shared.Audit.REBUILD_TAG], [True])
	except Exception as e:
		_log.warn("Rebuild trigger failed: %s" % e)


def _checkText(text, what):
	if len(text) < MIN_TEXT:
		raise _Refused("%s Must Be At Least %d Characters" % (what, MIN_TEXT))
	if len(text) > MAX_TEXT:
		raise _Refused("%s Must Be %d Characters Or Fewer" % (what, MAX_TEXT))


def openDialog(tagPath, viewName="", takeOut=None):
	"""Open the memo dialog for a device (right-click menu, OOS log page). takeOut None = from the device's state."""
	dev = _device(tagPath)
	if dev is None:
		return False
	if takeOut is None:
		takeOut = _enabled(dev["tagPath"])
	system.perspective.openPopup(
		id=POPUP_ID,
		view=POPUP_VIEW,
		params={"tagPath": dev["tagPath"], "deviceName": dev["name"], "takeOut": bool(takeOut),
			"viewName": str(viewName or "")},
		position={"width": 460, "height": 470},
		draggable=True,
		showCloseIcon=False,
		modal=True,
		overlayDismiss=False,
	)
	return True


def setOutOfService(session, tagPath, takeOut, reason, memo, viewName=""):
	"""Take a device out of service (takeOut True) or return it, with the memo. Returns {ok, error, recordId}.

	session is the calling script's self.session (gateway side). Everything is re-checked here: permission
	OutOfService/Set, memo length, reason, the device, its current state."""
	takeOut = bool(takeOut)
	memo = _text(memo)
	reason = _text(reason)
	tx = None
	wrote = False
	dev = None
	enabled = None
	try:
		if session is None or not shared.Security.require("OutOfService", "Set", tagPath, session):
			raise _Refused("Permission Denied - Out Of Service Requires The OutOfService/Set Permission")
		_checkText(memo, "Memo")
		if takeOut and reason not in REASONS:
			raise _Refused("Select A Reason")
		user, display = _user(session)
		if not user:
			raise _Refused("Log In To Change Out Of Service")
		dev = _device(tagPath)
		if dev is None:
			raise _Refused("Not A Device: %s" % tagPath)
		tp = dev["tagPath"]
		enabled = _enabled(tp)
		now = system.date.now()
		tx = system.db.beginTransaction(DB, system.db.READ_COMMITTED, 15000)
		openId = _openRecordId(tp, tx)
		if takeOut:
			if openId is not None and not enabled:
				raise _Refused("%s Is Already Out Of Service (Record %d)" % (dev["name"], openId))
			if openId is not None:
				# returned outside the HMI (Designer) while its record stayed open: close that record first
				_closeRecord(openId, BACKFILL_USER, "Returned Outside The HMI", now,
					"Device was found back in service when it was taken out of service again.", tx)
			recordId = _insertRecord(dev, user, display, now, reason, memo, False, tx)
			if enabled:
				_setEnabled(tp, False)
				wrote = True
		else:
			if openId is None:
				if enabled:
					raise _Refused("%s Is Already In Service" % dev["name"])
				# out of service with no record (before logging existed / outside the HMI): record it, then close it
				openId = _insertRecord(dev, BACKFILL_USER, BACKFILL_NAME, now, "Other", BACKFILL_MEMO, True, tx)
			_closeRecord(openId, user, display, now, memo, tx)
			recordId = openId
			if not enabled:
				_setEnabled(tp, True)
				wrote = True
		system.db.commitTransaction(tx)
	except _Refused as e:
		if tx is not None:
			system.db.rollbackTransaction(tx)
		return {"ok": False, "error": unicode(e), "recordId": None}
	except Exception as e:
		if tx is not None:
			try:
				system.db.rollbackTransaction(tx)
			except Exception:
				pass
		if wrote:
			try:
				_setEnabled(dev["tagPath"], enabled)
			except Exception as e2:
				_log.error("Could not restore %s.Enabled = %s after a failed log write: %s" % (dev["tagPath"], enabled, e2))
		_log.error("Out Of Service %s failed for %s: %s" % ("take" if takeOut else "return", tagPath, e))
		return {"ok": False, "error": "Not Saved - The Out Of Service Log Could Not Be Written (Device Unchanged)",
			"recordId": None}
	finally:
		if tx is not None:
			try:
				system.db.closeTransaction(tx)
			except Exception:
				pass
	tp = dev["tagPath"]
	after = (not takeOut) if wrote else enabled
	if takeOut:
		value = u"Enabled %s -> %s | Reason: %s | Memo: %s | Record %d" % (enabled, after, reason, memo, recordId)
	else:
		value = u"Enabled %s -> %s | Memo: %s | Record %d" % (enabled, after, memo, recordId)
	_audit("out of service" if takeOut else "return to service", tp, value, viewName)
	if wrote:
		_rebuild()
	_notify({"tagPath": tp, "recordId": recordId})
	return {"ok": True, "error": "", "recordId": recordId}


def historyPage(tagPath):
	"""Log page URL filtered to one device: route /operations/out-of-service/:device, device = the tag path without
	the provider with '/' -> '~' (the log view turns it back)."""
	tp = _text(tagPath)
	if tp.startswith("["):
		tp = tp.split("]", 1)[-1]
	return LOG_ROUTE + "/" + tp.strip("/").replace("/", "~")


def openHistory(tagPath):
	"""Out Of Service History (device right-click menu, log page Device History): the log page for one device."""
	if _device(tagPath) is None:
		return False
	system.perspective.navigate(page=historyPage(tagPath))
	return True


def addComment(session, recordId, status, comment):
	"""Comment (and optional status change) on a record. OutOfService/Comment. Returned records take comments but no
	status change. Returns {ok, error}."""
	comment = _text(comment)
	status = _text(status)
	tx = None
	try:
		if session is None or not shared.Security.require("OutOfService", "Comment", "record %s" % recordId, session):
			raise _Refused("Permission Denied - Comments Require The OutOfService/Comment Permission")
		_checkText(comment, "Comment")
		if status and status not in COMMENT_STATUSES:
			raise _Refused("Unknown Status: %s" % status)
		user, display = _user(session)
		if not user:
			raise _Refused("Log In To Comment")
		try:
			recordId = int(recordId)
		except Exception:
			raise _Refused("Select A Record")
		ds = _query("Record", {"allowed": 1, "id": recordId, "now": system.date.now(), "refresh": 0})
		if ds is None or not ds.getRowCount():
			raise _Refused("Record %s Not Found" % recordId)
		# returned records take comments too (equipment history); a status change needs an open record
		if status and ds.getValueAt(0, "returned_at") is not None:
			raise _Refused("Record %d Is Returned To Service - Status Changes Need An Open Record" % recordId)
		tp = str(ds.getValueAt(0, "tag_path"))
		now = system.date.now()
		tx = system.db.beginTransaction(DB, system.db.READ_COMMITTED, 15000)
		_query("InsertComment", {"recordId": recordId, "username": user, "displayName": display, "createdAt": now,
			"status": status or None, "comment": comment}, tx)
		if status:
			_query("SetStatus", {"id": recordId, "status": status}, tx)
		system.db.commitTransaction(tx)
	except _Refused as e:
		if tx is not None:
			system.db.rollbackTransaction(tx)
		return {"ok": False, "error": unicode(e)}
	except Exception as e:
		if tx is not None:
			try:
				system.db.rollbackTransaction(tx)
			except Exception:
				pass
		_log.error("Out Of Service comment failed for record %s: %s" % (recordId, e))
		return {"ok": False, "error": "Not Saved - The Comment Could Not Be Written"}
	finally:
		if tx is not None:
			try:
				system.db.closeTransaction(tx)
			except Exception:
				pass
	value = u"Record %d | Status: %s | Comment: %s" % (recordId, status or "No Change", comment)
	_audit("out of service comment", tp, value, "00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog")
	_notify({"tagPath": tp, "recordId": recordId})
	return {"ok": True, "error": ""}
