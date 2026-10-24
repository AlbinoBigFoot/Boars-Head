---
title: Discrete Inputs (Detectors, Rupture Disks, Level Switches)
sidebar_label: 09 Discrete Inputs
sidebar_position: 10
description: The 52 standalone DiscreteInput devices (ammonia / fire detectors, rupture disks, condenser level switches) mapped to P_DIn, and the Target Disagree alarm parity.
sources:
  - docs/pax-mapping/09-discrete-inputs.md
last_verified: 2026-10-23
---

# Discrete Inputs

Source doc: `docs/pax-mapping/09-discrete-inputs.md`. Type: [Devices/DiscreteInput](../reference/udts/devices/discreteinput.md)
(parameter `DInTag`, nested `DIn` -> [PLC/P_DIn](../reference/udts/plc/p-din.md)). The tank level switches are not
here: they live on the tanks ([Tanks](tanks.md)).

## Devices And PLC Objects

| Group | HMI devices | PLC objects | FT evidence |
|---|---|---|---|
| Ammonia / fire detectors (Plant Overview) | `<Area>/Detectors/AD01` .. `AD08`, `FD01`, `FD03`, `FD04`, `FD05` | `AD[1..8]`, `FD[1]`, `FD[3..5]` (there is no `FD[2]`) | `(STELLAR)DashBoard.gfx` `GO_P_DIn {[RCP1]AD[n]}`; the Utility Overview photo |
| Machine Room detectors | `Machine Room/Detectors/MR-AD1`, `VL-AD`, `MASTER-AD1` | `AD_MR1`, `AD_VL`, `MASTER_AD1` | `(STELLAR)MachineRoom.xml`, PAR files |
| Rupture disks | `Machine Room/RuptureDisks/PS01` .. `PS10`, `PS14` .. `PS37` (34) | `PS[1..10]`, `PS[14..37]` | `(STELLAR)RDisks.xml` |
| Condenser level switches | `Condensers/LevelSwitches/RS-LVL-OL2`, `RS-LVL-OL3`, `RS-LLCO2` | `RS_LVL_OL2`, `RS_LVL_OL3`, `RS_LLCO2` | `(STELLAR)Condensers.xml` |

Plus the LTU transfer input (`NH3_LTU`, nested in the LTU device, see [LTU](ltu.md)). The resolved object of every
instance is on the area `Detectors`, `RuptureDisks` and `LevelSwitches` pages under
[Device Instances](../reference/devices/index.md).

![Discrete input faceplate, live](/img/tags/di-faceplate-live.png)

## What The HMI Shows

| On the HMI | Member it reads | PLC tag (MR-AD1) |
|---|---|---|
| Tile text (OK / NH3 ALM / FIRE ALM / ALARM / LO) | `DIn/Sts` with the PLC state texts `DIn/Cfg_0StText` / `Cfg_1StText`; `DIn/Sts_TgtDisagree` for the alarm look | `AD_MR1.Sts`, `.Cfg_0StText` = "NH3 ALM", `.Cfg_1StText` = "OK" |
| Tile title | `DIn/Cfg_Label` | "MR-AD1" |
| "PV From Input" / "Current Value" | `DIn/Sts_PV` / `DIn/Sts` | |
| Target state | `DIn/Inp_Target` | |
| Substitute PV, debounce, options (Configuration tab) | `DIn/Cfg_*`, `MSet_SubstPV`, `Sts_SubstPV` (Leased) | |

The DI faceplate (`01_Popups/00_Faceplates/DiscreteInput`) and the status tile (`OverviewStatusTile`, used by the
Plant Overview, Machine Room, Rupture Disks and Condensers pages) take the DI's own `DIn` part, or the enclosing tank's
`*DIn` part for tank switches.

<details>
<summary>Full field map (18 fields, from docs/pax-mapping/09-discrete-inputs.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): MR-AD1 | Status |
|---|---|---|---|---|---|
| `Cfg_Debounce` | `DIn/Cfg_Debounce` | `AD_MR1.Cfg_Debounce` | Faceplate | 0 | mapped |
| `Cfg_Desc` | `DIn/Cfg_Desc` | `AD_MR1.Cfg_Desc` | Faceplate | "Discrete Input" | mapped |
| `Cfg_Label` | `DIn/Cfg_Label` | `AD_MR1.Cfg_Label` | Faceplate | "MR-AD1" | mapped |
| `Cfg_NoSubstPV` | `DIn/Cfg_NoSubstPV` | `AD_MR1.Cfg_NoSubstPV` | Faceplate | 0 | mapped |
| `Cfg_NormTextVis` | `DIn/Cfg_NormTextVis` | `AD_MR1.Cfg_NormTextVis` | Faceplate | 1 | mapped |
| `Cfg_PCmdClear` | `DIn/Cfg_PCmdClear` | `AD_MR1.Cfg_PCmdClear` | Faceplate | 1 | mapped |
| `Cfg_State0Txt` | `DIn/Cfg_0StText` | `AD_MR1.Cfg_0StText` | Faceplate | "NH3 ALM" | mapped |
| `Cfg_State1Txt` | `DIn/Cfg_1StText` | `AD_MR1.Cfg_1StText` | Faceplate | "OK" | mapped |
| `Cfg_Tag` | `DIn/Cfg_Tag` | `AD_MR1.Cfg_Tag` | Faceplate | "MR-AD1" | mapped |
| `Inp_Target` | `DIn/Inp_Target` | `AD_MR1.Inp_Target` | Status | 1 | mapped |
| `MCmd_InpPV` | `DIn/MCmd_InpPV` | `AD_MR1.MCmd_InpPV` | Faceplate | 0 | mapped |
| `MCmd_SubstPV` | `DIn/MCmd_SubstPV` | `AD_MR1.MCmd_SubstPV` | Faceplate | 0 | mapped |
| `MSet_SubstPV` | `DIn/MSet_SubstPV` | `AD_MR1.MSet_SubstPV` | Faceplate | 1 | mapped |
| `OCmd_ResetAckAll` | `DIn/OCmd_ResetAckAll` | `AD_MR1.OCmd_ResetAckAll` | Faceplate | 0 | mapped |
| `Sts_InpPV` | `DIn/Sts_PV` | `AD_MR1.Sts_PV` | Status | 1 | mapped |
| `Sts_PV` | `DIn/Sts` | `AD_MR1.Sts` | Status | 1 | mapped |
| `Sts_SubstPV` | `DIn/Sts_SubstPV` | `AD_MR1.Sts_SubstPV` | Status | 0 | mapped |
| `Sts_TgtDisagree` | `DIn/Sts_TgtDisagree` | `AD_MR1.Sts_TgtDisagree` | Status | 0 | mapped |

</details>

## Alarms (Target Disagree Parity)

The P_DIn library alarm **Target Disagree** (Medium, on `Sts_TgtDisagree`) is enabled only while the PLC object's
`Cfg_HasTgtDisagreeAlm` is 1. The live check found `Cfg_HasTgtDisagreeAlm` = 0 on every DI checked, so FT raises no
such alarm, while the ungated library alarm had raised 6 extra alarms (FD-01, LTR OPL, LTR LOLO, NH3 LTU input, MR EF,
BR EF). With the gating (user decision N2) they are gone. The tile text still follows `Sts_TgtDisagree`, as FT draws
it. The State Alarm stays off (`AlarmOnSts` = 0) on these devices.

## Live Check (2026-10-23)

- Every detector `Cfg_Label` = the FT tile text (AD-01 FREEZER ... FD-05 TRUCK DOCK, MR-AD1, VL-AD, MASTER-AD1); the
  rupture disks PS01 .. PS37 as ours.
- **FD-01 FREEZER** reads FIRE ALM (`Inp_PV` 0, `Inp_Target` 1 -> `Sts_TgtDisagree` 1), as on the FT photo. All other
  detectors and rupture disks read OK.
- `PS[33]` label and tag = "HTR-VESSEL-2", the same as PS32: a PLC duplicate (left as is).

## Open Items

- FD-01 FREEZER shows FIRE ALM on FT and on ours: check the detector on site.
- PS33 label duplicate in the PLC (probably HTR-VESSEL-3 or an oil pot): controls engineer.
