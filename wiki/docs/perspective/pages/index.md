---
title: Page Guides
sidebar_label: Overview
sidebar_position: 1
description: A guide per main BH page - what it shows, where its data comes from, and the bindings that matter.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/page-config/config.json"
last_verified: 2026-10-24
---

# Page Guides

One guide per main page (or family of pages) of the BH HMI. Each guide says **what the page shows**, **where the
data comes from** (tag paths, UDT members, SQL), and the **bindings** you need
to know before changing it. For the full, generated detail of a view (every component and binding) follow the
reference links.

Screenshots are from the lab gateway (local Groveport mode, light-cool theme, 1600 x 900), taken read-only on
2026-10-23. Values are live lab values.

| Guide | Routes | Main view |
|---|---|---|
| [Utility Overview](./utility-overview.md) | `/`, `/plants/groveport/utility-overview` | `00_Pages/Groveport/Utility/Overview` |
| [CG Pages](./cg-pages.md) | `/cg-a1` ... `/cg-g5` (19 pages) | `00_Pages/Groveport/<Area>/Utility/CG-xx` + `_Shared/CG/*` |
| [Machine Room](./machine-room.md) | `/machine-room` | `00_Pages/Groveport/Machine Room/Utility/Overview` |
| [Condensers](./condensers.md) | `/condensers` | `00_Pages/Groveport/Condensers/Utility/Overview` |
| [Device List Pages](./device-lists.md) | `/pumps`, `/valves`, `/tanks`, `/sensors`, `/compressors`, `/exhaust-fans`, `/condensers/*` | `.../<Type>/Overview` + `Boars Head/<Type>/Details` / `Design` |
| [Safety Relay And Rupture Disks](./safeties.md) | `/safety-relay`, `/rupture-disks` | `Machine Room/Utility/SafetyRelay`, `RuptureDisks` |
| [Alarm Status And Journal](./alarms.md) | `/alarms`, `/alarms/journal` | `00_Pages/Boars Head/Alarms/*` |
| [Trending](./trending.md) | `/trending`, `/trending/saved` (tool row v2) | `98_Configuration/AdhocTrend/*` |
| [Out Of Service Log](./out-of-service.md) | `/operations/out-of-service[/:device]` | `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` |
| [Operations Forms](./forms.md) | `/operations/forms/*` | `00_Pages/Groveport/Operations/Forms/*` |
| [Report Builder](./report-builder.md) | popup; pages `/operations/reports` (Report Builder) and `/operations/reports/saved` (Saved Reports) | `01_Popups/Reports/ReportBuilder` |
| [PLC Rack](./plc-rack.md) | `/operations/plcs` (overview), `/operations/plcs/:plc`, `/operations/plcs/:plc/3d`, `/plc-rack` | `00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview` |
| [Admin Pages](./admin.md) | `/operations/audit`, `/operations/users`, `/operations/roles-permissions` | `00_Pages/Boars Head/Operations/*` |
| [Enterprise Demo Pages](./enterprise.md) | `/enterprise`, `/plants/...` | hidden in local mode |

## Patterns Shared By Most Pages

- **Root class `bg-page`** for the themed page background.
- **Scale to fit.** The drawn pages (Utility Overview, Machine Room, Condensers, CG pages) are coordinate
  containers drawn at a fixed design size. An expr-struct binding on the root's style passes the page size
  (`page.props.dimensions.primaryView`) to `shared.Scale.cssTransform`, which returns a CSS `transform: scale(...)`
  so the drawing fills the screen without scrollbars.
- **Device graphics** are embedded views of `02_Components/01_Devices/*` with a `tagPath` param pointing at a UDT
  instance under `[default]Boars_Head/GrovePort/<Area>/...`. A click opens the faceplate (see
  [Faceplates](../faceplates.md)).
- **Ticket Logger right-click menu.** Almost every view root carries the same `meta.contextMenu` bindings and a
  page-scoped `ticketLog` message handler that calls `shared.Alerts.contextMenuTicketLog`. These are shown once on
  [Common Binding Patterns](../reference/common-patterns.md).
- **Add To Trend right-click** on historized values (project-wide trend context menu, `shared.TrendContext`). See [Trending](./trending.md).
