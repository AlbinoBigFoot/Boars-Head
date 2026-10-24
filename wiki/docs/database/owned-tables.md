---
title: Our Tables
sidebar_position: 2
description: The tables the BH project owns in the `ignition` database - purpose, key columns, who writes and reads them, rules and retention.
sources:
  - sql/*.sql
  - gateways/standard/data/projects/BH/ignition/named-query/**/*
  - docs/out-of-service.md
  - docs/operations-forms.md
  - docs/report-builder.md
last_verified: 2026-10-24
---

# Our Tables

Each table is created by an **idempotent** script in `sql/` (safe to re-run) and accessed only through named
queries. Full column lists: [SQL Schema Files](./reference/sql-schema.md). Times are written by the gateway
(`SYSDATETIME()` or `system.date.now()`), users come from the Perspective session.

## `dbo.adhoc_trend_configs` (saved trends)

`sql/adhoc_trend_configs.sql`. One row per saved trend.

| Column | Meaning |
|---|---|
| `username`, `trend_name` | owner and name (unique together) |
| `trend_config` | JSON of `session.custom.AdhocTrend` (pens, plots, colours, range) |
| `is_shared` | visible to everyone |
| `is_locked` | system trend (the FT trend displays seeded by `scripts/_build_saved_trends.py`): only roles with `Trends/ManageLocked` may save over or delete it |
| `created_at`, `updated_at` | UTC |

Written / read by the `AdhocTrend/*` named queries from the Trending and Saved Trends views. Saving needs
`Trends/Save`; overwriting someone else's or a locked trend needs `Trends/ManageLocked`. No retention: rows stay
until deleted.

## Operations Forms

`sql/operations_forms.sql`. All access through `shared.Forms` (`OpsForms/*`).

| Table | Purpose | Notes |
|---|---|---|
| `ops_form_submission` | one row per submitted Daily Rounds Log or NH3 Shift Log | `form_type` (`DailyRounds` / `ShiftLog`), `form_date`, `submitted_by` (username) / `submitted_name`, `submitted_at`, summary flags (`shift_status`, `is_abnormal`, `release_logged`, `open_items`, `summary`), and `data` = JSON of every field plus computed averages. Read only after submit. |
| `ops_pid_valve` | the 725-valve master list of the Annual P&ID Verification workbook | loaded once from `Annual P&ID Verification.xlsx` (natural key `sort_order`) |
| `ops_pid_cycle` | one yearly verification cycle | `status` Open / Complete; a filtered unique index allows only **one Open** cycle |
| `ops_pid_check` | the current check of a valve in a cycle | unique (`cycle_id`, `valve_pk`); `verified`, `verified_by`, `verified_date`, `notes`, `updated_by/at` |
| `ops_pid_check_log` | append-only copy of every check save | who changed what, when (audit trail for the shared cycle) |

Visibility rules are in the SQL: without `Forms/ViewAll` a user only sees rows where `submitted_by` is their own
username. PDFs are generated on demand from the stored row; no PDF is stored. No retention.

## Out Of Service

`sql/out_of_service_log.sql`. All writes through `shared.OutOfService`.

| Table | Purpose | Notes |
|---|---|---|
| `oos_record` | one row per time a device was taken out of service | `tag_path`, `device_name`, `device_type`, `site`, `area` (parsed from `Boars_Head/<Site>/<Area>/...`), `taken_by/name/at`, `reason`, `memo`, `status`, `returned_by/name/at`, `return_memo`, `is_backfill`. **Open while `returned_at IS NULL`**; the filtered unique index `UX_oos_record_open_tag` allows one open record per device. |
| `oos_comment` | comment / status thread on a record | `record_id` (FK, `ON DELETE CASCADE`), `username`, `display_name`, `created_at`, optional `status`, `comment` |

The record and the `<device>.Enabled` tag are written in **one transaction** (see
[Out Of Service](../features/out-of-service.md)). Page reads (`Records`, `Record`, `Comments`, `OpenCount`) carry
`:allowed` = `OutOfService/View`. No retention.

## Custom reports

| Table | File | Purpose |
|---|---|---|
| `report_template` | `sql/report_template.sql` | saved report definitions: `name`, `source`, `definition` (JSON), `owner_username` / `owner_name`, `is_shared`, `updated_by`; unique (`owner_username`, `name`). Only the owner, or `Reports/ManageTemplates` for a shared one, may edit or delete (also enforced in the SQL). |
| `report_run` | `sql/report_run.sql` | one row per download (user, source, title, definition, format, `run_at`) for the **Recent Runs** tab of Saved Reports (and the Report Builder's Recent list). Own rows only, all rows with `Reports/ManageTemplates`. Has no template id. Can be purged freely. |

Both through `shared.Reports` (`Reports/Templates/*`, `Reports/Runs/*`). The Report Builder also **reads**
`oos_record`, `ops_form_submission`, the alarm journal and the historian (see
[Report Builder](../features/custom-reports.md)).

## Ticket Logger outbox

| Table | File | Purpose |
|---|---|---|
| `ticket_outbox` | `sql/ticket_outbox.sql` | one row per ticket the HMI did not send straight to an external system: `destination`, `status`, `ticket_type`, `priority`, `area`, `title`, `reporter`, `username`, `view_name`, `route`, `payload` (the ticket as JSON, never credentials), `external_id`, `sent_at`, `last_error`. Status `Pending Oracle` = routed to the Oracle stub and waiting for the client integration; `Dry Run` = recorded while `[default]_Config/TicketLogger/DryRun` was on (nothing sent). A future sender sets `Sent` / `Failed`. |

Written by `shared.TicketLogger` through the named queries `TicketLogger/OutboxInsert` and `TicketLogger/OutboxCounts`.
Every role may submit a ticket (`TicketLogger/Use`); the routing settings need `TicketLogger/Settings` (OneShot only).

## Adding a table

1. Write `sql/<feature>.sql` in the same idempotent style: `IF OBJECT_ID(N'dbo.x', N'U') IS NULL BEGIN CREATE
   TABLE ... END GO`, named constraints (`PK_x`, `DF_x_col`, `UX_x_...`), indexes in `IF NOT EXISTS` blocks, a
   comment per column, `ALTER TABLE ... ADD` blocks for later columns.
2. Apply it with SSMS or `sqlcmd -I`; never create tables by hand on production without the file in git.
3. Access it only through named queries: Designer > Project Browser > Named Queries > right-click > New Named Query,
   type **Query** or **Update Query**, database `ignition`, then call it from a `shared.*` script
   ([Named Queries](../scripting/named-queries.md)).
4. Run `python -I wiki/tools/gen_all.py scripting` so [SQL Schema Files](./reference/sql-schema.md) shows it.
