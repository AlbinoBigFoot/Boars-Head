---
title: "shared.Alarms"
sidebar_label: "shared.Alarms"
description: "Script module shared.Alarms: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`  
**Lines:** 347. **Functions:** 8. **Called as:** `shared.Alarms.<function>(...)`

## What the source says

```text
Alarm rollup rebuild for Config/_Alarms (ported from LGChem / Citadel Rebuild script).
Called from UDT member Rebuild valueChanged via: shared.Alarms.rebuild(tagPath)
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.alarm`, `system.tag`, `system.util` |
| Logger names | `shared.Alarms` |

<details>
<summary>Module constants (3)</summary>

| Name | Value |
|---|---|
| `DEVICE_TYPE_FOLDERS` | `('Evaporators', 'Compressors', 'Pumps', 'ExhaustFans', 'C...` |
| `DEVICE_TYPE_PATTERNS` | `{'Evaporators': ['Evaporators', 'Utility/CG-']}` |
| `AREAS` | `('Freezer', 'SuperChill', 'Club', 'Palletizing', 'East PH...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_selection`](#_selection) (internal) | Multi-select dropdown value -&gt; list of non-empty strings. | 0 |
| [`sourceFilter`](#sourcefilter) | Alarm Status / Alarm Journal source filter from the Device Type and Area multi-selects. | 2 |
| [`deviceTypeSourceFilter`](#devicetypesourcefilter) | Build Alarm Status / Alarm Journal source filter from a multi-select Device Type list. | 0 |
| [`sourceWildcard`](#sourcewildcard) | Alarm Status source filter for a device tag path (same shape as the faceplate table). | 0 |
| [`_alarmEventId`](#_alarmeventid) (internal) | | 0 |
| [`_collectUnackedIds`](#_collectunackedids) (internal) | | 0 |
| [`acknowledgeForTag`](#acknowledgefortag) | Acknowledge unacked Ignition alarms associated with this device (same set as the faceplate table). | 4 |
| [`rebuild`](#rebuild) | Rebuild expression tags under an \_Alarms UDT instance. | 0 |

### \_selection {#_selection}

```python
def _selection(selected)
```
Line 26 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

```text
Multi-select dropdown value -> list of non-empty strings.
```

Used inside the module by: `sourceFilter`

### sourceFilter {#sourcefilter}

```python
def sourceFilter(deviceTypes=None, areas=None)
```
Line 43 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

```text
Alarm Status / Alarm Journal source filter from the Device Type and Area multi-selects.

Within one dropdown the selections are OR'd; across the two dropdowns they are AND'd (an alarm must be
in a selected area AND of a selected type). Nothing selected in either => '*' (all alarms).
The filter is a comma list of wildcards (OR), so the AND is built from area x type combinations:
  area only -> '*/<Area>/*'   type only -> '*<fragment>*'   both -> '*/<Area>/*<fragment>*'
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Alarms/Journal` | view | `root/AlarmJournalTable binding props.params.sourceFilter` |
| `00_Pages/Boars Head/Alarms/Summary` | view | `root/AlarmStatusTable binding props.params.sourceFilter` |

Used inside the module by: `deviceTypeSourceFilter`

### deviceTypeSourceFilter {#devicetypesourcefilter}

```python
def deviceTypeSourceFilter(selected)
```
Line 68 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

```text
Build Alarm Status / Alarm Journal source filter from a multi-select Device Type list.

Empty / None selection => '*' (show all device types).
One or more selections => comma-delimited '*Folder*' wildcards (OR match).
Device types map to tag path folders under [default], e.g. Evaporators → *Evaporators*.
Kept for callers without an Area filter; see sourceFilter().
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### sourceWildcard {#sourcewildcard}

```python
def sourceWildcard(tagPath)
```
Line 80 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

```text
Alarm Status source filter for a device tag path (same shape as the faceplate table).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `acknowledgeForTag`

### \_alarmEventId {#_alarmeventid}

```python
def _alarmEventId(event)
```
Line 98 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

_No docstring._

Used inside the module by: `_collectUnackedIds`

### \_collectUnackedIds {#_collectunackedids}

```python
def _collectUnackedIds(sourceFilter)
```
Line 113 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

_No docstring._

Used inside the module by: `acknowledgeForTag`

### acknowledgeForTag {#acknowledgefortag}

```python
def acknowledgeForTag(tagPath, username='', notes='Faceplate Ack / Reset')
```
Line 148 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

```text
Acknowledge unacked Ignition alarms associated with this device (same set as the faceplate table).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Pump/Alarms` | view | `root/AlarmBits/Body/BtnAckAll event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Alarms` | view | `root/AlarmBits/Body/BtnAckAll event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root/AinHome/LockRow/BtnReset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Alarms` | view | `root/AlarmBits/Body/BtnAckAll event component.onActionPerformed` |

### rebuild {#rebuild}

```python
def rebuild(rebuildTagPath)
```
Line 188 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py`.

```text
Rebuild expression tags under an _Alarms UDT instance.
rebuildTagPath should end with /_Alarms/Rebuild.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._
