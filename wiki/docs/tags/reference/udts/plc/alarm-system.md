---
title: "PLC/Alarm_System"
sidebar_label: "Alarm_System"
description: "UDT definition PLC/Alarm_System"
generated: true
---

:::note

:::
# UDT `PLC/Alarm_System`

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; PLC &gt; Alarm\_System |
| Tag path | `[default]_types_/PLC/Alarm_System` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/PLC/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 14 (14 atomic, 0 nested UDT, 0 folders) |
| Status | unused (raw L5K import) |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `TagPrefix` | String | - | own |
| `Description` | String | `Main PLC Alarm Management structure` | own |
| `DeviceName` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## OPC Item Path

14 members read OPC through the server `Ignition OPC UA Server`. Pattern: `ns=1;s=[{DeviceName}]{TagPrefix}.<member>`, so an instance with `DeviceName = RCP1` and `TagPrefix = X` reads `ns=1;s=[RCP1]X.<member>`. The Source column below shows the part after `[{DeviceName}]`.

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `CR_Alarm` | Boolean | OPC `{TagPrefix}.CR_Alarm` | | yes | | | | Alarm relay to external monitoring system |
| `CR_Horn` | Boolean | OPC `{TagPrefix}.CR_Horn` | | yes | | | | Silencable alarm horn |
| `CR_Light` | Boolean | OPC `{TagPrefix}.CR_Light` | | yes | | | | Alarm light |
| `CR_Reset` | Boolean | OPC `{TagPrefix}.CR_Reset` | | yes | | | | Digital Output to trigger hardwired alarm reset circuit |
| `Count` | Int4 | OPC `{TagPrefix}.Count` | | yes | | | | Total of current, active alarms |
| `HMI_Reset` | Boolean | OPC `{TagPrefix}.HMI_Reset` | | yes | | | | HMI Reset$NSet to $Q1$Q to reset all alarms |
| `HMI_Silence` | Boolean | OPC `{TagPrefix}.HMI_Silence` | | yes | | | | HMI Silence$NSet to $Q1$Q to silence all alarms |
| `HSA_Reset` | Boolean | OPC `{TagPrefix}.HSA_Reset` | | yes | | | | Alarm Reset Pushbutton |
| `HSA_Silence` | Boolean | OPC `{TagPrefix}.HSA_Silence` | | yes | | | | Alarm Silence Pushbutton |
| `Reset_Latch` | Boolean | OPC `{TagPrefix}.Reset_Latch` | | yes | | | | |
| `Sil_Count` | Int4 | OPC `{TagPrefix}.Sil_Count` | | yes | | | | Number of silenced system alarms |
| `Silence_Latch` | Boolean | OPC `{TagPrefix}.Silence_Latch` | | yes | | | | |
| `ZZZZZZZZZZAlarm_Syst0` | Int1 | OPC `{TagPrefix}.ZZZZZZZZZZAlarm_Syst0` | | yes | | | | |
| `ZZZZZZZZZZAlarm_Syst9` | Int1 | OPC `{TagPrefix}.ZZZZZZZZZZAlarm_Syst9` | | yes | | | | |

## Alarms

_No alarms defined on this type._

## Used By

Not used by any instance or other UDT (raw L5K import kept for reference).
