---
title: "East PH / Utility (Instances)"
sidebar_label: "East PH / Utility"
description: "Device instances in [default]Boars_Head/GrovePort/East PH/Utility: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/East PH/Utility`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; East PH &gt; Utility**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/East PH/Utility/udts.json`. 4 UDT instance(s): 4 x [Devices/Evaporator](../udts/devices/evaporator.md).

## CG-E2

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/East PH/Utility/CG-E2` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-E2 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[8\], ZATTag=CG\_ZAT\[8\], IntlkTag=CG\_Interlock\[8\], FansTag=CG\_Fans\[8\], FansRunTimeTag=CG\_Fans\_Runtime\[8\], LiquidSVTag=CG\_Liquid\_SV\[8\], SuctionSVTag=CG\_Suction\_SV\[8\], HotGasSVTag=CG\_HotGas\_SV\[8\], BleedSVTag=CG\_Bleed\_SV\[8\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[8]` |
| `ZATTag` | `CG_ZAT[8]` |
| `IntlkTag` | `CG_Interlock[8]` |
| `FansTag` | `CG_Fans[8]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[8]` |
| `LiquidSVTag` | `CG_Liquid_SV[8]` |
| `SuctionSVTag` | `CG_Suction_SV[8]` |
| `HotGasSVTag` | `CG_HotGas_SV[8]` |
| `BleedSVTag` | `CG_Bleed_SV[8]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[8]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[8]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[8]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[8]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[8]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[8]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[8]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[8]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[8]` | 11 tags |

## CG-E4

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/East PH/Utility/CG-E4` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-E4 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[10\], ZATTag=CG\_ZAT\[10\], IntlkTag=CG\_Interlock\[10\], FansTag=CG\_Fans\[10\], FansRunTimeTag=CG\_Fans\_Runtime\[10\], LiquidSVTag=CG\_Liquid\_SV\[10\], SuctionSVTag=CG\_Suction\_SV\[10\], HotGasSVTag=CG\_HotGas\_SV\[10\], BleedSVTag=CG\_Bleed\_SV\[10\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[10]` |
| `ZATTag` | `CG_ZAT[10]` |
| `IntlkTag` | `CG_Interlock[10]` |
| `FansTag` | `CG_Fans[10]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[10]` |
| `LiquidSVTag` | `CG_Liquid_SV[10]` |
| `SuctionSVTag` | `CG_Suction_SV[10]` |
| `HotGasSVTag` | `CG_HotGas_SV[10]` |
| `BleedSVTag` | `CG_Bleed_SV[10]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[10]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[10]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[10]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[10]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[10]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[10]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[10]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[10]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[10]` | 11 tags |

## CG-E1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/East PH/Utility/CG-E1` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-E1 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[7\], ZATTag=CG\_ZAT\[7\], IntlkTag=CG\_Interlock\[7\], FansTag=CG\_Fans\[7\], FansRunTimeTag=CG\_Fans\_Runtime\[7\], LiquidSVTag=CG\_Liquid\_SV\[7\], SuctionSVTag=CG\_Suction\_SV\[7\], HotGasSVTag=CG\_HotGas\_SV\[7\], BleedSVTag=CG\_Bleed\_SV\[7\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[7]` |
| `ZATTag` | `CG_ZAT[7]` |
| `IntlkTag` | `CG_Interlock[7]` |
| `FansTag` | `CG_Fans[7]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[7]` |
| `LiquidSVTag` | `CG_Liquid_SV[7]` |
| `SuctionSVTag` | `CG_Suction_SV[7]` |
| `HotGasSVTag` | `CG_HotGas_SV[7]` |
| `BleedSVTag` | `CG_Bleed_SV[7]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[7]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[7]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[7]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[7]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[7]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[7]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[7]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[7]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[7]` | 11 tags |

## CG-E3

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/East PH/Utility/CG-E3` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-E3 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[9\], ZATTag=CG\_ZAT\[9\], IntlkTag=CG\_Interlock\[9\], FansTag=CG\_Fans\[9\], FansRunTimeTag=CG\_Fans\_Runtime\[9\], LiquidSVTag=CG\_Liquid\_SV\[9\], SuctionSVTag=CG\_Suction\_SV\[9\], HotGasSVTag=CG\_HotGas\_SV\[9\], BleedSVTag=CG\_Bleed\_SV\[9\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[9]` |
| `ZATTag` | `CG_ZAT[9]` |
| `IntlkTag` | `CG_Interlock[9]` |
| `FansTag` | `CG_Fans[9]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[9]` |
| `LiquidSVTag` | `CG_Liquid_SV[9]` |
| `SuctionSVTag` | `CG_Suction_SV[9]` |
| `HotGasSVTag` | `CG_HotGas_SV[9]` |
| `BleedSVTag` | `CG_Bleed_SV[9]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[9]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[9]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[9]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[9]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[9]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[9]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[9]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[9]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[9]` | 11 tags |

