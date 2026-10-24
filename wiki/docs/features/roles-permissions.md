---
title: Roles & Permissions / User Management
sidebar_position: 10
description: The permission tiers (Read Only, Maintenance, Engineering, Administrator), the Roles & Permissions matrix tag, session permissions, server-side checks and the User Management page.
sources:
  - docs/user-management.md
  - docs/security-roles.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Security/code.py
  - gateways/standard/data/projects/BH/ignition/script-python/shared/UserAdmin/code.py
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json
last_verified: 2026-10-24
---

# Roles & Permissions / User Management

## What it does

Decides what each user may see and do. Users and roles live in the gateway's internal user source `default`; what a
role may do is **one column of ticks in a matrix tag**, so changing a tier is a checkbox on the Roles & Permissions
page, not a code change.

| Capability | Read Only | Maintenance | Engineering | Administrator / OneShot |
|---|---|---|---|---|
| View pages, alarms, nav | yes | yes | yes | yes |
| Trending, save own trends | yes | yes | yes | yes |
| Save over / delete locked or others' trends | - | - | yes | yes |
| Open faceplates | - | yes | yes | yes |
| Operate (modes, commands, setpoints, resets) | - | yes | yes | yes |
| Alarm Ack / Shelve | - | yes | yes | yes |
| Alarm Configuration tab | - | read only | yes | yes |
| Engineering content (FT Engineering pages) | - | read only | yes | yes |
| Out Of Service / Return | - | yes | yes | yes |
| Out Of Service comments | - | - | yes | yes |
| Operations Forms (use / see everyone's) | - | use | use + view all | use + view all |
| Reports (page and builder) | - | yes (builder) | yes (page and builder) | yes (+ manage shared templates) |
| Ticket Logger (use) | yes | yes | yes | yes |
| Ticket Logger Settings | - | - | - | OneShot only |
| Admin > Audit Log | - | - | yes | yes |
| Admin > User Management, Roles & Permissions | - | - | - | yes |

`RoleInherits = Engineering:Maintenance`: Engineering automatically gets every Maintenance tick. A user with
several roles gets the union.

![Roles & Permissions page: grouped, collapsible matrix with locked and inherited cells](/img/features/roles-permissions/roles-matrix.png)

![User Management page (names blurred)](/img/features/roles-permissions/users.png)

## How to use it (administrators)

- **Admin > User Management** (`/operations/users`): Users and Roles tabs; add / edit / remove users, assign roles,
  contact info and notes (design ported from the HBT / Scout template, redesigned 2026-10-23). Service accounts (`admin`, `ops`, `opcuauser`)
  are hidden; restricted roles show only to users who hold them. Errors from the gateway (duplicate name, password
  rule) are shown in the Alert popup; successful changes are audited.
- **Admin > Roles & Permissions** (`/operations/roles-permissions`): rows are grouped (General, Devices, Alarms,
  Engineering, Operations, Administration, Other) and collapse; search, filter by category, compare roles or show only
  differences. Tick or untick a role's cell (or a group's count to grant / revoke the whole group), then **Save Changes**
  (`RolesPermissions/Edit`; a confirm lists the changes). Administrator and OneShot are locked "All"; Engineering's
  inherited Maintenance ticks are grey and not clickable. A gateway role without a column gets one on its first tick.
  Every save writes an OpsAudit event **Permissions Changed**. Page detail: [Admin Pages](../perspective/pages/admin.md).

### New Role wizard

**Add Role** (on Roles & Permissions, in the Roles list header, and on User Management > Roles) opens a two-step popup,
centred over the page. It needs `RolesPermissions/Edit` and either `UserManagement/Add` or `/Edit`.

1. **Role:** type the **Role Name** (letters, digits, space, `-` and `_`, up to 50 characters) and choose **Copy
   Permissions From** (None starts from the defaults; or pick an existing role you can see). **Next** checks the name
   on the gateway: it must not be empty, must not match an existing role (case-insensitive), a matrix column key, or a
   name already used in any `_Config/Security` role list (for example `Admin` is in `AdminRoles`, so a new role of
   that name would silently be an administrator).
2. **Permissions:** the same grouped, collapsible list as the matrix, with search, **Expand / Collapse All**, a
   select-all box per group and an "N Of M Selected" count. The starting ticks are the copied role's effective
   permissions (its ticks, what it inherits, or everything for a full-permission role), or the defaults. Rows hidden
   from you (restricted rows) are not listed.

**Create Role** asks for confirmation, creates the role in the gateway user source, then adds its column to the
matrix with the ticks you chose. If the matrix write fails the role is removed again. One Audit Log event, **Role
Created**, records the role, the number of permissions, the role it was copied from and the keys. The wizard never
changes the `_Config/Security` lists (Full Access, Admin, Restricted stay deliberate tag edits).

### New roles

`[default]_Config/Security/NewRoleDefaults` holds the permissions every new role gets (today `TicketLogger/Use`).
A role created **directly in the Gateway** (Config > Security > User Sources > `default` > Roles) holds these at once
when one of its users logs in, and the first load of Roles & Permissions or User Management adds its column to the
matrix with them ticked (Audit Log event **Role Added To Matrix**). Existing columns are never changed by this.
The wizard pre-ticks the same defaults, and sets rows hidden from the creator (such as `TicketLogger/Use`) too.

## Where to find it

- **HMI**: nav Groveport > Admin > Roles & Permissions / User Management (the Admin folder only shows for users who may
  open it).
- **Designer**: Project Browser > Perspective > Views > `00_Pages` > `Boars Head` > `Operations` >
  `RolesPermissions` (and `UserManagement`, parts under `_Admin`). The matrix tag is in the Tag Browser under
  `default` > `_Config` > `RolesPermissions`; the role lists are under `_Config` > `Security`.
- **Gateway web UI** (`http://localhost:19088`): Platform > Security > User Sources > `default` holds the users and
  roles themselves (the pages edit these through `system.user.*`); see [Security](../gateway/security.md).

## Where the pieces live (developers)

| Piece | Where |
|---|---|
| Matrix | DataSet tag `[default]_Config/RolesPermissions`: columns `Description`, `Actions`, `Devices` + one Boolean per role |
| Role lists | `[default]_Config/Security/*`: `FullPermissionRoles` (every row), `AdminRoles`, `IntegrationRoles`, `RestrictedRoles`, `RestrictedRows`, `DeviceTypes`, `DeviceActionRules`, `RoleInherits`, `TierSeedVersion`; `PermissionCategories`, `PermissionCatalog` (the group a row lands in: Key, Category, Label, Order) |
| Session props | `session.custom.Permissions` (`shared.Security.permissions(roles, matrix, full, inherits)`), `ReadOnly`, `CanOpenFaceplates`, `EngineeringView`, `EngineeringReadOnly`, `AlarmConfigReadOnly`, `Administrator`, `TicketLogAccess`, `IntegrationAccess` - all **PROTECTED** (see [Perspective Scripting](../scripting/perspective-scripting.md)) |
| Server checks | `shared.Security.can / allowed / require` ([reference](../scripting/reference/modules/shared-security.md)) |
| Pages | `00_Pages/Boars Head/Operations/UserManagement/*`, `00_Pages/Boars Head/Operations/RolesPermissions` |
| Library | `shared.UserAdmin`, `shared.PermissionMatrix` |

### Rows the HMI enforces

| Row | Gate |
|---|---|
| `Faceplates/Open` | every faceplate open (`Navigation.Faceplate.openFaceplate` / `openDevice`), hover outlines, nav device leaves |
| `Faceplates/Operate` | `session.custom.ReadOnly`; `shared.Audit.writeTag`, `shared.ValveCommands` |
| `Engineering/View`, `Engineering/Edit` | Engineering tabs / cards hidden or read only (UI only) |
| `AlarmConfiguration/Edit` | Alarm Configuration rows; `shared.AlarmConfig.applyOverride` |
| `AlarmSummary/Acknowledge`, `/Shelve` | alarm tables, Safetys Reset / Silence |
| `OutOfService/Set`, `/View`, `/Comment` | see [Out Of Service](./out-of-service.md) |
| `AuditLog/View` | Audit Log nav, page, `:allowed` of the query |
| `UserManagement/Add`, `/Edit`, `RolesPermissions/Edit` | admin pages and their save scripts |
| `Trends/Save`, `Trends/ManageLocked` | saving trends; locked / others' trends |
| `Forms/Use`, `Forms/ViewAll` | Operations Forms |
| `Reports/Use`, `ShareTemplates`, `ManageTemplates`, `Reports/<Source>` | Report Builder |
| `Reports/Page` | the Reports nav item under Operations (Administrator, OneShot, Engineering) |
| `TicketLogger/Use` | the Ticket Logger menus and popup (every role) |
| `TicketLogger/Settings` | the Ticket Logger settings gear and API setup (OneShot only, see below) |
| `<Device>/Command`, `Mode`, `Interlocks`, `Setpoint`, `Configuration`, `Alarm` | device-type rows, see below |

### Device-type permissions

A control now needs **two** ticks: its general row **and** its device-type row. For example, starting a pump needs
`Faceplates/Operate` **and** `Pump/Command`; the mode buttons need `Faceplates/Operate` **and** `Pump/Mode`. The kinds
are Command, Mode, Interlocks, Setpoint, Configuration and Alarm (Alarm Configuration needs `AlarmConfiguration/Edit`
and `<Device>/Alarm`). A device type or action with no row in the matrix needs only the general row, so adding a row
such as `CoolingTower/Command` starts gating those controls.

- **What the user sees:** the control is disabled and its tooltip reads **Not Permitted: &lt;Device&gt; / &lt;Action&gt;**. If a
  write still reaches the gateway, the server refuses it and a **Not Permitted** dialog opens.
- **Where the mapping lives:** Tag Browser > `[default]_Config` > `Security` > `DeviceTypes` (dataset: UDT type id and
  the matrix Device name it maps to) and `DeviceActionRules` (dataset: which member names count as Command, Mode,
  Interlocks, Setpoint or Configuration writes).

### LTU Command

`LTU/Command` gates the LTU card's **Reset Count** button (Machine Room page, NH3 LTU group), in addition to
`Faceplates/Operate` and the [PLC write lock](./plc-write-lock.md). It was granted to every role that already held
`Faceplates/Operate`; untick it on Roles & Permissions to take the button away from a role. See
[Machine Room](../perspective/pages/machine-room.md#ltu-card-and-reset-count).

### Ticket Logger

`TicketLogger/Use` is ticked for **every role**, and for every new role by default: any signed-in user can log a ticket. `TicketLogger/Settings` (the
settings gear: API setup, routing, dry run) is **OneShot only**: the tag `_Config/Security/RestrictedRows` keeps the
row away from Administrator, and the row only shows on Roles & Permissions to OneShot users. See
[Ticket Logger](./ticket-logger.md).

### How a check works

`shared.Security.can(device, action, session=None)` reads the roles of the calling Perspective session (found on
the call stack if not passed), applies `RoleInherits`, reads the matrix and returns the tick. Outside a session
(gateway timers, tag events) it returns **True**; if the roles cannot be read it logs one warning and allows (the
UI gates still apply). `require()` also logs every refusal with the user name.

## How To Change It

- **Restrict a role from one device type:** Admin > Roles & Permissions, find the device's rows (for example Pump >
  Command), untick the role's cell and **Save Changes**. The role keeps everything else; only that device type's
  controls show the Not Permitted tooltip. New sessions pick it up on login.
- **Change a tier:** tick the matrix on the Roles & Permissions page (Admin > Roles & Permissions). No code edit.
- **Add a gated feature (a new permission row):**
  1. Tag Browser > `[default]_Config` > `RolesPermissions` > open the tag editor > edit the **Value** dataset. Add a
     row: `Devices` (the group, e.g. `Reports`), `Actions` (e.g. `Export`), `Description`, and tick the role columns
     that may use it.
  2. To place the row in a group on the page, add a matching row (Key `Device/Action`, Category, Label, Order) to
     `[default]_Config/Security/PermissionCatalog`.
  3. Gate the UI on `session.custom.Permissions.<Device>.<Action>` (for example the component's `enabled` or
     `visible` binding), and gate the server-side script on `shared.Security.require(...)`.
  4. Save, reload a session, and test with a user of each role.
- **Create a role:** Admin > Roles & Permissions (or User Management > Roles) > **Add Role** > the wizard above. If you
  create a role directly in the Gateway it gets only the defaults; open Roles & Permissions once so its column
  appears, then tick what the role needs.
- **Change the defaults of new roles:** Tag Browser > `[default]_Config/Security/NewRoleDefaults`.
- **Never hard-code role names** in views or scripts; use the matrix or the `_Config/Security` lists.
- **Role lists:** Tag Browser > `[default]_Config/Security/*` (for example `AdminRoles`, `FullPermissionRoles`).
- **The pages:** Project Browser > Perspective > Views > `00_Pages/Boars Head/Operations` > `RolesPermissions` and
  `UserManagement` (parts under `_Admin`). The scripts are `shared.UserAdmin` and `shared.PermissionMatrix` (Project
  Library). Users and roles themselves live in the Gateway web UI (Config > Security > User Sources > `default`).

## Known limitations and open questions

1. Engineering vs Maintenance is enforced only in the UI for individual tags (`writeTag` only knows the path).
2. Compressor/Command has no control yet (the compressor faceplate is read only), and CoolingTower, ExhaustFan, VFD and the other device types have no rows (LTU has only `LTU/Command`, for its Reset Count button), so only the general row applies to them.
3. Role create / rename / delete has no safe path on the permissions page (a rename does not move the matrix column or the `_Config/Security` lists); it stays on User Management with a note.
4. `_Config/Security/TicketLoggerRoles` is no longer used; the `TicketLogger/Use` row replaced it.

Source of truth: `docs/user-management.md`.
