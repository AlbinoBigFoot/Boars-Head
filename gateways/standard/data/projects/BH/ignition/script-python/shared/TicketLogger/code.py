# Ticket Logger (2026-10-24 ticket-routing): every logged-in user submits tickets (Roles & Permissions
# TicketLogger/Use); the ticket's selection (Type, plus the Area parsed from its tag path) picks a destination from
# [default]_Config/TicketLogger/Routing and send() dispatches it through that destination's adapter.
#
# Adapter interface (ADAPTERS, keyed by destination name):
#   adapter(ticket, route, dryRun) -> {"ok": True, "id": str, "url": str, "status": str, "message": str}
#   ticket = {"title", "tagPath", "viewName", "reporter", "username", "email", "priority" (1-4), "type",
#             "area", "sections": [(label, text)]}
#   route  = {"destination", "boardId", "groupId", "rule" (index or -1), "match" ("Type + Area" | "Type" | "Area" |
#             "Default")}
#   Raise an Exception with an operator-readable message on failure. Never put credentials in the result, the
#   outbox payload or an audit entry.
# Monday = the Monday.com Tickets board (createTicket, unchanged behaviour; a rule may override board / group).
# Oracle = stub until the client integration exists: validates and queues the ticket in dbo.ticket_outbox
#          (status "Pending Oracle"); a later Oracle adapter / sender drains that table without UI changes.
# Dry run ([default]_Config/TicketLogger/DryRun = true): no external call; the ticket is recorded in the outbox with
# status "Dry Run" and its resolved destination (test routing without creating Monday items).
# Settings (routing, dry run, integrations) need TicketLogger/Settings (OneShot only, a RestrictedRows row).
# device-perms + ticket-routing: TicketLogger/Use on send / createTicket, TicketLogger/Settings on settings calls.

API_URL = "https://api.monday.com/v2"
API_VERSION = "2026-07"

PRIORITY_LABELS = {
	1: "Critical",
	2: "High",
	3: "Medium",
	4: "Low",
}

INTEGRATION = "Monday"   # [default]_Config/Integrations/Monday (shared.Integrations)
ROUTING_TAG = "[default]_Config/TicketLogger/Routing"
DRY_RUN_TAG = "[default]_Config/TicketLogger/DryRun"
TYPES_TAG = "[default]_Config/TicketLogger/Types"
DESTINATIONS = ["Monday", "Oracle"]
ORACLE_PENDING = "Pending Oracle"
DRY_RUN_STATUS = "Dry Run"
DEVICE_ROOT = "Boars_Head"

_log = system.util.getLogger("BH.TicketLogger")


def _cfg(integration=INTEGRATION):
	cfg = shared.Integrations.get(integration)
	if not cfg:
		raise Exception("Integration %s not found under %s" % (integration, shared.Integrations.BASE))
	return cfg


def _col(settings, name, fallback):
	v = (settings.get("columns") or {}).get(name)
	return v if v else fallback


def _token(integration=INTEGRATION):
	t = shared.Integrations.token(integration)
	if not t:
		raise Exception("%s API Token missing (Ticket Logger > Settings > Destinations)" % integration)
	return t


def graphql(query, variables=None, integration=INTEGRATION):
	"""POST GraphQL to monday.com. Returns data dict; raises on HTTP/GraphQL errors."""
	cfg = _cfg(integration)
	client = system.net.httpClient(redirect_policy="ALWAYS")
	body = {"query": query}
	if variables is not None:
		body["variables"] = variables
	resp = client.post(
		url=cfg.get("url") or API_URL,
		headers={
			"Authorization": _token(integration),
			"Content-Type": "application/json",
			"API-Version": cfg.get("apiVersion") or API_VERSION,
		},
		data=system.util.jsonEncode(body),
	)
	status = resp.getStatusCode()
	text = resp.getText()
	if status != 200:
		raise Exception("Monday HTTP %s: %s" % (status, text))
	payload = system.util.jsonDecode(text)
	errors = payload.get("errors")
	if errors:
		raise Exception("Monday GraphQL: %s" % errors)
	return payload.get("data")


def ping():
	"""Return True if the Monday token can call me { id }."""
	try:
		data = graphql("query { me { id name } }")
		me = data.get("me") if data else None
		return me is not None and me.get("id") is not None
	except:
		return False


def _priority_label(priority):
	try:
		p = int(priority)
	except:
		p = 3
	return PRIORITY_LABELS.get(p, "Medium")


def _build_description(title, viewName, reporter, sections):
	"""sections: [(label, text)] in form order (the ticket type's fields)."""
	parts = [
		"Tag Path: %s" % (title or ""),
		"View Path: %s" % (viewName or ""),
		"Created By: %s" % (reporter or ""),
	]
	for label, text in sections:
		parts += ["", "%s:" % label, text or ""]
	text = "\n".join(parts)
	# long_text soft limit ~2000; keep column under that, full body goes to update
	if len(text) > 1900:
		return text[:1890] + "\n...(see update for full text)", text
	return text, text


def _mondayRequest(title, viewName, reporter, priority, email, requestType, sections, boardId=None, groupId=None):
	"""(boardId, groupId, itemName, column_values, fullDesc) for create_item; boardId / groupId '' = integration."""
	settings = _cfg().get("settings") or {}
	boardId = str(boardId or "").strip() or settings.get("boardId")
	if boardId is None or str(boardId).strip() == "":
		raise Exception("Monday boardId not set (Ticket Logger > Settings > Destinations > Monday settings)")
	groupId = str(groupId or "").strip() or settings.get("groupId") or "topics"

	colDesc = _col(settings, "Description", "long_text7")
	colEmp = _col(settings, "Employee Name", "text")
	colStatus = _col(settings, "Status", "status95")
	colPri = _col(settings, "Priority", "priority")
	colType = _col(settings, "Request Type", "request_type")
	colDate = _col(settings, "Creation Date", "date")
	colEmail = _col(settings, "Email", "email")

	shortDesc, fullDesc = _build_description(title, viewName, reporter, sections)
	today = system.date.format(system.date.now(), "yyyy-MM-dd")
	column_values = {
		colDesc: {"text": shortDesc},
		colEmp: reporter or "",
		colStatus: {"label": "New"},
		colPri: {"label": _priority_label(priority)},
		colType: {"label": requestType or "Issue"},
		colDate: {"date": today},
	}
	if email:
		column_values[colEmail] = {"email": str(email), "text": str(email)}
	return str(boardId), str(groupId), (title or "Untitled ticket")[:255], column_values, fullDesc


def createTicket(
	title,
	viewName,
	reporter,
	priority,
	expectedResult="",
	actualResult="",
	stepsToRecreate="",
	email=None,
	requestType="Issue",
	sections=None,
	boardId=None,
	groupId=None,
):
	"""
	Create a Monday Tickets board item (the Monday adapter; behaviour unchanged since 2026-09-30).

	sections: [(label, text)] from the ticket type's fields (_Config/TicketLogger/Types); without it the classic
	Expected / Actual / Steps trio is used. boardId / groupId: routing rule override ('' = integration settings).
	Returns dict: { "id": str, "url": str, "name": str }
	Raises on failure.
	"""
	# device-perms + ticket-routing: Roles & Permissions TicketLogger/Use (every role; gateway scripts pass)
	if not shared.Security.require('TicketLogger', 'Use', title):
		raise Exception("Ticket Logger is not permitted for your role (Roles & Permissions)")
	if sections is None:
		sections = [("Expected Result", expectedResult), ("Actual Result", actualResult),
					("Steps to Recreate", stepsToRecreate)]
	boardId, groupId, itemName, column_values, fullDesc = _mondayRequest(
		title, viewName, reporter, priority, email, requestType, sections, boardId, groupId)

	mutation = (
		"mutation ($boardId: ID!, $groupId: String, $itemName: String!, $columnValues: JSON!) {\n"
		"  create_item(\n"
		"    board_id: $boardId\n"
		"    group_id: $groupId\n"
		"    item_name: $itemName\n"
		"    column_values: $columnValues\n"
		"    create_labels_if_missing: true\n"
		"  ) { id name url }\n"
		"}"
	)
	# Monday JSON variable: pass encoded object string (API accepts JSON type as stringified object)
	variables = {
		"boardId": boardId,
		"groupId": groupId,
		"itemName": itemName,
		"columnValues": system.util.jsonEncode(column_values),
	}
	data = graphql(mutation, variables)
	item = data.get("create_item") if data else None
	if not item or not item.get("id"):
		raise Exception("Monday create_item returned no id: %s" % data)

	# Full repro as update when truncated or always useful for operators
	try:
		upd = (
			"mutation ($itemId: ID!, $body: String!) {\n"
			"  create_update(item_id: $itemId, body: $body) { id }\n"
			"}"
		)
		graphql(upd, {"itemId": str(item["id"]), "body": fullDesc})
	except:
		pass

	return {
		"id": str(item.get("id")),
		"url": item.get("url") or "",
		"name": item.get("name") or "",
	}


# ------------------------------------------------------------------------------------------------ routing

def _toPy(value):
	"""JSON text, plain Python or a Perspective / Java structure -> plain Python."""
	if value is None:
		return None
	if isinstance(value, (dict, list)):
		return _unq(value)
	if isinstance(value, basestring):
		try:
			return system.util.jsonDecode(value)
		except Exception:
			return None
	try:
		return plain(value)
	except Exception:
		return None


def _route(d, rule=-1, match="Default"):
	d = d or {}
	dest = str(d.get("destination") or "").strip()
	return {"destination": dest if dest in DESTINATIONS else "Monday",
			"type": str(d.get("type") or "").strip(),
			"area": str(d.get("area") or "").strip(),
			"boardId": str(d.get("boardId") or "").strip(),
			"groupId": str(d.get("groupId") or "").strip(),
			"rule": rule, "match": match}


def normalize(doc):
	"""Routing document -> {"default": route, "rules": [route]} (unknown destinations fall back to Monday)."""
	doc = _toPy(doc)
	if not isinstance(doc, dict):
		doc = {}
	rules = []
	for r in doc.get("rules") or []:
		if isinstance(r, dict):
			x = _route(r)
			rules.append({k: x[k] for k in ("type", "area", "destination", "boardId", "groupId")})
	d = _route(doc.get("default"))
	return {"default": {k: d[k] for k in ("destination", "boardId", "groupId")}, "rules": rules}


def loadRouting():
	v = system.tag.readBlocking([ROUTING_TAG])[0].value
	# a Document tag value prints as its JSON text
	return normalize(None if v is None else (v if isinstance(v, (dict, basestring)) else unicode(v)))


def dryRun():
	qv = system.tag.readBlocking([DRY_RUN_TAG])[0]
	return bool(qv.value) if qv.quality.isGood() else False


def areaOf(tagPath):
	"""Area of a device tag path ([default]Boars_Head/<Site>/<Area>/...), '' when the path is not a device path."""
	p = str(tagPath or "").strip()
	if "]" in p:
		p = p.split("]", 1)[1]
	parts = [x for x in p.split("/") if x]
	if len(parts) >= 3 and parts[0] == DEVICE_ROOT:
		return parts[2]
	return ""


def resolve(ticketType, area="", routing=None):
	"""The route for a selection: the most specific matching rule (Type + Area, then Type, then Area; table order on
	a tie), else the default. A rule's blank Type / Area means Any."""
	routing = routing or loadRouting()
	t = str(ticketType or "").strip().lower()
	a = str(area or "").strip().lower()
	best, bestScore, bestIdx = None, -1, -1
	for i, r in enumerate(routing.get("rules") or []):
		rt, ra = r["type"].lower(), r["area"].lower()
		if (rt and rt != t) or (ra and ra != a):
			continue
		score = (2 if rt else 0) + (1 if ra else 0)
		if score > bestScore:
			best, bestScore, bestIdx = r, score, i
	if best is None:
		return _route(routing.get("default"), -1, "Default")
	match = {3: "Type + Area", 2: "Type", 1: "Area", 0: "Any"}[bestScore]
	return _route(best, bestIdx, match)


def destinationFor(ticketType, tagPath=""):
	"""Destination name for a selection ('Monday' / 'Oracle'), '' on error."""
	try:
		return resolve(ticketType, areaOf(tagPath))["destination"]
	except Exception:
		return ""


def routeLabel(ticketType, tagPath="", rev=None):
	"""Ticket form hint: where this selection goes ('' until a type is picked)."""
	if not str(ticketType or "").strip():
		return ""
	dest = destinationFor(ticketType, tagPath)
	if not dest:
		return ""
	text = "Sends To " + ("Oracle (Queued Until Connected)" if dest == "Oracle" else dest)
	try:
		if dryRun():
			text += " - Dry Run, Nothing Is Sent"
	except Exception:
		pass
	return text


# ------------------------------------------------------------------------------------------------ outbox

def _outbox(ticket, route, status, externalId=""):
	payload = {"title": ticket.get("title"), "tagPath": ticket.get("tagPath"), "viewName": ticket.get("viewName"),
			   "reporter": ticket.get("reporter"), "email": ticket.get("email"), "priority": ticket.get("priority"),
			   "priorityLabel": _priority_label(ticket.get("priority")), "type": ticket.get("type"),
			   "area": ticket.get("area"),
			   "sections": [{"label": l, "text": t} for l, t in (ticket.get("sections") or [])]}
	routeText = "%s (%s%s)" % (route["destination"], route["match"],
							   (", rule %d" % (route["rule"] + 1)) if route["rule"] >= 0 else "")
	if route["destination"] == "Monday":
		routeText += " board %s group %s" % (route["boardId"] or "default", route["groupId"] or "default")
	ds = system.db.runNamedQuery("TicketLogger/OutboxInsert", {
		"destination": route["destination"], "status": status, "ticketType": str(ticket.get("type") or ""),
		"priority": str(ticket.get("priority") or ""), "area": str(ticket.get("area") or ""),
		"title": str(ticket.get("title") or "")[:400], "reporter": str(ticket.get("reporter") or "")[:200],
		"username": str(ticket.get("username") or "")[:200], "viewName": str(ticket.get("viewName") or "")[:400],
		"route": routeText[:400], "payload": system.util.jsonEncode(payload), "externalId": externalId})
	return str(ds.getValueAt(0, 0)) if ds is not None and ds.getRowCount() else ""


def _validate(ticket):
	errors = []
	if not str(ticket.get("title") or "").strip():
		errors.append("Title")
	if not str(ticket.get("type") or "").strip():
		errors.append("Type")
	try:
		if int(ticket.get("priority")) not in PRIORITY_LABELS:
			errors.append("Priority")
	except Exception:
		errors.append("Priority")
	if not [1 for _, t in (ticket.get("sections") or []) if str(t or "").strip()]:
		errors.append("Details")
	if errors:
		raise Exception("Ticket is missing: %s" % ", ".join(errors))


# ------------------------------------------------------------------------------------------------ adapters

def _adapterMonday(ticket, route, dry):
	if dry:
		board, group, _, _, _ = _mondayRequest(ticket.get("title"), ticket.get("viewName"), ticket.get("reporter"),
											   ticket.get("priority"), ticket.get("email"), ticket.get("type"),
											   ticket.get("sections") or [], route["boardId"], route["groupId"])
		oid = _outbox(ticket, route, DRY_RUN_STATUS)
		return {"ok": True, "id": oid, "url": "", "status": DRY_RUN_STATUS,
				"message": "Dry Run: Would Create A Monday Item (Board %s, Group %s). Nothing Was Sent." % (board, group)}
	result = createTicket(title=ticket.get("title"), viewName=ticket.get("viewName"), reporter=ticket.get("reporter"),
						  priority=ticket.get("priority"), email=ticket.get("email"), requestType=ticket.get("type"),
						  sections=ticket.get("sections") or [], boardId=route["boardId"], groupId=route["groupId"])
	return {"ok": True, "id": result.get("id", ""), "url": result.get("url", ""), "status": "Sent",
			"message": "Sent To Monday" + (("\n" + result["url"]) if result.get("url") else "")}


def _adapterOracle(ticket, route, dry):
	"""Stub until the client's Oracle integration exists: queue the ticket in dbo.ticket_outbox."""
	oid = _outbox(ticket, route, DRY_RUN_STATUS if dry else ORACLE_PENDING)
	if dry:
		return {"ok": True, "id": oid, "url": "", "status": DRY_RUN_STATUS,
				"message": "Dry Run: Would Queue For Oracle (Outbox #%s). Nothing Was Sent." % oid}
	return {"ok": True, "id": oid, "url": "", "status": ORACLE_PENDING,
			"message": "Queued For Oracle (Not Yet Connected). Outbox #%s." % oid}


ADAPTERS = {"Monday": _adapterMonday, "Oracle": _adapterOracle}


def send(ticket):
	"""Route and dispatch one ticket (dict, see the module header). Returns the adapter result plus destination,
	match and dryRun. Raises with an operator-readable message on failure."""
	ticket = dict(ticket or {})
	if not shared.Security.require('TicketLogger', 'Use', ticket.get("title")):
		raise Exception("Ticket Logger is not permitted for your role (Roles & Permissions)")
	ticket.setdefault("tagPath", ticket.get("title"))
	ticket["area"] = ticket.get("area") or areaOf(ticket.get("tagPath"))
	_validate(ticket)
	route = resolve(ticket.get("type"), ticket["area"])
	adapter = ADAPTERS.get(route["destination"])
	if adapter is None:
		raise Exception("No adapter for destination %s" % route["destination"])
	dry = dryRun()
	result = adapter(ticket, route, dry)
	result.update({"destination": route["destination"], "match": route["match"], "dryRun": dry})
	_log.info("Ticket '%s' (%s / %s) by %s -> %s via %s%s: %s" % (ticket.get("title"), ticket.get("type"),
		ticket["area"] or "-", ticket.get("username") or ticket.get("reporter"), route["destination"], route["match"],
		" [dry run]" if dry else "", result.get("status")))
	return result


# ------------------------------------------------------------------------------------------------ settings
# TicketLogger/Settings (OneShot only). Reads return empty for other sessions; writes raise.

def canConfigure(session=None):
	return shared.Security.can('TicketLogger', 'Settings', session)


def requireSettings(what=""):
	if not shared.Security.require('TicketLogger', 'Settings', what):
		raise Exception("Ticket Logger Settings is not permitted for your role (Roles & Permissions)")


def typeNames():
	ds = system.tag.readBlocking([TYPES_TAG])[0].value
	out = []
	if ds is not None:
		for i in range(ds.getRowCount()):
			out.append(str(ds.getValueAt(i, "Type")))
	return out


def areaNames():
	"""Areas under [default]Boars_Head/<Site>/ (one level), sorted, for the routing editor."""
	out = set()
	try:
		for site in system.tag.browse("[default]" + DEVICE_ROOT, {"tagType": "Folder"}).getResults():
			for a in system.tag.browse(str(site["fullPath"]), {"tagType": "Folder"}).getResults():
				out.add(str(a["name"]))
	except Exception:
		pass
	return sorted(out)


def routingForView(rev=None, *more):
	"""Settings views: routing, dry run, dropdown options, outbox counts ({} without TicketLogger/Settings; rev only
	re-triggers the runScript binding)."""
	if not canConfigure():
		return {}
	counts = outboxCounts()
	types = typeNames()
	areas = areaNames()
	return {"routing": loadRouting(), "dryRun": dryRun(), "types": types, "areas": areas,
			"typeOptions": [{"value": "", "label": "Any Type"}] + [{"value": t, "label": t} for t in types],
			"areaOptions": [{"value": "", "label": "Any Area"}] + [{"value": a, "label": a} for a in areas],
			"destOptions": [{"value": d, "label": d} for d in DESTINATIONS],
			"oraclePending": counts.get("Oracle|" + ORACLE_PENDING, 0),
			"dryRunCount": sum(v for k, v in counts.items() if k.endswith("|" + DRY_RUN_STATUS))}


def outboxCounts():
	out = {}
	try:
		ds = system.db.runNamedQuery("TicketLogger/OutboxCounts", {})
		for i in range(ds.getRowCount()):
			out["%s|%s" % (ds.getValueAt(i, "destination"), ds.getValueAt(i, "status"))] = int(ds.getValueAt(i, "n"))
	except Exception as e:
		_log.warn("outbox counts: %s" % e)
	return out


def _summary(routing):
	parts = []
	for r in routing["rules"]:
		parts.append("%s/%s>%s%s" % (r["type"] or "Any", r["area"] or "Any", r["destination"],
			(" %s:%s" % (r["boardId"] or "-", r["groupId"] or "-")) if r["destination"] == "Monday" and
			(r["boardId"] or r["groupId"]) else ""))
	d = routing["default"]
	return "Default %s; %d Rules: %s" % (d["destination"], len(routing["rules"]), ", ".join(parts))


def plain(obj):
	"""Perspective property / binding / runScript argument structures -> plain Python (dict / list / str)."""
	if obj is None:
		return None
	if isinstance(obj, (basestring, int, long, float, bool)):
		return obj
	if isinstance(obj, (dict, list, tuple)):
		return _unq(obj)
	try:
		from com.google.gson import JsonElement
		if isinstance(obj, JsonElement):
			return system.util.jsonDecode(obj.toString())
	except Exception:
		pass
	try:
		from com.inductiveautomation.ignition.common.gson import JsonElement as IaJsonElement
		if isinstance(obj, IaJsonElement):
			return system.util.jsonDecode(obj.toString())
	except Exception:
		pass
	# runScript arguments arrive as Java maps / arrays of QualifiedValues; _unq unwraps them (and anything else
	# through a JSON round trip)
	return _unq(obj)


def _unq(x):
	"""Deep copy without QualifiedValue wrappers (Java objects or their JSON {"value", "quality", "timestamp"})."""
	if x is None or isinstance(x, (basestring, int, long, float, bool)):
		return x
	if hasattr(x, "getQuality") and hasattr(x, "getValue"):
		return _unq(x.getValue())
	if isinstance(x, dict):
		if "value" in x and "quality" in x and len(x) <= 3:
			return _unq(x["value"])
		return dict((unicode(k), _unq(v)) for k, v in x.items())
	if isinstance(x, (list, tuple)):
		return [_unq(v) for v in x]
	try:
		from java.util import Map, Collection
		if isinstance(x, Map):
			return dict((unicode(k), _unq(x.get(k))) for k in x.keySet())
		if isinstance(x, Collection):
			return [_unq(v) for v in x]
	except Exception:
		pass
	try:
		return _unq(system.util.jsonDecode(system.util.jsonEncode(x)))
	except Exception:
		return x


def _destText(r):
	if r["destination"] != "Monday":
		return u"\u2014"
	if not r["boardId"] and not r["groupId"]:
		return "Integration Default"
	return "%s / %s" % (r["boardId"] or "Default", r["groupId"] or "Default")


def ruleRows(rules, sel=None):
	"""Routing editor table rows (blank Type / Area shown as Any)."""
	rows = []
	for i, r in enumerate(normalize({"rules": plain(rules) or []})["rules"]):
		rows.append({"idx": i + 1, "type": r["type"] or "Any", "area": r["area"] or "Any",
					 "destination": r["destination"], "boardGroup": _destText(r)})
	return rows


def applyRule(draft, sel, edit):
	"""Routing editor: put the edited rule at index sel (-1 = append). Returns [draft, sel, error]; nothing is saved."""
	d = normalize(plain(draft))
	e = _route(plain(edit) or {})
	rule = {k: e[k] for k in ("type", "area", "destination", "boardId", "groupId")}
	if rule["destination"] != "Monday":
		rule["boardId"] = rule["groupId"] = ""
	if not rule["type"] and not rule["area"]:
		return [d, sel, "Pick A Type Or An Area (A Rule For Any Type And Any Area Is The Default Destination)"]
	try:
		sel = int(sel)
	except Exception:
		sel = -1
	for i, r in enumerate(d["rules"]):
		if i != sel and r["type"].lower() == rule["type"].lower() and r["area"].lower() == rule["area"].lower():
			return [d, sel, "Rule %d Already Covers %s / %s" % (i + 1, rule["type"] or "Any Type",
																 rule["area"] or "Any Area")]
	if 0 <= sel < len(d["rules"]):
		d["rules"][sel] = rule
	else:
		d["rules"].append(rule)
		sel = len(d["rules"]) - 1
	return [d, sel, ""]


def removeRule(draft, sel):
	d = normalize(plain(draft))
	try:
		sel = int(sel)
	except Exception:
		sel = -1
	if 0 <= sel < len(d["rules"]):
		del d["rules"][sel]
	return d


def isDirty(draft, saved):
	if draft is None or saved is None:
		return False
	return normalize(plain(draft)) != normalize(plain(saved))


def saveRouting(doc, viewName=None):
	"""Validate and write the routing document; OpsAudit 'Ticket Routing Changed' (rules summary, no secrets).
	Returns [ok, message]."""
	requireSettings("routing")
	routing = normalize(doc)
	raw = _toPy(doc) or {}
	for r in list(raw.get("rules") or []) + [raw.get("default") or {}]:
		dest = str((r or {}).get("destination") or "").strip()
		if dest and dest not in DESTINATIONS:
			return [False, "Unknown destination %s" % dest]
	seen = set()
	for i, r in enumerate(routing["rules"]):
		key = (r["type"].lower(), r["area"].lower())
		if key in seen:
			return [False, "Rule %d repeats Type %s / Area %s" % (i + 1, r["type"] or "Any", r["area"] or "Any")]
		seen.add(key)
		if not r["type"] and not r["area"]:
			return [False, "Rule %d matches everything - use the Default Destination instead" % (i + 1)]
	old = loadRouting()
	if old == routing:
		return [True, "No Changes"]
	system.tag.writeBlocking([ROUTING_TAG], [system.util.jsonEncode(routing)])
	shared.Audit.logEvent("Ticket Routing Changed", "Ticket Logger Routing", _summary(routing)[:900],
						  tagPath=ROUTING_TAG, viewName=viewName)
	return [True, "Routing Saved"]


def setDryRun(on, viewName=None):
	requireSettings("dry run")
	on = bool(on)
	if dryRun() == on:
		return
	system.tag.writeBlocking([DRY_RUN_TAG], [on])
	shared.Audit.logEvent("Ticket Logger Dry Run", "Ticket Logger Dry Run", "On" if on else "Off",
						  tagPath=DRY_RUN_TAG, viewName=viewName)
