---
title: "SQL Schema Files Reference"
sidebar_label: "SQL Schema Files"
sidebar_position: 1
description: "Tables created by the repo's sql/*.sql scripts, parsed from the CREATE TABLE statements."
generated: true
custom_edit_url: null
---

:::note

:::

These are the tables the BH project owns in the MSSQL database `ignition`. Each `sql/*.sql` file is idempotent (`IF OBJECT_ID(...) IS NULL`), so it can be re-applied safely. Tables created by Ignition itself (historian, alarm journal, audit profiles) are described on the hand-written pages.

| Table | File | Columns | Purpose |
|---|---|---|---|
| [`dbo.adhoc_trend_configs`](#dbo-adhoc_trend_configs) | `sql/adhoc_trend_configs.sql` | 8 | Lightspeed AdhocTrend / user-saved trends schema (Microsoft SQL Server) Required by named queries under ignition/named-query/AdhocTrend/\* Database con |
| [`dbo.ops_form_submission`](#dbo-ops_form_submission) | `sql/operations_forms.sql` | 12 | form submissions |
| [`dbo.ops_pid_valve`](#dbo-ops_pid_valve) | `sql/operations_forms.sql` | 13 | P&ID valve master |
| [`dbo.ops_pid_cycle`](#dbo-ops_pid_cycle) | `sql/operations_forms.sql` | 10 | P&ID cycles |
| [`dbo.ops_pid_check`](#dbo-ops_pid_check) | `sql/operations_forms.sql` | 9 | P&ID checks |
| [`dbo.ops_pid_check_log`](#dbo-ops_pid_check_log) | `sql/operations_forms.sql` | 9 | append-only audit trail: one row per save of a check |
| [`dbo.oos_record`](#dbo-oos_record) | `sql/out_of_service_log.sql` | 18 | One row per time a device was taken out of service. Open while returned\_at IS NULL. |
| [`dbo.oos_comment`](#dbo-oos_comment) | `sql/out_of_service_log.sql` | 7 | Comment / status thread on a record (Engineering and up add; OutOfService/Comment) |
| [`dbo.report_run`](#dbo-report_run) | `sql/report_run.sql` | 7 | Report builder: recent report runs (Microsoft SQL Server, database 'ignition'). Idempotent. One row per download (PDF / Excel / CSV) so the bui |
| [`dbo.report_template`](#dbo-report_template) | `sql/report_template.sql` | 10 | Report builder: saved report templates (Microsoft SQL Server, database 'ignition'). Idempotent. Used by named queries ignition/named-query/Repo |
| [`dbo.ticket_outbox`](#dbo-ticket_outbox) | `sql/ticket_outbox.sql` | 16 | Ticket Logger outbox (Microsoft SQL Server, database 'ignition'). Idempotent. One row per ticket the HMI did not send straight to an external system: |

## dbo.adhoc\_trend\_configs {#dbo-adhoc_trend_configs}

Created by `sql/adhoc_trend_configs.sql`. Lightspeed AdhocTrend / user-saved trends schema (Microsoft SQL Server) Required by named queries under ignition/named-query/AdhocTrend/\* Database connection name in resource.json: "ignition"

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `username` | `NVARCHAR(255)` | NOT NULL | | |
| `trend_name` | `NVARCHAR(255)` | NOT NULL | | |
| `trend_config` | `NVARCHAR(MAX)` | NOT NULL | | JSON text (session.custom.AdhocTrend) |
| `is_shared` | `BIT` | NOT NULL | default 0 | |
| `created_at` | `DATETIME2(3)` | NOT NULL | default SYSUTCDATETIME() | |
| `updated_at` | `DATETIME2(3)` | NOT NULL | default SYSUTCDATETIME() | |
| `is_locked` | `BIT` | NOT NULL | default 0 | added by ALTER TABLE |

Constraints and indexes:

- `UNIQUE (username, trend_name)`
- `INDEX IX_adhoc_trend_configs_username (username)`
- `INDEX IX_adhoc_trend_configs_shared (is_shared) WHERE is_shared = 1`

## dbo.ops\_form\_submission {#dbo-ops_form_submission}

Created by `sql/operations_forms.sql`. form submissions

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `form_type` | `NVARCHAR(32)` | NOT NULL | | 'DailyRounds' \| 'ShiftLog' |
| `form_date` | `DATE` | NOT NULL | | the DATE field on the form |
| `submitted_by` | `NVARCHAR(255)` | NOT NULL | | session username (taken on the gateway) |
| `submitted_name` | `NVARCHAR(255)` | NULL | | NAME field on the form |
| `submitted_at` | `DATETIME2(0)` | NOT NULL | | gateway time of submit |
| `shift_status` | `NVARCHAR(64)` | NULL | | ShiftLog: Normal Operation / Abnormal - See Notes |
| `is_abnormal` | `BIT` | NOT NULL | default 0 | |
| `release_logged` | `BIT` | NOT NULL | default 0 | |
| `open_items` | `BIT` | NOT NULL | default 0 | |
| `summary` | `NVARCHAR(400)` | NULL | | one-line key summary for the history table |
| `data` | `NVARCHAR(MAX)` | NOT NULL | | JSON of every form field |

Constraints and indexes:

- `INDEX IX_ops_form_submission_date (form_date DESC, id DESC)`
- `INDEX IX_ops_form_submission_user (submitted_by, form_date DESC)`

## dbo.ops\_pid\_valve {#dbo-ops_pid_valve}

Created by `sql/operations_forms.sql`. P&ID valve master

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `valve_pk` | `INT` | NOT NULL | identity, PK | |
| `sort_order` | `INT` | NOT NULL | | row order of "All Valves (flat)" (1..725), natural key |
| `category` | `NVARCHAR(64)` | NOT NULL | | one of the six category tabs |
| `category_order` | `INT` | NOT NULL | | |
| `pid` | `NVARCHAR(32)` | NULL | | P&ID drawing (R-1, R-2, ...) |
| `unit_id` | `NVARCHAR(32)` | NOT NULL | | |
| `unit_desc` | `NVARCHAR(255)` | NULL | | Index tab description |
| `valve_id` | `NVARCHAR(64)` | NOT NULL | | |
| `size` | `NVARCHAR(64)` | NULL | | |
| `valve_type` | `NVARCHAR(64)` | NULL | | |
| `position` | `NVARCHAR(32)` | NULL | | |
| `function_service` | `NVARCHAR(400)` | NULL | | |
| `source_sheet` | `NVARCHAR(64)` | NULL | | |

Constraints and indexes:

- `CONSTRAINT UQ_ops_pid_valve_sort UNIQUE (sort_order)`

## dbo.ops\_pid\_cycle {#dbo-ops_pid_cycle}

Created by `sql/operations_forms.sql`. P&ID cycles

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `cycle_year` | `INT` | NOT NULL | | |
| `drawing_revision` | `NVARCHAR(255)` | NULL | | |
| `performed_by` | `NVARCHAR(255)` | NULL | | |
| `reviewed_by` | `NVARCHAR(255)` | NULL | | |
| `status` | `NVARCHAR(16)` | NOT NULL | default N'Open' | |
| `created_by` | `NVARCHAR(255)` | NOT NULL | | |
| `created_at` | `DATETIME2(0)` | NOT NULL | | |
| `completed_by` | `NVARCHAR(255)` | NULL | | |
| `completed_at` | `DATETIME2(0)` | NULL | | |

Constraints and indexes:

- `UNIQUE INDEX UX_ops_pid_cycle_open (status) WHERE status = N'Open'`

## dbo.ops\_pid\_check {#dbo-ops_pid_check}

Created by `sql/operations_forms.sql`. P&ID checks

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `cycle_id` | `INT` | NOT NULL | FK -&gt; dbo.ops\_pid\_cycle(id) | |
| `valve_pk` | `INT` | NOT NULL | FK -&gt; dbo.ops\_pid\_valve(valve\_pk) | |
| `verified` | `BIT` | NOT NULL | default 0 | |
| `verified_by` | `NVARCHAR(255)` | NULL | | operator name (Verified By column) |
| `verified_date` | `DATE` | NULL | | |
| `notes` | `NVARCHAR(1000)` | NULL | | Notes / Discrepancy |
| `updated_by` | `NVARCHAR(255)` | NOT NULL | | session username of the last save |
| `updated_at` | `DATETIME2(0)` | NOT NULL | | |

Constraints and indexes:

- `CONSTRAINT UQ_ops_pid_check UNIQUE (cycle_id, valve_pk)`

## dbo.ops\_pid\_check\_log {#dbo-ops_pid_check_log}

Created by `sql/operations_forms.sql`. append-only audit trail: one row per save of a check

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `cycle_id` | `INT` | NOT NULL | | |
| `valve_pk` | `INT` | NOT NULL | | |
| `verified` | `BIT` | NOT NULL | | |
| `verified_by` | `NVARCHAR(255)` | NULL | | |
| `verified_date` | `DATE` | NULL | | |
| `notes` | `NVARCHAR(1000)` | NULL | | |
| `updated_by` | `NVARCHAR(255)` | NOT NULL | | |
| `updated_at` | `DATETIME2(0)` | NOT NULL | | |

Constraints and indexes:

- `INDEX IX_ops_pid_check_log_cycle_user (cycle_id, updated_by)`

## dbo.oos\_record {#dbo-oos_record}

Created by `sql/out_of_service_log.sql`. One row per time a device was taken out of service. Open while returned\_at IS NULL.

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `tag_path` | `NVARCHAR(400)` | NOT NULL | | device UDT instance, e.g. [default]Boars\_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 2 |
| `device_name` | `NVARCHAR(200)` | NOT NULL | | |
| `device_type` | `NVARCHAR(100)` | NOT NULL | | UDT typeId leaf (Pump, Valve, Sensor ...) |
| `site` | `NVARCHAR(100)` | NOT NULL | default N'' | |
| `area` | `NVARCHAR(100)` | NOT NULL | default N'' | |
| `taken_by` | `NVARCHAR(255)` | NOT NULL | | session username (gateway side) |
| `taken_name` | `NVARCHAR(255)` | NOT NULL | | display name at the time |
| `taken_at` | `DATETIME2(3)` | NOT NULL | | gateway clock |
| `reason` | `NVARCHAR(50)` | NOT NULL | | |
| `memo` | `NVARCHAR(2000)` | NOT NULL | | |
| `status` | `NVARCHAR(50)` | NOT NULL | default N'Out Of Service' | Out Of Service / In Progress / Awaiting Parts / ... / Returned |
| `returned_by` | `NVARCHAR(255)` | NULL | | |
| `returned_name` | `NVARCHAR(255)` | NULL | | |
| `returned_at` | `DATETIME2(3)` | NULL | | |
| `return_memo` | `NVARCHAR(2000)` | NULL | | |
| `is_backfill` | `BIT` | NOT NULL | default 0 | 1 = device was found out of service with no record |
| `updated_at` | `DATETIME2(3)` | NOT NULL | default SYSDATETIME() | |

Constraints and indexes:

- `UNIQUE INDEX UX_oos_record_open_tag (tag_path) WHERE returned_at IS NULL`
- `INDEX IX_oos_record_taken_at (taken_at DESC)`

## dbo.oos\_comment {#dbo-oos_comment}

Created by `sql/out_of_service_log.sql`. Comment / status thread on a record (Engineering and up add; OutOfService/Comment)

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `record_id` | `INT` | NOT NULL | FK -&gt; dbo.oos\_record(id) cascade | |
| `username` | `NVARCHAR(255)` | NOT NULL | | session username (gateway side) |
| `display_name` | `NVARCHAR(255)` | NOT NULL | | |
| `created_at` | `DATETIME2(3)` | NOT NULL | | gateway clock |
| `status` | `NVARCHAR(50)` | NULL | | optional status change carried by this comment |
| `comment` | `NVARCHAR(2000)` | NOT NULL | | |

Constraints and indexes:

- `INDEX IX_oos_comment_record (record_id, created_at)`

## dbo.report\_run {#dbo-report_run}

Created by `sql/report_run.sql`. Report builder: recent report runs (Microsoft SQL Server, database 'ignition'). Idempotent.

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `username` | `NVARCHAR(255)` | NOT NULL | | |
| `source` | `NVARCHAR(40)` | NOT NULL | | |
| `title` | `NVARCHAR(200)` | NOT NULL | | |
| `definition` | `NVARCHAR(MAX)` | NOT NULL | | |
| `format` | `NVARCHAR(10)` | NOT NULL | | |
| `run_at` | `DATETIME2(3)` | NOT NULL | default SYSDATETIME() | |

Constraints and indexes:

- `INDEX IX_report_run_user (username, run_at DESC)`

## dbo.report\_template {#dbo-report_template}

Created by `sql/report_template.sql`. Report builder: saved report templates (Microsoft SQL Server, database 'ignition'). Idempotent.

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `name` | `NVARCHAR(120)` | NOT NULL | | |
| `source` | `NVARCHAR(40)` | NOT NULL | | |
| `definition` | `NVARCHAR(MAX)` | NOT NULL | | |
| `owner_username` | `NVARCHAR(255)` | NOT NULL | | |
| `owner_name` | `NVARCHAR(255)` | NULL | | |
| `is_shared` | `BIT` | NOT NULL | default 0 | |
| `created_at` | `DATETIME2(3)` | NOT NULL | default SYSDATETIME() | |
| `updated_at` | `DATETIME2(3)` | NOT NULL | default SYSDATETIME() | |
| `updated_by` | `NVARCHAR(255)` | NULL | | |

Constraints and indexes:

- `CONSTRAINT UQ_report_template_owner_name UNIQUE (owner_username, name)`
- `INDEX IX_report_template_shared (is_shared) WHERE is_shared = 1`

## dbo.ticket\_outbox {#dbo-ticket_outbox}

Created by `sql/ticket_outbox.sql`. Ticket Logger outbox (Microsoft SQL Server, database 'ignition'). Idempotent. One row per ticket the HMI did not send straight to an external system: status 'Pending Oracle' = routed to Oracle (stub adapter) and waiting for the client integration to drain it; status 'Dry Run'        = recorded while [default]\_Config/TicketLogger/DryRun was on (nothing was sent). A future sender sets status 'Sent' / 'Failed', external\_id, sent\_at and last\_error. Written by shared.TicketLogger through the named queries TicketLogger/Outbox\* (docs/ticket-logger.md).

| Column | Type | Null | Keys / defaults | Comment |
|---|---|---|---|---|
| `id` | `INT` | NOT NULL | identity, PK | |
| `created_at` | `DATETIME2(3)` | NOT NULL | default SYSDATETIME() | |
| `destination` | `NVARCHAR(40)` | NOT NULL | | |
| `status` | `NVARCHAR(40)` | NOT NULL | | |
| `ticket_type` | `NVARCHAR(40)` | NOT NULL | | |
| `priority` | `NVARCHAR(10)` | NOT NULL | | |
| `area` | `NVARCHAR(100)` | NOT NULL | | |
| `title` | `NVARCHAR(400)` | NOT NULL | | |
| `reporter` | `NVARCHAR(200)` | NOT NULL | | |
| `username` | `NVARCHAR(200)` | NOT NULL | | |
| `view_name` | `NVARCHAR(400)` | NOT NULL | | |
| `route` | `NVARCHAR(400)` | NOT NULL | | |
| `payload` | `NVARCHAR(MAX)` | NOT NULL | | |
| `external_id` | `NVARCHAR(100)` | NULL | | |
| `sent_at` | `DATETIME2(3)` | NULL | | |
| `last_error` | `NVARCHAR(1000)` | NULL | | |

Constraints and indexes:

- `INDEX IX_ticket_outbox_status (destination, status, created_at)`
