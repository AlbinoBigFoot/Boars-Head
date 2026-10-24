---
title: "shared.TrendHistorized"
sidebar_label: "shared.TrendHistorized"
description: "Script module shared.TrendHistorized: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendHistorized/code.py`  
**Lines:** 330. **Functions:** 2. **Called as:** `shared.TrendHistorized.<function>(...)`

## What the source says

```text


Historized-tag index used by shared.TrendContext (no tag reads, no getConfiguration):
  TYPES      typeId -> '|'-joined historized member paths (nested UDT instances expanded, String left out)
  INSTANCES  top-level UDT instance path (no provider, [default]) -> typeId
  TAGS       standalone historized atomic tags (no provider)
  OVERRIDES  instance member historyEnabled overrides (path -> bool)
  NESTED_LABELS / MEMBER_LABELS  pen label parts; UNITS  member leaf -> static engUnit
```

<details>
<summary>Module constants (9)</summary>

| Name | Value |
|---|---|
| `TYPES` | `{'Config/Interlock': 'Cfg_Bypassable/Value\|Cfg_HasNav/Val...` |
| `INSTANCES` | `{'Boars_Head/GrovePort/Club/Detectors/AD03': 'Devices/Dis...` |
| `TAGS` | `'Boars_Head/GrovePort/Production/FCM/HND/OEE/Value\|Boars_...` |
| `OVERRIDES` | `{}` |
| `LEGACY` | `{'Devices/Evaporator': {'Temp': 'ZAT/Val', 'Temp/Value': ...` |
| `NESTED_LABELS` | `{'AIn': u'', 'AInRef': u'', 'CG': u'', 'Comp': u'', 'DIn'...` |
| `MEMBER_LABELS` | `{'AIDefrostStart': u'Defrost Start', 'AIDefrostStop': u'D...` |
| `UNITS` | `{'Amps': u'A', 'DisP': u'psi', 'DisT': u'°F', 'FLA': u'%'...` |
| `_SETS` | `{}` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`members`](#members) | Set of historized member paths for a UDT type (cached). | 0 |
| [`tags`](#tags) | Set of standalone historized atomic tag paths (cached). | 0 |

### members {#members}

```python
def members(typeId)
```
Line 315 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendHistorized/code.py`.

```text
Set of historized member paths for a UDT type (cached).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### tags {#tags}

```python
def tags()
```
Line 324 of `gateways/standard/data/projects/BH/ignition/script-python/shared/TrendHistorized/code.py`.

```text
Set of standalone historized atomic tag paths (cached).
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._
