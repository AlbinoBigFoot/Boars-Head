# Integration endpoints (API connections): [default]_Config/Integrations/<Name>, one Config/Integration UDT
# instance each (Monday today; Oracle etc. later). Common members hold the endpoint and status; Settings is a
# Document member for provider-specific values (Monday: workspaceId, boardId, groupId, columns).
# The API token is write-only from the HMI: get() / listForView() only report hasToken; token() is for gateway-side
# callers (shared.TicketLogger) and never goes to a view.
# ticket-routing (2026-10-24): the view-facing calls (detail / listForView / settingsRows / save / setToken / add /
# test) need Roles & Permissions TicketLogger/Settings (OneShot only); get() / token() stay open for the submit path
# (shared.TicketLogger) and gateway scripts (pingAll timer).

BASE = "[default]_Config/Integrations"
TYPE_ID = "Config/Integration"
FIELDS = ["Provider", "Description", "Enabled", "Endpoint URL", "API Version", "Connected", "Last Check", "Last Error",
		  "Settings"]
EDITABLE = {"description": "Description", "enabled": "Enabled", "url": "Endpoint URL", "apiVersion": "API Version"}
PROVIDERS = ["Monday", "Oracle", "HTTP"]


def _path(name, member=None):
	p = "%s/%s" % (BASE, name)
	if member:
		p += "/" + member
	return p


def _toPy(value):
	"""Document tag value -> plain dict / list."""
	if value is None:
		return None
	if isinstance(value, (dict, list)):
		return value
	for f in (lambda v: system.util.jsonDecode(str(v)), lambda v: system.util.jsonDecode(system.util.jsonEncode(v))):
		try:
			return f(value)
		except Exception:
			pass
	return None


def names():
	out = []
	try:
		results = system.tag.browse(BASE, {"tagType": "UdtInstance"}).getResults()
	except Exception:
		return out
	for r in results:
		try:
			out.append(str(r["name"]))
		except Exception:
			pass
	return sorted(out)


def get(name):
	"""Config and status for one integration, without the token."""
	name = str(name or "")
	if not name:
		return {}
	qvs = system.tag.readBlocking([_path(name, f) for f in FIELDS] + [_path(name, "API Token")])
	v = dict(zip(FIELDS, [q.value for q in qvs[:len(FIELDS)]]))
	settings = _toPy(v.get("Settings"))
	return {
		"name": name,
		"provider": str(v.get("Provider") or ""),
		"description": str(v.get("Description") or ""),
		"enabled": bool(v.get("Enabled")),
		"url": str(v.get("Endpoint URL") or ""),
		"apiVersion": str(v.get("API Version") or ""),
		"connected": bool(v.get("Connected")),
		"lastCheck": v.get("Last Check"),
		"lastError": str(v.get("Last Error") or ""),
		"settings": settings if isinstance(settings, dict) else {},
		"hasToken": bool(str(qvs[-1].value or "").strip()),
	}


def _settingsAllowed():
	return shared.Security.can("TicketLogger", "Settings")


def _requireSettings(what):
	if not shared.Security.require("TicketLogger", "Settings", what):
		raise Exception("Ticket Logger Settings is not permitted for your role (Roles & Permissions)")


def detail(name, rev=None):
	"""get() for the view's runScript binding (rev only re-triggers it after Save / Test)."""
	if not _settingsAllowed():
		return {}
	return get(name)


def statusText(cfg):
	if not cfg.get("enabled"):
		return "Disabled"
	if cfg.get("connected"):
		return "Connected"
	return "Not Connected"


def listForView(rev=None):
	"""Rows for the Integrations table (rev only re-triggers the runScript binding)."""
	rows = []
	if not _settingsAllowed():
		return rows
	for n in names():
		cfg = get(n)
		rows.append({"name": n, "provider": cfg["provider"], "status": statusText(cfg),
					 "url": cfg["url"], "enabled": cfg["enabled"]})
	return rows


def token(name):
	qv = system.tag.readBlocking([_path(name, "API Token")])[0]
	return str(qv.value or "").strip()


def _flatten(d, prefix=""):
	rows = []
	for k in sorted(d.keys()):
		key = prefix + str(k)
		if isinstance(d[k], dict):
			rows.extend(_flatten(d[k], key + "."))
		else:
			rows.append({"key": key, "value": "" if d[k] is None else str(d[k])})
	return rows


def settingsRows(name, rev=None):
	"""Settings document as key / value rows (nested keys dotted: columns.Description)."""
	if not _settingsAllowed():
		return []
	return _flatten(get(name).get("settings") or {})


def unflatten(rows):
	out = {}
	for r in rows or []:
		try:
			key = str(r["key"]).strip()
			value = r["value"]
		except Exception:
			continue
		if not key:
			continue
		node = out
		parts = key.split(".")
		for p in parts[:-1]:
			node = node.setdefault(p, {})
		node[parts[-1]] = "" if value is None else str(value)
	return out


def save(name, values, viewName=None):
	"""values: any of description, enabled, url, apiVersion, settings (dict). Changed members are audited."""
	_requireSettings("integration %s" % name)
	name = str(name or "")
	if not name:
		raise ValueError("Select an integration")
	for key, member in EDITABLE.items():
		if key in values:
			shared.Audit.writeTag(_path(name, member), values[key], viewName=viewName)
	if "settings" in values:
		new = values["settings"] or {}
		if new != (get(name).get("settings") or {}):
			system.tag.writeBlocking([_path(name, "Settings")], [system.util.jsonEncode(new)])
			shared.Audit.logEvent("Integration Settings", "%s Settings" % name, system.util.jsonEncode(new),
								  tagPath=_path(name, "Settings"), viewName=viewName)


def setToken(name, newToken, viewName=None):
	"""Replace the API token; the audit entry never carries the value."""
	_requireSettings("integration %s token" % name)
	newToken = str(newToken or "").strip()
	if not newToken:
		raise ValueError("Enter the new API token")
	system.tag.writeBlocking([_path(name, "API Token")], [newToken])
	shared.Audit.logEvent("Token Replaced", "%s API Token" % name, "(hidden)", tagPath=_path(name, "API Token"),
						  viewName=viewName)


def add(name, provider, viewName=None):
	_requireSettings("new integration")
	name = str(name or "").strip()
	if not name or "/" in name or name.startswith("_"):
		raise ValueError("Enter a name (no '/', not starting with '_')")
	if name in names():
		raise ValueError("%s already exists" % name)
	system.tag.configure(BASE, [{"name": name, "typeId": TYPE_ID, "tagType": "UdtInstance",
								 "tags": [{"name": "Provider", "tagType": "AtomicTag", "value": str(provider or "HTTP")}]}],
						 "a")
	shared.Audit.logEvent("Integration Added", name, str(provider or "HTTP"), tagPath=_path(name), viewName=viewName)


# ------------------------------------------------------------------------------------------ connection tests

def _testMonday(name):
	data = shared.TicketLogger.graphql("query { me { id name } }", integration=name)
	me = data.get("me") if data else None
	if not me or me.get("id") is None:
		raise Exception("Monday returned no user for this token")
	return "Connected as %s" % me.get("name")


def _testHttp(name):
	"""Any other provider until it has its own check: the endpoint must answer below HTTP 400."""
	url = get(name).get("url")
	if not url:
		raise Exception("No Endpoint URL")
	headers = {}
	tok = token(name)
	if tok:
		headers["Authorization"] = tok
	resp = system.net.httpClient(timeout=10000).get(url, headers=headers)
	code = resp.getStatusCode()
	if code >= 400:
		raise Exception("HTTP %s" % code)
	return "HTTP %s" % code


TESTERS = {"Monday": _testMonday}


def test(name):
	"""Run the provider check and write Connected / Last Check / Last Error. Returns [ok, message]."""
	_requireSettings("integration %s test" % name)
	ok, msg = False, ""
	try:
		cfg = get(name)
		if not cfg.get("enabled"):
			raise Exception("Disabled")
		msg = TESTERS.get(cfg.get("provider"), _testHttp)(name)
		ok = True
	except Exception as e:
		msg = str(e)
	system.tag.writeBlocking([_path(name, "Connected"), _path(name, "Last Check"), _path(name, "Last Error")],
							 [ok, system.date.now(), "" if ok else msg[:500]])
	return [ok, msg]


def pingAll():
	for n in names():
		try:
			test(n)
		except Exception:
			pass
