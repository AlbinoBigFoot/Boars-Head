---
title: Sensors (Pressures, Outside Air, Underfloor)
sidebar_label: 03 Sensors
sidebar_position: 4
description: The nine sensor devices mapped to P_AIn objects (SYS_PT1-5, TS_AIR, TS_UF1/2) or a read-only reference, including the underfloor swap decision.
sources:
  - docs/pax-mapping/03-sensors.md
last_verified: 2026-10-23
---

# Sensors

Source doc: `docs/pax-mapping/03-sensors.md`. Type: [Devices/Sensor](../reference/udts/devices/sensor.md); instances:
[Machine Room / Sensors](../reference/devices/machine-room-sensors.md),
[Condensers / Sensors](../reference/devices/condensers-sensors.md),
[Freezer / Sensors](../reference/devices/freezer-sensors.md), [SuperChill / Sensors](../reference/devices/superchill-sensors.md).

## Devices And PLC Objects

| HMI device | PLC object | Part | FT label | Unit |
|---|---|---|---|---|
| `Machine Room/Sensors/LSS-Pumps Pressure` | `SYS_PT1` | `AIn` (owner) | LSS-PT1 | PSIG |
| `Machine Room/Sensors/HSS-Pumps Pressure` | `SYS_PT2` | `AIn` (owner) | HSS-PT2 | PSIG |
| `Machine Room/Sensors/HSD-Discharge Pressure` | `SYS_PT3` | `AIn` (owner) | HSD-PT3 | PSIG |
| `Machine Room/Sensors/LSL-Pumps Pressure` | `SYS_PT4` | `AIn` (owner) | LSL-PUMPS PRESSURE | PSIG |
| `Machine Room/Sensors/HSL-Pumps Pressure` | `SYS_PT5` | `AIn` (owner) | HSL-PUMPS PRESSURE | PSIG |
| `Machine Room/Sensors/Condenser Sump Level` | `LT_CSV` | **`AInRef`** -> `Condensers/Tanks/CSV/LvlAIn` | CSV-LEVEL | In" |
| `Condensers/Sensors/Outside Air Temp` | `TS_AIR` | `AIn` (owner) | OUTSIDE AIR | °F |
| `Freezer/Sensors/Underfloor Temp` | **`TS_UF2`** | `AIn` (owner) | FREEZER UND.FLOOR | °F |
| `SuperChill/Sensors/Underfloor Temp` | **`TS_UF1`** | `AIn` (owner) | SUPERCHILL UND.FLOOR | °F |

Parameters: `PlcDevice`, `AInTag` (owner object), `AInSource` (reference path), `AInEU` (unit; PSIG on every
pressure, from the PLC / FT text). The part key a shared view uses is `AIn` or `AInRef`, whichever part is enabled.

![Sensors page, live](/img/tags/sensors-page.png)

## What The Faceplate Shows

| On the HMI | Member it reads | PLC tag (HSS-PT2) |
|---|---|---|
| Value with unit | `AIn/Val` (unit from `EngUnit` = `AInEU`) | `SYS_PT2.Val` |
| Status OK / LO / HI / LOLO / HIHI / FAIL / CFGERR | `AIn/Val_Fault` | `SYS_PT2.Val_Fault` |
| Alarm flags | `AIn/Sts_HiHi`, `Sts_Hi`, `Sts_Lo`, `Sts_LoLo`, `Sts_Fail` | `SYS_PT2.Sts_*` |
| Alarm limits (table and trend lines) | `AIn/Val_HiHiLim`, `Val_HiLim`, `Val_LoLim`, `Val_LoLoLim` (Leased; 1.5e38 = no limit, shown as a dash) | `SYS_PT2.Val_*Lim` |
| Raw input, scaling | `AIn/Val_InpPV`, `Cfg_InpRawMin` / `Max`, `Cfg_PVEUMin` / `Max` | |
| Mode, lock | `AIn/Sts_Oper`, `Sts_Prog`, `Sts_Maint`, `AIn/Mode/Sts_ProgOperLock` | |
| Labels | `AIn/Cfg_Label`, `Cfg_Tag`, `Cfg_Desc` | "HSS-PT2" |
| Trend default pen | `AIn/Val` (historized) | |

For the `AInRef` sensor the same members are read under `AInRef/` (they mirror the CSV tank's `LvlAIn`).

Field map (43 fields per sensor, all mapped; the old member name is the `shared.Pax.FIELDS` key):

| Field (old member) | Reads now |
|---|---|
| `Value` | `AIn/Val` |
| `HiHi` / `Hi` / `Lo` / `LoLo` / `Fail` | `AIn/Sts_HiHi` / `Sts_Hi` / `Sts_Lo` / `Sts_LoLo` / `Sts_Fail` |
| `HiHiLim` / `HiLim` / `LoLim` / `LoLoLim` | `AIn/Val_HiHiLim` / `Val_HiLim` / `Val_LoLim` / `Val_LoLoLim` |
| `Status` | `AIn/Val_Fault` |
| `Val_InpPV` | `AIn/Val_InpPV` |
| `Cmd_Reset` | `AIn/OCmd_Reset` |
| `OCmd_Lock` / `OCmd_Oper` | `AIn/Mode/OCmd_AcqLock` |
| `OCmd_Unlock` / `OCmd_Prog` | `AIn/Mode/OCmd_UnlockRel` |
| `Sts_OperLocked` | `AIn/Mode/Sts_ProgOperLock` |
| `Cfg_ProgDefault` | `AIn/Mode/Cfg_ProgDefault` |
| `Sts_Oper` / `Sts_Prog` / `Sts_Maint` / `Sts_NoMode` | same names under `AIn/` |
| every `Cfg_*` (`Cfg_EU`, `Cfg_PVEUMin`, `Cfg_InpRawMax`, `Cfg_HiDB`, `Cfg_FiltTC`, `Cfg_Label` ...) | same name under `AIn/` |

(`AInRef/` instead of `AIn/` on the Condenser Sump Level sensor.)

## Decisions And Evidence

1. **One owner per controller object.** `SYS_PT1` / `SYS_PT2` are owned by the sensors and referenced by the LTR / HTR
   tanks (`PressAIn`); `LT_CSV` is owned by the CSV tank and referenced by `Condenser Sump Level`. So the Condenser
   Sump Level alarms come only from the tank.
2. **Underfloor temperatures: what FT binds wins.** FT's Plant Overview `(STELLAR)DashBoard.gfx` (binary, read as
   bytes) binds the upper tile FREEZER UND.FLOOR (between CG-C1 and CG-B1) to `TS_UF2` and the lower tile SUPERCHILL
   UND.FLOOR (between CG-A1 and CG-D1) to `TS_UF1`, and the live `Cfg_Label`s agree (`TS_UF1` = SUPERCHILL). The L5X
   tag **descriptions** say the opposite. The user decided "do what is bound in the FT export": Freezer = `TS_UF2`,
   SuperChill = `TS_UF1` (applied 2026-10-23, the N1 swap). History recorded under each device path before the swap
   came from the other transmitter (both read -40 °F, so no visible difference).
3. **The tile positions** on the Utility Overview were swapped against FT and were fixed .
4. **`LSS_PT` and `Sump_pT`** are P_AIn objects in the PLC with no FT display: `LSS_PT` is a live, configured
   transmitter ("NH3-LSS-PT", Low-Stage Suction Pressure, 48.7 psig), `Sump_pT` is unconfigured. Both left out.
5. **"null.00" on `/sensors`**: PlantPAx writes +/-1.5e38 into an unused limit; the table formatted it into a 39-digit
   string. Any value of 1e30 or more is now "no value" (gray dash, no unit).

## Alarms

The P_AIn library alarms on the owner parts, each enabled only while the PLC object's matching `Cfg_Has*Alm` is on:
Input Failure (High), High-High (High), High (Medium), Low (Medium), Low-Low (High). `SYS_PT1` has no alarms
configured in the PLC, so none fire for it. Reference parts have no alarms.

## Live Check (2026-10-23)

- SYS_PT1 32.2, SYS_PT2 33.4, SYS_PT3 144.3, SYS_PT4 33.7, SYS_PT5 93.0 psig; TS_AIR 54.3 °F; labels as FT.
- `TS_UF1` / `TS_UF2` read -40.0 °F = `Cfg_PVEUMin` with raw input 0 and `Sts_PVBad` 0: the bottom of range, a failed
  or unwired input that the PLC does not flag. Matches the FT photo (-40.00 on both).

## Open Items

- **Underfloor -40 °F**: check the sensors / wiring on site (rack Slot 4 Ch1 / Ch2 read Under Range); their P_AIn
  scaling (0-10000) is wider than the 0-5 V channel range.
- **TS_UF1 / TS_UF2 conflict**: L5X descriptions vs PLC labels / FT bindings; confirm on site which slab each
  transmitter is in.
- `/sensors` limit columns for `SYS_PT1`: no alarms configured in the PLC, the limits show dashes.
