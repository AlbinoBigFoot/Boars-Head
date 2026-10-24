---
title: Tanks (HTR / LTR / HPR / CSV)
sidebar_label: 02 Tanks
sidebar_position: 3
description: The Machine Room vessels HTR, LTR, HPR and the Condensers CSV mapped to P_AIn level, P_DIn level switches, pump alarm DIs and setpoint atomics.
sources:
  - docs/pax-mapping/02-tanks.md
last_verified: 2026-10-23
---

# Tanks (HTR / LTR / HPR / CSV)

Source doc: `docs/pax-mapping/02-tanks.md`. Type: [Devices/Tank](../reference/udts/devices/tank.md); instances:
[Machine Room / Tanks](../reference/devices/machine-room-tanks.md), [Condensers / Tanks](../reference/devices/condensers-tanks.md).

## Devices And PLC Objects

| HMI device | `LvlAIn` (P_AIn) | `PressAIn` | `HlcoDIn` / `HiHiDIn` / `OplDIn` / `LoLoDIn` (P_DIn) | `Pump1Alm` / `Pump2Alm` (P_DIn, state alarm) | `StartPress` / `LeadPump` (atomics) |
|---|---|---|---|---|---|
| `Machine Room/Tanks/HTR` | `HT_LVL` | reference to `Sensors/HSS-Pumps Pressure/AIn` (`SYS_PT2`) | `HTR_HLCO` / `HTR_HIHI` / `HTR_OPL` / `HTR_LOLO` | `HTR_PUMPS_ALM[1]` / `[2]` | `HTPS_SET` / `HTRL_PUMPS_SEQ.Cfg_Lead` |
| `Machine Room/Tanks/LTR` | `LT_LVL` | reference to `Sensors/LSS-Pumps Pressure/AIn` (`SYS_PT1`) | `LTR_HLCO` / `LTR_HIHI` / `LTR_OPL` / `LTR_LOLO` | `LTR_PUMPS_ALM[1]` / `[2]` | `LTPS_SET` / `LTRL_PUMPS_SEQ.Cfg_Lead` |
| `Machine Room/Tanks/HPR` | `LT_HPR` | none (FT shows no pressure) | only `LoLoDIn` = `HPR_LOLO` | - | - |
| `Condensers/Tanks/CSV` | `LT_CSV` (owner; the `Condenser Sump Level` sensor references it) | - | - | - | - |

The exact parameters per tank are on the generated instance pages. Parts the vessel has no object for stay disabled
and show the gray placeholder.

![HTR tank faceplate, live](/img/tags/tank-faceplate-live.png)

*HTR tank faceplate (2026-10-23): level from `LvlAIn/Val` with the HH / H / L / LL markers at the P_AIn alarm limits,
the HSL pumps pressure and HSS-PT2 tiles from the Machine Room sensors, the pump cards from the pumps.*

## What The Faceplate Shows

| On the HMI | Member it reads | PLC tag (HTR) |
|---|---|---|
| Level value and bar | `LvlAIn/Val` (scale `LvlAIn/Cfg_PVEUMin` .. `Cfg_PVEUMax`, unit `LvlAIn/Cfg_EU`) | `HT_LVL.Val` |
| HH / H / L / LL markers and flags | `LvlAIn/Val_HiHiLim` / `Val_HiLim` / `Val_LoLim` / `Val_LoLoLim`; `Sts_HiHi` / `Sts_Hi` / `Sts_Lo` / `Sts_LoLo` | `HT_LVL.Val_HiHiLim` ... |
| Tank status text (OK / LO / HI / LOLO / HIHI / FAIL / CFGERR) | `LvlAIn/Val_Fault` (FT's "exceptions" indicator) | `HT_LVL.Val_Fault` |
| Operator Mode lock | `LvlAIn/Mode/Sts_ProgOperLock`, `Sts_Oper` | `HT_LVL.Mode.Sts_ProgOperLock` |
| Vessel / suction pressure | `PressAIn/Val` (reference to the sensor) | `SYS_PT2.Val` |
| HSL / LSL pumps pressure tiles | the Machine Room sensors' `AIn/Val` | `SYS_PT5` (HSL), `SYS_PT4` (LSL) |
| Level switch tiles HTR-HLCO, HTR-HI LEVEL, HTR-OPL, HTR-LOLO LEVEL | `HlcoDIn/Sts`, `HiHiDIn/Sts`, `OplDIn/Sts`, `LoLoDIn/Sts` with the PLC state texts `Cfg_0StText` / `Cfg_1StText` and `Sts_TgtDisagree` | `HTR_HLCO.Sts` ... |
| Pump #1 / #2 alarm | `Pump1Alm/Sts`, `Pump2Alm/Sts` | `HTR_PUMPS_ALM[1].Sts` |
| Start Pressure | `StartPress` (Leased) | `HTPS_SET` |
| Lead Pump (Make Pump #1 / #2 Lead) | `LeadPump` | `HTRL_PUMPS_SEQ.Cfg_Lead` (range 1-2) |
| Configuration tab (raw scaling, limits, deadbands, filter) | `LvlAIn/Cfg_*`, `Val_*Lim` (Leased) | `HT_LVL.Cfg_*` |
| Trend default pens | level + pumps pressure (`HT_LVL.Val` with `SYS_PT5.Val`, as FT HTR-SP `Trend1`) | |

Per-tank coverage: HTR 126 / LTR 126 fields mapped, HPR 67 mapped + 59 no PLC object, CSV 49 + 77.

<details>
<summary>Full field map (45 fields, from docs/pax-mapping/02-tanks.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): HTR / LTR / HPR / CSV | Status |
|---|---|---|---|---|---|
| `Cfg_LeadPump` | `LeadPump` | `HTRL_PUMPS_SEQ.Cfg_Lead` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `Cfg_PumpStartPress` | `StartPress` | `HTPS_SET` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_Debounce` | `HlcoDIn/Cfg_Debounce` | `HTR_HLCO.Cfg_Debounce` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_Desc` | `HlcoDIn/Cfg_Desc` | `HTR_HLCO.Cfg_Desc` | Faceplate | Discrete Input / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_Label` | `HlcoDIn/Cfg_Label` | `HTR_HLCO.Cfg_Label` | Faceplate | HTR-HLCO / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_NoSubstPV` | `HlcoDIn/Cfg_NoSubstPV` | `HTR_HLCO.Cfg_NoSubstPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_NormTextVis` | `HlcoDIn/Cfg_NormTextVis` | `HTR_HLCO.Cfg_NormTextVis` | Faceplate | true / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_PCmdClear` | `HlcoDIn/Cfg_PCmdClear` | `HTR_HLCO.Cfg_PCmdClear` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_State0Txt` | `HlcoDIn/Cfg_0StText` | `HTR_HLCO.Cfg_0StText` | Faceplate | OK / OK / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_State1Txt` | `HlcoDIn/Cfg_1StText` | `HTR_HLCO.Cfg_1StText` | Faceplate | HLCO / HLCO / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Cfg_Tag` | `HlcoDIn/Cfg_Tag` | `HTR_HLCO.Cfg_Tag` | Faceplate | HTR-HLCO / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Inp_Target` | `HlcoDIn/Inp_Target` | `HTR_HLCO.Inp_Target` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/MCmd_InpPV` | `HlcoDIn/MCmd_InpPV` | `HTR_HLCO.MCmd_InpPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/MCmd_SubstPV` | `HlcoDIn/MCmd_SubstPV` | `HTR_HLCO.MCmd_SubstPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/MSet_SubstPV` | `HlcoDIn/MSet_SubstPV` | `HTR_HLCO.MSet_SubstPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/OCmd_ResetAckAll` | `HlcoDIn/OCmd_ResetAckAll` | `HTR_HLCO.OCmd_ResetAckAll` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Sts_InpPV` | `HlcoDIn/Sts_PV` | `HTR_HLCO.Sts_PV` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Sts_PV` | `HlcoDIn/Sts` | `HTR_HLCO.Sts` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Sts_SubstPV` | `HlcoDIn/Sts_SubstPV` | `HTR_HLCO.Sts_SubstPV` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HLCO/Sts_TgtDisagree` | `HlcoDIn/Sts_TgtDisagree` | `HTR_HLCO.Sts_TgtDisagree` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_Debounce` | `HiHiDIn/Cfg_Debounce` | `HTR_HIHI.Cfg_Debounce` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_Desc` | `HiHiDIn/Cfg_Desc` | `HTR_HIHI.Cfg_Desc` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_Label` | `HiHiDIn/Cfg_Label` | `HTR_HIHI.Cfg_Label` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_NoSubstPV` | `HiHiDIn/Cfg_NoSubstPV` | `HTR_HIHI.Cfg_NoSubstPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_NormTextVis` | `HiHiDIn/Cfg_NormTextVis` | `HTR_HIHI.Cfg_NormTextVis` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_PCmdClear` | `HiHiDIn/Cfg_PCmdClear` | `HTR_HIHI.Cfg_PCmdClear` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_State0Txt` | `HiHiDIn/Cfg_0StText` | `HTR_HIHI.Cfg_0StText` | Faceplate | OK / OK / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_State1Txt` | `HiHiDIn/Cfg_1StText` | `HTR_HIHI.Cfg_1StText` | Faceplate | HI / HI / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Cfg_Tag` | `HiHiDIn/Cfg_Tag` | `HTR_HIHI.Cfg_Tag` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Inp_Target` | `HiHiDIn/Inp_Target` | `HTR_HIHI.Inp_Target` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/MCmd_InpPV` | `HiHiDIn/MCmd_InpPV` | `HTR_HIHI.MCmd_InpPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/MCmd_SubstPV` | `HiHiDIn/MCmd_SubstPV` | `HTR_HIHI.MCmd_SubstPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/MSet_SubstPV` | `HiHiDIn/MSet_SubstPV` | `HTR_HIHI.MSet_SubstPV` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/OCmd_ResetAckAll` | `HiHiDIn/OCmd_ResetAckAll` | `HTR_HIHI.OCmd_ResetAckAll` | Faceplate | _leased_ / _leased_ / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Sts_InpPV` | `HiHiDIn/Sts_PV` | `HTR_HIHI.Sts_PV` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Sts_PV` | `HiHiDIn/Sts` | `HTR_HIHI.Sts` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Sts_SubstPV` | `HiHiDIn/Sts_SubstPV` | `HTR_HIHI.Sts_SubstPV` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_HiLevel/Sts_TgtDisagree` | `HiHiDIn/Sts_TgtDisagree` | `HTR_HIHI.Sts_TgtDisagree` | Status | false / false / - / - | mapped / mapped / no PLC object / no PLC object |
| `DI_LoLo/Cfg_Debounce` | `LoLoDIn/Cfg_Debounce` | `HTR_LOLO.Cfg_Debounce` | Faceplate | _leased_ / _leased_ / _leased_ / - | mapped / mapped / mapped / no PLC object |
| `DI_LoLo/Cfg_Desc` | `LoLoDIn/Cfg_Desc` | `HTR_LOLO.Cfg_Desc` | Faceplate | _leased_ / _leased_ / Discrete Input / - | mapped / mapped / mapped / no PLC object |
| `DI_LoLo/Cfg_Label` | `LoLoDIn/Cfg_Label` | `HTR_LOLO.Cfg_Label` | Faceplate | _leased_ / _leased_ / HPR-LO LEVEL / - | mapped / mapped / mapped / no PLC object |
| `DI_LoLo/Cfg_NoSubstPV` | `LoLoDIn/Cfg_NoSubstPV` | `HTR_LOLO.Cfg_NoSubstPV` | Faceplate | _leased_ / _leased_ / false / - | mapped / mapped / mapped / no PLC object |
| `DI_LoLo/Cfg_NormTextVis` | `LoLoDIn/Cfg_NormTextVis` | `HTR_LOLO.Cfg_NormTextVis` | Faceplate | _leased_ / _leased_ / _leased_ / - | mapped / mapped / mapped / no PLC object |
| `DI_LoLo/Cfg_PCmdClear` | `LoLoDIn/Cfg_PCmdClear` | `HTR_LOLO.Cfg_PCmdClear` | Faceplate | _leased_ / _leased_ / true / - | mapped / mapped / mapped / no PLC object |
| `DI_LoLo/Cfg_State0Txt` | `LoLoDIn/Cfg_0StText` | `HTR_LOLO.Cfg_0StText` | Faceplate | OK |  |

</details>

## Decisions And Evidence

1. **HPR has no pressure transmitter.** FT `(STELLAR)MachineRoom.xml` binds only `{[RCP1]LT_HPR}` and
   `{[RCP1]HPR_LOLO}` for HPR; the photo shows only its level. The field is hidden **data-driven**: a tank whose
   `PressAIn` part is disabled gets no pressure cell in the Tanks table (`shared.Pax.configured()`) and no
   pump-pressure tiles (`position.display` = `PressAIn.Enabled`). No HPR-specific code.
2. **HTR = SYS_PT2 / LTR = SYS_PT1** (vessel / suction pressure) and SYS_PT5 / SYS_PT4 (pumps pressure), from the P_AIn
   global objects on FT HTR-SP / LTR-SP. These transmitters are owned by the Machine Room sensors; the tank's
   `PressAIn` is a read-only reference, so each object is subscribed and alarmed once.
3. **No level setpoint.** FT and the PLC have none; the HH / H / L / LL markers are the P_AIn alarm limits, as FT draws
   them (`{#102.Val_LoLoLim}` appears 12 times in the FT Machine Room display).
4. **Status = `Val_Fault`**, exactly FT's exceptions indicator; the notification icon (`Val_Notify`) corresponds to our
   alarm frame / badge.
5. **Pump alarm DIs live on the tank** as `Pump1Alm` / `Pump2Alm`: `Devices/Tank` sets the library parameter
   `AlarmOnSts = 1` and `Description = "Pump #1 Alarm"` / `"Pump #2 Alarm"` on those parts (in the type, not on
   instances), which turns on the P_DIn **State Alarm**.
6. **P_DIn semantics** (FT `DIN_Display`): "PV From Input" = `Sts_PV`; "Current Value" and the tiles = `Sts`.
7. **Lead pump selector** = `HTRL_PUMPS_SEQ.Cfg_Lead` (FT `num_Input4`, range 1-2): read only, the buttons are
   locked like every PLC command.
8. **`LTR1_LSHH`** exists in the PLC (P_DIn) but no FT display binds it and its description is the library default:
   unused, left out.

## Alarms

On the nested parts: `LvlAIn` P_AIn alarms (High-High, Low-Low, Input Failure High; High, Low Medium), the DIn
**Target Disagree** (Medium) and the pump alarm **State Alarm** (High). All gated on the PLC's own alarm enables
([Alarms](../alarms.md)), which differ per tank: `HT_LVL` has Lo / LoLo / Hi / HiHi / Fail enabled, `LT_LVL` none. Since
the gating, the LTR Low / Low-Low alarms that FT does not show are gone.

## Live Check (2026-10-23)

- Levels HTR 29.5 %, LTR -0.03 % (LO / LOLO), HPR 51.2 %, CSV 68-81 In; HTR-OPL OK, LTR-OPL ALARM and LTR-LOLO LO (the
  same pattern as the FT photo). Start pressures `HTPS_SET` 60, `LTPS_SET` 20.
- Labels HTR-LEVEL, LTR-LEVEL, HPR-LEVEL, CSV-LEVEL, the -HLCO / -HI LEVEL / -OPL / -LOLO LEVEL switches, HPR-LO LEVEL
  and HTR/LTR-P1/P2-ALARM all match the FT tiles.
- Start Pressure and the lead pump buttons fill after the Leased value arrives (a few seconds).

![LTR tank configuration while the Leased values load](/img/tags/tank-config-loading.png)

*The LTR tank Configuration tab just after opening: Leased members show the gray dash until the first value arrives
(a checkbox shows only once its value is usable).*

## Open Items

- The LTR tank uses the same layout as HTR (same UDT, same view); confirmed against the FT HTR-SP screenshot.
- Tank `Interlock/*` is an HMI-owned layout folder with no PLC object (kept, used by `_Assets/Interlocks`).
