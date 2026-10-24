---
title: "_Root/Digital"
sidebar_label: "Digital"
description: "UDT definition _Root/Digital: digital"
generated: true
---

:::note

:::
# UDT `_Root/Digital`

digital

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; \_Root &gt; Digital |
| Tag path | `[default]_types_/_Root/Digital` |
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
| `Value` | Boolean | reference | | | historian, OnChange, db 0.0 Absolute (Discrete) | | | value |

<details>
<summary>State labels (1 members)</summary>

| Member | States (value = label) |
|---|---|
| `Value` | 0 = Off, 1 = On |

</details>

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Config/Interlock](../config/interlock.md) (as `MSet_Bypass00`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass01`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass02`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass03`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass04`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass05`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass06`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass07`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass08`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass09`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass10`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass11`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass12`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass13`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass14`), [Config/Interlock](../config/interlock.md) (as `MSet_Bypass15`), [Config/Interlock](../config/interlock.md) (as `OCmd_Reset`), [Config/Interlock](../config/interlock.md) (as `Rdy_Reset`), [Config/Interlock](../config/interlock.md) (as `Sts_BypActive`), [Config/Interlock](../config/interlock.md) (as `Sts_IntlkOK`), [Config/Interlock](../config/interlock.md) (as `Sts_NBIntlkOK`), [Config/Interlock](../config/interlock.md) (as `Cfg_PCmdClear`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Alm`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Cmd_Auto`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Cmd_Manual`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Cmd_Start`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Cmd_Stop`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Comm`), [Devices/CoolingTower](../devices/coolingtower.md) (as `Failed`), [Devices/CoolingTower](../devices/coolingtower.md) (as `MAINT`), [Devices/CoolingTower](../devices/coolingtower.md) (as `OPER`), [Devices/CoolingTower](../devices/coolingtower.md) (as `PROG`), [Devices/Tank](../devices/tank.md) (as `Interlock/Rdy_Reset`), [Devices/Tank](../devices/tank.md) (as `Interlock/OCmd_Reset`), [Devices/Tank](../devices/tank.md) (as `Interlock/Sts_IntlkOK`), [Devices/VFD](../devices/vfd.md) (as `CMD`), [Devices/VFD](../devices/vfd.md) (as `Fault`), [Devices/LTU](../devices/ltu.md) (as `Cmd_ResetCount`), [Devices/LTU](../devices/ltu.md) (as `Count_Alarm`), [Devices/LTU](../devices/ltu.md) (as `ResetDaily`), [Devices/SuctionSequence](../devices/suctionsequence.md) (as `Cfg_HasEnable`)

8 direct instance(s):

| Instance | Instance page |
|---|---|
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/FIRE` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/MR AD` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/RDISKS` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/VL AD` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Light` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Circuit` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Reset` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Digitals/Alarm Silence` | [Machine Room/Digitals](../../devices/machine-room-digitals.md) |
