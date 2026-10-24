---
title: Recirc Pumps (HTLR / LTLR)
sidebar_label: 01 Recirc Pumps
sidebar_position: 2
description: The four Machine Room recirculator pumps mapped to P_Motor, P_Intlk and P_RunTime in RCP1 - field map, decisions, alarms, live check and open items.
sources:
  - docs/pax-mapping/01-recirc-pumps.md
last_verified: 2026-10-23
---

# Recirc Pumps (HTLR / LTLR)

The first device type mapped to the live PLC (pilot, 2026-10-22) and the pattern every other type follows. Source
doc: `docs/pax-mapping/01-recirc-pumps.md`.

## Devices And PLC Objects

| HMI device (`[default]Boars_Head/GrovePort/Machine Room/Pumps/...`) | `Motor` (`PLC/P_Motor`) | `Intlk` (`PLC/P_Intlk`) | `RunTime` (`PLC/P_RunTime`) |
|---|---|---|---|
| `HTLR-Pump 1` | `HTR_PUMPS[1]` | `HTR_PUMP1_INTLK` | `HTR_PUMPS_RUNTIME[1]` |
| `HTLR-Pump 2` | `HTR_PUMPS[2]` | `HTR_PUMP2_INTLK` | `HTR_PUMPS_RUNTIME[2]` |
| `LTLR-Pump 1` | `LTR_PUMPS[1]` | `LTR_PUMP1_INTLK` | `LTR_PUMPS_RUNTIME[1]` |
| `LTLR-Pump 2` | `LTR_PUMPS[2]` | `LTR_PUMP2_INTLK` | `LTR_PUMPS_RUNTIME[2]` |

Type: [Devices/Pump](../reference/udts/devices/pump.md); instances:
[Machine Room / Pumps](../reference/devices/machine-room-pumps.md). Parameters `PlcDevice = RCP1`, `MotorTag`,
`IntlkTag`, `RunTimeTag`; all three parts enabled.

The pump alarm discrete inputs `HTR_PUMPS_ALM[n]` / `LTR_PUMPS_ALM[n]` are **not** on the pump: they live on the
tank (`Pump1Alm` / `Pump2Alm`, see [Tanks](tanks.md)), where FT HTR-SP / LTR-SP show them, so the alarm exists once.

## What The Faceplate Shows

| On the HMI | Member it reads | PLC tag (HTLR-Pump 1) |
|---|---|---|
| Status RUNNING / STOPPED, the tile color | `Motor/Val_Sts` (state labels) and `Motor/Sts_Running` / `Sts_Stopped` | `HTR_PUMPS[1].Val_Sts`, `.Sts_Running` |
| Mode Operator / Program / Maintenance (and Hand, Override, No Mode icons) | `Motor/Sts_Oper`, `Sts_Prog`, `Sts_Maint`, `Sts_Hand`, `Sts_Ovrd`, `Sts_NoMode`; `Motor/Mode/Val` | `HTR_PUMPS[1].Sts_Oper` ..., `.Mode.Val` |
| PERM / INTLK / BYPASS chips | `Motor/Inp_PermOK` + `Inp_NBPermOK`, `Intlk/Sts_IntlkOK` + `Sts_NBIntlkOK`, `Intlk/Sts_BypActive` | `HTR_PUMPS[1].Inp_PermOK`, `HTR_PUMP1_INTLK.Sts_IntlkOK` |
| Faults: FAIL START, FAIL STOP, I/O FAULT, INTLK TRIP, START FAILED | `Motor/Alm_FailToStart`, `Alm_FailToStop`, `Alm_IOFault`, `Alm_IntlkTrip`, `Sts_FailToStart` (`Sts_IOFault` for the I/O state; the `Ack_*` bits on the Alarms tab) | `HTR_PUMPS[1].Alm_FailToStart` ... |
| Start / Stop ready, "not ready" reasons | `Motor/Rdy_Start`, `Rdy_Stop`, `Nrdy_*` | `HTR_PUMPS[1].Rdy_Start` ... |
| KPI Runtime hours / Motor starts | `RunTime/Val_TotRunHrs`, `RunTime/Val_Starts` | `HTR_PUMPS_RUNTIME[1].Val_TotRunHrs`, `.Val_Starts` |
| KPI Fail-to-start timer | `Motor/Cfg_FailToStartT` (Leased) | `HTR_PUMPS[1].Cfg_FailToStartT` |
| Interlocks tab: 16 conditions, first out, bypass | `Intlk/Cfg_CondTxt/Cfg_CondTxt_n_`, `Intlk/Sts_Intlk`, `Sts_FirstOut`, `MSet_Bypass00..15` | `HTR_PUMP1_INTLK.Cfg_CondTxt[n]` ... |
| Configuration tab (Has Run Feedback, Shed On Fail ...) | `Motor/Cfg_*` (Leased) | `HTR_PUMPS[1].Cfg_*` |
| Labels | `Motor/Cfg_Label`, `Cfg_Tag`, `Cfg_Desc` | `HTR_PUMPS[1].Cfg_Label` = "HTRL-PUMP #1" |
| Trend tab default pens | `Motor/Val_Sts`, `RunTime/Val_TotRunHrs` | (historized) |

**Coverage:** 125 HMI fields per pump (78 pump members + 47 interlock members): 123 mapped, 2 site-only. 20 members
the controller has (`Cfg_FailToStartT`, `Cfg_HasNav`, `Cfg_Latched`, `Cfg_OKState`, the 16 `Cfg_CondTxt`) were added to
the library because the `_RCP1_` keep rule had pruned them.

<details>
<summary>Full field map (125 fields, from docs/pax-mapping/01-recirc-pumps.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): HTLR-Pump 1 / HTLR-Pump 2 / LTLR-Pump 1 / LTLR-Pump 2 | Status |
|---|---|---|---|---|---|
| `Ack_FailToStart` | `Motor/Ack_FailToStart` | `HTR_PUMPS[1].Ack_FailToStart` | Status | true / true / true / true | mapped |
| `Ack_FailToStop` | `Motor/Ack_FailToStop` | `HTR_PUMPS[1].Ack_FailToStop` | Status | true / true / true / true | mapped |
| `Ack_IOFault` | `Motor/Ack_IOFault` | `HTR_PUMPS[1].Ack_IOFault` | Status | true / true / true / true | mapped |
| `Ack_IntlkTrip` | `Motor/Ack_IntlkTrip` | `HTR_PUMPS[1].Ack_IntlkTrip` | Status | true / true / true / true | mapped |
| `Alm_FailToStart` | `Motor/Alm_FailToStart` | `HTR_PUMPS[1].Alm_FailToStart` | Status | false / false / false / false | mapped |
| `Alm_FailToStop` | `Motor/Alm_FailToStop` | `HTR_PUMPS[1].Alm_FailToStop` | Status | false / false / false / false | mapped |
| `Alm_IOFault` | `Motor/Alm_IOFault` | `HTR_PUMPS[1].Alm_IOFault` | Status | false / false / false / false | mapped |
| `Alm_IntlkTrip` | `Motor/Alm_IntlkTrip` | `HTR_PUMPS[1].Alm_IntlkTrip` | Status | false / false / false / false | mapped |
| `AutoEN` | - | - | - | - / - / - / - | site-only |
| `Cfg_FailToStopT` | `Motor/Cfg_FailToStopT` | `HTR_PUMPS[1].Cfg_FailToStopT` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_HasIntlkObj` | `Motor/Cfg_HasIntlkObj` | `HTR_PUMPS[1].Cfg_HasIntlkObj` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_HasOvldObj` | `Motor/Cfg_HasOvldObj` | `HTR_PUMPS[1].Cfg_HasOvldObj` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_HasPermObj` | `Motor/Cfg_HasPermObj` | `HTR_PUMPS[1].Cfg_HasPermObj` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_HasResInhObj` | `Motor/Cfg_HasResInhObj` | `HTR_PUMPS[1].Cfg_HasResInhObj` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_HasRunFdbk` | `Motor/Cfg_HasRunFdbk` | `HTR_PUMPS[1].Cfg_HasRunFdbk` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_HasRunTimeObj` | `Motor/Cfg_HasRunTimeObj` | `HTR_PUMPS[1].Cfg_HasRunTimeObj` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_OCmdResets` | `Motor/Cfg_OCmdResets` | `HTR_PUMPS[1].Cfg_OCmdResets` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_OvrdPermIntlk` | `Motor/Cfg_OvrdPermIntlk` | `HTR_PUMPS[1].Cfg_OvrdPermIntlk` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_PCmdClear` | `Motor/Cfg_PCmdClear` | `HTR_PUMPS[1].Cfg_PCmdClear` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_SimFdbkT` | `Motor/Cfg_SimFdbkT` | `HTR_PUMPS[1].Cfg_SimFdbkT` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_AllowLocal` | `Motor/Cfg_AllowLocal` | `HTR_PUMPS[1].Cfg_AllowLocal` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_OperStopPrio` | `Motor/Cfg_OperStopPrio` | `HTR_PUMPS[1].Cfg_OperStopPrio` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_ShedOnFailToStart` | `Motor/Cfg_ShedOnFailToStart` | `HTR_PUMPS[1].Cfg_ShedOnFailToStart` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_ShedOnIOFault` | `Motor/Cfg_ShedOnIOFault` | `HTR_PUMPS[1].Cfg_ShedOnIOFault` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Cfg_Tag` | `Motor/Cfg_Tag` | `HTR_PUMPS[1].Cfg_Tag` | Faceplate | `HTRL-PUMP #3` / `HTRL-PUMP #2` / `LTRL-PUMP #1` / `LTRL-PUMP #2` | mapped |
| `Cfg_Label` | `Motor/Cfg_Label` | `HTR_PUMPS[1].Cfg_Label` | Faceplate | `HTRL-PUMP #1` / `HTRL-PUMP #2` / `LTRL-PUMP #1` / `LTRL-PUMP #2` | mapped |
| `Cfg_Desc` | `Motor/Cfg_Desc` | `HTR_PUMPS[1].Cfg_Desc` | Faceplate | `Single Speed Motor` / `Single Speed Motor` / `Single Speed Motor` / `Single Speed Motor` | mapped |
| `Fail_Timer_PRE` | `Motor/Cfg_FailToStartT` | `HTR_PUMPS[1].Cfg_FailToStartT` | Faceplate | `10` / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Inp_Sim` | `Motor/Inp_Sim` | `HTR_PUMPS[1].Inp_Sim` | Status | false / false / false / false | mapped |
| `Interlock/Cfg_Bypassable` | `Intlk/Cfg_Bypassable` | `HTR_PUMP1_INTLK.Cfg_Bypassable` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/Cfg_CondTxt00` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_0_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[0]` | Faceplate | `HSS Comp Running` / `HSS Comp Running` / `LSS Comp Running` / `LSS Comp Running` | mapped (added) |
| `Interlock/Cfg_CondTxt01` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_1_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[1]` | Faceplate | `HTR OPL Ok` / `HTR-LoLo Alarm` / `LTR OPL Ok` / `LTR OPL Ok` | mapped (added) |
| `Interlock/Cfg_CondTxt02` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_2_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[2]` | Faceplate | `HTR P1 Guardian Alm` / `HTR P2 Guardian Alm` / `LTR P1 Guardian Alm` / `LTR P2 Guardian Alm` | mapped (added) |
| `Interlock/Cfg_CondTxt03` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_3_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[3]` | Faceplate | `RCP-MCR` / `RCP-MCR` / `RCP-MCR` / `RCP-MCR` | mapped (added) |
| `Interlock/Cfg_CondTxt04` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_4_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[4]` | Faceplate | `Power Up Time` / `Power Up Time` / `Power Up Time` / `Power Up Time` | mapped (added) |
| `Interlock/Cfg_CondTxt05` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_5_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[5]` | Faceplate | `Start Pressure` / `Start Pressure` / `Start Pressure` / `Start Pressure` | mapped (added) |
| `Interlock/Cfg_CondTxt06` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_6_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[6]` | Faceplate | `Pump LoLo Pressure` / `Pump LoLo Pressure` / `Pump LoLo Pressure` / `Pump LoLo Pressure` | mapped (added) |
| `Interlock/Cfg_CondTxt07` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_7_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[7]` | Faceplate | `Pump LoLo Pressure` / `Pump LoLo Pressure` / `Pump LoLo Pressure` / `Pump LoLo Pressure` | mapped (added) |
| `Interlock/Cfg_CondTxt08` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_8_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[8]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_CondTxt09` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_9_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[9]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_CondTxt10` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_10_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[10]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_CondTxt11` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_11_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[11]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_CondTxt12` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_12_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[12]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_CondTxt13` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_13_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[13]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_CondTxt14` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_14_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[14]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_CondTxt15` | `Intlk/Cfg_CondTxt/Cfg_CondTxt_15_` | `HTR_PUMP1_INTLK.Cfg_CondTxt[15]` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/MSet_Bypass00` | `Intlk/MSet_Bypass00` | `HTR_PUMP1_INTLK.MSet_Bypass00` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass01` | `Intlk/MSet_Bypass01` | `HTR_PUMP1_INTLK.MSet_Bypass01` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass02` | `Intlk/MSet_Bypass02` | `HTR_PUMP1_INTLK.MSet_Bypass02` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass03` | `Intlk/MSet_Bypass03` | `HTR_PUMP1_INTLK.MSet_Bypass03` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass04` | `Intlk/MSet_Bypass04` | `HTR_PUMP1_INTLK.MSet_Bypass04` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass05` | `Intlk/MSet_Bypass05` | `HTR_PUMP1_INTLK.MSet_Bypass05` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass06` | `Intlk/MSet_Bypass06` | `HTR_PUMP1_INTLK.MSet_Bypass06` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass07` | `Intlk/MSet_Bypass07` | `HTR_PUMP1_INTLK.MSet_Bypass07` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass08` | `Intlk/MSet_Bypass08` | `HTR_PUMP1_INTLK.MSet_Bypass08` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass09` | `Intlk/MSet_Bypass09` | `HTR_PUMP1_INTLK.MSet_Bypass09` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass10` | `Intlk/MSet_Bypass10` | `HTR_PUMP1_INTLK.MSet_Bypass10` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass11` | `Intlk/MSet_Bypass11` | `HTR_PUMP1_INTLK.MSet_Bypass11` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass12` | `Intlk/MSet_Bypass12` | `HTR_PUMP1_INTLK.MSet_Bypass12` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass13` | `Intlk/MSet_Bypass13` | `HTR_PUMP1_INTLK.MSet_Bypass13` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass14` | `Intlk/MSet_Bypass14` | `HTR_PUMP1_INTLK.MSet_Bypass14` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/MSet_Bypass15` | `Intlk/MSet_Bypass15` | `HTR_PUMP1_INTLK.MSet_Bypass15` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/OCmd_Reset` | `Intlk/OCmd_Reset` | `HTR_PUMP1_INTLK.OCmd_Reset` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/Rdy_Reset` | `Intlk/Rdy_Reset` | `HTR_PUMP1_INTLK.Rdy_Reset` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Interlock/Sts_BypActive` | `Intlk/Sts_BypActive` | `HTR_PUMP1_INTLK.Sts_BypActive` | Status | false / false / false / false | mapped |
| `Interlock/Sts_FirstOut` | `Intlk/Sts_FirstOut` | `HTR_PUMP1_INTLK.Sts_FirstOut` | Status | 0 / 0 / 32 / 1 | mapped |
| `Interlock/Sts_Intlk` | `Intlk/Sts_Intlk` | `HTR_PUMP1_INTLK.Sts_Intlk` | Status | 0 / 0 / 33 / 33 | mapped |
| `Interlock/Sts_IntlkOK` | `Intlk/Sts_IntlkOK` | `HTR_PUMP1_INTLK.Sts_IntlkOK` | Status | true / true / false / false | mapped |
| `Interlock/Sts_NBIntlkOK` | `Intlk/Sts_NBIntlkOK` | `HTR_PUMP1_INTLK.Sts_NBIntlkOK` | Status | true / true / false / false | mapped |
| `Interlock/Cfg_OKState` | `Intlk/Cfg_OKState` | `HTR_PUMP1_INTLK.Cfg_OKState` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_Latched` | `Intlk/Cfg_Latched` | `HTR_PUMP1_INTLK.Cfg_Latched` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_HasNav` | `Intlk/Cfg_HasNav` | `HTR_PUMP1_INTLK.Cfg_HasNav` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped (added) |
| `Interlock/Cfg_Desc` | `Intlk/Cfg_Desc` | `HTR_PUMP1_INTLK.Cfg_Desc` | Faceplate | `Interlocks with First Out` / `Interlocks with First Out` / `Interlocks with First Out` / `Interlocks with First Out` | mapped |
| `Interlock/Cfg_Label` | `Intlk/Cfg_Label` | `HTR_PUMP1_INTLK.Cfg_Label` | Faceplate | `HTR Pump1` / `HTR Pump2` / `LTR Pump1` / `LTR Pump2` | mapped |
| `Interlock/Cfg_Tag` | `Intlk/Cfg_Tag` | `HTR_PUMP1_INTLK.Cfg_Tag` | Faceplate | `P_Intlk` / `P_Intlk` / `P_Intlk` / `P_Intlk` | mapped |
| `Interlock/Cfg_PCmdClear` | `Intlk/Cfg_PCmdClear` | `HTR_PUMP1_INTLK.Cfg_PCmdClear` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `MCmd_Disable` | `Motor/MCmd_Disable` | `HTR_PUMPS[1].MCmd_Disable` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `MCmd_Enable` | `Motor/MCmd_Enable` | `HTR_PUMPS[1].MCmd_Enable` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Min_Runtime_Set` | - | - | - | - / - / - / - | site-only |
| `NBPermOK` | `Motor/Inp_NBPermOK` | `HTR_PUMPS[1].Inp_NBPermOK` | Status | true / true / false / false | mapped |
| `Nrdy_CfgErr` | `Motor/Nrdy_CfgErr` | `HTR_PUMPS[1].Nrdy_CfgErr` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Nrdy_Disabled` | `Motor/Nrdy_Disabled` | `HTR_PUMPS[1].Nrdy_Disabled` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Nrdy_Fail` | `Motor/Nrdy_Fail` | `HTR_PUMPS[1].Nrdy_Fail` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Nrdy_IOFault` | `Motor/Nrdy_IOFault` | `HTR_PUMPS[1].Nrdy_IOFault` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Nrdy_Intlk` | `Motor/Nrdy_Intlk` | `HTR_PUMPS[1].Nrdy_Intlk` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Nrdy_NoMode` | `Motor/Nrdy_NoMode` | `HTR_PUMPS[1].Nrdy_NoMode` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Nrdy_Perm` | `Motor/Nrdy_Perm` | `HTR_PUMPS[1].Nrdy_Perm` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `OCmd_AcqLock` | `Motor/Mode/OCmd_AcqLock` | `HTR_PUMPS[1].Mode.OCmd_AcqLock` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `OCmd_Bypass` | `Motor/OCmd_Bypass` | `HTR_PUMPS[1].OCmd_Bypass` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `OCmd_Reset` | `Motor/OCmd_Reset` | `HTR_PUMPS[1].OCmd_Reset` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `OCmd_ResetAckAll` | `Motor/OCmd_ResetAckAll` | `HTR_PUMPS[1].OCmd_ResetAckAll` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `OCmd_Start` | `Motor/OCmd_Start` | `HTR_PUMPS[1].OCmd_Start` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `OCmd_Stop` | `Motor/OCmd_Stop` | `HTR_PUMPS[1].OCmd_Stop` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `OCmd_UnlockRel` | `Motor/Mode/OCmd_UnlockRel` | `HTR_PUMPS[1].Mode.OCmd_UnlockRel` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Ovrd` | `Motor/Inp_Ovrd` | `HTR_PUMPS[1].Inp_Ovrd` | Status | false / false / false / false | mapped |
| `PermOK` | `Motor/Inp_PermOK` | `HTR_PUMPS[1].Inp_PermOK` | Status | true / true / false / false | mapped |
| `Rdy_OAcq` | `Motor/Mode/Rdy_OAcq` | `HTR_PUMPS[1].Mode.Rdy_OAcq` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Rdy_OLock` | `Motor/Mode/Rdy_OLock` | `HTR_PUMPS[1].Mode.Rdy_OLock` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Rdy_ORel` | `Motor/Mode/Rdy_ORel` | `HTR_PUMPS[1].Mode.Rdy_ORel` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Rdy_OUnlock` | `Motor/Mode/Rdy_OUnlock` | `HTR_PUMPS[1].Mode.Rdy_OUnlock` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Rdy_ResetAckAll` | `Motor/Rdy_ResetAckAll` | `HTR_PUMPS[1].Rdy_ResetAckAll` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Rdy_Start` | `Motor/Rdy_Start` | `HTR_PUMPS[1].Rdy_Start` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Rdy_Stop` | `Motor/Rdy_Stop` | `HTR_PUMPS[1].Rdy_Stop` | Faceplate | _leased_ / _leased_ / _leased_ / _leased_ | mapped |
| `Sts_AlmInh` | `Motor/Sts_AlmInh` | `HTR_PUMPS[1].Sts_AlmInh` | Status | false / false / false / false | mapped |
| `Sts_Disabled` | `Motor/Sts_Disabled` | `HTR_PUMPS[1].Sts_Disabled` | Status | false / false / false / false | mapped |
| `Sts_Err` | `Motor/Sts_Err` | `HTR_PUMPS[1].Sts_Err` | Status | false / false / false / false | mapped |
| `Sts_FailToStart` | `Motor/Sts_FailToStart` | `HTR_PUMPS[1].Sts_FailToStart` | Status | false / false / false / false | mapped |
| `Sts_FailToStop` | `Motor/Sts_FailToStop` | `HTR_PUMPS[1].Sts_FailToStop` | Status | false / false / false / false | mapped |
| `Sts_Hand` | `Motor/Sts_Hand` | `HTR_PUMPS[1].Sts_Hand` | Status | false / false / false / false | mapped |
| `Sts_IOFault` | `Motor/Sts_IOFault` | `HTR_PUMPS[1].Sts_IOFault` | Status | false / false / false / false | mapped |
| `Sts_Maint` | `Motor/Sts_Maint` | `HTR_PUMPS[1].Sts_Maint` | Status | false / false / false / false | mapped |
| `Sts_MaintByp` | `Motor/Sts_MaintByp` | `HTR_PUMPS[1].Sts_MaintByp` | Status | false / false / false / false | mapped |
| `Sts_NoMode` | `Motor/Sts_NoMode` | `HTR_PUMPS[1].Sts_NoMode` | Status | false / false / false / false | mapped |
| `Sts_Oper` | `Motor/Sts_Oper` | `HTR_PUMPS[1].Sts_Oper` | Status | false / false / false / false | mapped |
| `Sts_Ovrd` | `Motor/Sts_Ovrd` | `HTR_PUMPS[1].Sts_Ovrd` | Status | false / false / false / false | mapped |
| `Sts_Prog` | `Motor/Sts_Prog` | `HTR_PUMPS[1].Sts_Prog` | Status | true / true / true / true | mapped |
| `Sts_ProgOperLock` | `Motor/Mode/Sts_ProgOperLock` | `HTR_PUMPS[1].Mode.Sts_ProgOperLock` | Status | false / false / false / false | mapped |
| `Sts_ProgOperSel` | `Motor/Mode/Sts_ProgOperSel` | `HTR_PUMPS[1].Mode.Sts_ProgOperSel` | Status | true / true / true / true | mapped |
| `Sts_Running` | `Motor/Sts_Running` | `HTR_PUMPS[1].Sts_Running` | Status | false / true / false / false | mapped |
| `Sts_Stopped` | `Motor/Sts_Stopped` | `HTR_PUMPS[1].Sts_Stopped` | Status | true / false / true / true | mapped |
| `Val_Mode` | `Motor/Mode/Val` | `HTR_PUMPS[1].Mode.Val` | Status | 8 / 8 / 8 / 8 | mapped |
| `Val_Notify` | `Motor/Val_Notify` | `HTR_PUMPS[1].Val_Notify` | Status | 0 / 0 / 0 / 0 | mapped |
| `Val_Starts` | `RunTime/Val_Starts` | `HTR_PUMPS_RUNTIME[1].Val_Starts` | Status | 456 / 502 / 1 / 1 | mapped |
| `Val_Sts` | `Motor/Val_Sts` | `HTR_PUMPS[1].Val_Sts` | Status | 1 / 2 / 1 / 1 | mapped |
| `Val_TotRunHrs` | `RunTime/Val_TotRunHrs` | `HTR_PUMPS_RUNTIME[1].Val_TotRunHrs` | Status | 4.03e+04 / 4.65e+04 / 0 / 0 | mapped |

</details>

The two site-only fields `AutoEN` / `Min_Runtime_Set` (no P_Motor member) were **removed** on 2026-10-23 at the
user's request, together with the "Auto Enable" configuration row. (On compressors the same names are real PLC
members and stay.)

## Decisions

- **Device UDT with nested PlantPAx UDTs** (this pilot set the design): the library stays generic
  (`DeviceName` / `TagPrefix`) and the device passes its own tag names ([PlantPAx Library](../udts/pax-library.md)).
- **Live alarms** on the library members with the old pump priorities (user Q1).
- **History** on every numeric `Val*` member of the Direct group (user Q3); Leased members are not historized.
- **PAX tag groups** `PAX_Status` / `PAX_Faceplate` (user Q4), later re-tuned (Status 1 s -> 5 s, Faceplate background
  60 s) because the SecureLink link is the bottleneck.
- **Gray placeholder for bad values** instead of "null" (the "Fail-to-start timer null" report): the member was right,
  it was a Leased value still loading over a slow link.
- **Commands refused**: `shared.ValveCommands` (start / stop / reset / mode / bypass) refuses every write for a
  PLC-mapped device; the buttons are disabled.

## Alarms

From the library ([Alarms](../alarms.md)): **IO Fault** (Critical), **Fail To Start** (High), **Fail To Stop**
(High), **Interlock Trip** (Medium) on `Motor/Alm_*`. Site / Area / Device from the path. No alarm on the interlock
or run time parts.

## Live Check (2026-10-23, Read Only)

- HTLR-Pump 2 running, HTLR-Pump 1 and both LTLR pumps stopped (matches the FT Machine Room photo). Lead pump:
  `HTRL_PUMPS_SEQ.Cfg_Lead` = 2 (HTR), 1 (LTR).
- `Cfg_Label` = HTRL-PUMP #1 / #2, LTRL-PUMP #1 / #2 (the FT labels).
- Every faceplate value live, no binding error. Leased values (for example the 10 s fail-to-start timer) show the
  gray dash for a few seconds after opening, then fill.

## Open Items

1. `HTR_PUMPS[1].Cfg_Tag` reads "HTRL-PUMP #3" while its label is "#1": a PLC configuration typo (we only read it);
   tell the controls engineer.
2. The LTR pumps show 0.0 run hours, 1 start, Permissives Not OK and are interlocked ("LSS Comp Running", "Start
   Pressure"): expected for standby pumps behind the LSS sequence.
3. The pump faceplate MODE value showed the gray dash after the cleanup; fixed 2026-10-23 (the shared `Modes` asset
   now reads `'/' + {view.custom.pax} + '/Sts_*'`).
