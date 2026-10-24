---
title: "shared.PermissionMatrix"
sidebar_label: "shared.PermissionMatrix"
description: "Script module shared.PermissionMatrix: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`  
**Lines:** 465. **Functions:** 24. **Called as:** `shared.PermissionMatrix.<function>(...)`

## What the source says

```text
Roles & Permissions page (Operations > Roles & Permissions) - server side.

The matrix [default]_Config/RolesPermissions stays the source of truth (Devices / Actions / Description + one Boolean
column per role); this module never reorders rows or rewrites the dataset. save() re-reads the tag right before the

role-wizard (2026-10-24): a role the matrix has no column for gets one with _Config/Security/NewRoleDefaults ticked
(syncRoles on page load, save); createRole() = the New Role wizard (gateway role + matrix column + audit, rolled back
when the matrix write fails). Rows hidden from the viewer (RestrictedRows) are never changed by their saves.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.dataset`, `system.perspective`, `system.tag`, `system.user`, `system.util` |
| Logger names | `shared.PermissionMatrix` |
| Calls modules | [shared.Audit](./shared-audit.md), [shared.Security](./shared-security.md), [shared.UserAdmin](./shared-useradmin.md) |

<details>
<summary>Module constants (8)</summary>

| Name | Value |
|---|---|
| `MATRIX` | `'[default]_Config/RolesPermissions'` |
| `SEC` | `'[default]_Config/Security/'` |
| `KEY_COLS` | `('Devices', 'Actions', 'Description', 'Category')` |
| `VIEW_NAME` | `'Operations/RolesPermissions'` |
| `ROLE_LIST_TAGS` | `('AdminRoles', 'FullPermissionRoles', 'RestrictedRoles', ...` |
| `NAME_CHARS` | `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123...` |
| `WIZARD_VIEW` | `'00_Pages/Boars Head/Operations/_Admin/NewRole'` |
| `WIZARD_ID` | `'newRoleWizard'` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_roleColumns`](#_rolecolumns) (internal) | | 0 |
| [`roleInfo`](#roleinfo) | Roles shown as matrix columns: [\{name, users, members, restricted, inMatrix\}]. | 0 |
| [`_rows`](#_rows) (internal) | | 0 |
| [`model`](#model) | (perms, cats): perms = [\{key, dev, act, label, desc, cat, sub, ticks\{col: bool\}\}] merged by Devices/Actions, in | 0 |
| [`_esc`](#_esc) (internal) | | 0 |
| [`roleSummary`](#rolesummary) | roleInfo() plus, per role, what it is granted (saved matrix, inheritance + full roles applied): | 10 |
| [`editSummary`](#editsummary) | Change bar text: 'ReadOnly: +3 Granted, Maintenance: 1 Revoked'. | 2 |
| [`_summary`](#_summary) (internal) | Readable lines for the confirm dialog: 'Maintenance: Grant View Audit Log'. | 0 |
| [`describe`](#describe) | | 1 |
| [`save`](#save) | | 1 |
| [`_save`](#_save) (internal) | Apply \{"Devices/Actions\|Role": bool\} to the live matrix. Returns \{"ok", "changed", "message"\}. | 0 |
| [`_defaults`](#_defaults) (internal) | Devices/Actions keys a new role gets (\_Config/Security/NewRoleDefaults). | 0 |
| [`_key`](#_key) (internal) | | 0 |
| [`_addRoleColumn`](#_addrolecolumn) (internal) | ds plus a Boolean column for role; rows whose Devices/Actions key is in ticks are True. | 0 |
| [`syncRoles`](#syncroles) | Add a matrix column (NewRoleDefaults ticked) for every gateway role without one - a role created in the gateway, | 0 |
| [`_viewerRoles`](#_viewerroles) (internal) | | 0 |
| [`_userName`](#_username) (internal) | | 0 |
| [`_hiddenKeys`](#_hiddenkeys) (internal) | | 0 |
| [`wizardModel`](#wizardmodel) | New Role wizard data: \{groups: [\{name, icon, desc, rows: [\{key, label, desc, sub\}]\}], defaults: [keys the | 1 |
| [`roleGrants`](#rolegrants) | Copy Permissions From: the keys `role` effectively holds (its ticks, RoleInherits, full permission role), | 1 |
| [`checkRoleName`](#checkrolename) | '' when name can be a new role, else the reason (operator-readable). | 1 |
| [`mayCreate`](#maycreate) | Add Users And Roles (or Edit Users And Roles) plus Edit Roles & Permissions. | 1 |
| [`createRole`](#createrole) | New Role wizard: add the role to the user source and its matrix column (the chosen visible rows; hidden | 1 |
| [`openWizard`](#openwizard) | Open the New Role wizard popup, centred in the caller's viewport (never larger than it). | 2 |

### \_roleColumns {#_rolecolumns}

```python
def _roleColumns(ds)
```
Line 20 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

Used inside the module by: `createRole`, `roleInfo`, `syncRoles`

### roleInfo {#roleinfo}

```python
def roleInfo(userSource, viewerRoles)
```
Line 24 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Roles shown as matrix columns: [{name, users, members, restricted, inMatrix}].

Gateway roles only (as before); RestrictedRoles the viewer does not hold are left out (shared.UserAdmin).
Order: the matrix column order, then roles the matrix has no column for yet (alphabetical).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `roleSummary`

### \_rows {#_rows}

```python
def _rows(ds)
```
Line 51 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

Used inside the module by: `model`

### model {#model}

```python
def model()
```
Line 55 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
(perms, cats): perms = [{key, dev, act, label, desc, cat, sub, ticks{col: bool}}] merged by Devices/Actions, in
page order; cats = [{name, icon, desc}]. Same grouping rules as the page expressions (permission_catalog.py).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `roleSummary`, `wizardModel`

### \_esc {#_esc}

```python
def _esc(s)
```
Line 94 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

Used inside the module by: `roleSummary`

### roleSummary {#rolesummary}

```python
def roleSummary(userSource, viewerRoles)
```
Line 98 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
roleInfo() plus, per role, what it is granted (saved matrix, inheritance + full roles applied):
{full, base, heirs, granted, total, html} - html = one block per group for the Roles tab (markdown, raw HTML).
```

<details>
<summary>Called from 10 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root event system.onStartup` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler nrCreated` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpSaveConfirmed` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root/Content/HeaderCard/TitleRow/Tabs/Tab_roles event dom.onClick` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root event system.onStartup` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler nrCreated` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umDeleteConfirmed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleDeleteConfirmed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleSaveConfirmed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umSaveConfirmed` |
</details>

### editSummary {#editsummary}

```python
def editSummary(edits)
```
Line 147 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Change bar text: 'ReadOnly: +3 Granted, Maintenance: 1 Revoked'.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpBulkApply` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpToggle` |

### \_summary {#_summary}

```python
def _summary(edits, labels)
```
Line 162 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Readable lines for the confirm dialog: 'Maintenance: Grant View Audit Log'.
```

Used inside the module by: `describe`

### describe {#describe}

```python
def describe(edits, labels, limit=6)
```
Line 171 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpSave` |

### save {#save}

```python
def save(session, edits)
```
Line 180 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpSaveConfirmed` |

### \_save {#_save}

```python
def _save(session, edits)
```
Line 185 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Apply {"Devices/Actions|Role": bool} to the live matrix. Returns {"ok", "changed", "message"}.

Every row with that Devices/Actions gets the tick (duplicate keys are OR-ed by shared.Security anyway). A role the
matrix has no column for yet gets a Boolean column appended (NewRoleDefaults ticked, the rest False). _Config/Security/RoleInherits pairs: a grant

step the same way). Full permission roles are skipped (they always hold everything).
```

Used inside the module by: `save`

### \_defaults {#_defaults}

```python
def _defaults()
```
Line 270 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Devices/Actions keys a new role gets (_Config/Security/NewRoleDefaults).
```

Used inside the module by: `_save`, `createRole`, `syncRoles`, `wizardModel`

### \_key {#_key}

```python
def _key(ds, i)
```
Line 275 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

Used inside the module by: `_addRoleColumn`, `createRole`

### \_addRoleColumn {#_addrolecolumn}

```python
def _addRoleColumn(ds, role, ticks)
```
Line 279 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
ds plus a Boolean column for role; rows whose Devices/Actions key is in ticks are True.
```

Used inside the module by: `_save`, `createRole`, `syncRoles`

### syncRoles {#syncroles}

```python
def syncRoles(userSource='default')
```
Line 285 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Add a matrix column (NewRoleDefaults ticked) for every gateway role without one - a role created in the gateway,
not through the wizard. Existing columns are never changed. Returns the role names added.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `roleSummary`

### \_viewerRoles {#_viewerroles}

```python
def _viewerRoles(session)
```
Line 318 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

Used inside the module by: `createRole`

### \_userName {#_username}

```python
def _userName(session)
```
Line 325 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

Used inside the module by: `createRole`

### \_hiddenKeys {#_hiddenkeys}

```python
def _hiddenKeys(viewerRoles)
```
Line 332 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

_No docstring._

Used inside the module by: `createRole`, `roleGrants`, `wizardModel`

### wizardModel {#wizardmodel}

```python
def wizardModel(userSource, viewerRoles)
```
Line 337 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
New Role wizard data: {groups: [{name, icon, desc, rows: [{key, label, desc, sub}]}], defaults: [keys the
viewer sees pre-ticked], roles: [role names to copy from], total}. RestrictedRows the viewer may not see are left
out (createRole sets them to their NewRoleDefaults value).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | view | `root event system.onStartup` |

### roleGrants {#rolegrants}

```python
def roleGrants(role, viewerRoles)
```
Line 356 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Copy Permissions From: the keys `role` effectively holds (its ticks, RoleInherits, full permission role),
limited to the rows the viewer sees.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | view | `root/ActionBar/Next event component.onActionPerformed` |

### checkRoleName {#checkrolename}

```python
def checkRoleName(userSource, name)
```
Line 366 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
'' when name can be a new role, else the reason (operator-readable).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | view | `root/ActionBar/Next event component.onActionPerformed` |

Used inside the module by: `createRole`

### mayCreate {#maycreate}

```python
def mayCreate(session)
```
Line 393 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Add Users And Roles (or Edit Users And Roles) plus Edit Roles & Permissions.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | view | `root event system.onStartup` |

Used inside the module by: `createRole`

### createRole {#createrole}

```python
def createRole(session, userSource, name, grants, copyFrom='')
```
Line 400 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
New Role wizard: add the role to the user source and its matrix column (the chosen visible rows; hidden
RestrictedRows get their NewRoleDefaults value), then audit "Role Created". The role is removed again when the
matrix write fails. No _Config/Security role list is changed. Returns {"ok", "message", "granted"}.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | view | `root message handler nrCreateConfirmed` |

### openWizard {#openwizard}

```python
def openWizard(page, userSource='default')
```
Line 450 of `gateways/standard/data/projects/BH/ignition/script-python/shared/PermissionMatrix/code.py`.

```text
Open the New Role wizard popup, centred in the caller's viewport (never larger than it).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root/Content/RolesBody/RoleList/Head/AddRole event component.onActionPerformed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root/Content/RolesBody/RoleList/Head/AddRole event component.onActionPerformed` |
