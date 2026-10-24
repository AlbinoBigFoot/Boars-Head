---
title: "shared.TicketLogger"
sidebar_label: "shared.TicketLogger"
description: "Script module shared.TicketLogger: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`  
**Lines:** 640. **Functions:** 39. **Called as:** `shared.TicketLogger.<function>(...)`

## What the source says

```text
Ticket Logger (2026-10-24 ticket-routing): every logged-in user submits tickets (Roles & Permissions
TicketLogger/Use); the ticket's selection (Type, plus the Area parsed from its tag path) picks a destination from
[default]_Config/TicketLogger/Routing and send() dispatches it through that destination's adapter.

Adapter interface (ADAPTERS, keyed by destination name):
adapter(ticket, route, dryRun) -> {"ok": True, "id": str, "url": str, "status": str, "message": str}
ticket = {"title", "tagPath", "viewName", "reporter", "username", "email", "priority" (1-4), "type",
"area", "sections": [(label, text)]}
route  = {"destination", "boardId", "groupId", "rule" (index or -1), "match" ("Type + Area" | "Type" | "Area" |
"Default")}
Raise an Exception with an operator-readable message on failure. Never put credentials in the result, the
outbox payload or an audit entry.
Monday = the Monday.com Tickets board (createTicket, unchanged behaviour; a rule may override board / group).
Oracle = stub until the client integration exists: validates and queues the ticket in dbo.ticket_outbox
(status "Pending Oracle"); a later Oracle adapter / sender drains that table without UI changes.
Dry run ([default]_Config/TicketLogger/DryRun = true): no external call; the ticket is recorded in the outbox with
status "Dry Run" and its resolved destination (test routing without creating Monday items).
Settings (routing, dry run, integrations) need TicketLogger/Settings (OneShot only, a RestrictedRows row).
device-perms + ticket-routing: TicketLogger/Use on send / createTicket, TicketLogger/Settings on settings calls.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.db`, `system.net`, `system.tag`, `system.util` |
| Logger names | `BH.TicketLogger` |
| Calls modules | [shared.Audit](./shared-audit.md), [shared.Integrations](./shared-integrations.md), [shared.Security](./shared-security.md) |
| Called by modules | [shared.Integrations](./shared-integrations.md) |

<details>
<summary>Module constants (12)</summary>

| Name | Value |
|---|---|
| `API_URL` | `'https://api.monday.com/v2'` |
| `API_VERSION` | `'2026-07'` |
| `PRIORITY_LABELS` | `{1: 'Critical', 2: 'High', 3: 'Medium', 4: 'Low'}` |
| `INTEGRATION` | `'Monday'` |
| `ROUTING_TAG` | `'[default]_Config/TicketLogger/Routing'` |
| `DRY_RUN_TAG` | `'[default]_Config/TicketLogger/DryRun'` |
| `TYPES_TAG` | `'[default]_Config/TicketLogger/Types'` |
| `DESTINATIONS` | `['Monday', 'Oracle']` |
| `ORACLE_PENDING` | `'Pending Oracle'` |
| `DRY_RUN_STATUS` | `'Dry Run'` |
| `DEVICE_ROOT` | `'Boars_Head'` |
| `ADAPTERS` | `{'Monday': _adapterMonday, 'Oracle': _adapterOracle}` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_cfg`](#_cfg) (internal) | | 0 |
| [`_col`](#_col) (internal) | | 0 |
| [`_token`](#_token) (internal) | | 0 |
| [`graphql`](#graphql) | POST GraphQL to monday.com. Returns data dict; raises on HTTP/GraphQL errors. | 1 |
| [`ping`](#ping) | Return True if the Monday token can call me \{ id \}. | 0 |
| [`_priority_label`](#_priority_label) (internal) | | 0 |
| [`_build_description`](#_build_description) (internal) | sections: [(label, text)] in form order (the ticket type's fields). | 0 |
| [`_mondayRequest`](#_mondayrequest) (internal) | (boardId, groupId, itemName, column\_values, fullDesc) for create\_item; boardId / groupId '' = integration. | 0 |
| [`createTicket`](#createticket) | Create a Monday Tickets board item (the Monday adapter; behaviour unchanged since 2026-09-30). | 0 |
| [`_toPy`](#_topy) (internal) | JSON text, plain Python or a Perspective / Java structure -&gt; plain Python. | 0 |
| [`_route`](#_route) (internal) | | 0 |
| [`normalize`](#normalize) | Routing document -&gt; \{"default": route, "rules": [route]\} (unknown destinations fall back to Monday). | 2 |
| [`loadRouting`](#loadrouting) | | 0 |
| [`dryRun`](#dryrun) | | 0 |
| [`areaOf`](#areaof) | Area of a device tag path ([default]Boars\_Head/&lt;Site&gt;/&lt;Area&gt;/...), '' when the path is not a device path. | 0 |
| [`resolve`](#resolve) | The route for a selection: the most specific matching rule (Type + Area, then Type, then Area; table order on | 0 |
| [`destinationFor`](#destinationfor) | Destination name for a selection ('Monday' / 'Oracle'), '' on error. | 0 |
| [`routeLabel`](#routelabel) | Ticket form hint: where this selection goes ('' until a type is picked). | 1 |
| [`_outbox`](#_outbox) (internal) | | 0 |
| [`_validate`](#_validate) (internal) | | 0 |
| [`_adapterMonday`](#_adaptermonday) (internal) | | 0 |
| [`_adapterOracle`](#_adapteroracle) (internal) | Stub until the client's Oracle integration exists: queue the ticket in dbo.ticket\_outbox. | 0 |
| [`send`](#send) | Route and dispatch one ticket (dict, see the module header). Returns the adapter result plus destination, | 1 |
| [`canConfigure`](#canconfigure) | | 0 |
| [`requireSettings`](#requiresettings) | | 0 |
| [`typeNames`](#typenames) | | 0 |
| [`areaNames`](#areanames) | Areas under [default]Boars\_Head/&lt;Site&gt;/ (one level), sorted, for the routing editor. | 0 |
| [`routingForView`](#routingforview) | Settings views: routing, dry run, dropdown options, outbox counts (\{\} without TicketLogger/Settings; rev only | 2 |
| [`outboxCounts`](#outboxcounts) | | 0 |
| [`_summary`](#_summary) (internal) | | 0 |
| [`plain`](#plain) | Perspective property / binding / runScript argument structures -&gt; plain Python (dict / list / str). | 1 |
| [`_unq`](#_unq) (internal) | Deep copy without QualifiedValue wrappers (Java objects or their JSON \{"value", "quality", "timestamp"\}). | 0 |
| [`_destText`](#_desttext) (internal) | | 0 |
| [`ruleRows`](#rulerows) | Routing editor table rows (blank Type / Area shown as Any). | 1 |
| [`applyRule`](#applyrule) | Routing editor: put the edited rule at index sel (-1 = append). Returns [draft, sel, error]; nothing is saved. | 1 |
| [`removeRule`](#removerule) | | 1 |
| [`isDirty`](#isdirty) | | 1 |
| [`saveRouting`](#saverouting) | Validate and write the routing document; OpsAudit 'Ticket Routing Changed' (rules summary, no secrets). | 1 |
| [`setDryRun`](#setdryrun) | | 1 |

### \_cfg {#_cfg}

```python
def _cfg(integration=INTEGRATION)
```
Line 43 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `_mondayRequest`, `graphql`

### \_col {#_col}

```python
def _col(settings, name, fallback)
```
Line 50 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `_mondayRequest`

### \_token {#_token}

```python
def _token(integration=INTEGRATION)
```
Line 55 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `graphql`

### graphql {#graphql}

```python
def graphql(query, variables=None, integration=INTEGRATION)
```
Line 62 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
POST GraphQL to monday.com. Returns data dict; raises on HTTP/GraphQL errors.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Integrations._testMonday` | script | |

Used inside the module by: `createTicket`, `ping`

### ping {#ping}

```python
def ping()
```
Line 89 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Return True if the Monday token can call me { id }.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### \_priority\_label {#_priority_label}

```python
def _priority_label(priority)
```
Line 99 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `_mondayRequest`, `_outbox`

### \_build\_description {#_build_description}

```python
def _build_description(title, viewName, reporter, sections)
```
Line 107 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
sections: [(label, text)] in form order (the ticket type's fields).
```

Used inside the module by: `_mondayRequest`

### \_mondayRequest {#_mondayrequest}

```python
def _mondayRequest(title, viewName, reporter, priority, email, requestType, sections, boardId=None, groupId=None)
```
Line 123 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
(boardId, groupId, itemName, column_values, fullDesc) for create_item; boardId / groupId '' = integration.
```

Used inside the module by: `_adapterMonday`, `createTicket`

### createTicket {#createticket}

```python
def createTicket(title, viewName, reporter, priority, expectedResult='', actualResult='', stepsToRecreate='', email=None, requestType='Issue', sections=None, boardId=None, groupId=None)
```
Line 154 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Create a Monday Tickets board item (the Monday adapter; behaviour unchanged since 2026-09-30).

sections: [(label, text)] from the ticket type's fields (_Config/TicketLogger/Types); without it the classic
Expected / Actual / Steps trio is used. boardId / groupId: routing rule override ('' = integration settings).
Returns dict: { "id": str, "url": str, "name": str }
Raises on failure.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_adapterMonday`

### \_toPy {#_topy}

```python
def _toPy(value)
```
Line 228 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
JSON text, plain Python or a Perspective / Java structure -> plain Python.
```

Used inside the module by: `normalize`, `saveRouting`

### \_route {#_route}

```python
def _route(d, rule=-1, match='Default')
```
Line 245 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `applyRule`, `normalize`, `resolve`

### normalize {#normalize}

```python
def normalize(doc)
```
Line 256 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Routing document -> {"default": route, "rules": [route]} (unknown destinations fall back to Monday).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketRouting` | view | `root/Content/ActionBar/Save event component.onActionPerformed` |
| `98_Configuration/TicketRouting` | view | `root/Content/Rules event component.onRowClick` |

Used inside the module by: `applyRule`, `isDirty`, `loadRouting`, `removeRule`, `ruleRows`, `saveRouting`

### loadRouting {#loadrouting}

```python
def loadRouting()
```
Line 270 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `resolve`, `routingForView`, `saveRouting`

### dryRun {#dryrun}

```python
def dryRun()
```
Line 276 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `routeLabel`, `routingForView`, `send`, `setDryRun`

### areaOf {#areaof}

```python
def areaOf(tagPath)
```
Line 281 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Area of a device tag path ([default]Boars_Head/<Site>/<Area>/...), '' when the path is not a device path.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `destinationFor`, `send`

### resolve {#resolve}

```python
def resolve(ticketType, area='', routing=None)
```
Line 292 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
The route for a selection: the most specific matching rule (Type + Area, then Type, then Area; table order on
a tie), else the default. A rule's blank Type / Area means Any.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `destinationFor`, `send`

### destinationFor {#destinationfor}

```python
def destinationFor(ticketType, tagPath='')
```
Line 312 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Destination name for a selection ('Monday' / 'Oracle'), '' on error.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `routeLabel`

### routeLabel {#routelabel}

```python
def routeLabel(ticketType, tagPath='', rev=None)
```
Line 320 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Ticket form hint: where this selection goes ('' until a type is picked).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketLogger` | view | `binding custom.route` |

### \_outbox {#_outbox}

```python
def _outbox(ticket, route, status, externalId='')
```
Line 338 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `_adapterMonday`, `_adapterOracle`

### \_validate {#_validate}

```python
def _validate(ticket)
```
Line 357 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `send`

### \_adapterMonday {#_adaptermonday}

```python
def _adapterMonday(ticket, route, dry)
```
Line 376 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

### \_adapterOracle {#_adapteroracle}

```python
def _adapterOracle(ticket, route, dry)
```
Line 391 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Stub until the client's Oracle integration exists: queue the ticket in dbo.ticket_outbox.
```

### send {#send}

```python
def send(ticket)
```
Line 404 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Route and dispatch one ticket (dict, see the module header). Returns the adapter result plus destination,
match and dryRun. Raises with an operator-readable message on failure.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketLogger` | view | `root/Buttons/SendButton event dom.onClick` |

### canConfigure {#canconfigure}

```python
def canConfigure(session=None)
```
Line 429 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `routingForView`

### requireSettings {#requiresettings}

```python
def requireSettings(what='')
```
Line 433 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `saveRouting`, `setDryRun`

### typeNames {#typenames}

```python
def typeNames()
```
Line 438 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `routingForView`

### areaNames {#areanames}

```python
def areaNames()
```
Line 447 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Areas under [default]Boars_Head/<Site>/ (one level), sorted, for the routing editor.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `routingForView`

### routingForView {#routingforview}

```python
def routingForView(rev=None, *more)
```
Line 459 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Settings views: routing, dry run, dropdown options, outbox counts ({} without TicketLogger/Settings; rev only
re-triggers the runScript binding).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketLoggerSettings` | view | `binding custom.data` |
| `98_Configuration/TicketRouting` | view | `binding custom.data` |

### outboxCounts {#outboxcounts}

```python
def outboxCounts()
```
Line 475 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `routingForView`

### \_summary {#_summary}

```python
def _summary(routing)
```
Line 486 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `saveRouting`

### plain {#plain}

```python
def plain(obj)
```
Line 496 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Perspective property / binding / runScript argument structures -> plain Python (dict / list / str).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketRouting` | view | `root/Content/ActionBar/Discard event component.onActionPerformed` |

Used inside the module by: `_toPy`, `applyRule`, `isDirty`, `removeRule`, `ruleRows`

### \_unq {#_unq}

```python
def _unq(x)
```
Line 521 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Deep copy without QualifiedValue wrappers (Java objects or their JSON {"value", "quality", "timestamp"}).
```

Used inside the module by: `_toPy`, `plain`

### \_destText {#_desttext}

```python
def _destText(r)
```
Line 547 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

Used inside the module by: `ruleRows`

### ruleRows {#rulerows}

```python
def ruleRows(rules, sel=None)
```
Line 555 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Routing editor table rows (blank Type / Area shown as Any).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketRouting` | view | `root/Content/Rules binding props.data` |

### applyRule {#applyrule}

```python
def applyRule(draft, sel, edit)
```
Line 564 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Routing editor: put the edited rule at index sel (-1 = append). Returns [draft, sel, error]; nothing is saved.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketRouting` | view | `root/Content/Editor/Buttons/Apply event component.onActionPerformed` |

### removeRule {#removerule}

```python
def removeRule(draft, sel)
```
Line 589 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketRouting` | view | `root/Content/Editor/Buttons/Remove event component.onActionPerformed` |

### isDirty {#isdirty}

```python
def isDirty(draft, saved)
```
Line 600 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketRouting` | view | `binding custom.dirty` |

### saveRouting {#saverouting}

```python
def saveRouting(doc, viewName=None)
```
Line 606 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

```text
Validate and write the routing document; OpsAudit 'Ticket Routing Changed' (rules summary, no secrets).
Returns [ok, message].
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketRouting` | view | `root message handler tlRoutingSave` |

### setDryRun {#setdryrun}

```python
def setDryRun(on, viewName=None)
```
Line 633 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TicketLogger/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `98_Configuration/TicketLoggerSettings` | view | `root/Content/Destinations/DryRun/Head/Toggle event component.onActionPerformed` |
