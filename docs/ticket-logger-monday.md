# Ticket Logger → Monday.com (design)

Replace Azure DevOps work-item creation used by Perspective **Ticket Logger** (`98_Configuration/TicketLogger`) with Monday GraphQL.

**Convention:** every new Perspective view must ship with Ticket Logger context-menu wiring (`ticketLog` → `shared.Alerts.contextMenuTicketLog`). See `.cursor/rules/perspective-ticket-logger.mdc`.

**Sources:** Monday platform API docs (auth, create_item, column types, updates, files, rate limits); Lightspeed `HBT.AzureRESTAPI`; BH `TicketLogger/view.json`.

---

## Current ADO behavior (what to replace)

| Piece | Location / behavior |
| --- | --- |
| UI | `views/98_Configuration/TicketGenerator` (title: Ticket Logger) |
| Call site | Send button → `shared.AzureRESTAPI.createWorkItem(...)` then `system.db.runNamedQuery("IssueLogs/Insert", ...)` |
| Script module | **Missing in BH.** Lives in Lightspeed as `HBT.AzureRESTAPI` (port as `shared.*`, never keep `HBT`) |
| HTTP | `system.net.httpPost` to `https://dev.azure.com/{org}/{project}/_apis/wit/workitems/${type}?api-version=7.1-preview.3`, `Content-Type: application/json-patch+json`, Basic auth `username=basic`, `password=PAT` |
| Config tags | `[default]_Config/Azure Devops/{Organization,Project Name,Personal Access Token,Area Path,Iteration Path,Tags}` |
| Gate | `session.custom.TicketGenAccess` ← Connected tag + `OneShot` role |

**ADO fields sent today**

| Input | ADO field |
| --- | --- |
| Tag path (UI “title”) | `System.Title` |
| HTML: Tag Path / View Path / Created By | `System.Description` |
| Expected / Actual / Steps | `Custom.ExpectedResult`, `Custom.ActualResult`, `Custom.StepstoRecreate` |
| Priority dropdown | `Microsoft.VSTS.Common.Priority` |
| Area / Iteration / Tags (from tags) | `System.AreaPath`, `System.IterationPath`, `System.Tags` |
| workItemType | URL type (`Bug` default) |

Local SQL insert (`IssueLogs/Insert`) should stay unless product asks to drop it; only the remote create swaps to Monday.

---

## 1. Auth (Ignition-friendly)

**Recommended: personal V2 API token** for a dedicated Monday service user (or shared eng account) with write access to the ticket board.

- Header: `Authorization: <token>` (raw token; Monday docs do not require `Bearer` for personal tokens)
- Also send: `Content-Type: application/json`, `API-Version: 2026-07` (or current stable from Monday release notes)
- Permissions: mirror the token user’s board access (must be able to create items + set columns on the target board)

**OAuth / app tokens:** better for multi-tenant apps; poor fit for gateway scripts (browser consent, token storage, no refresh tokens). Skip unless BH later builds a Monday marketplace app.

**Token lifecycle:** regenerating invalidates immediately — treat like ADO PAT.

---

## 2. Minimal GraphQL

**Endpoint:** `POST https://api.monday.com/v2`  
**Files (optional):** `POST https://api.monday.com/v2/file` (multipart only)

### Discover board schema (one-time / ops)

```graphql
query ($boardIds: [ID!]) {
  boards(ids: $boardIds) {
    id
    name
    groups { id title }
    columns { id title type settings }
  }
}
```

### Create ticket

```graphql
mutation ($boardId: ID!, $itemName: String!, $columnVals: JSON!, $groupId: String) {
  create_item(
    board_id: $boardId
    group_id: $groupId
    item_name: $itemName
    column_values: $columnVals
  ) {
    id
    name
    url
  }
}
```

`column_values` is a **JSON string** (pass object via GraphQL variables so Monday receives typed JSON; with variables, pass the object and let the client encode — see Python pattern below using `system.util.jsonEncode` for the whole body).

**Column value shapes (keys = real column IDs from the board):**

| Type | Value |
| --- | --- |
| `text` | `"plain string"` |
| `long_text` | `{"text": "multi\\nline"}` (max ~2000 chars) |
| `status` / priority-as-status | `{"label": "High"}` (prefer label; labels must exist unless `create_labels_if_missing: true`) |
| `people` | `{"personsAndTeams": [{"id": 123, "kind": "person"}]}` |
| `dropdown` / tags-like | per column docs (often `{"labels": ["SCADA"]}` or ids) |

### Optional update (long repro notes)

```graphql
mutation ($itemId: ID!, $body: String!) {
  create_update(item_id: $itemId, body: $body) { id }
}
```

### Optional file

Multipart to `/v2/file` with `add_file_to_column` / `add_file_to_update`. Phase 1: skip files (Jython multipart is painful). Phase 2: only if Ticket Logger gains screenshots.

---

## 3. Board / column config (Boar’s Head)

### Live board (confirmed via Monday MCP)

| | |
| --- | --- |
| Workspace | **Service Agent Workspace** `16700086` |
| Board | **Tickets** `18423731526` ([open](https://oneshotautomation-company.monday.com/boards/18423731526)) |
| Item term | Ticket |
| Default group | `topics` — Unassigned tickets |
| Connectivity test | Item `12626840909` — `[BH Ticket Logger] Connectivity test` |

This is a **Service / AI agent** tickets board (Status + AI Status + Agent + Email), not a blank engineering backlog. Map Ignition Issue Logger fields onto these existing columns; do **not** invent parallel SCADA-only columns unless needed later.

### Column IDs (use these in `create_item`)

| Ticket Logger field | Monday column | Column id | Value shape |
| --- | --- | --- | --- |
| Title | Name | `name` | item `item_name` |
| Reporter | Employee Name | `text` | plain string |
| Expected / Actual / Steps (+ tag path, view) | Description | `long_text7` | `{"text":"..."}` (fold tag/view into body) |
| Priority 1–4 | Priority | `priority` | `{"label":"Critical\|High\|Medium\|Low"}` |
| Type (Bug ≈ Issue) | Request Type | `request_type` | `{"label":"Issue"}` (also Question, Request) |
| — | Status | `status95` | always set `{"label":"New"}` on create |
| Ticket date | Creation Date | `date` | `{"date":"YYYY-MM-DD"}` (optional time) |
| Session user email (if available) | Email | `email` | `{"email":"...","text":"..."}` **both required** |
| — | Agent | `people0` | leave empty (human/AI assign later) |
| — | AI Status | `ai_status` | leave alone (agent-managed) |
| Screenshots (later) | Attached Files | `files` | multipart file API |

### Groups (workflow)

| Group id | Title | Use from Ignition |
| --- | --- | --- |
| `topics` | Unassigned tickets | **Default** for new HMI tickets |
| `group_title` | Open tickets | After agent pickup |
| `new_group36390` | Waiting for response | — |
| `group_mm4tejv6` | AI Resolved tickets | — |
| `new_group` | Resolved tickets | — |

### Optional later columns (only if operators need them on the board)

Tag path / view name can stay inside Description for v1. If filtering in Monday becomes painful, add Text columns `Tag Path` / `View` via MCP `create_column` and store their ids under `_Config/Monday/Columns/*`.

### Where to store config (already on BH gateway)

| Value | Tag path | Live value |
| --- | --- | --- |
| API token | `[default]_Config/Monday/API Token` | set (gitignored runtime) |
| Board | `[default]_Config/Monday/Board Id` | `18423731526` |
| Default group | `[default]_Config/Monday/Group Id` | `topics` |
| Workspace | `[default]_Config/Monday/Workspace Id` | `16700086` |
| Connected | `[default]_Config/Monday/Connected` | `true` |
| Column ids | `[default]_Config/Monday/Columns/{Description,Employee Name,...}` | see table above |

**Do not** keep Azure org/project/area/iteration tags once cut over. Retarget `session.custom.TicketLogAccess` from Azure Connected → `_Config/Monday/Connected`.

---

## 4. Ignition 8.3 HTTP pattern (Jython)

Prefer `system.net.httpClient()` over legacy `httpPost` (ADO used `httpPost`).

```python
# Pseudocode for shared.TicketLogger / shared.MondayAPI
API_URL = "https://api.monday.com/v2"
API_VERSION = "2026-07"

def _token():
	# prefer env; fallback tag
	t = system.util.getEnvironmentVariable("MONDAY_API_TOKEN")
	if not t:
		t = system.tag.readBlocking(["[default]_Config/Monday/API Token"])[0].value
	return t

def graphql(query, variables=None):
	client = system.net.httpClient()
	body = {"query": query}
	if variables is not None:
		body["variables"] = variables
	resp = client.post(
		API_URL,
		headers={
			"Authorization": _token(),
			"Content-Type": "application/json",
			"API-Version": API_VERSION,
		},
		data=system.util.jsonEncode(body),
	)
	if resp.statusCode != 200:
		raise Exception("Monday HTTP %s: %s" % (resp.statusCode, resp.text))
	payload = system.util.jsonDecode(resp.text)
	if payload.get("errors"):
		raise Exception("Monday GraphQL: %s" % payload["errors"])
	return payload.get("data")
```

**Variables tip:** for `column_values`, pass a **dict** in variables (GraphQL `JSON` type). Encode the HTTP body once with `jsonEncode`; do not double-stringify unless the schema demands a string (Monday accepts JSON variables for `column_values`).

---

## 5. Errors / rate limits / permissions

| Concern | Handling |
| --- | --- |
| Auth / board access | GraphQL errors / 401 — surface alert; set Connected=false |
| Missing column / bad label | Fail create; log column IDs from discover query |
| Rate limits | Complexity (personal ~10M/min), daily calls (plan-based), minute QPS, concurrency. Response headers `RateLimit` / `retry_in_seconds`. Ticket Logger is low volume — simple retry once after sleep is enough |
| long_text > 2k | Truncate column; put full text in `create_update` |
| Validation rules (Pro+) | Required columns must be set or create fails |
| Token user leaves | Prefer service account; document regen process |

Do **not** retry immediately on rate-limit errors without waiting.

---

## 6. Interface sketch: `shared.TicketLogger`

Replace `shared.AzureRESTAPI.createWorkItem(...)` (never recreate `HBT`).

```python
# shared/TicketLogger/code.py  (conceptual)

def createTicket(
	title,                 # item name / tag path
	viewName,
	reporter,
	priority,              # UI value → severity label
	expectedResult,
	actualResult,
	stepsToRecreate,
	tagPath=None,          # optional explicit; default title
	workItemType="Bug",    # maps to status/group if configured
	attachUpdate=True,     # post create_update with full repro
):
	"""
	Returns dict: { "id": str, "url": str, "name": str }
	Raises on HTTP/GraphQL failure (caller shows Alerts).
	"""

def ping():
	"""query { me { id name } } — used to set Connected tag / health."""
```

View Send script becomes:

```python
from shared import TicketLogger
from shared import Alerts
# ... validate expectedResult ...
result = TicketLogger.createTicket(
	title=tagPathText,
	viewName=viewName,
	reporter=issuerName,
	priority=priority,
	expectedResult=expectedResult,
	actualResult=actualResult,
	stepsToRecreate=stepsToRecreate,
)
workId = result.get("id", "") if result else ""
# keep IssueLogs/Insert with work_id = Monday item id; store url if column added later
```

Keep signature close enough that TicketGenerator changes stay small; drop ADO-only args (`organization`, `projectName`, `personalAccessToken`, `areaPath`, `iterationPath`, `tags`) — read those from module config instead of the view.

---

## 7. `.env.example` checklist (placeholders only)

```bash
# Monday.com Ticket Logger (gateway scripts)
# Personal V2 API token from monday.com → Developers → API token
MONDAY_API_TOKEN=
# Numeric board id from https://monday.com/boards/{id}
MONDAY_BOARD_ID=
# Optional group id (from boards{groups{id}})
MONDAY_GROUP_ID=
# Optional API version pin
MONDAY_API_VERSION=2026-07
# Column IDs (from boards{columns{id title type}}) — leave empty to use Ignition tags instead
MONDAY_COL_TAG_PATH=
MONDAY_COL_VIEW_NAME=
MONDAY_COL_REPORTER=
MONDAY_COL_SEVERITY=
MONDAY_COL_DESCRIPTION=
MONDAY_COL_TYPE=
```

Never commit real tokens. Prefer env for the token; tags OK for board/column IDs.

---

## 8. ADO vs Monday cheat sheet

| ADO | Monday |
| --- | --- |
| PAT + Basic auth | Personal API token in `Authorization` |
| REST JSON Patch `_apis/wit/workitems` | GraphQL `create_item` on `/v2` |
| Work item type in URL | Group and/or status/dropdown column |
| `System.Title` | `item_name` |
| HTML Description + custom fields | text / long_text columns + optional `create_update` |
| Priority int | Status/dropdown label |
| Area / Iteration | Groups or drop |
| Tags string | Tags/dropdown column or omit |
| Returned `id` | Item `id` (+ `url` for UI link) |
| `system.net.httpPost` | `system.net.httpClient().post` |

---

## Implementation checklist (for next agent)

1. Create Monday board + columns; run discover query; record IDs in tags/env.
2. Add `shared/TicketLogger` (or `shared/MondayAPI` + thin TicketLogger wrapper).
3. Wire TicketGenerator Send → `TicketLogger.createTicket`; remove AzureRESTAPI import.
4. Retarget session `TicketGenAccess` to `_Config/Monday/Connected`.
5. Extend `.env.example`; document token owner + regen.
6. Keep `IssueLogs/Insert`; store Monday item id (and optionally url).
7. UAT: create item, verify columns, rate-limit/error alerts, role gate.
8. Decommission Azure DevOps tags/PAT when stable.
