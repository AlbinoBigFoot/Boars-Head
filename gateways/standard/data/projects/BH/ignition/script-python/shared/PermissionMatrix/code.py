# Roles & Permissions page (Operations > Roles & Permissions) - server side (.cursor/tasks/user-management/build_admin.py).
#
# The matrix [default]_Config/RolesPermissions stays the source of truth (Devices / Actions / Description + one Boolean
# column per role); this module never reorders rows or rewrites the dataset. save() re-reads the tag right before the
# write and applies only the edited cells, so rows / columns another builder added meanwhile are kept.
# role-wizard (2026-10-24): a role the matrix has no column for gets one with _Config/Security/NewRoleDefaults ticked
# (syncRoles on page load, save); createRole() = the New Role wizard (gateway role + matrix column + audit, rolled back
# when the matrix write fails). Rows hidden from the viewer (RestrictedRows) are never changed by their saves.

import threading

MATRIX = "[default]_Config/RolesPermissions"
SEC = "[default]_Config/Security/"
KEY_COLS = ("Devices", "Actions", "Description", "Category")
VIEW_NAME = "Operations/RolesPermissions"
_log = system.util.getLogger("shared.PermissionMatrix")
_lock = threading.Lock()       # one matrix read-modify-write at a time (save / syncRoles / createRole)


def _roleColumns(ds):
	return [c for c in ds.getColumnNames() if c not in KEY_COLS]


def roleInfo(userSource, viewerRoles):
	"""Roles shown as matrix columns: [{name, users, members, restricted, inMatrix}].

	Gateway roles only (as before); RestrictedRoles the viewer does not hold are left out (shared.UserAdmin).
	Order: the matrix column order, then roles the matrix has no column for yet (alphabetical)."""
	roles = [str(r) for r in shared.UserAdmin.visibleRoles(userSource, viewerRoles)]
	users = shared.UserAdmin.visibleUsers(userSource)
	ds = system.tag.readBlocking([MATRIX])[0].value
	cols = _roleColumns(ds) if ds is not None else []
	restricted = [r.lower() for r in shared.Security.roles("RestrictedRoles")]
	ordered = [c for c in cols if c in roles] + sorted([r for r in roles if r not in cols], key=lambda s: s.lower())
	out = []
	for r in ordered:
		members = []
		for u in users:
			try:
				held = [str(x) for x in (u.getRoles() or [])]
			except Exception:
				held = []
			if r in held:
				name = " ".join(p for p in [u.get("firstname") or "", u.get("lastname") or ""] if p).strip()
				members.append({"username": str(u.get("username")), "display": name or str(u.get("username"))})
		out.append({"name": r, "users": len(members), "members": members, "restricted": r.lower() in restricted,
			"inMatrix": r in cols})
	return out


def _rows(ds):
	return [dict((c, ds.getValueAt(i, c)) for c in ds.getColumnNames()) for i in range(ds.getRowCount())]


def model():
	"""(perms, cats): perms = [{key, dev, act, label, desc, cat, sub, ticks{col: bool}}] merged by Devices/Actions, in
	page order; cats = [{name, icon, desc}]. Same grouping rules as the page expressions (permission_catalog.py)."""
	vals = system.tag.readBlocking([MATRIX, SEC + "PermissionCatalog", SEC + "PermissionCategories"])
	ds, cat_ds, cats_ds = vals[0].value, vals[1].value, vals[2].value
	cats = [{"name": str(r["Name"]), "order": r["Order"], "icon": str(r["Icon"] or ""), "desc": str(r["Description"] or "")}
		for r in (_rows(cats_ds) if cats_ds is not None else [])]
	names = [c["name"] for c in cats]
	catalog = dict((str(r["Key"]), r) for r in (_rows(cat_ds) if cat_ds is not None else []))

	def entry(k, col):
		r = catalog.get(k)
		return str(r[col] or "") if r is not None and r[col] is not None else ""

	perms, seen = [], {}
	for n, r in enumerate(_rows(ds) if ds is not None else []):
		key = "%s/%s" % (r["Devices"], r["Actions"])
		if key in seen:
			p = seen[key]
			p["desc"] += " / " + str(r["Description"] or "")
			for c in p["ticks"]:
				p["ticks"][c] = p["ticks"][c] or bool(r[c])
			continue
		dev = str(r["Devices"])
		catCol = str(r.get("Category") or "")
		cat = next((c for c in (entry(key, "Category"), catCol if catCol in names else "",
			entry(catCol, "Category") if catCol else "", entry(dev, "Category")) if c and c in names), "Other")
		p = {"key": key, "dev": dev, "act": str(r["Actions"]), "desc": str(r["Description"] or ""), "cat": cat,
			"label": entry(key, "Label") or str(r["Description"] or "") or (dev + " " + str(r["Actions"])),
			"sub": entry(dev, "Label") or dev, "n": n,
			"devOrder": catalog[dev]["Order"] if dev in catalog else 999,
			"ticks": dict((c, bool(r[c])) for c in r if c not in KEY_COLS)}
		seen[key] = p
		perms.append(p)
	order = dict((c["name"], c["order"]) for c in cats)
	perms.sort(key=lambda p: (order.get(p["cat"], 99), p["devOrder"], p["n"]))
	return perms, cats


def _esc(s):
	return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def roleSummary(userSource, viewerRoles):
	"""roleInfo() plus, per role, what it is granted (saved matrix, inheritance + full roles applied):
	{full, base, heirs, granted, total, html} - html = one block per group for the Roles tab (markdown, raw HTML)."""
	syncRoles(userSource)
	info = roleInfo(userSource, viewerRoles)
	perms, cats = model()
	# device-perms (2026-10-24): RestrictedRows (Ticket Logger) - hidden from viewers without their role, and not implied
	# by a full permission role (only ticks count)
	rcsv = system.tag.readBlocking([SEC + "RestrictedRows"])[0].value
	restricted = shared.Security.restrictedRows(rcsv)
	perms = [p for p in perms if shared.Security.rowVisible(p["key"], viewerRoles, rcsv)]
	full = [r.lower() for r in shared.Security.roles("FullPermissionRoles")]
	pairs = []
	for item in str(system.tag.readBlocking([SEC + "RoleInherits"])[0].value or "").split(","):
		a, _, b = item.partition(":")
		if a.strip() and b.strip():
			pairs.append((a.strip().lower(), b.strip().lower()))
	proper = dict((str(r["name"]).lower(), r["name"]) for r in info)
	for r in info:
		name = r["name"]
		held = shared.Security.effectiveRoles([name], ",".join("%s:%s" % p for p in pairs))
		isFull = name.lower() in full

		def has(p):
			return (isFull and p["key"] not in restricted) or any(v for c, v in p["ticks"].items() if c.lower() in held)
		r["full"] = isFull
		r["base"] = ", ".join(proper.get(b, b) for a, b in pairs if a == name.lower())
		r["heirs"] = ", ".join(proper.get(a, a) for a, b in pairs if b == name.lower())
		r["total"] = len(perms)
		r["granted"] = len([p for p in perms if has(p)])
		blocks = []
		for c in cats:
			ps = [p for p in perms if p["cat"] == c["name"]]
			if not ps:
				continue
			yes = [p["label"] for p in ps if has(p)]
			no = [p["label"] for p in ps if not has(p)]
			pct = int(round(100.0 * len(yes) / len(ps)))
			blocks.append('<div class="admin-md-cat"><div class="admin-md-head"><span class="admin-md-name">%s</span>'
				'<span class="admin-md-track"><span class="admin-md-fill" style="width:%d%%"></span></span>'
				'<span class="admin-md-count">%d/%d</span></div>%s%s</div>' % (
					_esc(c["name"]), pct, len(yes), len(ps),
					('<div class="admin-md-yes">Granted: %s</div>' % _esc(", ".join(yes))) if yes else "",
					('<div class="admin-md-no">Not Granted: %s</div>' % _esc(", ".join(no))) if no else ""))
		r["html"] = "".join(blocks)
		r["membersText"] = ", ".join("%s (%s)" % (m["display"], m["username"]) for m in r["members"]) or "No Users"
	return info


def editSummary(edits):
	"""Change bar text: 'ReadOnly: +3 Granted, Maintenance: 1 Revoked'."""
	per = {}
	for k, v in (edits or {}).items():
		role = str(k).partition("|")[2]
		g = per.setdefault(role, [0, 0])
		g[0 if v else 1] += 1
	parts = []
	for role in sorted(per, key=lambda s: s.lower()):
		g, r = per[role]
		bits = (["+%d Granted" % g] if g else []) + (["%d Revoked" % r] if r else [])
		parts.append("%s: %s" % (role, " / ".join(bits)))
	return ", ".join(parts)


def _summary(edits, labels):
	"""Readable lines for the confirm dialog: 'Maintenance: Grant View Audit Log'."""
	lines = []
	for k in sorted(edits.keys()):
		key, _, role = k.partition("|")
		lines.append("%s: %s %s" % (role, "Grant" if edits[k] else "Revoke", labels.get(key, key)))
	return lines


def describe(edits, labels, limit=6):
	lines = _summary(edits, labels)
	more = len(lines) - limit
	text = "\n".join(lines[:limit])
	if more > 0:
		text += "\n... and %d more" % more
	return text


def save(session, edits):
	with _lock:
		return _save(session, edits)


def _save(session, edits):
	"""Apply {"Devices/Actions|Role": bool} to the live matrix. Returns {"ok", "changed", "message"}.

	Every row with that Devices/Actions gets the tick (duplicate keys are OR-ed by shared.Security anyway). A role the
	matrix has no column for yet gets a Boolean column appended (NewRoleDefaults ticked, the rest False). _Config/Security/RoleInherits pairs: a grant
	to the base role is also written to the heir for the edited rows (the security-tiers builder keeps the matrix in
	step the same way). Full permission roles are skipped (they always hold everything)."""
	if not shared.Security.allowed(session, "RolesPermissions", "Edit"):
		return {"ok": False, "changed": 0, "message": "You do not have Edit Roles & Permissions."}
	edits = dict(edits or {})
	if not edits:
		return {"ok": True, "changed": 0, "message": "No changes to save."}
	full = [r.lower() for r in shared.Security.roles("FullPermissionRoles")]
	pairs = []
	for item in str(system.tag.readBlocking([SEC + "RoleInherits"])[0].value or "").split(","):
		a, _, b = item.partition(":")
		if a.strip() and b.strip():
			pairs.append((a.strip(), b.strip()))
	# device-perms (2026-10-24): a RestrictedRows row (Ticket Logger) is saved only by a viewer holding one of its roles,
	# and its full-role columns are real ticks there (not skipped)
	rcsv = system.tag.readBlocking([SEC + "RestrictedRows"])[0].value
	restricted = shared.Security.restrictedRows(rcsv)
	try:
		viewer = [str(r) for r in (session.props.auth.user.roles or [])]
	except Exception:
		viewer = []
	hidden = [k for k in restricted if not shared.Security.rowVisible(k, viewer, rcsv)]
	if any(str(k).partition("|")[0] in hidden for k in edits):
		return {"ok": False, "changed": 0, "message": "Some of these rows are managed by another role."}
	ds = system.tag.readBlocking([MATRIX])[0].value       # re-read right before the write
	if ds is None:
		return {"ok": False, "changed": 0, "message": "The permission matrix tag could not be read."}
	byKey = {}
	for i in range(ds.getRowCount()):
		byKey.setdefault("%s/%s" % (ds.getValueAt(i, "Devices"), ds.getValueAt(i, "Actions")), []).append(i)
	changed = 0
	skipped = []
	cells = []
	for k, v in edits.items():
		key, _, role = str(k).partition("|")
		if role.lower() in full and key not in restricted:
			continue
		if key not in byKey:
			skipped.append(key)
			continue
		cells.append((key, role, bool(v)))
		for heir, base in pairs:
			if bool(v) and base.lower() == role.lower() and (heir.lower() not in full or key in restricted):
				cells.append((key, heir, True))
	cols = list(ds.getColumnNames())
	for key, role, v in cells:
		col = next((c for c in cols if c.lower() == role.lower()), None)
		if col is None:
			ds = _addRoleColumn(ds, role, _defaults())
			cols.append(role)
			col = role
		for i in byKey[key]:
			if bool(ds.getValueAt(i, col)) != v:
				ds = system.dataset.setValue(ds, i, col, v)
				changed += 1
	if changed:
		qc = system.tag.writeBlocking([MATRIX], [ds])[0]
		if not qc.isGood():
			_log.warn("matrix write failed: %s" % qc)
			return {"ok": False, "changed": 0, "message": "The matrix write was refused (%s)." % qc}
		try:
			detail = "; ".join("%s %s=%s" % (k.partition("|")[0], k.partition("|")[2], bool(v)) for k, v in sorted(edits.items()))
			shared.Audit.logEvent("Permissions Changed", "RolesPermissions", detail[:900], tagPath=MATRIX, viewName=VIEW_NAME)
		except Exception as e:
			_log.warn("audit failed: %s" % e)
	msg = "Saved %d change%s." % (len(edits), "" if len(edits) == 1 else "s")
	if skipped:
		msg += " Not found (removed meanwhile): %s." % ", ".join(sorted(set(skipped)))
	return {"ok": True, "changed": changed, "message": msg}


# ---- role-wizard (2026-10-24): new roles -------------------------------------------------------------------------
# Role-list tags a new role name must not appear in (a name already listed there would silently inherit that power).
ROLE_LIST_TAGS = ("AdminRoles", "FullPermissionRoles", "RestrictedRoles", "IntegrationRoles", "ReadOnlyRoles",
	"TicketLoggerRoles")
NAME_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 _-"
WIZARD_VIEW = "00_Pages/Boars Head/Operations/_Admin/NewRole"
WIZARD_ID = "newRoleWizard"


def _defaults():
	"""Devices/Actions keys a new role gets (_Config/Security/NewRoleDefaults)."""
	return shared.Security.newRoleDefaults(system.tag.readBlocking([SEC + "NewRoleDefaults"])[0].value)


def _key(ds, i):
	return "%s/%s" % (ds.getValueAt(i, "Devices"), ds.getValueAt(i, "Actions"))


def _addRoleColumn(ds, role, ticks):
	"""ds plus a Boolean column for role; rows whose Devices/Actions key is in ticks are True."""
	vals = [_key(ds, i) in ticks for i in range(ds.getRowCount())]
	return system.dataset.addColumn(ds, ds.getColumnCount(), vals, role, bool)


def syncRoles(userSource="default"):
	"""Add a matrix column (NewRoleDefaults ticked) for every gateway role without one - a role created in the gateway,
	not through the wizard. Existing columns are never changed. Returns the role names added."""
	try:
		roles = [str(r) for r in (system.user.getRoles(userSource) or [])]
	except Exception as e:
		_log.warn("syncRoles: roles of %s unreadable: %s" % (userSource, e))
		return []
	with _lock:
		ds = system.tag.readBlocking([MATRIX])[0].value
		if ds is None:
			return []
		have = set(c.lower() for c in _roleColumns(ds))
		missing = [r for r in roles if r.lower() not in have]
		if not missing:
			return []
		ticks = _defaults()
		for r in missing:
			ds = _addRoleColumn(ds, r, ticks)
		qc = system.tag.writeBlocking([MATRIX], [ds])[0]
	if not qc.isGood():
		_log.warn("syncRoles: matrix write failed: %s" % qc)
		return []
	for r in missing:
		_log.info("Role %s added to the matrix with %s" % (r, ", ".join(sorted(ticks)) or "no permissions"))
		try:
			shared.Audit.logEvent("Role Added To Matrix", r, "New gateway role; default permissions: %s"
				% (", ".join(sorted(ticks)) or "none"), tagPath=MATRIX, viewName=VIEW_NAME)
		except Exception as e:
			_log.warn("audit failed: %s" % e)
	return missing


def _viewerRoles(session):
	try:
		return [str(r) for r in (session.props.auth.user.roles or [])]
	except Exception:
		return []


def _userName(session):
	try:
		return str(session.props.auth.user.userName)
	except Exception:
		return "?"


def _hiddenKeys(viewerRoles):
	rcsv = system.tag.readBlocking([SEC + "RestrictedRows"])[0].value
	return set(k for k in shared.Security.restrictedRows(rcsv) if not shared.Security.rowVisible(k, viewerRoles, rcsv))


def wizardModel(userSource, viewerRoles):
	"""New Role wizard data: {groups: [{name, icon, desc, rows: [{key, label, desc, sub}]}], defaults: [keys the
	viewer sees pre-ticked], roles: [role names to copy from], total}. RestrictedRows the viewer may not see are left
	out (createRole sets them to their NewRoleDefaults value)."""
	perms, cats = model()
	hidden = _hiddenKeys(viewerRoles)
	perms = [p for p in perms if p["key"] not in hidden]
	groups = []
	for c in cats:
		rows = [{"key": p["key"], "label": p["label"], "desc": p["desc"], "sub": p["sub"]} for p in perms
			if p["cat"] == c["name"]]
		if rows:
			groups.append({"name": c["name"], "icon": c["icon"] or "material/folder", "desc": c["desc"], "rows": rows})
	shown = set(p["key"] for p in perms)
	roles = sorted([str(r) for r in shared.UserAdmin.visibleRoles(userSource, viewerRoles)], key=lambda x: x.lower())
	return {"groups": groups, "defaults": sorted(k for k in _defaults() if k in shown), "roles": roles,
		"total": len(perms)}


def roleGrants(role, viewerRoles):
	"""Copy Permissions From: the keys `role` effectively holds (its ticks, RoleInherits, full permission role),
	limited to the rows the viewer sees."""
	qv = system.tag.readBlocking([MATRIX, SEC + "FullPermissionRoles", SEC + "RoleInherits", SEC + "RestrictedRows",
		SEC + "NewRoleDefaults"])
	perms = shared.Security.permissions([role], qv[0].value, qv[1].value, qv[2].value, qv[3].value, qv[4].value)
	hidden = _hiddenKeys(viewerRoles)
	return sorted(d + "/" + a for d in perms for a in perms[d] if perms[d][a] and (d + "/" + a) not in hidden)


def checkRoleName(userSource, name):
	"""'' when name can be a new role, else the reason (operator-readable)."""
	name = str(name or "").strip()
	if not name:
		return "Enter A Role Name."
	if len(name) > 50:
		return "Role Names Are At Most 50 Characters."
	if any(ch not in NAME_CHARS for ch in name):
		return "Use Letters, Numbers, Spaces, - And _ Only."
	low = name.lower()
	if low in [k.lower() for k in KEY_COLS]:
		return "%s Is A Reserved Matrix Column Name." % name
	if low in [str(r).lower() for r in (system.user.getRoles(userSource) or [])]:
		return "A Role Named %s Already Exists." % name
	vals = system.tag.readBlocking([SEC + t for t in ROLE_LIST_TAGS] + [SEC + "RoleInherits", SEC + "RestrictedRows"])
	for t, qv in zip(ROLE_LIST_TAGS, vals[:len(ROLE_LIST_TAGS)]):
		if low in shared.Security.roleList(qv.value):
			return "%s Is Listed In _Config/Security/%s - Pick Another Name (Or Edit That Tag First)." % (name, t)
	for item in str(vals[-2].value or "").split(","):
		if low in [x.strip().lower() for x in item.split(":")]:
			return "%s Is Listed In _Config/Security/RoleInherits - Pick Another Name." % name
	for who in shared.Security.restrictedRows(vals[-1].value).values():
		if low in who:
			return "%s Is Listed In _Config/Security/RestrictedRows - Pick Another Name." % name
	return ""


def mayCreate(session):
	"""Add Users And Roles (or Edit Users And Roles) plus Edit Roles & Permissions."""
	return shared.Security.allowed(session, "RolesPermissions", "Edit") and (
		shared.Security.allowed(session, "UserManagement", "Add") or
		shared.Security.allowed(session, "UserManagement", "Edit"))


def createRole(session, userSource, name, grants, copyFrom=""):
	"""New Role wizard: add the role to the user source and its matrix column (the chosen visible rows; hidden
	RestrictedRows get their NewRoleDefaults value), then audit "Role Created". The role is removed again when the
	matrix write fails. No _Config/Security role list is changed. Returns {"ok", "message", "granted"}."""
	if not mayCreate(session):
		return {"ok": False, "message": "Creating A Role Needs Add Users And Roles And Edit Roles & Permissions."}
	name = str(name or "").strip()
	err = checkRoleName(userSource, name)
	if err:
		return {"ok": False, "message": err}
	hidden = _hiddenKeys(_viewerRoles(session))
	defaults = _defaults()
	errs = shared.UserAdmin.responseErrors(system.user.addRole(userSource, name))
	if errs:
		return {"ok": False, "message": "The Gateway Refused The Role: " + "; ".join(errs)}
	ticks = set()
	qc = None
	with _lock:
		ds = system.tag.readBlocking([MATRIX])[0].value
		if ds is not None:
			keys = set(_key(ds, i) for i in range(ds.getRowCount()))
			ticks = set(str(k) for k in (grants or []) if str(k) in keys and str(k) not in hidden)
			ticks |= set(k for k in defaults if k in hidden and k in keys)
			col = next((c for c in _roleColumns(ds) if c.lower() == name.lower()), None)
			if col is None:
				ds = _addRoleColumn(ds, name, ticks)
			else:                       # a column left by a deleted role (or syncRoles meanwhile): it is this role's now
				for i in range(ds.getRowCount()):
					if bool(ds.getValueAt(i, col)) != (_key(ds, i) in ticks):
						ds = system.dataset.setValue(ds, i, col, _key(ds, i) in ticks)
			qc = system.tag.writeBlocking([MATRIX], [ds])[0]
	if qc is None or not qc.isGood():
		_log.warn("createRole %s: matrix write failed (%s) - removing the role again" % (name, qc))
		try:
			system.user.removeRole(userSource, name)
		except Exception as e:
			_log.error("createRole %s: rollback failed: %s" % (name, e))
		return {"ok": False, "message": "The Permission Matrix Could Not Be Written, So The Role Was Not Created."}
	n = len(ticks)
	detail = "User source %s; %d permission%s%s: %s" % (userSource, n, "" if n == 1 else "s",
		(" (copied from %s, then edited)" % copyFrom) if copyFrom else "", ", ".join(sorted(ticks)))
	try:
		shared.Audit.logEvent("Role Created", name, detail[:900], tagPath=MATRIX, viewName=VIEW_NAME)
	except Exception as e:
		_log.warn("audit failed: %s" % e)
	_log.info("Role %s created by %s with %d permissions" % (name, _userName(session), n))
	return {"ok": True, "message": "Created Role %s With %d Permission%s." % (name, n, "" if n == 1 else "s"),
		"granted": n}


def openWizard(page, userSource="default"):
	"""Open the New Role wizard popup, centred in the caller's viewport (never larger than it)."""
	vw, vh = 1366, 768
	try:
		vw = int(page.props.dimensions.viewport.width or vw)
		vh = int(page.props.dimensions.viewport.height or vh)
	except Exception:
		pass
	w, h = min(760, vw - 32), min(660, vh - 32)
	try:
		system.perspective.closePopup(WIZARD_ID)
	except Exception:
		pass
	system.perspective.openPopup(id=WIZARD_ID, view=WIZARD_VIEW, params={"userSource": userSource},
		position={"left": max(0, (vw - w) // 2), "top": max(0, (vh - h) // 2), "width": w, "height": h},
		modal=True, draggable=False, resizable=False, showCloseIcon=False, overlayDismiss=False, viewportBound=True)
