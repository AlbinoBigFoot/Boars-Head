---
title: "shared.UserAdmin"
sidebar_label: "shared.UserAdmin"
description: "Script module shared.UserAdmin: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`  
**Lines:** 279. **Functions:** 18. **Called as:** `shared.UserAdmin.<function>(...)`

## What the source says

```text
User Management helpers (Operations > User Management, ported from the HBT/Scout template).

The template's views call system.user.* directly but never looked at the UIResponse, so a gateway-side
failure (duplicate name, password rule, ...) went back to Home silently. commit() surfaces those errors
in the standard alert popup and records successful changes in OpsAudit.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.user`, `system.util` |
| Logger names | `shared.UserAdmin` |
| Calls modules | [shared.Alerts](./shared-alerts.md), [shared.Audit](./shared-audit.md), [shared.Security](./shared-security.md) |
| Called by modules | [shared.PermissionMatrix](./shared-permissionmatrix.md) |

<details>
<summary>Module constants (2)</summary>

| Name | Value |
|---|---|
| `VIEW_NAME` | `'Operations/UserManagement'` |
| `HIDDEN_USERS` | `set(['admin', 'ops', 'opcuauser'])` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`isHiddenUser`](#ishiddenuser) | | 0 |
| [`visibleUsers`](#visibleusers) | system.user.getUsers without the service accounts (admin, OPS, ...). | 1 |
| [`hiddenRoles`](#hiddenroles) | Restricted roles the viewer (session user) does not hold - hide these from lists. | 0 |
| [`visibleRoles`](#visibleroles) | | 2 |
| [`keepHiddenRoles`](#keephiddenroles) | Selected roles plus any restricted roles the user already has but the viewer could not see. | 0 |
| [`responseErrors`](#responseerrors) | Error strings from a system.user.\* UIResponse (empty list when it succeeded). | 1 |
| [`commit`](#commit) | True when the gateway accepted the change; otherwise shows the errors and returns False. | 0 |
| [`rolesOf`](#rolesof) | | 0 |
| [`_txt`](#_txt) (internal) | | 0 |
| [`adjMillis`](#adjmillis) | A schedule date as epoch milliseconds (java Date, number or empty -&gt; None). | 1 |
| [`userRecord`](#userrecord) | | 0 |
| [`pageData`](#pagedata) | Everything the page lists: users (people only), every username (duplicate check), roles, options. | 6 |
| [`languageOptions`](#languageoptions) | | 0 |
| [`validateUser`](#validateuser) | Same rules as the template form: username required and unique, password pair, notes / badge &lt;= 500. | 1 |
| [`saveUser`](#saveuser) | Add / edit a user (template behaviour). Returns True when the gateway accepted it. | 1 |
| [`deleteUser`](#deleteuser) | | 1 |
| [`saveRole`](#saverole) | | 1 |
| [`deleteRole`](#deleterole) | | 1 |

### isHiddenUser {#ishiddenuser}

```python
def isHiddenUser(username)
```
Line 16 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `visibleUsers`

### visibleUsers {#visibleusers}

```python
def visibleUsers(userSource)
```
Line 20 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
system.user.getUsers without the service accounts (admin, OPS, ...).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix.roleInfo` | script | |

Used inside the module by: `pageData`

### hiddenRoles {#hiddenroles}

```python
def hiddenRoles(viewerRoles)
```
Line 25 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
Restricted roles the viewer (session user) does not hold - hide these from lists.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `keepHiddenRoles`, `visibleRoles`

### visibleRoles {#visibleroles}

```python
def visibleRoles(userSource, viewerRoles)
```
Line 31 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix.roleInfo` | script | |
| `shared.PermissionMatrix.wizardModel` | script | |

Used inside the module by: `pageData`

### keepHiddenRoles {#keephiddenroles}

```python
def keepHiddenRoles(userObject, selectedRoles, viewerRoles)
```
Line 36 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
Selected roles plus any restricted roles the user already has but the viewer could not see.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `saveUser`

### responseErrors {#responseerrors}

```python
def responseErrors(resp)
```
Line 50 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
Error strings from a system.user.* UIResponse (empty list when it succeeded).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.PermissionMatrix.createRole` | script | |

Used inside the module by: `commit`

### commit {#commit}

```python
def commit(kind, action, target, resp, detail='')
```
Line 60 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
True when the gateway accepted the change; otherwise shows the errors and returns False.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `deleteRole`, `deleteUser`, `saveRole`, `saveUser`

### rolesOf {#rolesof}

```python
def rolesOf(userObject)
```
Line 79 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `saveUser`

### \_txt {#_txt}

```python
def _txt(v)
```
Line 93 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

Used inside the module by: `pageData`, `saveRole`, `saveUser`, `userRecord`, `validateUser`

### adjMillis {#adjmillis}

```python
def adjMillis(v)
```
Line 97 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
A schedule date as epoch milliseconds (java Date, number or empty -> None).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umAdjSet` |

Used inside the module by: `saveUser`, `userRecord`, `validateUser`

### userRecord {#userrecord}

```python
def userRecord(u)
```
Line 111 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `pageData`

### pageData {#pagedata}

```python
def pageData(userSource, viewerRoles)
```
Line 139 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
Everything the page lists: users (people only), every username (duplicate check), roles, options.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root event system.onStartup` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler nrCreated` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umDeleteConfirmed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleDeleteConfirmed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleSaveConfirmed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umSaveConfirmed` |

### languageOptions {#languageoptions}

```python
def languageOptions()
```
Line 159 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `pageData`

### validateUser {#validateuser}

```python
def validateUser(userSource, mode, draft)
```
Line 171 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
Same rules as the template form: username required and unique, password pair, notes / badge <= 500.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umSave` |

Used inside the module by: `saveUser`

### saveUser {#saveuser}

```python
def saveUser(session, userSource, mode, draft)
```
Line 199 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

```text
Add / edit a user (template behaviour). Returns True when the gateway accepted it.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umSaveConfirmed` |

### deleteUser {#deleteuser}

```python
def deleteUser(session, userSource, username)
```
Line 238 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umDeleteConfirmed` |

### saveRole {#saverole}

```python
def saveRole(session, userSource, mode, oldName, newName)
```
Line 247 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleSaveConfirmed` |

### deleteRole {#deleterole}

```python
def deleteRole(session, userSource, role)
```
Line 268 of `gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleDeleteConfirmed` |
