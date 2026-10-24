---
title: "SuperChill / Utility (Instances)"
sidebar_label: "SuperChill / Utility"
description: "Device instances in [default]Boars_Head/GrovePort/SuperChill/Utility: types, parameters and the resolved PLC objects."
generated: true
---

:::note

:::
# `Boars_Head/GrovePort/SuperChill/Utility`

Tag Browser: **default > Boars\_Head &gt; GrovePort &gt; SuperChill &gt; Utility**. File: `gateways/standard/data/config/resources/core/ignition/tag-definition/default/Boars_Head/GrovePort/SuperChill/Utility/udts.json`. 2 UDT instance(s): 2 x [Devices/Evaporator](../udts/devices/evaporator.md).

## CG-B2

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-B2 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[4\], ZATTag=CG\_ZAT\[4\], IntlkTag=CG\_Interlock\[4\], FansTag=CG\_Fans\[4\], FansRunTimeTag=CG\_Fans\_Runtime\[4\], LiquidSVTag=CG\_Liquid\_SV\[4\], SuctionSVTag=CG\_Suction\_SV\[4\], HotGasSVTag=CG\_HotGas\_SV\[4\], BleedSVTag=CG\_Bleed\_SV\[4\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[4]` |
| `ZATTag` | `CG_ZAT[4]` |
| `IntlkTag` | `CG_Interlock[4]` |
| `FansTag` | `CG_Fans[4]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[4]` |
| `LiquidSVTag` | `CG_Liquid_SV[4]` |
| `SuctionSVTag` | `CG_Suction_SV[4]` |
| `HotGasSVTag` | `CG_HotGas_SV[4]` |
| `BleedSVTag` | `CG_Bleed_SV[4]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[4]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[4]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[4]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[4]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[4]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[4]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[4]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[4]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[4]` | 11 tags |

## CG-B1

| | |
|---|---|
| Tag path | `[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1` |
| Type | [Devices/Evaporator](../udts/devices/evaporator.md) |
| Label | CG-B1 |
| Description | evaporator. Live PLC \[RCP1\] (read only): CGTag=CG\[3\], ZATTag=CG\_ZAT\[3\], IntlkTag=CG\_Interlock\[3\], FansTag=CG\_Fans\[3\], FansRunTimeTag=CG\_Fans\_Runtime\[3\], LiquidSVTag=CG\_Liquid\_SV\[3\], SuctionSVTag=CG\_Suction\_SV\[3\], HotGasSVTag=CG\_HotGas\_SV\[3\], BleedSVTag=CG\_Bleed\_SV\[3\]. PLC parts only (flat stand-ins removed 2026-10-23). |

| Parameter | Value |
|---|---|
| `PlcDevice` | `RCP1` |
| `CGTag` | `CG[3]` |
| `ZATTag` | `CG_ZAT[3]` |
| `IntlkTag` | `CG_Interlock[3]` |
| `FansTag` | `CG_Fans[3]` |
| `FansRunTimeTag` | `CG_Fans_Runtime[3]` |
| `LiquidSVTag` | `CG_Liquid_SV[3]` |
| `SuctionSVTag` | `CG_Suction_SV[3]` |
| `HotGasSVTag` | `CG_HotGas_SV[3]` |
| `BleedSVTag` | `CG_Bleed_SV[3]` |

| Member | Part type | Enabled | Reads (resolved) | In `_RCP1_` mirror |
|---|---|---|---|---|
| `Valves/Liquid SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Liquid_SV[3]` | 151 tags |
| `Valves/Liquid SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Suction SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Suction_SV[3]` | 151 tags |
| `Valves/Suction SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Bleed SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_Bleed_SV[3]` | 151 tags |
| `Valves/Bleed SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `Valves/Hot Gas SV/Valve` | [PLC/P\_ValveSO](../udts/plc/p-valveso.md) | yes | `[RCP1]CG_HotGas_SV[3]` | 151 tags |
| `Valves/Hot Gas SV/Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | (no PLC object) | |
| `CG` | [PLC/CG\_RL\_Evap](../udts/plc/cg-rl-evap.md) | yes | `[RCP1]CG[3]` | 108 tags |
| `ZAT` | [PLC/P\_AIn](../udts/plc/p-ain.md) | yes | `[RCP1]CG_ZAT[3]` | 174 tags |
| `Intlk` | [PLC/P\_Intlk](../udts/plc/p-intlk.md) | yes | `[RCP1]CG_Interlock[3]` | 31 tags |
| `Fans` | [PLC/P\_Motor](../udts/plc/p-motor.md) | yes | `[RCP1]CG_Fans[3]` | 108 tags |
| `FansRunTime` | [PLC/P\_RunTime](../udts/plc/p-runtime.md) | yes | `[RCP1]CG_Fans_Runtime[3]` | 11 tags |

