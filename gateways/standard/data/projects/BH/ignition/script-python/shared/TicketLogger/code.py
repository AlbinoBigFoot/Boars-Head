# Monday.com Ticket Logger — replaces Lightspeed HBT.AzureRESTAPI for BH.

API_URL = "https://api.monday.com/v2"
API_VERSION = "2026-07"

PRIORITY_LABELS = {
	1: "Critical",
	2: "High",
	3: "Medium",
	4: "Low",
}

_TAG_PREFIX = "[default]_Config/Monday/"


def _tag(path):
	qv = system.tag.readBlocking([_TAG_PREFIX + path])[0]
	if qv is None:
		return None
	try:
		if not qv.quality.isGood():
			return None
	except:
		pass
	return qv.value


def _col(name, fallback):
	v = _tag("Columns/" + name)
	return v if v else fallback


def _token():
	t = _tag("API Token")
	if t is None or str(t).strip() == "":
		raise Exception("Monday API Token missing at %sAPI Token" % _TAG_PREFIX)
	return str(t).strip()


def graphql(query, variables=None):
	"""POST GraphQL to monday.com. Returns data dict; raises on HTTP/GraphQL errors."""
	client = system.net.httpClient(redirect_policy="ALWAYS")
	body = {"query": query}
	if variables is not None:
		body["variables"] = variables
	resp = client.post(
		url=API_URL,
		headers={
			"Authorization": _token(),
			"Content-Type": "application/json",
			"API-Version": API_VERSION,
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


def _build_description(title, viewName, reporter, expectedResult, actualResult, stepsToRecreate):
	parts = [
		"Tag Path: %s" % (title or ""),
		"View Path: %s" % (viewName or ""),
		"Created By: %s" % (reporter or ""),
		"",
		"Expected Result:",
		expectedResult or "",
		"",
		"Actual Result:",
		actualResult or "",
		"",
		"Steps to Recreate:",
		stepsToRecreate or "",
	]
	text = "\n".join(parts)
	# long_text soft limit ~2000; keep column under that, full body goes to update
	if len(text) > 1900:
		return text[:1890] + "\n…(see update for full text)", text
	return text, text


def createTicket(
	title,
	viewName,
	reporter,
	priority,
	expectedResult,
	actualResult,
	stepsToRecreate,
	email=None,
	requestType="Issue",
):
	"""
	Create a Monday Tickets board item.

	Returns dict: { "id": str, "url": str, "name": str }
	Raises on failure.
	"""
	boardId = _tag("Board Id")
	if boardId is None or str(boardId).strip() == "":
		raise Exception("Monday Board Id not configured")
	groupId = _tag("Group Id") or "topics"

	colDesc = _col("Description", "long_text7")
	colEmp = _col("Employee Name", "text")
	colStatus = _col("Status", "status95")
	colPri = _col("Priority", "priority")
	colType = _col("Request Type", "request_type")
	colDate = _col("Creation Date", "date")
	colEmail = _col("Email", "email")

	shortDesc, fullDesc = _build_description(
		title, viewName, reporter, expectedResult, actualResult, stepsToRecreate
	)

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
		"boardId": str(boardId),
		"groupId": str(groupId),
		"itemName": (title or "Untitled ticket")[:255],
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
