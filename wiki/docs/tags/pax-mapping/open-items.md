---
title: Open And Parked Items
sidebar_label: Open Items
sidebar_position: 17
description: Every PAX mapping question still open, parked or waiting for a site check, with the user decisions already applied on 2026-10-23.
sources:
  - docs/pax-mapping/QUESTIONS-2026-10-23.md
  - docs/pax-mapping/16-user-answers-2026-10-23.md
last_verified: 2026-10-23
---

# Open And Parked Items

Sources: `docs/pax-mapping/QUESTIONS-2026-10-23.md` and `docs/pax-mapping/16-user-answers-2026-10-23.md`. The user
answered the question list on 2026-10-23; what was applied is summarized first, then what is still open.

## Decisions Applied (2026-10-23)

| # | Decision | Result |
|---|---|---|
| 01-3 | Remove pump `AutoEN` / `Min_Runtime_Set` | removed from `Devices/Pump` and its 11 instances, the "Auto Enable" row and 548 stand-ins |
| 01-4, N3 | Historized members polled continuously; faceplate values fast without overloading RCP1 | all 115 historized tags were already on Direct groups; `RCP1_Status` -> Leased, `PAX_Status` 1 s -> 5 s, `PAX_Faceplate` 60 s background: first values 34-48 s -> 0-5 s |
| 03-2, N1 | Underfloor: do what FT binds | Freezer = `TS_UF2`, SuperChill = `TS_UF1` |
| 04-3 | `HSS_FL_SV` is not physical | deleted from `_RCP1_` (151 tags) |
| 05-4 | `COMP[0]`, `[2]`, `[3]` unused | nothing existed to remove |
| 06-1 | 3 fan symbols, one `CG_Fans[n]` motor | already so |
| 06-2 | Forms stay as defined; CG pressure is a manual gauge entry | Fill From Live no longer maps CG suction pressure (109 -> 90 live entries) |
| 06-4, 07-4 | Bleed valve from `CG.Cfg_HasBleedValve` | CG page and faceplate follow the PLC flag (`PAX_Config` group) |
| 08-1 | Interlocks tab only where the interlock object has real conditions | `ShowInterlocks` rule; hidden on the 7 condenser motors and the 2 make-up valves |
| 09-2, 10-2, N2 | Gate our alarms on the PLC alarm enables | P_AIn and P_DIn alarms gated on `Cfg_Has*Alm`; active Groveport alarms 13 -> 3 |
| 10-1 | Map `MR_EEF1` / `MR_EEF2` only if they work | not mapped (no routine, `EnableIn` 0) |
| 11-1 | LTU count reset: later | Reset Count hidden; the reset to wire is `HMI_Ltu_Clear` |
| 13-1, 13-2 | Hide HSS enable; 2 LSS positions | already so |
| 13-4, N4 | Fix the HSD CSV-LEVEL line | done |
| 14-1 | Keep Reset / Silence, wired as FT | reference the lock-governed `_RCP1_` `ALARM.HMI_Reset` / `HMI_Silence`; refused with the alert while locked |
| 14-2 | MR AD / VL AD lamps exactly as FT | done: blink red / yellow in alarm (`status-dot-blink`) |
| 14-3 | Delete the legacy UnderfloorTemp memory tags | deleted |
| 14-4 | Production / FCM out of scope | unreachable in local mode, unchanged |
| C1, C2 | Delete `Units/Machine Room`; remove the exhaust fan `Airflow` field | done |
| /sensors | Fix "null.00" | PlantPAx 1.5e38 no-limit sentinel -> gray dash; PSIG units |
| Pump MODE | Fix the gray dash | the shared Modes asset reads the device's own part |
| CG zone temp | Confirm Too Hot / Too Cold; red value | real PLC bits; ZAT red while set; they no longer alarm |

## Still Open

| Item | What is needed | Page |
|---|---|---|
| `HTR_PUMPS[1].Cfg_Tag` = "HTRL-PUMP #3" (label "#1") | PLC typo: tell the controls engineer | [Recirc Pumps](recirc-pumps.md) |
| `CD1A_FAN1` / `CD1A_FAN2` labels swapped in the PLC | controls engineer | [Condenser Pumps And Fans](condenser-pumps-fans.md) |
| `PS[33]` label duplicates PS32 ("HTR-VESSEL-2") | controls engineer | [Discrete Inputs](discrete-inputs.md) |
| `TS_UF1` / `TS_UF2`: L5X descriptions vs PLC labels / FT bindings | confirm on site which slab each transmitter is in | [Sensors](sensors.md) |
| Underfloor temps read -40 °F (raw 0, Under Range) | check the sensors and wiring (rack Slot 4 Ch1 / Ch2) | [Sensors](sensors.md) |
| FD-01 FREEZER shows FIRE ALM (FT and ours) | check the detector on site | [Discrete Inputs](discrete-inputs.md) |
| LTU count reset | wire `HMI_Ltu_Clear` when PLC writes are allowed | [LTU](ltu.md) |
| Compressor labels "COMP #n" | label-only rename if wanted | [Compressors](compressors.md) |
| Valve instance names vs FT labels | rename only with a history / OOS migration | [Valves](valves.md) |
| RCP1 driver `cipConnectionSize` 500 -> 4000 | done (4000 now); `concurrentRequests` 2 -> 4 only if needed | [History And Polling](../history.md) |
| `/plc-rack` "Modules Faulted" showed "No Data" once; last major fault code | rack follow-up | [PLC Rack UDTs](../udts/plc-rack.md) |
| Nested CG valves enable an `Intlk` part with no tag | harmless; clean up on the instance | [CG Valves](cg-valves.md) |
| Retire `_RCP1_` (down to diagnostics + rack I/O + PAR-only objects) | later; first repoint the SAFETYS references | [Machine Room SAFETYS](machine-room-safetys.md) |
| Production / FCM KPI data source | unknown (another PLC / MES?); blocked | [Machine Room SAFETYS](machine-room-safetys.md#not-mapped-nothing-to-map) |

## Parked (By Design)

- **PLC writes**: every command stays disabled until the user tests and lifts the [PLC Write Lock](../plc-write-lock.md).
- **Leased first-value delay**: faceplate-only values can take a few seconds (up to a minute on a slow link); the gray
  placeholder covers it.
