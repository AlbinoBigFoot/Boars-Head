---
title: "Club / Utility (Instances)"
sidebar_label: "Club / Utility"
description: "Device instances in [default]Boars_Head/GrovePort/Club/Utility: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Club/Utility`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Club &gt; Utility**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Club/Utility/udts.json`. 1 UDT instance(s): 1 x [Devices/Evaporator](../udts/devices/evaporator.md).

## CG-C1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Club/Utility/CG-C1` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-C1 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[5\], ZATTag=CG\_ZAT\[5\], IntlkTag=CG\_Interlock\[5\], FansTag=CG\_Fans\[5\], FansRunTimeTag=CG\_Fans\_Runtime\[5\], LiquidSVTag=CG\_Liquid\_SV\[5\], SuctionSVTag=CG\_Suction\_SV\[5\], HotGasSVTag=CG\_HotGas\_SV\[5\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[5]` |
| `ZATTag` | `CG_ZAT[5]` |
| `IntlkTag` | `CG_Interlock[5]` |
| `FansTag` | `CG_Fans[5]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[5]` |
| `LiquidSVTag` | `CG_Liquid_SV[5]` |
| `SuctionSVTag` | `CG_Suction_SV[5]` |
| `HotGasSVTag` | `CG_HotGas_SV[5]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[5]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[5]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | no | (no PLC object) | |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | no | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[5]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[5]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[5]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[5]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[5]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[5]` | 11 tags |

