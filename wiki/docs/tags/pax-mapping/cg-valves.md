---
title: CG Solenoid Valves (76 Nested Valves)
sidebar_label: 07 CG Valves
sidebar_position: 8
description: The four solenoid valves inside each CG evaporator mapped to the CG_*_SV P_ValveSO arrays; 3-valve and 4-valve groups.
sources:
  - docs/pax-mapping/07-cg-valves.md
last_verified: 2026-10-23
---

# CG Solenoid Valves

Source doc: `docs/pax-mapping/07-cg-valves.md`. Each CG evaporator nests four `Devices/Valve` instances under
`<CG>/Valves/`: `Liquid SV`, `Suction SV`, `Hot Gas SV`, `Bleed SV`. They use exactly the
[standalone valve](valves.md) design (nested `Valve` part, `PLC/P_ValveSO`, read only); the evaporator passes its
`LiquidSVTag` / `SuctionSVTag` / `HotGasSVTag` / `BleedSVTag` parameters down to each valve's `ValveTag`.

Before this mapping the 76 valves were static placeholders (the "CLOSED 2.0 s" states on the CG pages were not real).

## PLC Objects

| CG | n | Display | Liquid SV | Suction SV | Hot Gas SV | Bleed SV |
|---|---|---|---|---|---|---|
| CG-A1, A2, B1, B2 | 1-4 | 4-valve | `CG_Liquid_SV[n]` | `CG_Suction_SV[n]` | `CG_HotGas_SV[n]` | `CG_Bleed_SV[n]` |
| CG-C1, D1 | 5, 6 | 3-valve | `CG_Liquid_SV[n]` | `CG_Suction_SV[n]` | `CG_HotGas_SV[n]` | **no PLC object** |
| CG-E1 .. E4, F1 .. F4, G1 | 7-15 | 4-valve | `CG_Liquid_SV[n]` | `CG_Suction_SV[n]` | `CG_HotGas_SV[n]` | `CG_Bleed_SV[n]` |
| CG-G2 .. G5 | 16-19 | 3-valve | `CG_Liquid_SV[n]` | `CG_Suction_SV[n]` | `CG_HotGas_SV[n]` | **no PLC object** |

70 of the 76 valves are mapped. The six Bleed SV instances of the 3-valve groups keep `BleedSVTag` empty and their
part disabled; the CG page does not draw them (it follows `CG/Cfg_HasBleedValve`) and the evaporator faceplate's
valve row shows the gray dash. Resolved objects per instance: the area `Utility` pages under
[Device Instances](../reference/devices/index.md).

**Evidence:** FT `(STELLAR)CGDX,4VL(L,S,B,HG)` has four `GO_P_ValveSO` objects (`{[#3]CG_Liquid_SV[#1]}` ...),
`(STELLAR)CGDX,3VL(L,S,HG)` the same without the bleed valve; which CG uses which display comes from the DashBoard
CG objects. The controller agrees: the `_RCP1_` keep rule kept `CG_Bleed_SV[n]` for exactly the 13 four-valve
groups.

## What The CG Page Shows

The P&ID valve embeds (`02_Components/01_Devices/SolenoidValve`) read `Valves/<name>/Valve/Val_Sts` (state and travel
text), and the valve faceplate is the standard one ([Valves](valves.md)).

<details>
<summary>Full field map (106 fields, from docs/pax-mapping/07-cg-valves.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | Controller member (CG-F2 Liquid SV) | Tag group | Status |
|---|---|---|---|---|
| `Ack_FullStall` | `Valve/Ack_FullStall` | `CG_Liquid_SV[12].Ack_FullStall` | Status | mapped |
| `Ack_IOFault` | `Valve/Ack_IOFault` | `CG_Liquid_SV[12].Ack_IOFault` | Status | mapped |
| `Ack_IntlkTrip` | `Valve/Ack_IntlkTrip` | `CG_Liquid_SV[12].Ack_IntlkTrip` | Status | mapped |
| `Ack_TransitStall` | `Valve/Ack_TransitStall` | `CG_Liquid_SV[12].Ack_TransitStall` | Status | mapped |
| `Alm_FullStall` | `Valve/Alm_FullStall` | `CG_Liquid_SV[12].Alm_FullStall` | Status | mapped |
| `Alm_IOFault` | `Valve/Alm_IOFault` | `CG_Liquid_SV[12].Alm_IOFault` | Status | mapped |
| `Alm_IntlkTrip` | `Valve/Alm_IntlkTrip` | `CG_Liquid_SV[12].Alm_IntlkTrip` | Status | mapped |
| `Alm_TransitStall` | `Valve/Alm_TransitStall` | `CG_Liquid_SV[12].Alm_TransitStall` | Status | mapped |
| `Cfg_FailOpen` | `Valve/Cfg_FailOpen` | `CG_Liquid_SV[12].Cfg_FailOpen` | Faceplate | mapped |
| `Cfg_FullStallT` | `Valve/Cfg_FullStallT` | `CG_Liquid_SV[12].Cfg_FullStallT` | Faceplate | mapped |
| `Cfg_HasClosedLS` | `Valve/Cfg_HasClosedLS` | `CG_Liquid_SV[12].Cfg_HasClosedLS` | Faceplate | mapped |
| `Cfg_HasIntlkObj` | `Valve/Cfg_HasIntlkObj` | `CG_Liquid_SV[12].Cfg_HasIntlkObj` | Faceplate | mapped |
| `Cfg_HasOpenLS` | `Valve/Cfg_HasOpenLS` | `CG_Liquid_SV[12].Cfg_HasOpenLS` | Faceplate | mapped |
| `Cfg_HasPermObj` | `Valve/Cfg_HasPermObj` | `CG_Liquid_SV[12].Cfg_HasPermObj` | Faceplate | mapped |
| `Cfg_HasStatsObj` | `Valve/Cfg_HasStatsObj` | `CG_Liquid_SV[12].Cfg_HasStatsObj` | Faceplate | mapped |
| `Cfg_LSFail` | `Valve/Cfg_LSFail` | `CG_Liquid_SV[12].Cfg_LSFail` | Faceplate | mapped |
| `Cfg_OCmdResets` | `Valve/Cfg_OCmdResets` | `CG_Liquid_SV[12].Cfg_OCmdResets` | Faceplate | mapped |
| `Cfg_OvrdPermIntlk` | `Valve/Cfg_OvrdPermIntlk` | `CG_Liquid_SV[12].Cfg_OvrdPermIntlk` | Faceplate | mapped |
| `Cfg_PCmdClear` | `Valve/Cfg_PCmdClear` | `CG_Liquid_SV[12].Cfg_PCmdClear` | Faceplate | mapped |
| `Cfg_Tag` | `Valve/Cfg_Tag` | `CG_Liquid_SV[12].Cfg_Tag` | Faceplate | mapped |
| `Cfg_Label` | `Valve/Cfg_Label` | `CG_Liquid_SV[12].Cfg_Label` | Faceplate | mapped |
| `Cfg_Desc` | `Valve/Cfg_Desc` | `CG_Liquid_SV[12].Cfg_Desc` | Faceplate | mapped |
| `Cfg_ShedOnFullStall` | `Valve/Cfg_ShedOnFullStall` | `CG_Liquid_SV[12].Cfg_ShedOnFullStall` | Faceplate | mapped |
| `Cfg_ShedOnIOFault` | `Valve/Cfg_ShedOnIOFault` | `CG_Liquid_SV[12].Cfg_ShedOnIOFault` | Faceplate | mapped |
| `Cfg_ShedOnTransitStall` | `Valve/Cfg_ShedOnTransitStall` | `CG_Liquid_SV[12].Cfg_ShedOnTransitStall` | Faceplate | mapped |
| `Cfg_SimFdbkT` | `Valve/Cfg_SimFdbkT` | `CG_Liquid_SV[12].Cfg_SimFdbkT` | Faceplate | mapped |
| `ClosedLS` | `Valve/Inp_ClosedLS` | `CG_Liquid_SV[12].Inp_ClosedLS` | Status | mapped |
| `Cmd` | `Valve/Out` | `CG_Liquid_SV[12].Out` | Status | mapped |
| `Cmd_Bypass` | `Valve/OCmd_Bypass` | `CG_Liquid_SV[12].OCmd_Bypass` | Faceplate | mapped |
| `Cmd_Close` | `Valve/OCmd_Close` | `CG_Liquid_SV[12].OCmd_Close` | Faceplate | mapped |
| `Cmd_Disable` | `Valve/MCmd_Disable` | `CG_Liquid_SV[12].MCmd_Disable` | Faceplate | mapped |
| `Cmd_Enable` | `Valve/MCmd_Enable` | `CG_Liquid_SV[12].MCmd_Enable` | Faceplate | mapped |
| `Cmd_Open` | `Valve/OCmd_Open` | `CG_Liquid_SV[12].OCmd_Open` | Faceplate | mapped |
| `Cmd_Position` | - | - | - | site-only |
| `Cmd_Reset` | `Valve/OCmd_Reset` | `CG_Liquid_SV[12].OCmd_Reset` | Faceplate | mapped |
| `Cmd_ResetAckAll` | `Valve/OCmd_ResetAckAll` | `CG_Liquid_SV[12].OCmd_ResetAckAll` | Faceplate | mapped |
| `Comm` | `Valve/Sts_IOFault` | `CG_Liquid_SV[12].Sts_IOFault` | Status | mapped |
| `Disabled` | `Valve/Sts_Disabled` | `CG_Liquid_SV[12].Sts_Disabled` | Status | mapped |
| `Failed` | `Valve/Nrdy_Fail` | `CG_Liquid_SV[12].Nrdy_Fail` | Faceplate | mapped |
| `Interlock/Cfg_Bypassable` | `Intlk/Cfg_Bypassable` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt00` | `Intlk/Cfg_CondTxt00` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt01` | `Intlk/Cfg_CondTxt01` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt02` | `Intlk/Cfg_CondTxt02` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt03` | `Intlk/Cfg_CondTxt03` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt04` | `Intlk/Cfg_CondTxt04` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt05` | `Intlk/Cfg_CondTxt05` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt06` | `Intlk/Cfg_CondTxt06` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt07` | `Intlk/Cfg_CondTxt07` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt08` | `Intlk/Cfg_CondTxt08` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt09` | `Intlk/Cfg_CondTxt09` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt10` | `Intlk/Cfg_CondTxt10` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt11` | `Intlk/Cfg_CondTxt11` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt12` | `Intlk/Cfg_CondTxt12` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt13` | `Intlk/Cfg_CondTxt13` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt14` | `Intlk/Cfg_CondTxt14` | - | - | no PLC object |
| `Interlock/Cfg_CondTxt15` | `Intlk/Cfg_CondTxt15` | - | - | no PLC object |
| `Interlock/MSet_Bypass00` | `Intlk/MSet_Bypass00` | - | - | no PLC object |
| `Interlock/MSet_Bypass01` | `Intlk/MSet_Bypass01` | - | - | no PLC object |
| `Interlock/MSet_Bypass02` | `Intlk/MSet_Bypass02` | - | - | no PLC object |
| `Interlock/MSet_Bypass03` | `Intlk/MSet_Bypass03` | - | - | no PLC object |
| `Interlock/MSet_Bypass04` | `Intlk/MSet_Bypass04` | - | - | no PLC object |
| `Interlock/MSet_Bypass05` | `Intlk/MSet_Bypass05` | - | - | no PLC object |
| `Interlock/MSet_Bypass06` | `Intlk/MSet_Bypass06` | - | - | no PLC object |
| `Interlock/MSet_Bypass07` | `Intlk/MSet_Bypass07` | - | - | no PLC object |
| `Interlock/MSet_Bypass08` | `Intlk/MSet_Bypass08` | - | - | no PLC object |
| `Interlock/MSet_Bypass09` | `Intlk/MSet_Bypass09` | - | - | no PLC object |
| `Interlock/MSet_Bypass10` | `Intlk/MSet_Bypass10` | - | - | no PLC object |
| `Interlock/MSet_Bypass11` | `Intlk/MSet_Bypass11` | - | - | no PLC object |
| `Interlock/MSet_Bypass12` | `Intlk/MSet_Bypass12` | - | - | no PLC object |
| `Interlock/MSet_Bypass13` | `Intlk/MSet_Bypass13` | - | - | no PLC object |
| `Interlock/MSet_Bypass14` | `Intlk/MSet_Bypass14` | - | - | no PLC object |
| `Interlock/MSet_Bypass15` | `Intlk/MSet_Bypass15` | - | - | no PLC object |
| `Interlock/OCmd_Reset` | `Intlk/OCmd_Reset` | - | - | no PLC object |
| `Interlock/Rdy_Reset` | `Intlk/Rdy_Reset` | - | - | no PLC object |
| `Interlock/Sts_BypActive` | `Valve/Sts_BypActive` | `CG_Liquid_SV[12].Sts_BypActive` | Status | mapped |
| `Interlock/Sts_FirstOut` | `Intlk/Sts_FirstOut` | - | - | no PLC object |
| `Interlock/Sts_Intlk` | `Intlk/Sts_Intlk` | - | - | no PLC object |
| `Interlock/Sts_IntlkOK` | `Valve/Inp_IntlkOK` | `CG_Liquid_SV[12].Inp_IntlkOK` | Status | mapped |
| `Interlock/Sts_NBIntlkOK` | `Valve/Inp_NBIntlkOK` | `CG_Liquid_SV[12].Inp_NBIntlkOK` | Status | mapped |
| `Interlock/Cfg_OKState` | `Intlk/Cfg_OKState` | - | - | no PLC object |
| `Interlock/Cfg_Latched` | `Intlk/Cfg_Latched` | - | - | no PLC object |
| `Interlock/Cfg_HasNav` | `Intlk/Cfg_HasNav` | - | - | no PLC object |
| `Interlock/Cfg_Desc` | `Intlk/Cfg_Desc` | - | - | no PLC object |
| `Interlock/Cfg_Label` | `Intlk/Cfg_Label` | - | - | no PLC object |
| `Interlock/Cfg_Tag` | `Intlk/Cfg_Tag` | - | - | no PLC object |
| `Interlock/Cfg_PCmdClear` | `Intlk/Cfg_PCmdClear` | - | - | no PLC object |
| `MAINT` | `Valve/Sts_Maint` | `CG_Liquid_SV[12].Sts_Maint` | Status | mapped |
| `NBPermOK` | `Valve/Inp_NBPermOK` | `CG_Liquid_SV[12].Inp_NBPermOK` | Status | mapped |
| `Nrdy_CfgErr` | `Valve/Nrdy_CfgErr` | `CG_Liquid_SV[12].Nrdy_CfgErr` | Faceplate | mapped |
| `Nrdy_Disabled` | `Valve/Nrdy_Disabled` | `CG_Liquid_SV[12].Nrdy_Disabled` | Faceplate | mapped |
| `Nrdy_Fail` | `Valve/Nrdy_Fail` | `CG_Liquid_SV[12].Nrdy_Fail` | Faceplate | mapped |
| `Nrdy_IOFault` | `Valve/Nrdy_IOFault` | `CG_Liquid_SV[12].Nrdy_IOFault` | Faceplate | mapped |
| `Nrdy_Intlk` | `Valve/Nrdy_Intlk` | `CG_Liquid_SV[12].Nrdy_Intlk` | Faceplate | mapped |
| `Nrdy_NoMode` | `Valve/Nrdy_NoMode` | `CG_Liquid_SV[12].Nrdy_NoMode` | Faceplate | mapped |
| `Nrdy_Perm` | `Valve/Nrdy_Perm` | `CG_Liquid_SV[12].Nrdy_Perm` | Faceplate | mapped |
| `OPER` | `Valve/Sts_Oper` | `CG_Liquid_SV[12].Sts_Oper` | Status | mapped |
| `OpenLS` | `Valve/Inp_OpenLS` | `CG_Liquid_SV[12].Inp_OpenLS` | Status | mapped |
| `Ovrd` | `Valve/Inp_Ovrd` | `CG_Liquid_SV[12].Inp_Ovrd` | Status | mapped |
| `PROG` | `Valve/Sts_Prog` | `CG_Liquid_SV[12].Sts_Prog` | Status | mapped |
| `PermOK` | `Valve/Inp_PermOK` | `CG_Liquid_SV[12].Inp_PermOK` | Status | mapped |
| `Rdy_Close` | `Valve/Rdy_Close` | `CG_Liquid_SV[12].Rdy_Close` | Faceplate | mapped |
| `Rdy_Open` | `Valve/Rdy_Open` | `CG_Liquid_SV[12].Rdy_Open` | Faceplate | mapped |
| `Status` | `Valve/Val_Sts` | `CG_Liquid_SV[12].Val_Sts` | Status | mapped |
| `Sts_Bypass` | `Valve/Sts_Bypass` | `CG_Liquid_SV[12].Sts_Bypass` | Status | mapped |
| `TravelTime` | `Valve/Cfg_TransitStallT` | `CG_Liquid_SV[12].Cfg_TransitStallT` | Faceplate | mapped |
| `valveType` | - | - | - | site-only |

</details>

## Decisions

- **3-valve = 4-valve without the top valve and its piping**: checked against `Control Group Overview 4 Valve.png`
  (CG-F2); the 3-valve groups draw without the Bleed SV and its loop, driven by `Cfg_HasBleedValve`.
- **Labels stay short** ("Liquid SV" ...); the PLC `Cfg_Label` is "CG-xx LIQUID SV" (the CG name is already the page
  title).
- **`CG_SoftHotGas_SV`, `CG_DC_SV`, `CG_Reheat_SV`** exist and are driven in `Evaporator_NH3/CG_Control`, but appear on
  no FT display: not used by the HMI.

## Alarms

P_ValveSO library alarms on the 70 mapped valves: IO Fault (High), Full Stall (High), Transit Stall (High),
Interlock Trip (Medium).

## Live Check (2026-10-23)

States read live on the CG pages and the CG valve faceplate (FAILED chip Leased: gray for a few seconds, then OK).
`CG[n].Cfg_HasBleedValve` = 0 on C1, D1, G2-G5.

## Open Items

- The nested CG valves have their `Intlk` part enabled by the instance overrides, but the evaporator passes no
  `IntlkTag`, so that part has no PLC object (visible on the generated instance pages as "(no PLC object)"). The
  valves have no P_Intlk in the PLC; the override is harmless but could be cleaned up on those instances (disable the `Intlk` part).
