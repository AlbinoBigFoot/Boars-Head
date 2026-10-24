---
title: "Config/_Alarms"
sidebar_label: "_Alarms"
description: "UDT definition Config/_Alarms"
generated: true
---

:::note

:::
# UDT `Config/_Alarms`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; Config &gt; \_Alarms |
| Tag path | `[default]_types_/Config/_Alarms` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Config/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 12 (12 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

_No parameters._

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `_AckHighPriority` | Int4 | reference `[.]../Alarm Metrics.highestAckedPriority` | | | | | | |
| `_Active` | Boolean | reference `[.]../Alarm Metrics.hasActive` | | | | | | |
| `_ActiveCount` | Int4 | reference `[.]../Alarm Metrics.activeUnackCount` | | | | | | |
| `_ActiveCountCritical` | Int4 | reference `[.]../Alarm Metrics.activeCountCritical` | | | | | | |
| `_ActiveCountHigh` | Int4 | reference `[.]../Alarm Metrics.activeCountHigh` | | | | | | |
| `_ActiveCountLow` | Int4 | reference `[.]../Alarm Metrics.activeCountLow` | | | | | | |
| `_ActiveCountMedium` | Int4 | reference `[.]../Alarm Metrics.activeCountMedium` | | | | | | |
| `_ActiveHighPriority` | Int4 | reference `[.]../Alarm Metrics.highestActivePriority` | | | | | | |
| `_Color` | String | expr `case({[.]_HighestPriority},      4, {[~]_Config/Colors/Alarms/Critica…` (full below) | | | | | | |
| `_Flash` | Boolean | expr `if({[.]_AckHighPriority} != {[.]_ActiveHighPriority} && {[.]_Active},…` (full below) | | | | | | |
| `_HighestPriority` | | expr `max({[.]_ActiveHighPriority},  {[.]_AckHighPriority},  -1)` | | | | | | |
| `_Icon` | String | expr `case({[.]_HighestPriority},      4, {[~]_Config/Icons/Alarms/Critical…` (full below) | | | | | | |

<details>
<summary>Full expressions / references (3)</summary>

**`_Color`** (expr)

```
case({[.]_HighestPriority},
     4, {[~]_Config/Colors/Alarms/Critical},
     3, {[~]_Config/Colors/Alarms/High},
     2, {[~]_Config/Colors/Alarms/Medium},
     1, {[~]_Config/Colors/Alarms/Low},
     '')
```

**`_Flash`** (expr)

```
if({[.]_AckHighPriority} != {[.]_ActiveHighPriority} && {[.]_Active},
	{[~]_Config/Flash},
	True
)
```

**`_Icon`** (expr)

```
case({[.]_HighestPriority},
     4, {[~]_Config/Icons/Alarms/Critical},
     3, {[~]_Config/Icons/Alarms/High},
     2, {[~]_Config/Icons/Alarms/Medium},
     1, {[~]_Config/Icons/Alarms/Low},
     {[~]_Config/Icons/Blank})
```


</details>

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/Valve](../devices/valve.md) (as `_Alarms`), [Devices/Compressor](../devices/compressor.md) (as `_Alarms`), [Devices/CoolingTower](../devices/coolingtower.md) (as `_Alarms`), [Devices/Pump](../devices/pump.md) (as `_Alarms`), [Devices/ExhaustFan](../devices/exhaustfan.md) (as `_Alarms`), [Devices/Tank](../devices/tank.md) (as `_Alarms`), [Devices/Sensor](../devices/sensor.md) (as `_Alarms`), [Devices/Evaporator](../devices/evaporator.md) (as `_Alarms`), [Devices/LTU](../devices/ltu.md) (as `_Alarms`), [Devices/SafetyRelay](../devices/safetyrelay.md) (as `_Alarms`), [Units/AHU](../units/ahu.md) (as `_Alarms`)

Reached through nesting by 56 top-level instance(s).
