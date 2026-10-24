---
title: NH3 Liquid Transfer Unit (LTU)
sidebar_label: 11 LTU
sidebar_position: 12
description: The NH3 LTU transfer count, alarm setpoint and transfer input mapped to RCP1 controller tags; the count reset is wired (2026-10-24) but untested against the live PLC.
sources:
  - docs/pax-mapping/11-ltu.md
last_verified: 2026-10-24
---

# NH3 Liquid Transfer Unit (LTU)

Source doc: `docs/pax-mapping/11-ltu.md`. Type: [Devices/LTU](../reference/udts/devices/ltu.md); instance
`Machine Room/LTU/NH3 LTU` ([page](../reference/devices/machine-room-ltu.md)). Shown in the LTU box on `/machine-room`.

The three LTU values are plain controller tags (no UDT), so they are read-only OPC atomics on the device; the
transfer input is a nested DiscreteInput.

| On the HMI | Member | PLC tag | Group |
|---|---|---|---|
| Transfer Counts | `PlcCount` | `NH3_LTU_HMI_Count` (DINT) | Direct |
| Alarm Setpoint | `PlcCountAlarmSP` | `NH3_LTU_Count_Alarm_SP` (DINT) | Leased |
| Count alarm (blinking count on FT) | `PlcCountAlarm` | `NH3_LTU_Count_Alarm_Inp` (BOOL) | Direct |
| Transfer input | `Input/DIn/*` | `NH3_LTU` (P_DIn) | Status / Faceplate |
| Daily reset settings | `ResetDaily`, `ResetTime` | HMI-owned | - |

<details>
<summary>Full field map (24 fields, from docs/pax-mapping/11-ltu.md)</summary>

| Field (old member name / `shared.Pax` key) | Reads now (member of the device) | PLC tag (first instance) | Tag group | Live sample (read only, 2026-10-22/23): NH3 LTU | Status |
|---|---|---|---|---|---|
| `Cmd_ResetCount` | `PlcResetCount` | `HMI_Ltu_Clear` | Status (atomic) | - | mapped, write-only command |
| `Count` | `PlcCount` | `NH3_LTU_HMI_Count` | Status (atomic) | 0 | mapped |
| `Count_Alarm` | `PlcCountAlarm` | `NH3_LTU_Count_Alarm_Inp` | Status (atomic) | 0 | mapped |
| `Count_Alarm_SP` | `PlcCountAlarmSP` | `NH3_LTU_Count_Alarm_SP` | Status (atomic) | 2000 | mapped |
| `Input/Cfg_Debounce` | `Input/DIn/Cfg_Debounce` | `NH3_LTU.Cfg_Debounce` | Faceplate | 0 | mapped |
| `Input/Cfg_Desc` | `Input/DIn/Cfg_Desc` | `NH3_LTU.Cfg_Desc` | Faceplate | "Discrete Input" | mapped |
| `Input/Cfg_Label` | `Input/DIn/Cfg_Label` | `NH3_LTU.Cfg_Label` | Faceplate | "Discrete Input" | mapped |
| `Input/Cfg_NoSubstPV` | `Input/DIn/Cfg_NoSubstPV` | `NH3_LTU.Cfg_NoSubstPV` | Faceplate | 0 | mapped |
| `Input/Cfg_NormTextVis` | `Input/DIn/Cfg_NormTextVis` | `NH3_LTU.Cfg_NormTextVis` | Faceplate | 1 | mapped |
| `Input/Cfg_PCmdClear` | `Input/DIn/Cfg_PCmdClear` | `NH3_LTU.Cfg_PCmdClear` | Faceplate | 1 | mapped |
| `Input/Cfg_State0Txt` | `Input/DIn/Cfg_0StText` | `NH3_LTU.Cfg_0StText` | Faceplate | "Off" | mapped |
| `Input/Cfg_State1Txt` | `Input/DIn/Cfg_1StText` | `NH3_LTU.Cfg_1StText` | Faceplate | "On" | mapped |
| `Input/Cfg_Tag` | `Input/DIn/Cfg_Tag` | `NH3_LTU.Cfg_Tag` | Faceplate | "P_DIn" | mapped |
| `Input/Inp_Target` | `Input/DIn/Inp_Target` | `NH3_LTU.Inp_Target` | Status | 1 | mapped |
| `Input/MCmd_InpPV` | `Input/DIn/MCmd_InpPV` | `NH3_LTU.MCmd_InpPV` | Faceplate | 0 | mapped |
| `Input/MCmd_SubstPV` | `Input/DIn/MCmd_SubstPV` | `NH3_LTU.MCmd_SubstPV` | Faceplate | 0 | mapped |
| `Input/MSet_SubstPV` | `Input/DIn/MSet_SubstPV` | `NH3_LTU.MSet_SubstPV` | Faceplate | 0 | mapped |
| `Input/OCmd_ResetAckAll` | `Input/DIn/OCmd_ResetAckAll` | `NH3_LTU.OCmd_ResetAckAll` | Faceplate | 0 | mapped |
| `Input/Sts_InpPV` | `Input/DIn/Sts_PV` | `NH3_LTU.Sts_PV` | Status | 0 | mapped |
| `Input/Sts_PV` | `Input/DIn/Sts` | `NH3_LTU.Sts` | Status | 0 | mapped |
| `Input/Sts_SubstPV` | `Input/DIn/Sts_SubstPV` | `NH3_LTU.Sts_SubstPV` | Status | 0 | mapped |
| `Input/Sts_TgtDisagree` | `Input/DIn/Sts_TgtDisagree` | `NH3_LTU.Sts_TgtDisagree` | Status | 1 | mapped |
| `ResetDaily` | - | - | - | - | site-only |
| `ResetTime` | - | - | - | - | site-only |

</details>

## Alarms

`PlcCountAlarm` carries the device alarm **Transfer Count High** (Medium), defined in `ATOMIC_ALARMS` of
`scripts/_build_udt_alarms.py` (count >= setpoint). The input's Target Disagree alarm is gated on the PLC enable
(off).

## Count Reset (Wired 2026-10-24)

FT's `Button5` "Reset Count" sets `{[RCP1]HMI_Ltu_Clear}` to one. In the PLC (`Equip_LTU` rung 2) that bit is a momentary 1:
the PLC clears the count and then clears the bit itself, so the HMI only writes `True` (the other branch of the rung is the
daily midnight reset). There is no interlock.

- The UDT `Devices/LTU` has a read-only OPC member `PlcResetCount` (`[{PlcDevice}]{ResetCountTag}`, tag group
  `PAX_Status`); the instance parameter `ResetCountTag` is `HMI_Ltu_Clear`.
- The LTU card on `/machine-room` shows a **Reset Count** button. A click is **one click with no confirm dialog**
  (like FT). On the gateway it checks the PLC write lock first (`PlcWriteLock.writeAllowed`: while locked it says
  "PLC Writes Locked" and writes nothing), then the permissions `Faceplates/Operate` **and** `LTU/Command`, then
  writes through `shared.Audit.writeTag`, which logs it.
- The button is disabled with a tooltip when the session is read only ("Your Role Cannot Operate Equipment") or the count is
  not Good ("PLC Link Lost - Reset Unavailable").
- Status: pending a live test, which needs PLC writes to be allowed (both write-protection layers open; see
  [PLC Write Lock](../plc-write-lock.md)).

## Live Check (2026-10-23)

Count 0, alarm SP 2000, count alarm 0: matches the FT Machine Room photo (0 / 2000). The setpoint is Leased (gray for
a few seconds after the page opens). The input `NH3_LTU` has the default label "Discrete Input".
