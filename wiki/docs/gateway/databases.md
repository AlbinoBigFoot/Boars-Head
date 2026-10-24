---
title: Databases And Store & Forward
sidebar_position: 6
description: The ignition database connection to MSSQL, JDBC drivers and translators, the Store & Forward engine, and what uses the database.
sources:
  - gateways/standard/data/config/resources/core/ignition/database-connection/ignition/config.json
  - gateways/standard/data/config/resources/core/ignition/store-and-forward-engine/ignition/config.json
  - sql/*.sql
last_verified: 2026-10-24
---

# Databases And Store & Forward

## The `ignition` Connection

**Where:** Connections > Databases > Connections > `ignition`
(`config/resources/core/ignition/database-connection/ignition/config.json`, not tracked: it holds the encrypted
password).

| Setting | Value | Notes |
|---|---|---|
| Driver / translator | `Microsoft SQLServer` / `MSSQL` | JDBC driver jar shipped in `database-driver/Microsoft SQLServer/` |
| Connect URL | `jdbc:sqlserver://mssql:1433` | `mssql` is the SQL container's hostname on the Docker network `bh-ot` |
| Extra properties | `databaseName=ignition;encrypt=true;trustServerCertificate=true` | TLS on, self-signed server certificate accepted (lab) |
| Username | `sa` (lab only) | **Production: use a least-privilege SQL login** owning only the `ignition` database |
| Pool | max active 8, max idle 8, max wait 5000 ms | Raise max active if many sessions run queries at once |
| Validation | `SELECT 1`, test on borrow, every 10 s | |
| Slow query log threshold | 60000 ms | Queries slower than this are logged |
| Failover | none | |

The connection is **not created automatically**: on a new gateway create it in the web UI (or restore a `.gwbk`). Its
name must be exactly `ignition`; the historian, the alarm journal, both audit profiles and every named query use it.

## What Lives In The Database

| Owner | Tables | Created By |
|---|---|---|
| SQL Historian | `sqlth_*`, `sqlt_data_1_YYYY_MM` | the gateway |
| Alarm journal `MSSQL` | `alarm_events`, `alarm_event_data` | the gateway |
| Audit profiles | `ops_audit_events` (OpsAudit), `dev_audit_events` (DevAudit), `audit_events` (unused) | the gateway (`autoCreate`) |
| Ad-hoc trends | `adhoc_trend_configs` | `sql/adhoc_trend_configs.sql` |
| Operations Forms | `ops_form_submission`, `ops_pid_valve`, `ops_pid_cycle`, `ops_pid_check`, `ops_pid_check_log` | `sql/operations_forms.sql` |
| Out Of Service | `oos_record`, `oos_comment` | `sql/out_of_service_log.sql` |
| Report Builder | `report_template`, `report_run` | `sql/report_template.sql`, `sql/report_run.sql` |
| Ticket Logger | `ticket_outbox` | `sql/ticket_outbox.sql` |

Schema details per table: [Database](../database/index.md). The SQL Server side (container, volume, memory cap):
[MSSQL](../infrastructure/mssql.md).

## Drivers And Translators

**Where:** Connections > Databases > Settings (Drivers / Translators tabs). The gateway ships drivers for MariaDB,
Microsoft SQL Server, MySQL, Oracle, PostgreSQL and SQLite, each with a translator (SQL dialect). Only
`Microsoft SQLServer` / `MSSQL` is used.

## Store & Forward

**Where:** Platform > System > Store & Forward (`ignition/store-and-forward-engine/ignition/config.json`).

Store & Forward buffers history, alarm journal and audit writes on disk when the database is slow or down, then
forwards them.

| Setting | Value |
|---|---|
| Forwarding policy | `ALL` |
| Forward rate / batch size | every 1000 ms, up to 10,000 records |
| Data threshold / time threshold | 10,000 records / 30 s |
| Scan rate | 100 ms |
| Primary and secondary maintenance | prevent new data after 1,000,000 records |

The journal (`useStoreAndForward: true`) and audit pipelines go through it; their status tags are under
`[System]Gateway/StoreAndForward/ignition/Pipelines/**` (the Auditing pipeline folder is whitelisted in git).

**If data stops arriving:** check Connections > Databases (status Valid?), then the Store & Forward page for quarantined
records, then `docker logs bh-mssql`.
