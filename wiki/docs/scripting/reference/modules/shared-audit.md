---
title: "shared.Audit"
sidebar_label: "shared.Audit"
description: "Script module shared.Audit: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`  
**Lines:** 289. **Functions:** 9. **Called as:** `shared.Audit.<function>(...)`

## What the source says

```text
OPS Audit helpers for Perspective writable values.

Central write path for AnalogValue / Control Numeric (and later any
writable view field). Records into the OpsAudit profile table
ops_audit_events with every configured column populated.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag`, `system.util` |
| Logger names | `shared.Audit` |
| Calls modules | [shared.Enums](./shared-enums.md), [shared.PlcWriteLock](./shared-plcwritelock.md), [shared.Security](./shared-security.md) |
| Called by modules | [shared.AlarmConfig](./shared-alarmconfig.md), [shared.Alerts](./shared-alerts.md), [shared.Integrations](./shared-integrations.md), [shared.OutOfService](./shared-outofservice.md), [shared.PermissionMatrix](./shared-permissionmatrix.md), [shared.TicketLogger](./shared-ticketlogger.md), [shared.UserAdmin](./shared-useradmin.md), [shared.ValveCommands](./shared-valvecommands.md) |

<details>
<summary>Module constants (3)</summary>

| Name | Value |
|---|---|
| `OPS_AUDIT_PROFILE` | `'OpsAudit'` |
| `REBUILD_TAG` | `'[default]_Config/Rebuild'` |
| `_DEDUPE_MS` | `1000` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_value_key`](#_value_key) (internal) | | 0 |
| [`_status_code`](#_status_code) (internal) | | 0 |
| [`valuesEqual`](#valuesequal) | True when two tag values should be treated as the same (no write / no audit). | 5 |
| [`_describe`](#_describe) (internal) | | 0 |
| [`_target_from_tag_path`](#_target_from_tag_path) (internal) | Build a short target label from a tag path, e.g. EV-01 Temp SP. | 1 |
| [`_sessionMayWrite`](#_sessionmaywrite) (internal) | security-tiers: server-side write gate for Perspective sessions (gateway scripts pass). | 0 |
| [`_plcWriteBlocked`](#_plcwriteblocked) (internal) | plc-write-lock: True when shared.PlcWriteLock refuses the write (an error blocks only paths naming RCP1). | 0 |
| [`writeTag`](#writetag) | Write a tag and log the change to OpsAudit. | 15 |
| [`logEvent`](#logevent) | Record an operator action in OpsAudit without writing a tag. | 13 |

### \_value\_key {#_value_key}

```python
def _value_key(value)
```
Line 19 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

_No docstring._

Used inside the module by: `writeTag`

### \_status\_code {#_status_code}

```python
def _status_code(quality)
```
Line 30 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

_No docstring._

Used inside the module by: `writeTag`

### valuesEqual {#valuesequal}

```python
def valuesEqual(a, b)
```
Line 40 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

```text
True when two tag values should be treated as the same (no write / no audit).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `03_Elements/00_Control/AnalogInput` | view | `root/EditValue binding custom.editedValue` |
| `03_Elements/00_Control/StringInput` | view | `root/EditIcon event dom.onClick` |
| `03_Elements/00_Control/StringInput` | view | `root/EditValue event component.onActionPerformed` |
| `03_Elements/00_Control/TimeInput` | view | `root/EditValue binding custom.editedValue` |
| `shared.Alerts.confirmApplyWrite` | script | |

Used inside the module by: `writeTag`

### \_describe {#_describe}

```python
def _describe(tagPath, value)
```
Line 57 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

_No docstring._

Used inside the module by: `writeTag`

### \_target\_from\_tag\_path {#_target_from_tag_path}

```python
def _target_from_tag_path(tagPath)
```
Line 64 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

```text
Build a short target label from a tag path, e.g. EV-01 Temp SP.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.OutOfService._target` | script | |

Used inside the module by: `logEvent`, `writeTag`

### \_sessionMayWrite {#_sessionmaywrite}

```python
def _sessionMayWrite(tagPath)
```
Line 83 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

```text
security-tiers: server-side write gate for Perspective sessions (gateway scripts pass).

Writes need Faceplates/Operate; Out Of Service (<device>.Enabled) needs OutOfService/Set. Ticket Logger
integration settings (_Config/Integrations) are gated by session.custom.IntegrationAccess at the caller.
```

Used inside the module by: `writeTag`

### \_plcWriteBlocked {#_plcwriteblocked}

```python
def _plcWriteBlocked(tagPath)
```
Line 103 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

```text
plc-write-lock: True when shared.PlcWriteLock refuses the write (an error blocks only paths naming RCP1).
```

Used inside the module by: `writeTag`

### writeTag {#writetag}

```python
def writeTag(tagPath, value, label=None, viewName=None)
```
Line 113 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

```text
Write a tag and log the change to OpsAudit.

Parameters
----------
tagPath : str
        Full tag path to write.
value : any
        New value.
label : str, optional
        Unused for audit target (kept for call-site compatibility /
        confirm dialogs). Target is derived from the tag path.
viewName : str, optional
        Perspective view path for originating_system context.

Returns
-------
dict
        {ok, oldValue, newValue, quality, statusCode}
```

<details>
<summary>Called from 15 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/Alerts/Alert` | view | `dialog/footer/actionPrimary event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root message handler writeValue` |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` | view | `root message handler writeValue` |
| `02_Components/01_Devices/LTU` | view | `root/ResetRow/ResetCount event component.onActionPerformed` |
| `02_Components/02_Widgets/Safetys` | view | `root/TopRow/AlarmButtons/Reset event component.onActionPerformed` |
| `02_Components/02_Widgets/Safetys` | view | `root/TopRow/AlarmButtons/Silence event component.onActionPerformed` |
| `03_Elements/00_Control/AnalogInput` | view | `root message handler writeValue` |
| `03_Elements/00_Control/MultiStateInput` | view | `root message handler cancel` |
| `03_Elements/00_Control/MultiStateInput` | view | `root message handler writeValue` |
| `03_Elements/00_Control/MultiStateInput` | view | `root/StateSelect binding props.value` |
| `03_Elements/00_Control/StringInput` | view | `root message handler writeValue` |
| `03_Elements/00_Control/TimeInput` | view | `root message handler writeValue` |
| `03_Elements/00_Control/_Assets/Numeric` | view | `root message handler writeValue` |
| `shared.Integrations.save` | script | |
| `shared.ValveCommands._write` | script | |
</details>

### logEvent {#logevent}

```python
def logEvent(action, actionTarget, actionValue, tagPath=None, viewName=None, statusCode=0)
```
Line 245 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py`.

```text
Record an operator action in OpsAudit without writing a tag.

Used for alarm config (system.tag.configure) and ack/reset (multi-tag pulse).
```

<details>
<summary>Called from 13 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Pump/Alarms` | view | `root/AlarmBits/Body/BtnAckAll event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Alarms` | view | `root/AlarmBits/Body/BtnAckAll event component.onActionPerformed` |
| `shared.AlarmConfig.applyOverride` | script | |
| `shared.Integrations.add` | script | |
| `shared.Integrations.save` | script | |
| `shared.Integrations.setToken` | script | |
| `shared.OutOfService._audit` | script | |
| `shared.PermissionMatrix._save` | script | |
| `shared.PermissionMatrix.createRole` | script | |
| `shared.PermissionMatrix.syncRoles` | script | |
| `shared.TicketLogger.saveRouting` | script | |
| `shared.TicketLogger.setDryRun` | script | |
| `shared.UserAdmin.commit` | script | |
</details>
