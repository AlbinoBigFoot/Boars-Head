---
title: "_Root/Analog"
sidebar_label: "Analog"
description: "UDT definition _Root/Analog: analog"
generated: true
---

:::note

:::
# UDT `_Root/Analog`

analog

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; \_Root &gt; Analog |
| Tag path | `[default]_types_/_Root/Analog` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/_Root/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 1 (1 atomic, 0 nested UDT, 0 folders) |
| Status | in use |

## Parameters

_No parameters._

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Value` | Float4 | reference | | | historian, OnChange, db 0.01 Absolute (Discrete) | | | value |

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Config/Interlock](../config/interlock.md) (as `Cfg_Bypassable`), [Config/Interlock](../config/interlock.md) (as `Sts_FirstOut`), [Config/Interlock](../config/interlock.md) (as `Sts_Intlk`), [Config/Interlock](../config/interlock.md) (as `Cfg_OKState`), [Config/Interlock](../config/interlock.md) (as `Cfg_Latched`), [Config/Interlock](../config/interlock.md) (as `Cfg_HasNav`), [Devices/Valve](../devices/valve.md) (as `Cmd_Position`), [Devices/CoolingTower](../devices/coolingtower.md) (as `MotorStarts`), [Devices/CoolingTower](../devices/coolingtower.md) (as `RuntimeHours`), [Devices/CoolingTower](../devices/coolingtower.md) (as `SPD_FBK`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Temp`), [Devices/VFD](../devices/vfd.md) (as `SPD_FBK`), [Devices/LTU](../devices/ltu.md) (as `Count`), [Devices/LTU](../devices/ltu.md) (as `Count_Alarm_SP`), [Devices/LTU](../devices/ltu.md) (as `ResetTime`), [Devices/SuctionSequence](../devices/suctionsequence.md) (as `Cfg_Positions`), [Units/AHU](../units/ahu.md) (as `Temp`)

Reached through nesting by 26 top-level instance(s).
