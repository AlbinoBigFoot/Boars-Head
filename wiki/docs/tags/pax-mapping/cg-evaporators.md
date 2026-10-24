---
title: CG Evaporators (19 Control Groups)
sidebar_label: 06 CG Evaporators
sidebar_position: 7
description: The 19 control groups CG-A1 to CG-G5 mapped to CG_RL_Evap, the zone air temp P_AIn, P_Intlk, the fan P_Motor / P_RunTime, the HmiStatus conversion and the Too Hot / Too Cold behaviour.
sources:
  - docs/pax-mapping/06-evaporators.md
last_verified: 2026-10-23
---

# CG Evaporators (Control Groups)

Source doc: `docs/pax-mapping/06-evaporators.md`. Type: [Devices/Evaporator](../reference/udts/devices/evaporator.md);
instances in each area's `Utility` folder (for example [West PH / Utility](../reference/devices/west-ph-utility.md)).
The four valves of each CG are on [CG Valves](cg-valves.md).

Before this mapping the 19 CGs had **no live data at all**: their members were static placeholders from the simulator
removal, so the Utility Overview temperatures and states were not real.

## PLC Objects Per CG

For control group number `n`:

| Part | PLC tag | Type | What |
|---|---|---|---|
| `CG` | `CG[n]` | [PLC/CG_RL_Evap](../reference/udts/plc/cg-rl-evap.md) | site UDT: defrost sequencer, setpoints, zone air temp control, phase `Sts_State` |
| `ZAT` | `CG_ZAT[n]` | [PLC/P_AIn](../reference/udts/plc/p-ain.md) (`°F`) | zone air temperature |
| `Intlk` | `CG_Interlock[n]` | P_Intlk | CG interlocks |
| `Fans` | `CG_Fans[n]` | P_Motor | all fans of the group, one object |
| `FansRunTime` | `CG_Fans_Runtime[n]` | P_RunTime | fan run hours |
| `Valves/Liquid SV`, `Suction SV`, `Hot Gas SV`, `Bleed SV` | `CG_Liquid_SV[n]`, `CG_Suction_SV[n]`, `CG_HotGas_SV[n]`, `CG_Bleed_SV[n]` | nested Devices/Valve -> P_ValveSO | see [CG Valves](cg-valves.md) |

**CG number per HMI device** (from the FT Plant Overview `(STELLAR)DashBoard.gfx` CG objects: `#150` number,
`#151` label, `#153` display):

| CG | n | FT label | Valves | CG | n | FT label | Valves |
|---|---|---|---|---|---|---|---|
| CG-A1 | 1 | -10°F FREEZER | 4 | CG-E4 | 10 | +36°F EAST-PENTHOUSE | 4 |
| CG-A2 | 2 | -10°F FREEZER | 4 | CG-F1 | 11 | +36°F WEST-PENTHOUSE | 4 |
| CG-B1 | 3 | +26°F SUPERCHILL | 4 | CG-F2 | 12 | +36°F WEST-PENTHOUSE | 4 |
| CG-B2 | 4 | +26°F SUPERCHILL | 4 | CG-F3 | 13 | +36°F WEST-PENTHOUSE | 4 |
| CG-C1 | 5 | +36°F CLUB | 3 | CG-F4 | 14 | +36°F WEST-PENTHOUSE | 4 |
| CG-D1 | 6 | +36°F PALLETIZING | 3 | CG-G1 | 15 | +36°F DOCK | 4 |
| CG-E1 | 7 | +36°F EAST-PENTHOUSE | 4 | CG-G2 | 16 | +36°F DOCK | 3 |
| CG-E2 | 8 | +36°F EAST-PENTHOUSE | 4 | CG-G3 | 17 | +36°F DOCK | 3 |
| CG-E3 | 9 | +36°F EAST-PENTHOUSE | 4 | CG-G4 / G5 | 18 / 19 | +36°F DOCK | 3 |

## What The HMI Shows

| On the HMI (CG page panel / faceplate / tiles) | Member it reads | PLC tag (CG-C1, n = 5) |
|---|---|---|
| Zone Air Temp | `ZAT/Val` (red while Too Hot / Too Cold) | `CG_ZAT[5].Val` |
| Target SP, Deadband | `CG/Cfg_ZoneAirTemp`, `CG/Cfg_ZoneAirTempDB` | `CG[5].Cfg_ZoneAirTemp` |
| State (CLG / IDLE / STOP / DFT ... on tiles; PLC phase name on the CG page) | `HmiStatus` (expression on `CG/Sts_State`); the page uses the `Evaporator/PlcState` enum | `CG[5].Sts_State` |
| Evaporator Enabled | `CG/HMIEnable` | `CG[5].HMIEnable` |
| Permissives / Interlocks OK | `CG/PermOK`, `CG/IntlkOK`; Interlocks button `Intlk/Sts_IntlkOK` | |
| Start / Stop Defrost | `CG/HMIStartDefrost`, `CG/HMIStopDefrost` (disabled: write lock) | |
| Defrost Mode (ToD / Cooling / Runtime) | `CG/Cfg_DefrostStartMode` with the `Evaporator/DefrostStartMode` enum | |
| Cycle Fans / Idle Fan Mode (Off / Cycle / On) | `CG/Cfg_CycFans` with the `Evaporator/CycleFans` enum | |
| TOD schedule 1st .. 4th | `CG/Cfg_Def1stTOD` .. `Cfg_Def4thTOD` | |
| Step timers Pump Out / Hot Gas / Bleed / Fan Delay | `CG/Cfg_PumpOut`, `Cfg_MainHotGas`, `Cfg_Bleed`, `Cfg_FanDelay` (+ `Cfg_SoftHotGas`) | |
| Cooling time / runtime values and setpoints | `CG/Val_CoolingTime`, `Val_RunTime`, `Cfg_CoolingTime`, `Cfg_RunTime`; time left `Val_TimeLeft` | |
| Set Back Min / Max / Start / Stop / Enable | `CG/ZAT_MinSet`, `ZAT_MaxSet`, `SB_StartTime`, `SB_StopTime`, `SB_Enable` | |
| Fans running / fault (the 3 fan symbols) | `Fans/Sts_Running`, `Fans/Nrdy_Fail` (one motor for all three symbols) | `CG_Fans[5].*` |
| Bleed valve drawn or not | `CG/Cfg_HasBleedValve` (`PAX_Config`), page param `bleed` only as fallback | `CG[5].Cfg_HasBleedValve` = 0 |
| Trend / 12 h history | `ZAT/Val`, `CG/Val_TimeLeft` | |

![CG-E4 page with Zone Air Temp in red](/img/tags/cg-e4-too-hot.png)

*CG-E4 (2026-10-23): `CG[10].TooHot` = 1, so the zone air temp shows red on the page, the tile and the faceplate,
(the Too Hot bit no longer raises an alarm).*

<details>
<summary>Full field map (96 fields, from docs/pax-mapping/06-evaporators.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): CG-C1 | Status |
|---|---|---|---|---|---|
| `Cfg_Bleed` | `CG/Cfg_Bleed` | `CG[5].Cfg_Bleed` | Faceplate | 5 | mapped |
| `Cfg_CoolingTime` | `CG/Cfg_CoolingTime` | `CG[5].Cfg_CoolingTime` | Faceplate | 2260 | mapped |
| `Cfg_CycFans` | `CG/Cfg_CycFans` | `CG[5].Cfg_CycFans` | Faceplate | 0 | mapped |
| `Cfg_Def1stTOD` | `CG/Cfg_Def1stTOD` | `CG[5].Cfg_Def1stTOD` | Faceplate | 1400 | mapped |
| `Cfg_Def2ndTOD` | `CG/Cfg_Def2ndTOD` | `CG[5].Cfg_Def2ndTOD` | Faceplate | 0 | mapped |
| `Cfg_Def3rdTOD` | `CG/Cfg_Def3rdTOD` | `CG[5].Cfg_Def3rdTOD` | Faceplate | 0 | mapped |
| `Cfg_Def4thTOD` | `CG/Cfg_Def4thTOD` | `CG[5].Cfg_Def4thTOD` | Faceplate | 0 | mapped |
| `Cfg_DefrostStartMode` | `CG/Cfg_DefrostStartMode` | `CG[5].Cfg_DefrostStartMode` | Faceplate | 0 | mapped |
| `Cfg_FanDelay` | `CG/Cfg_FanDelay` | `CG[5].Cfg_FanDelay` | Faceplate | 2 | mapped |
| `Cfg_MainHotGas` | `CG/Cfg_MainHotGas` | `CG[5].Cfg_MainHotGas` | Faceplate | 20 | mapped |
| `Cfg_PumpOut` | `CG/Cfg_PumpOut` | `CG[5].Cfg_PumpOut` | Faceplate | 10 | mapped |
| `Cfg_Runtime` | `CG/Cfg_RunTime` | `CG[5].Cfg_RunTime` | Faceplate | 2200 | mapped |
| `Cfg_SoftHotGas` | `CG/Cfg_SoftHotGas` | `CG[5].Cfg_SoftHotGas` | Faceplate | 2 | mapped |
| `Cfg_ZoneAirTempDB` | `CG/Cfg_ZoneAirTempDB` | `CG[5].Cfg_ZoneAirTempDB` | Faceplate | 1 | mapped |
| `Cleanup` | `CG/Cleanup` | `CG[5].Cleanup` | Status | 0 | mapped |
| `Cmd_StartDefrost` | `CG/HMIStartDefrost` | `CG[5].HMIStartDefrost` | Faceplate | 0 | mapped |
| `Cmd_StopDefrost` | `CG/HMIStopDefrost` | `CG[5].HMIStopDefrost` | Faceplate | 0 | mapped |
| `Fan 1/CMD` | `Fans/Sts_Running` | `CG_Fans[5].Sts_Running` | Status | 0 | mapped |
| `Fan 1/Fault` | `Fans/Nrdy_Fail` | `CG_Fans[5].Nrdy_Fail` | Faceplate | 0 | mapped |
| `Fan 1/SPD_FBK` | `_NoPlc/Fan1Speed` | - | - | - | no PLC object |
| `Fan 1/SummaryInstances` | - | - | - | - | site-only |
| `Fan 2/CMD` | `Fans/Sts_Running` | `CG_Fans[5].Sts_Running` | Status | 0 | mapped |
| `Fan 2/Fault` | `Fans/Nrdy_Fail` | `CG_Fans[5].Nrdy_Fail` | Faceplate | 0 | mapped |
| `Fan 2/SPD_FBK` | `_NoPlc/Fan2Speed` | - | - | - | no PLC object |
| `Fan 2/SummaryInstances` | - | - | - | - | site-only |
| `Fan 3/CMD` | `Fans/Sts_Running` | `CG_Fans[5].Sts_Running` | Status | 0 | mapped |
| `Fan 3/Fault` | `Fans/Nrdy_Fail` | `CG_Fans[5].Nrdy_Fail` | Faceplate | 0 | mapped |
| `Fan 3/SPD_FBK` | `_NoPlc/Fan3Speed` | - | - | - | no PLC object |
| `Fan 3/SummaryInstances` | - | - | - | - | site-only |
| `HMIEnable` | `CG/HMIEnable` | `CG[5].HMIEnable` | Faceplate | 0 | mapped |
| `HMI_HeatMode_Enable` | `CG/HMI_HeatMode_Enable` | `CG[5].HMI_HeatMode_Enable` | Faceplate | 0 | mapped |
| `Interlock/Cfg_Bypassable` | `Intlk/Cfg_Bypassable` | `CG_Interlock[5].Cfg_Bypassable` | Faceplate | 0 | mapped |
| `Interlock/Cfg_CondTxt00` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_0_` | `CG_Interlock[5].Cfg_CondTxt[0]` | Faceplate | "RCP-MCR" | mapped (added) |
| `Interlock/Cfg_CondTxt01` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_1_` | `CG_Interlock[5].Cfg_CondTxt[1]` | Faceplate | "Power Up Timer" | mapped (added) |
| `Interlock/Cfg_CondTxt02` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_2_` | `CG_Interlock[5].Cfg_CondTxt[2]` | Faceplate | "Liq SV Not in Prog" | mapped (added) |
| `Interlock/Cfg_CondTxt03` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_3_` | `CG_Interlock[5].Cfg_CondTxt[3]` | Faceplate | "Suc SV Not in Prog" | mapped (added) |
| `Interlock/Cfg_CondTxt04` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_4_` | `CG_Interlock[5].Cfg_CondTxt[4]` | Faceplate | "HG SV Not in Prog" | mapped (added) |
| `Interlock/Cfg_CondTxt05` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_5_` | `CG_Interlock[5].Cfg_CondTxt[5]` | Faceplate | "Fans  Not in Prog" | mapped (added) |
| `Interlock/Cfg_CondTxt06` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_6_` | `CG_Interlock[5].Cfg_CondTxt[6]` | Faceplate | "AD-3 NH3 Alarm" | mapped (added) |
| `Interlock/Cfg_CondTxt07` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_7_` | `CG_Interlock[5].Cfg_CondTxt[7]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt08` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_8_` | `CG_Interlock[5].Cfg_CondTxt[8]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt09` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_9_` | `CG_Interlock[5].Cfg_CondTxt[9]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt10` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_10_` | `CG_Interlock[5].Cfg_CondTxt[10]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt11` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_11_` | `CG_Interlock[5].Cfg_CondTxt[11]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt12` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_12_` | `CG_Interlock[5].Cfg_CondTxt[12]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt13` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_13_` | `CG_Interlock[5].Cfg_CondTxt[13]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt14` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_14_` | `CG_Interlock[5].Cfg_CondTxt[14]` | Faceplate | "" | mapped (added) |
| `Interlock/Cfg_CondTxt15` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_15_` | `CG_Interlock[5].Cfg_CondTxt[15]` | Faceplate | "" | mapped (added) |
| `Interlock/MSet_Bypass00` | `Intlk/MSet_Bypass00` | `CG_Interlock[5].MSet_Bypass00` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass01` | `Intlk/MSet_Bypass01` | `CG_Interlock[5].MSet_Bypass01` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass02` | `Intlk/MSet_Bypass02` | `CG_Interlock[5].MSet_Bypass02` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass03` | `Intlk/MSet_Bypass03` | `CG_Interlock[5].MSet_Bypass03` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass04` | `Intlk/MSet_Bypass04` | `CG_Interlock[5].MSet_Bypass04` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass05` | `Intlk/MSet_Bypass05` | `CG_Interlock[5].MSet_Bypass05` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass06` | `Intlk/MSet_Bypass06` | `CG_Interlock[5].MSet_Bypass06` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass07` | `Intlk/MSet_Bypass07` | `CG_Interlock[5].MSet_Bypass07` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass08` | `Intlk/MSet_Bypass08` | `CG_Interlock[5].MSet_Bypass08` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass09` | `Intlk/MSet_Bypass09` | `CG_Interlock[5].MSet_Bypass09` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass10` | `Intlk/MSet_Bypass10` | `CG_Interlock[5].MSet_Bypass10` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass11` | `Intlk/MSet_Bypass11` | `CG_Interlock[5].MSet_Bypass11` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass12` | `Intlk/MSet_Bypass12` | `CG_Interlock[5].MSet_Bypass12` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass13` | `Intlk/MSet_Bypass13` | `CG_Interlock[5].MSet_Bypass13` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass14` | `Intlk/MSet_Bypass14` | `CG_Interlock[5].MSet_Bypass14` | Faceplate | 0 | mapped |
| `Interlock/MSet_Bypass15` | `Intlk/MSet_Bypass15` | `CG_Interlock[5].MSet_Bypass15` | Faceplate | 0 | mapped |
| `Interlock/OCmd_Reset` | `Intlk/OCmd_Reset` | `CG_Interlock[5].OCmd_Reset` | Faceplate | 0 | mapped |
| `Interlock/Rdy_Reset` | `Intlk/Rdy_Reset` | `CG_Interlock[5].Rdy_Reset` | Faceplate | 0 | mapped |
| `Interlock/Sts_BypActive` | `Intlk/Sts_BypActive` | `CG_Interlock[5].Sts_BypActive` | Status | 0 | mapped |
| `Interlock/Sts_FirstOut` | `Intlk/Sts_FirstOut` | `CG_Interlock[5].Sts_FirstOut` | Status | 0 | mapped |
| `Interlock/Sts_Intlk` | `Intlk/Sts_Intlk` | `CG_Interlock[5].Sts_Intlk` | Status | 0 | mapped |
| `Interlock/Sts_IntlkOK` | `Intlk/Sts_IntlkOK` | `CG_Interlock[5].Sts_IntlkOK` | Status | 1 | mapped |
| `Interlock/Sts_NBIntlkOK` | `Intlk/Sts_NBIntlkOK` | `CG_Interlock[5].Sts_NBIntlkOK` | Status | 1 | mapped |
| `Interlock/Cfg_OKState` | `Intlk/Cfg_OKState` | `CG_Interlock[5].Cfg_OKState` | Faceplate | 63 | mapped (added) |
| `Interlock/Cfg_Latched` | `Intlk/Cfg_Latched` | `CG_Interlock[5].Cfg_Latched` | Faceplate | 0 | mapped (added) |
| `Interlock/Cfg_HasNav` | `Intlk/Cfg_HasNav` | `CG_Interlock[5].Cfg_HasNav` | Faceplate | 0 | mapped (added) |
| `Interlock/Cfg_Desc` | `Intlk/Cfg_Desc` | `CG_Interlock[5].Cfg_Desc` | Faceplate | "Interlocks with First Out" | mapped |
| `Interlock/Cfg_Label` | `Intlk/Cfg_Label` | `CG_Interlock[5].Cfg_Label` | Faceplate | "CG-C1 Interlock" | mapped |
| `Interlock/Cfg_Tag` | `Intlk/Cfg_Tag` | `CG_Interlock[5].Cfg_Tag` | Faceplate | "P_Intlk" | mapped |
| `Interlock/Cfg_PCmdClear` | `Intlk/Cfg_PCmdClear` | `CG_Interlock[5].Cfg_PCmdClear` | Faceplate | 1 | mapped |
| `IntlkOK` | `CG/IntlkOK` | `CG[5].IntlkOK` | Status | 0 | mapped |
| `Off` | `CG/Off` | `CG[5].Off` | Status | 0 | mapped |
| `PermOK` | `CG/PermOK` | `CG[5].PermOK` | Status | 0 | mapped |
| `Pressure` | `_NoPlc/Pressure` | - | - | - | no PLC object |
| `SB_Enable` | `CG/SB_Enable` | `CG[5].SB_Enable` | Faceplate | 0 | mapped |
| `SB_StartTime` | `CG/SB_StartTime` | `CG[5].SB_StartTime` | Faceplate | 715 | mapped |
| `SB_StopTime` | `CG/SB_StopTime` | `CG[5].SB_StopTime` | Faceplate | 2200 | mapped |
| `Status` | `HmiStatus` | `CG[5].Sts_State` | expression (from CG/Sts_State) | 0 | mapped |
| `SummaryInstances` | - | - | - | - | site-only |
| `Temp` | `ZAT/Val` | `CG_ZAT[5].Val` | Status | 32.66 | mapped |
| `Temp/SP` | `CG/Cfg_ZoneAirTemp` | `CG[5].Cfg_ZoneAirTemp` | Faceplate | 33 | mapped |
| `TimeLeft` | `CG/Val_TimeLeft` | `CG[5].Val_TimeLeft` | Status | 0 | mapped |
| `TooCold` | `CG/TooCold` | `CG[5].TooCold` | Status | 0 | mapped |
| `TooHot` | `CG/TooHot` | `CG[5].TooHot` | Status | 0 | mapped |
| `Val_CoolingTime` | `CG/Val_CoolingTime` | `CG[5].Val_CoolingTime` | Status | 2 | mapped |
| `Val_Runtime` | `CG/Val_RunTime` | `CG[5].Val_RunTime` | Status | 0 | mapped |
| `ZAT_MaxSet` | `CG/ZAT_MaxSet` | `CG[5].ZAT_MaxSet` | Faceplate | 0 | mapped |
| `ZAT_MinSet` | `CG/ZAT_MinSet` | `CG[5].ZAT_MinSet` | Faceplate | 0 | mapped |

</details>

The `Fan n/*` and `_NoPlc/*` rows describe the old fan sub-devices and the no-PLC fields; since the cleanup the fans
read the one `Fans` part directly and the no-PLC fields (fan speed, CG pressure) are gone.

## Decisions And Evidence

1. **Three fan symbols, one PLC motor.** The controller has one `CG_Fans[n]` P_Motor per CG and FT draws one fan
   object; the three HMI fan symbols all read it (`CMD` -> `Fans/Sts_Running`, `Fault` -> `Fans/Nrdy_Fail`). Fan speed
   (`SPD_FBK`) has no PLC member (no VSD) and was dropped.
2. **Status** comes from the read-only expression `HmiStatus` that converts `CG/Sts_State` (0-10) into the HMI code
   (table on [Device UDTs](../udts/device-udts.md#derived-members)); FT shows the raw state, which the CG page shows
   via the `PlcState` enum. Confirmed live (0 -> STOP, 6 -> CLG, 7 -> IDLE, 1 -> DFT PD).
3. **CG pressure has no PLC object** (no `CG_*` pressure transmitter, nothing on the FT CG displays). The Daily Rounds
   form keeps its CG pressure field as a **manual gauge entry** (user decision); "Fill From Live Values" no longer
   maps it.
4. **Interlock list kept**: FT has `CG_Interlock[n]` on the CG display and the evaporator interlock faceplate photos.
5. **Library scope**: `CG_RL_Evap` keeps its 68 top-level members; the 16-word sequencer array and the four internal
   timers are PLC internals and left out.
6. **Bleed valve follows the PLC flag** `CG/Cfg_HasBleedValve` (0 on exactly C1, D1, G2-G5, live and L5X agree).

## Alarms

- `CG/TooHot` / `CG/TooCold` no longer alarm (they only turn the zone air temp red).
- The P_AIn alarms of `ZAT` (gated on the PLC enables; HiHi / LoLo are enabled on every CG) and the P_Motor alarms of
  `Fans` (IO Fault, Fail To Start / Stop, Interlock Trip).

### Too Hot / Too Cold And The Red Value

`TooHot` / `TooCold` are the PLC's own CG bits (they also drive the reheat / liquid valves in routine `CG_Control`),
so the HMI invents no threshold. From the L5X: `ZAT_HiHi = Cfg_ZoneAirTemp + 3` and `ZAT_LoLo = Cfg_ZoneAirTemp - 3`;
`TooHot` sets when ZAT >= setpoint + 3 °F and holds while ZAT > setpoint (latched), `TooCold` the mirror image. The
P_AIn alarm limits of `CG_ZAT[n]` are wider and were not active. Live 2026-10-23:

| CG | ZAT | Threshold | PLC bits | Verdict |
|---|---|---|---|---|
| CG-E4 | 36.48 °F | setpoint 33.0 + 3 = 36.0 | TooHot 1 (CG in defrost bleed) | real PLC condition |
| CG-A1 | 32.78 °F | setpoint 38.0 - 3 = 35.0 | TooCold 1 | real PLC condition |
| CG-G5 | 32.99 °F | setpoint 33.5 - 3 = 30.5 (set earlier, held while below 33.5) | TooCold 1 | real PLC condition (latched) |

While either bit is 1 the zone air temp is **red** (style class `value-alarm`, theme `--error`; the theme has no
warm / cold tokens, so red for both) on the CG tiles, the CG page Temperature card (`AhuEvapPanel`) and the evaporator
faceplate. A bad value stays gray (value-bad wins). These two bits no longer raise alarms: the CG
zone-temperature alarms come only from the ZAT P_AIn Hi / HiHi / Lo / LoLo alarms.

## Live Check (2026-10-23)

ZAT on all 19 CGs 31.5-36.0 °F (`Sts_PVBad` 0); states match the icon semantics. Labels: ZAT "CG-xx" plus the area name, fans
"CG-xx FANS", interlock "CG-xx Interlock". Red values: CG-A1 / CG-G5 Too Cold, CG-E4 Too Hot.

## Open Items

- `Cfg_DefrostStopMode`, `Cfg_SucType`, `Last_State` are in the controller but not shown (not needed).
