---
title: Audit Log
sidebar_position: 11
description: The OpsAudit trail of operator actions (what is recorded, what is not) and the Admin > Audit Log page.
sources:
  - docs/ops-audit.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Audit/code.py
  - gateways/standard/data/projects/BH/ignition/named-query/OpsAudit/**/*
  - gateways/standard/data/config/resources/core/ignition/audit-profile/OpsAudit/config.json
last_verified: 2026-10-23
---

# Audit Log

## What it does

Every operator action that changes something is written to the **OpsAudit** audit profile (table
`dbo.ops_audit_events`), with who, from where, what, old and new value. **Admin > Audit Log**
(`/operations/audit`) lets Engineering and Administrators search it.

| Recorded | By |
|---|---|
| tag writes that actually changed a value (`tag write`, `old -> new`, enum words) | `shared.Audit.writeTag` |
| Out Of Service, Return To Service, comments | `shared.OutOfService` via `shared.Audit.logEvent` |
| alarm configuration changes, ack / reset | `shared.AlarmConfig`, faceplate Alarms tabs |
| user and role changes (`user add/edit/delete`, `role add/edit/delete`) | `shared.UserAdmin.commit` |
| Roles & Permissions saves (action **Permissions Changed**, value = the changed cells such as `Valve/Command Maintenance=True`) | `shared.PermissionMatrix.save` |
| integration settings, token replaced | `shared.Integrations` |

**Not recorded**: writes refused before they happened (no permission, PLC write lock, `readOnly` tags, direct
`.Enabled` from a session; decided 2026-10-23 not to log anything about the PLC write lock), writes that changed
nothing, Operations Forms (they have their own SQL history), report templates.

Gateway-side (Designer, login, gateway start) events go to a separate profile, `DevAudit`
(`dev_audit_events`); see [Ignition Tables](../database/ignition-tables.md).

## How to use it

1. **Admin > Audit Log** (needs `AuditLog/View`).
2. Pick a range: **24 Hours / 7 Days / 30 Days** (default 7 days) or Start / End.
3. **Search** matches user, action, target, value, tag path and view.
4. Columns: **Time**, **User**, **Action**, **Target** (friendly device path; the raw tag path in the tooltip),
   **Change** (`old → new`), **Source** (the view that made the change). Every column sorts.
5. Click a row for a detail card with every field in full.

At most 5,000 rows are returned ("Latest 5,000 Events (Limit) · Narrow The Range").

The layout is the Form Layout System look (`form-*` style classes): a title row with the event count ("N Events"; at
the 5,000-row limit "Latest 5,000 Events (Limit) - Narrow The Range"), **one fixed filter bar** (range buttons,
Start, End, Search, Refresh) and a table that fills the rest of the height, with only its body scrolling (pager 25-500
rows, default 100). Each cell is one line with an ellipsis; the tooltip shows the raw value (Target = raw tag path,
Change = raw value, Source = view path and host). A row click opens the detail card with every field in full: a 400 px
side pane at 1500 px or wider, otherwise it replaces the table (Back To List). Under 1000 px the Source column hides.

![OPS Audit Log, 7 Days range (user names blurred)](/img/features/audit-log/audit-log.png)

## Where to find it

- **HMI**: nav Groveport > Admin > Audit Log.
- **Designer**: Project Browser > Perspective > Views > `00_Pages` > `Boars Head` > `Operations` > `AuditLog`;
  Project Browser > Named Queries > `OpsAudit` > `AuditLog`; scripts `shared.Audit`.
- **Gateway web UI**: Platform > Security > Audit Profiles (the `OpsAudit` profile writes table `ops_audit_events` in the
  `ignition` database).

## Where the pieces live (developers)

| Piece | Where |
|---|---|
| Audit profile | Gateway **Config > Security > Auditing** profile `OpsAudit`: database `ignition`, table `ops_audit_events`, 90-day pruning (`config/resources/core/ignition/audit-profile/OpsAudit`) |
| Write path | `shared.Audit.writeTag`, `shared.Audit.logEvent` (`system.util.audit(..., auditProfile="OpsAudit")`) - see [Write Paths](../scripting/write-path.md) |
| Page | `00_Pages/Boars Head/Operations/AuditLog`, cell view `00_Pages/Boars Head/Operations/_Assets/AuditLogCell` |
| Query | `OpsAudit/AuditLog` (`:startDate`, `:endDate`, `:search`, `:allowed`); display, tooltip and detail columns are computed in the SQL (`STRING_SPLIT` with ordinals needs SQL Server 2022 / compatibility 160) |
| Security | Content / Denied on `session.custom.Permissions.AuditLog.View`; `:allowed` bound to it |
| Component names | The page's Denied, DeniedMsg, Content, Table and Subtitle components are referenced by name: keep those names when you edit the page |

Column values: `actor` = session user (`Unknown` from gateway scope), `action_target` = the last three tag path
parts, `originating_system` = `tagPath:...:/tagName:...:/view:<view path>`.

## How To Change It

- **The page (Designer):** Project Browser > Perspective > Views > `00_Pages/Boars Head/Operations` > `AuditLog`. The
  table, filter bar and detail pane are components of that view; the cell look is the view
  `_Assets/AuditLogCell`. Edit, save, then test in a session as an Engineering user.
- **The columns:** Project Browser > Named Queries > `OpsAudit` > `AuditLog`. The display, tooltip and detail columns
  are computed in the SQL; edit the query, click **Test Query**, save.
- **A new audited action:** in the script that performs the action call
  `shared.Audit.logEvent(action, target, value, tagPath=..., viewName=...)` after it succeeds (Project Library >
  `shared` > `Audit`). Use a short lower-case action name (the page Title-Cases it).
- **Retention:** Gateway web UI > Config > Security > Audit Profiles > `OpsAudit`: raise the retention days if the
  site needs more than 90.

## Known limitations and parked items

- **Why the log looked empty before 2026-10-23**: few audited actions since 2026-10-02 (the device tags read the
  read-only PLC tags behind the write lock, so faceplate writes are refused and not audited), and the old page
  defaulted to a one-day window.
- Refused writes stay unlogged by decision (the PLC write lock is temporary).
