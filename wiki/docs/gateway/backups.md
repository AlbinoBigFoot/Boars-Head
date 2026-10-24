---
title: Backups
sidebar_position: 15
description: Gateway backups (.gwbk), the config DB autobackups, scheduled backups, the Bors-backups folder, and what each backup does and doesn't contain.
sources:
  - gateways/standard/data/config/resources/core/ignition/system-properties/config.json
  - .gitignore
last_verified: 2026-10-23
---

# Backups

Three different things protect this project. Know which one you need.

| What | Contains | Where |
|---|---|---|
| **Git** | Project `BH`, themes, icons, UDTs, whitelisted tag folders, tag groups `RCP1_*`/`PAX_*`, audit profiles, co-branding | GitHub `AlbinoBigFoot/Boars-Head` |
| **Gateway backup `.gwbk`** | The whole gateway: every project, every tag, devices, database connections, users, security, modules' config, OPC certificates | A file you download; never committed (`*.gwbk` is not to be committed) |
| **MSSQL data** | History, alarm journal, audit, forms, Out Of Service, report templates, trend configs | Docker volume `bh-mssql-data`; back up with SQL Server tools |

A `.gwbk` does **not** contain the SQL data, and git does not contain the gateway's secrets, `_RCP1_` tags or device
config. A full restore needs both a `.gwbk` and a database backup.

## Taking A Gateway Backup

**Where:** Platform > System > **Backup & Restore** > Backup tab. Click **Download Backup**; the file is named like
`bh-standard_Ignition-backup-standard<timestamp>.gwbk`.

When to take one:
- before any gateway restart you're unsure about, a module upgrade, or an Ignition upgrade;
- before bulk tag operations (`_RCP1_` prune, UDT restructures);
- before and after a production deployment.

Keep them outside the repo, e.g. `C:\Users\<you>\Documents\Bors-backups\` (a folder outside the repo, so a backup
is never committed by accident).

## Scheduled Backups

**Where:** Platform > System > Gateway Settings > Scheduled Backups. Current setting: **off**
(`scheduledBackupsEnabled: false`); prepared values: daily at 01:15 (`15 1 * * *`), keep 5, file name
`${gatewayName}_Ignition-backup-${edition}${timestamp}.gwbk`, no path set. Production should turn this on with a path
on a backed-up share.

## Config DB Autobackups

The gateway keeps copies of its internal config database in `gateways/standard/data/db/autobackup/`
(`configdb_YYYYMMDD_HHMMSS.idb`, written before migrations and at intervals). Not tracked. They are a last resort
after a corrupted `config.idb`; restoring one means stopping the gateway and swapping the file.

## Restoring

1. Platform > System > Backup & Restore > **Restore** tab, choose the `.gwbk`.
2. The gateway restarts with the backup's configuration. On this lab the restore also rewrites the bind-mounted files,
   so `git status` will show differences against `main`: review them before keeping or discarding.
3. Re-check: RCP1 device status, the `ignition` database connection (status Valid), the trial, the RCP1 write block
   (confirm with the system integrator) and `[default]_Config/PlcWriteLock/Locked = true`.

## Tag-Only Backups

For tag work, export JSON instead of a full `.gwbk`: Designer Tag Browser > right-click a folder > **Export Tags**
(JSON). Take one before any bulk tag change.
