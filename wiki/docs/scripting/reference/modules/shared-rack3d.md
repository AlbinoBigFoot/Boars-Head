---
title: "shared.Rack3d"
sidebar_label: "shared.Rack3d"
description: "Script module shared.Rack3d: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`  
**Lines:** 194. **Functions:** 11. **Called as:** `shared.Rack3d.<function>(...)`

## What the source says

```text
PLC Rack 3D (WebDev rack3d/*): READ ONLY rack / IO state for the three.js page, and the locally served static files.

Nothing here writes a tag: system.tag.readBlocking only, and only below [default]Boars_Head/ (never [RCP1] or
[default]_RCP1_). Callers check the login first (shared.WebAuth.perspectiveUser).
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.date`, `system.tag`, `system.util` |
| Calls modules | [shared.WebAuth](./shared-webauth.md) |

<details>
<summary>Module constants (8)</summary>

| Name | Value |
|---|---|
| `LOGGER` | `'BH.Rack3d'` |
| `LIST_TAG` | `'[default]_Config/PLCs/List'` |
| `DEFAULT_FOLDER` | `'[default]Boars_Head/GrovePort/Machine Room/PLC/'` |
| `SITE_PREFIX` | `'[default]Boars_Head/'` |
| `_NAME` | `re.compile('^[A-Za-z0-9_\\-]{1,40}$')` |
| `CTRL` | `['Connected', 'Mode', 'Run', 'MajorFault', 'MinorFault', ...` |
| `FILES` | `{'three.module.min.js': 'text/javascript; charset=utf-8',...` |
| `LIB_REL` | `'projects/BH/com.inductiveautomation.webdev/resources/rac...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`param`](#param) | | 0 |
| [`_py`](#_py) (internal) | Document tag value -&gt; plain Python (dict / list). | 0 |
| [`sitePath`](#sitepath) | Site UDT instance of a PLC name: the \_Config/PLCs/List entry, else the Groveport Machine Room folder. | 0 |
| [`screwType`](#screwtype) | 'phillips' (default) or 'flat': the screwType of this PLC's \_Config/PLCs/List entry (Designer Tag Browser only). | 0 |
| [`_good`](#_good) (internal) | | 0 |
| [`_val`](#_val) (internal) | | 0 |
| [`_bits`](#_bits) (internal) | | 0 |
| [`_num`](#_num) (internal) | | 0 |
| [`state`](#state) | | 1 |
| [`_libDir`](#_libdir) (internal) | | 0 |
| [`serveFile`](#servefile) | Bytes of one whitelisted rack3d/lib file (read from the project folder on the gateway; cached per mtime). | 2 |

### param {#param}

```python
def param(request, key, default='')
```
Line 22 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `state`

### \_py {#_py}

```python
def _py(v)
```
Line 37 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

```text
Document tag value -> plain Python (dict / list).
```

Used inside the module by: `screwType`, `sitePath`, `state`

### sitePath {#sitepath}

```python
def sitePath(plc)
```
Line 52 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

```text
Site UDT instance of a PLC name: the _Config/PLCs/List entry, else the Groveport Machine Room folder.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `state`

### screwType {#screwtype}

```python
def screwType(plc)
```
Line 69 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

```text
'phillips' (default) or 'flat': the screwType of this PLC's _Config/PLCs/List entry (Designer Tag Browser only).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `state`

### \_good {#_good}

```python
def _good(qv)
```
Line 81 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

_No docstring._

Used inside the module by: `_val`, `state`

### \_val {#_val}

```python
def _val(qv)
```
Line 88 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

_No docstring._

Used inside the module by: `state`

### \_bits {#_bits}

```python
def _bits(v)
```
Line 92 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

_No docstring._

Used inside the module by: `state`

### \_num {#_num}

```python
def _num(v)
```
Line 99 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

_No docstring._

Used inside the module by: `state`

### state {#state}

```python
def state(request)
```
Line 106 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `rack3d/state` | webdev | `doGet` |

### \_libDir {#_libdir}

```python
def _libDir(request)
```
Line 170 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

_No docstring._

Used inside the module by: `serveFile`

### serveFile {#servefile}

```python
def serveFile(request, name)
```
Line 178 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py`.

```text
Bytes of one whitelisted rack3d/lib file (read from the project folder on the gateway; cached per mtime).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `rack3d/lib` | webdev | `doGet` |
| `rack3d/view` | webdev | `doGet` |
