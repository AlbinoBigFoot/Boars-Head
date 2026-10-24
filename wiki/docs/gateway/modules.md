---
title: Modules
sidebar_position: 13
description: The 34 modules installed on bh-standard, which ones the BH project actually depends on, and the third-party ones.
sources:
  - gateways/standard/data/modules.json
last_verified: 2026-10-24
---

# Modules

**Where:** Platform > System > Modules (`gateways/standard/data/modules.json` lists file names and startup state;
the `.modl` files live in the image and `data/var/ignition/modl/`).

## Required By The BH Project

| Module | ID | Used For |
|---|---|---|
| **Perspective** | `com.inductiveautomation.perspective` | The whole HMI |
| **Reporting** | `com.inductiveautomation.reporting` | Operations Forms PDFs (`OpsForms/*`), Report Builder PDF (`Reports/CustomReport`) |
| **WebDev** | `com.inductiveautomation.webdev` | The enterprise globe page (`globe/map`, `globe/mapMarkers`) and the PLC Rack 3D page (`rack3d/*`); both login-gated |
| **Historian** + **SQL Historian** | `com.inductiveautomation.historian`, `.historian.sql` | Tag history provider `historian` |
| **OPC-UA** | `com.inductiveautomation.opcua` | OPC UA server + client; hosts the drivers |
| **Logix Driver** | `com.inductiveautomation.opcua.drivers.logix` | The `RCP1` device |
| **MSSQL JDBC Driver** | `com.inductiveautomation.jdbc.mssql` | The `ignition` database connection |
| **Integration Toolkit** 2.1.5 (Automation Professionals, third party) | `com.automation_pros.simaids` | Expression functions `tag()`, `try()`, `isGood()`, `isBadOrError()`, `coalesce()` used across bindings. Free |
| **ApexCharts** 2.0.1 (Kyvis Labs, third party) | `com.kyvislabs.apexcharts` | The `kyvislabs.display.apexchart` component (most charts). Its certificate and EULA are accepted under `com.inductiveautomation.eam/module-certificates` and `module-eulas` |

Without Integration Toolkit, many bindings fail with "function not found". Without ApexCharts, charts render as
missing components. Install both on any new gateway **before** importing the project.

## Installed But Not Used By BH

Alarm Notification, SMS Notification, Voice Notification, Kafka Connector, EventStream, Enterprise Administration
(EAM), SFC, SQL Bridge (transaction groups), Symbol Factory, Vision, MariaDB and PostgreSQL JDBC drivers, and the
drivers BACnet, DNP3 (v1 and v2), IEC 61850, Micro800, Mitsubishi, Modbus v2, Omron, Siemens, Siemens Enhanced, UDP/TCP,
Allen-Bradley legacy (`ablegacy`). They come with the full Ignition image. On a production gateway you can leave them
installed (unlicensed modules only matter if used) or remove them to shorten startup.

## Version Check

Every module reports `ACTIVE` and license state `Trial` (REST: `GET /data/api/v1/modules/healthy`). The Inductive
modules are versioned with the platform (8.3.7, build b2026060908). Third-party modules must be the **8.3 builds**
(`-v83`): an 8.1 build won't load on 8.3.
