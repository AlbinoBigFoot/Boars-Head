---
title: Perspective Project Overview
sidebar_label: Overview
sidebar_position: 1
description: How the BH Perspective project is laid out - view folders, page routes, docks, session properties and events - and how to find a view from a URL and back.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/page-config/config.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-permissions/data.bin"
last_verified: 2026-10-24
---

# Perspective Project Overview

The HMI that operators use is one Ignition **Perspective** project called **`BH`**. Perspective is Ignition's
web-based HMI module: every screen is a **view** (a JSON document of components), views are reached through
**page routes** (URLs), and each browser tab is a **session** with its own session properties.

This page explains how the BH project is organised, so you know where to look before you open the Designer.

| What | Where |
|---|---|
| Client URL (lab) | `http://localhost:19088/data/perspective/client/BH` (log in with a gateway user; see [Getting Started](../getting-started/index.md)) |
| Project folder in the repo | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/` |
| Designer | Launch the Designer from the gateway home page, open project **BH**, then **Project Browser > Perspective** |
| Generated reference | [Perspective Reference](./reference/index.md): one page per view, every route, binding and style class |

:::tip Every Designer save is a file change
The gateway's data folder is bind-mounted from the repo (`gateways/standard/data`), so every Designer save lands
in git as a file change. Make all changes in the Designer; see [Common Tasks](../getting-started/common-tasks.md).
:::

## What Is In The Project Folder

```text
gateways/standard/data/projects/BH/
  project.json                                  title "BH"
  com.inductiveautomation.perspective/
    views/<folder>/<name>/view.json             every view (resource.json beside it holds the metadata)
    page-config/config.json                     URL routes, shared docks
    session-props/props.json                    session props + session custom properties
    session-permissions/data.bin                who may open a session (Authenticated)
    style-classes/<name>/style.json             project style classes (Designer: Styles)
    stylesheet/stylesheet.css                   Advanced Stylesheet
  ignition/
    script-python/...                           project script library (shared.*, Navigation.*, L5K.*)
    named-query/...                             SQL named queries
    tag-change/, timer/, message/               gateway events
  com.inductiveautomation.reporting/            report resources (Forms PDFs, Report Builder)
  com.inductiveautomation.webdev/               WebDev resources (globe, rack3d; login-gated)
```

Themes and the `equipment` icon library are **gateway** resources, not project resources. They live under
`gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/{themes,icons}/`. See
[Styling](./styling/index.md).

Every resource folder has a `resource.json` with metadata that the Designer and gateway keep up to date. Don't edit it
or the view files by hand: save in the Designer instead ([Merge Conflicts](../git-workflow/merge-conflicts.md) covers
the damaged-file case).

## View Folder Taxonomy

The numbered top folders sort the Project Browser the same way on every machine. The rule of thumb: **pages** are
what a URL opens, **popups** are what a click opens, **components** are reusable device graphics, **elements** are
small reusable parts inside components and faceplates.

| Folder | What goes here | Examples |
|---|---|---|
| `00_Pages/00_Docked/` | The chrome that is docked on every page: the top **Header**, the left **Navigation** tree, the right **Legend**. `_Assets/` holds the header pieces (logo, user chip, alarm bell, theme picker, PLC write-lock pill). `TempNav` is an older copy of the nav view; no page docks it. | [Header](./reference/views/00-pages/00-docked/header.md), [Navigation](./reference/views/00-pages/00-docked/navigation.md) |
| `00_Pages/Groveport/` | The Groveport site pages that are routed today: Utility Overview, the 19 CG (control group) pages, Machine Room and its device pages, Condensers, Operations > Forms, the PLC rack, plus the enterprise demo pages (site dashboards, Production, area KPIs) that are hidden in local mode. `_Shared/CG/` holds the CG page body shared by all 19 CG routes. | [Utility Overview](./reference/views/00-pages/groveport/utility/overview.md), [CG-E2](./reference/views/00-pages/groveport/east-ph/utility/cg-e2.md) |
| `00_Pages/Boars Head/` | Pages that are not tied to one site: Alarms (Status, Journal), Operations (Audit Log, Out Of Service, User Management, Roles & Permissions), the per-device-type **Details / Design** bodies (`Pumps/Details`, `Valves/Design` ...), the landing globe and the `NoViewPath` fallback. | [Alarm Summary](./reference/views/00-pages/boars-head/alarms/summary.md), [TypeTable](./reference/views/00-pages/boars-head/devices/typetable.md) |
| `01_Popups/00_Faceplates/` | Every **faceplate** (device popup). The tabbed shell `Faceplate` plus device-specific popups (`TankOverview`, `DiscreteInput`, sequences, `PlcRack/CardDetail`). `_Assets/<Device>/<Tab>` are the tab bodies. `Alerts/` holds the confirm dialog, the context menu and the Out Of Service memo dialog. Faceplates live **only** here. | [Faceplate shell](./reference/views/01-popups/00-faceplates/faceplate.md) |
| `01_Popups/Reports/` | The Report Builder popup and its parts. | [ReportBuilder](./reference/views/01-popups/reports/reportbuilder.md) |
| `02_Components/00_Controls/` | Small reusable controls: `NavButton`, `InterlockButton`. | |
| `02_Components/01_Devices/` | The device graphics placed on pages: Pump, Compressor, SolenoidValve, Tank, Sensor, Evaporator, ExhaustFan, Condenser, SafetyRelay, LTU, CoolingTower, VesselGeneric. Each takes a `tagPath` (UDT instance) and opens its faceplate on click. | [Components](./components.md) |
| `02_Components/02_Widgets/` | Dashboard widgets: `KPI`, `MetricCard`, `SiteCard`, `Safetys`. | |
| `02_Components/03_PLC/` | The PLC rack drawing: controller, one view per 1769 card type, end cap, `RackSlot`, `ModuleDetail`, `ModuleHover`, `PointRow`. | [PLC Rack](./pages/plc-rack.md) |
| `03_Elements/00_Control/` | Value entry elements used in faceplates and panels: `AnalogInput`, `MultiStateInput`, `TimeInput`, `StringInput`, `AnalogValue`. | |
| `03_Elements/01_Status/` | Status elements: `StatusIndicator`, `StatusDot`, `AnalogValue` (read only), `IconHeader` (mode / state icon strip), `AlarmHeader`, `Icons/*` and `NotificationIcons/*`. | |
| `03_Elements/03_Table/` | Table cell renderers (embedded views inside Table columns): `Numeric`, `Boolean`, `StateText`, `CgHit`, `DisplayTrend`, `DeviceLabelAlarmIndicator`. | |
| `98_Configuration/` | Tools and configuration screens: `AdhocTrend` (the `/trending` page and its parts), `TicketLogger`, `Integrations`, `ComponentPreview` (Designer preview pages), `Tools/L5K` (the L5K tag import tool). | [Trend](./reference/views/98-configuration/adhoctrend/trend.md) |

`_Assets/` folders inside any of these hold pieces that are only embedded by their parent views; they never have
a route of their own. The [All Views](./reference/views-index.md) page lists every view with its kind, routes,
and binding count.

## Page Routes (page-config)

A **page** in Perspective is a URL route that maps to one view, plus optional docks. BH has 93 routes in
`page-config/config.json` (Designer: **Project Browser > Perspective > Page Configuration**). The full list with
titles and views is generated on [Page Routes](./reference/routes.md).

| Route | View | Notes |
|---|---|---|
| `/` and `/plants/groveport/utility-overview` | `00_Pages/Groveport/Utility/Overview` | Home. In local mode `/` redirects to the Utility Overview URL. |
| `/cg-a1` ... `/cg-g5` | `00_Pages/Groveport/<Area>/Utility/CG-xx` | One per control group. |
| `/machine-room`, `/condensers` | Machine Room and Condensers overviews | |
| `/pumps`, `/valves`, `/tanks`, `/sensors`, `/compressors`, `/exhaust-fans` | Machine Room device-type pages | Details table + Design graphics. |
| `/condensers/pumps` ... `/condensers/condenser-fans` | Condenser device-type pages | |
| `/safety-relay`, `/rupture-disks` | Machine Room safeties | |
| `/alarms`, `/alarms/journal` | Alarm Status, Alarm Journal | |
| `/trending`, `/trending/saved` | Adhoc Trend, saved trends | |
| `/operations/...` | Out Of Service, Forms, Reports (`/operations/reports` Report Builder, `/operations/reports/saved` Saved Reports), Audit Log, Users, Roles & Permissions, PLCs | `/operations/plcs` is the PLC Overview (one card per PLC); `/operations/plcs/:plc`, `/operations/plcs/:plc/3d` (3D rack) and `/operations/out-of-service/:device` take a URL parameter. |
| `/enterprise`, `/plants/...` | Enterprise demo pages | Redirected to the Utility Overview in local mode. |
| `/no-view` | `00_Pages/Boars Head/NoViewPath` | Placeholder for a nav item that has no page. |

### Docks

A **dock** is a view pinned to an edge of the page. BH uses **shared docks** (on every page):

| Dock id | Edge | View | Behaviour |
|---|---|---|---|
| `app-header` | top, 48 px | [Header](./reference/views/00-pages/00-docked/header.md) | Always visible. |
| `plant-nav` | left, 260 px (auto-widens up to 480 px to fit the tree) | [Navigation](./reference/views/00-pages/00-docked/navigation.md) | Visible; collapses below 768 px; the header hamburger toggles it (`system.perspective.toggleDock('plant-nav')`). |
| `legend` | right, 220 px | [Legend](./reference/views/00-pages/00-docked/legend.md) | On demand (the info tab on the right edge). Some pages redefine it with `handle: hide`. |

![Header and nav dock](/img/perspective/header.png)

## Session Properties

Each browser tab gets a session. Session properties are defined in `session-props/props.json` (Designer:
**Project Browser > Perspective > Session Properties**). The generated
[Session Properties](./reference/session-properties.md) page shows every one with its binding and the views that
read it.

| Property | What it holds |
|---|---|
| `session.props.theme` | Theme folder name, default `light-cool` (see [Themes](./styling/themes.md)). |
| `session.props.animations` | Animations on / off (ChangeTheme popup). |
| `session.props.auth.user.roles` | The logged-in user's roles; every security binding starts here. |
| `session.custom.Permissions` | `{Device: {Action: bool}}` for the logged-in user, built from the Roles & Permissions matrix tag. Gate controls on this. See [Security In The UI](./security-ui.md). |
| `session.custom.ReadOnly` | `true` unless the user has `Faceplates/Operate`. Disables every write control. |
| `session.custom.CanOpenFaceplates` | `Faceplates/Open`. |
| `session.custom.EngineeringView` / `EngineeringReadOnly` | Engineering fields visible / editable. |
| `session.custom.AlarmConfigReadOnly` | Alarm Configuration tab editable or not. |
| `session.custom.Administrator`, `IntegrationAccess`, `TicketLogAccess`, `TicketLogSettings` | Role-list / matrix checks. `TicketLogAccess` = row `TicketLogger/Use` (every role); `TicketLogSettings` = row `TicketLogger/Settings` (OneShot only; also gates `IntegrationAccess`). |
| `session.custom.AdhocTrend` | The **trend basket**: pens (`tags`), plots, time range, realtime, colors. "Add To Trend" right-click menus append to it; the `/trending` page and the trend faceplate read it. |
| `session.custom.trend`, `session.custom.trendTools` | The trend basket summary and the trend tool state (Zoom Time / Zoom Area / Pan mode, Auto-Scale Y, zoom range) shared by the toolbar and the plots. See [Trending](./pages/trending.md). |

### Session Events

The BH project has **no Perspective session event scripts** (no session startup / shutdown / page startup
scripts and no session message handlers in the project). Work that other projects put in session startup is done
by bindings instead: `session.custom.Permissions` is an expression-structure binding that recomputes on login and
role change, and the Header's route guard runs from a binding plus a change script. Gateway-side events
(tag change, timer, message handlers) are documented in [Gateway Events](../scripting/gateway-events.md).

Session permissions (`session-permissions/data.bin`) require the **Authenticated** security level: an
anonymous browser gets the "You must log in" screen, for every route and popup (login required for everything, 2026-10-24; see [Security Access](../features/security-access.md)).

## Find A View From A URL

1. Take the path after `/client/BH`, for example `/operations/plcs/RCP1`.
2. Look it up on [Page Routes](./reference/routes.md). A parameterised route (`/operations/plcs/:plc`) matches any
   value in that slot. The route gives the view path, here `00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview`.
3. In the Designer open **Project Browser > Perspective > Views** and follow the folders of that path. Or open the
   view's reference page (search the wiki for the view name) for its components and bindings.
4. What you see on the page is often an **embedded view**: the reference page lists what each view embeds and what
   embeds it. For example `/pumps` is a thin page whose `Content` embed switches between
   `00_Pages/Boars Head/Pumps/Details` and `.../Design`.

## Find The URL Of A View

1. Open the view's reference page. "Routes" lists every route that opens it, "Docked" lists docks.
2. No route? Then it is a piece of another view. Follow "Embedded in" or "Opened or named by" upwards until you reach
   a page (or a popup that a page opens).
3. In the Designer, **Page Configuration** shows the same route table (one entry per URL, with its primary view and
   docks).

## Where To Go Next

- [Navigation](./navigation.md): the nav tree, its flags, local vs enterprise mode and the route guard.
- [Page Guides](./pages/index.md): what each main page shows and where its data comes from.
- [Faceplates](./faceplates.md) and [Components](./components.md).
- [Bindings](./bindings.md): binding conventions and the Integration Toolkit functions.
- [Styling](./styling/index.md) and [Security In The UI](./security-ui.md).
- Tags and UDTs that the views read: [Tags](../tags/index.md). Script modules: [Scripting](../scripting/index.md).
