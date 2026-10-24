---
title: "Named Queries: TicketLogger"
sidebar_label: "TicketLogger"
description: "Named queries under TicketLogger/: SQL, parameters and callers."
generated: true
custom_edit_url: null
---

:::note

:::

Designer: **Project Browser > Data > Named Queries > TicketLogger**. Files: `gateways/standard/data/projects/BH/ignition/named-query/TicketLogger/<Query>/query.sql + resource.json`.

| Query | Type | Parameters | Callers |
|---|---|---|---|
| [`TicketLogger/OutboxCounts`](#ticketlogger-outboxcounts) | `Query` | | 1 |
| [`TicketLogger/OutboxInsert`](#ticketlogger-outboxinsert) | `Query` | `destination, status, ticketType, priority, area, title, reporter, username, viewName, route, payload, externalId` | 1 |

## TicketLogger/OutboxCounts {#ticketlogger-outboxcounts}

| Setting | Value |
|---|---|
| Path (what callers pass) | `TicketLogger/OutboxCounts` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

```sql
-- Ticket Logger outbox counts per destination / status (Ticket Logger > Settings).
SELECT destination, status, COUNT(*) AS n
FROM dbo.ticket_outbox
GROUP BY destination, status
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.TicketLogger.outboxCounts` | script | |

## TicketLogger/OutboxInsert {#ticketlogger-outboxinsert}

| Setting | Value |
|---|---|
| Path (what callers pass) | `TicketLogger/OutboxInsert` |
| Type | `Query` |
| Database | `ignition` |
| Enabled | `True` |
| Scope | `DG` |
| Cache | `off` |
| Max rows | `unlimited` |
| Security | no role / zone restriction (the SQL and the callers check) |

| Parameter | Mode | SQL type |
|---|---|---|
| `:destination` | Parameter | `String` |
| `:status` | Parameter | `String` |
| `:ticketType` | Parameter | `String` |
| `:priority` | Parameter | `String` |
| `:area` | Parameter | `String` |
| `:title` | Parameter | `String` |
| `:reporter` | Parameter | `String` |
| `:username` | Parameter | `String` |
| `:viewName` | Parameter | `String` |
| `:route` | Parameter | `String` |
| `:payload` | Parameter | `String` |
| `:externalId` | Parameter | `String` |

```sql
-- Ticket Logger outbox row (shared.TicketLogger._outbox: Oracle stub / dry run); returns the id.
INSERT INTO dbo.ticket_outbox
    (destination, status, ticket_type, priority, area, title, reporter, username, view_name, route, payload,
     external_id)
OUTPUT INSERTED.id
VALUES
    (:destination, :status, :ticketType, :priority, :area, :title, :reporter, :username, :viewName, :route, :payload,
     NULLIF(:externalId, ''))
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `shared.TicketLogger._outbox` | script | |
