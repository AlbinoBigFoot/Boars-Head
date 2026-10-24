# User Management helpers (Operations > User Management, ported from the HBT/Scout template).
#
# The template's views call system.user.* directly but never looked at the UIResponse, so a gateway-side
# failure (duplicate name, password rule, ...) went back to Home silently. commit() surfaces those errors
# in the standard alert popup and records successful changes in OpsAudit.

logger = system.util.getLogger("shared.UserAdmin")
VIEW_NAME = "Operations/UserManagement"

# Service / shared accounts that are not listed (lower-case usernames). They stay in the user source.
HIDDEN_USERS = set(["admin", "ops", "opcuauser"])
# Roles only shown to users who hold them ([default]_Config/Security/RestrictedRoles). Hidden roles are never
# dropped from data on save.


def isHiddenUser(username):
	return str(username or "").strip().lower() in HIDDEN_USERS


def visibleUsers(userSource):
	"""system.user.getUsers without the service accounts (admin, OPS, ...)."""
	return [u for u in (system.user.getUsers(userSource) or []) if not isHiddenUser(u.get("username"))]


def hiddenRoles(viewerRoles):
	"""Restricted roles the viewer (session user) does not hold - hide these from lists."""
	held = set(str(r) for r in (viewerRoles or []))
	return sorted(r for r in shared.Security.roles('RestrictedRoles') if r not in held)


def visibleRoles(userSource, viewerRoles):
	hide = set(hiddenRoles(viewerRoles))
	return [r for r in (system.user.getRoles(userSource) or []) if str(r) not in hide]


def keepHiddenRoles(userObject, selectedRoles, viewerRoles):
	"""Selected roles plus any restricted roles the user already has but the viewer could not see."""
	roles = list(selectedRoles or [])
	hide = set(hiddenRoles(viewerRoles))
	try:
		current = [str(r) for r in (userObject.getRoles() or [])]
	except Exception:
		current = []
	for r in current:
		if r in hide and r not in roles:
			roles.append(r)
	return roles


def responseErrors(resp):
	"""Error strings from a system.user.* UIResponse (empty list when it succeeded)."""
	if resp is None:
		return []
	try:
		return [str(e) for e in (resp.getErrors() or [])]
	except Exception:
		return []


def commit(kind, action, target, resp, detail=""):
	"""True when the gateway accepted the change; otherwise shows the errors and returns False."""
	errors = responseErrors(resp)
	if errors:
		logger.warn("%s %s %s rejected: %s" % (kind, action, target, errors))
		shared.Alerts.showAlert(
			state="error",
			title="Cannot %s %s" % (action.title(), kind.title()),
			message="\n".join(errors),
			btnTextPrimary="OK",
		)
		return False
	try:
		shared.Audit.logEvent("%s %s" % (kind, action), str(target), detail, viewName=VIEW_NAME)
	except Exception as e:
		logger.warn("audit %s %s %s failed: %s" % (kind, action, target, e))
	return True


def rolesOf(userObject):
	try:
		return ",".join(sorted(str(r) for r in (userObject.getRoles() or [])))
	except Exception:
		return ""


# ==== build_admin (User Management page, .cursor/tasks/user-management/build_admin.py) ====
# Server side of the User Management page (Users / Roles tabs). Same gateway calls and rules as the template views
# (system.user.*, commit() errors + OpsAudit, hidden restricted roles kept, no self delete, Administrator role kept).
# Schedule adjustments (per user, as the template: Start / End / Available / Note) are edited in the user's Profile card;
# a save writes the draft list back with system.user.createScheduleAdjustment + User.setScheduleAdjustments.


def _txt(v):
	return "" if v is None else str(v)


def adjMillis(v):
	"""A schedule date as epoch milliseconds (java Date, number or empty -> None)."""
	if v is None or v == "":
		return None
	try:
		return long(v.getTime())
	except Exception:
		pass
	try:
		return long(v)
	except Exception:
		return None


def userRecord(u):
	first, last, un = _txt(u.get("firstname")), _txt(u.get("lastname")), _txt(u.get("username"))
	name = " ".join(p for p in [first, last] if p).strip()
	ini = "".join(p[0] for p in [first, last] if p).upper() or un[:2].upper()
	try:
		roles = sorted([str(r) for r in (u.getRoles() or [])], key=lambda s: s.lower())
	except Exception:
		roles = []
	contacts = []
	try:
		for c in (u.getContactInfo() or []):
			contacts.append({"type": _txt(c.contactType), "value": _txt(c.value)})
	except Exception:
		pass
	adjustments = []
	try:
		for a in (u.getScheduleAdjustments() or []):
			adjustments.append({"start": adjMillis(a.getStart()), "end": adjMillis(a.getEnd()),
				"available": bool(a.isAvailable()), "note": _txt(a.getNote())})
	except Exception:
		pass
	return {"username": un, "first": first, "last": last, "display": name or un, "initials": ini[:2],
		"adjustments": adjustments,
		"roles": roles, "contacts": contacts, "schedule": _txt(u.get("schedule")) or "Always",
		"language": _txt(u.get("language")), "badge": _txt(u.get("badge")), "notes": _txt(u.get("notes")),
		"search": (" ".join([un, first, last] + roles)).lower()}


def pageData(userSource, viewerRoles):
	"""Everything the page lists: users (people only), every username (duplicate check), roles, options."""
	users = sorted([userRecord(u) for u in visibleUsers(userSource)], key=lambda r: r["username"].lower())
	allNames = [_txt(u.get("username")).lower() for u in (system.user.getUsers(userSource) or [])]
	full = [r.lower() for r in shared.Security.roles("FullPermissionRoles")]
	restricted = [r.lower() for r in shared.Security.roles("RestrictedRoles")]
	roles = []
	for r in sorted([str(x) for x in visibleRoles(userSource, viewerRoles)], key=lambda s: s.lower()):
		members = [{"username": u["username"], "display": u["display"]} for u in users if r in u["roles"]]
		roles.append({"name": r, "users": len(members), "members": members, "full": r.lower() in full,
			"restricted": r.lower() in restricted})
	schedules = []
	for s in (system.user.getSchedules() or []):
		n = str(s.getName())
		if n not in [x["value"] for x in schedules]:
			schedules.append({"value": n, "label": n})
	return {"users": users, "allNames": allNames, "roles": roles, "schedules": schedules or [{"value": "Always", "label": "Always"}],
		"languages": languageOptions()}


def languageOptions():
	from java.util import Locale
	seen = {}
	for loc in Locale.getAvailableLocales():
		tag = str(loc.toLanguageTag()).replace("-", "_")
		if not tag or tag == "und":
			continue
		label = loc.getDisplayLanguage() + ((" (" + loc.getDisplayCountry() + ")") if loc.getDisplayCountry() else "")
		seen[tag] = label
	return [{"value": k, "label": v} for k, v in sorted(seen.items(), key=lambda kv: kv[1].lower())]


def validateUser(userSource, mode, draft):
	"""Same rules as the template form: username required and unique, password pair, notes / badge <= 500."""
	errs = []
	un = _txt(draft.get("username")).strip()
	if not un:
		errs.append("Username is required.")
	others = [_txt(u.get("username")).lower() for u in (system.user.getUsers(userSource) or [])]
	if mode == "add" and un.lower() in others:
		errs.append("Username already exists.")
	if mode == "edit" and un.lower() != _txt(draft.get("originalUsername")).lower() and un.lower() in others:
		errs.append("Username already exists.")
	if mode == "add" or draft.get("changePassword"):
		if not _txt(draft.get("password")) or draft.get("password") != draft.get("confirm"):
			errs.append("Password fields do not match or are empty.")
	for a in (draft.get("adjustments") or []):
		if adjMillis(a.get("start")) is None or adjMillis(a.get("end")) is None:
			errs.append("Every schedule adjustment needs a start and an end date.")
			break
		if adjMillis(a.get("end")) < adjMillis(a.get("start")):
			errs.append("A schedule adjustment cannot end before it starts.")
			break
	if len(_txt(draft.get("notes"))) > 500:
		errs.append("Notes cannot be more than 500 characters.")
	if len(_txt(draft.get("badge"))) > 500:
		errs.append("Badge cannot be more than 500 characters.")
	return errs


def saveUser(session, userSource, mode, draft):
	"""Add / edit a user (template behaviour). Returns True when the gateway accepted it."""
	if not (shared.Security.allowed(session, "UserManagement", "Edit") or
			(mode == "add" and shared.Security.allowed(session, "UserManagement", "Add"))):
		return False
	errs = validateUser(userSource, mode, draft)
	if errs:
		shared.Alerts.showAlert(state="error", title="Cannot Save User", message="\n".join(errs), btnTextPrimary="OK")
		return False
	un = _txt(draft.get("username")).strip()
	if mode == "add":
		u = system.user.getNewUser(userSource, un)
	else:
		u = system.user.getUser(userSource, _txt(draft.get("originalUsername")))
		if u is None:
			shared.Alerts.showAlert(state="error", title="Cannot Save User", message="The user no longer exists.", btnTextPrimary="OK")
			return False
	for k in ("firstname", "lastname", "schedule", "notes", "language", "badge"):
		u.set(k, _txt(draft.get(k)))
	u.set("username", un)
	changePassword = mode == "add" or bool(draft.get("changePassword"))
	if changePassword:
		u.set("password", _txt(draft.get("password")))
	viewer = session.props.auth.user.roles
	u.setRoles(keepHiddenRoles(u, [str(r) for r in (draft.get("roles") or [])], viewer))
	adj = []
	for a in (draft.get("adjustments") or []):
		adj.append(system.user.createScheduleAdjustment(system.date.fromMillis(adjMillis(a.get("start"))),
			system.date.fromMillis(adjMillis(a.get("end"))), bool(a.get("available")), _txt(a.get("note"))))
	u.setScheduleAdjustments(adj)
	u.setContactInfo(None)
	for c in (draft.get("contacts") or []):
		if _txt(c.get("value")).strip():
			u.addContactInfo({_txt(c.get("type")) or "email": _txt(c.get("value")).strip()})
	resp = system.user.addUser(userSource, u) if mode == "add" else system.user.editUser(userSource, u)
	detail = "roles=%s%s; schedule adjustments=%d" % (rolesOf(u), "; password changed" if changePassword else "", len(adj))
	return commit("user", mode, un, resp, detail)


def deleteUser(session, userSource, username):
	if not shared.Security.allowed(session, "UserManagement", "Edit"):
		return False
	if username == session.props.auth.user.userName:
		shared.Alerts.showAlert(state="error", title="Cannot Delete User", message="You cannot delete your own account.", btnTextPrimary="OK")
		return False
	return commit("user", "delete", username, system.user.removeUser(userSource, username))


def saveRole(session, userSource, mode, oldName, newName):
	if not (shared.Security.allowed(session, "UserManagement", "Edit") or
			(mode == "add" and shared.Security.allowed(session, "UserManagement", "Add"))):
		return False
	newName = _txt(newName).strip()
	existing = [str(r) for r in (system.user.getRoles(userSource) or [])]
	err = ""
	if not newName:
		err = "Role name cannot be empty."
	elif newName in existing and (mode == "add" or newName != oldName):
		err = "Role already exists."
	if err:
		shared.Alerts.showAlert(state="error", title="Cannot Save Role", message=err, btnTextPrimary="OK")
		return False
	if mode == "add":
		resp = system.user.addRole(userSource, newName)
	else:
		resp = system.user.editRole(userSource, oldName, newName)
	return commit("role", mode, newName, resp, "" if mode == "add" else "renamed from %s" % oldName)


def deleteRole(session, userSource, role):
	if not shared.Security.allowed(session, "UserManagement", "Edit"):
		return False
	# was: role == "Administrator"; now any role in _Config/Security AdminRoles / FullPermissionRoles (no role names here)
	keep = [r.lower() for r in shared.Security.roles("AdminRoles") + shared.Security.roles("FullPermissionRoles")]
	if str(role).lower() in keep:
		shared.Alerts.showAlert(state="error", title="Cannot Delete Role",
			message="%s is listed in _Config/Security (AdminRoles / FullPermissionRoles) and cannot be deleted here." % role,
			btnTextPrimary="OK")
		return False
	return commit("role", "delete", role, system.user.removeRole(userSource, role))
# ==== end build_admin ====
