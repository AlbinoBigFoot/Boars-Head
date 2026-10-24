---
title: "shared.DevicePages"
sidebar_label: "shared.DevicePages"
description: "Script module shared.DevicePages: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/DevicePages/code.py`  
**Lines:** 288. **Functions:** 6. **Called as:** `shared.DevicePages.<function>(...)`

## What the source says

```text
Device-type pages (Tanks / Pumps / Compressors / Valves / Sensors / Exhaust Fans).


COLUMNS is the plain-English default column set per device type: the members shown on
the Details table, in order, with their header text and how the value is written.
Every other member stays in the table hidden, with a readable label from label(), so an
admin column editor can switch it on later. shared.Overview and Overview/Instances are
unchanged: applyColumns() only relabels / reorders / hides the columns they produce.
Row clicks open faceplates with Navigation.Faceplate.openDevice (no type mapping here),
except for status-only types in NO_FACEPLATE.
```

## At a glance

| | |
|---|---|
| Calls modules | [Navigation.Faceplate](./navigation-faceplate.md) |

<details>
<summary>Module constants (20)</summary>

| Name | Value |
|---|---|
| `ALARM` | `{'0': 'Normal', '1': 'Alarm'}` |
| `FAULT` | `{'0': 'OK', '1': 'Fault'}` |
| `YES_NO` | `{'0': 'No', '1': 'Yes'}` |
| `RUN` | `{'0': 'Stopped', '1': 'Running'}` |
| `PERM` | `{'0': 'Not OK', '1': 'OK'}` |
| `CMD_OPEN` | `{'0': 'Close', '1': 'Open'}` |
| `LIMIT` | `{'0': 'Off', '1': 'On'}` |
| `MODE_REMOTE` | `{'1': 'Remote', '2': 'Auto', '3': 'Manual'}` |
| `COMP_RUN` | `{'0': 'Off', '1': 'Running', '2': 'Anti-Recycle', '3': 'S...` |
| `PUMP_STS` | `{'1': 'Stopped', '2': 'Running', '7': 'Stopping', '8': 'S...` |
| `LEAD_PUMP` | `{'1': 'Pump 1', '2': 'Pump 2'}` |
| `INT` | `'#,##0'` |
| `NO_FACEPLATE` | `('ExhaustFan',)` |
| `STATE_WORD` | `{'ExhaustFan': ('Started',), 'Pump': ('Val_Sts',), 'Compr...` |
| `DEVICE_LABEL` | `'Device'` |
| `DEVICE_WIDTH` | `170` |
| `COLUMNS` | `{'Tank': [('Level', 'Level', None, 110), ('Pressure', 'Pr...` |
| `LABELS` | `{'AutoEN': 'Auto Enabled', 'Cfg_WebGuiUrl': 'Web GUI URL'...` |
| `_PREFIXES` | `[('Cfg_', 'Config: '), ('Sts_', ''), ('Val_', ''), ('Alm_...` |
| `_WORDS` | `{'Intlk': 'Interlock', 'IO': 'I/O', 'Perm': 'Permissive',...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_splitWords`](#_splitwords) (internal) | 'FailToStopT' -&gt; ['Fail', 'To', 'Stop', 'T']; 'IOFault' -&gt; ['IO', 'Fault']. | 0 |
| [`label`](#label) | Plain-English header for a UDT member (default columns first, then LABELS, then a guess). | 0 |
| [`_typeKey`](#_typekey) (internal) | | 0 |
| [`hasFaceplate`](#hasfaceplate) | | 1 |
| [`_plain`](#_plain) (internal) | Column dicts from Overview/Instances arrive as documents; copy to plain dicts/lists. | 0 |
| [`applyColumns`](#applycolumns) | Relabel, reorder and hide shared.Overview table columns for one device type. | 1 |

### \_splitWords {#_splitwords}

```python
def _splitWords(s)
```
Line 192 of `gateways/standard/data/projects/BH/ignition/script-python/shared/DevicePages/code.py`.

```text
'FailToStopT' -> ['Fail', 'To', 'Stop', 'T']; 'IOFault' -> ['IO', 'Fault'].
```

Used inside the module by: `label`

### label {#label}

```python
def label(field, deviceType=None)
```
Line 212 of `gateways/standard/data/projects/BH/ignition/script-python/shared/DevicePages/code.py`.

```text
Plain-English header for a UDT member (default columns first, then LABELS, then a guess).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `applyColumns`

### \_typeKey {#_typekey}

```python
def _typeKey(typeId)
```
Line 232 of `gateways/standard/data/projects/BH/ignition/script-python/shared/DevicePages/code.py`.

_No docstring._

Used inside the module by: `applyColumns`, `hasFaceplate`, `label`

### hasFaceplate {#hasfaceplate}

```python
def hasFaceplate(typeId)
```
Line 236 of `gateways/standard/data/projects/BH/ignition/script-python/shared/DevicePages/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table event component.onRowClick` |

### \_plain {#_plain}

```python
def _plain(obj)
```
Line 240 of `gateways/standard/data/projects/BH/ignition/script-python/shared/DevicePages/code.py`.

```text
Column dicts from Overview/Instances arrive as documents; copy to plain dicts/lists.
```

Used inside the module by: `applyColumns`

### applyColumns {#applycolumns}

```python
def applyColumns(columns, typeId)
```
Line 249 of `gateways/standard/data/projects/BH/ignition/script-python/shared/DevicePages/code.py`.

```text
Relabel, reorder and hide shared.Overview table columns for one device type.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table binding props.columns` |
