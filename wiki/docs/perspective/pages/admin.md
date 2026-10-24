---
title: Admin Pages
sidebar_position: 13
description: Groveport > Admin - the OPS Audit Log, User Management and Roles & Permissions pages.
sources:
  - docs/ops-audit.md
  - docs/user-management.md
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/AuditLog/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/UserManagement/UserManagement/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/RolesPermissions/view.json"
  - "docs/security-roles.md"
last_verified: 2026-10-24
---

# Admin Pages

The Admin folder of the nav holds three pages. Each nav leaf carries a `data.permission`, so the folder only shows
what the logged-in user may open.

| Nav (Groveport > Admin) | Route | View | Nav permission |
|---|---|---|---|
| Audit Log | `/operations/audit` | [`00_Pages/Boars Head/Operations/AuditLog`](../reference/views/00-pages/boars-head/operations/auditlog.md) | `AuditLog/View` |
| User Management | `/operations/users` | [`00_Pages/Boars Head/Operations/UserManagement/UserManagement`](../reference/views/00-pages/boars-head/operations/usermanagement/usermanagement.md) | `UserManagement/Edit` |
| Roles & Permissions | `/operations/roles-permissions` | [`00_Pages/Boars Head/Operations/RolesPermissions`](../reference/views/00-pages/boars-head/operations/rolespermissions.md) | `RolesPermissions/Edit` |

## OPS Audit Log

![Audit Log (user names blurred)](/img/perspective/audit-log.png)

Every operator action that the HMI writes (setpoint changes, commands, Out Of Service, configuration edits) leaves
an OpsAudit entry (`shared.Audit`). This page lists them.

- Parts: the page, the one-line cell view `00_Pages/Boars Head/Operations/_Assets/AuditLogCell` and the named query
  `OpsAudit/AuditLog`.
- Layout (no subtitle): title row with the event count, one filter bar (Range 24 Hours / 7 Days / 30 Days, Start, End, Search,
  Refresh), and a table that fills the rest of the height: Time, User, Action, Target (friendly device path, the raw
  tag path in the tooltip), Change (old to new), Source (the view that made the change). A row click opens a detail
  pane with the full values.
- Data: a named query binding (`OpsAudit/AuditLog`, dataset) whose parameters are expressions:

```js
startDate: {view.custom.startDate}
endDate:   {view.custom.endDate}
search:    if(trim(coalesce({view.custom.search}, '')) = '', '', '%' + trim(coalesce({view.custom.search}, '')) + '%')
allowed:   if(coalesce({session.custom.Permissions.AuditLog.View}, false), 1, 0)
refresh:   coalesce({view.custom.refresh}, 0)
```

  `allowed` puts the permission check in the SQL, the same pattern as the Out Of Service log.

## User Management

![User Management](/img/perspective/user-management.png)

Manages users and roles in the gateway internal user source **`default`**. Two tabs, **Users** and **Roles**.

- **Users tab**: a list card (search by name, username or role, a role filter, **Add User**; each row = avatar, name,
  username, first role and +N) and a detail card with Account (username is fixed after creation; Change Password with
  a confirm field that is outlined red while the two differ), Profile (first / last name, language, schedule, badge),
  Roles (option cards: name, user count, Full Access / Restricted badges), Contact Information (type + value rows)
  and Notes. Action bar: Delete User, status, Discard, Save User.
- **Roles tab**: the role list and an editor (Role Name, members read only, Delete Role / Save Role, Add Role). A rename
  shows a note: the matrix column and the `_Config/Security` role lists are **not** renamed with it.
- Every save or delete asks for confirmation; switching user with unsaved edits asks to discard. Service accounts
  (`admin`, `ops`, `opcuauser`) are hidden, restricted roles show only to users who hold them, there is no self-delete,
  and there is no enabled flag (the internal user source has none). Schedule adjustments are editable per user: in the Profile area each
  adjustment has Start, End, Available and Note fields, and **Add Adjustment** adds a row (Start must not be after End); they save with the user.
- All reads and writes go through `shared.UserAdmin` (`system.user.getUser / addUser / editUser / removeUser / addRole /
  editRole / removeRole`; `commit()` shows gateway errors in the Alert popup and writes the OpsAudit events
  "user add/edit/delete" and "role add/edit/delete"). Server checks: `UserManagement/Edit` (and `/Add` for new users
  and roles).
- Repeated rows are embedded views from `00_Pages/Boars Head/Operations/_Admin/` (`UMUserRow`, `UMRoleOption`,
  `UMContactRow`, `RoleItem`); styling is the `admin-*` style classes.

## Roles & Permissions

![Roles & Permissions](/img/perspective/roles-permissions.png)

The permission matrix, grouped and collapsible (laptop first, 1366 x 768, no horizontal scroll). Saving writes the
DataSet tag **`[default]_Config/RolesPermissions`**, which every session turns into `session.custom.Permissions` (see
[Security In The UI](../security-ui.md)).

- **Header card**: title, tabs **Permissions (N)** and **Roles (N)**, and a toolbar: search (label, key,
  description), a category dropdown, a role-focus multi-select (show one role or compare several), **Show Only
  Differences**, Expand All / Collapse All.
- **Matrix card** (the only scrolling area): a sticky head row (one column per role with its user count; a lock =
  full-permission role "Always All", a link = inherits). Rows are in collapsible **groups** (General, Devices,
  Alarms, Engineering, Operations, Administration, Other) with a count, a short description and a per-role granted
  count (`3/5`); clicking a role's count = **Grant All In Group** / **Revoke All** after a confirm (it only stages
  edits). Each row shows a friendly label, the `Devices/Actions` key chip and the description.
- **Cells**: a check box; a changed cell is highlighted with a dot; **Locked "All"** for the roles in
  `_Config/Security/FullPermissionRoles`; **Inherited** (grey tick + link, not clickable) where `RoleInherits` gives
  the role the tick (Engineering from Maintenance); read-only ticks if the viewer lacks `RolesPermissions/Edit`.
- **Change bar** under the matrix: "No Unsaved Changes" / "3 Unsaved Changes" / "Saved 3 changes" with Discard and
  **Save Changes** (a confirm lists the changes).
- **Roles tab**: each role's users, granted count and badges (Full Access / Inherits X / Restricted), plus a per-group
  summary computed on the gateway (`shared.PermissionMatrix.roleSummary`). **Edit In Matrix** jumps to the Permissions
  tab focused on that role. Adding, renaming or deleting roles stays on User Management.
- No access: an "Administrator Access Required" card.

How a row lands in a group: two DataSet tags,
`_Config/Security/PermissionCategories` (Name, Order, Icon, Description) and `_Config/Security/PermissionCatalog`
(Key, Category, Label, Order; a key is a Devices value or a `Devices/Actions` key). A new action on a known device lands
in its device's group by itself; a new device shows under **Other** until it has a catalog line.

Save behaviour: edits are staged in `custom.edits`; **Save** -> confirm -> `shared.PermissionMatrix.save(session,
edits)` checks `RolesPermissions/Edit` on the gateway, re-reads the tag right before the write, applies only the edited
cells with `system.dataset.setValue`, writes the base -> heir tick for `RoleInherits` pairs, skips full-permission
roles, writes once, and logs one OpsAudit event **Permissions Changed**.

- Source of truth: `docs/user-management.md`.

### How To Change It

- **Page layout:** Project Browser > Perspective > Views > `00_Pages/Boars Head/Operations` > `UserManagement` /
  `RolesPermissions` (parts in `_Admin`); edit the components and the `admin-*` style classes, save, test as an
  Administrator.
- **Save, load and group logic:** Project Library > `shared` > `PermissionMatrix` and `UserAdmin`.
- **Add a permission row or group:** edit the DataSet tags `[default]_Config/RolesPermissions`,
  `_Config/Security/PermissionCatalog` and `PermissionCategories` in the Tag Browser
  ([Roles And Permissions](../../features/roles-permissions.md#how-to-change-it)).
