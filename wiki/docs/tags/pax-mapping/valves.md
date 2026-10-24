---
title: Solenoid Valves (Machine Room, Condensers)
sidebar_label: 04 Valves
sidebar_position: 5
description: The four standalone solenoid valves mapped to P_ValveSO (MAIN LIQ SV, MAIN HG SV, CSV MAKEUP SV, CSV MAKEUP BACKUP SV), with the label and interlock decisions.
sources:
  - docs/pax-mapping/04-valves.md
last_verified: 2026-10-23
---

# Solenoid Valves

Source doc: `docs/pax-mapping/04-valves.md`. Type: [Devices/Valve](../reference/udts/devices/valve.md) with the nested
`Valve` part [PLC/P_ValveSO](../reference/udts/plc/p-valveso.md). Instances:
[Machine Room / Valves](../reference/devices/machine-room-valves.md), [Condensers / Valves](../reference/devices/condensers-valves.md).
The 76 valves inside the CG evaporators use the same design: [CG Valves](cg-valves.md).

## Devices And PLC Objects

| HMI device (tag path, unchanged) | PLC object | HMI label = FT label | `Intlk` part |
|---|---|---|---|
| `Machine Room/Valves/Main Liq SV` | `MAIN_LIQ_CV5` | **MAIN LIQ SV** | none (disabled) |
| `Condensers/Valves/Main HG CV6` | `MAIN_HG_CV6` | **MAIN HG SV** | none (disabled) |
| `Condensers/Valves/Main MW CV25` | `RS_MW_CV25` | **CSV MAKEUP SV** | `EC1_INTLK` (shared condenser interlock) |
| `Condensers/Valves/Backup MW CV26` | `RS_BACKUP_MW_CV26` | **CSV MAKEUP BACKUP SV** | `EC1_INTLK` |

Parameters `PlcDevice`, `ValveTag`, `IntlkTag`. Not mapped: `HSS_FL_SV` (no physical valve; deleted from `_RCP1_`),
`EPCS_CV1` (referenced by FT but no longer in the controller), and the two "OPL 1" valve symbols on FT Machine Room
(they bind no valve object).

![Valve faceplate, live](/img/tags/valve-faceplate-live.png)

## What The Faceplate Shows

| On the HMI | Member it reads | PLC tag (MAIN LIQ SV) |
|---|---|---|
| State OPENED / CLOSED / OPENING / CLOSING, travel | `Valve/Val_Sts` (state labels) | `MAIN_LIQ_CV5.Val_Sts` |
| Open / closed limit switches | `Valve/Inp_OpenLS`, `Inp_ClosedLS` (and `Cfg_HasOpenLS` / `Cfg_HasClosedLS`) | `MAIN_LIQ_CV5.Inp_OpenLS` |
| Command output | `Valve/Out` | `MAIN_LIQ_CV5.Out` |
| PERM / INTLK / BYPASS | `Valve/Inp_PermOK` + `Inp_NBPermOK`, `Valve/Inp_IntlkOK` + `Inp_NBIntlkOK`, `Valve/Sts_BypActive`, `Sts_Bypass` | |
| FAILED chip | `Valve/Nrdy_Fail` ("Device Failure (shed requires reset)", Leased) | `MAIN_LIQ_CV5.Nrdy_Fail` |
| COMM chip | `Valve/Sts_IOFault` (I/O fault) | `MAIN_LIQ_CV5.Sts_IOFault` |
| Alarms: IO FAULT, FULL STALL, TRANSIT STALL, INTLK TRIP | `Valve/Alm_IOFault`, `Alm_FullStall`, `Alm_TransitStall`, `Alm_IntlkTrip` | |
| Mode (Operator / Program / Maintenance) | `Valve/Sts_Oper`, `Sts_Prog`, `Sts_Maint` | |
| Travel time | `Valve/Cfg_TransitStallT` | |
| Not-ready reasons (Diagnostics) | `Valve/Nrdy_*` | |
| Trend default pen | `Valve/Val_Sts` | |

`valveType` and `Cmd_Position` (motor-operated / control valves only) are HMI-owned.

<details>
<summary>Full field map (106 fields, from docs/pax-mapping/04-valves.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): Main Liq SV / Main HG CV6 / Main MW CV25 / Backup MW CV26 | Status |
|---|---|---|---|---|---|
| `Ack_FullStall` | `Valve/Ack_FullStall` | `MAIN_LIQ_CV5.Ack_FullStall` | Status | 1 / 1 / 1 / 1 | mapped |
| `Ack_IOFault` | `Valve/Ack_IOFault` | `MAIN_LIQ_CV5.Ack_IOFault` | Status | 1 / 1 / 1 / 1 | mapped |
| `Ack_IntlkTrip` | `Valve/Ack_IntlkTrip` | `MAIN_LIQ_CV5.Ack_IntlkTrip` | Status | 1 / 1 / 1 / 1 | mapped |
| `Ack_TransitStall` | `Valve/Ack_TransitStall` | `MAIN_LIQ_CV5.Ack_TransitStall` | Status | 1 / 1 / 1 / 1 | mapped |
| `Alm_FullStall` | `Valve/Alm_FullStall` | `MAIN_LIQ_CV5.Alm_FullStall` | Status | 0 / 0 / 0 / 0 | mapped |
| `Alm_IOFault` | `Valve/Alm_IOFault` | `MAIN_LIQ_CV5.Alm_IOFault` | Status | 0 / 0 / 0 / 0 | mapped |
| `Alm_IntlkTrip` | `Valve/Alm_IntlkTrip` | `MAIN_LIQ_CV5.Alm_IntlkTrip` | Status | 0 / 0 / 0 / 0 | mapped |
| `Alm_TransitStall` | `Valve/Alm_TransitStall` | `MAIN_LIQ_CV5.Alm_TransitStall` | Status | 0 / 0 / 0 / 0 | mapped |
| `Cfg_FailOpen` | `Valve/Cfg_FailOpen` | `MAIN_LIQ_CV5.Cfg_FailOpen` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_FullStallT` | `Valve/Cfg_FullStallT` | `MAIN_LIQ_CV5.Cfg_FullStallT` | Faceplate | 5 / 5 / 5 / 5 | mapped |
| `Cfg_HasClosedLS` | `Valve/Cfg_HasClosedLS` | `MAIN_LIQ_CV5.Cfg_HasClosedLS` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_HasIntlkObj` | `Valve/Cfg_HasIntlkObj` | `MAIN_LIQ_CV5.Cfg_HasIntlkObj` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_HasOpenLS` | `Valve/Cfg_HasOpenLS` | `MAIN_LIQ_CV5.Cfg_HasOpenLS` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_HasPermObj` | `Valve/Cfg_HasPermObj` | `MAIN_LIQ_CV5.Cfg_HasPermObj` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_HasStatsObj` | `Valve/Cfg_HasStatsObj` | `MAIN_LIQ_CV5.Cfg_HasStatsObj` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_LSFail` | `Valve/Cfg_LSFail` | `MAIN_LIQ_CV5.Cfg_LSFail` | Faceplate | 1 / 1 / 1 / 1 | mapped |
| `Cfg_OCmdResets` | `Valve/Cfg_OCmdResets` | `MAIN_LIQ_CV5.Cfg_OCmdResets` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_OvrdPermIntlk` | `Valve/Cfg_OvrdPermIntlk` | `MAIN_LIQ_CV5.Cfg_OvrdPermIntlk` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_PCmdClear` | `Valve/Cfg_PCmdClear` | `MAIN_LIQ_CV5.Cfg_PCmdClear` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cfg_Tag` | `Valve/Cfg_Tag` | `MAIN_LIQ_CV5.Cfg_Tag` | Faceplate | "MAIN LIQ SV" / "MAIN HG SV" / "CSV MAKEUP SV" / "CSV MAKEUP BACKUP SV" | mapped |
| `Cfg_Label` | `Valve/Cfg_Label` | `MAIN_LIQ_CV5.Cfg_Label` | Faceplate | "MAIN LIQ SV" / "MAIN HG SV" / "CSV MAKEUP SV" / "CSV MAKEUP BACKUP SV" | mapped |
| `Cfg_Desc` | `Valve/Cfg_Desc` | `MAIN_LIQ_CV5.Cfg_Desc` | Faceplate | "Solenoid Operated Valve" / "Solenoid Operated Valve" / "Solenoid Operated Valve" / "Solenoid Operated Valve" | mapped |
| `Cfg_ShedOnFullStall` | `Valve/Cfg_ShedOnFullStall` | `MAIN_LIQ_CV5.Cfg_ShedOnFullStall` | Faceplate | 1 / 1 / 1 / 1 | mapped |
| `Cfg_ShedOnIOFault` | `Valve/Cfg_ShedOnIOFault` | `MAIN_LIQ_CV5.Cfg_ShedOnIOFault` | Faceplate | 1 / 1 / 1 / 1 | mapped |
| `Cfg_ShedOnTransitStall` | `Valve/Cfg_ShedOnTransitStall` | `MAIN_LIQ_CV5.Cfg_ShedOnTransitStall` | Faceplate | 1 / 1 / 1 / 1 | mapped |
| `Cfg_SimFdbkT` | `Valve/Cfg_SimFdbkT` | `MAIN_LIQ_CV5.Cfg_SimFdbkT` | Faceplate | 2 / 2 / 2 / 2 | mapped |
| `ClosedLS` | `Valve/Inp_ClosedLS` | `MAIN_LIQ_CV5.Inp_ClosedLS` | Status | 0 / 0 / 0 / 0 | mapped |
| `Cmd` | `Valve/Out` | `MAIN_LIQ_CV5.Out` | Status | 1 / 1 / 0 / 0 | mapped |
| `Cmd_Bypass` | `Valve/OCmd_Bypass` | `MAIN_LIQ_CV5.OCmd_Bypass` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cmd_Close` | `Valve/OCmd_Close` | `MAIN_LIQ_CV5.OCmd_Close` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cmd_Disable` | `Valve/MCmd_Disable` | `MAIN_LIQ_CV5.MCmd_Disable` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cmd_Enable` | `Valve/MCmd_Enable` | `MAIN_LIQ_CV5.MCmd_Enable` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cmd_Open` | `Valve/OCmd_Open` | `MAIN_LIQ_CV5.OCmd_Open` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cmd_Position` | - | - | - | - / - / - / - | site-only |
| `Cmd_Reset` | `Valve/OCmd_Reset` | `MAIN_LIQ_CV5.OCmd_Reset` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Cmd_ResetAckAll` | `Valve/OCmd_ResetAckAll` | `MAIN_LIQ_CV5.OCmd_ResetAckAll` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Comm` | `Valve/Sts_IOFault` | `MAIN_LIQ_CV5.Sts_IOFault` | Status | 0 / 0 / 0 / 0 | mapped |
| `Disabled` | `Valve/Sts_Disabled` | `MAIN_LIQ_CV5.Sts_Disabled` | Status | 0 / 0 / 0 / 0 | mapped |
| `Failed` | `Valve/Nrdy_Fail` | `MAIN_LIQ_CV5.Nrdy_Fail` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Interlock/Cfg_Bypassable` | `Intlk/Cfg_Bypassable` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt00` | `Intlk/Cfg_CondTxt00` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt01` | `Intlk/Cfg_CondTxt01` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt02` | `Intlk/Cfg_CondTxt02` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt03` | `Intlk/Cfg_CondTxt03` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt04` | `Intlk/Cfg_CondTxt04` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt05` | `Intlk/Cfg_CondTxt05` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt06` | `Intlk/Cfg_CondTxt06` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt07` | `Intlk/Cfg_CondTxt07` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt08` | `Intlk/Cfg_CondTxt08` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt09` | `Intlk/Cfg_CondTxt09` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt10` | `Intlk/Cfg_CondTxt10` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt11` | `Intlk/Cfg_CondTxt11` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt12` | `Intlk/Cfg_CondTxt12` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt13` | `Intlk/Cfg_CondTxt13` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt14` | `Intlk/Cfg_CondTxt14` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_CondTxt15` | `Intlk/Cfg_CondTxt15` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass00` | `Intlk/MSet_Bypass00` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass01` | `Intlk/MSet_Bypass01` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass02` | `Intlk/MSet_Bypass02` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass03` | `Intlk/MSet_Bypass03` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass04` | `Intlk/MSet_Bypass04` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass05` | `Intlk/MSet_Bypass05` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass06` | `Intlk/MSet_Bypass06` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass07` | `Intlk/MSet_Bypass07` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass08` | `Intlk/MSet_Bypass08` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass09` | `Intlk/MSet_Bypass09` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass10` | `Intlk/MSet_Bypass10` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass11` | `Intlk/MSet_Bypass11` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass12` | `Intlk/MSet_Bypass12` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass13` | `Intlk/MSet_Bypass13` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass14` | `Intlk/MSet_Bypass14` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/MSet_Bypass15` | `Intlk/MSet_Bypass15` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/OCmd_Reset` | `Intlk/OCmd_Reset` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Rdy_Reset` | `Intlk/Rdy_Reset` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Sts_BypActive` | `Valve/Sts_BypActive` | `MAIN_LIQ_CV5.Sts_BypActive` | Status | 0 / 0 / 0 / 0 | mapped |
| `Interlock/Sts_FirstOut` | `Intlk/Sts_FirstOut` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Sts_Intlk` | `Intlk/Sts_Intlk` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Sts_IntlkOK` | `Valve/Inp_IntlkOK` | `MAIN_LIQ_CV5.Inp_IntlkOK` | Status | 1 / 1 / 1 / 1 | mapped |
| `Interlock/Sts_NBIntlkOK` | `Valve/Inp_NBIntlkOK` | `MAIN_LIQ_CV5.Inp_NBIntlkOK` | Status | 1 / 1 / 1 / 1 | mapped |
| `Interlock/Cfg_OKState` | `Intlk/Cfg_OKState` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_Latched` | `Intlk/Cfg_Latched` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_HasNav` | `Intlk/Cfg_HasNav` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_Desc` | `Intlk/Cfg_Desc` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_Label` | `Intlk/Cfg_Label` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_Tag` | `Intlk/Cfg_Tag` | - | Faceplate | - / - / - / - | no PLC object |
| `Interlock/Cfg_PCmdClear` | `Intlk/Cfg_PCmdClear` | - | Faceplate | - / - / - / - | no PLC object |
| `MAINT` | `Valve/Sts_Maint` | `MAIN_LIQ_CV5.Sts_Maint` | Status | 0 / 0 / 0 / 0 | mapped |
| `NBPermOK` | `Valve/Inp_NBPermOK` | `MAIN_LIQ_CV5.Inp_NBPermOK` | Status | 1 / 1 / 1 / 1 | mapped |
| `Nrdy_CfgErr` | `Valve/Nrdy_CfgErr` | `MAIN_LIQ_CV5.Nrdy_CfgErr` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Nrdy_Disabled` | `Valve/Nrdy_Disabled` | `MAIN_LIQ_CV5.Nrdy_Disabled` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Nrdy_Fail` | `Valve/Nrdy_Fail` | `MAIN_LIQ_CV5.Nrdy_Fail` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Nrdy_IOFault` | `Valve/Nrdy_IOFault` | `MAIN_LIQ_CV5.Nrdy_IOFault` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Nrdy_Intlk` | `Valve/Nrdy_Intlk` | `MAIN_LIQ_CV5.Nrdy_Intlk` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Nrdy_NoMode` | `Valve/Nrdy_NoMode` | `MAIN_LIQ_CV5.Nrdy_NoMode` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Nrdy_Perm` | `Valve/Nrdy_Perm` | `MAIN_LIQ_CV5.Nrdy_Perm` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `OPER` | `Valve/Sts_Oper` | `MAIN_LIQ_CV5.Sts_Oper` | Status | 0 / 0 / 0 / 0 | mapped |
| `OpenLS` | `Valve/Inp_OpenLS` | `MAIN_LIQ_CV5.Inp_OpenLS` | Status | 0 / 0 / 0 / 0 | mapped |
| `Ovrd` | `Valve/Inp_Ovrd` | `MAIN_LIQ_CV5.Inp_Ovrd` | Status | 0 / 0 / 0 / 0 | mapped |
| `PROG` | `Valve/Sts_Prog` | `MAIN_LIQ_CV5.Sts_Prog` | Status | 1 / 1 / 1 / 1 | mapped |
| `PermOK` | `Valve/Inp_PermOK` | `MAIN_LIQ_CV5.Inp_PermOK` | Status | 1 / 1 / 1 / 1 | mapped |
| `Rdy_Close` | `Valve/Rdy_Close` | `MAIN_LIQ_CV5.Rdy_Close` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Rdy_Open` | `Valve/Rdy_Open` | `MAIN_LIQ_CV5.Rdy_Open` | Faceplate | 0 / 0 / 0 / 0 | mapped |
| `Status` | `Valve/Val_Sts` | `MAIN_LIQ_CV5.Val_Sts` | Status | 2 / 2 / 1 / 1 | mapped |
| `Sts_Bypass` | `Valve/Sts_Bypass` | `MAIN_LIQ_CV5.Sts_Bypass` | Status | 0 / 0 / 0 / 0 | mapped |
| `TravelTime` | `Valve/Cfg_TransitStallT` | `MAIN_LIQ_CV5.Cfg_TransitStallT` | Faceplate | 10 / 10 / 10 / 10 | mapped |
| `valveType` | - | - | - | - / - / - / - | site-only |

</details>

In the table, the 44 `Interlock/*` rows marked "no PLC object" were the old flat interlock members; they were removed
in the cleanup (valves have no P_Intlk object; the three status bits come from the valve object itself).

## Decisions And Evidence

1. **Labels renamed to the FT labels** (FT prints the PLC `Cfg_Label` on each valve object; the photos show MAIN LIQ
   SV, MAIN HG SV, CSV MAKEUP SV, CSV MAKEUP BACKUP SV). Changed in the embeds' `label` params, the nav labels, the
   instance `shortDescription`.
2. **Tag paths stay** (`Main HG CV6`, `Main MW CV25` ...): renaming instances would break history, Out Of Service
   records, saved trends and nav paths.
3. **`FAILED` = `Nrdy_Fail`, `COMM` = `Sts_IOFault`** (no stand-in address existed); confirmed live against the FT
   Diagnostics photo (every Not Ready reason off).
4. **No interlock condition list**: FT's valve faceplate shows only the interlock / permissive lamps and the Maintenance
   enable / bypass block; "Enable navigation to interlock object" is unchecked on the FT Engineering page. Our
   Interlocks tab shows the same Device / Bypass block. The two make-up valves take their interlock from the shared
   condenser object `EC1_INTLK` (L5X routine `Condensers/Interlocks`), whose only condition text is the PLC default, so
   `ShowInterlocks` hides their tab; Main Liq / Main HG SV have no interlock object and keep the valve's own tab.

## Alarms

P_ValveSO library alarms with the old names / priorities: **IO Fault** (High), **Full Stall** (High), **Transit
Stall** (High), **Interlock Trip** (Medium).

## Live Check (2026-10-23)

All four: every `Nrdy_*` = 0 and `Sts_IOFault` = 0 (FAILED / COMM OK, same as the FT Diagnostics photo). MAIN LIQ SV
and MAIN HG SV Opened / Program, both make-up SVs Closed / Program (matches the photos). Live `Cfg_Label` = the new
labels. The FAILED chip is Leased: gray for a few seconds after opening.

## Open Items

- Rename the instances to the FT names too? Only if the tag browser should match (history / OOS / trends would need a
  migration). Kept for now.
