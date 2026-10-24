---
title: "shared.Overview"
sidebar_label: "shared.Overview"
description: "Script module shared.Overview: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`  
**Lines:** 612. **Functions:** 29. **Called as:** `shared.Overview.<function>(...)`

## What the source says

```text

Triggered when Overview/.../Rebuild is set True (gateway Tag Change).

Writes {columns, data} to Overview/Instances/Value where data cells are tag
paths (not live values). Cell views bind Value / Metadata from those paths.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag`, `system.util` |
| Logger names | `shared.Overview` |
| Calls modules | [shared.Pax](./shared-pax.md) |

<details>
<summary>Module constants (4)</summary>

| Name | Value |
|---|---|
| `EXCLUDE_NAMES` | `set(['Overview', 'SummaryInstances', 'Metadata', '_Alarms...` |
| `EXCLUDE_PREFIXES` | `('Fan',)` |
| `BOOLEAN_FIELDS` | `set(['Status'])` |
| `PREFERRED_ORDER` | `['Temp', 'Pressure', 'Status']` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_browseName`](#_browsename) (internal) | | 0 |
| [`_browseFullPath`](#_browsefullpath) (internal) | | 0 |
| [`_browseTagType`](#_browsetagtype) (internal) | | 0 |
| [`_browseTypeId`](#_browsetypeid) (internal) | UDT typeId from browse result, else tag configuration. | 0 |
| [`_parentPath`](#_parentpath) (internal) | | 0 |
| [`_pathsEqual`](#_pathsequal) (internal) | Compare tag paths ignoring trailing slash / provider bracket quirks. | 0 |
| [`_naturalSortKey`](#_naturalsortkey) (internal) | | 0 |
| [`_isEnabled`](#_isenabled) (internal) | | 0 |
| [`_normalizeOverviewPath`](#_normalizeoverviewpath) (internal) | Accept .../Overview/Rebuild, .../Overview, or equipment folder. | 0 |
| [`_equipmentFolder`](#_equipmentfolder) (internal) | | 0 |
| [`makeTagPathColumn`](#maketagpathcolumn) | | 0 |
| [`makeNumericColumn`](#makenumericcolumn) | | 0 |
| [`makeBooleanColumn`](#makebooleancolumn) | | 0 |
| [`_includeChild`](#_includechild) (internal) | | 0 |
| [`_columnKind`](#_columnkind) (internal) | | 0 |
| [`discoverPointFields`](#discoverpointfields) | Return ordered list of (fieldName, kind) from a device UDT template. | 0 |
| [`_isEquipmentDeviceType`](#_isequipmentdevicetype) (internal) | True for folder-level device UDTs (Devices/Evaporator, Devices/Pump, …). | 0 |
| [`findDevices`](#finddevices) | Enabled device UDT instances that are direct children of the equipment folder. | 0 |
| [`buildInstancesPayload`](#buildinstancespayload) | | 4 |
| [`buildInstancesPayloadForType`](#buildinstancespayloadfortype) | Overview table payload for one Devices/\* type under a plant/area folder. | 4 |
| [`writeInstances`](#writeinstances) | | 0 |
| [`writeDeviceCount`](#writedevicecount) | Lightspeed Overview/DeviceCount/Value — memory Int4 device tally. | 0 |
| [`buildActiveAlarmCountExpression`](#buildactivealarmcountexpression) | Lightspeed pattern: sum(\{path1/\_Alarms/\_Active\}, \{path2/\_Alarms/\_Active\}, ...) | 0 |
| [`writeActiveAlarmCount`](#writeactivealarmcount) | Write Overview/ActiveAlarmCount/Value as an expression tag that sums | 0 |
| [`clearRebuild`](#clearrebuild) | | 0 |
| [`rebuildOverview`](#rebuildoverview) | Rebuild Overview/Instances/Value plus DeviceCount and ActiveAlarmCount | 0 |
| [`rebuildAllOverviews`](#rebuildalloverviews) | Rebuild every known equipment Overview (used by [default]\_Config/Rebuild). | 0 |
| [`rebuildFromRebuildTag`](#rebuildfromrebuildtag) | Entry point for gateway Tag Change on Overview/.../Rebuild or \_Config/Rebuild. | 2 |
| [`listRebuildPaths`](#listrebuildpaths) | List Overview/\*/Rebuild paths (helper for configuring Tag Change paths). | 0 |

### \_browseName {#_browsename}

```python
def _browseName(br)
```
Line 26 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `discoverPointFields`, `findDevices`

### \_browseFullPath {#_browsefullpath}

```python
def _browseFullPath(br)
```
Line 36 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `_browseTypeId`, `findDevices`

### \_browseTagType {#_browsetagtype}

```python
def _browseTagType(br)
```
Line 46 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `findDevices`

### \_browseTypeId {#_browsetypeid}

```python
def _browseTypeId(br, pathStr=None)
```
Line 56 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
UDT typeId from browse result, else tag configuration.
```

Used inside the module by: `findDevices`

### \_parentPath {#_parentpath}

```python
def _parentPath(pathStr)
```
Line 83 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `_equipmentFolder`, `findDevices`

### \_pathsEqual {#_pathsequal}

```python
def _pathsEqual(a, b)
```
Line 90 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Compare tag paths ignoring trailing slash / provider bracket quirks.
```

Used inside the module by: `findDevices`

### \_naturalSortKey {#_naturalsortkey}

```python
def _naturalSortKey(s)
```
Line 101 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `discoverPointFields`, `findDevices`

### \_isEnabled {#_isenabled}

```python
def _isEnabled(pathStr)
```
Line 106 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `buildInstancesPayload`, `findDevices`

### \_normalizeOverviewPath {#_normalizeoverviewpath}

```python
def _normalizeOverviewPath(tagPath)
```
Line 116 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Accept .../Overview/Rebuild, .../Overview, or equipment folder.
```

Used inside the module by: `rebuildOverview`

### \_equipmentFolder {#_equipmentfolder}

```python
def _equipmentFolder(overviewPath)
```
Line 132 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `rebuildOverview`

### makeTagPathColumn {#maketagpathcolumn}

```python
def makeTagPathColumn()
```
Line 136 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `buildInstancesPayload`

### makeNumericColumn {#makenumericcolumn}

```python
def makeNumericColumn(fieldName)
```
Line 178 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `buildInstancesPayload`

### makeBooleanColumn {#makebooleancolumn}

```python
def makeBooleanColumn(fieldName)
```
Line 220 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `buildInstancesPayload`

### \_includeChild {#_includechild}

```python
def _includeChild(name)
```
Line 262 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `discoverPointFields`, `findDevices`

### \_columnKind {#_columnkind}

```python
def _columnKind(fieldName, valueTagPath)
```
Line 271 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

Used inside the module by: `discoverPointFields`

### discoverPointFields {#discoverpointfields}

```python
def discoverPointFields(templatePath)
```
Line 299 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Return ordered list of (fieldName, kind) from a device UDT template.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `buildInstancesPayload`

### \_isEquipmentDeviceType {#_isequipmentdevicetype}

```python
def _isEquipmentDeviceType(typeId)
```
Line 327 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
True for folder-level device UDTs (Devices/Evaporator, Devices/Pump, …).
False for nested VFDs, Overview UDTs, point UDTs (_Root/Analog), alarms, etc.
```

Used inside the module by: `findDevices`

### findDevices {#finddevices}

```python
def findDevices(folderPath, typeIdFilter=None, _nested=False)
```
Line 341 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Enabled device UDT instances that are direct children of the equipment folder.
Requires typeId under Devices/* (excludes Overview, nested Fans/VFDs, point UDTs).

typeIdFilter: optional exact typeId (e.g. 'Devices/Tank') or suffix ('Tank').
With a typeIdFilter and no direct match, devices one sub-folder down are used instead, named '<folder>/<device>'
(Condensers/Condensers/EC-1A/Fan 1: condenser fans grouped per condenser, 2026-10-01).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `buildInstancesPayload`, `rebuildOverview`

### buildInstancesPayload {#buildinstancespayload}

```python
def buildInstancesPayload(folderPath, templatePath=None, typeIdFilter=None)
```
Line 394 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table binding props.columns` |
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table binding props.data` |
| `00_Pages/Boars Head/Unit/Overview` | view | `root/Table binding props.columns` |
| `00_Pages/Boars Head/Unit/Overview` | view | `root/Table binding props.data` |

Used inside the module by: `buildInstancesPayloadForType`, `rebuildOverview`

### buildInstancesPayloadForType {#buildinstancespayloadfortype}

```python
def buildInstancesPayloadForType(folderPath, typeId)
```
Line 428 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Overview table payload for one Devices/* type under a plant/area folder.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table binding props.columns` |
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table binding props.data` |
| `00_Pages/Boars Head/Unit/Overview` | view | `root/Table binding props.columns` |
| `00_Pages/Boars Head/Unit/Overview` | view | `root/Table binding props.data` |

### writeInstances {#writeinstances}

```python
def writeInstances(overviewPath, payload)
```
Line 433 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `rebuildOverview`

### writeDeviceCount {#writedevicecount}

```python
def writeDeviceCount(overviewPath, count)
```
Line 443 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Lightspeed Overview/DeviceCount/Value — memory Int4 device tally.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `rebuildOverview`

### buildActiveAlarmCountExpression {#buildactivealarmcountexpression}

```python
def buildActiveAlarmCountExpression(devicePaths, targetSuffix='/_Alarms/_Active')
```
Line 455 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Lightspeed pattern: sum({path1/_Alarms/_Active}, {path2/_Alarms/_Active}, ...)
Boolean/active tags coerce to 0/1 in expression sum.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `writeActiveAlarmCount`

### writeActiveAlarmCount {#writeactivealarmcount}

```python
def writeActiveAlarmCount(overviewPath, devicePaths)
```
Line 470 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Write Overview/ActiveAlarmCount/Value as an expression tag that sums
each device's /_Alarms/_Active (Lightspeed Meter/CRAC Overview pattern).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `rebuildOverview`

### clearRebuild {#clearrebuild}

```python
def clearRebuild(rebuildTagPath)
```
Line 498 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

_No docstring._

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `rebuildFromRebuildTag`, `rebuildOverview`

### rebuildOverview {#rebuildoverview}

```python
def rebuildOverview(overviewOrRebuildPath)
```
Line 505 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Rebuild Overview/Instances/Value plus DeviceCount and ActiveAlarmCount
(Lightspeed Overview pattern) for the equipment folder that owns this Overview.
Accepts .../Overview/Rebuild or .../Overview or the equipment folder path.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `rebuildAllOverviews`, `rebuildFromRebuildTag`

### rebuildAllOverviews {#rebuildalloverviews}

```python
def rebuildAllOverviews(provider='default')
```
Line 548 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Rebuild every known equipment Overview (used by [default]_Config/Rebuild).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `rebuildFromRebuildTag`

### rebuildFromRebuildTag {#rebuildfromrebuildtag}

```python
def rebuildFromRebuildTag(rebuildTagPath)
```
Line 564 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
Entry point for gateway Tag Change on Overview/.../Rebuild or _Config/Rebuild.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `overviewRebuild` | gateway tag-change | `onTagChange.py` |
| `rebuildOverviewInstances` | gateway tag-change | `onTagChange.py` |

### listRebuildPaths {#listrebuildpaths}

```python
def listRebuildPaths(provider='default', pathFilter='*')
```
Line 576 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Overview/code.py`.

```text
List Overview/*/Rebuild paths (helper for configuring Tag Change paths).

```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `rebuildAllOverviews`
