---
title: Glossary
sidebar_position: 6
description: Ignition, PlantPAx, refrigeration and project jargon used throughout the wiki.
sources:
  - docs/plc-write-lock.md
  - docs/rcp1-pax-inventory.md
  - docs/ignition-resource-signatures.md
last_verified: 2026-10-23
---

# Glossary

## Ignition

| Term | Meaning |
|---|---|
| **Gateway** | The Ignition server process. Runs tags, drivers, scripts, history and serves Perspective. Here: container `bh-ignition-standard`, system name `bh-standard` |
| **Gateway web UI** | The browser admin console at `http://localhost:19088` (sections Home, Platform, Connections, Network, Services, Diagnostics in 8.3) |
| **Designer** | The desktop IDE (launched through the Designer Launcher) for editing projects and tags |
| **Project** | A set of resources (views, scripts, queries ...). Ours is **`BH`**. `Lightspeed-FrontEnd` is a reference project copied from another job and not part of the deliverable |
| **Resource** | One unit of project or gateway config: a folder with `resource.json` (metadata) plus content files such as `view.json`, `code.py`, `config.json` |
| **Resource signature** | `attributes.lastModificationSignature` in `resource.json`: a SHA-256 over the resource's metadata and content digests. Disk edits without repairing it break the Designer (`ProtoSerializationException`) |
| **CAS / `.resources`** | Content-addressed store `projects/.resources/<sha256>`: the gateway keeps a copy of each content file under its hash. The gateway rewrites it constantly; never commit that churn |
| **Scan** | `POST /data/api/v1/scan/projects` or `/scan/config`: tells the gateway to reload resources changed on disk |
| **Perspective** | Ignition's web HMI module. Sessions run in a browser at `/data/perspective/client/BH` |
| **View** | A Perspective screen or component (`view.json`). Pages, docks, popups and embedded components are all views |
| **Page / route** | A URL (`/cg-e2`) mapped to a primary view in `page-config` |
| **Dock** | A view docked to a page edge (header top, navigation left, legend right) |
| **Faceplate** | A popup that shows one device's detail and controls (`01_Popups/00_Faceplates/...`), opened with `shared.Alerts.showFaceplate` |
| **Binding** | A live link from a component property to a tag, expression, property, query or script |
| **Expression / expression structure** | Ignition's formula language. Expression structure (`expr-struct`) bindings evaluate several named expressions. Preferred over scripts |
| **Transform** | A post-processing step on a binding result (map, format, expression, script) |
| **Style class** | A named, reusable Perspective style (Project Browser > Perspective > Styles) |
| **Advanced Stylesheet** | The project-wide `stylesheet.css` for rules style classes can't express |
| **Theme** | Gateway-level CSS variables (`light-cool`, `dark-cool` ...), chosen per session by `session.props.theme` |
| **Tag** | A named data point. **OPC tag**: reads a device address. **Memory tag**: holds a value. **Expression tag**: computed. **Reference tag**: points at another tag. **Query tag**: SQL |
| **Tag provider** | A tag namespace. `[default]` (standard provider, about 88,000 tags) and `[System]` (gateway-managed) |
| **UDT** | User Defined Type: a tag template (definition under `_types_`), instantiated for each device. UDTs can nest other UDTs |
| **Tag group** | The scan class that decides how often OPC tags are polled. **Direct**: always at its rate. **Leased**: fast only while someone (a screen) subscribes, otherwise at its slow rate (or not at all when the rate is 0) |
| **Tag historian / SQL Historian** | Stores tag value history in SQL. Our provider is named `historian` |
| **Alarm journal** | SQL record of alarm events (`alarm_events`, `alarm_event_data`), profile `MSSQL` |
| **Audit profile** | Where audit events go: `DevAudit` (gateway/Designer changes) and `OpsAudit` (operator actions) |
| **Named query** | A SQL query stored as a project resource and called by name with parameters |
| **Gateway event script** | Script that runs on the gateway: tag change, timer, startup/shutdown, message handler |
| **Integration Toolkit** | Third-party module (Automation Professionals) adding expression functions such as `tag()`, `try()`, `isGood()` |
| **ApexCharts** | Third-party Perspective chart component (Kyvis Labs), used for most charts |
| **.gwbk** | A full gateway backup file |
| **Trend basket** | `session.custom.AdhocTrend`: the list of pens (historized tags) a session is trending. "Add To Trend" right-click menus add to it; the Trending page and the trend faceplate read it ([Trending](../features/trending.md)) |
| **Historized** | A tag with History enabled, so the SQL Historian stores its values; only historized tags can be trended |
| **Trial** | Unlicensed Ignition runs for 2 hours at a time; `ignition-trial-watch` resets it |

## PLC And PlantPAx

| Term | Meaning |
|---|---|
| **RCP1** | The plant's ControlLogix PLC (Refrigeration Control Panel 1). Gateway device name `RCP1`, Logix driver |
| **`[RCP1]`** | The OPC address prefix of that device, e.g. `ns=1;s=[RCP1]Controller:Global/...` |
| **`_RCP1_`** | Tag folder `[default]_RCP1_`: the browsed, pruned controller tags (about 35,000), all read only |
| **PlantPAx / PAX** | Rockwell's Process Library. Its objects (`P_Motor`, `P_AIn`, `P_DIn`, `P_ValveSO`, `P_Intlk`, `P_RunTime`, `P_Alarm`) are UDTs in the PLC; we mirror them as Ignition UDTs under `_types_/PLC` |
| **PAX mapping** | The device-by-device work of pointing HMI device UDTs at their real PlantPAx objects (`docs/pax-mapping/`) |
| **`Sts_*`, `Val_*`, `Cfg_*`, `PCmd_*`, `OCmd_*`** | PlantPAx member prefixes: status, value, configuration, program command, operator command |
| **L5K / L5X** | Studio 5000 project exports, used to read UDT definitions and descriptions |
| **FT / FactoryTalk View SE** | The old HMI being replaced. "FT parity" = same information as the FT screen |
| **SecureLink** | The remote-access VPN used to reach the plant network from the lab |
| **PLC write lock** | `[default]_Config/PlcWriteLock/Locked` (default `true`): sets `readOnly` on every tag that reads RCP1 |
| **OPC write block** | `rolePermissionMappings` on the RCP1 device: the OPC UA server refuses every write to it |

## Refrigeration And Plant

| Term | Meaning |
|---|---|
| **NH3** | Ammonia, the refrigerant |
| **CG** | Control Group: one evaporator coil group (CG-A1 ... CG-G5, 19 of them) with its fans and valves |
| **Evaporator** | Cools a room; modes Cooling (CLG), Defrost (DFT), Idle, Stop, Fault (FLT) |
| **Compressor** | Screw compressors COMP 1, 4, 5, 6, 7 in the Machine Room |
| **Condenser** | Rejects heat outdoors; EC fans, sump pumps, the CSV tank |
| **HTR / LTR / HPR / CSV** | High-Temperature Recirculator, Low-Temperature Recirculator, High-Pressure Receiver, Condenser Sump Vessel (tanks) |
| **HLCO / OPL / LOLO** | Tank level switches: High Level Cut-Out, Operating Level, Low-Low |
| **ZAT** | Zone Air Temperature |
| **Machine Room** | The compressor/vessel room; page `/machine-room` |
| **Utility Overview** | The plant floor plan with every CG; the local home page |
| **Out Of Service (OOS)** | A device taken out of service with a memo (`<device>.Enabled = false`) |
| **Level switch tile** | The small status tile for a tank's HLCO / HI LEVEL / OPL / LOLO LEVEL input (a P_DIn object), on the Machine Room page and on the Tank faceplate ([Level Switches](../features/machine-room-level-switches.md)) |
| **PLC Overview / rack** | Groveport > Operations > PLCs: one card per PLC, then the read-only drawing of its local I/O cards ([PLC Rack / IO](../features/plc-rack-io.md)) |
| **Areas** | Freezer, SuperChill, Club, Palletizing, East PH, West PH, Dock, Machine Room, Condensers |

## Project Shorthand

| Term | Meaning |
|---|---|
| **Local Groveport mode / enterprise mode** | The two nav/route modes behind `[default]_Config/DemoEnterpriseNav` |
| **Permission matrix** | The DataSet tag `[default]_Config/RolesPermissions`: one row per Device / Action, one tick column per role; edited on Admin > Roles & Permissions ([Roles & Permissions](../features/roles-permissions.md)) |
| **Handoff** | `docs/handoff/HANDOFF.md`, the running session log (local only) |
| **One Shot** | One Shot Automation, the integrator (also the `OneShot` role) |
