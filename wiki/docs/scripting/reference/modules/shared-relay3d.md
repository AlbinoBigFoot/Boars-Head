---
title: "shared.Relay3d"
sidebar_label: "shared.Relay3d"
description: "Script module shared.Relay3d: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`  
**Lines:** 133. **Functions:** 8. **Called as:** `shared.Relay3d.<function>(...)`

## What the source says

```text
HLCO Safety Relay 3D (WebDev relay3d/*): READ ONLY relay state for the three.js page, and the locally served static files.

Nothing here writes a tag: system.tag.readBlocking only, and only below [default]Boars_Head/ (never [RCP1] or
[default]_RCP1_). Callers check the login first (shared.WebAuth.perspectiveUser).
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.tag`, `system.util` |
| Calls modules | [shared.WebAuth](./shared-webauth.md) |

<details>
<summary>Module constants (10)</summary>

| Name | Value |
|---|---|
| `DEVICE_FOLDER` | `'[default]Boars_Head/GrovePort/Machine Room/SafetyRelays/'` |
| `SITE_PREFIX` | `'[default]Boars_Head/'` |
| `LIST_TAG` | `'[default]_Config/PLCs/List'` |
| `_NAME` | `re.compile('^[A-Za-z0-9 _\\-]{1,60}$')` |
| `_PLC` | `re.compile('^[A-Za-z0-9_\\-]{1,40}$')` |
| `CATALOG` | `'440C-CR30-22BBB/A'` |
| `POINTS` | `['Pt%02dData' % i for i in range(10)] + ['Pt18Data', 'Pt1...` |
| `CODES` | `['MajorFaultCode', 'MajorFaultType']` |
| `FILES` | `{'relay3d.js': 'text/javascript; charset=utf-8', 'relay3d...` |
| `LIB_REL` | `'projects/BH/com.inductiveautomation.webdev/resources/rel...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`param`](#param) | | 0 |
| [`devicePath`](#devicepath) | | 0 |
| [`screwType`](#screwtype) | 'phillips' (default) or 'flat': the same Designer-only screwType the 3D rack reads from \_Config/PLCs/List (this PLC's entry). | 0 |
| [`_good`](#_good) (internal) | | 0 |
| [`_bool`](#_bool) (internal) | | 0 |
| [`state`](#state) | | 1 |
| [`_libDir`](#_libdir) (internal) | | 0 |
| [`serveFile`](#servefile) | Bytes of one whitelisted relay3d/lib file (read from the project folder on the gateway; cached per mtime). | 2 |

### param {#param}

```python
def param(request, key, default='')
```
Line 23 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `state`

### devicePath {#devicepath}

```python
def devicePath(name)
```
Line 38 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `state`

### screwType {#screwtype}

```python
def screwType(plc)
```
Line 45 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

```text
'phillips' (default) or 'flat': the same Designer-only screwType the 3D rack reads from _Config/PLCs/List (this PLC's entry).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `state`

### \_good {#_good}

```python
def _good(qv)
```
Line 60 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

_No docstring._

Used inside the module by: `_bool`, `state`

### \_bool {#_bool}

```python
def _bool(qv)
```
Line 67 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

_No docstring._

Used inside the module by: `state`

### state {#state}

```python
def state(request)
```
Line 76 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `relay3d/state` | webdev | `doGet` |

### \_libDir {#_libdir}

```python
def _libDir(request)
```
Line 109 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

_No docstring._

Used inside the module by: `serveFile`

### serveFile {#servefile}

```python
def serveFile(request, name)
```
Line 117 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py`.

```text
Bytes of one whitelisted relay3d/lib file (read from the project folder on the gateway; cached per mtime).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `relay3d/lib` | webdev | `doGet` |
| `relay3d/view` | webdev | `doGet` |
