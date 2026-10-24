---
title: Alarm Status And Journal
sidebar_position: 8
description: The /alarms (Alarm Status) and /alarms/journal (Alarm Journal) pages, their filters, permissions and the header alarm bell.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Alarms/**/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/AlarmNotification/view.json"
last_verified: 2026-10-23
---

# Alarm Status And Journal

Two pages built on Ignition's own alarm components, plus the alarm bell in the header.

![Alarm Status](/img/perspective/alarms.png)

| | Alarm Status | Alarm Journal |
|---|---|---|
| Route | `/alarms` | `/alarms/journal` |
| Page view | [`00_Pages/Boars Head/Alarms/Summary`](../reference/views/00-pages/boars-head/alarms/summary.md) | [`00_Pages/Boars Head/Alarms/Journal`](../reference/views/00-pages/boars-head/alarms/journal.md) |
| Table view | [`_Assets/AlarmStatusTable`](../reference/views/00-pages/boars-head/alarms/assets/alarmstatustable.md) (`ia.display.alarmstatustable`) | [`_Assets/AlarmJournalTable`](../reference/views/00-pages/boars-head/alarms/assets/alarmjournaltable.md) (`ia.display.alarmjournaltable`, journal `MSSQL`) |
| Nav | Groveport > Operations > Alarm Status | Groveport > Operations > Alarm Journal |

## Where The Alarms Come From

BH alarms are **Ignition alarms defined on UDT member values** (in the UDT definitions under
`tag-type-definition`, built by `scripts/_build_udt_alarms.py`), never on individual instances. Every device
instance inherits them. The PlantPAx devices also raise the PLC's own alarm bits through their mapped members. See
[Tags](../../tags/index.md) for the alarm definitions and associated data (Site, Area, Device, Label).

The **journal** is the gateway's database alarm journal named `MSSQL` (SQL Server `ignition` database). Without the
database connection the Journal page is empty.

## Alarm Status Page

- **Filters:** Device Type and Area multi-select dropdowns. An alarm must match both; an empty filter shows all.
  The table's `props.filters.active.conditions.source` is bound to a `sourceFilter` param, which the page builds:

```python
# Summary root/AlarmStatusTable props.params.sourceFilter  (expr-struct over the two dropdowns, script transform)
return shared.Alarms.sourceFilter(value.types, value.areas)
```

- **Colours:** active unacknowledged rows use the full priority colour, acknowledged rows a darker shade. These are
  the theme-invariant `--alarm-*` tokens, so a priority looks the same in all four themes (see
  [Themes](../styling/themes.md)).
- **Permissions:** Acknowledge needs `AlarmSummary/Acknowledge`; shelve and unshelve need `AlarmSummary/Shelve`:

```js
// AlarmStatusTable props.enableAcknowledge
coalesce({session.custom.Permissions.AlarmSummary.Acknowledge}, false)
```

- **Generate Report** opens the [Report Builder](../../features/custom-reports.md) pre-filled with the Alarms source and the
  page's Area filter.

## Alarm Journal Page

Same filter bar (Device Type, Area, Generate Report) over the journal table, which lists alarm events (active,
cleared, acknowledged) from the `MSSQL` journal.

## Header Alarm Bell

`00_Pages/00_Docked/_Assets/AlarmNotification` is the bell left of
the lock icon:

- the badge counts active alarms (acknowledged and unacknowledged) from the alarm metrics of the `[default]`
  provider root;
- it takes the highest active priority colour and flashes while anything is unacknowledged (CSS `alarm-flash`,
  stopped when animations are off);
- a click opens `/alarms`.

## Changing It

Column sets, filters and colours live in the table component props (Designer: select the table, Property Editor).
Alarm text, priority and associated data belong to the UDT alarm definitions, not to these views.
