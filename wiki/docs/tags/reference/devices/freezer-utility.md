---
title: "Freezer / Utility (Instances)"
sidebar_label: "Freezer / Utility"
description: "Device instances in [default]Boars_Head/GrovePort/Freezer/Utility: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Freezer/Utility`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Freezer &gt; Utility**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Freezer/Utility/udts.json`. 2 UDT instance(s): 2 x [Devices/Evaporator](../udts/devices/evaporator.md).

## CG-A2

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-A2 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[2\], ZATTag=CG\_ZAT\[2\], IntlkTag=CG\_Interlock\[2\], FansTag=CG\_Fans\[2\], FansRunTimeTag=CG\_Fans\_Runtime\[2\], LiquidSVTag=CG\_Liquid\_SV\[2\], SuctionSVTag=CG\_Suction\_SV\[2\], HotGasSVTag=CG\_HotGas\_SV\[2\], BleedSVTag=CG\_Bleed\_SV\[2\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[2]` |
| `ZATTag` | `CG_ZAT[2]` |
| `IntlkTag` | `CG_Interlock[2]` |
| `FansTag` | `CG_Fans[2]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[2]` |
| `LiquidSVTag` | `CG_Liquid_SV[2]` |
| `SuctionSVTag` | `CG_Suction_SV[2]` |
| `HotGasSVTag` | `CG_HotGas_SV[2]` |
| `BleedSVTag` | `CG_Bleed_SV[2]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[2]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[2]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[2]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[2]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[2]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[2]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[2]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[2]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[2]` | 11 tags |

## CG-A1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-A1 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[1\], ZATTag=CG\_ZAT\[1\], IntlkTag=CG\_Interlock\[1\], FansTag=CG\_Fans\[1\], FansRunTimeTag=CG\_Fans\_Runtime\[1\], LiquidSVTag=CG\_Liquid\_SV\[1\], SuctionSVTag=CG\_Suction\_SV\[1\], HotGasSVTag=CG\_HotGas\_SV\[1\], BleedSVTag=CG\_Bleed\_SV\[1\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[1]` |
| `ZATTag` | `CG_ZAT[1]` |
| `IntlkTag` | `CG_Interlock[1]` |
| `FansTag` | `CG_Fans[1]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[1]` |
| `LiquidSVTag` | `CG_Liquid_SV[1]` |
| `SuctionSVTag` | `CG_Suction_SV[1]` |
| `HotGasSVTag` | `CG_HotGas_SV[1]` |
| `BleedSVTag` | `CG_Bleed_SV[1]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[1]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[1]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[1]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[1]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[1]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[1]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[1]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[1]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[1]` | 11 tags |

