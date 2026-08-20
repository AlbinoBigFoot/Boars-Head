# Pump (P_Motor) FT → BH Faceplate Gap Matrix

Reference: Machine Room recirculation pumps (`HTR_PUMPS[n]` / `LTR_PUMPS[n]`) via RA-BAS **P_Motor**.
FT archive has **`(RA-BAS) P_Motor-Quick`** (+ Help) — full multi-tab Faceplate XML was not in the export; Controls/Config/Interlocks/Alarms rows below also use PLC `P_Motor` research + Valve faceplate parity.

Copy FT screenshots into `docs/handoff/ft-pump-motor/` when available (`01-home.png` …).

## Tab mapping

| FT area | BH tab | Notes |
|---------|--------|-------|
| Quick / Home | Controls | Mode, Val_Sts, Start/Stop/Reset, P/I, Rdy_*, Nrdy_* |
| Maintenance | Controls + Interlocks + Configuration | Enable/bypass → Interlocks; timers → Config |
| Engineering | Configuration | Cfg_* curated rows (typed Pump Configuration like Valve) |
| Diagnostics | Controls | Not Ready Reasons |
| Alarms | Alarms + Alarm Configuration | Alm_* + Ack_* + OCmd_ResetAckAll |
| Runtime / Ovld / ResInh nav | Deferred | Nested AOI faceplates — out of scope for v1 |

## Controls (FT Quick + Diagnostics)

| FT / function | PLC | Devices path | Present (pre-plan) | Phase |
|---------------|-----|--------------|--------------------|-------|
| Mode Oper/Prog/Maint | Sts_Oper/Prog/Maint | same | Y | 1 |
| Status banner | Val_Sts | Val_Sts | Y (UI weak) | 1 |
| Start / Stop / Reset | OCmd_* | same | Y | 1 |
| Running / Stopped | Sts_Running / Sts_Stopped | Sts_Running; Sts_Stopped | Partial | 1 |
| Fail to Start sts/alm | Sts_FailToStart / Alm_FailToStart | same | Y | 1 |
| Fail to Stop | Sts_FailToStop / Alm_FailToStop | same | N | 1 |
| IO Fault | Sts_IOFault / Alm_IOFault | Alm_IOFault; Sts_IOFault | Partial | 1 |
| Intlk Trip alm | Alm_IntlkTrip | Alm_IntlkTrip | N | 1 |
| Permissive OK (P) | Inp_PermOK | PermOK | N | 1 |
| Interlock OK (I) | Inp_IntlkOK | Interlock/Sts_IntlkOK | Y (folder) | 1 |
| Bypass active | Sts_BypActive | Interlock/Sts_BypActive | Y | 1 |
| Rdy Start/Stop | Rdy_Start / Rdy_Stop | same | N | 1 |
| Rdy ResetAckAll | Rdy_ResetAckAll | same | N | 1 |
| Nrdy Disabled | Nrdy_Disabled | same | N | 1 |
| Nrdy Cfg Err | Nrdy_CfgErr | same | N | 1 |
| Nrdy Intlk | Nrdy_Intlk | same | N | 1 |
| Nrdy Perm | Nrdy_Perm | same | N | 1 |
| Nrdy IO Fault | Nrdy_IOFault | same | N | 1 |
| Nrdy Fail | Nrdy_Fail | same | N | 1 |
| Nrdy No Mode | Nrdy_NoMode | same | N | 1 |
| Runtime KPI | Val_TotRunHrs / Val_Starts | same | Y | 1 |

## Configuration (FT Engineering — curated)

| Function | PLC | Devices | Present | Phase |
|----------|-----|---------|---------|-------|
| Has run feedback | Cfg_HasRunFdbk | same | N | 2 |
| Has perm/intlk/runtime objs | Cfg_HasPermObj / HasIntlkObj / HasRunTimeObj | same | N | 2 |
| Fail to start delay | Cfg_FailToStartT | Fail_Timer_PRE (alias) | Y (rename later) | 2 |
| Fail to stop delay | Cfg_FailToStopT | same | N | 2 |
| OCmd resets fault | Cfg_OCmdResets | same | N | 2 |
| Clear Prog cmds | Cfg_PCmdClear | same | N | 2 |
| Min runtime | (not P_Motor) | Min_Runtime_Set | Removed from UI — not on FT P_Motor faceplate | — |
| Auto enable | (site) | AutoEN | Y (locked) | 2 |

## Interlocks (FT Maintenance)

| Function | PLC | Devices | Present | Phase |
|----------|-----|---------|---------|-------|
| Bypass active | Sts_BypActive | Interlock/Sts_BypActive | Y | 3 |
| Bypass cmd | OCmd_Bypass | OCmd_Bypass | N | 3 |
| Override perms/intlks | Cfg_OvrdPermIntlk | same | N | 3 |
| Override input | Inp_Ovrd | Ovrd | N | 3 |
| Enable / Disable | MCmd_Enable / MCmd_Disable | OCmd_Enable / OCmd_Disable | N | 3 |
| Disabled status | Sts_Disabled | Sts_Disabled | N | 3 |
| CondTxt / FirstOut | P_Intlk | Interlock/* | Partial | 3 |

## Alarms

| Function | PLC | Devices | Present | Phase |
|----------|-----|---------|---------|-------|
| Fail to Start | Alm_FailToStart | same | Y | 4 |
| Fail to Stop | Alm_FailToStop | same | N | 4 |
| IO Fault | Alm_IOFault | same | Y | 4 |
| Intlk Trip | Alm_IntlkTrip | same | N | 4 |
| Ack bits | Ack_* | Ack_* | N | 4 |
| Reset ack all | OCmd_ResetAckAll | OCmd_ResetAckAll | N | 4 |

## Out of scope (v1)
- Nested Runtime / Overload / Restart-Inhibit faceplates (`Cfg_HasRunTimeObj`, `Cfg_HasOvldObj`, `Cfg_HasResInhObj` nav only).
- FT Help popup; pixel-perfect RA-BAS icons.
- Hand / Ovrd as separate Modes buttons (defer unless required).

## Implementation status

| Phase | Status |
|-------|--------|
| 0 Gap doc | Done — this file |
| 1 Controls tags + UI | Done — Devices/Pump + RCP1×4 + Plant wired; Controls P/I + Nrdy + Rdy gate |
| 2 Configuration | Done — `_Assets/Pump/Configuration` (Cfg_HasRunFdbk, behavior, object nav, timers) |
| 3 Interlocks | Done — `_Assets/Pump/Interlocks` (MCmd_Enable/Disable, OCmd_Bypass, Sts_Disabled) |
| 4 Alarms | Done — `_Assets/Pump/Alarms` chips + Ack/Reset (`OCmd_ResetAckAll`) |
| 5 Verify | Scan; reopen HTLR-Pump 1 (vertical tabs) |

Naming: Pump keeps **PLC leaf names** (`OCmd_*`, `Sts_*`, `Val_Sts`) — already closer to FT than Valve’s older `OPER`/`Cmd_Open` aliases.
