---
title: Gateway UI Map
sidebar_position: 1
description: Where every setting used by this project lives in the Ignition 8.3 Gateway web UI, and its file in the repo.
sources:
  - gateways/standard/data/config/resources/core/**/config.json
last_verified: 2026-10-23
---

# Gateway UI Map

The Ignition 8.3 Gateway web UI (http://localhost:19088, Administrator login) has six sections in the left rail.
The menu below was read from the live gateway (`/data/app/navigation`, 2026-10-23). Every page also has a direct URL
under `http://localhost:19088/app/...`, and the **Search Gateway** box at the top finds settings by name.

![Connections > Devices > Connections in the 8.3 Gateway web UI](/img/gateway/device-connections.png)

## Settings Used By This Project

| Setting | UI Location | URL (`/app` + ...) | File (under `config/resources/core/`) |
|---|---|---|---|
| Gateway name, backups schedule, Designer RAM | Platform > System > Gateway Settings | `/platform/system/gateway/settings` | `ignition/system-properties/config.json` |
| Projects (`BH`, `Lightspeed-FrontEnd`) | Platform > System > Projects | `/platform/system/projects` | `projects/` (outside `config/`) |
| Modules | Platform > System > Modules | `/platform/system/modules` | `data/modules.json` |
| License / trial | Platform > System > Licensing | `/platform/system/licensing` | `local/ignition/local-system-properties` |
| Store & Forward | Platform > System > Store & Forward | `/platform/system/store-and-forward` | `ignition/store-and-forward-engine/ignition/` |
| Backup / restore | Platform > System > Backup & Restore | `/platform/system/backup-restore/backup` | n/a |
| Gateway / Designer permissions, audit profile, system IdP | Platform > Security > General Settings | `/platform/security/settings` | `ignition/security-properties/config.json` |
| Users and roles | Platform > Security > User Sources | `/platform/security/user-sources` | `ignition/user-source/default/` (`users.json`) |
| Identity providers (`default`, `Lightspeed`, `temp`) | Platform > Security > Identity Providers | `/platform/security/idps` | `ignition/identity-provider/*/` |
| Audit profiles (`DevAudit`, `OpsAudit`) | Platform > Security > Audit Profiles | `/platform/security/audit-profiles` | `ignition/audit-profile/*/` |
| Security levels | Platform > Security > Levels | `/platform/security/levels` | `ignition/security-levels/config.json` |
| Security zones (`Default`) | Platform > Security > Zones | `/platform/security/zones` | `ignition/security-zone/Default/` |
| API keys (`Access`) | Platform > Security > API Keys | `/platform/security/api-keys` | `ignition/api-token/Access/` |
| PLC device `RCP1` | Connections > Devices > Connections | `/connections/devices` | `com.inductiveautomation.opcua/device/RCP1/` |
| Database `ignition` | Connections > Databases > Connections | `/connections/databases` | `ignition/database-connection/ignition/` |
| JDBC drivers, translators | Connections > Databases > Settings | `/connections/databases/settings/drivers-jdbc` | `ignition/database-driver/*`, `database-translator/*` |
| OPC UA server | Connections > OPC > OPC UA Server Settings > General Settings | `/opc/server-settings` | `com.inductiveautomation.opcua/server-config/` |
| OPC UA default permissions | Connections > OPC > OPC UA Server Settings > Permissions | `/opc/permissions-settings` | `com.inductiveautomation.opcua/access-control/` |
| OPC client connection | Connections > OPC > Connections | `/connections/opc-client-connections` | `ignition/opc-connection/Ignition OPC UA Server/` |
| OPC certificates | Connections > OPC > Security (Client / Server tabs) | `/connections/opc/security/client` | `local/com.inductiveautomation.opcua/*-keystore` |
| OPC Quick Client (browse/read) | Connections > OPC > Quick Client | `/connections/quick-client` | n/a |
| Gateway network | Network > Gateway Network > Settings / Connections | `/network/gateway/settings` | `ignition/gateway-network-settings/` |
| Enterprise Administration | Network > Enterprise > Configure | `/network/eam/configure` | `com.inductiveautomation.eam/*` |
| Historian `historian` | Services > Historians > Historians | `/services/historian/providers` | `com.inductiveautomation.historian/historian-provider/historian/` |
| Tag providers | Services > Tags | `/services/tags` | `ignition/tag-provider/*/` |
| Alarm settings | Services > Alarming > Settings | `/services/alarming/settings` | `ignition/general-alarm-settings/` |
| Alarm journal `MSSQL` | Services > Alarming > Journals | `/services/alarming/journals` | `ignition/alarm-journal/MSSQL/` |
| Alarm schedules | Services > Alarming > Scheduling | `/services/alarming/scheduling/schedules` | `ignition/schedule/Example/` |
| Perspective co-branding | Home > Perspective > Brand Settings | `/home/perspective/branding` | `ignition/cobranding/config.json` |
| Perspective sessions | Home > Perspective > Sessions | `/home/perspective/sessions` | n/a (runtime) |
| Designer Launcher | Home > Designer > Download | `/home/designer/download` | n/a |
| Logs | Diagnostics > Logs | `/diagnostics/logs` | container `/usr/local/bin/ignition/logs/system_logs.idb` |
| Running scripts, gateway scripts | Diagnostics > Scripts | `/diagnostics/scripts/running` | n/a |
| Threads, performance, metrics | Diagnostics > Threads / Performance / Metrics Dashboard | `/diagnostics/threads` | n/a |

## Settings That Are Not In The Web UI

| Setting | Where It Is Instead |
|---|---|
| **Tag groups** | Designer: Tag Browser > **Edit Tag Groups** (clock icon). Files `ignition/tag-group/<provider>/<group>/config.json` |
| **UDT definitions, tags** | Designer Tag Browser; files `tag-type-definition/**`, `tag-definition/**` |
| **Per-device OPC UA role permissions** (the RCP1 write block) | Not shown in 8.3.7. Only through the resource REST API; see [RCP1 Device](devices-rcp1.md#layer-2-opc-ua-server-block) |
| **Gateway event scripts** | Designer: Project Browser > Scripting > Gateway Events (per project) |
| **Heap size** | Container start argument `-m` from `STANDARD_MAX_MEMORY_MB` in `.env` |

## The Whole Menu

<details>
<summary>All six sections as of 8.3.7</summary>

- **Home**: Welcome; Designer (Download, Connections); Perspective (Launch, Download, Sessions, Brand Settings);
  Vision (Launch, Download, Clients)
- **Platform**: Overview; System (Gateway Settings, Projects, Modules, Licensing, Redundancy, Modes, Store & Forward,
  Ignition Exchange, Backup & Restore); Security (General Settings, User Sources, Identity Providers, Secret Providers,
  Audit Profiles, Levels, Zones, API Keys, OAuth2 Clients)
- **Connections**: Overview; Devices (Settings, Connections); Databases (Settings, Connections); Service Connectors
  (Connections); OPC (OPC UA Server Settings, Security, Connections, Quick Client)
- **Network**: Overview; Network Settings (Web Server, Email Settings); Gateway Network (Settings, Connections);
  Enterprise (Configure)
- **Services**: Overview; Historians; Tags; Alarming (Settings, Pipelines, Journals, Notification, Rosters, Manage
  Scripts, Scheduling); Reports; SFCs (Settings, Charts); Transaction Groups; Event Streams
- **Diagnostics**: Overview; Metrics Dashboard; Logs; Execution (Shared, Private); Performance; Scripts (Running,
  Gateway Scripts: Startup / Update ...); Threads

</details>
