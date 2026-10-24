---
title: "Dock / Utility (Instances)"
sidebar_label: "Dock / Utility"
description: "Device instances in [default]Boars_Head/GrovePort/Dock/Utility: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/Dock/Utility`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; Dock &gt; Utility**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/Dock/Utility/udts.json`. 5 UDT instance(s): 5 x [Devices/Evaporator](../udts/devices/evaporator.md).

## CG-G5

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Dock/Utility/CG-G5` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-G5 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[19\], ZATTag=CG\_ZAT\[19\], IntlkTag=CG\_Interlock\[19\], FansTag=CG\_Fans\[19\], FansRunTimeTag=CG\_Fans\_Runtime\[19\], LiquidSVTag=CG\_Liquid\_SV\[19\], SuctionSVTag=CG\_Suction\_SV\[19\], HotGasSVTag=CG\_HotGas\_SV\[19\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[19]` |
| `ZATTag` | `CG_ZAT[19]` |
| `IntlkTag` | `CG_Interlock[19]` |
| `FansTag` | `CG_Fans[19]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[19]` |
| `LiquidSVTag` | `CG_Liquid_SV[19]` |
| `SuctionSVTag` | `CG_Suction_SV[19]` |
| `HotGasSVTag` | `CG_HotGas_SV[19]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[19]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[19]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | no | (no PLC object) | |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | no | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[19]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[19]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[19]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[19]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[19]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[19]` | 11 tags |

## CG-G3

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Dock/Utility/CG-G3` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-G3 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[17\], ZATTag=CG\_ZAT\[17\], IntlkTag=CG\_Interlock\[17\], FansTag=CG\_Fans\[17\], FansRunTimeTag=CG\_Fans\_Runtime\[17\], LiquidSVTag=CG\_Liquid\_SV\[17\], SuctionSVTag=CG\_Suction\_SV\[17\], HotGasSVTag=CG\_HotGas\_SV\[17\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[17]` |
| `ZATTag` | `CG_ZAT[17]` |
| `IntlkTag` | `CG_Interlock[17]` |
| `FansTag` | `CG_Fans[17]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[17]` |
| `LiquidSVTag` | `CG_Liquid_SV[17]` |
| `SuctionSVTag` | `CG_Suction_SV[17]` |
| `HotGasSVTag` | `CG_HotGas_SV[17]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[17]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[17]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | no | (no PLC object) | |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | no | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[17]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[17]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[17]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[17]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[17]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[17]` | 11 tags |

## CG-G2

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Dock/Utility/CG-G2` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-G2 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[16\], ZATTag=CG\_ZAT\[16\], IntlkTag=CG\_Interlock\[16\], FansTag=CG\_Fans\[16\], FansRunTimeTag=CG\_Fans\_Runtime\[16\], LiquidSVTag=CG\_Liquid\_SV\[16\], SuctionSVTag=CG\_Suction\_SV\[16\], HotGasSVTag=CG\_HotGas\_SV\[16\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[16]` |
| `ZATTag` | `CG_ZAT[16]` |
| `IntlkTag` | `CG_Interlock[16]` |
| `FansTag` | `CG_Fans[16]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[16]` |
| `LiquidSVTag` | `CG_Liquid_SV[16]` |
| `SuctionSVTag` | `CG_Suction_SV[16]` |
| `HotGasSVTag` | `CG_HotGas_SV[16]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[16]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[16]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | no | (no PLC object) | |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | no | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[16]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[16]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[16]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[16]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[16]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[16]` | 11 tags |

## CG-G1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Dock/Utility/CG-G1` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-G1 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[15\], ZATTag=CG\_ZAT\[15\], IntlkTag=CG\_Interlock\[15\], FansTag=CG\_Fans\[15\], FansRunTimeTag=CG\_Fans\_Runtime\[15\], LiquidSVTag=CG\_Liquid\_SV\[15\], SuctionSVTag=CG\_Suction\_SV\[15\], HotGasSVTag=CG\_HotGas\_SV\[15\], BleedSVTag=CG\_Bleed\_SV\[15\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[15]` |
| `ZATTag` | `CG_ZAT[15]` |
| `IntlkTag` | `CG_Interlock[15]` |
| `FansTag` | `CG_Fans[15]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[15]` |
| `LiquidSVTag` | `CG_Liquid_SV[15]` |
| `SuctionSVTag` | `CG_Suction_SV[15]` |
| `HotGasSVTag` | `CG_HotGas_SV[15]` |
| `BleedSVTag` | `CG_Bleed_SV[15]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[15]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[15]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[15]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[15]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[15]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[15]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[15]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[15]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[15]` | 11 tags |

## CG-G4

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/Dock/Utility/CG-G4` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-G4 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[18\], ZATTag=CG\_ZAT\[18\], IntlkTag=CG\_Interlock\[18\], FansTag=CG\_Fans\[18\], FansRunTimeTag=CG\_Fans\_Runtime\[18\], LiquidSVTag=CG\_Liquid\_SV\[18\], SuctionSVTag=CG\_Suction\_SV\[18\], HotGasSVTag=CG\_HotGas\_SV\[18\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[18]` |
| `ZATTag` | `CG_ZAT[18]` |
| `IntlkTag` | `CG_Interlock[18]` |
| `FansTag` | `CG_Fans[18]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[18]` |
| `LiquidSVTag` | `CG_Liquid_SV[18]` |
| `SuctionSVTag` | `CG_Suction_SV[18]` |
| `HotGasSVTag` | `CG_HotGas_SV[18]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[18]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[18]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | no | (no PLC object) | |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | no | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[18]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[18]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[18]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[18]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[18]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[18]` | 11 tags |

