---
title: Gateway
description: Everything configured on the Ignition Standard gateway bh-standard, with links to each setting's page.
sources:
  - gateways/standard/data/config/resources/core/**/config.json
  - gateways/standard/data/modules.json
  - docker-compose.yml
last_verified: 2026-10-24
---

# Gateway

The lab's primary gateway is **`bh-standard`**: Ignition **8.3.7 (b2026060908)**, Standard edition, Java 17, time zone
`America/New_York`, running in the container `bh-ignition-standard` at **http://localhost:19088**. It hosts the `BH`
project and every service the HMI uses.

## How 8.3 Stores Gateway Settings

Ignition 8.3 keeps gateway configuration as **resource files** under `data/config/resources/`, in collections:

| Collection | Path | Holds |
|---|---|---|
| `core` | `config/resources/core/<module>/<type>/<name>/config.json` | Almost everything: devices, tag providers, tag groups, databases, historian, journals, audit profiles, users, security, themes |
| `local` | `config/resources/local/...` | Per-machine items that must not be copied to another gateway: OPC UA keystores, the gateway UUID, trial time remaining |
| `external` | `config/resources/external/` | Resources managed from outside (empty here) |

Because the data folder is bind-mounted from the repo (`gateways/standard/data`), you can **read** every setting as
JSON. Change them through the Gateway web UI or the Designer; don't hand-edit `config.json`, because the
`resource.json` metadata would no longer match (same rule as for project files). Secrets inside these files
(database password, OPC user password, keystore passwords) are stored encrypted, and most of these folders are
gitignored.

## Map Of The Gateway

| Area | Configured Item | Page |
|---|---|---|
| Connections > Devices | `RCP1` Allen-Bradley Logix driver, with the OPC UA write block | [RCP1 Device And Write Protection](devices-rcp1.md) |
| Connections > OPC | OPC UA server (port 62541, localhost only), the loopback client connection `Ignition OPC UA Server`, default permissions | [OPC UA](opc-ua.md) |
| Services > Tags; Designer tag groups | Providers `default` and `System`; tag groups `Default`, `Default Historical`, `RCP1_Status`, `RCP1_Faceplate`, `PAX_Status`, `PAX_Faceplate`, `PAX_Config` | [Tag Providers And Tag Groups](tag-providers-and-groups.md) |
| Services > Historians | SQL Historian `historian` on database `ignition` | [Historian](historian.md) |
| Connections > Databases | Connection `ignition` (MSSQL), JDBC drivers, translators; Store & Forward engine | [Databases And Store & Forward](databases.md) |
| Services > Alarming | Journal `MSSQL`, general alarm settings | [Alarming](alarming.md) |
| Platform > Security > Audit Profiles | `DevAudit`, `OpsAudit` | [Audit Profiles](audit-profiles.md) |
| Platform > Security | User sources `default` and `opcua-module`, identity providers, security levels, zone `Default`, API key `Access` | [Security](security.md) |
| Home > Perspective > Brand Settings | Login and loading screen co-branding | [Perspective Co-Branding](cobranding.md) |
| Designer > Project Browser > Web Dev | WebDev resources `globe/*` and `rack3d/*` (login-gated, see [Security](security.md)) | [Gateway Event Scripts](event-scripts.md) |
| Designer > Gateway Events | Tag change scripts and timers of project `BH` | [Gateway Event Scripts](event-scripts.md) |
| Platform > System > Licensing | Trial mode, the trial watcher | [Trial And Licensing](trial-and-licensing.md) |
| Platform > System > Modules | 34 modules incl. Perspective, Reporting, WebDev, SQL Historian, Logix, Integration Toolkit, ApexCharts | [Modules](modules.md) |
| `-m` start argument, `ignition.conf` | Heap 5120 MB live (6144 default), Designer 4 GB | [Memory And Performance](memory-and-performance.md) |
| Platform > System > Backup & Restore | `.gwbk` backups, config DB autobackups | [Backups](backups.md) |
| Diagnostics | Logs, threads, performance, running scripts | [Logging And Diagnostics](logging-diagnostics.md) |
| REST API `/data/api/v1` | Scans, resources, tags, trial | [REST API](rest-api.md) |
| Network, Redundancy, EAM, Edge sync | Gateway network, Enterprise Administration, schedules | [Other Gateway Settings](other-settings.md) |
| Everything above | Where each one lives in the 8.3 web UI | [Gateway UI Map](gateway-ui-map.md) |

## The Second Gateway

An optional **Ignition Edge** gateway (`bh-ignition-edge`, http://localhost:19188) shares the stack. It is not part of
the running lab today; it is the planned home of the local Groveport deployment. See
[Edge Gateway](../infrastructure/edge-gateway.md) and [The Edge Move](../deployment/edge-move.md).
