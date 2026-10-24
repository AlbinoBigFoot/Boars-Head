---
title: "shared.OutOfService"
sidebar_label: "shared.OutOfService"
description: "Script module shared.OutOfService: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`  
**Lines:** 352. **Functions:** 19. **Called as:** `shared.OutOfService.<function>(...)`

## What the source says

```text

Docs:
docs/out-of-service.md.

Every Take Out Of Service / Return To Service / comment goes through here, on the gateway:
permission  shared.Security (Roles & Permissions OutOfService/Set, OutOfService/Comment) from the calling session
memo        at least MIN_TEXT characters after trimming (the dialog checks too; this is the real check)
who / when  session.props.auth.user + the gateway clock (never client-supplied params)
log         dbo.oos_record / dbo.oos_comment (sql/out_of_service_log.sql) through named queries OutOfService/*
tag         <device>.Enabled (the UDT instance's enabled property = the out-of-service flag)
audit       shared.Audit.logEvent -> OpsAudit (ops_audit_events) with old/new value, reason and memo
Order: the DB row is written inside a transaction, then the tag; the transaction commits only when the tag write
read back as written, otherwise it rolls back (and a written tag is put back), so the log and the tag agree.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.db`, `system.perspective`, `system.tag`, `system.util` |
| Logger names | `shared.OutOfService` |
| Calls modules | [shared.Audit](./shared-audit.md), [shared.Security](./shared-security.md) |

<details>
<summary>Module constants (14)</summary>

| Name | Value |
|---|---|
| `DB` | `'ignition'` |
| `NQ` | `'OutOfService/'` |
| `MIN_TEXT` | `10` |
| `MAX_TEXT` | `2000` |
| `REASONS` | `['Maintenance', 'Repair', 'Awaiting Parts', 'Seasonal', '...` |
| `COMMENT_STATUSES` | `['In Progress', 'Awaiting Parts', 'On Hold', 'Ready To Re...` |
| `OPEN_STATUS` | `'Out Of Service'` |
| `RETURNED_STATUS` | `'Returned'` |
| `BACKFILL_USER` | `'system'` |
| `BACKFILL_NAME` | `'Unknown (Before Logging)'` |
| `BACKFILL_MEMO` | `'Taken out of service before the Out Of Service log exist...` |
| `POPUP_ID` | `'oosDialog'` |
| `POPUP_VIEW` | `'01_Popups/00_Faceplates/Alerts/OutOfService'` |
| `LOG_ROUTE` | `'/operations/out-of-service'` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_Refused`](#_refused) (internal) | A request the user can fix (shown in the dialog), not a fault. | 0 |
| [`_text`](#_text) (internal) | | 0 |
| [`_user`](#_user) (internal) | (username, display name) of the session's logged-in user; ('', '') when not logged in. | 0 |
| [`_device`](#_device) (internal) | \{tagPath, name, type, site, area\} for a device UDT instance (typeId Devices/\*), else None. | 0 |
| [`_enabled`](#_enabled) (internal) | | 0 |
| [`_setEnabled`](#_setenabled) (internal) | Write &lt;device&gt;.Enabled and read it back; raises when it did not take. | 0 |
| [`_query`](#_query) (internal) | | 0 |
| [`_openRecordId`](#_openrecordid) (internal) | | 0 |
| [`_insertRecord`](#_insertrecord) (internal) | | 0 |
| [`_closeRecord`](#_closerecord) (internal) | | 0 |
| [`_target`](#_target) (internal) | | 0 |
| [`_audit`](#_audit) (internal) | | 0 |
| [`_notify`](#_notify) (internal) | Refresh the log page / header badge in this session (other sessions poll). | 0 |
| [`_rebuild`](#_rebuild) (internal) | Device tables drop / regain the device right away (shared.Overview via \_Config/Rebuild). | 0 |
| [`_checkText`](#_checktext) (internal) | | 0 |
| [`openDialog`](#opendialog) | Open the memo dialog for a device (right-click menu, OOS log page). takeOut None = from the device's state. | 10 |
| [`setOutOfService`](#setoutofservice) | Take a device out of service (takeOut True) or return it, with the memo. Returns \{ok, error, recordId\}. | 10 |
| [`historyPage`](#historypage) | Log page URL filtered to one device: route /operations/out-of-service/:device, device = the tag path without | 0 |
| [`openHistory`](#openhistory) | Out Of Service History (device right-click menu, log page Device History): the log page for one device. | 10 |
| [`addComment`](#addcomment) | Comment (and optional status change) on a record. OutOfService/Comment. Returned records take comments but no | 1 |

### \_Refused {#_refused}

```python
class _Refused
```
Line 32 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
A request the user can fix (shown in the dialog), not a fault.
```

Used inside the module by: `_checkText`, `addComment`, `setOutOfService`

### \_text {#_text}

```python
def _text(v)
```
Line 37 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `_device`, `_user`, `addComment`, `historyPage`, `setOutOfService`

### \_user {#_user}

```python
def _user(session)
```
Line 46 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
(username, display name) of the session's logged-in user; ('', '') when not logged in.
```

Used inside the module by: `addComment`, `setOutOfService`

### \_device {#_device}

```python
def _device(tagPath)
```
Line 66 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
{tagPath, name, type, site, area} for a device UDT instance (typeId Devices/*), else None.
```

Used inside the module by: `openDialog`, `openHistory`, `setOutOfService`

### \_enabled {#_enabled}

```python
def _enabled(tp)
```
Line 91 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `_setEnabled`, `openDialog`, `setOutOfService`

### \_setEnabled {#_setenabled}

```python
def _setEnabled(tp, value)
```
Line 96 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Write <device>.Enabled and read it back; raises when it did not take.
```

Used inside the module by: `setOutOfService`

### \_query {#_query}

```python
def _query(name, params, tx=None)
```
Line 108 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `_closeRecord`, `_insertRecord`, `_openRecordId`, `addComment`

### \_openRecordId {#_openrecordid}

```python
def _openRecordId(tp, tx=None)
```
Line 114 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `setOutOfService`

### \_insertRecord {#_insertrecord}

```python
def _insertRecord(dev, user, display, now, reason, memo, backfill, tx)
```
Line 119 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `setOutOfService`

### \_closeRecord {#_closerecord}

```python
def _closeRecord(recordId, user, display, now, memo, tx)
```
Line 127 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `setOutOfService`

### \_target {#_target}

```python
def _target(tp)
```
Line 134 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `_audit`

### \_audit {#_audit}

```python
def _audit(action, tp, value, viewName)
```
Line 141 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `addComment`, `setOutOfService`

### \_notify {#_notify}

```python
def _notify(payload)
```
Line 148 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Refresh the log page / header badge in this session (other sessions poll).
```

Used inside the module by: `addComment`, `setOutOfService`

### \_rebuild {#_rebuild}

```python
def _rebuild()
```
Line 156 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Device tables drop / regain the device right away (shared.Overview via _Config/Rebuild).
```

Used inside the module by: `setOutOfService`

### \_checkText {#_checktext}

```python
def _checkText(text, what)
```
Line 164 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

_No docstring._

Used inside the module by: `addComment`, `setOutOfService`

### openDialog {#opendialog}

```python
def openDialog(tagPath, viewName='', takeOut=None)
```
Line 171 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Open the memo dialog for a device (right-click menu, OOS log page). takeOut None = from the device's state.
```

<details>
<summary>Called from 10 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `root/Content/Detail/Record/Body/Actions/Return event component.onActionPerformed` |
| `02_Components/01_Devices/Compressor` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/CoolingTower` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Evaporator` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/ExhaustFan` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/LTU` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Pump` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Sensor` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/SolenoidValve` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Tank` | view | `root message handler oosToggle` |
</details>

### setOutOfService {#setoutofservice}

```python
def setOutOfService(session, tagPath, takeOut, reason, memo, viewName='')
```
Line 192 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Take a device out of service (takeOut True) or return it, with the memo. Returns {ok, error, recordId}.

session is the calling script's self.session (gateway side). Everything is re-checked here: permission
OutOfService/Set, memo length, reason, the device, its current state.
```

<details>
<summary>Called from 10 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/Alerts/OutOfService` | view | `dialog/footer/Confirm event component.onActionPerformed` |
| `02_Components/01_Devices/Compressor` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/CoolingTower` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Evaporator` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/ExhaustFan` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/LTU` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Pump` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Sensor` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/SolenoidValve` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Tank` | view | `root message handler oosToggle` |
</details>

### historyPage {#historypage}

```python
def historyPage(tagPath)
```
Line 281 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Log page URL filtered to one device: route /operations/out-of-service/:device, device = the tag path without
the provider with '/' -> '~' (the log view turns it back).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `openHistory`

### openHistory {#openhistory}

```python
def openHistory(tagPath)
```
Line 290 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Out Of Service History (device right-click menu, log page Device History): the log page for one device.
```

<details>
<summary>Called from 10 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `root/Content/Detail/Record/Body/Actions/History event component.onActionPerformed` |
| `02_Components/01_Devices/Compressor` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/CoolingTower` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Evaporator` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/ExhaustFan` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/LTU` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Pump` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Sensor` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/SolenoidValve` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Tank` | view | `root message handler oosHistory` |
</details>

### addComment {#addcomment}

```python
def addComment(session, recordId, status, comment)
```
Line 298 of `gateways/standard/data/projects/BH/ignition/script-python/shared/OutOfService/code.py`.

```text
Comment (and optional status change) on a record. OutOfService/Comment. Returned records take comments but no
status change. Returns {ok, error}.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `root/Content/Detail/AddComment/Body/Foot/Add event component.onActionPerformed` |
