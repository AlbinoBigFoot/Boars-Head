---
title: Ignition Tables
sidebar_position: 3
description: Tables that Ignition itself creates in the `ignition` database - the tag historian (sqlth_* / sqlt_data_*), the alarm journal and the audit profiles - with example read-only queries.
sources:
  - gateways/standard/data/config/resources/core/ignition/alarm-journal/**/config.json
  - gateways/standard/data/config/resources/core/ignition/audit-profile/**/config.json
  - gateways/standard/data/config/resources/core/ignition/security-properties/config.json
  - gateways/standard/data/config/resources/core/com.inductiveautomation.historian/**/config.json
last_verified: 2026-10-23
---

# Ignition Tables

These tables are created and written by Ignition subsystems. Do not change their schema; query them read-only, and
prefer the Ignition APIs (`system.tag.queryTagHistory`, the Alarm Journal component, the audit named query) over
raw SQL in the HMI.

## Tag historian (SQL Historian provider `historian`)

Gateway web UI: **Config > Tags > History** (8.3: **Services > Historians**). Config file
`config/resources/core/com.inductiveautomation.historian/historian-provider/historian/config.json`.

| Setting | Value |
|---|---|
| Type | SQL Historian on database `ignition` |
| Partitions | monthly (`size 1 MONTH`), not "optimized" |
| Pruning | **on, 2 years** |
| Stale multiplier | 2; scan-class execution tracking on |

| Table | Holds |
|---|---|
| `sqlth_te` | one row per historized tag path and data type: `id`, `tagpath` (lower-case, without provider), `scid`, `datatype`, `querymode`, `created`, `retired` (epoch ms; NULL = live). 18,792 rows, 1,908 live (2026-10-23): retired rows are old paths (`Plant/...`, `Evaporators_Legacy/...`, sim tags). |
| `sqlth_partitions` | the data tables and their time ranges (`sqlt_data_1_2026_07` ... `sqlt_data_1_2026_10`, one per month) |
| `sqlt_data_1_YYYY_MM` | the samples: `tagid` (-> `sqlth_te.id`), `intvalue` / `floatvalue` / `stringvalue` / `datevalue`, `dataintegrity` (192 = good), `t_stamp` (epoch ms). About 209 million rows over four months. |
| `sqlth_drv` | historian drivers (`bh-standard`, provider `default`) |
| `sqlth_scinfo`, `sqlth_sce` | scan-class info / execution records |
| `sqlth_annotations` | trend annotations (empty) |

Which tags are historized is set on the tag or UDT member (**History** section of the Tag Editor; PAX status
members are historized "on change" by `pax-devices`). Real PLC history begins 2026-10-23 around 09:30 local, when
the devices were mapped to the PLC; earlier rows are simulator or placeholder data.

Example (read only): the last hour of one tag.

```sql
SELECT TOP 100 DATEADD(ms, d.t_stamp % 1000, DATEADD(s, d.t_stamp / 1000, '1970-01-01')) AS utc_time,
       d.floatvalue, d.dataintegrity
FROM dbo.sqlt_data_1_2026_10 d
JOIN dbo.sqlth_te t ON t.id = d.tagid
WHERE t.tagpath = 'boars_head/groveport/machine room/compressors/comp 5/comp/sucp' AND t.retired IS NULL
ORDER BY d.t_stamp DESC;
```

In scripts use `system.tag.queryTagHistory(paths=[...], startDate=..., endDate=..., aggregationMode="Average",
intervalHours=1)`, as `shared.Reports` does; it handles partitions and retired ids for you.

## Alarm journal (profile `MSSQL`)

Gateway web UI: **Config > Alarming > Journal**. Config
`config/resources/core/ignition/alarm-journal/MSSQL/config.json`.

| Setting | Value |
|---|---|
| Datasource | `ignition`, store-and-forward on |
| Tables | `alarm_events` (one row per event), `alarm_event_data` (properties of each event) |
| Stored | min priority Diagnostic, shelved events, enabled-change events, static + dynamic associated data |
| Pruning | **on, 1 year** |

`alarm_events`: `id`, `eventid` (alarm UUID), `source` (full alarm path), `displaypath`, `priority` (0
Diagnostic ... 4 Critical), `eventtype` (0 active, 1 clear, 2 ack, 4/5 enabled / disabled changes), `eventflags`,
`eventtime`. `alarm_event_data`: `id` (-> `alarm_events.id`), `propname`, `dtype`, `intvalue` / `floatvalue` /
`strvalue`. The most common properties are the associated data `Site`, `Area`, `Device` (added on the UDT alarms), `eventValue`, `ackUser`, `ackNotes`. 1.1 M events since 2026-07-25.

Used by: Operations > **Alarm Journal** (the Alarm Journal Table component, profile name `MSSQL`) and the Report
Report Builder's Alarm History source (`Reports/Alarms/*` named queries). Do not create a second journal profile; the
views expect `MSSQL`.

## Audit profiles

| Profile | Table | Used for | Retention |
|---|---|---|---|
| `OpsAudit` | `ops_audit_events` | **operator actions**: every `shared.Audit.writeTag` that changed a value (`tag write`), Out Of Service / return / comments, alarm config, ack / reset, user and role changes, integration settings | 90 days, pruning on |
| `DevAudit` | `dev_audit_events` | the **gateway audit profile** (`security-properties` `gatewayAuditProfile`): Designer resource edits, project updates, logins, gateway start / stop, config changes | 90 days, pruning on |
| (none) | `audit_events` | empty leftover table from an earlier default profile | - |

`ops_audit_events` columns: `audit_events_id`, `event_timestamp`, `actor` (session user; `Unknown` from gateway
scope), `actor_host`, `action`, `action_target`, `action_value` (for tag writes `old -> new`), `status_code`,
`originating_system` (for example `tagPath:...:/tagName:...:/view:<view path>`), `originating_context`.
Breakdown on 2026-10-23: 9,846 `tag write`, 20 `alarm config`, 4 `out of service`, 4 `return to service`, 3
`out of service comment`, 2 `role add`, 2 `alarm ack/reset`.

The Audit Log page reads it through `OpsAudit/AuditLog` (see [Audit Log](../features/audit-log.md)).

:::note DevAudit's column mapping is unusual
The `DevAudit` profile maps some columns to `dev_*` names (`dev_action`, `dev_action_target`) and others to the
plain names, so `dev_audit_events` has both sets (18 columns, half of them always NULL). It works; just query the
mapped ones (`event_timestamp`, `actor`, `dev_action`, `dev_action_target`, `action_value`).
:::
