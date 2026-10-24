---
title: "Machine Room / Tanks (Instances)"
sidebar_label: "Machine Room / Tanks"
description: "Device instances in [default]Boars_Head/GrovePort/Machine Room/Tanks: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Machine Room/Tanks`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Machine Room &gt; Tanks**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Machine Room/Tanks/udts.json`. 4 UDT instance(s): 3 x [Devices/Tank](../udts/devices/tank.md), 1 x [Overview/Tank Overview](../udts/overview/tank-overview.md).

## HTR

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR` |
| Type | [Devices/Tank](../udts/devices/tank.md) |
| Label | HTR |
| Description | tank. Live PLC \[RCP1\] (read only): LevelTag=HT\_LVL, PressSource=\[default\]Boars\_Head/GrovePort/Machine Room/Sensors/HSS-Pumps Pressure/AIn, HLCOTag=HTR\_HLCO, HiHiTag=HTR\_HIHI, OPLTag=HTR\_OPL, LoLoTag=HTR\_LOLO, Pump1AlmTag=HTR\_PUMPS\_ALM\[1\], Pump2AlmTag=HTR\_PUMPS\_ALM\[2\], StartPressTag=HTPS\_SET, LeadTag=HTRL\_PUMPS\_SEQ.Cfg\_Lead, LevelEU=%, PressEU=PSIG. PLC parts only (flat stand-ins removed 2026-10-2… |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `LevelTag` | `HT_LVL` |
| `PressSource` | `[default]Boars_Head/GrovePort/Machine Room/Sensors/HSS-Pumps Pressure/AIn` |
| `HLCOTag` | `HTR_HLCO` |
| `HiHiTag` | `HTR_HIHI` |
| `OPLTag` | `HTR_OPL` |
| `LoLoTag` | `HTR_LOLO` |
| `Pump1AlmTag` | `HTR_PUMPS_ALM[1]` |
| `Pump2AlmTag` | `HTR_PUMPS_ALM[2]` |
| `StartPressTag` | `HTPS_SET` |
| `LeadTag` | `HTRL_PUMPS_SEQ.Cfg_Lead` |
| `LevelEU` | `%` |
| `PressEU` | `PSIG` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `LvlAIn` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]HT_LVL` | 174 tags |
| `PressAIn` | [PLC\_Ref/P\_AIn](../udts/plc-ref/p-ain.md) | yes | reference to `[default]Boars_Head/GrovePort/Machine Room/Sensors/HSS-Pumps Pressure/AIn` | |
| `HlcoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]HTR_HLCO` | 52 tags |
| `HiHiDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]HTR_HIHI` | 52 tags |
| `OplDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]HTR_OPL` | 52 tags |
| `LoLoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]HTR_LOLO` | 52 tags |
| `Pump1Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]HTR_PUMPS_ALM[1]` | 52 tags |
| `Pump2Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]HTR_PUMPS_ALM[2]` | 52 tags |
| `StartPress` | OPC atomic | yes | `ns=1;s=[RCP1]HTPS_SET` | 1 tags |
| `LeadPump` | OPC atomic | yes | `ns=1;s=[RCP1]HTRL_PUMPS_SEQ.Cfg_Lead` | 1 tags |

## LTR

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Tanks/LTR` |
| Type | [Devices/Tank](../udts/devices/tank.md) |
| Label | LTR |
| Description | tank. Live PLC \[RCP1\] (read only): LevelTag=LT\_LVL, PressSource=\[default\]Boars\_Head/GrovePort/Machine Room/Sensors/LSS-Pumps Pressure/AIn, HLCOTag=LTR\_HLCO, HiHiTag=LTR\_HIHI, OPLTag=LTR\_OPL, LoLoTag=LTR\_LOLO, Pump1AlmTag=LTR\_PUMPS\_ALM\[1\], Pump2AlmTag=LTR\_PUMPS\_ALM\[2\], StartPressTag=LTPS\_SET, LeadTag=LTRL\_PUMPS\_SEQ.Cfg\_Lead, LevelEU=%, PressEU=PSIG. PLC parts only (flat stand-ins removed 2026-10-2… |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `LevelTag` | `LT_LVL` |
| `PressSource` | `[default]Boars_Head/GrovePort/Machine Room/Sensors/LSS-Pumps Pressure/AIn` |
| `HLCOTag` | `LTR_HLCO` |
| `HiHiTag` | `LTR_HIHI` |
| `OPLTag` | `LTR_OPL` |
| `LoLoTag` | `LTR_LOLO` |
| `Pump1AlmTag` | `LTR_PUMPS_ALM[1]` |
| `Pump2AlmTag` | `LTR_PUMPS_ALM[2]` |
| `StartPressTag` | `LTPS_SET` |
| `LeadTag` | `LTRL_PUMPS_SEQ.Cfg_Lead` |
| `LevelEU` | `%` |
| `PressEU` | `PSIG` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `LvlAIn` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]LT_LVL` | 174 tags |
| `PressAIn` | [PLC\_Ref/P\_AIn](../udts/plc-ref/p-ain.md) | yes | reference to `[default]Boars_Head/GrovePort/Machine Room/Sensors/LSS-Pumps Pressure/AIn` | |
| `HlcoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]LTR_HLCO` | 52 tags |
| `HiHiDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]LTR_HIHI` | 52 tags |
| `OplDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]LTR_OPL` | 52 tags |
| `LoLoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]LTR_LOLO` | 52 tags |
| `Pump1Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]LTR_PUMPS_ALM[1]` | 52 tags |
| `Pump2Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]LTR_PUMPS_ALM[2]` | 52 tags |
| `StartPress` | OPC atomic | yes | `ns=1;s=[RCP1]LTPS_SET` | 1 tags |
| `LeadPump` | OPC atomic | yes | `ns=1;s=[RCP1]LTRL_PUMPS_SEQ.Cfg_Lead` | 1 tags |

## Overview

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Tanks/Overview` |
| Type | [Overview/Tank Overview](../udts/overview/tank-overview.md) |

## HPR

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Machine Room/Tanks/HPR` |
| Type | [Devices/Tank](../udts/devices/tank.md) |
| Label | HPR |
| Description | tank. Live PLC \[RCP1\] (read only): LevelTag=LT\_HPR, LoLoTag=HPR\_LOLO, LevelEU=%. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `LevelTag` | `LT_HPR` |
| `LoLoTag` | `HPR_LOLO` |
| `LevelEU` | `%` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `LvlAIn` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]LT_HPR` | 174 tags |
| `PressAIn` | [PLC\_Ref/P\_AIn](../udts/plc-ref/p-ain.md) | no | reference to `(empty)` | |
| `HlcoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `HiHiDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `OplDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `LoLoDIn` | [PLC/P\_DIn](../udts/plc/p-din.md) | yes | `[RCP1]HPR_LOLO` | 52 tags |
| `Pump1Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `Pump2Alm` | [PLC/P\_DIn](../udts/plc/p-din.md) | no | (no PLC object) | |
| `StartPress` | OPC atomic | yes | `ns=1;s=[RCP1]` | |
| `LeadPump` | OPC atomic | yes | `ns=1;s=[RCP1]` | |

