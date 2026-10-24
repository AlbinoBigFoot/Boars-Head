---
title: "Condensers / Tanks (Instances)"
sidebar_label: "Condensers / Tanks"
description: "Device instances in [default]Boars_Head/GrovePort/Condensers/Tanks: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Condensers/Tanks`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Condensers &gt; Tanks**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Condensers/Tanks/udts.json`. 1 UDT instance(s): 1 x [Devices/Tank](../udts/devices/tank.md).

## CSV

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Tanks/CSV` |
| Type | [Devices/Tank](../udts/devices/tank.md) |
| Label | CSV |
| Description | tank. Live PLC \[RCP1\] (read only): LevelTag=LT\_CSV, LevelEU=In". PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `LevelTag` | `LT_CSV` |
| `LevelEU` | `In"` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `LvlAIn` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]LT_CSV` | 174 tags |
| `PressAIn` | [PLC\_Ref/P\_AIn](../udts/plc-ref/p-ain.md) | no | reference to `(empty)` | |
| `HlcoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `HiHiDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `OplDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `LoLoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `Pump1Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `Pump2Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `StartPress` | OPC atomic | yes | `ns=1;s=[RCP1]` | |
| `LeadPump` | OPC atomic | yes | `ns=1;s=[RCP1]` | |

