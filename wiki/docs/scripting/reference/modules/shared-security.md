---
title: "shared.Security"
sidebar_label: "shared.Security"
description: "Script module shared.Security: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`  
**Lines:** 398. **Functions:** 25. **Called as:** `shared.Security.<function>(...)`

## What the source says

```text
Role lists from [default]_Config/Security and the Roles & Permissions matrix [default]_Config/RolesPermissions
(no hard-coded role names - a renamed role only needs the tag / matrix column changed).
Role lists are comma-separated, matched case-insensitively. Tiers:
what a role may do is its column in the matrix; several roles = the union; FullPermissionRoles hold everything.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.tag`, `system.util` |
| Logger names | `shared.Security` |
| Calls modules | [shared.Alerts](./shared-alerts.md), [shared.Audit](./shared-audit.md), [shared.PermissionMatrix](./shared-permissionmatrix.md) |
| Called by modules | [Navigation.Faceplate](./navigation-faceplate.md), [shared.AlarmConfig](./shared-alarmconfig.md), [shared.Alerts](./shared-alerts.md), [shared.Audit](./shared-audit.md), [shared.Forms](./shared-forms.md), [shared.Globe](./shared-globe.md), [shared.Integrations](./shared-integrations.md), [shared.OutOfService](./shared-outofservice.md), [shared.PermissionMatrix](./shared-permissionmatrix.md), [shared.Reports](./shared-reports.md), [shared.TicketLogger](./shared-ticketlogger.md), [shared.UserAdmin](./shared-useradmin.md), [shared.ValveCommands](./shared-valvecommands.md) |

<details>
<summary>Module constants (6)</summary>

| Name | Value |
|---|---|
| `BASE` | `'[default]_Config/Security/'` |
| `MATRIX` | `'[default]_Config/RolesPermissions'` |
| `DEVICE_TYPES` | `BASE + 'DeviceTypes'` |
| `DEVICE_ACTION_RULES` | `BASE + 'DeviceActionRules'` |
| `STAND_IN` | `{'Setpoint': 'Configuration', 'Configuration': 'Setpoint'}` |
| `_TYPE_TTL_MS` | `300000` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`roleList`](#rolelist) | 'A, b ,C' -&gt; ['a', 'b', 'c'] (lower-case, blanks dropped). | 1 |
| [`hasAnyRole`](#hasanyrole) | True when any of the user's roles is in the comma-separated list. | 2 |
| [`roles`](#roles) | Role names (original case) from \_Config/Security/&lt;name&gt;. | 6 |
| [`effectiveRoles`](#effectiveroles) | Held roles (lower-case) plus the roles they inherit from \_Config/Security/RoleInherits. | 1 |
| [`restrictedRows`](#restrictedrows) | \_Config/Security/RestrictedRows 'TicketLogger/Use:OneShot, A/B:X\|Y' -&gt; \{'TicketLogger/Use': ['oneshot'], ...\}. | 4 |
| [`rowVisible`](#rowvisible) | False when Devices/Actions key is a RestrictedRows row and the viewer holds none of its roles. | 3 |
| [`rowRules`](#rowrules) | \{'restricted': [Devices/Actions keys], 'hidden': [those the viewer may not see]\} for the Roles & Permissions page. | 1 |
| [`newRoleDefaults`](#newroledefaults) | \_Config/Security/NewRoleDefaults 'TicketLogger/Use, A/B' -&gt; set of Devices/Actions keys a role gets when the | 1 |
| [`permissions`](#permissions) | \{Device: \{Action: bool\}\} for a user holding userRoles, from the RolesPermissions dataset. | 4 |
| [`_currentSession`](#_currentsession) (internal) | The Perspective session running this script (component / message / page scripts), else None. | 2 |
| [`_rolesOf`](#_rolesof) (internal) | Roles of a session (script wrapper self.session or the gateway session object); None when unreadable. | 0 |
| [`_userOf`](#_userof) (internal) | | 0 |
| [`_sessionPerms`](#_sessionperms) (internal) | (session, perms) for the Perspective session running this script; (None, None) outside a session, (s, None) | 0 |
| [`can`](#can) | Server-side check: may the Perspective session (given, else the one running this script) do Device/Action? | 3 |
| [`allowed`](#allowed) | can() for view scripts that hold self.session. | 36 |
| [`require`](#require) | can(), logging the refusal (who, what) when it is denied. | 13 |
| [`_dsRows`](#_dsrows) (internal) | | 0 |
| [`_typeIds`](#_typeids) (internal) | \{path: TypeId or ''\} for tag paths (cached 5 min; a TypeId only changes when a device is re-instanced). | 0 |
| [`deviceOf`](#deviceof) | (devicePath, device): the deepest instance on tagPath (itself or an ancestor) whose UDT TypeId is listed in | 0 |
| [`actionOf`](#actionof) | Matrix action for a write to tagPath below devicePath (\_Config/Security/DeviceActionRules, else Setpoint). | 0 |
| [`deviceRow`](#devicerow) | The matrix action that gates device/action: itself, its Setpoint/Configuration stand-in, or None (no row). | 0 |
| [`_deny`](#_deny) (internal) | | 0 |
| [`requireDevice`](#requiredevice) | Device-type row only (the caller checked the general row): True unless the session's roles lack the | 1 |
| [`checkWrite`](#checkwrite) | (ok, key) for a Perspective session writing tagPath: Faceplates/Operate, then the device-type row of the member | 0 |
| [`requireWrite`](#requirewrite) | checkWrite() for shared.Audit.writeTag / Alerts.confirmApplyWrite / ValveCommands. A device-type refusal | 4 |

### roleList {#rolelist}

```python
def roleList(csv)
```
Line 12 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
'A, b ,C' -> ['a', 'b', 'c'] (lower-case, blanks dropped).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix.checkRoleName` | script | |

Used inside the module by: `hasAnyRole`

### hasAnyRole {#hasanyrole}

```python
def hasAnyRole(userRoles, csv)
```
Line 17 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
True when any of the user's roles is in the comma-separated list.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `session-props` | session props | `binding custom.Administrator` |
| `shared.Globe.adminWriter` | script | |

Used inside the module by: `permissions`

### roles {#roles}

```python
def roles(name)
```
Line 29 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
Role names (original case) from _Config/Security/<name>.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix._save` | script | |
| `shared.PermissionMatrix.roleInfo` | script | |
| `shared.PermissionMatrix.roleSummary` | script | |
| `shared.UserAdmin.deleteRole` | script | |
| `shared.UserAdmin.hiddenRoles` | script | |
| `shared.UserAdmin.pageData` | script | |

### effectiveRoles {#effectiveroles}

```python
def effectiveRoles(userRoles, inheritsCsv)
```
Line 35 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
Held roles (lower-case) plus the roles they inherit from _Config/Security/RoleInherits.

'Engineering:Maintenance, A:B' = Engineering also gets every Maintenance tick; chains follow (A:B, B:C).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix.roleSummary` | script | |

Used inside the module by: `permissions`

### restrictedRows {#restrictedrows}

```python
def restrictedRows(csv)
```
Line 58 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
_Config/Security/RestrictedRows 'TicketLogger/Use:OneShot, A/B:X|Y' -> {'TicketLogger/Use': ['oneshot'], ...}.

A restricted row is not given to FullPermissionRoles implicitly (only its ticks count) and the Roles &
Permissions page shows / saves it only for viewers holding one of its roles (device-perms 2026-10-24).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix._hiddenKeys` | script | |
| `shared.PermissionMatrix._save` | script | |
| `shared.PermissionMatrix.checkRoleName` | script | |
| `shared.PermissionMatrix.roleSummary` | script | |

Used inside the module by: `permissions`, `rowRules`, `rowVisible`

### rowVisible {#rowvisible}

```python
def rowVisible(key, viewerRoles, restrictedCsv)
```
Line 71 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
False when Devices/Actions key is a RestrictedRows row and the viewer holds none of its roles.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix._hiddenKeys` | script | |
| `shared.PermissionMatrix._save` | script | |
| `shared.PermissionMatrix.roleSummary` | script | |

Used inside the module by: `rowRules`

### rowRules {#rowrules}

```python
def rowRules(viewerRoles, restrictedCsv)
```
Line 83 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
{'restricted': [Devices/Actions keys], 'hidden': [those the viewer may not see]} for the Roles & Permissions page.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `binding custom.rowRules` |

### newRoleDefaults {#newroledefaults}

```python
def newRoleDefaults(csv)
```
Line 89 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
_Config/Security/NewRoleDefaults 'TicketLogger/Use, A/B' -> set of Devices/Actions keys a role gets when the
matrix first sees it (role-wizard 2026-10-24).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix._defaults` | script | |

Used inside the module by: `permissions`

### permissions {#permissions}

```python
def permissions(userRoles, matrix, fullCsv, inheritsCsv='', restrictedCsv='', defaultsCsv='')
```
Line 95 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
{Device: {Action: bool}} for a user holding userRoles, from the RolesPermissions dataset.

A row is allowed when any held (or inherited, see effectiveRoles) role's column is ticked (union);
FullPermissionRoles get every row except the RestrictedRows ones (Ticket Logger: ticks only). Role -> column
matching is case-insensitive. Rows sharing Device/Action are OR-ed. A held role the matrix has no column for
yet (created in the gateway) holds the NewRoleDefaults rows (role-wizard 2026-10-24; the Roles & Permissions
page then adds its column with the same ticks, shared.PermissionMatrix.syncRoles).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/_RPProbe` | view | `root/L1 binding props.text` |
| `00_Pages/Boars Head/Operations/_RPProbe` | view | `root/L2 binding props.text` |
| `session-props` | session props | `binding custom.Permissions` |
| `shared.PermissionMatrix.roleGrants` | script | |

Used inside the module by: `_sessionPerms`

### \_currentSession {#_currentsession}

```python
def _currentSession()
```
Line 126 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
The Perspective session running this script (component / message / page scripts), else None.

Perspective's PageModel.PAGE / InternalSession.SESSION thread-locals are empty in component scripts (checked
2026-10-01, 8.3.7), so in practice the session comes from the calling script's self.session on the stack.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Audit._sessionMayWrite` | script | |
| `shared.Reports.open` | script | |

Used inside the module by: `_sessionPerms`, `requireWrite`, `require`

### \_rolesOf {#_rolesof}

```python
def _rolesOf(session)
```
Line 173 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
Roles of a session (script wrapper self.session or the gateway session object); None when unreadable.
```

Used inside the module by: `_sessionPerms`

### \_userOf {#_userof}

```python
def _userOf(session)
```
Line 191 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

_No docstring._

Used inside the module by: `_deny`, `requireWrite`, `require`

### \_sessionPerms {#_sessionperms}

```python
def _sessionPerms(session=None)
```
Line 198 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
(session, perms) for the Perspective session running this script; (None, None) outside a session, (s, None)
when its roles cannot be read (logged once) - callers then allow, the UI gates still apply.
```

Used inside the module by: `can`, `checkWrite`, `requireDevice`

### can {#can}

```python
def can(device, action, session=None)
```
Line 215 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
Server-side check: may the Perspective session (given, else the one running this script) do Device/Action?

Outside a Perspective session (gateway timer / tag event scripts, no user) this is True so gateway logic keeps
working. If the session context cannot be read it logs once and allows (the UI gates still apply).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `Navigation.Faceplate.openDevice` | script | |
| `shared.Integrations._settingsAllowed` | script | |
| `shared.TicketLogger.canConfigure` | script | |

Used inside the module by: `allowed`, `require`

### allowed {#allowed}

```python
def allowed(session, device, action)
```
Line 226 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
can() for view scripts that hold self.session.
```

<details>
<summary>Called from 36 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpBulk` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpBulkApply` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpSave` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpSaveConfirmed` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpToggle` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root event system.onStartup` |
| `02_Components/01_Devices/Compressor` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Compressor` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/CoolingTower` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/CoolingTower` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Evaporator` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Evaporator` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/ExhaustFan` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/ExhaustFan` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/LTU` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/LTU` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Pump` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Pump` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Sensor` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Sensor` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/SolenoidValve` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/SolenoidValve` | view | `root message handler oosToggle` |
| `02_Components/01_Devices/Tank` | view | `root message handler oosHistory` |
| `02_Components/01_Devices/Tank` | view | `root message handler oosToggle` |
| `98_Configuration/AdhocTrend/UserSavedTrendConfig` | view | `root message handler TrendDeleteConfirm` |
| `98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` | view | `root/Buttons/Save event component.onActionPerformed` |
| `shared.Forms.allowed` | script | |
| `shared.PermissionMatrix._save` | script | |
| `shared.PermissionMatrix.mayCreate` | script | |
| `shared.Reports._formRows` | script | |
| `shared.Reports.allowed` | script | |
| `shared.Reports.sourceAllowed` | script | |
| `shared.UserAdmin.deleteRole` | script | |
| `shared.UserAdmin.deleteUser` | script | |
| `shared.UserAdmin.saveRole` | script | |
| `shared.UserAdmin.saveUser` | script | |
</details>

### require {#require}

```python
def require(device, action, what='', session=None)
```
Line 231 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
can(), logging the refusal (who, what) when it is denied.
```

<details>
<summary>Called from 13 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `Navigation.Faceplate.openFaceplate` | script | |
| `shared.AlarmConfig.applyOverride` | script | |
| `shared.Forms.pdfBytes` | script | |
| `shared.Forms.pidSaveCheck` | script | |
| `shared.Forms.submit` | script | |
| `shared.Integrations._requireSettings` | script | |
| `shared.OutOfService.addComment` | script | |
| `shared.OutOfService.setOutOfService` | script | |
| `shared.Reports.open` | script | |
| `shared.Reports.run` | script | |
| `shared.TicketLogger.createTicket` | script | |
| `shared.TicketLogger.requireSettings` | script | |
| `shared.TicketLogger.send` | script | |
</details>

### \_dsRows {#_dsrows}

```python
def _dsRows(ds, *cols)
```
Line 256 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

_No docstring._

Used inside the module by: `actionOf`, `deviceOf`

### \_typeIds {#_typeids}

```python
def _typeIds(paths)
```
Line 268 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
{path: TypeId or ''} for tag paths (cached 5 min; a TypeId only changes when a device is re-instanced).
```

Used inside the module by: `deviceOf`

### deviceOf {#deviceof}

```python
def deviceOf(tagPath)
```
Line 294 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
(devicePath, device): the deepest instance on tagPath (itself or an ancestor) whose UDT TypeId is listed in
_Config/Security/DeviceTypes, and its matrix Devices value; ('', '') when the path is no device.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `checkWrite`, `requireDevice`

### actionOf {#actionof}

```python
def actionOf(tagPath, devicePath)
```
Line 320 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
Matrix action for a write to tagPath below devicePath (_Config/Security/DeviceActionRules, else Setpoint).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `checkWrite`

### deviceRow {#devicerow}

```python
def deviceRow(perms, device, action)
```
Line 333 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
The matrix action that gates device/action: itself, its Setpoint/Configuration stand-in, or None (no row).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `checkWrite`, `requireDevice`

### \_deny {#_deny}

```python
def _deny(s, key, what, notify)
```
Line 344 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

_No docstring._

Used inside the module by: `requireDevice`, `requireWrite`

### requireDevice {#requiredevice}

```python
def requireDevice(tagPath, action, what='', session=None, notify=True)
```
Line 357 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
Device-type row only (the caller checked the general row): True unless the session's roles lack the
<Device>/<action> row of the device on tagPath (then a 'Not Permitted' dialog and a log line).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.AlarmConfig.applyOverride` | script | |

### checkWrite {#checkwrite}

```python
def checkWrite(tagPath, session=None)
```
Line 372 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
(ok, key) for a Perspective session writing tagPath: Faceplates/Operate, then the device-type row of the member
(deviceOf + actionOf). key = the refusing 'Device/Action' row, '' when allowed. Gateway scripts: (True, '').
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `requireWrite`

### requireWrite {#requirewrite}

```python
def requireWrite(tagPath, what='', session=None, notify=True)
```
Line 388 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py`.

```text
checkWrite() for shared.Audit.writeTag / Alerts.confirmApplyWrite / ValveCommands. A device-type refusal
shows a 'Not Permitted' dialog naming the row; a Faceplates/Operate refusal stays silent (the UI is read only).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `02_Components/01_Devices/LTU` | view | `root/ResetRow/ResetCount event component.onActionPerformed` |
| `shared.Alerts.confirmApplyWrite` | script | |
| `shared.Audit._sessionMayWrite` | script | |
| `shared.ValveCommands._write` | script | |
