---
title: Logging And Diagnostics
sidebar_position: 16
description: Where the gateway logs go, how to read them (web UI, docker logs, system_logs.idb), loggers used by the project, and other diagnostics pages.
sources:
  - gateways/standard/data/logback.xml
  - gateways/standard/data/projects/BH/ignition/script-python/shared/**/code.py
last_verified: 2026-10-24
---

# Logging And Diagnostics

## Reading The Logs

| Method | Command / Location | Best For |
|---|---|---|
| Gateway web UI | Diagnostics > **Logs** | Filtering by logger and level, live tail, changing a logger's level temporarily |
| Docker | `docker logs --tail 200 bh-ignition-standard` (`-f` to follow) | Quick look, startup errors |
| Log database | `/usr/local/bin/ignition/logs/system_logs.idb` (SQLite) **inside the container**, not in the bind mount. Copy it out: `docker cp bh-ignition-standard:/usr/local/bin/ignition/logs/system_logs.idb .` (`wrapper.log` sits next to it) | Searching history; this is where the trial expiry pattern was found |
| REST | `GET /data/api/v1/logs` (token needs read access) | Scripts |

`logback.xml` sends every event to the console (what `docker logs` shows) and, asynchronously, to the SQLite log
database (`DB` appender, queue 100,000).

## Loggers Used By The Project

Project scripts log with `system.util.getLogger("<name>")`. Filter Diagnostics > Logs by these names:

| Logger | From |
|---|---|
| `shared.PlcWriteLock` | Write lock flips: `PLC write lock (flip): Locked=False -> readOnly=False on 37322 tags ...` |
| `shared.Audit` | OpsAudit write failures |
| `shared.Overview` | Overview rebuilds |
| `shared.Integrations` | Monday.com pings (every 300 s) |
| `BH.TicketLogger` | One line per ticket sent: destination, match (Type + Area / Type / Area / Default) and dry run; Oracle-routed tickets go to the `ticket_outbox` table |
| `shared.Security` | Permission refusals: `Denied Pump/Command for '<user>'` (device-type rows) |
| `trend-context`, `AdhocTrend` | Trend zoom events and trend-context fallbacks |
| `shared.Forms`, `shared.OutOfService`, `shared.Reports` | Feature engines |
| `Perspective.*`, `perspective.binding` | Binding and component errors in sessions |

The full list of modules and their loggers is in the generated [Scripting](../scripting/index.md) reference.

## Common Messages

| Message | Meaning |
|---|---|
| `Demo_Expired` → `Demo_Enabled` | The trial was reset by the watcher ([Trial](trial-and-licensing.md)) |
| `ProtoSerializationException`, `No value present`, `NoSuchFileException .../projects/.resources/<hash>` | A project file was damaged (bad merge or hand edit). Restore its last good version from git and reopen the project in the Designer ([Merge Conflicts](../git-workflow/merge-conflicts.md)) |
| `Bad_NotWritable`, `Bad_UserAccessDenied` on `[RCP1]` | The write protection working as intended |
| `Uncertain_LastKnownValue` on RCP1 tags | The driver restarted and is catching up (minutes over SecureLink) |

## Other Diagnostics Pages

| Page | Use |
|---|---|
| Diagnostics > Overview / Metrics Dashboard | CPU, heap, threads, database and device health at a glance |
| Diagnostics > Performance | Heap and CPU graphs |
| Diagnostics > Execution | Scheduled executors (shared and private): what runs how often |
| Diagnostics > Scripts > Running | Currently running gateway scripts; cancel a stuck one |
| Diagnostics > Threads | Thread dump (download it for IA support) |
| Home > Perspective > Sessions | Open HMI sessions, their user, page, and a way to close them |
| Connections > Devices | Device status (Connected, Disconnected, Faulted) |

## Raising A Log Level Temporarily

Diagnostics > Logs > the logger > set level `DEBUG` or `TRACE`. The change lasts until the gateway restarts. Set it
back when done: TRACE on driver loggers floods the log database.
