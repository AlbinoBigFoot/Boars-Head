---
title: Out Of Service Log
sidebar_position: 10
description: The Out Of Service log page (/operations/out-of-service and /:device), the right-click take / return menu and the memo dialog.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/OutOfService/**/view.json"
  - "docs/out-of-service.md"
last_verified: 2026-10-23
---

# Out Of Service Log

A device is **out of service** (OOS) when its UDT instance is disabled (`<device>.Enabled = false`). This page lists
every take-out and return with the reason, memo, who and when, and lets users add comments. The full feature
(SQL tables, audit, permissions) is described in [Features](../../features/index.md) and `docs/out-of-service.md`;
this guide covers the views.

![Out Of Service Log](/img/perspective/out-of-service.png)

| | |
|---|---|
| Routes | `/operations/out-of-service` (all devices), `/operations/out-of-service/:device` (one device's history; title "Out Of Service History") |
| View | [`00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog`](../reference/views/00-pages/boars-head/operations/outofservice/outofservicelog.md), param `device` from the URL |
| Parts | `_Assets/CommentEntry` (comment box), `_Assets/TwoLineCell` (table cell) |
| Dialog | `01_Popups/00_Faceplates/Alerts/OutOfService` (memo dialog, modal) |
| Changing it | [Out Of Service](../../features/out-of-service.md#how-to-change-it) |
| SQL | `dbo.oos_record`, `dbo.oos_comment` through the named queries `OutOfService/Records`, `Record`, `Comments`, `OpenCount` |
| Nav | Groveport > Operations > Out Of Service Log (`data.permission: OutOfService/View`); header notes icon; device right-click "Out Of Service History" |

## What It Shows

- **Filter bar:** Show (Out Of Service / Returned / All), From / To dates, Search (device, area, type, reason),
  Refresh, and the record count.
- **Table:** one row per record. Selecting a row opens the detail pane with the full record, its comments and a
  comment box (`CommentEntry`, calls `shared.OutOfService.addComment`).
- **Narrow screens:** `custom.narrow` / `custom.compact` switch the layout below set widths.

Data comes from named-query bindings on custom properties, for example:

```js
// custom.records: named query OutOfService/Records, return format dataset; each parameter is an expression
allowed:   if(coalesce({session.custom.Permissions.OutOfService.View}, false), 1, 0)
filter:    coalesce({view.custom.filter}, 'open')            // open | returned | all
search:    if(trim(coalesce({view.custom.search}, '')) = '', '', '%' + trim(coalesce({view.custom.search}, '')) + '%')
device:    coalesce({view.custom.devicePath}, '')            // from the :device URL param
startDate: {view.custom.startDate}
endDate:   {view.custom.endDate}
now:       now(60000)                                       // re-query every minute
refresh:   coalesce({view.custom.refresh}, 0)               // bumped by Refresh and after a comment
```

The `allowed` parameter puts the permission check into the SQL itself, so a session without `OutOfService/View`
gets no rows even if it reaches the page. A comment can also set a status (No Status Change, In Progress, Awaiting
Parts, On Hold, Ready To Return).

## Taking A Device Out Of Service

From any device graphic: right-click > **Take Out Of Service** (or **Return To Service**). The item shows only with
`session.custom.Permissions.OutOfService.Set`. The menu sends a page message `oosToggle`; the clicked component's
handler opens the memo dialog through `shared.OutOfService.openDialog`:

- Reason (required to take out): Maintenance, Repair, Awaiting Parts, Seasonal, Safety Lockout, Other.
- Memo (required both ways): 10 to 2000 characters, with a live counter.
- Confirm calls `shared.OutOfService.setOutOfService(self.session, ...)`, which re-checks the permission, writes the
  SQL record and the `.Enabled` flag in one transaction, and writes an OpsAudit entry.

`shared.Audit.writeTag` refuses direct `.Enabled` writes from sessions, so this dialog is the only way to change
the flag from the HMI.

While a device is OOS, its component shows only the Out Of Service icon and the `OUT OF SERVICE` status: values,
alarm frame and comm loss are hidden (CSS `device-oos`). Device tables skip disabled instances.

## Header Notes Icon

`00_Pages/00_Docked/_Assets/OosNotification` shows the number of open OOS records (`OutOfService/OpenCount`, polled
every 30 s) and opens this page. It is hidden without `OutOfService/View`:

```js
// Header root/OosNotification position.display
coalesce({session.custom.Permissions.OutOfService.View}, false)
```
