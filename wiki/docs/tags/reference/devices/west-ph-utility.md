---
title: "West PH / Utility (Instances)"
sidebar_label: "West PH / Utility"
description: "Device instances in [default]Boars_Head/GrovePort/West PH/Utility: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/West PH/Utility`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; West PH &gt; Utility**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/West PH/Utility/udts.json`. 4 UDT instance(s): 4 x [Devices/Evaporator](../udts/devices/evaporator.md).

## CG-F2

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/West PH/Utility/CG-F2` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-F2 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[12\], ZATTag=CG\_ZAT\[12\], IntlkTag=CG\_Interlock\[12\], FansTag=CG\_Fans\[12\], FansRunTimeTag=CG\_Fans\_Runtime\[12\], LiquidSVTag=CG\_Liquid\_SV\[12\], SuctionSVTag=CG\_Suction\_SV\[12\], HotGasSVTag=CG\_HotGas\_SV\[12\], BleedSVTag=CG\_Bleed\_SV\[12\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[12]` |
| `ZATTag` | `CG_ZAT[12]` |
| `IntlkTag` | `CG_Interlock[12]` |
| `FansTag` | `CG_Fans[12]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[12]` |
| `LiquidSVTag` | `CG_Liquid_SV[12]` |
| `SuctionSVTag` | `CG_Suction_SV[12]` |
| `HotGasSVTag` | `CG_HotGas_SV[12]` |
| `BleedSVTag` | `CG_Bleed_SV[12]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[12]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[12]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[12]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[12]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[12]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[12]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[12]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[12]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[12]` | 11 tags |

## CG-F4

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/West PH/Utility/CG-F4` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-F4 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[14\], ZATTag=CG\_ZAT\[14\], IntlkTag=CG\_Interlock\[14\], FansTag=CG\_Fans\[14\], FansRunTimeTag=CG\_Fans\_Runtime\[14\], LiquidSVTag=CG\_Liquid\_SV\[14\], SuctionSVTag=CG\_Suction\_SV\[14\], HotGasSVTag=CG\_HotGas\_SV\[14\], BleedSVTag=CG\_Bleed\_SV\[14\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[14]` |
| `ZATTag` | `CG_ZAT[14]` |
| `IntlkTag` | `CG_Interlock[14]` |
| `FansTag` | `CG_Fans[14]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[14]` |
| `LiquidSVTag` | `CG_Liquid_SV[14]` |
| `SuctionSVTag` | `CG_Suction_SV[14]` |
| `HotGasSVTag` | `CG_HotGas_SV[14]` |
| `BleedSVTag` | `CG_Bleed_SV[14]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[14]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[14]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[14]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[14]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[14]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[14]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[14]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[14]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[14]` | 11 tags |

## CG-F1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/West PH/Utility/CG-F1` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-F1 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[11\], ZATTag=CG\_ZAT\[11\], IntlkTag=CG\_Interlock\[11\], FansTag=CG\_Fans\[11\], FansRunTimeTag=CG\_Fans\_Runtime\[11\], LiquidSVTag=CG\_Liquid\_SV\[11\], SuctionSVTag=CG\_Suction\_SV\[11\], HotGasSVTag=CG\_HotGas\_SV\[11\], BleedSVTag=CG\_Bleed\_SV\[11\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[11]` |
| `ZATTag` | `CG_ZAT[11]` |
| `IntlkTag` | `CG_Interlock[11]` |
| `FansTag` | `CG_Fans[11]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[11]` |
| `LiquidSVTag` | `CG_Liquid_SV[11]` |
| `SuctionSVTag` | `CG_Suction_SV[11]` |
| `HotGasSVTag` | `CG_HotGas_SV[11]` |
| `BleedSVTag` | `CG_Bleed_SV[11]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[11]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[11]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[11]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[11]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[11]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[11]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[11]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[11]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[11]` | 11 tags |

## CG-F3

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/West PH/Utility/CG-F3` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-F3 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[13\], ZATTag=CG\_ZAT\[13\], IntlkTag=CG\_Interlock\[13\], FansTag=CG\_Fans\[13\], FansRunTimeTag=CG\_Fans\_Runtime\[13\], LiquidSVTag=CG\_Liquid\_SV\[13\], SuctionSVTag=CG\_Suction\_SV\[13\], HotGasSVTag=CG\_HotGas\_SV\[13\], BleedSVTag=CG\_Bleed\_SV\[13\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[13]` |
| `ZATTag` | `CG_ZAT[13]` |
| `IntlkTag` | `CG_Interlock[13]` |
| `FansTag` | `CG_Fans[13]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[13]` |
| `LiquidSVTag` | `CG_Liquid_SV[13]` |
| `SuctionSVTag` | `CG_Suction_SV[13]` |
| `HotGasSVTag` | `CG_HotGas_SV[13]` |
| `BleedSVTag` | `CG_Bleed_SV[13]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[13]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[13]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[13]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[13]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[13]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[13]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[13]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[13]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[13]` | 11 tags |

