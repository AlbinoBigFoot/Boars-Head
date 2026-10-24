---
title: Exhaust Fans (MR EF, BR EF)
sidebar_label: 10 Exhaust Fans
sidebar_position: 11
description: The Machine Room and boiler room exhaust fans mapped to their run-feedback P_DIn and fail-to-start BOOL.
sources:
  - docs/pax-mapping/10-exhaust-fans.md
last_verified: 2026-10-23
---

# Exhaust Fans

Source doc: `docs/pax-mapping/10-exhaust-fans.md`. Type: [Devices/ExhaustFan](../reference/udts/devices/exhaustfan.md)
(parameters `FanTag`, `FailTag`; part `DIn` -> P_DIn; atomic `FailToStart`). Instances:
[Machine Room / ExhaustFans](../reference/devices/machine-room-exhaustfans.md).

| HMI device | `DIn` (P_DIn, run feedback) | `FailToStart` (BOOL) | FT evidence |
|---|---|---|---|
| `Machine Room/ExhaustFans/MR EF` | `MR_EEF15` | `MR_EEF15_FailToStart` | `(STELLAR)MachineRoom.xml`: `MR_EEF15.Sts_PV`, `MR_EEF15_FailToStart` (SAFETYS box "MR EF") |
| `Machine Room/ExhaustFans/BR EF` | `BR_EEF17` | `BR_EEF17_FailToStart` | same, "BR EF" |

## Field Map

| Field (old member) | Reads now | PLC tag (MR EF) | Notes |
|---|---|---|---|
| `Started` | `DIn/Sts_PV` | `MR_EEF15.Sts_PV` | the sail switch run confirm; the fan symbol |
| `Failed` | `FailToStart` | `MR_EEF15_FailToStart` | Direct atomic |
| `Status` | `DIn/Val_Fault` | `MR_EEF15.Val_Fault` | 16 = target disagree |
| `Alm` | `DIn/Sts_TgtDisagree` | `MR_EEF15.Sts_TgtDisagree` | the stand-in pointed at `Sts_Fault`, which a P_DIn does not have |

The `Airflow` field of the old component was removed (there never was such a member).

## Decisions

- **`MR_EEF1` / `MR_EEF2`** (P_Motor "Machine Room Emergency Exhaust Fan #1 / #2") are called by **no routine** in the
  L5X and read `EnableIn` 0 live, so they are not mapped (user: map only if they work). The fans stay on the run
  confirms `MR_EEF15` / `BR_EEF17`.
- The Interlocks tab is hidden (P_DIn has no interlock).

## Alarms

The P_DIn **Target Disagree** alarm, gated on `Cfg_HasTgtDisagreeAlm` (0 on both fans, so no alarm, as FT). Live both
fans read `Inp_PV` 0 with `Inp_Target` 1, so `Sts_TgtDisagree` = 1; before the gating that raised two alarms FT never
showed.

## Open Items

- The `/exhaust-fans` table shows "True" for `Val_Fault` = 16 (display oddity).
- The exhaust fan faceplate was not opened by the automated checks (row click target); open it by hand once.
