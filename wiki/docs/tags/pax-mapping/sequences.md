---
title: Sequences (HSS, LSS, HSD)
sidebar_label: 13 Sequences
sidebar_position: 14
description: The compressor suction sequences HSS / LSS (Comp_Sequence) and the high stage discharge sequencer HSD (FB_2SpUpDownSeqr plus controller atomics).
sources:
  - docs/pax-mapping/13-sequences.md
last_verified: 2026-10-23
---

# Sequences (HSS, LSS, HSD)

Source doc: `docs/pax-mapping/13-sequences.md`. Types: [Devices/SuctionSequence](../reference/udts/devices/suctionsequence.md),
[Devices/DischargeSequence](../reference/udts/devices/dischargesequence.md). Instances:
[Machine Room / Sequences](../reference/devices/machine-room-sequences.md) (HSS, LSS),
[Condensers / Sequences](../reference/devices/condensers-sequences.md) (HSD). Shown in the **HSS Suction SP**,
**LSS Suction SP** (from `/machine-room`) and **Discharge SP** (from `/condensers`) popups.

| HMI device | Key | PLC objects | FT evidence |
|---|---|---|---|
| `Machine Room/Sequences/HSS` | `Seq` | `HSS` (`Comp_Sequence`, part `Seq`) | `(STELLAR) L3-HSS_Seq.xml`: `HSS.Sequence_Set[1..4]`, start / stop pressure, deadbands, delays, time left, target, `SYS_PT2` |
| `Machine Room/Sequences/LSS` | `Seq` | `LSS` (`Comp_Sequence`) + `LSS_HMI_Enable` (BOOL) | `(STELLAR) L3-LSS_Seq.xml`: the same with `Sequence_Set[1..2]`, `LSS_HMI_Enable`, `SYS_PT1` |
| `Condensers/Sequences/HSD` | `Dsq` | `HSD_Seqr` (`FB_2SpUpDownSeqr`, part `Seqr`) + `HSD_Sequence[1..7]`, `HSD_Fixed_SP`, `Cmd_FirstNoDelay`, `CD_SUMP_OPLL/OPLH/OPL1L/OPL1H_SET` | `(STELLAR) L3-HSD_Seq.xml`; the Condensers High Stage Discharge photo |

The single controller tags are read-only OPC atomics on the device (`PlcHmiEnable`, `PlcSequence1..7`, `PlcFixedSP`,
`PlcFirstNoDelay`, `PlcMainOpenSP`, `PlcMainCloseSP`, `PlcBackupOpenSP`, `PlcBackupCloseSP`). HMI-owned settings:
`Cfg_HasEnable`, `Cfg_Notes`, `Cfg_Positions`, `Cfg_SensorLabel` / `Cfg_SensorPath`, `Cfg_LevelLabel` /
`Cfg_LevelPath` (links to the sensor / level devices whose PV the popup shows).

![HSD sequence popup, live](/img/tags/hsd-sequence-popup.png)

## HSD Make-Up Setpoints

Which tag is which comes from the FT display object positions matched against the photo rows:

| On the HMI | PLC tag | Photo value |
|---|---|---|
| MAIN MAKE-UP OPEN | `CD_SUMP_OPLL_SET` | 35.0 |
| MAIN MAKE-UP CLOSE | `CD_SUMP_OPLH_SET` | 60.0 |
| BACKUP MAKE-UP OPEN | `CD_SUMP_OPL1L_SET` | 35.0 |
| BACKUP MAKE-UP CLOSE | `CD_SUMP_OPL1H_SET` | 55.0 |
| CONTROL MODE Static Setpoint (`Target_Pressure_Set`) | `HSD_Fixed_SP` | 140.0 |
| First Element No Delay | `Cmd_FirstNoDelay` (a controller-scope BOOL, not `HSD_Seqr.Cmd_FirstNoDelay`) | 1 |
| Sequence positions Sump Pump #1..#3, Cond 1A / 1B Fan #1 / #2 | `HSD_Sequence[1..7]` | 0 / 4 / 2 / 4 / 3 / 1 / 2 |

All confirmed live on 2026-10-23.

## Field Maps

<details>
<summary>HSS field map</summary>

| Field (old member name / `shared.Pax` key) | New member | Controller tag | Status |
|---|---|---|---|
| `Cfg_HasEnable` | - | - | site-only |
| `Cfg_Notes` | - | - | site-only |
| `Cfg_Positions` | - | - | site-only |
| `Cfg_SensorLabel` | - | - | site-only |
| `Cfg_SensorPath` | - | - | site-only |
| `HMI_Enable` | `PlcHmiEnable` | - | no PLC object |
| `Sequence_Set_1` | `Seq/Sequence_Set/Sequence_Set_1_` | `HSS.Sequence_Set[1]` | mapped |
| `Sequence_Set_2` | `Seq/Sequence_Set/Sequence_Set_2_` | `HSS.Sequence_Set[2]` | mapped |
| `Sequence_Set_3` | `Seq/Sequence_Set/Sequence_Set_3_` | `HSS.Sequence_Set[3]` | mapped |
| `Sequence_Set_4` | `Seq/Sequence_Set/Sequence_Set_4_` | `HSS.Sequence_Set[4]` | mapped |
| `Start_Delay_Set` | `Seq/Start_Delay_Set` | `HSS.Start_Delay_Set` | mapped |
| `Start_Pressure` | `Seq/Start_Pressure` | `HSS.Start_Pressure` | mapped |
| `Start_Pressure_DB` | `Seq/Start_Pressure_DB` | `HSS.Start_Pressure_DB` | mapped |
| `Start_Time_Left` | `Seq/Start_Time_Left` | `HSS.Start_Time_Left` | mapped |
| `Stop_Delay_Set` | `Seq/Stop_Delay_Set` | `HSS.Stop_Delay_Set` | mapped |
| `Stop_Pressure` | `Seq/Stop_Pressure` | `HSS.Stop_Pressure` | mapped |
| `Stop_Pressure_DB` | `Seq/Stop_Pressure_DB` | `HSS.Stop_Pressure_DB` | mapped |
| `Stop_Time_Left` | `Seq/Stop_Time_Left` | `HSS.Stop_Time_Left` | mapped |
| `Target_Pressure` | `Seq/Target_Pressure` | `HSS.Target_Pressure` | mapped |
| `Target_Pressure_Set` | `Seq/Target_Pressure_Set` | `HSS.Target_Pressure_Set` | mapped |

</details>

<details>
<summary>LSS field map</summary>

| Field (old member name / `shared.Pax` key) | New member | Controller tag | Status |
|---|---|---|---|
| `Cfg_HasEnable` | - | - | site-only |
| `Cfg_Notes` | - | - | site-only |
| `Cfg_Positions` | - | - | site-only |
| `Cfg_SensorLabel` | - | - | site-only |
| `Cfg_SensorPath` | - | - | site-only |
| `HMI_Enable` | `PlcHmiEnable` | `LSS_HMI_Enable` | mapped |
| `Sequence_Set_1` | `Seq/Sequence_Set/Sequence_Set_1_` | `LSS.Sequence_Set[1]` | mapped |
| `Sequence_Set_2` | `Seq/Sequence_Set/Sequence_Set_2_` | `LSS.Sequence_Set[2]` | mapped |
| `Sequence_Set_3` | `Seq/Sequence_Set/Sequence_Set_3_` | `LSS.Sequence_Set[3]` | mapped |
| `Sequence_Set_4` | `Seq/Sequence_Set/Sequence_Set_4_` | `LSS.Sequence_Set[4]` | mapped |
| `Start_Delay_Set` | `Seq/Start_Delay_Set` | `LSS.Start_Delay_Set` | mapped |
| `Start_Pressure` | `Seq/Start_Pressure` | `LSS.Start_Pressure` | mapped |
| `Start_Pressure_DB` | `Seq/Start_Pressure_DB` | `LSS.Start_Pressure_DB` | mapped |
| `Start_Time_Left` | `Seq/Start_Time_Left` | `LSS.Start_Time_Left` | mapped |
| `Stop_Delay_Set` | `Seq/Stop_Delay_Set` | `LSS.Stop_Delay_Set` | mapped |
| `Stop_Pressure` | `Seq/Stop_Pressure` | `LSS.Stop_Pressure` | mapped |
| `Stop_Pressure_DB` | `Seq/Stop_Pressure_DB` | `LSS.Stop_Pressure_DB` | mapped |
| `Stop_Time_Left` | `Seq/Stop_Time_Left` | `LSS.Stop_Time_Left` | mapped |
| `Target_Pressure` | `Seq/Target_Pressure` | `LSS.Target_Pressure` | mapped |
| `Target_Pressure_Set` | `Seq/Target_Pressure_Set` | `LSS.Target_Pressure_Set` | mapped |

</details>

<details>
<summary>HSD field map</summary>

| Field (old member name / `shared.Pax` key) | New member | Controller tag | Status |
|---|---|---|---|
| `BackupMakeUp_Close_SP` | `PlcBackupCloseSP` | `CD_SUMP_OPL1H_SET` | mapped |
| `BackupMakeUp_Open_SP` | `PlcBackupOpenSP` | `CD_SUMP_OPL1L_SET` | mapped |
| `Cfg_FastStartDB` | `Seqr/Cfg_FastStartDB` | `HSD_Seqr.Cfg_FastStartDB` | mapped |
| `Cfg_FastStartDelay` | `Seqr/Cfg_FastStartDelay` | `HSD_Seqr.Cfg_FastStartDelay` | mapped |
| `Cfg_FastStopDB` | `Seqr/Cfg_FastStopDB` | `HSD_Seqr.Cfg_FastStopDB` | mapped |
| `Cfg_FastStopDelay` | `Seqr/Cfg_FastStopDelay` | `HSD_Seqr.Cfg_FastStopDelay` | mapped |
| `Cfg_LevelLabel` | - | - | site-only |
| `Cfg_LevelPath` | - | - | site-only |
| `Cfg_SensorLabel` | - | - | site-only |
| `Cfg_SensorPath` | - | - | site-only |
| `Cfg_SlowStartDB` | `Seqr/Cfg_SlowStartDB` | `HSD_Seqr.Cfg_SlowStartDB` | mapped |
| `Cfg_SlowStartDelay` | `Seqr/Cfg_SlowStartDelay` | `HSD_Seqr.Cfg_SlowStartDelay` | mapped |
| `Cfg_SlowStopDB` | `Seqr/Cfg_SlowStopDB` | `HSD_Seqr.Cfg_SlowStopDB` | mapped |
| `Cfg_SlowStopDelay` | `Seqr/Cfg_SlowStopDelay` | `HSD_Seqr.Cfg_SlowStopDelay` | mapped |
| `Cmd_FirstNoDelay` | `PlcFirstNoDelay` | `Cmd_FirstNoDelay` | mapped |
| `MainMakeUp_Close_SP` | `PlcMainCloseSP` | `CD_SUMP_OPLH_SET` | mapped |
| `MainMakeUp_Open_SP` | `PlcMainOpenSP` | `CD_SUMP_OPLL_SET` | mapped |
| `Sequence_1` | `PlcSequence1` | `HSD_Sequence[1]` | mapped |
| `Sequence_2` | `PlcSequence2` | `HSD_Sequence[2]` | mapped |
| `Sequence_3` | `PlcSequence3` | `HSD_Sequence[3]` | mapped |
| `Sequence_4` | `PlcSequence4` | `HSD_Sequence[4]` | mapped |
| `Sequence_5` | `PlcSequence5` | `HSD_Sequence[5]` | mapped |
| `Sequence_6` | `PlcSequence6` | `HSD_Sequence[6]` | mapped |
| `Sequence_7` | `PlcSequence7` | `HSD_Sequence[7]` | mapped |
| `Sts_StartTimeLeft` | `Seqr/Sts_StartTimeLeft` | `HSD_Seqr.Sts_StartTimeLeft` | mapped |
| `Sts_StopTimeLeft` | `Seqr/Sts_StopTimeLeft` | `HSD_Seqr.Sts_StopTimeLeft` | mapped |
| `Target_Pressure_Set` | `PlcFixedSP` | `HSD_Fixed_SP` | mapped |

</details>

## Decisions

- **HSS enable hidden**: FT has an HMI enable only for LSS (`LSS_HMI_Enable`); HSS `Cfg_HasEnable` = 0, its
  `PlcHmiEnable` part has no tag (gray).
- **LSS shows 2 positions** (`Cfg_Positions` = 2), as FT.
- **PV / level lines** read the linked sensor's `AIn/Val` or `AInRef/Val` through `custom.sensorPax` / `levelPax`
  and go gray when bad. The CSV-LEVEL line regression after the cleanup (it read `AIn/Val` on an `AInRef` sensor) was
  fixed on 2026-10-23 (live 75.68 In").
- The Machine Room discharge pressure arrow reads `Sensors/HSD-Discharge Pressure/AIn/Val`.

## Live Check (2026-10-23)

HSS popup live (32.9 psig, sequence 4 / 5 / 6 / 7), HSS enable row hidden; `LSS_HMI_Enable` 0; HSD values as in the
table. The HSD setpoints are Leased: gray for a few seconds after the popup opens.
