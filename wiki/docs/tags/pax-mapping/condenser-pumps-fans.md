---
title: Condenser Sump Pumps And Fans
sidebar_label: 08 Condenser Pumps / Fans
sidebar_position: 9
description: The three condenser sump pumps and four evaporative condenser fans mapped with the pump design (P_Motor, P_RunTime) and the shared EC1_INTLK interlock.
sources:
  - docs/pax-mapping/08-condenser-pumps-fans.md
last_verified: 2026-10-23
---

# Condenser Sump Pumps And Fans

Source doc: `docs/pax-mapping/08-condenser-pumps-fans.md`. These seven motors are `Devices/Pump` instances and use the
[recirc pump](recirc-pumps.md) design unchanged. Instances: [Condensers / Pumps](../reference/devices/condensers-pumps.md),
[EC-1A](../reference/devices/condensers-condensers-ec-1a.md), [EC-1B](../reference/devices/condensers-condensers-ec-1b.md).

## Devices And PLC Objects

| HMI device | `Motor` (P_Motor) | `RunTime` (P_RunTime) | `Intlk` |
|---|---|---|---|
| `Condensers/Pumps/Sump Pump 1` .. `3` | `CD1_P1` .. `CD1_P3` | `CD1_P1_Runtime` .. `CD1_P3_Runtime` | `EC1_INTLK` |
| `Condensers/Condensers/EC-1A/Fan 1`, `Fan 2` | `CD1A_FAN1`, `CD1A_FAN2` | `CD1A_FAN1_Runtime`, `CD1A_FAN2_Runtime` | `EC1_INTLK` |
| `Condensers/Condensers/EC-1B/Fan 1`, `Fan 2` | `CD1B_FAN1`, `CD1B_FAN2` | `CD1B_FAN1_Runtime`, `CD1B_FAN2_Runtime` | `EC1_INTLK` |

FT evidence: `(STELLAR)Condensers.xml` `GO_P_Motor {[RCP1]CD1_Pn}` with `#124 {[RCP1]CD1_Pn_Runtime}`; the condenser
fan faceplate photos ("CD1A-FAN #1 - Single Speed Motor").

The condenser graphic `02_Components/01_Devices/Condenser` (EC-1A / EC-1B) reads its fans' `Motor/Val_Sts`; the sump
pumps use the standard Pump component and faceplate. Field map: identical to the recirc pumps (76 mapped fields per
motor).

<details>
<summary>Full field map (125 fields, from docs/pax-mapping/08-condenser-pumps-fans.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): Sump Pump 1 | Status |
|---|---|---|---|---|---|
| `Ack_FailToStart` | `Motor/Ack_FailToStart` | `CD1_P1.Ack_FailToStart` | Status | 1 | mapped |
| `Ack_FailToStop` | `Motor/Ack_FailToStop` | `CD1_P1.Ack_FailToStop` | Status | 1 | mapped |
| `Ack_IOFault` | `Motor/Ack_IOFault` | `CD1_P1.Ack_IOFault` | Status | 1 | mapped |
| `Ack_IntlkTrip` | `Motor/Ack_IntlkTrip` | `CD1_P1.Ack_IntlkTrip` | Status | 1 | mapped |
| `Alm_FailToStart` | `Motor/Alm_FailToStart` | `CD1_P1.Alm_FailToStart` | Status | 0 | mapped |
| `Alm_FailToStop` | `Motor/Alm_FailToStop` | `CD1_P1.Alm_FailToStop` | Status | 0 | mapped |
| `Alm_IOFault` | `Motor/Alm_IOFault` | `CD1_P1.Alm_IOFault` | Status | 0 | mapped |
| `Alm_IntlkTrip` | `Motor/Alm_IntlkTrip` | `CD1_P1.Alm_IntlkTrip` | Status | 0 | mapped |
| `AutoEN` | - | - | - | - | site-only |
| `Cfg_FailToStopT` | `Motor/Cfg_FailToStopT` | `CD1_P1.Cfg_FailToStopT` | Faceplate | 10 | mapped |
| `Cfg_HasIntlkObj` | `Motor/Cfg_HasIntlkObj` | `CD1_P1.Cfg_HasIntlkObj` | Faceplate | 0 | mapped |
| `Cfg_HasOvldObj` | `Motor/Cfg_HasOvldObj` | `CD1_P1.Cfg_HasOvldObj` | Faceplate | 0 | mapped |
| `Cfg_HasPermObj` | `Motor/Cfg_HasPermObj` | `CD1_P1.Cfg_HasPermObj` | Faceplate | 0 | mapped |
| `Cfg_HasResInhObj` | `Motor/Cfg_HasResInhObj` | `CD1_P1.Cfg_HasResInhObj` | Faceplate | 0 | mapped |
| `Cfg_HasRunFdbk` | `Motor/Cfg_HasRunFdbk` | `CD1_P1.Cfg_HasRunFdbk` | Faceplate | 0 | mapped |
| `Cfg_HasRunTimeObj` | `Motor/Cfg_HasRunTimeObj` | `CD1_P1.Cfg_HasRunTimeObj` | Faceplate | 1 | mapped |
| `Cfg_OCmdResets` | `Motor/Cfg_OCmdResets` | `CD1_P1.Cfg_OCmdResets` | Faceplate | 0 | mapped |
| `Cfg_OvrdPermIntlk` | `Motor/Cfg_OvrdPermIntlk` | `CD1_P1.Cfg_OvrdPermIntlk` | Faceplate | 0 | mapped |
| `Cfg_PCmdClear` | `Motor/Cfg_PCmdClear` | `CD1_P1.Cfg_PCmdClear` | Faceplate | 0 | mapped |
| `Cfg_SimFdbkT` | `Motor/Cfg_SimFdbkT` | `CD1_P1.Cfg_SimFdbkT` | Faceplate | 2 | mapped |
| `Cfg_AllowLocal` | `Motor/Cfg_AllowLocal` | `CD1_P1.Cfg_AllowLocal` | Faceplate | 0 | mapped |
| `Cfg_OperStopPrio` | `Motor/Cfg_OperStopPrio` | `CD1_P1.Cfg_OperStopPrio` | Faceplate | 0 | mapped |
| `Cfg_ShedOnFailToStart` | `Motor/Cfg_ShedOnFailToStart` | `CD1_P1.Cfg_ShedOnFailToStart` | Faceplate | 1 | mapped |
| `Cfg_ShedOnIOFault` | `Motor/Cfg_ShedOnIOFault` | `CD1_P1.Cfg_ShedOnIOFault` | Faceplate | 1 | mapped |
| `Cfg_Tag` | `Motor/Cfg_Tag` | `CD1_P1.Cfg_Tag` | Faceplate | "CD-SUMP-PUMP #1" | mapped |
| `Cfg_Label` | `Motor/Cfg_Label` | `CD1_P1.Cfg_Label` | Faceplate | "CD-SUMP-PUMP #1" | mapped |
| `Cfg_Desc` | `Motor/Cfg_Desc` | `CD1_P1.Cfg_Desc` | Faceplate | "Single Speed Motor" | mapped |
| `Fail_Timer_PRE` | `Motor/Cfg_FailToStartT` | `CD1_P1.Cfg_FailToStartT` | Faceplate | 10 | mapped (added) |
| `Inp_Sim` | `Motor/Inp_Sim` | `CD1_P1.Inp_Sim` | Status | 0 | mapped |
| `Interlock/Cfg_Bypassable` | `Intlk/Cfg_Bypassable` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt00` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_0_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt01` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_1_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt02` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_2_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt03` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_3_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt04` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_4_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt05` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_5_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt06` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_6_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt07` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_7_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt08` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_8_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt09` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_9_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt10` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_10_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt11` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_11_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt12` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_12_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt13` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_13_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt14` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_14_` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_CondTxt15` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_15_` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass00` | `Intlk/MSet_Bypass00` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass01` | `Intlk/MSet_Bypass01` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass02` | `Intlk/MSet_Bypass02` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass03` | `Intlk/MSet_Bypass03` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass04` | `Intlk/MSet_Bypass04` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass05` | `Intlk/MSet_Bypass05` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass06` | `Intlk/MSet_Bypass06` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass07` | `Intlk/MSet_Bypass07` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass08` | `Intlk/MSet_Bypass08` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass09` | `Intlk/MSet_Bypass09` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass10` | `Intlk/MSet_Bypass10` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass11` | `Intlk/MSet_Bypass11` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass12` | `Intlk/MSet_Bypass12` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass13` | `Intlk/MSet_Bypass13` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass14` | `Intlk/MSet_Bypass14` | - | Faceplate | - | no PLC object |
| `Interlock/MSet_Bypass15` | `Intlk/MSet_Bypass15` | - | Faceplate | - | no PLC object |
| `Interlock/OCmd_Reset` | `Intlk/OCmd_Reset` | - | Faceplate | - | no PLC object |
| `Interlock/Rdy_Reset` | `Intlk/Rdy_Reset` | - | Faceplate | - | no PLC object |
| `Interlock/Sts_BypActive` | `Intlk/Sts_BypActive` | - | Status | - | no PLC object |
| `Interlock/Sts_FirstOut` | `Intlk/Sts_FirstOut` | - | Status | - | no PLC object |
| `Interlock/Sts_Intlk` | `Intlk/Sts_Intlk` | - | Status | - | no PLC object |
| `Interlock/Sts_IntlkOK` | `Intlk/Sts_IntlkOK` | - | Status | - | no PLC object |
| `Interlock/Sts_NBIntlkOK` | `Intlk/Sts_NBIntlkOK` | - | Status | - | no PLC object |
| `Interlock/Cfg_OKState` | `Intlk/Cfg_OKState` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_Latched` | `Intlk/Cfg_Latched` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_HasNav` | `Intlk/Cfg_HasNav` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_Desc` | `Intlk/Cfg_Desc` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_Label` | `Intlk/Cfg_Label` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_Tag` | `Intlk/Cfg_Tag` | - | Faceplate | - | no PLC object |
| `Interlock/Cfg_PCmdClear` | `Intlk/Cfg_PCmdClear` | - | Faceplate | - | no PLC object |
| `MCmd_Disable` | `Motor/MCmd_Disable` | `CD1_P1.MCmd_Disable` | Faceplate | 0 | mapped |
| `MCmd_Enable` | `Motor/MCmd_Enable` | `CD1_P1.MCmd_Enable` | Faceplate | 0 | mapped |
| `Min_Runtime_Set` | - | - | - | - | site-only |
| `NBPermOK` | `Motor/Inp_NBPermOK` | `CD1_P1.Inp_NBPermOK` | Status | 1 | mapped |
| `Nrdy_CfgErr` | `Motor/Nrdy_CfgErr` | `CD1_P1.Nrdy_CfgErr` | Faceplate | 0 | mapped |
| `Nrdy_Disabled` | `Motor/Nrdy_Disabled` | `CD1_P1.Nrdy_Disabled` | Faceplate | 0 | mapped |
| `Nrdy_Fail` | `Motor/Nrdy_Fail` | `CD1_P1.Nrdy_Fail` | Faceplate | 0 | mapped |
| `Nrdy_IOFault` | `Motor/Nrdy_IOFault` | `CD1_P1.Nrdy_IOFault` | Faceplate | 0 | mapped |
| `Nrdy_Intlk` | `Motor/Nrdy_Intlk` | `CD1_P1.Nrdy_Intlk` | Faceplate | 0 | mapped |
| `Nrdy_NoMode` | `Motor/Nrdy_NoMode` | `CD1_P1.Nrdy_NoMode` | Faceplate | 0 | mapped |
| `Nrdy_Perm` | `Motor/Nrdy_Perm` | `CD1_P1.Nrdy_Perm` | Faceplate | 0 | mapped |
| `OCmd_AcqLock` | `Motor/Mode/OCmd_AcqLock` | `CD1_P1.Mode.OCmd_AcqLock` | Faceplate | 0 | mapped |
| `OCmd_Bypass` | `Motor/OCmd_Bypass` | `CD1_P1.OCmd_Bypass` | Faceplate | 0 | mapped |
| `OCmd_Reset` | `Motor/OCmd_Reset` | `CD1_P1.OCmd_Reset` | Faceplate | 0 | mapped |
| `OCmd_ResetAckAll` | `Motor/OCmd_ResetAckAll` | `CD1_P1.OCmd_ResetAckAll` | Faceplate | 0 | mapped |
| `OCmd_Start` | `Motor/OCmd_Start` | `CD1_P1.OCmd_Start` | Faceplate | 0 | mapped |
| `OCmd_Stop` | `Motor/OCmd_Stop` | `CD1_P1.OCmd_Stop` | Faceplate | 0 | mapped |
| `OCmd_UnlockRel` | `Motor/Mode/OCmd_UnlockRel` | `CD1_P1.Mode.OCmd_UnlockRel` | Faceplate | 0 | mapped |
| `Ovrd` | `Motor/Inp_Ovrd` | `CD1_P1.Inp_Ovrd` | Status | 0 | mapped |
| `PermOK` | `Motor/Inp_PermOK` | `CD1_P1.Inp_PermOK` | Status | 1 | mapped |
| `Rdy_OAcq` | `Motor/Mode/Rdy_OAcq` | `CD1_P1.Mode.Rdy_OAcq` | Faceplate | 1 | mapped |
| `Rdy_OLock` | `Motor/Mode/Rdy_OLock` | `CD1_P1.Mode.Rdy_OLock` | Faceplate | 0 | mapped |
| `Rdy_ORel` | `Motor/Mode/Rdy_ORel` | `CD1_P1.Mode.Rdy_ORel` | Faceplate | 0 | mapped |
| `Rdy_OUnlock` | `Motor/Mode/Rdy_OUnlock` | `CD1_P1.Mode.Rdy_OUnlock` | Faceplate | 0 | mapped |
| `Rdy_ResetAckAll` | `Motor/Rdy_ResetAckAll` | `CD1_P1.Rdy_ResetAckAll` | Faceplate | 0 | mapped |
| `Rdy_Start` | `Motor/Rdy_Start` | `CD1_P1.Rdy_Start` | Faceplate | 0 | mapped |
| `Rdy_Stop` | `Motor/Rdy_Stop` | `CD1_P1.Rdy_Stop` | Faceplate | 0 | mapped |
| `Sts_AlmInh` | `Motor/Sts_AlmInh` | `CD1_P1.Sts_AlmInh` | Status | 0 | mapped |
| `Sts_Disabled` | `Motor/Sts_Disabled` | `CD1_P1.Sts_Disabled` | Status | 0 | mapped |
| `Sts_Err` | `Motor/Sts_Err` | `CD1_P1.Sts_Err` | Status | 0 | mapped |
| `Sts_FailToStart` | `Motor/Sts_FailToStart` | `CD1_P1.Sts_FailToStart` | Status | 0 | mapped |
| `Sts_FailToStop` | `Motor/Sts_FailToStop` | `CD1_P1.Sts_FailToStop` | Status | 0 | mapped |
| `Sts_Hand` | `Motor/Sts_Hand` | `CD1_P1.Sts_Hand` | Status | 0 | mapped |
| `Sts_IOFault` | `Motor/Sts_IOFault` | `CD1_P1.Sts_IOFault` | Status | 0 | mapped |
| `Sts_Maint` | `Motor/Sts_Maint` | `CD1_P1.Sts_Maint` | Status | 0 | mapped |
| `Sts_MaintByp` | `Motor/Sts_MaintByp` | `CD1_P1.Sts_MaintByp` | Status | 0 | mapped |
| `Sts_NoMode` | `Motor/Sts_NoMode` | `CD1_P1.Sts_NoMode` | Status | 0 | mapped |
| `Sts_Oper` | `Motor/Sts_Oper` | `CD1_P1.Sts_Oper` | Status | 0 | mapped |
| `Sts_Ovrd` | `Motor/Sts_Ovrd` | `CD1_P1.Sts_Ovrd` | Status | 0 | mapped |
| `Sts_Prog` | `Motor/Sts_Prog` | `CD1_P1.Sts_Prog` | Status | 1 | mapped |
| `Sts_ProgOperLock` | `Motor/Mode/Sts_ProgOperLock` | `CD1_P1.Mode.Sts_ProgOperLock` | Status | 0 | mapped |
| `Sts_ProgOperSel` | `Motor/Mode/Sts_ProgOperSel` | `CD1_P1.Mode.Sts_ProgOperSel` | Status | 1 | mapped |
| `Sts_Running` | `Motor/Sts_Running` | `CD1_P1.Sts_Running` | Status | 0 | mapped |
| `Sts_Stopped` | `Motor/Sts_Stopped` | `CD1_P1.Sts_Stopped` | Status | 1 | mapped |
| `Val_Mode` | `Motor/Mode/Val` | `CD1_P1.Mode.Val` | Status | 8 | mapped |
| `Val_Notify` | `Motor/Val_Notify` | `CD1_P1.Val_Notify` | Status | 0 | mapped |
| `Val_Starts` | `RunTime/Val_Starts` | `CD1_P1_Runtime.Val_Starts` | Status | 62 | mapped |
| `Val_Sts` | `Motor/Val_Sts` | `CD1_P1.Val_Sts` | Status | 1 | mapped |
| `Val_TotRunHrs` | `RunTime/Val_TotRunHrs` | `CD1_P1_Runtime.Val_TotRunHrs` | Status | 171.6 | mapped |

</details>

The table is the mapping as first done: the `Interlock/*` rows were "no PLC object" and `AutoEN` /
`Min_Runtime_Set` were site-only. Since 2026-10-23 the `Intlk` part reads the shared `EC1_INTLK` (below) and the two
site-only fields are removed.

## Interlocks Tab

All seven motors take `Inp_IntlkOK` from the shared P_Intlk **`EC1_INTLK`** (L5X routine `Condensers/Interlocks`,
conditions `RCP_MCR.Sts_Out` and `Tmr_PwrUp20.DN`), so their `Intlk` part reads it. Its only condition text is the
PLC default "Enter Description #0", so the `ShowInterlocks` rule **hides** the Interlocks tab on these motors (user
decision, second round of 2026-10-23). `CD1A_INTLK` / `CD1B_INTLK` exist but are used in no routine.

## Alarms

P_Motor library alarms: IO Fault (Critical), Fail To Start / Fail To Stop (High), Interlock Trip (Medium).

## Live Check (2026-10-23)

- Run states: HMI = PLC at the same moment (fans stage on and off).
- Labels: `CD1A_FAN1.Cfg_Label` = "CD1A-FAN #2" and `CD1A_FAN2.Cfg_Label` = "CD1A-FAN #1" (swapped / duplicated in the
  PLC; both `Cfg_Tag` "CD1A-FAN #1"); CD1B and the sump pumps are consistent. **Our labels are kept** ("Fan 1" under
  EC-1A).
- HSD sequence positions (sump pumps 0 / 4 / 2; fans 4 / 3 / 1 / 2) match the FT Condensers High Stage Discharge
  photo (they come from the [HSD sequence](sequences.md)).

## Open Items

- Tell the controls engineer about the swapped `CD1A_FAN1` / `CD1A_FAN2` labels in the PLC.
