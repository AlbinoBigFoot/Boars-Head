---
title: Database Operations
sidebar_label: Operations
sidebar_position: 4
description: Querying the BH database safely, retention, backups (none yet), recreating the schema on a new server, and removing test data.
sources:
  - sql/*.sql
  - docker-compose.yml
  - .env.example
last_verified: 2026-10-24
---

# Database Operations

## Query it (read only)

From the host with any SQL client: server `localhost,11433`, database `ignition`, user `sa`, password from your
local `.env`. Or inside the container, without typing the password (it is read from the container's environment):

```bash
docker exec -it bh-mssql sh -c '/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "$MSSQL_SA_PASSWORD" -C -d ignition -W -s "|" -Q "SELECT TOP 20 * FROM dbo.oos_record ORDER BY id DESC"'
```

`-C` trusts the self-signed certificate; `-I` (quoted identifiers) is needed when you **apply** the schema files
(filtered indexes require it). From PowerShell keep the inner command simple (PowerShell mangles parentheses in
quoted `sh -c` strings); put longer SQL in a file, `docker cp` it into the container and run `sqlcmd -i`.

Never paste the password into docs, tickets or commits.

## Retention

| Data | Retention today | Notes |
|---|---|---|
| Historian samples | **2 years** (pruning on) | monthly partitions, about 50-85 M rows per month |
| Alarm journal | **1 year** (pruning on) | 1.1 M events in three months |
| `ops_audit_events`, `dev_audit_events` | 90 days (profile pruning) | an audit trail older than 90 days is lost; raise `retentionDays` if the site needs longer |
| Our tables (forms, OOS, templates, trends) | forever | small; `report_run` can be purged freely |

Before production, decide retention with the site (regulatory needs for the NH3 forms and audit trail) and change
the pruning ages of the historian and journal in the Gateway web UI if needed.

## Backups

:::danger No database backup exists (2026-10-23)
The database is in the **FULL** recovery model and `msdb` shows **no backup ever taken**. The data lives only in
the Docker named volume `bh-mssql-data`. A `docker volume rm`, a Docker Desktop reset or a disk failure loses all
forms, Out Of Service history, templates, audit trail, alarm journal and history. FULL recovery without log
backups also lets the transaction log grow without bound (0.8 GB now).
:::

Minimum to add before go-live:

```sql
-- inside bh-mssql (sqlcmd -I), to a folder you then copy off the container
BACKUP DATABASE ignition TO DISK = N'/var/opt/mssql/backup/ignition_full.bak' WITH INIT, COMPRESSION;
BACKUP LOG ignition TO DISK = N'/var/opt/mssql/backup/ignition_log.trn' WITH INIT;   -- if staying in FULL
```

Schedule it (SQL Agent is not enabled in the container image by default; a host scheduled task running the
`docker exec ... sqlcmd` command works), copy the files off the machine, and test a restore. Alternatively switch
to `SIMPLE` recovery if point-in-time restore is not needed. The Ignition gateway backup (`.gwbk`) does **not**
contain SQL data.

## Recreate the schema on a new server

1. Create the database `ignition` (and a login for the gateway; production should not use `sa`).
2. Apply our tables (each file is idempotent):

   Run `sql/adhoc_trend_configs.sql`, `sql/operations_forms.sql`, `sql/out_of_service_log.sql`,
   `sql/report_template.sql`, `sql/report_run.sql` and `sql/ticket_outbox.sql` with SSMS / Azure Data Studio, or with
   `sqlcmd -I -d ignition -i <file>` inside `bh-mssql` (`-I` turns QUOTED_IDENTIFIER on, which the filtered indexes
   need). The P&ID valve list (`ops_pid_valve`, 725 rows from the Annual P&ID Verification workbook) is not in the
   SQL file: copy it from the existing database, or ask the system integrator to load it.
3. In the Gateway web UI create the connection **`ignition`** (Config > Databases > Connections), then the alarm
   journal profile **`MSSQL`**, the audit profiles **`OpsAudit`** (table `ops_audit_events`) and **`DevAudit`**,
   and the SQL historian. Ignition creates their tables itself (`autoCreate`).
4. Check: Operations > Out Of Service Log loads, a test form submits, Alarm Journal shows events, the Audit Log
   shows the test write.

## Remove test data

Test rows entered while commissioning are marked "TEST". Remove them when no longer wanted:

```sql
DELETE FROM dbo.ops_form_submission WHERE id IN (1, 2, 3) AND submitted_name LIKE 'TEST%';
DELETE FROM dbo.oos_record WHERE taken_name LIKE N'TEST%';          -- comments cascade
DELETE FROM dbo.report_template WHERE name LIKE N'TEST%';
```

Check the row counts with a `SELECT` using the same `WHERE` first.
