---
title: Named Queries
sidebar_position: 7
description: The BH named queries (OpsForms, OutOfService, Reports, AdhocTrend, OpsAudit, TicketLogger) - how they are organised, called, secured and changed.
sources:
  - gateways/standard/data/projects/BH/ignition/named-query/**/*
last_verified: 2026-10-24
---

# Named Queries

A **named query** is a SQL statement saved as a project resource, with typed parameters. Scripts and bindings
call it by path (`system.db.runNamedQuery("BH", "OutOfService/Records", params)` or a Query binding) instead of
building SQL strings, which keeps SQL injection out and puts all SQL in one place.

- Designer: **Project Browser > Data > Named Queries**.
- Disk: `gateways/standard/data/projects/BH/ignition/named-query/<Folder>/<Query>/query.sql` plus
  `resource.json` (type, database, parameters, caching).
- Database: every BH query runs on the gateway database connection **`ignition`** (MSSQL, see
  [Database](../database/index.md)).
- Full SQL, parameters and callers of each query: [Named Queries reference](./reference/named-queries/index.md).

## The folders

| Folder | Queries | Used by | Tables |
|---|---|---|---|
| `AdhocTrend/*` | Select, SelectTrendConfigById, Insert, Update, Delete | Trending page, Saved Trends | `adhoc_trend_configs` |
| `OpsAudit/AuditLog` | 1 | Operations > Audit Log page (`:allowed` = `AuditLog/View`) | `ops_audit_events` |
| `OpsForms/Submission/*`, `OpsForms/Pid/*` | 4 + 12 | `shared.Forms` only | `ops_form_submission`, `ops_pid_*` |
| `OutOfService/*` | 9 | page bindings (`Records`, `Record`, `Comments`, `OpenCount`) and `shared.OutOfService` (writes) | `oos_record`, `oos_comment` |
| `TicketLogger/*` | OutboxInsert, OutboxCounts | `shared.TicketLogger` (Oracle-routed and dry-run tickets; counts on the Settings screen) | `ticket_outbox` |
| `Reports/*` | Alarms (4), Forms, History (2), OOS (2), Runs (5: Get, Insert, LastByTitle, List, Recent), Templates (6: Delete, Get, Insert, List, NameTaken, Update) | `shared.Reports` only | journal, historian, `oos_record`, `ops_form_submission`, `report_run`, `report_template` |

Edit them in the Designer: Project Browser > Data > Named Queries > the folder > the query. Use **Test Query** before
saving.

## How BH secures queries

Named queries here have no role restriction in their resource (the "Security" setting is empty). Security is done
two ways instead:

1. **Gateway-only callers.** Write queries (`OutOfService/InsertRecord`, `OpsForms/Submission/Insert`,
   `Reports/Templates/Update` ...) are called only from library functions that first run
   `shared.Security.require(...)` and take the username from the session.
2. **An `:allowed` parameter bound to a PROTECTED session prop** for queries that a page binds directly:
   `WHERE :allowed = 1 AND ...`, with `allowed` bound to, for example,
   `{session.custom.Permissions.OutOfService.View}`. A user without the permission gets zero rows even if they
   craft a request.
3. **Row-level rules in the SQL** where users may only see their own rows, for example Form History:
   `WHERE (:viewAll = 1 OR submitted_by = :username)`, with `username` supplied by `shared.Forms` from the session.

## Calling a query from a script

```python
ds = system.db.runNamedQuery(project="BH", path="OutOfService/OpenCount", parameters={"allowed": 1, "refresh": 0})
newId = system.db.runNamedQuery(project="BH", path="OpsForms/Submission/Insert", parameters=params, getKey=True)
```

- `project="BH"` is required from gateway scope (timers, report scripts, WebDev); harmless from a session.
- `getKey=True` returns the new identity value of an `INSERT` (or use `OUTPUT INSERTED.id` in the SQL, as
  `OutOfService/InsertRecord` does).
- Inside a DB transaction pass `tx=` (see `shared.OutOfService._query`).
- Libraries wrap this in a helper (`shared.Forms._nq(path, params)`, `shared.Reports._nq(...)`) that adds the
  folder prefix, so a search for the full path may not find the caller: search for the last part too.

## Gotchas

- **No `:name` inside SQL comments.** Ignition turns any `:word` into a JDBC placeholder, even in a `--` comment,
  and the query fails with "index N is out of range". Write "the start date" in comments, not `:startDate`.
- **`:refresh` parameters** in the page queries do nothing in SQL (`AND :refresh >= 0`); bumping the bound value
  forces the binding to re-run.
- **Parameter types** (`sqlType`): 2 Int4, 6 Boolean, 7 String, 8 DateTime. A DateTime parameter must get a Java
  `Date` (`system.date.now()`), not a string.
- **Caching** is off on every query; lists refresh on their own polling or `:refresh`.

## Adding a query

1. Designer > Project Browser > Data > Named Queries > right-click the folder (or the root) > **New Named Query**.
   Pick the type (**Query** for a read, **Update Query** for a write), database `ignition`, and paste the SQL.
2. Use parameters for every value (Parameters tab: name, type, default). For a page-bound query add `:allowed` and
   bind it to a session permission.
3. Click **Test Query** with sample values, then save.
4. Call it from a script (`system.db.runNamedQuery('<Folder>/<Query>', {...})` in a `shared.*` function) or from a
   query binding on a component.
5. Run `python -I wiki/tools/gen_all.py scripting` so the reference lists it with its callers.
