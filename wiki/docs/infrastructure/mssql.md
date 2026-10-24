---
title: MSSQL
sidebar_position: 5
description: The SQL Server 2022 container, the ignition database and its tables, memory cap, connecting from tools, schema scripts and backups.
sources:
  - docker-compose.yml
  - sql/*.sql
last_verified: 2026-10-24
---

# MSSQL

| Item | Value |
|---|---|
| Container | `bh-mssql`, image `mcr.microsoft.com/mssql/server:2022-latest`, Developer edition |
| From the host | `localhost,11433` (SSMS / Azure Data Studio, SQL authentication) |
| From containers | `mssql:1433` (the gateway uses this) |
| Database | **`ignition`** |
| Data | named volume `bh-mssql-data` (not in git) |
| Login | `sa` with `MSSQL_SA_PASSWORD` from `.env` (lab only) |
| Memory cap | 2048 MB (`max server memory`, persists in the volume) |

## Tables

| Group | Tables | Details |
|---|---|---|
| Historian | `sqlth_te`, `sqlth_partitions`, `sqlth_sce`, `sqlth_scinfo`, `sqlth_drv`, `sqlth_annotations`, `sqlt_data_1_YYYY_MM` | [Historian](../gateway/historian.md) |
| Alarm journal | `alarm_events`, `alarm_event_data` | [Alarming](../gateway/alarming.md) |
| Audit | `ops_audit_events`, `dev_audit_events`, `audit_events` | [Audit Profiles](../gateway/audit-profiles.md) |
| Project | `adhoc_trend_configs`, `ops_form_submission`, `ops_pid_*`, `oos_record`, `oos_comment`, `report_template`, `report_run`, `ticket_outbox` | [Database](../database/index.md) |

## Running SQL

Without a password on the command line, using the container's own environment variable:

```powershell
docker exec bh-mssql sh -c '/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -C -d ignition -Q "SELECT COUNT(*) FROM dbo.oos_record"'
```

Apply a schema script (note **`-I`**, QUOTED_IDENTIFIER ON, required for the filtered indexes):

```powershell
Get-Content sql\out_of_service_log.sql | docker exec -i bh-mssql sh -c '/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -C -I -d ignition'
```

`-C` trusts the self-signed server certificate. The scripts in `sql/` are idempotent where possible (create if not
exists); read each before running it on a database with data.

## Memory

```sql
EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
EXEC sp_configure 'max server memory (MB)', 2048; RECONFIGURE;
```

Without the cap SQL Server grows until WSL runs out of memory.

## Backups

The volume is the only copy of history, journal and project data. Back it up with SQL Server itself:

```powershell
docker exec bh-mssql sh -c '/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -C -Q "BACKUP DATABASE ignition TO DISK=''/var/opt/mssql/backup/ignition.bak'' WITH INIT"'
docker cp bh-mssql:/var/opt/mssql/backup/ignition.bak C:\Users\<you>\Documents\Bors-backups\
```

The history tables are large (tens of millions of rows per month), so expect a multi-GB file.

## Production

Use a managed SQL Server, a dedicated least-privilege login for the gateway (owner of `ignition` only), regular
backups, and enable historian and journal pruning.
