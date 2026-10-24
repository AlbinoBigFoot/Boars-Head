---
title: _Config Tags
sidebar_label: _Config Tags
sidebar_position: 8
description: Every tag under [default]_Config - navigation, roles and permissions, security role lists, enums, the PLC write lock, deployment mode, reports, forms, alarm colors, integrations - what each is for and what reads it.
sources:
  - gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/**/tags.json
  - docs/local-groveport-mode.md
last_verified: 2026-10-24
---

# `_Config` Tags

`[default]_Config` holds small, global settings the HMI reads at runtime by tag path. Most are edited in the Tag Browser;
a few are edited from admin pages. The generated [_Config Tags](reference/config-tags.md) page lists every tag with
its type, documentation and the project resources that read it.

:::caution Values are not in the wiki
Some `_Config` tags hold credentials (the Monday / Integrations API tokens). The wiki never shows `_Config` values;
read them in the Designer. The folders that hold credentials (`Integrations`, `Monday`) are not in git.
:::

## Deployment And Navigation

| Tag | Type | What | Read by |
|---|---|---|---|
| `_Config/DemoEnterpriseNav` | Boolean | **Deployment mode switch.** `false` = local Groveport (only Groveport / Utility in the nav, Boars Head and home go to the Utility Overview, enterprise routes redirect there). `true` = enterprise demo (other plants, globe, production overview). Change it only in the Tag Browser (set the value); a file edit blanks the live value. See [Deployment Modes](../deployment/deployment-modes.md). | Header, Navigation, `Navigation.Nav`, route guards |
| `_Config/Navigation` | Document | The nav tree (mirror of `00_Docked/Navigation` `view.custom.items`): nodes with `data.hidden`, `data.demo`, `data.demoPage`, `data.adminOnly`, `data.flattenLocal`, `data.localIcon`. Copy the view's `custom.items` into it after every nav edit ([Navigation](../perspective/navigation.md#sync-the-tag)). | `Navigation.Nav`, the globe map markers web endpoint |
| `_Config/MapMarkerGeoJson`, `MapMarkerHover`, `MapMarkerNavigation`, `Map/MapMarkerGeoJson` | Document / String | Enterprise globe markers (plant locations, hover text, marker -> page). | WebDev `globe/mapMarkers` |
| `_Config/Rebuild` | Boolean | Set true to rebuild every device table cache (`Overview` instances). | tag-change events `overviewRebuild`, `rebuildOverviewInstances`; `shared.Overview`, `shared.Audit`, `shared.OutOfService` |
| `_Config/Flash` | Boolean (expression) | Blink clock for unacknowledged alarms. | `Config/_Alarms._Flash` |
| `_Config/Sync File System` | Boolean | Legacy flag, nothing reads it. | - |

## Security And Permissions

Roles & Permissions and User Management were redesigned on 2026-10-23: the matrix tag is unchanged, and two new
DataSet tags, `_Config/Security/PermissionCategories` and `_Config/Security/PermissionCatalog`, decide which group a
row lands in on the page (see [Roles & Permissions](../features/roles-permissions.md)). The generated page lists every tag.

| Tag | Type | What |
|---|---|---|
| `_Config/RolesPermissions` | DataSet | **The permission matrix**: columns `Devices`, `Actions`, `Description` plus one Boolean column per role. The session property script turns it into `session.custom.Permissions.<Device>.<Action>` for the logged-in user (union over the user's roles, Administrator = everything). Gate new controls on that, not on role names. Edited on Operations > Roles & Permissions (`/operations/roles-permissions`). |
| `_Config/Security/AdminRoles` | String | Comma-separated roles that are HMI administrators (`session.custom.Administrator`: User Management and Roles & Permissions pages, `adminOnly` nav items). |
| `_Config/Security/FullPermissionRoles` | String | Roles that hold every matrix action even without a tick. |
| `_Config/Security/RoleInherits` | String | `A:B` pairs: role A also gets every tick of role B (for example `Engineering:Maintenance`). |
| `_Config/Security/RestrictedRoles` | String | Roles hidden in User Management unless the viewer holds them. |
| `_Config/Security/IntegrationRoles` | String | Older role list for Ticket Logger > Integrations. Since 2026-10-24 `session.custom.IntegrationAccess` follows the matrix row `TicketLogger/Settings` instead. |
| `_Config/Security/TicketLoggerRoles` | String | **Unused since 2026-10-24** (kept): the Ticket Logger is gated by the matrix rows `TicketLogger/Use` (every role) and `TicketLogger/Settings` (OneShot only). |
| `_Config/Security/RestrictedRows` | String | Matrix rows only certain roles may hold or even see, as `Devices/Actions:RoleA\|RoleB` pairs (today `TicketLogger/Settings:OneShot`). Such a row is not implied for `FullPermissionRoles` and is hidden on Roles & Permissions from other roles. |
| `_Config/Security/DeviceTypes` | DataSet | Device-type rows: UDT TypeId -> the matrix Devices value (`Devices/Pump` -> `Pump`). Edit to map a type to another row set. |
| `_Config/Security/DeviceActionRules` | DataSet | Server-side classification of a written member into Command / Mode / Interlocks / Setpoint (regex on the member path, first match wins; no match = Setpoint). |
| `_Config/Security/TierSeedVersion` | Int | Version of the one-time permission seed (the initial tier ticks). Leave it alone: it stops a later tick made on Roles & Permissions from being reverted. |
| `_Config/Security/ReadOnlyRoles` | String | Informational since 2026-10-01 (read only = no Faceplates/Operate tick); not used for gating. |
| `_Config/Security/PermissionCatalog`, `PermissionCategories` | DataSet | Grouping and labels of the Roles & Permissions page . |

Rule: role lists live in these tags and are read through `shared.Security` / session properties; never hard-code
role names in views or scripts.

## PLC Write Lock

| Tag | What |
|---|---|
| `_Config/PlcWriteLock/Locked` | `true` = every tag that reads the RCP1 PLC is read only and the HMI write guards refuse. The single lock boolean (v2, 2026-10-23): there is no page, permission row or scope tag. Only the project owner changes it, in the Designer Tag Browser. Fail-safe: bad or null = locked, and a gateway start forces `true`. See [PLC Write Lock](plc-write-lock.md). |
| `_Config/PlcWriteLock/_Test/Locked` | The TEST boolean; drives only the test tags `_Test/Tags/*` and the test UDT instance `_Test/Instance`. |

## Enums

`_Config/Enums/Evaporator/DefrostStartMode`, `CycleFans`, `PlcState`: code to text DataSets, see [Enums](enums.md).

## Reports And Forms

| Tag | What |
|---|---|
| `_Config/Reports/Catalog` | Document: the custom report builder catalog (sources, measures, scope trees, breakdowns, filters), read by `shared.Reports`. |
| `_Config/Forms/Operators` | Comma-separated operator list for the Name / Operator / Verified By dropdowns of the Operations Forms (Daily Rounds, NH3 Shift Log), read by `shared.Forms`. |
| `_Config/Forms/PidDrawingRevision` | Default "Verified Against Drawing Revision" for a new Annual P&ID Verification cycle. |

## Alarm Colors And Icons

`_Config/Colors/Alarms/Critical | High | Medium | Low` (color strings) and `_Config/Icons/Alarms/*`, `Icons/Blank`
(icon paths), read by `Config/_Alarms._Color` / `_Icon` through `{[~]_Config/...}` (`[~]` = the same provider). Not
in git (recreate from a backup or the Designer).

## Integrations And Ticket Logger

| Tag | What |
|---|---|
| `_Config/Integrations/<Name>` | One `Config/Integration` UDT instance per API endpoint (today `Monday`): provider, endpoint URL, API version, **API token (write-only from the HMI)**, enabled, connected, last check / error. Read by `shared.Integrations` and `shared.TicketLogger`. Not in git. |
| `_Config/Monday/*`, `_Config/Monday/Columns/*` | Older Monday board / column ids for the Ticket Logger. Not in git. |
| `_Config/TicketLogger/Types`, `Fields` | DataSets: ticket types and the input fields per type (`98_Configuration/TicketLogger`). Not in git. |
| `_Config/TicketLogger/Routing` | Document: where a ticket is sent, by Type and Area (`{default: {destination, boardId, groupId}, rules: [...]}`; the most specific rule wins). Edited on the Ticket Logger Settings > Routing screen (OneShot only). Not in git. |
| `_Config/TicketLogger/DryRun` | Boolean: while true nothing is sent; tickets are recorded in `dbo.ticket_outbox` with status `Dry Run`. Not in git. |
| `_Config/PLCs/List` | Document `{plcs: [{name, path, description, location, page, show}]}`: one PLC Overview card per entry (add a PLC here). |

## Adding Or Changing A `_Config` Tag

1. Designer > Tag Browser > `[default]_Config` > the folder > right-click > **New Tag > Memory Tag**. Set the data type
   and a documentation string that says what reads it.
2. Set its value in the tag editor (**Value** field; for a DataSet or Document tag open the value editor).
3. If it lives in a folder that is not whitelisted in `.gitignore`, add the `!` lines, unless it holds a secret (then it
   must stay out of git).
4. Run `python -I wiki/tools/gen_all.py tags` so the generated list shows it.

To change a value, edit it in the Tag Browser. Never edit `_Config/DemoEnterpriseNav` in the JSON file.

