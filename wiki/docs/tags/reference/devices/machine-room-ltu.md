---
title: "Machine Room / LTU (Instances)"
sidebar_label: "Machine Room / LTU"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/LTU: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/LTU`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; LTU**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/LTU/udts.json`. 1 UDT instance(s): 1 x [Devices/LTU](../udts/devices/ltu.md).

## NH3 LTU

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/LTU/NH3 LTU` |
| Type | [Devices/LTU](../udts/devices/ltu.md) |
| Label | NH3 LTU |
| Description | NH3 liquid transfer unit |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `InputTag` | `NH3_LTU` |
| `CountTag` | `NH3_LTU_HMI_Count` |
| `CountAlarmTag` | `NH3_LTU_Count_Alarm_Inp` |
| `CountAlarmSPTag` | `NH3_LTU_Count_Alarm_SP` |
| `ResetCountTag` | `HMI_Ltu_Clear` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Input/DIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]NH3_LTU` | 52 tags |
| `PlcCount` | OPC atomic | yes | `ns=1;s=[RCP1]NH3_LTU_HMI_Count` | 1 tags |
| `PlcCountAlarm` | OPC atomic | yes | `ns=1;s=[RCP1]NH3_LTU_Count_Alarm_Inp` | 1 tags |
| `PlcCountAlarmSP` | OPC atomic | yes | `ns=1;s=[RCP1]NH3_LTU_Count_Alarm_SP` | 1 tags |
| `PlcResetCount` | OPC atomic | yes | `ns=1;s=[RCP1]HMI_Ltu_Clear` | 1 tags |

