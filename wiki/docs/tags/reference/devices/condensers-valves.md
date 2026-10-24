---
title: "Condensers / Valves (Instances)"
sidebar_label: "Condensers / Valves"
description: "Device instances in [default]Boars_Head/GrovePort/Condensers/Valves: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Condensers/Valves`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Condensers &gt; Valves**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Condensers/Valves/udts.json`. 3 UDT instance(s): 3 x [Devices/Valve](../udts/devices/valve.md).

## Main HG CV6

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Valves/Main HG CV6` |
| Type | [Devices/Valve](../udts/devices/valve.md) |
| Label | MAIN HG SV |
| Description | valve. Live PLC \[RCP1\] (read only): ValveTag=MAIN\_HG\_CV6. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `ValveTag` | `MAIN_HG_CV6` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]MAIN_HG_CV6` | 151 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | no | (no PLC object) | |

## Main MW CV25

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Valves/Main MW CV25` |
| Type | [Devices/Valve](../udts/devices/valve.md) |
| Label | CSV MAKEUP SV |
| Description | valve. Live PLC \[RCP1\] (read only): ValveTag=RS\_MW\_CV25, IntlkTag=EC1\_INTLK. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `ValveTag` | `RS_MW_CV25` |
| `IntlkTag` | `EC1_INTLK` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]RS_MW_CV25` | 151 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]EC1_INTLK` | not in mirror |

## Backup MW CV26

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Condensers/Valves/Backup MW CV26` |
| Type | [Devices/Valve](../udts/devices/valve.md) |
| Label | CSV MAKEUP BACKUP SV |
| Description | valve. Live PLC \[RCP1\] (read only): ValveTag=RS\_BACKUP\_MW\_CV26, IntlkTag=EC1\_INTLK. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `ValveTag` | `RS_BACKUP_MW_CV26` |
| `IntlkTag` | `EC1_INTLK` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]RS_BACKUP_MW_CV26` | 151 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]EC1_INTLK` | not in mirror |

