---
title: Alarms
sidebar_position: 9
description: Alarm Status, Alarm Journal, the header bell, faceplate Alarms / Alarm Configuration tabs, ack and shelving, and the CG zone-temperature alarms - where alarms are defined and how to change them.
sources:
  - docs/central-alarming.md
  - docs/pax-mapping/06-evaporators.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py
  - gateways/standard/data/projects/BH/ignition/script-python/shared/AlarmConfig/code.py
  - gateways/standard/data/config/resources/core/ignition/alarm-journal/**/config.json
last_verified: 2026-10-23
---

# Alarms

## What it does

The HMI uses **Ignition alarms** (alarms configured on tags, evaluated by the gateway) for every device. Operators
see them in four places:

| Where | What |
|---|---|
| **Alarm Status** (Operations > Alarm Status, `/alarms`, view `00_Pages/Boars Head/Alarms/Summary`) | live alarms in a built-in Alarm Status Table, coloured by priority, filterable by **Device Type** and **Area** (multi-select), with Site / Area / Device columns; ack and shelve |
| **Alarm Journal** (Operations > Alarm Journal, `/alarms/journal`, view `.../Alarms/Journal`) | history from the journal profile `MSSQL`, same filters; **Generate Report** opens the [Report Builder](./custom-reports.md) |
| **Header bell** | the count of active / unacknowledged alarms (Scout AlarmNotification style) |
| **Device components and faceplates** | numbered alarm badges on device tiles (`alarm-indicators`), a faceplate **Alarms** tab (active alarms of that device, priority colours, Ack / Reset) and an **Alarm Configuration** tab (priorities, limits) |

![Alarm Status (2026-10-23): the RCP1 Communication Lost alarm is active because the SecureLink is down](/img/features/alarms/alarms-page.png)

Row colours (stylesheet tokens): Critical `#E22028`, High `#EC8629`, Medium `#F5E11B`, Low `#916AAD`; an
acknowledged active alarm uses the darker `-ack` shade; cleared rows are neutral.

## How to use it (operators)

- **Acknowledge**: select rows in Alarm Status and Ack, or use Ack / Reset on the faceplate Alarms tab. Needs
  `AlarmSummary/Acknowledge` (Maintenance and up).
- **Shelve**: from the Alarm Status table's shelve action (temporarily hide a nuisance alarm); needs
  `AlarmSummary/Shelve`. Shelved events are stored in the journal.
- **Filter**: Device Type (Evaporators, Compressors, Pumps, ExhaustFans, CoolingTowers) and Area (Freezer,
  SuperChill, Club, Palletizing, East PH, West PH, Dock, Machine Room). An alarm must match both; empty = all.
- **Change a limit or priority**: device faceplate > Alarm Configuration tab (Engineering and up edit, Maintenance
  sees it read only). Every change is audited (`alarm config`).

## Where alarms are defined (developers)

**Alarms live on UDT definitions, never on instances.** They are configured on the
members of the PLC library types (since the 2026-10-23 PAX cleanup every device alarm sits on its PlantPAx member):

| Library type | Alarms |
|---|---|
| `PLC/P_Motor` | IO fault, fail to start / stop, interlock trip ... (`Alm_*`) |
| `PLC/P_AIn` | `Sts_HiHi`, `Sts_Hi`, `Sts_Lo`, `Sts_LoLo`, `Sts_Fail` |
| `PLC/P_DIn` | `Sts_TgtDisagree` + the state alarm (AlarmOnSts) |
| `PLC/P_ValveSO`, `Screw_Compressor`, `CG_RL_Evap`, `CR30_Input` | the controller's own alarm bits |
| device atomics | for example LTU Transfer Count High |

Each alarm is **gated by the PLC object's own alarm enable** (`enabled` = `coalesce({[.]<enable member>}, false)`),
so the HMI alarms exactly when the controller says the alarm exists. Associated data `Site`, `Area`, `Device` is
added so the tables and the journal can show and filter them.

### CG zone temperature alarms

The CG zone-temperature alarms now come **only from the ZAT `P_AIn` alarms** (Hi, HiHi, Lo, LoLo) of each
evaporator, gated on the PLC's own alarm enables. **Too Hot / Too Cold no longer alarm**, but they still turn the
zone temperature red on the CG tiles and pages (`value-alarm` class) while the PLC bit `CG/TooHot` / `CG/TooCold` is
set (L5X `CG_Control`: TooHot when ZAT is at least setpoint + 3, held while ZAT is above the setpoint; TooCold when
ZAT is at most setpoint - 3, held while below the setpoint). To change the CG alarm limits edit the ZAT alarms on the
`PLC/P_AIn` definition or the device's Alarm Configuration tab.

### Other pieces

| Piece | Where |
|---|---|
| Tables | `00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable`, `AlarmJournalTable` (param `sourceFilter`) |
| Filters | `shared.Alarms.sourceFilter` / `deviceTypeSourceFilter` (wildcard source conditions) |
| Faceplate Alarm Configuration | `shared.AlarmConfig.listAlarms` / `applyOverride` (gated by `AlarmConfiguration/Edit`) |
| Journal | profile `MSSQL`, tables `alarm_events` / `alarm_event_data` (see [Ignition Tables](../database/ignition-tables.md)) |
| Permissions | `AlarmSummary/Acknowledge`, `AlarmSummary/Shelve`, `AlarmConfiguration/Edit` |

## How To Change It

**Add or change an alarm (Designer):**
1. Tag Browser > **UDT Definitions** tab > `PLC` > the library type (for example `P_AIn`, `P_Motor`).
2. Select the member that carries the alarm (for example `Sts_Hi`) and open it in the tag editor.
3. In the **Alarming** section add or edit the alarm: name, mode, setpoint, priority, display path and the `enabled`
   expression (gate it on the PLC object's own enable, for example `coalesce({[.]Cfg_HasHiAlm}, false)`).
4. Add the associated data `Site`, `Area`, `Device` so the tables and the journal can filter it.
5. Click **OK**, then save the project. Instances follow the definition; check one device's Alarm Status row.

**Change a limit on one device:** open its faceplate > Alarm Configuration tab (Engineering and up).

**Change a table or filter (Designer):** Project Browser > Perspective > Views > `00_Pages/Boars Head/Alarms/_Assets` >
`AlarmStatusTable` or `AlarmJournalTable`; edit the `sourceFilter` param, or the filter functions in the
`shared.Alarms` script module (Project Browser > Scripting > Project Library > `shared` > `Alarms`).

**Rules:**
- Do not create a second journal profile; the views expect `MSSQL`.
- Never put alarms on instances (they differ per device and would be lost when the UDT definition is updated).
- Save, then test in a Perspective session: trigger the condition or read the alarm in Status > Alarms on the Gateway
  web UI.

## Known limitations and parked items

- Alarm row blink for unacknowledged alarms is not built.
- The journal prunes at 1 year (Services > Alarming > Journals > `MSSQL`); it grows about 400,000 events a month.
- Ack / shelve inside the built-in alarm table component is gated by props bound to the matrix, not re-checked on
  the gateway.
