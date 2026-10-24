---
title: "_Config Tags (Generated)"
sidebar_label: "_Config Tags"
description: "Every tag under [default]_Config with its type, documentation and the resources that read it."
generated: true
---

:::note

:::
Every tag under `[default]_Config` (configuration tags the HMI reads at runtime). **Values are not shown on purpose** (some hold credentials); read them in the Designer Tag Browser. **Read by** lists the project resources whose source mentions the full tag path (views, project scripts, gateway events, UDTs); scripts that build a path at runtime (for example `shared.Enums` with `_Config/Enums/` + a name) only show up on the parent folder.

What each one is for: [_Config Tags](../config-tags.md). **In git** = the folder is whitelisted in `.gitignore` (untracked folders exist only on this gateway).

| Tag | Type | Value source | Documentation | Read by | In git |
|---|---|---|---|---|---|
| `[default]_Config/DemoEnterpriseNav` | Boolean | memory | Deployment mode. false = LOCAL Groveport (Utility nav only, Boars Head / home -&gt; Utility Overview, enterprise routes redirect there). true = enterprise demo: shows t… | `view 00_Pages/00_Docked/Header`, `view 00_Pages/00_Docked/Navigation`, `script Navigation.Nav`, `script shared.Reports` | yes |
| `[default]_Config/Sync File System` | Boolean | memory | | - | yes |
| `[default]_Config/Rebuild` | Boolean | memory | | `script shared.Audit`, `script shared.OutOfService`, `script shared.Overview`, `tag-change overviewRebuild (trigger)`, `tag-change rebuildOverviewInstances (trigger)` | yes |
| `[default]_Config/Navigation` | Document | memory | | `webdev globe/mapMarkers`, `script Navigation.Nav` | yes |
| `[default]_Config/RolesPermissions` | DataSet | memory | HBT Roles &amp; Permissions matrix (Operations &gt; Roles &amp; Permissions): one Boolean column per role, union over a user's roles. | `view 00_Pages/Boars Head/Operations/_RPProbe`, `view 00_Pages/Boars Head/Operations/RolesPermissions`, `session props`, `script shared.PermissionMatrix`, `script shared.Security` | yes |
| `[default]_Config/MapMarkerNavigation` | Document | memory | | - | yes |
| `[default]_Config/MapMarkerHover` | String | memory | | `webdev globe/mapMarkers` | yes |
| `[default]_Config/Flash` | Boolean | expr `getSecond(now(0)) % 2 = 0` | 1 Hz blink clock for unacked alarm icons (Lightspeed/LGChem pattern) | `UDT Config/_Alarms` | yes |
| `[default]_Config/MapMarkerGeoJson` | Document | memory | | `webdev globe/mapMarkers` | yes |
| `[default]_Config/Colors/Alarms/Critical` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Colors/Alarms/High` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Colors/Alarms/Medium` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Colors/Alarms/Low` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Enums/Evaporator/DefrostStartMode` | DataSet | memory | Evaporator Cfg\_DefrostStartMode code -&gt; text. PLC (L5K CG\_RL\_Evap): 0 TOD, 1 Liquid Time, 2 Run Time, 3 DI Initiate, 4 AI Initiate. FT (STELLAR)CGDX 3VL/4VL: 0 ToD, 1 Cooling, 2 Runtime (input 0-2, security code F). The… | `view 00_Pages/Groveport/_Shared/CG/AhuEvapPanel`, `view 01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | yes |
| `[default]_Config/Enums/Evaporator/CycleFans` | DataSet | memory | Evaporator Cfg\_CycFans code -&gt; text: fan mode while the unit is idle. PLC (L5K CG\_RL\_Evap): 'Cycle Fans Mode for When the Unit is in Idle' 0 Fans Off, 1 Cycle Fans, 2 Fans On. FT: 0 Fans Off, 1 Cycle, 2 Fans On (securit… | `view 00_Pages/Groveport/_Shared/CG/AhuEvapPanel`, `view 01_Popups/00_Faceplates/_Assets/Evaporator/Controls`, `script shared.Enums` | yes |
| `[default]_Config/Enums/Evaporator/PlcState` | DataSet | memory | PLC CG\_RL\_Evap Sts\_State (control group phase, L5K wording) -&gt; hmiStatus = the Devices/Evaporator Status/Value code (0 Off, 1 Cooling, 2 Defrost, 3 Fault, 5 Idle, 6 Pump Down, 7 Hot Gas, 8 Bleed, 9 Fan Delay) for the PA… | - | yes |
| `[default]_Config/Forms/SeedVersion` | Int4 | memory | | - | yes |
| `[default]_Config/Forms/Operators` | String | memory | Operations Forms operator list (comma-separated): Name / Operator / Verified By dropdowns on Daily Rounds Log, NH3 Shift Log and Annual P&amp;ID Verification. The logged-in user's own name is always offered too. Seeded from… | `script shared.Forms` | yes |
| `[default]_Config/Forms/PidDrawingRevision` | String | memory | Annual P&amp;ID Verification: default 'Verified Against Drawing Revision' for a new cycle. | - | yes |
| `[default]_Config/Icons/Blank` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Icons/Alarms/Critical` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Icons/Alarms/High` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Icons/Alarms/Medium` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Icons/Alarms/Low` | String | memory | | `UDT Config/_Alarms` | no |
| `[default]_Config/Integrations/Monday` | UDT Config/Integration | instance | | `script shared.TicketLogger`, `script shared.TrendHistorized` | no |
| `[default]_Config/Map/MapMarkerGeoJson` | Document | memory | | - | no |
| `[default]_Config/Monday/Connected` | Boolean | memory | | - | no |
| `[default]_Config/Monday/Group Id` | String | memory | | - | no |
| `[default]_Config/Monday/API Token` | String | memory | | - | no |
| `[default]_Config/Monday/Board Id` | String | memory | | - | no |
| `[default]_Config/Monday/Workspace Id` | String | memory | | - | no |
| `[default]_Config/Monday/Enabled` | Boolean | memory | | - | no |
| `[default]_Config/Monday/Columns/Priority` | String | memory | | - | no |
| `[default]_Config/Monday/Columns/Email` | String | memory | | - | no |
| `[default]_Config/Monday/Columns/Description` | String | memory | | - | no |
| `[default]_Config/Monday/Columns/Status` | String | memory | | - | no |
 | String | memory | | - | no |
| `[default]_Config/Monday/Columns/Request Type` | String | memory | | - | no |
| `[default]_Config/Monday/Columns/Employee Name` | String | memory | | - | no |
| `[default]_Config/Monday/Columns/Creation Date` | String | memory | | - | no |
| `[default]_Config/Monday/Columns/Attached Files` | String | memory | | - | no |
| `[default]_Config/PLCs/List` | Document | memory | PLC Overview list (docs/plc-rack-io.md 'PLC Overview'): one entry per PLC site UDT instance. Add a PLC here (no view edit). | `view 00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview`, `view 00_Pages/Groveport/Operations/PlcOverview`, `script shared.Rack3d`, `script shared.Relay3d` | yes |
| `[default]_Config/PlcWriteLock/Locked` | Boolean | memory | PLC WRITE LOCK (docs/plc-write-lock.md). true = every tag that reads the RCP1 controller (all of \[default\]\_RCP1\_ and the OPC members of the PLC / Devices UDT definitions) is read only and HMI writes into the PLC are ref… | `view 00_Pages/00_Docked/_Assets/PlcWriteLock`, `view 00_Pages/00_Docked/Header`, `script shared.Alerts`, `script shared.PlcWriteLock`, `tag-change plcWriteLock (trigger)` | yes |
| `[default]_Config/PlcWriteLock/_Test/Locked` | Boolean | memory | PLC write lock TEST boolean: drives readOnly only on \_Config/PlcWriteLock/\_Test/Tags and the \_types\_/\_PlcWriteLockTest UDT (memory tags - never the PLC). Used to test shared.PlcWriteLock. | `tag-change plcWriteLockTest (trigger)` | yes |
| `[default]_Config/PlcWriteLock/_Test/Tags/TEST_A` | Boolean | memory | | - | yes |
| `[default]_Config/PlcWriteLock/_Test/Tags/TEST_B` | Float4 | memory | | - | yes |
| `[default]_Config/PlcWriteLock/_Test/Tags/Sub/TEST_C` | String | memory | | - | yes |
| `[default]_Config/PlcWriteLock/_Test/Instance` | UDT \_PlcWriteLockTest/TestCard | instance | | `script shared.TrendHistorized` | yes |
| `[default]_Config/Reports/Catalog` | Document | memory | Report builder data catalog (shared.Reports): sources, measures, scope trees, breakdowns, filters, sections, presets. | `script shared.Reports` | yes |
| `[default]_Config/Security/PermissionCatalog` | DataSet | memory | Roles &amp; Permissions page grouping: Key = Devices value (Category, sub-group Label, Order) or Devices/Actions (row Label, optional Category). Unknown devices go to Other. | `view 00_Pages/Boars Head/Operations/RolesPermissions` | yes |
| `[default]_Config/Security/RestrictedRoles` | String | memory | Roles hidden in User Management unless the viewer holds them. | `script shared.UserAdmin` | yes |
| `[default]_Config/Security/RestrictedRows` | String | memory | Roles &amp; Permissions rows only some roles manage: 'Devices/Actions:RoleA\|RoleB', comma-separated (device-perms 2026-10-24; role-wizard v7: BOTH Ticket Logger rows are OneShot only on the page - Use stays ticked for every… | `view 00_Pages/Boars Head/Operations/RolesPermissions`, `session props`, `script shared.PermissionMatrix`, `script shared.Security` | yes |
| `[default]_Config/Security/IntegrationRoles` | String | memory | Roles that see Ticket Logger &gt; Integrations (API endpoints, tokens, Test Connection) - session.custom.IntegrationAccess. | - | yes |
| `[default]_Config/Security/ReadOnlyRoles` | String | memory | Informational since 2026-10-01 (security tiers): read only = no Faceplates/Operate tick in \[default\]\_Config/RolesPermissions for any of the user's roles (session.custom.ReadOnly). Kept for reference; not used for gating. | - | yes |
| `[default]_Config/Security/RoleInherits` | String | memory | Role inheritance for the Roles &amp; Permissions matrix: 'A:B' = role A also gets every tick of role B (comma-separated pairs, chains follow, case-insensitive). Engineering:Maintenance keeps Engineering a superset of Mainte… | `view 00_Pages/Boars Head/Operations/_Admin/RPRoleHead`, `view 00_Pages/Boars Head/Operations/_RPProbe`, `view 00_Pages/Boars Head/Operations/RolesPermissions`, `session props`, `script shared.PermissionMatrix`, `script shared.Security` | yes |
| `[default]_Config/Security/TierSeedVersion` | Int4 | memory | Not used by the HMI. | - | yes |
| `[default]_Config/Security/DeviceTypes` | DataSet | memory | device-perms (2026-10-24): UDT TypeId -&gt; Roles &amp; Permissions Devices value. A device control needs its general row AND &lt;Device&gt;/&lt;Action&gt; when that row exists (no row = general only). shared.Security.deviceOf (server) an… | `view 00_Pages/Groveport/_Shared/CG/AhuEvapPanel`, `view 01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow`, `view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField`, `view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow`, `view 01_Popups/00_Faceplates/_Assets/CoolingTower/Controls`, `view 01_Popups/00_Faceplates/_Assets/Evaporator/Controls`, `view 01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls`, `view 01_Popups/00_Faceplates/_Assets/InterlockPanel` +21 more | yes |
| `[default]_Config/Security/AdminRoles` | String | memory | Roles that are HMI administrators (session.custom.Administrator: User Management / Roles &amp; Permissions pages besides the matrix rows, legacy adminOnly nav items). Comma-separated, case-insensitive. Faceplates, Engineeri… | `session props`, `script shared.Globe` | yes |
| `[default]_Config/Security/TicketLoggerRoles` | String | memory | UNUSED since 2026-10-24 (device-perms): the Ticket Logger is gated by the Roles &amp; Permissions rows TicketLogger/Use (every role; session.custom.TicketLogAccess) and TicketLogger/Settings (OneShot only). Kept for referen… | - | yes |
| `[default]_Config/Security/DeviceActionRules` | DataSet | memory | device-perms (2026-10-24): which device-type row (&lt;Device&gt;/&lt;Action&gt;) a server-side write needs. Pattern = Python regex searched in the member path below the device instance (e.g. 'Motor/OCmd\_Start/Value'); first match w… | `script shared.Security` | yes |
| `[default]_Config/Security/PermissionCategories` | DataSet | memory | Roles &amp; Permissions page groups (Name, Order, Icon, Description). | `view 00_Pages/Boars Head/Operations/RolesPermissions` | yes |
| `[default]_Config/Security/NewRoleDefaults` | String | memory | Roles &amp; Permissions rows ('Devices/Actions', comma-separated) a NEW role gets (role-wizard 2026-10-24, user: every role may log tickets): a role created in the gateway holds them until its matrix column exists, and the… | `session props`, `script shared.PermissionMatrix`, `script shared.Security` | yes |
| `[default]_Config/Security/FullPermissionRoles` | String | memory | Roles that hold every Roles &amp; Permissions action, even where the matrix has no tick. | `view 00_Pages/Boars Head/Operations/_Admin/RPRoleHead`, `view 00_Pages/Boars Head/Operations/_RPProbe`, `view 00_Pages/Boars Head/Operations/RolesPermissions`, `session props` | yes |
| `[default]_Config/TicketLogger/Types` | DataSet | memory | Ticket Logger types. Fields = comma-separated \_Config/TicketLogger/Fields keys, in form order. | `view 98_Configuration/TicketLogger`, `script shared.TicketLogger` | no |
| `[default]_Config/TicketLogger/Routing` | Document | memory | Ticket Logger routing (ticket-routing 2026-10-24): rules \[\{type, area, destination, boardId, groupId\}\] ('' = Any; most specific match wins: Type + Area, Type, Area) and the default for unmatched selections. destination… | `script shared.TicketLogger` | no |
| `[default]_Config/TicketLogger/DryRun` | Boolean | memory | Ticket Logger dry run (ticket-routing 2026-10-24): true = no Monday item is created and nothing is queued for Oracle; tickets are recorded in dbo.ticket\_outbox as 'Dry Run' with their routed destination. Ticket Logger &gt;… | `script shared.TicketLogger` | no |
| `[default]_Config/TicketLogger/Fields` | DataSet | memory | Ticket Logger input fields (the view has one block per key; a new key needs a view block too). | `view 98_Configuration/TicketLogger` | no |
