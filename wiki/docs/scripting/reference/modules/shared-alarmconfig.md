---
title: "shared.AlarmConfig"
sidebar_label: "shared.AlarmConfig"
description: "Script module shared.AlarmConfig: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`  
**Lines:** 419. **Functions:** 12. **Called as:** `shared.AlarmConfig.<function>(...)`

## What the source says

```text
List alarm-configured leaves under a device for Faceplate Alarm Configuration.
Prefer explicit Alm_*/Value candidates — recursive browse often skips nested Digitals.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag`, `system.util` |
| Logger names | `shared.AlarmConfig` |
| Calls modules | [shared.Audit](./shared-audit.md), [shared.Security](./shared-security.md) |

<details>
<summary>Module constants (5)</summary>

| Name | Value |
|---|---|
| `_EXPLICIT_ALMS` | `('Alm_IOFault', 'Alm_FullStall', 'Alm_TransitStall', 'Alm...` |
| `_ALM_LABELS` | `{'Alm_IOFault': 'I/O Fault', 'Alm_FullStall': 'Full Stall...` |
| `_GENERIC_ALARM_NAMES` | `set(['Alarm', 'Value', 'Alm', ''])` |
| `_SETPOINT_MODES` | `set(['AboveSetpoint', 'BelowSetpoint', 'BetweenSetpoints'...` |
| `_DIGITAL_MODES` | `set(['Equality', 'Inequality', 'AnyChange', 'Bit', 'OnCha...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_parseHidden`](#_parsehidden) (internal) | | 0 |
| [`_isHidden`](#_ishidden) (internal) | | 0 |
| [`_isNoise`](#_isnoise) (internal) | | 0 |
| [`_modeName`](#_modename) (internal) | | 0 |
| [`_dataTypeName`](#_datatypename) (internal) | | 0 |
| [`_browseCandidates`](#_browsecandidates) (internal) | Return candidate tag paths under root (browse + explicit Alm\_\* leaves). | 0 |
| [`_alarmsOn`](#_alarmson) (internal) | Return (resolvedPath, nodeCfg, alarmsList) or (None, None, None). | 0 |
| [`_folderName`](#_foldername) (internal) | | 0 |
| [`_humanize`](#_humanize) (internal) | | 0 |
| [`_labelFor`](#_labelfor) (internal) | | 0 |
| [`listAlarms`](#listalarms) | Return rows for Alarm Configuration flex-repeater: | 1 |
| [`applyOverride`](#applyoverride) | Merge priority/mode onto the instance alarm (UDT instance override). | 1 |

### \_parseHidden {#_parsehidden}

```python
def _parseHidden(text)
```
Line 42 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `listAlarms`

### \_isHidden {#_ishidden}

```python
def _isHidden(fullPath, hidden_set)
```
Line 57 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `listAlarms`

### \_isNoise {#_isnoise}

```python
def _isNoise(fullPath)
```
Line 81 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `_browseCandidates`

### \_modeName {#_modename}

```python
def _modeName(mode)
```
Line 89 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `listAlarms`

### \_dataTypeName {#_datatypename}

```python
def _dataTypeName(dt)
```
Line 103 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `listAlarms`

### \_browseCandidates {#_browsecandidates}

```python
def _browseCandidates(root_path)
```
Line 114 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

```text
Return candidate tag paths under root (browse + explicit Alm_* leaves).
```

Used inside the module by: `listAlarms`

### \_alarmsOn {#_alarmson}

```python
def _alarmsOn(path)
```
Line 154 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

```text
Return (resolvedPath, nodeCfg, alarmsList) or (None, None, None).

Only real getConfiguration alarm definitions — do not invent rows from
AlarmEvalEnabled (that property is True for many non-alarmed leaves).
```

Used inside the module by: `listAlarms`

### \_folderName {#_foldername}

```python
def _folderName(full_path)
```
Line 185 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `_labelFor`, `listAlarms`

### \_humanize {#_humanize}

```python
def _humanize(token)
```
Line 198 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `_labelFor`, `listAlarms`

### \_labelFor {#_labelfor}

```python
def _labelFor(full_path, node, root_path)
```
Line 218 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

_No docstring._

Used inside the module by: `listAlarms`

### listAlarms {#listalarms}

```python
def listAlarms(tagPath, hiddenTags='')
```
Line 241 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

```text
Return rows for Alarm Configuration flex-repeater:
[{tagPath, alarmName, label, isDigital, hasSetpoint, mode}, ...]
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/AlarmConfiguration` | view | `binding custom.tags` |

### applyOverride {#applyoverride}

```python
def applyOverride(tagPath, alarmName, priority=None, mode=None, viewName=None)
```
Line 322 of `gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py`.

```text
Merge priority/mode onto the instance alarm (UDT instance override).

Boolean alarms use WhenTrue / WhenFalse (not Equality).
Successful changes are written to OpsAudit.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root message handler writeValue` |
