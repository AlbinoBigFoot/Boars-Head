---
title: Alarming
sidebar_position: 7
description: The MSSQL alarm journal, general alarm settings, and where alarms are defined and shown.
sources:
  - gateways/standard/data/config/resources/core/ignition/alarm-journal/MSSQL/config.json
  - gateways/standard/data/config/resources/core/ignition/general-alarm-settings/config.json
  - gateways/standard/data/config/resources/core/ignition/schedule/Example/config.json
  - docs/central-alarming.md
last_verified: 2026-10-23
---

# Alarming

Alarms in Ignition are defined **on tags** (here on UDT member definitions, never on instances) and evaluated by the
gateway. The gateway side has three parts: general settings, the journal, and (unused here) notification pipelines.

## General Alarm Settings

**Where:** Services > Alarming > Settings (`ignition/general-alarm-settings/config.json`).

| Setting | Value | Meaning |
|---|---|---|
| Startup suppression time | 10 s | Alarms that become active in the first 10 s after startup don't notify |
| Live event limit | 5 | Events kept in memory per alarm |
| Notify initial events | off | |

## Alarm Journal `MSSQL`

**Where:** Services > Alarming > Journals > `MSSQL` (`ignition/alarm-journal/MSSQL/config.json`).

| Setting | Value |
|---|---|
| Type | Database (`DATASOURCE`), datasource `ignition` |
| Tables | `alarm_events` (one row per event: active, clear, ack) and `alarm_event_data` (its properties) |
| Store and Forward | on |
| Minimum priority | `Diagnostic` (everything is journaled) |
| Stores shelved events, enabled-change events | yes, yes |
| Event data stored | dynamic config, static and dynamic associated data (not static config) |
| Query only | no |
| Pruning | **on, 1 year** |

The journal had about 1.1 million events and 3.6 million data rows on 2026-10-23. Events older than 1 year are
pruned. To change the retention, open Services > Alarming > Journals > `MSSQL` and edit the pruning age.

**Who reads it:** the Alarm Journal page (`/alarms/journal`), the Report Builder Alarms source (named query
`Reports/Alarms`), and the Alarm History of faceplates.

## Pipelines, Notification, Rosters, Schedules

- **Pipelines / Notification / Rosters:** none configured. The Alarm Notification, SMS and Voice modules are
  installed but unused; the HMI only shows alarms on screen.
- **Schedules:** only the stock `Example` schedule (weekdays 8:00 to 11:45, 12:30 to 17:00), unused.

## Where Alarms Are Defined And Shown

| What | Where |
|---|---|
| Alarm definitions | UDT member Values in `tag-type-definition/**` (e.g. PlantPAx `P_AIn` HiHi/Hi/Lo/LoLo, `P_Motor` fail, `P_DIn` state). Edit them in the Designer UDT editor, never on instances (see [Tags: Alarms](../tags/alarms.md)) |
| Alarm enables | PLC configuration bits (`Cfg_Has*Alm`) in the `PAX_Config` tag group gate the library alarms |
| Alarm Status page | `/alarms` (Alarm Status Table, Device Type filter, priority row colours) |
| Header bell | Active alarm count, links to `/alarms` |
| Faceplate Alarms tab | Per device, with Ack / Shelve gated by the permission matrix |

Full write-up: [Features](../features/index.md) and [Tags](../tags/index.md).
