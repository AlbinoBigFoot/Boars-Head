---
title: "Named Queries Reference"
sidebar_label: "Named Queries"
sidebar_position: 5
description: "All named queries of the BH project, by folder."
generated: true
custom_edit_url: null
---

:::note

:::

53 named queries. Every one runs on the database connection `ignition` (MSSQL, see the Database section).

| Folder | Queries | Page |
|---|---|---|
| `AdhocTrend` | 5 | [AdhocTrend](./adhoctrend.md) |
| `OpsAudit` | 1 | [OpsAudit](./opsaudit.md) |
| `OpsForms` | 16 | [OpsForms](./opsforms.md) |
| `OutOfService` | 9 | [OutOfService](./outofservice.md) |
| `Reports` | 20 | [Reports](./reports.md) |
| `TicketLogger` | 2 | [TicketLogger](./ticketlogger.md) |

| Query | Type | Parameters | Callers |
|---|---|---|---|
| [`AdhocTrend/Delete`](./adhoctrend.md#adhoctrend-delete) | `UpdateQuery` | `id, isAdmin` | 1 |
| [`AdhocTrend/Insert`](./adhoctrend.md#adhoctrend-insert) | `UpdateQuery` | `username, trendName, isShared, trendConfig` | 1 |
| [`AdhocTrend/Select`](./adhoctrend.md#adhoctrend-select) | `Query` | `currentUser` | 1 |
| [`AdhocTrend/SelectTrendConfigById`](./adhoctrend.md#adhoctrend-selecttrendconfigbyid) | `Query` | `trendId` | 1 |
| [`AdhocTrend/Update`](./adhoctrend.md#adhoctrend-update) | `UpdateQuery` | `trendId, trendName, trendConfig, isShared, isAdmin` | 1 |
| [`OpsAudit/AuditLog`](./opsaudit.md#opsaudit-auditlog) | `Query` | `startDate, endDate, search, allowed, refresh` | 1 |
| [`OpsForms/Pid/Check`](./opsforms.md#opsforms-pid-check) | `Query` | `cycleId, valvePk` | 1 |
| [`OpsForms/Pid/CompleteCycle`](./opsforms.md#opsforms-pid-completecycle) | `UpdateQuery` | `id, user, now` | 1 |
| [`OpsForms/Pid/CreateCycle`](./opsforms.md#opsforms-pid-createcycle) | `UpdateQuery` | `year, revision, performedBy, reviewedBy, user, now` | 1 |
| [`OpsForms/Pid/CycleById`](./opsforms.md#opsforms-pid-cyclebyid) | `Query` | `id` | 1 |
| [`OpsForms/Pid/Cycles`](./opsforms.md#opsforms-pid-cycles) | `Query` | `viewAll, username` | 1 |
| [`OpsForms/Pid/OpenCycle`](./opsforms.md#opsforms-pid-opencycle) | `Query` | | 2 |
| [`OpsForms/Pid/Rows`](./opsforms.md#opsforms-pid-rows) | `Query` | `cycleId, category, unit, search, show` | 2 |
| [`OpsForms/Pid/SaveCheck`](./opsforms.md#opsforms-pid-savecheck) | `UpdateQuery` | `cycleId, valvePk, verified, verifiedBy, verifiedDate, notes, user, now` | 1 |
| [`OpsForms/Pid/Summary`](./opsforms.md#opsforms-pid-summary) | `Query` | `cycleId` | 2 |
| [`OpsForms/Pid/Units`](./opsforms.md#opsforms-pid-units) | `Query` | `category` | 1 |
| [`OpsForms/Pid/UpdateCycleHeader`](./opsforms.md#opsforms-pid-updatecycleheader) | `UpdateQuery` | `id, revision, performedBy, reviewedBy` | 1 |
| [`OpsForms/Pid/UserChecks`](./opsforms.md#opsforms-pid-userchecks) | `Query` | `cycleId, username` | 1 |
| [`OpsForms/Submission/Get`](./opsforms.md#opsforms-submission-get) | `Query` | `id, viewAll, username` | 2 |
| [`OpsForms/Submission/Insert`](./opsforms.md#opsforms-submission-insert) | `UpdateQuery` | `formType, formDate, submittedBy, submittedName, submittedAt, shiftStatus, isAbnormal, releaseLogged, openItems, summary, data` | 1 |
| [`OpsForms/Submission/List`](./opsforms.md#opsforms-submission-list) | `Query` | `formType, startDate, endDate, viewAll, username, userFilter` | 1 |
| [`OpsForms/Submission/Users`](./opsforms.md#opsforms-submission-users) | `Query` | `viewAll` | 1 |
| [`OutOfService/CloseRecord`](./outofservice.md#outofservice-closerecord) | `UpdateQuery` | `id, status, returnedBy, returnedName, returnedAt, returnMemo` | 1 |
| [`OutOfService/Comments`](./outofservice.md#outofservice-comments) | `Query` | `allowed, id, refresh` | 1 |
| [`OutOfService/InsertComment`](./outofservice.md#outofservice-insertcomment) | `UpdateQuery` | `recordId, username, displayName, createdAt, status, comment` | 1 |
| [`OutOfService/InsertRecord`](./outofservice.md#outofservice-insertrecord) | `Query` | `tagPath, deviceName, deviceType, site, area, takenBy, takenName, takenAt, reason, memo, status, isBackfill` | 1 |
| [`OutOfService/OpenCount`](./outofservice.md#outofservice-opencount) | `Query` | `allowed, refresh` | 1 |
| [`OutOfService/OpenRecordId`](./outofservice.md#outofservice-openrecordid) | `Query` | `tagPath` | 1 |
| [`OutOfService/Record`](./outofservice.md#outofservice-record) | `Query` | `allowed, id, now, refresh` | 2 |
| [`OutOfService/Records`](./outofservice.md#outofservice-records) | `Query` | `allowed, filter, search, now, refresh, device, startDate, endDate` | 1 |
| [`OutOfService/SetStatus`](./outofservice.md#outofservice-setstatus) | `UpdateQuery` | `id, status` | 1 |
| [`Reports/Alarms/Events`](./reports.md#reports-alarms-events) | `Query` | `start, end, areas, devices, priorities, shifts, n` | 1 |
| [`Reports/Alarms/Facts`](./reports.md#reports-alarms-facts) | `Query` | `start, end, areas, devices, priorities, shifts, grain, groupBy` | 1 |
| [`Reports/Alarms/Options`](./reports.md#reports-alarms-options) | `Query` | `start, end, areas, devices, priorities, shifts` | 1 |
| [`Reports/Alarms/Top`](./reports.md#reports-alarms-top) | `Query` | `start, end, areas, devices, priorities, shifts, dim, orderBy, n` | 1 |
| [`Reports/Forms/Submissions`](./reports.md#reports-forms-submissions) | `Query` | `start, end, username, viewAll` | 1 |
| [`Reports/History/Coverage`](./reports.md#reports-history-coverage) | `Query` | `paths` | 1 |
| [`Reports/History/FirstSample`](./reports.md#reports-history-firstsample) | `Query` | `paths` | 1 |
| [`Reports/OOS/Options`](./reports.md#reports-oos-options) | `Query` | | 1 |
| [`Reports/OOS/Records`](./reports.md#reports-oos-records) | `Query` | `start, end` | 1 |
| [`Reports/Runs/Get`](./reports.md#reports-runs-get) | `Query` | `id, username` | 1 |
| [`Reports/Runs/Insert`](./reports.md#reports-runs-insert) | `UpdateQuery` | `username, source, title, definition, format, now` | 1 |
| [`Reports/Runs/LastByTitle`](./reports.md#reports-runs-lastbytitle) | `Query` | `username` | 1 |
| [`Reports/Runs/List`](./reports.md#reports-runs-list) | `Query` | `username, viewAll` | 1 |
| [`Reports/Runs/Recent`](./reports.md#reports-runs-recent) | `Query` | `username` | 1 |
| [`Reports/Templates/Delete`](./reports.md#reports-templates-delete) | `UpdateQuery` | `id, username, manage` | 1 |
| [`Reports/Templates/Get`](./reports.md#reports-templates-get) | `Query` | `id, username` | 1 |
| [`Reports/Templates/Insert`](./reports.md#reports-templates-insert) | `UpdateQuery` | `name, source, definition, username, ownerName, isShared, now` | 1 |
| [`Reports/Templates/List`](./reports.md#reports-templates-list) | `Query` | `username` | 1 |
| [`Reports/Templates/NameTaken`](./reports.md#reports-templates-nametaken) | `Query` | `username, name, id` | 1 |
| [`Reports/Templates/Update`](./reports.md#reports-templates-update) | `UpdateQuery` | `id, name, source, definition, isShared, now, username, manage` | 1 |
| [`TicketLogger/OutboxCounts`](./ticketlogger.md#ticketlogger-outboxcounts) | `Query` | | 1 |
| [`TicketLogger/OutboxInsert`](./ticketlogger.md#ticketlogger-outboxinsert) | `Query` | `destination, status, ticketType, priority, area, title, reporter, username, viewName, route, payload, externalId` | 1 |
