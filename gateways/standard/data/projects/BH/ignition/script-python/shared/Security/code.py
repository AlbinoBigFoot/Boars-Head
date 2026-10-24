# Role lists from [default]_Config/Security and the Roles & Permissions matrix [default]_Config/RolesPermissions
# (no hard-coded role names - a renamed role only needs the tag / matrix column changed).
# Role lists are comma-separated, matched case-insensitively. Tiers (2026-10-01, .cursor/tasks/security-tiers):
# what a role may do is its column in the matrix; several roles = the union; FullPermissionRoles hold everything.

BASE = "[default]_Config/Security/"
MATRIX = "[default]_Config/RolesPermissions"
_log = system.util.getLogger("shared.Security")
_state = {"ctxWarned": False}


def roleList(csv):
	"""'A, b ,C' -> ['a', 'b', 'c'] (lower-case, blanks dropped)."""
	return [r.strip().lower() for r in str(csv or "").split(",") if r.strip()]


def hasAnyRole(userRoles, csv):
	"""True when any of the user's roles is in the comma-separated list."""
	wanted = set(roleList(csv))
	if not wanted:
		return False
	try:
		held = [str(r).strip().lower() for r in (userRoles or [])]
	except Exception:
		held = []
	return any(r in wanted for r in held)


def roles(name):
	"""Role names (original case) from _Config/Security/<name>."""
	qv = system.tag.readBlocking([BASE + name])[0]
	return [r.strip() for r in str(qv.value or "").split(",") if r.strip()]


def effectiveRoles(userRoles, inheritsCsv):
	"""Held roles (lower-case) plus the roles they inherit from _Config/Security/RoleInherits.

	'Engineering:Maintenance, A:B' = Engineering also gets every Maintenance tick; chains follow (A:B, B:C)."""
	try:
		held = set(str(r).strip().lower() for r in (userRoles or []) if str(r).strip())
	except Exception:
		held = set()
	pairs = []
	for item in str(inheritsCsv or "").split(","):
		a, _, b = item.partition(":")
		if a.strip() and b.strip():
			pairs.append((a.strip().lower(), b.strip().lower()))
	grew = True
	while grew:
		grew = False
		for a, b in pairs:
			if a in held and b not in held:
				held.add(b)
				grew = True
	return held


def restrictedRows(csv):
	"""_Config/Security/RestrictedRows 'TicketLogger/Use:OneShot, A/B:X|Y' -> {'TicketLogger/Use': ['oneshot'], ...}.

	A restricted row is not given to FullPermissionRoles implicitly (only its ticks count) and the Roles &
	Permissions page shows / saves it only for viewers holding one of its roles (device-perms 2026-10-24)."""
	out = {}
	for item in str(csv or "").split(","):
		key, _, who = item.partition(":")
		if key.strip():
			out[key.strip()] = [r.strip().lower() for r in who.split("|") if r.strip()]
	return out


def rowVisible(key, viewerRoles, restrictedCsv):
	"""False when Devices/Actions key is a RestrictedRows row and the viewer holds none of its roles."""
	who = restrictedRows(restrictedCsv).get(str(key))
	if who is None:
		return True
	try:
		held = set(str(r).strip().lower() for r in (viewerRoles or []))
	except Exception:
		held = set()
	return any(r in held for r in who)


def rowRules(viewerRoles, restrictedCsv):
	"""{'restricted': [Devices/Actions keys], 'hidden': [those the viewer may not see]} for the Roles & Permissions page."""
	keys = sorted(restrictedRows(restrictedCsv).keys())
	return {"restricted": keys, "hidden": [k for k in keys if not rowVisible(k, viewerRoles, restrictedCsv)]}


def newRoleDefaults(csv):
	"""_Config/Security/NewRoleDefaults 'TicketLogger/Use, A/B' -> set of Devices/Actions keys a role gets when the
	matrix first sees it (role-wizard 2026-10-24)."""
	return set(k.strip() for k in str(csv or "").split(",") if k.strip())


def permissions(userRoles, matrix, fullCsv, inheritsCsv="", restrictedCsv="", defaultsCsv=""):
	"""{Device: {Action: bool}} for a user holding userRoles, from the RolesPermissions dataset.

	A row is allowed when any held (or inherited, see effectiveRoles) role's column is ticked (union);
	FullPermissionRoles get every row except the RestrictedRows ones (Ticket Logger: ticks only). Role -> column
	matching is case-insensitive. Rows sharing Device/Action are OR-ed. A held role the matrix has no column for
	yet (created in the gateway) holds the NewRoleDefaults rows (role-wizard 2026-10-24; the Roles & Permissions
	page then adds its column with the same ticks, shared.PermissionMatrix.syncRoles)."""
	perms = {}
	if matrix is None:
		return perms
	try:
		names = list(matrix.getColumnNames())
	except Exception:
		return perms
	held = effectiveRoles(userRoles, inheritsCsv)
	full = hasAnyRole(held, fullCsv)
	restricted = restrictedRows(restrictedCsv)
	roleCols = [c for c in names if c not in ("Devices", "Actions", "Description", "Category")]
	cols = [c for c in roleCols if c.strip().lower() in held]
	known = set(c.strip().lower() for c in roleCols)
	defaults = newRoleDefaults(defaultsCsv) if any(r not in known for r in held) else set()
	for i in range(matrix.getRowCount()):
		dev = str(matrix.getValueAt(i, "Devices"))
		act = str(matrix.getValueAt(i, "Actions"))
		key = dev + "/" + act
		ok = (full and key not in restricted) or key in defaults or any(bool(matrix.getValueAt(i, c)) for c in cols)
		perms.setdefault(dev, {})[act] = bool(perms.get(dev, {}).get(act)) or ok
	return perms


def _currentSession():
	"""The Perspective session running this script (component / message / page scripts), else None.

	Perspective's PageModel.PAGE / InternalSession.SESSION thread-locals are empty in component scripts (checked
	2026-10-01, 8.3.7), so in practice the session comes from the calling script's self.session on the stack."""
	errs = []
	try:
		from com.inductiveautomation.perspective.gateway.model import PageModel
		page = PageModel.PAGE.get()
		if page is not None:
			return page.session
		errs.append("PAGE empty")
	except Exception as e:
		errs.append("PAGE: %r" % e)
	try:
		from com.inductiveautomation.perspective.gateway.session import InternalSession
		s = InternalSession.SESSION.get()
		if s is not None:
			return s
		errs.append("SESSION empty")
	except Exception as e:
		errs.append("SESSION: %r" % e)
	# a component / view script up the call stack has self.session (event, message handler, transform)
	try:
		import sys
		f = sys._getframe(1)
		depth = 0
		while f is not None and depth < 30:
			me = f.f_locals.get("self")
			if me is not None:
				try:
					s = me.session
				except Exception:
					s = None
				if s is not None:
					return s
			f = f.f_back
			depth += 1
		errs.append("no self.session on the stack")
	except Exception as e:
		errs.append("stack: %r" % e)
	# gateway scripts (timers, tag events, gateway message handlers) end here - no user, no session
	_state["ctxErr"] = errs
	_log.debug("no Perspective session context: %s" % "; ".join(errs))
	return None


def _rolesOf(session):
	"""Roles of a session (script wrapper self.session or the gateway session object); None when unreadable."""
	try:
		return [str(r) for r in (session.props.auth.user.roles or [])]
	except Exception:
		pass
	try:
		from com.inductiveautomation.perspective.gateway.script import SessionScriptWrapper
		return [str(r) for r in (SessionScriptWrapper(session).props.auth.user.roles or [])]
	except Exception:
		pass
	try:
		user = session.getWebAuthStatus().getUser()
		return [str(r) for r in user.get().getRoles()] if user.isPresent() else []
	except Exception:
		return None


def _userOf(session):
	try:
		return str(session.props.auth.user.userName or "")
	except Exception:
		return ""


def _sessionPerms(session=None):
	"""(session, perms) for the Perspective session running this script; (None, None) outside a session, (s, None)
	when its roles cannot be read (logged once) - callers then allow, the UI gates still apply."""
	s = session if session is not None else _currentSession()
	if s is None:
		return None, None
	held = _rolesOf(s)
	if held is None:
		if not _state["ctxWarned"]:
			_state["ctxWarned"] = True
			_log.warn("Session roles unreadable - server-side permission checks fall back to allow")
		return s, None
	qv = system.tag.readBlocking([MATRIX, BASE + "FullPermissionRoles", BASE + "RoleInherits", BASE + "RestrictedRows",
		BASE + "NewRoleDefaults"])
	return s, permissions(held, qv[0].value, qv[1].value, qv[2].value, qv[3].value, qv[4].value)


def can(device, action, session=None):
	"""Server-side check: may the Perspective session (given, else the one running this script) do Device/Action?

	Outside a Perspective session (gateway timer / tag event scripts, no user) this is True so gateway logic keeps
	working. If the session context cannot be read it logs once and allows (the UI gates still apply)."""
	s, perms = _sessionPerms(session)
	if perms is None:
		return True
	return bool(perms.get(device, {}).get(action, False))


def allowed(session, device, action):
	"""can() for view scripts that hold self.session."""
	return can(device, action, session)


def require(device, action, what="", session=None):
	"""can(), logging the refusal (who, what) when it is denied."""
	if can(device, action, session):
		return True
	s = session if session is not None else _currentSession()
	_log.info("Denied %s/%s for '%s'%s" % (device, action, _userOf(s) if s is not None else "",
		(": " + str(what)) if what else ""))
	return False


# ---------------------------------------------------------------------------------------------- device-type rows
# device-perms (2026-10-24, user decision 16a): a device control needs its general row (Faceplates/Operate,
# Engineering/Edit, AlarmConfiguration/Edit) AND its device-type row (<Device>/<Action>, e.g. Pump/Command).
#   _Config/Security/DeviceTypes        DataSet TypeId -> Device (matrix Devices value), e.g. Devices/Pump -> Pump
#   _Config/Security/DeviceActionRules  DataSet Pattern (regex on the member path below the device) -> Action,
#                                       first match wins, anything else = Setpoint
# A type or action without a matrix row needs only the general row. Setpoint and Configuration stand in for each
# other when a type has only one of them (Pump / Valve: Configuration, Evaporator / Tank: Setpoint).
DEVICE_TYPES = BASE + "DeviceTypes"
DEVICE_ACTION_RULES = BASE + "DeviceActionRules"
STAND_IN = {"Setpoint": "Configuration", "Configuration": "Setpoint"}
_typeCache = {}
_TYPE_TTL_MS = 300000


def _dsRows(ds, *cols):
	out = []
	if ds is None:
		return out
	try:
		for i in range(ds.getRowCount()):
			out.append(tuple(ds.getValueAt(i, c) for c in cols))
	except Exception:
		pass
	return out


def _typeIds(paths):
	"""{path: TypeId or ''} for tag paths (cached 5 min; a TypeId only changes when a device is re-instanced)."""
	now = system.date.toMillis(system.date.now())
	out, todo = {}, []
	for p in paths:
		hit = _typeCache.get(p)
		if hit is not None and now - hit[1] < _TYPE_TTL_MS:
			out[p] = hit[0]
		else:
			todo.append(p)
	if todo:
		if len(_typeCache) > 4000:
			_typeCache.clear()
		qvs = system.tag.readBlocking([p + ".TypeId" for p in todo])
		for p, qv in zip(todo, qvs):
			v = ""
			try:
				if qv.quality.isGood() and qv.value is not None:
					v = str(qv.value)
			except Exception:
				v = ""
			_typeCache[p] = (v, now)
			out[p] = v
	return out


def deviceOf(tagPath):
	"""(devicePath, device): the deepest instance on tagPath (itself or an ancestor) whose UDT TypeId is listed in
	_Config/Security/DeviceTypes, and its matrix Devices value; ('', '') when the path is no device."""
	p = str(tagPath or "").strip().replace(chr(92), "/")
	if not p:
		return "", ""
	prov = ""
	if p.startswith("["):
		prov, _, p = p.partition("]")
		prov += "]"
	parts = [x for x in p.split("/") if x]
	if parts and "." in parts[-1]:
		parts[-1] = parts[-1].split(".")[0]          # x.Enabled -> the tag itself
	cands = [prov + "/".join(parts[:i]) for i in range(len(parts), 1, -1)]
	if not cands:
		return "", ""
	types = dict((str(t), str(d or "")) for t, d in _dsRows(system.tag.readBlocking([DEVICE_TYPES])[0].value,
		"TypeId", "Device"))
	ids = _typeIds(cands)
	for c in cands:
		dev = types.get(ids.get(c, ""))
		if dev:
			return c, dev
	return "", ""


def actionOf(tagPath, devicePath):
	"""Matrix action for a write to tagPath below devicePath (_Config/Security/DeviceActionRules, else Setpoint)."""
	import re
	rel = str(tagPath or "").replace(chr(92), "/")[len(str(devicePath or "")):].lstrip("/")
	for pat, act in _dsRows(system.tag.readBlocking([DEVICE_ACTION_RULES])[0].value, "Pattern", "Action"):
		try:
			if pat and re.search(str(pat), rel):
				return str(act)
		except Exception:
			_log.warn("bad DeviceActionRules pattern %r" % (pat,))
	return "Setpoint"


def deviceRow(perms, device, action):
	"""The matrix action that gates device/action: itself, its Setpoint/Configuration stand-in, or None (no row)."""
	acts = (perms or {}).get(device) or {}
	if action in acts:
		return action
	alt = STAND_IN.get(action)
	if alt in acts:
		return alt
	return None


def _deny(s, key, what, notify):
	dev, _, act = key.partition("/")
	_log.info("Denied %s for '%s'%s" % (key, _userOf(s) if s is not None else "", (": " + str(what)) if what else ""))
	if notify:
		try:
			shared.Alerts.showAlert(state="warning", title="Not Permitted",
				message="Your role does not have <b>%s / %s</b> in Roles &amp; Permissions, so nothing was "
				"written.<br><br>%s" % (dev, act, str(what or "")), showCloseBtn=True, overlayDismiss=True)
		except Exception as e:
			_log.debug("refusal dialog failed: %s" % e)
	return False


def requireDevice(tagPath, action, what="", session=None, notify=True):
	"""Device-type row only (the caller checked the general row): True unless the session's roles lack the
	<Device>/<action> row of the device on tagPath (then a 'Not Permitted' dialog and a log line)."""
	s, perms = _sessionPerms(session)
	if perms is None:
		return True
	devPath, dev = deviceOf(tagPath)
	if not dev:
		return True
	row = deviceRow(perms, dev, action)
	if row is None or perms[dev][row]:
		return True
	return _deny(s, dev + "/" + row, what or tagPath, notify)


def checkWrite(tagPath, session=None):
	"""(ok, key) for a Perspective session writing tagPath: Faceplates/Operate, then the device-type row of the member
	(deviceOf + actionOf). key = the refusing 'Device/Action' row, '' when allowed. Gateway scripts: (True, '')."""
	s, perms = _sessionPerms(session)
	if perms is None:
		return True, ""
	if not perms.get("Faceplates", {}).get("Operate", False):
		return False, "Faceplates/Operate"
	devPath, dev = deviceOf(tagPath)
	if dev:
		row = deviceRow(perms, dev, actionOf(tagPath, devPath))
		if row is not None and not perms[dev][row]:
			return False, dev + "/" + row
	return True, ""


def requireWrite(tagPath, what="", session=None, notify=True):
	"""checkWrite() for shared.Audit.writeTag / Alerts.confirmApplyWrite / ValveCommands. A device-type refusal
	shows a 'Not Permitted' dialog naming the row; a Faceplates/Operate refusal stays silent (the UI is read only)."""
	ok, key = checkWrite(tagPath, session)
	if ok:
		return True
	s = session if session is not None else _currentSession()
	if key == "Faceplates/Operate":
		_log.info("Denied %s for '%s': %s" % (key, _userOf(s) if s is not None else "", what or tagPath))
		return False
	return _deny(s, key, what or tagPath, notify)
