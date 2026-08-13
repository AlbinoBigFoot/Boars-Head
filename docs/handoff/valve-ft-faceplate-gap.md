# Valve (P_ValveSO) FT → BH Faceplate Gap Matrix

Reference for Main Liq SV / Solenoid Operated Valve faceplate.
FT screenshots were provided in chat (Home, Maintenance, Engineering 1–2, Diagnostics, Alarms).
Copy into `docs/handoff/ft-valve-so/` when available (`01-home.png` … `06-alarms.png`).

## Tab mapping

| FT tab | BH tab | Notes |
|--------|--------|-------|
| Home | Controls | Mode, Val_Sts banner, Open/Close/Reset, P/I |
| Maintenance | Controls + Interlocks + Configuration | Mode/enable → Controls; bypass → Interlocks; timers → Config |
| Engineering 1–2 | Configuration | Cfg_* curated rows |
| Diagnostics | Controls | Not Ready Reasons (`Nrdy_*`) |
| Alarms | Alarms + Alarm Configuration | Alm_* + Ack_* |

## Controls (FT Home + Diagnostics)

| FT / function | PLC | Devices path | Present (pre-plan) | Phase |
|---------------|-----|--------------|--------------------|-------|
| Mode Oper/Prog/Maint | Sts_Oper/Prog/Maint | OPER, PROG, MAINT | Y | 1 |
| Status banner Open/Closed/… | Val_Sts | Status | Y (UI weak) | 1 |
| Open / Close / Reset | OCmd_* | Cmd_Open, Cmd_Close, Cmd_Reset | Y | 1 |
| Open/Closed LS | Inp_*LS | OpenLS, ClosedLS | Y | 1 |
| Failed / Comm | Sts_FullStall / Sts_IOFault | Failed, Comm | Y | 1 |
| Permissive OK (P) | Inp_PermOK | PermOK | N | 1 |
| Interlock OK (I) | Inp_IntlkOK | Interlock/Sts_IntlkOK | Y (folder) | 1 |
| Rdy Open/Close | Rdy_Open / Rdy_Close | Rdy_Open, Rdy_Close | N | 1 |
| Nrdy Disabled | Nrdy_Disabled | Nrdy_Disabled | N | 1 |
| Nrdy Cfg Err | Nrdy_CfgErr | Nrdy_CfgErr | N | 1 |
| Nrdy Intlk | Nrdy_Intlk | Nrdy_Intlk | N | 1 |
| Nrdy Perm | Nrdy_Perm | Nrdy_Perm | N | 1 |
| Nrdy IO Fault | Nrdy_IOFault | Nrdy_IOFault | N | 1 |
| Nrdy Fail | Nrdy_Fail | Nrdy_Fail | N | 1 |
| Nrdy No Mode | Nrdy_NoMode | Nrdy_NoMode | N | 1 |

## Configuration (FT Engineering)

| Function | PLC | Devices | Present | Phase |
|----------|-----|---------|---------|-------|
| Has Closed LS | Cfg_HasClosedLS | Cfg_HasClosedLS | N | 2 |
| Has Open LS | Cfg_HasOpenLS | Cfg_HasOpenLS | N | 2 |
| Fault when both LS | Cfg_LSFail | Cfg_LSFail | N | 2 |
| Fail Open | Cfg_FailOpen | Cfg_FailOpen | N | 2 |
| Clear Prog cmds | Cfg_PCmdClear | Cfg_PCmdClear | N | 2 |
| Oper cmd resets fault | Cfg_OCmdResets | Cfg_OCmdResets | N | 2 |
| Nav to Perm/Intlk/Stats | Cfg_HasPermObj / HasIntlkObj / HasStatsObj | same | N | 2 |
| Shed on IO/Transit/Full | Cfg_ShedOn* | same | N | 2 |
| Transit stall T | Cfg_TransitStallT | TravelTime | Y | 2 |
| Full stall T | Cfg_FullStallT | Cfg_FullStallT | N | 2 |
| Sim feedback delay | Cfg_SimFdbkT | Cfg_SimFdbkT | N | 2 |

## Interlocks (FT Maintenance)

| Function | PLC | Devices | Present | Phase |
|----------|-----|---------|---------|-------|
| Bypass active | Sts_BypActive | Interlock/Sts_BypActive | Y | 3 |
| Bypass cmd | OCmd_Bypass | Cmd_Bypass | N | 3 |
| Override perms/intlks | Cfg_OvrdPermIntlk | Cfg_OvrdPermIntlk | N | 3 |
| Override input | Inp_Ovrd | Ovrd | N | 3 |
| Enable / Disable | MCmd_Enable / MCmd_Disable | Cmd_Enable / Cmd_Disable | N | 3 |
| Disabled status | Sts_Disabled | Disabled | N | 3 |
| CondTxt / FirstOut | P_Intlk / CondTxt | Interlock/* | Partial | 3 |

## Alarms

| Function | PLC | Devices | Present | Phase |
|----------|-----|---------|---------|-------|
| IO Fault | Alm_IOFault | Alm_IOFault | Y | 4 |
| Full Stall | Alm_FullStall | Alm_FullStall | Y | 4 |
| Transit Stall | Alm_TransitStall | Alm_TransitStall | Y | 4 |
| Intlk Trip | Alm_IntlkTrip | Alm_IntlkTrip | Y | 4 |
| Ack bits | Ack_* | Ack_* | N | 4 |
| Reset ack all | OCmd_ResetAckAll | Cmd_ResetAckAll | N | 4 |

## Out of scope
- FT Help popup, Valve Stats deep navigation, pixel-perfect FT icons.
- Hand / Ovrd as separate Modes buttons (defer unless required).

## Implementation status (Aug 2026)

| Phase | Status |
|-------|--------|
| 0 Gap doc | Done — this file |
| 1 Controls tags + UI | Done — Status banner, P/I, Nrdy list, Rdy gating |
| 2 Configuration | Done — `_Assets/Valve/Configuration` curated Cfg_* |
| 3 Interlocks | Done — `_Assets/Valve/Interlocks` enable/bypass + shared channels |
| 4 Alarms | Done — `_Assets/Valve/Alarms` chips + Ack/Reset + shared table |
| 5 Verify | Scan config/projects; reopen Main Liq SV with Simulate ON |

Devices/Valve expanded (~56 members). RCP1/Main Liq SV rebuilt as compact OPC AtomicTags (~52). Units + Plant Valves `sourceTagPath` wired.
