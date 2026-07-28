"""OPS Audit helpers for Perspective writable values.

Central write path for AnalogValue / Control Numeric (and later any
writable view field). Records into the OpsAudit profile table
ops_audit_events with every configured column populated.
"""

OPS_AUDIT_PROFILE = "OpsAudit"


def _status_code(quality):
	try:
		return int(quality.getCode())
	except Exception:
		try:
			return int(quality)
		except Exception:
			return 0


def writeTag(tagPath, value, label=None, viewName=None):
	"""Write a tag and log the change to OpsAudit.

	Parameters
	----------
	tagPath : str
		Full tag path to write.
	value : any
		New value.
	label : str, optional
		Human label for the audit action_target (defaults to tag leaf).
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

	old_qv = system.tag.readBlocking([tagPath])[0]
	old_value = old_qv.value
	qualities = system.tag.writeBlocking([tagPath], [value])
	quality = qualities[0] if qualities else None
	ok = False
	try:
		ok = bool(quality.isGood())
	except Exception:
		ok = str(quality) in ("Good", "192")

	status = _status_code(quality) if quality is not None else 0
	leaf = tagPath.split("/")[-1]
	target = label if label not in (None, "") else tagPath
	action_value = "%s -> %s" % (old_value, value)

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

	return {
		"ok": ok,
		"oldValue": old_value,
		"newValue": value,
		"quality": quality,
		"statusCode": status,
	}
