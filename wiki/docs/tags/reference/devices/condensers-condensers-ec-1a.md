---
title: "Condensers / Condensers / EC-1A (Instances)"
sidebar_label: "Condensers / Condensers / EC-1A"
description: "Device instances in [default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Condensers/Condensers/EC-1A`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Condensers &gt; Condensers &gt; EC-1A**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Condensers/Condensers/EC-1A/udts.json`. 2 UDT instance(s): 2 x [Devices/Pump](../udts/devices/pump.md).

## Fan 1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 1` |
| Type | [Devices/Pump](../udts/devices/pump.md) |
| Label | CD1A-FAN #1 |
| Description | pump. Live PLC \[RCP1\] (read only): MotorTag=CD1A\_FAN1, IntlkTag=EC1\_INTLK, RunTimeTag=CD1A\_FAN1\_Runtime. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `MotorTag` | `CD1A_FAN1` |
| `IntlkTag` | `EC1_INTLK` |
| `RunTimeTag` | `CD1A_FAN1_Runtime` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Motor` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CD1A_FAN1` | 108 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]EC1_INTLK` | not in mirror |
| `RunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CD1A_FAN1_Runtime` | 11 tags |

## Fan 2

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 2` |
| Type | [Devices/Pump](../udts/devices/pump.md) |
| Label | CD1A-FAN #2 |
| Description | pump. Live PLC \[RCP1\] (read only): MotorTag=CD1A\_FAN2, IntlkTag=EC1\_INTLK, RunTimeTag=CD1A\_FAN2\_Runtime. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `MotorTag` | `CD1A_FAN2` |
| `IntlkTag` | `EC1_INTLK` |
| `RunTimeTag` | `CD1A_FAN2_Runtime` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Motor` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CD1A_FAN2` | 108 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]EC1_INTLK` | not in mirror |
| `RunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CD1A_FAN2_Runtime` | 11 tags |

