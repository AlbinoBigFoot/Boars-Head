---
title: "shared.Enums"
sidebar_label: "shared.Enums"
description: "Script module shared.Enums: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`  
**Lines:** 137. **Functions:** 9. **Called as:** `shared.Enums.<function>(...)`

## What the source says

```text
Code -> text enums (evap-defrost-strings, 2026-10-22).

One source of truth per enum: a memory DataSet tag [default]_Config/Enums/<Group>/<Name> with the columns
value (Int4), label, short (String), selectable (Boolean), plus optional extras (PlcState: hmiStatus).
Expressions read the tag with lookup(), e.g.
        lookup({[default]_Config/Enums/Evaporator/CycleFans}, toInt(x), toStr(x), 'value', 'label')
and scripts use the functions below. Every function is fail-safe: on any error it falls back to the raw value.
Docs: docs/evaporator-hmi-components.md.
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.tag` |
| Calls modules | [shared.Alerts](./shared-alerts.md), [shared.Audit](./shared-audit.md) |
| Called by modules | [shared.Alerts](./shared-alerts.md), [shared.Audit](./shared-audit.md) |

<details>
<summary>Module constants (2)</summary>

| Name | Value |
|---|---|
| `ROOT` | `'[default]_Config/Enums/'` |
| `MEMBERS` | `{'Cfg_DefrostStartMode': 'Evaporator/DefrostStartMode', '...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_int`](#_int) (internal) | Integral numbers (2, 2.0, '2') -&gt; int; anything else (None, bool, 1.5, text) -&gt; None. | 0 |
| [`_tagPath`](#_tagpath) (internal) | | 0 |
| [`rows`](#rows) | Rows as dicts \{value, label, short, selectable, &lt;extra columns&gt;\} in tag order; [] if the tag is missing / bad. | 0 |
| [`_find`](#_find) (internal) | | 0 |
| [`label`](#label) | Long text for value ('Time Of Day'); default (None) when there is no match. | 0 |
| [`short`](#short) | Short text for value ('ToD'); default (None) when there is no match. | 0 |
| [`options`](#options) | Dropdown options [\{value, label, isDisabled\}]: every row; rows with selectable false stay listed but disabled | 1 |
| [`forTagPath`](#fortagpath) | Enum path for a member tag path ('.../CG-E2/Cfg\_DefrostStartMode/Value', '[RCP1]CG[3].Cfg\_CycFans'), or None. | 0 |
| [`describe`](#describe) | 'Time Of Day (0)' when the member has an enum and the value a row; otherwise the raw value as text. | 2 |

### \_int {#_int}

```python
def _int(value)
```
Line 21 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

```text
Integral numbers (2, 2.0, '2') -> int; anything else (None, bool, 1.5, text) -> None.
```

Used inside the module by: `_find`, `options`, `rows`

### \_tagPath {#_tagpath}

```python
def _tagPath(enumPath)
```
Line 33 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

_No docstring._

Used inside the module by: `rows`

### rows {#rows}

```python
def rows(enumPath, dataset=None)
```
Line 40 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

```text
Rows as dicts {value, label, short, selectable, <extra columns>} in tag order; [] if the tag is missing / bad.

dataset: the DataSet when the caller already has it (a binding), so no tag read is needed.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `_find`, `options`

### \_find {#_find}

```python
def _find(enumPath, value, dataset=None)
```
Line 75 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

_No docstring._

Used inside the module by: `describe`, `label`, `short`

### label {#label}

```python
def label(enumPath, value, default=None)
```
Line 85 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

```text
Long text for value ('Time Of Day'); default (None) when there is no match.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### short {#short}

```python
def short(enumPath, value, default=None)
```
Line 91 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

```text
Short text for value ('ToD'); default (None) when there is no match.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### options {#options}

```python
def options(enumPath, current=None, dataset=None)
```
Line 97 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

```text
Dropdown options [{value, label, isDisabled}]: every row; rows with selectable false stay listed but disabled
(so the dropdown still shows a mode only the PLC can set). A current value missing from the enum is appended,
disabled, so it shows as itself instead of a blank dropdown.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `03_Elements/00_Control/MultiStateInput` | view | `root/StateSelect binding props.options` |

### forTagPath {#fortagpath}

```python
def forTagPath(tagPath)
```
Line 110 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

```text
Enum path for a member tag path ('.../CG-E2/Cfg_DefrostStartMode/Value', '[RCP1]CG[3].Cfg_CycFans'), or None.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

Used inside the module by: `describe`

### describe {#describe}

```python
def describe(tagPath, value, enumPath=None)
```
Line 127 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Enums/code.py`.

```text
'Time Of Day (0)' when the member has an enum and the value a row; otherwise the raw value as text.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.Alerts._describe` | script | |
| `shared.Audit._describe` | script | |
