# Phase — Pump (`260731-5un`)

## Done
- Trimmed **`Devices/Pump`** to PLC `P_Motor` / `P_RunTime` / `P_Intlk`-backed members only.
- **`Interlock`**: Folder → `UdtInstance` `typeId: Config/Interlock` (dropped `Cfg_CondTxt*`).
- Locked **`AutoEN`**, **`Fail_Timer_PRE`**, **`Min_Runtime_Set`**: `_Root/Digital` / `_Root/Analog`.
- Created **`RCP1/HTLR-Pump 1`** OPC folder for Machine Room test pump.
- Wired **`Units/Machine Room/HTLR-Pump 1`** `…/Value` `sourceTagPath`s → `[default]RCP1/HTLR-Pump 1/…`.
- Updated Pump Controls faceplate + overview device bindings for renames/removals.
- Sim: Pump faceplate defaults/profiles + dtype helpers only.

## Devices/Pump final members

| Member | typeId | PLC source |
|--------|--------|------------|
| Alm_FailToStart | `_Root/Digital` | `HTR_PUMPS[1].Alm_FailToStart` |
| Alm_IOFault | `_Root/Digital` | `HTR_PUMPS[1].Alm_IOFault` |
| AutoEN | `_Root/Digital` | (locked; no P_Motor leaf — unwired) |
| OCmd_Start | `_Root/Digital` | `HTR_PUMPS[1].OCmd_Start` |
| OCmd_Stop | `_Root/Digital` | `HTR_PUMPS[1].OCmd_Stop` |
| OCmd_Reset | `_Root/Digital` | `HTR_PUMPS[1].OCmd_Reset` |
| Fail_Timer_PRE | `_Root/Analog` | `HTR_PUMPS[1].Cfg_FailToStartT` |
| Sts_FailToStart | `_Root/Digital` | `HTR_PUMPS[1].Sts_FailToStart` |
| Sts_Maint | `_Root/Digital` | `HTR_PUMPS[1].Sts_Maint` |
| Sts_Oper | `_Root/Digital` | `HTR_PUMPS[1].Sts_Oper` |
| Sts_Prog | `_Root/Digital` | `HTR_PUMPS[1].Sts_Prog` |
| Sts_Running | `_Root/Digital` | `HTR_PUMPS[1].Sts_Running` |
| Val_Starts | `_Root/Analog` | `HTR_PUMPS_RUNTIME[1].Val_Starts` |
| Val_Sts | `_Root/Multistate` | `HTR_PUMPS[1].Val_Sts` |
| Val_TotRunHrs | `_Root/Analog` | `HTR_PUMPS_RUNTIME[1].Val_TotRunHrs` |
| Min_Runtime_Set | `_Root/Analog` | (locked; no P_Motor leaf — unwired) |
| Interlock | `Config/Interlock` | `HTR_PUMP1_INTLK.*` |
| _Alarms | `Config/_Alarms` | HMI rollup |

## Removed (not P_Motor-backed)

| Removed | Notes |
|---------|-------|
| Flow (+ SP) | Process KPI; not on P_Motor |
| SummaryInstances | Expression rollup; not PLC |
| Cmd_Auto / Cmd_Manual | No matching P_Motor cmds |
| Cfg_CondTxt00–15 | Not in Config/Interlock / P_Intlk HMI set |
| Alm / Comm / Failed / Started / OPER / MAINT / PROG / Cmd_* / RuntimeHours / MotorStarts / Status | Renamed to PLC leaf names |

## RCP1 path

| Layer | Path |
|-------|------|
| Ignition tags | `[default]RCP1/HTLR-Pump 1/<member>` |
| Motor OPC | `ns=1;s=[RCP1]HTR_PUMPS[1].<member>` |
| Runtime OPC | `ns=1;s=[RCP1]HTR_PUMPS_RUNTIME[1].Val_Starts` / `Val_TotRunHrs` |
| Interlock OPC | `ns=1;s=[RCP1]HTR_PUMP1_INTLK.<member>` |
| Unit instance | `Units/Machine Room` → `HTLR-Pump 1` |

## Notes
- `Devices/udts.json` / `Units/udts.json` Pump edits were applied atomically in this agent session and landed in HEAD via concurrent `feat(260731-5un): Tank UDT trim…` commit (shared file). This commit adds RCP1 OPC folder, faceplate/overview bindings, sim CSV, and this phase note.
