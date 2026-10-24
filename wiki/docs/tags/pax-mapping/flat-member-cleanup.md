---
title: Flat-Member Cleanup (End State)
sidebar_label: 15 Flat-Member Cleanup
sidebar_position: 16
description: What the 2026-10-23 cleanup removed from the device UDTs (flat stand-in members, the _Pax flag, old alarms), what stayed, the bindings changed, rollback and verification.
sources:
  - docs/pax-mapping/15-flat-member-cleanup.md
last_verified: 2026-10-23
---

# Flat-Member Cleanup (End State)

Source doc: `docs/pax-mapping/15-flat-member-cleanup.md`. Done 2026-10-23.

## Why There Were Flat Members

During the device-by-device mapping (pages 01-14), each device UDT carried two copies of every field:

- the **flat** HMI members (`Sts_Running/Value`, `Level/Value` ...), memory stand-ins that referenced placeholder
  tags under `Boars_Head/GrovePort/PLC/RCP1/**`, so unmapped devices kept working;
- the **nested** PLC parts (`Motor/Sts_Running`), enabled on mapped devices;
- a `_Pax` flag on the instance (`Motor`, `Tank`, `AIn` ...) and views with
  `if(coalesce({view.custom.pax}, '') = 'Motor', '/Motor/Sts_Running', '/Sts_Running/Value')` switches (835 on the
  pump views alone).

Once every type was mapped, the transition design was removed type by type.

## What Was Removed / Kept

| Devices type | Removed (flat members) | Kept: PLC | Kept: owned | Hidden (no PLC source) |
|---|---|---|---|---|
| `Pump` | 77 + `_Pax` | `Motor`, `Intlk`, `RunTime` | `_Alarms` (`AutoEN`, `Min_Runtime_Set` removed later the same day) | - |
| `Tank` | 16 + `_Pax` | `LvlAIn`, `PressAIn`, the four `*DIn`, `Pump1Alm`, `Pump2Alm`, `StartPress`, `LeadPump` | `Interlock`, `_Alarms` | HPR `PressAIn` (pressure tile hidden) |
| `Sensor` | 43 + `_Pax` | `AIn`, `AInRef` | `_Alarms` | - |
| `Valve` | 58 + `_Pax` | `Valve` (later also `Intlk`) | `Cmd_Position`, `_Alarms`, `valveType` | the 6 Bleed SV of the 3-valve CGs |
| `Compressor` | 25 + `_Pax` | `Comp`, `Intlk` | `Cfg_WebGuiUrl`, `_Alarms` | tile FLA / SVP setpoint coloring |
| `Evaporator` | 39 + `_Pax` (incl. the `Fan 1..3` sub-devices) | `CG`, `ZAT`, `Intlk`, `Fans`, `FansRunTime` | `SummaryInstances`, `Valves`, `_Alarms`, `HmiStatus` | CG `Pressure` (faceplate row hidden; Daily Rounds = manual gauge entry), fan speed |
| `DiscreteInput` | 18 + `_Pax` | `DIn` | - | - |
| `ExhaustFan` | 4 + `_Pax` | `DIn`, `FailToStart` | `_Alarms` | - |
| `LTU` | 4 + `_Pax` | `PlcCount`, `PlcCountAlarm`, `PlcCountAlarmSP` | `Input`, `ResetDaily`, `ResetTime`, `_Alarms` | Reset Count button |
| `SafetyRelay` | 32 + `_Pax` | `IO`, `PlcMajorFault`, `PlcResetAlm` | `_Alarms` | - |
| `SuctionSequence` | 15 + `_Pax` | `Seq`, `PlcHmiEnable` | `Cfg_HasEnable`, `Cfg_Notes`, `Cfg_Positions`, `Cfg_SensorLabel`, `Cfg_SensorPath` | HSS enable |
| `DischargeSequence` | 23 + `_Pax` | `Seqr`, `PlcSequence1..7`, `PlcFixedSP`, `PlcFirstNoDelay`, `PlcMain/BackupOpen/CloseSP` | `Cfg_LevelLabel`, `Cfg_LevelPath`, `Cfg_SensorLabel`, `Cfg_SensorPath` | - |

No placeholder values were invented: a field with no PLC source became a named HMI-owned member or was hidden.

Also removed: the `PLC/RCP1` memory stand-ins (1,719 unreferenced on 2026-10-23, the rest with the user answers the
same day, so none is left), the stale AdhocTrend tree cache, and the temporary `_paxRead` WebDev probe. The old
flat-member alarms were removed with the flat members; alarms now sit on the PLC library members
([Alarms](../alarms.md)).

## How The Views Work Now

- **Device-specific views** read the PLC member directly (`/Motor/Sts_Running`).
- **Shared views** (Modes, IconHeader, Trend, InterlockPanel, Sensor AIn / AInRef) keep a switch **between PLC
  parts** only, keyed by the part key computed from the instance (`.TypeId` + which part is enabled), not a
  nested-vs-flat switch.
- Don't reintroduce an `if(key = 'K', '<PLC member>', '<flat member>')` chain: bind directly to the PLC member.
- `shared.Pax` keeps `FIELDS` / `member()` / `resolve()` / `livePath()` for names that are not member paths (Details
  table columns, ConfigSection rows, `shared.ValveCommands`, Daily Rounds live values).
- The mapping is final: the flat members are gone and the PLC part members are the only source.

## Bindings Changed (Summary)

| Type | Where |
|---|---|
| Pump | pump faceplate (Controls / Alarms / Interlocks / Trend), pump cards on the Tank Overview, condenser fans, Details columns, `shared.ValveCommands._resolve` |
| Tank | Tank Overview faceplate + tile, DI tab title, Daily Rounds tank fields |
| Sensor | sensor faceplate, sequence popup sensor links, Machine Room HSD arrow, Utility Overview underfloor tiles, Daily Rounds |
| Valve | valve faceplate, valve tiles, condenser valves, CG valve rows |
| Compressor | compressor tile + faceplate (`Comp/*`, `Intlk/*`), tile SP coloring dropped |
| Evaporator | CG pages, CG tiles, `OverviewKpis`, 12 h history, evaporator faceplate, InterlockPanel / InterlockButton |
| DiscreteInput | DI faceplate and `OverviewStatusTile` |
| ExhaustFan, LTU, SafetyRelay, sequences | their components and popups |

## Rollback

The earlier design (flat members and `_Pax` switches) is in git history before the cleanup commit. The removal is
not meant to be undone; to look at the old version use `git log` / `git show` on the UDT definition files.

## Verification

After each type and at the end the device pages and faceplates were checked in a Perspective session: 0 binding error
overlays, 0 console errors, 0 "null" texts on
`/machine-room`, `/condensers`, `/plants/groveport/utility-overview`, `/compressors`, `/tanks`, `/valves`,
`/condensers/valves`, `/rupture-disks`, `/safety-relay`, `/exhaust-fans`, `/cg-f2`, `/cg-c1`, `/sensors`, `/pumps`,
`/operations/forms/daily-rounds`. A search for `_Pax` over the project and the tag tree finds 0 hits.

## Intentional Leftovers

- Production FCM `Status` (FCM line tags, not a device type) and `CoolingTower` (not PLC-mapped).
- `_Assets/Interlocks` reads the tank's HMI-owned `Interlock` folder.
- `shared.ValveCommands` legacy field names (resolved through `livePath`; every PLC write is refused).
