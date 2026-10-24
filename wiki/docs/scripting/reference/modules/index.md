---
title: "Script Library Reference"
sidebar_label: "Script Modules"
sidebar_position: 2
description: "Every project script module of the BH project, generated from ignition/script-python."
generated: true
custom_edit_url: null
---

:::note

:::

All project library modules (Designer: **Project Browser > Scripting > Project Library**). Path on disk: `gateways/standard/data/projects/BH/ignition/script-python/<package>/<Module>/code.py`.

| Module | Lines | Functions | External callers | Summary |
|---|---|---|---|---|
| [L5K.Parser](./l5k-parser.md) | 1318 | 17 | 4 | |
| [Navigation.Faceplate](./navigation-faceplate.md) | 84 | 2 | 26 | |
| [Navigation.Nav](./navigation-nav.md) | 656 | 25 | 14 | Navigation |
| [shared.AdhocTrend](./shared-adhoctrend.md) | 1107 | 52 | 76 | |
| [shared.AlarmConfig](./shared-alarmconfig.md) | 419 | 12 | 2 | List alarm-configured leaves under a device for Faceplate Alarm Configuration. |
| [shared.Alarms](./shared-alarms.md) | 347 | 8 | 6 | Alarm rollup rebuild for Config/\_Alarms (ported from LGChem / Citadel Rebuild script). |
| [shared.Alerts](./shared-alerts.md) | 323 | 9 | 443 | Alert Popup Script |
| [shared.Audit](./shared-audit.md) | 289 | 9 | 34 | OPS Audit helpers for Perspective writable values. |
| [shared.DevicePages](./shared-devicepages.md) | 288 | 6 | 2 | Device-type pages (Tanks / Pumps / Compressors / Valves / Sensors / Exhaust Fans). |
| [shared.Enums](./shared-enums.md) | 137 | 9 | 3 | Code -&gt; text enums (evap-defrost-strings, 2026-10-22). |
| [shared.FaceplateTrend](./shared-faceplatetrend.md) | 115 | 1 | 1 | Faceplate Trend tab defaults. |
| [shared.Forms](./shared-forms.md) | 776 | 51 | 49 | Operations Forms (Operations &gt; Forms): Daily Rounds Log, NH3 Shift Log, Annual P&ID Verification, Form History. |
| [shared.Globe](./shared-globe.md) | 168 | 8 | 7 | Globe landing page (WebDev iframe &lt;-&gt; Perspective page), scoped to ONE session + page. |
| [shared.GlobePage](./shared-globepage.md) | 2104 | 1 | 1 | Globe page HTML for WebDev globe/map (served only after shared.WebAuth). |
| [shared.Integrations](./shared-integrations.md) | 245 | 20 | 11 | Integration endpoints (API connections): [default]\_Config/Integrations/&lt;Name&gt;, one Config/Integration UDT |
| [shared.OutOfService](./shared-outofservice.md) | 352 | 19 | 31 | 
| [shared.Overview](./shared-overview.md) | 612 | 29 | 10 | 
| [shared.Pax](./shared-pax.md) | 1268 | 7 | 18 | 
| [shared.PermissionMatrix](./shared-permissionmatrix.md) | 465 | 24 | 21 | Roles & Permissions page (Operations &gt; Roles & Permissions) - server side. |
| [shared.PlcRack](./shared-plcrack.md) | 36 | 1 | 1 | PLC Rack / IO helpers. UI only: nothing here |
| [shared.PlcWriteLock](./shared-plcwritelock.md) | 428 | 26 | 8 | 
| [shared.ProductionMetrics](./shared-productionmetrics.md) | 652 | 3 | 4 | 
| [shared.Rack3d](./shared-rack3d.md) | 194 | 11 | 3 | PLC Rack 3D (WebDev rack3d/\*): READ ONLY rack / IO state for the three.js page, and the locally served static files. |
| [shared.Relay3d](./shared-relay3d.md) | 133 | 8 | 3 | HLCO Safety Relay 3D (WebDev relay3d/\*): READ ONLY relay state for the three.js page, and the locally served static files. |
| [shared.Reports](./shared-reports.md) | 2730 | 137 | 44 | Report builder engine (Production KPIs, Alarms, ... any source in the catalog). |
| [shared.Scale](./shared-scale.md) | 89 | 5 | 16 | Coordinate-container view scaling (Scout-style). |
| [shared.Security](./shared-security.md) | 398 | 25 | 82 | Role lists from [default]\_Config/Security and the Roles & Permissions matrix [default]\_Config/RolesPermissions |
| [shared.TicketLogger](./shared-ticketlogger.md) | 640 | 39 | 14 | Ticket Logger (2026-10-24 ticket-routing): every logged-in user submits tickets (Roles & Permissions |
| [shared.TrendContext](./shared-trendcontext.md) | 640 | 40 | 160 | Trend context menu + session trend basket (2026-10-23). See docs/trending.md. |
| [shared.TrendHistorized](./shared-trendhistorized.md) | 330 | 2 | 0 | 
| [shared.UserAdmin](./shared-useradmin.md) | 279 | 18 | 16 | User Management helpers (Operations &gt; User Management, ported from the HBT/Scout template). |
| [shared.Utilities](./shared-utilities.md) | 26 | 1 | 0 | Multistate / boolean label helpers for Perspective table cells. |
| [shared.UtilityMetrics](./shared-utilitymetrics.md) | 320 | 13 | 2 | Utility Overview (OverviewKpis) metrics from the REAL plant data only: live reads for status / counts, |
| [shared.ValveCommands](./shared-valvecommands.md) | 247 | 19 | 24 | Valve / pump faceplate command helpers (SO/MO). |
| [shared.WebAuth](./shared-webauth.md) | 73 | 5 | 74 | Login check for WebDev resources that a logged-in Perspective session loads (iframe src, fetch from the iframe). |
| [shared.tagsTree](./shared-tagstree.md) | 112 | 3 | 0 | |
