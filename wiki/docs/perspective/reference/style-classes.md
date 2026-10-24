---
title: "Style Class Catalog"
sidebar_label: "Style Class Catalog"
description: "Every project style class (style-classes/) with its CSS and the views that use it."
generated: true
sidebar_position: 7
---

:::note

:::


Source: `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/style-classes/<name>/style.json` (Designer: Project Browser > Perspective > Styles). 204 style classes. Perspective emits each as `.psc-<name>` after the stylesheet, sorted by name. A view uses one by putting its name in `props.style.classes`.

## adhoc

### adhoc-trend-plot-title

```css
.psc-adhoc-trend-plot-title {
  font-weight: 600;
}
```

[98\_Configuration/AdhocTrend/\_Assets/Plot](./views/98-configuration/adhoctrend/assets/plot.md)

### adhoc-trend-toolbar-label

```css
.psc-adhoc-trend-toolbar-label {
  font-family: Bahnschrift, "Segoe UI", sans-serif;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--text-secondary);
}
```

[98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md)

## admin

### admin-avatar

```css
.psc-admin-avatar {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 700;
  color: var(--callToAction);
  background-color: var(--surface-page);
  border-radius: 50%;
  text-align: center;
}
```

[00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/UMUserRow](./views/00-pages/boars-head/operations/admin/umuserrow.md)

### admin-avatar-selected

```css
.psc-admin-avatar-selected {
  color: var(--neutral-10);
  background-color: var(--callToAction);
}
```

[00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md)

### admin-bar-pending

```css
.psc-admin-bar-pending {
  border-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-btn-danger

```css
.psc-admin-btn-danger {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--error);
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--error);
  border-radius: 4px;
  padding-left: 14px;
  padding-right: 14px;
}
```

[00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md)

### admin-cell

```css
.psc-admin-cell {
  border-radius: 0px;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md)

### admin-cell-changed

```css
.psc-admin-cell-changed {
  background-color: var(--callToActionHighlight);
}
```

[00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md)

### admin-cell-click

```css
.psc-admin-cell-click {
  cursor: pointer;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-cell-text

```css
.psc-admin-cell-text {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/RPBulk](./views/00-pages/boars-head/operations/admin/rpbulk.md), [00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md)

### admin-cell-text-muted

```css
.psc-admin-cell-text-muted {
  color: var(--text-muted);
}
```

[00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md)

### admin-chip

```css
.psc-admin-chip {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  background-color: var(--surface-page);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 9px;
  padding-left: 8px;
  padding-right: 8px;
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/RoleItem](./views/00-pages/boars-head/operations/admin/roleitem.md), [00\_Pages/Boars Head/Operations/\_Admin/UMUserRow](./views/00-pages/boars-head/operations/admin/umuserrow.md)

### admin-count

```css
.psc-admin-count {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  background-color: var(--surface-card);
  border-radius: 9px;
  padding-left: 7px;
  padding-right: 7px;
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./views/00-pages/boars-head/operations/admin/nrgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./views/00-pages/boars-head/operations/admin/rpgroup.md)

### admin-desc

```css
.psc-admin-desc {
  font-family: sans-serif;
  font-size: 12px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./views/00-pages/boars-head/operations/admin/nrgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/NRRow](./views/00-pages/boars-head/operations/admin/nrrow.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./views/00-pages/boars-head/operations/admin/rpgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/RPRow](./views/00-pages/boars-head/operations/admin/rprow.md), [00\_Pages/Boars Head/Operations/\_Admin/RoleItem](./views/00-pages/boars-head/operations/admin/roleitem.md), [00\_Pages/Boars Head/Operations/\_Admin/UMRoleOption](./views/00-pages/boars-head/operations/admin/umroleoption.md), [00\_Pages/Boars Head/Operations/\_Admin/UMUserRow](./views/00-pages/boars-head/operations/admin/umuserrow.md)

### admin-dot

```css
.psc-admin-dot {
  background-color: var(--callToAction);
  border-radius: 3px;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md)

### admin-empty-title

```css
.psc-admin-empty-title {
  font-family: sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  text-align: center;
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md)

### admin-group

```css
.psc-admin-group {
  background-color: var(--surface-page);
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: var(--border);
  cursor: pointer;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./views/00-pages/boars-head/operations/admin/nrgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./views/00-pages/boars-head/operations/admin/rpgroup.md)

### admin-group-name

```css
.psc-admin-group-name {
  font-family: sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./views/00-pages/boars-head/operations/admin/nrgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./views/00-pages/boars-head/operations/admin/rpgroup.md)

### admin-head-label

```css
.psc-admin-head-label {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md)

### admin-head-sub

```css
.psc-admin-head-sub {
  font-family: sans-serif;
  font-size: 11px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/\_Admin/RPRoleHead](./views/00-pages/boars-head/operations/admin/rprolehead.md), [00\_Pages/Boars Head/Operations/\_Admin/RPRow](./views/00-pages/boars-head/operations/admin/rprow.md)

### admin-ico-muted

```css
.psc-admin-ico-muted {
  color: var(--text-muted);
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./views/00-pages/boars-head/operations/admin/nrgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md), [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./views/00-pages/boars-head/operations/admin/rpgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/RPRoleHead](./views/00-pages/boars-head/operations/admin/rprolehead.md), [00\_Pages/Boars Head/Operations/\_Admin/RoleItem](./views/00-pages/boars-head/operations/admin/roleitem.md), [00\_Pages/Boars Head/Operations/\_Admin/UMAdjustRow](./views/00-pages/boars-head/operations/admin/umadjustrow.md), [00\_Pages/Boars Head/Operations/\_Admin/UMContactRow](./views/00-pages/boars-head/operations/admin/umcontactrow.md)

### admin-ico-off

```css
.psc-admin-ico-off {
  color: var(--border-strong);
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./views/00-pages/boars-head/operations/admin/nrgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md), [00\_Pages/Boars Head/Operations/\_Admin/UMRoleOption](./views/00-pages/boars-head/operations/admin/umroleoption.md)

### admin-ico-on

```css
.psc-admin-ico-on {
  color: var(--callToAction);
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./views/00-pages/boars-head/operations/admin/nrgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/NRRow](./views/00-pages/boars-head/operations/admin/nrrow.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/RPBulk](./views/00-pages/boars-head/operations/admin/rpbulk.md), [00\_Pages/Boars Head/Operations/\_Admin/RPCell](./views/00-pages/boars-head/operations/admin/rpcell.md), [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./views/00-pages/boars-head/operations/admin/rpgroup.md), [00\_Pages/Boars Head/Operations/\_Admin/RoleItem](./views/00-pages/boars-head/operations/admin/roleitem.md)

### admin-item-title

```css
.psc-admin-item-title {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/RoleItem](./views/00-pages/boars-head/operations/admin/roleitem.md), [00\_Pages/Boars Head/Operations/\_Admin/UMUserRow](./views/00-pages/boars-head/operations/admin/umuserrow.md)

### admin-key

```css
.psc-admin-key {
  font-family: monospace;
  font-size: 10px;
  color: var(--text-muted);
  background-color: var(--surface-page);
  border-radius: 3px;
  padding-left: 5px;
  padding-right: 5px;
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRRow](./views/00-pages/boars-head/operations/admin/nrrow.md), [00\_Pages/Boars Head/Operations/\_Admin/RPRow](./views/00-pages/boars-head/operations/admin/rprow.md)

### admin-list-item

```css
.psc-admin-list-item {
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: var(--border);
  border-left-width: 3px;
  border-left-style: solid;
  border-left-color: transparent;
  cursor: pointer;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-list-item-selected

```css
.psc-admin-list-item-selected {
  background-color: var(--callToActionHighlight);
  border-left-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-matrix-head

```css
.psc-admin-matrix-head {
  background-color: var(--surface-page);
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: var(--border);
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md)

### admin-note

```css
.psc-admin-note {
  font-family: sans-serif;
  font-size: 12px;
  color: var(--text);
  background-color: var(--surface-page);
  border-radius: 4px;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 12px;
  padding-right: 12px;
  white-space: normal;
}
```

[00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md)

### admin-option

```css
.psc-admin-option {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
  cursor: pointer;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-option-on

```css
.psc-admin-option-on {
  background-color: var(--callToActionHighlight);
  border-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-role-name

```css
.psc-admin-role-name {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/RPRoleHead](./views/00-pages/boars-head/operations/admin/rprolehead.md)

### admin-row

```css
.psc-admin-row {
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: color-mix(in srgb, var(--border) 60%, transparent);
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRRow](./views/00-pages/boars-head/operations/admin/nrrow.md), [00\_Pages/Boars Head/Operations/\_Admin/RPRow](./views/00-pages/boars-head/operations/admin/rprow.md)

### admin-row-label

```css
.psc-admin-row-label {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NRRow](./views/00-pages/boars-head/operations/admin/nrrow.md), [00\_Pages/Boars Head/Operations/\_Admin/RPRow](./views/00-pages/boars-head/operations/admin/rprow.md), [00\_Pages/Boars Head/Operations/\_Admin/UMRoleOption](./views/00-pages/boars-head/operations/admin/umroleoption.md)

### admin-section-label

```css
.psc-admin-section-label {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md)

### admin-status-pending

```css
.psc-admin-status-pending {
  color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-step-dot

```css
.psc-admin-step-dot {
  background-color: var(--surface-page);
  border-radius: 11px;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-step-dot-on

```css
.psc-admin-step-dot-on {
  background-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-step-label

```css
.psc-admin-step-label {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md)

### admin-step-label-on

```css
.psc-admin-step-label-on {
  color: var(--text);
  font-weight: 700;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-step-line

```css
.psc-admin-step-line {
  background-color: var(--border);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-step-line-on

```css
.psc-admin-step-line-on {
  background-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-step-num

```css
.psc-admin-step-num {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-step-num-on

```css
.psc-admin-step-num-on {
  color: var(--neutral-10);
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md)

### admin-sub

```css
.psc-admin-sub {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/\_Admin/RPRow](./views/00-pages/boars-head/operations/admin/rprow.md)

### admin-tab

```css
.psc-admin-tab {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  background-color: transparent;
  border-radius: 4px;
  padding-left: 14px;
  padding-right: 14px;
  cursor: pointer;
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md)

### admin-tab-active

```css
.psc-admin-tab-active {
  color: var(--neutral-10);
  background-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### admin-tabs

```css
.psc-admin-tabs {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border-strong);
  border-radius: 6px;
  padding-top: 3px;
  padding-bottom: 3px;
  padding-left: 3px;
  padding-right: 3px;
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md)

### admin-toolbar

```css
.psc-admin-toolbar {
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: var(--border);
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md)

## bg

### bg-page

```css
.psc-bg-page {
  background-color: var(--surface-page);
}
```

<details>
<summary>Used in 99 views</summary>

[00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Design](./views/00-pages/boars-head/exhaustfans/design.md), [00\_Pages/Boars Head/ExhaustFans/Details](./views/00-pages/boars-head/exhaustfans/details.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/LandingPage/Globe](./views/00-pages/boars-head/landingpage/globe.md), [00\_Pages/Boars Head/LandingPage/PlantPlaceholder](./views/00-pages/boars-head/landingpage/plantplaceholder.md), [00\_Pages/Boars Head/Machine Room/Overview](./views/00-pages/boars-head/machine-room/overview.md), [00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Pumps/Design](./views/00-pages/boars-head/pumps/design.md), [00\_Pages/Boars Head/Pumps/Details](./views/00-pages/boars-head/pumps/details.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Design](./views/00-pages/boars-head/sensors/design.md), [00\_Pages/Boars Head/Sensors/Details](./views/00-pages/boars-head/sensors/details.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Design](./views/00-pages/boars-head/tanks/design.md), [00\_Pages/Boars Head/Tanks/Details](./views/00-pages/boars-head/tanks/details.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Design](./views/00-pages/boars-head/valves/design.md), [00\_Pages/Boars Head/Valves/Details](./views/00-pages/boars-head/valves/details.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Area/DomainKpis](./views/00-pages/groveport/area/domainkpis.md), [00\_Pages/Groveport/Club/Utility/CG-C1](./views/00-pages/groveport/club/utility/cg-c1.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Design](./views/00-pages/groveport/condensers/utility/condenserfans/design.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Design](./views/00-pages/groveport/condensers/utility/pumps/design.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Design](./views/00-pages/groveport/condensers/utility/sensors/design.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Design](./views/00-pages/groveport/condensers/utility/tanks/design.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Design](./views/00-pages/groveport/condensers/utility/valves/design.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Dock/Utility/CG-G1](./views/00-pages/groveport/dock/utility/cg-g1.md), [00\_Pages/Groveport/Dock/Utility/CG-G2](./views/00-pages/groveport/dock/utility/cg-g2.md), [00\_Pages/Groveport/Dock/Utility/CG-G3](./views/00-pages/groveport/dock/utility/cg-g3.md), [00\_Pages/Groveport/Dock/Utility/CG-G4](./views/00-pages/groveport/dock/utility/cg-g4.md), [00\_Pages/Groveport/Dock/Utility/CG-G5](./views/00-pages/groveport/dock/utility/cg-g5.md), [00\_Pages/Groveport/East PH/Utility/CG-E1](./views/00-pages/groveport/east-ph/utility/cg-e1.md), [00\_Pages/Groveport/East PH/Utility/CG-E2](./views/00-pages/groveport/east-ph/utility/cg-e2.md), [00\_Pages/Groveport/East PH/Utility/CG-E3](./views/00-pages/groveport/east-ph/utility/cg-e3.md), [00\_Pages/Groveport/East PH/Utility/CG-E4](./views/00-pages/groveport/east-ph/utility/cg-e4.md), [00\_Pages/Groveport/Freezer/Utility/CG-A1](./views/00-pages/groveport/freezer/utility/cg-a1.md), [00\_Pages/Groveport/Freezer/Utility/CG-A2](./views/00-pages/groveport/freezer/utility/cg-a2.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Design](./views/00-pages/groveport/machine-room/utility/compressors/design.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Details](./views/00-pages/groveport/machine-room/utility/compressors/details.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](./views/00-pages/groveport/machine-room/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](./views/00-pages/groveport/machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](./views/00-pages/groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/PlcOverview](./views/00-pages/groveport/operations/plcoverview.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Palletizing/Utility/CG-D1](./views/00-pages/groveport/palletizing/utility/cg-d1.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/SuperChill/Utility/CG-B1](./views/00-pages/groveport/superchill/utility/cg-b1.md), [00\_Pages/Groveport/SuperChill/Utility/CG-B2](./views/00-pages/groveport/superchill/utility/cg-b2.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/West PH/Utility/CG-F1](./views/00-pages/groveport/west-ph/utility/cg-f1.md), [00\_Pages/Groveport/West PH/Utility/CG-F2](./views/00-pages/groveport/west-ph/utility/cg-f2.md), [00\_Pages/Groveport/West PH/Utility/CG-F3](./views/00-pages/groveport/west-ph/utility/cg-f3.md), [00\_Pages/Groveport/West PH/Utility/CG-F4](./views/00-pages/groveport/west-ph/utility/cg-f4.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./views/00-pages/groveport/shared/cg/ahuevapdisplay.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/PlcRack/CardDetail](./views/01-popups/00-faceplates/plcrack/carddetail.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/ComponentPreview/Condenser-SafetyRelay](./views/98-configuration/componentpreview/condenser-safetyrelay.md), [98\_Configuration/ComponentPreview/VesselGeneric](./views/98-configuration/componentpreview/vesselgeneric.md)

</details>

## color

### color-icon

```css
.psc-color-icon {
  color: var(--icon);
}
```

<details>
<summary>Used in 18 views</summary>

[00\_Pages/00\_Docked/Header](./views/00-pages/00-docked/header.md), [00\_Pages/00\_Docked/\_Assets/AlarmNotification](./views/00-pages/00-docked/assets/alarmnotification.md), [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./views/00-pages/00-docked/assets/integratorcontact.md), [00\_Pages/00\_Docked/\_Assets/OosNotification](./views/00-pages/00-docked/assets/oosnotification.md), [00\_Pages/00\_Docked/\_Assets/User](./views/00-pages/00-docked/assets/user.md), [00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./views/00-pages/00-docked/assets/userrolesandlogin.md), [00\_Pages/00\_Docked/\_Assets/UserSettings](./views/00-pages/00-docked/assets/usersettings.md), [01\_Popups/00\_Faceplates/AdhocTrend](./views/01-popups/00-faceplates/adhoctrend.md), [01\_Popups/00\_Faceplates/AdhocTrendConfig](./views/01-popups/00-faceplates/adhoctrendconfig.md), [01\_Popups/00\_Faceplates/DischargeSequence](./views/01-popups/00-faceplates/dischargesequence.md), [01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/Faceplate](./views/01-popups/00-faceplates/faceplate.md), [01\_Popups/00\_Faceplates/Interlock](./views/01-popups/00-faceplates/interlock.md), [01\_Popups/00\_Faceplates/SuctionSequence](./views/01-popups/00-faceplates/suctionsequence.md), [01\_Popups/00\_Faceplates/TankOverview](./views/01-popups/00-faceplates/tankoverview.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

</details>

## container

### container-button

```css
.psc-container-button {
  background-color: var(--text-muted);
  border-style: none;
  box-shadow: var(--boxShadow1);
}
```

[00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./views/00-pages/00-docked/assets/userrolesandlogin.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [01\_Popups/00\_Faceplates/Faceplate](./views/01-popups/00-faceplates/faceplate.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/NamePlot](./views/98-configuration/adhoctrend/assets/nameplot.md), [98\_Configuration/AdhocTrend/\_Assets/RemovePlot](./views/98-configuration/adhoctrend/assets/removeplot.md), [98\_Configuration/AdhocTrend/\_Assets/SaveTrendConfig](./views/98-configuration/adhoctrend/assets/savetrendconfig.md), [98\_Configuration/AdhocTrend/\_Assets/ToolBar](./views/98-configuration/adhoctrend/assets/toolbar.md), [98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/Integrations](./views/98-configuration/integrations.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

## faceplate

### faceplate-alarm-name

```css
.psc-faceplate-alarm-name {
  font-size: 14px;
  font-weight: 600;
  text-align: center;
  overflow: hidden;
  white-space: nowrap;
}
```

[01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./views/01-popups/00-faceplates/assets/alarmconfigurationrow.md)

### faceplate-alarm-notes

```css
.psc-faceplate-alarm-notes {
  font-size: 11px;
  text-align: center;
  color: var(--text-muted);
}
```

[01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./views/01-popups/00-faceplates/assets/alarmconfigurationrow.md)

### faceplate-bypass-banner

```css
.psc-faceplate-bypass-banner {
  color: var(--status-level-warning, #fbc02d);
  font-weight: 700;
}
```

[01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md)

### faceplate-cmd-btn

```css
.psc-faceplate-cmd-btn {
  padding: 4px 10px;
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 4px;
  background-color: var(--surface-container);
  color: var(--text);
  font-size: 11px;
  font-weight: 600;
}
```

<details>
<summary>Used in 32 views</summary>

[00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](./views/00-pages/groveport/machine-room/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](./views/00-pages/groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/\_Assets/HistoryActions](./views/00-pages/groveport/operations/forms/assets/historyactions.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./views/00-pages/groveport/shared/cg/ahuevapdisplay.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./views/01-popups/00-faceplates/assets/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_Position](./views/01-popups/00-faceplates/assets/valve/cmd-position.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md), [01\_Popups/TrendContext/QuickHistory](./views/01-popups/trendcontext/quickhistory.md), [02\_Components/00\_Controls/InterlockButton](./views/02-components/00-controls/interlockbutton.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/02\_Widgets/Safetys](./views/02-components/02-widgets/safetys.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md)

</details>

### faceplate-cmd-btn-active

```css
.psc-faceplate-cmd-btn-active {
  border-color: var(--text);
  background-color: var(--surface-card);
}
```

[01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md)

### faceplate-cmd-btn-bypass

```css
.psc-faceplate-cmd-btn-bypass {
  border-color: var(--status-level-warning, #fbc02d);
  background-color: var(--status-level-warning, #fbc02d);
  color: #212121;
}
```

[01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md)

### faceplate-config-empty

```css
.psc-faceplate-config-empty {
  color: var(--text-muted);
  font-size: 12px;
}
```

[01\_Popups/00\_Faceplates/\_Assets/Configuration/Configuration](./views/01-popups/00-faceplates/assets/configuration/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./views/01-popups/00-faceplates/assets/interlocks.md)

### faceplate-fault-chip

```css
.psc-faceplate-fault-chip {
  padding: 4px 6px;
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 4px;
  background-color: var(--surface-container);
}
```

[01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md)

### faceplate-fault-code

```css
.psc-faceplate-fault-code {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: var(--text-muted);
}
```

[01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md)

### faceplate-interlock-sts

```css
.psc-faceplate-interlock-sts {
  font-family: monospace;
  font-size: 11px;
  text-align: center;
}
```

[01\_Popups/00\_Faceplates/\_Assets/InterlockRow](./views/01-popups/00-faceplates/assets/interlockrow.md)

### faceplate-kpi-label

```css
.psc-faceplate-kpi-label {
  font-size: 12px;
  font-weight: 700;
  white-space: nowrap;
}
```

[01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](./views/01-popups/00-faceplates/assets/dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./views/01-popups/00-faceplates/assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md)

### faceplate-mode-btn-label

```css
.psc-faceplate-mode-btn-label {
  font-size: 10px;
  font-weight: 600;
  line-height: 1.1;
  white-space: nowrap;
}
```

[01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md)

### faceplate-mode-code

```css
.psc-faceplate-mode-code {
  font-size: 12px;
  color: var(--text);
  font-weight: 600;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### faceplate-section

```css
.psc-faceplate-section {
  margin-bottom: 12px;
}
```

<details>
<summary>Used in 26 views</summary>

[00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](./views/01-popups/00-faceplates/assets/configuration/configsection.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/Configuration](./views/01-popups/00-faceplates/assets/configuration/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](./views/01-popups/00-faceplates/assets/dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./views/01-popups/00-faceplates/assets/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./views/01-popups/00-faceplates/assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md)

</details>

### faceplate-section-card

```css
.psc-faceplate-section-card {
  background-color: var(--surface-card);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 4px;
  padding: 8px 10px;
  margin-bottom: 8px;
  overflow: hidden;
}
```

<details>
<summary>Used in 24 views</summary>

[00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](./views/01-popups/00-faceplates/assets/configuration/configsection.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](./views/01-popups/00-faceplates/assets/dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./views/01-popups/00-faceplates/assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md)

</details>

### faceplate-section-title

```css
.psc-faceplate-section-title {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--text-muted);
  margin-bottom: 4px;
}
```

<details>
<summary>Used in 25 views</summary>

[00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./views/01-popups/00-faceplates/assets/alarmconfiguration.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](./views/01-popups/00-faceplates/assets/configuration/configsection.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](./views/01-popups/00-faceplates/assets/dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./views/01-popups/00-faceplates/assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md)

</details>

### faceplate-stub

```css
.psc-faceplate-stub {
  font-size: 12px;
  color: var(--text-muted);
  padding: 8px;
  border-width: 1px;
  border-style: dashed;
  border-color: var(--border);
  border-radius: 6px;
  background-color: var(--surface-container);
}
```

[01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./views/01-popups/00-faceplates/assets/alarmconfiguration.md)

### faceplate-title

```css
.psc-faceplate-title {
  font-weight: 700;
  font-size: 16px;
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
}
```

[01\_Popups/00\_Faceplates/DischargeSequence](./views/01-popups/00-faceplates/dischargesequence.md), [01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/Faceplate](./views/01-popups/00-faceplates/faceplate.md), [01\_Popups/00\_Faceplates/Interlock](./views/01-popups/00-faceplates/interlock.md), [01\_Popups/00\_Faceplates/SuctionSequence](./views/01-popups/00-faceplates/suctionsequence.md), [01\_Popups/00\_Faceplates/TankOverview](./views/01-popups/00-faceplates/tankoverview.md)

## Fonts

### Fonts/BadData

```css
.psc-Fonts\/BadData {
  color: var(--text-muted);
  font-family: sans-serif;
  font-size: 0.9em;
  font-style: italic;
  font-weight: 500;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### Fonts/Button

```css
.psc-Fonts\/Button {
  color: var(--text-inverse);
  font-family: sans-serif;
  font-size: 0.8rem;
  font-weight: normal;
}
```

<details>
<summary>Used in 14 views</summary>

[00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./views/00-pages/00-docked/assets/userrolesandlogin.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [01\_Popups/00\_Faceplates/Faceplate](./views/01-popups/00-faceplates/faceplate.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/NamePlot](./views/98-configuration/adhoctrend/assets/nameplot.md), [98\_Configuration/AdhocTrend/\_Assets/RemovePlot](./views/98-configuration/adhoctrend/assets/removeplot.md), [98\_Configuration/AdhocTrend/\_Assets/SaveTrendConfig](./views/98-configuration/adhoctrend/assets/savetrendconfig.md), [98\_Configuration/AdhocTrend/\_Assets/ToolBar](./views/98-configuration/adhoctrend/assets/toolbar.md), [98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/Integrations](./views/98-configuration/integrations.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

</details>

### Fonts/Header

```css
.psc-Fonts\/Header {
  color: var(--text-secondary);
  font-family: sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
}
```

[00\_Pages/00\_Docked/\_Assets/ChangeTheme](./views/00-pages/00-docked/assets/changetheme.md), [01\_Popups/00\_Faceplates/Alerts/Alert](./views/01-popups/00-faceplates/alerts/alert.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md)

### Fonts/Label

```css
.psc-Fonts\/Label {
  font-family: sans-serif;
  font-size: 0.8rem;
  font-weight: 500;
}
```

<details>
<summary>Used in 127 views</summary>

[00\_Pages/00\_Docked/Legend](./views/00-pages/00-docked/legend.md), [00\_Pages/00\_Docked/Navigation](./views/00-pages/00-docked/navigation.md), [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./views/00-pages/00-docked/assets/integratorcontact.md), [00\_Pages/00\_Docked/\_Assets/PlcWriteLock](./views/00-pages/00-docked/assets/plcwritelock.md), [00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./views/00-pages/00-docked/assets/userrolesandlogin.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Alarms/\_Assets/AlarmJournalTable](./views/00-pages/boars-head/alarms/assets/alarmjournaltable.md), [00\_Pages/Boars Head/Alarms/\_Assets/AlarmStatusTable](./views/00-pages/boars-head/alarms/assets/alarmstatustable.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/DesignOverview](./views/00-pages/boars-head/devices/designoverview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/LandingPage/PlantPlaceholder](./views/00-pages/boars-head/landingpage/plantplaceholder.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/CommentEntry](./views/00-pages/boars-head/operations/outofservice/assets/commententry.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](./views/00-pages/groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/\_Assets/HistoryActions](./views/00-pages/groveport/operations/forms/assets/historyactions.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewKpis](./views/00-pages/groveport/utility/overviewkpis.md), [00\_Pages/Groveport/Utility/OverviewStatusTile](./views/00-pages/groveport/utility/overviewstatustile.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./views/00-pages/groveport/shared/cg/ahuevapdisplay.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapHistory](./views/00-pages/groveport/shared/cg/ahuevaphistory.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapStatusBar](./views/00-pages/groveport/shared/cg/ahuevapstatusbar.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./views/01-popups/00-faceplates/assets/alarmconfiguration.md), [01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./views/01-popups/00-faceplates/assets/alarmconfigurationrow.md), [01\_Popups/00\_Faceplates/\_Assets/Alarms](./views/01-popups/00-faceplates/assets/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./views/01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](./views/01-popups/00-faceplates/assets/configuration/configsection.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/Configuration](./views/01-popups/00-faceplates/assets/configuration/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](./views/01-popups/00-faceplates/assets/dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockRow](./views/01-popups/00-faceplates/assets/interlockrow.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./views/01-popups/00-faceplates/assets/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Modes](./views/01-popups/00-faceplates/assets/modes.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./views/01-popups/00-faceplates/assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./views/01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./views/01-popups/00-faceplates/assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [01\_Popups/00\_Faceplates/\_Assets/Trend](./views/01-popups/00-faceplates/assets/trend.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./views/01-popups/00-faceplates/assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_MO](./views/01-popups/00-faceplates/assets/valve/cmd-mo.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_Position](./views/01-popups/00-faceplates/assets/valve/cmd-position.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_SO](./views/01-popups/00-faceplates/assets/valve/cmd-so.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./views/01-popups/00-faceplates/assets/valve/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./views/01-popups/00-faceplates/assets/valve/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md), [01\_Popups/TrendContext/CopyPath](./views/01-popups/trendcontext/copypath.md), [01\_Popups/TrendContext/Menu](./views/01-popups/trendcontext/menu.md), [01\_Popups/TrendContext/QuickHistory](./views/01-popups/trendcontext/quickhistory.md), [01\_Popups/TrendContext/Toast](./views/01-popups/trendcontext/toast.md), [02\_Components/00\_Controls/InterlockButton](./views/02-components/00-controls/interlockbutton.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md), [02\_Components/02\_Widgets/MetricCard](./views/02-components/02-widgets/metriccard.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [03\_Elements/00\_Control/AnalogInput](./views/03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/MultiStateInput](./views/03-elements/00-control/multistateinput.md), [03\_Elements/00\_Control/StringInput](./views/03-elements/00-control/stringinput.md), [03\_Elements/00\_Control/TimeInput](./views/03-elements/00-control/timeinput.md), [03\_Elements/00\_Control/\_Assets/Numeric](./views/03-elements/00-control/assets/numeric.md), [03\_Elements/03\_Table/DeviceLabelAlarmIndicator](./views/03-elements/03-table/devicelabelalarmindicator.md), [03\_Elements/03\_Table/DisplayTrend](./views/03-elements/03-table/displaytrend.md), [03\_Elements/03\_Table/Numeric](./views/03-elements/03-table/numeric.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/Plot](./views/98-configuration/adhoctrend/assets/plot.md), [98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/Integrations](./views/98-configuration/integrations.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

</details>

### Fonts/LiveData

```css
.psc-Fonts\/LiveData {
  color: var(--callToAction);
  font-family: sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
}
```

[03\_Elements/03\_Table/Boolean](./views/03-elements/03-table/boolean.md), [03\_Elements/03\_Table/StateText](./views/03-elements/03-table/statetext.md)

### Fonts/LiveDataEntry

```css
.psc-Fonts\/LiveDataEntry {
  color: var(--qual-7, var(--accent));
  font-family: Roboto-Mono, monospace;
  font-weight: bold;
}
```

[00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/Utility/OverviewKpis](./views/00-pages/groveport/utility/overviewkpis.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md), [02\_Components/02\_Widgets/MetricCard](./views/02-components/02-widgets/metriccard.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md)

### Fonts/Title

```css
.psc-Fonts\/Title {
  color: var(--text-secondary);
  font-family: sans-serif;
  font-size: 1rem;
  font-weight: 400;
}
```

<details>
<summary>Used in 64 views</summary>

[00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/DetailsOverview](./views/00-pages/boars-head/devices/detailsoverview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/LandingPage/PlantPlaceholder](./views/00-pages/boars-head/landingpage/plantplaceholder.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](./views/00-pages/groveport/machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](./views/00-pages/groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapHistory](./views/00-pages/groveport/shared/cg/ahuevaphistory.md), [01\_Popups/00\_Faceplates/AdhocTrend](./views/01-popups/00-faceplates/adhoctrend.md), [01\_Popups/00\_Faceplates/AdhocTrendConfig](./views/01-popups/00-faceplates/adhoctrendconfig.md), [01\_Popups/00\_Faceplates/DischargeSequence](./views/01-popups/00-faceplates/dischargesequence.md), [01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/Faceplate](./views/01-popups/00-faceplates/faceplate.md), [01\_Popups/00\_Faceplates/Interlock](./views/01-popups/00-faceplates/interlock.md), [01\_Popups/00\_Faceplates/SuctionSequence](./views/01-popups/00-faceplates/suctionsequence.md), [01\_Popups/00\_Faceplates/TankOverview](./views/01-popups/00-faceplates/tankoverview.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md), [02\_Components/02\_Widgets/MetricCard](./views/02-components/02-widgets/metriccard.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/ToolBar](./views/98-configuration/adhoctrend/assets/toolbar.md), [98\_Configuration/ComponentPreview/Condenser-SafetyRelay](./views/98-configuration/componentpreview/condenser-safetyrelay.md), [98\_Configuration/ComponentPreview/VesselGeneric](./views/98-configuration/componentpreview/vesselgeneric.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

</details>

### Fonts/Value

```css
.psc-Fonts\/Value {
  font-family: sans-serif;
  font-size: 0.8rem;
  font-weight: normal;
}
```

<details>
<summary>Used in 85 views</summary>

[00\_Pages/00\_Docked/\_Assets/AlarmNotification](./views/00-pages/00-docked/assets/alarmnotification.md), [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./views/00-pages/00-docked/assets/integratorcontact.md), [00\_Pages/00\_Docked/\_Assets/OosNotification](./views/00-pages/00-docked/assets/oosnotification.md), [00\_Pages/00\_Docked/\_Assets/User](./views/00-pages/00-docked/assets/user.md), [00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./views/00-pages/00-docked/assets/userrolesandlogin.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/CommentEntry](./views/00-pages/boars-head/operations/outofservice/assets/commententry.md), [00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewStatusTile](./views/00-pages/groveport/utility/overviewstatustile.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/Alerts/Alert](./views/01-popups/00-faceplates/alerts/alert.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./views/01-popups/00-faceplates/assets/alarmconfigurationrow.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./views/01-popups/00-faceplates/assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./views/01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./views/01-popups/00-faceplates/assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DischargeSequence/Controls](./views/01-popups/00-faceplates/assets/dischargesequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockRow](./views/01-popups/00-faceplates/assets/interlockrow.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./views/01-popups/00-faceplates/assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./views/01-popups/00-faceplates/assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Cmd\_Position](./views/01-popups/00-faceplates/assets/valve/cmd-position.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./views/01-popups/00-faceplates/assets/valve/interlocks.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/\_Assets/SavedListRow](./views/01-popups/reports/assets/savedlistrow.md), [01\_Popups/TrendContext/CopyPath](./views/01-popups/trendcontext/copypath.md), [01\_Popups/TrendContext/Menu](./views/01-popups/trendcontext/menu.md), [01\_Popups/TrendContext/Toast](./views/01-popups/trendcontext/toast.md), [02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](./views/02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](./views/02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](./views/02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](./views/02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/01\_Devices/Pump](./views/02-components/01-devices/pump.md), [02\_Components/01\_Devices/SafetyRelay](./views/02-components/01-devices/safetyrelay.md), [02\_Components/01\_Devices/Sensor](./views/02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](./views/02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md), [02\_Components/02\_Widgets/Safetys](./views/02-components/02-widgets/safetys.md), [02\_Components/03\_PLC/PointRow](./views/02-components/03-plc/pointrow.md), [03\_Elements/00\_Control/AnalogInput](./views/03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/MultiStateInput](./views/03-elements/00-control/multistateinput.md), [03\_Elements/00\_Control/StringInput](./views/03-elements/00-control/stringinput.md), [03\_Elements/00\_Control/TimeInput](./views/03-elements/00-control/timeinput.md), [03\_Elements/00\_Control/\_Assets/Numeric](./views/03-elements/00-control/assets/numeric.md), [03\_Elements/01\_Status/StatusDot](./views/03-elements/01-status/statusdot.md), [03\_Elements/03\_Table/CgHit](./views/03-elements/03-table/cghit.md), [98\_Configuration/AdhocTrend/Trend](./views/98-configuration/adhoctrend/trend.md), [98\_Configuration/AdhocTrend/\_Assets/NamePlot](./views/98-configuration/adhoctrend/assets/nameplot.md), [98\_Configuration/AdhocTrend/\_Assets/Pen](./views/98-configuration/adhoctrend/assets/pen.md), [98\_Configuration/AdhocTrend/\_Assets/PenPlot](./views/98-configuration/adhoctrend/assets/penplot.md), [98\_Configuration/AdhocTrend/\_Assets/RemovePlot](./views/98-configuration/adhoctrend/assets/removeplot.md), [98\_Configuration/AdhocTrend/\_Assets/SaveTrendConfig](./views/98-configuration/adhoctrend/assets/savetrendconfig.md), [98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/Integrations](./views/98-configuration/integrations.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

</details>

## form

### form-banner

```css
.psc-form-banner {
  font-family: sans-serif;
  font-size: 13px;
  color: var(--text);
  background-color: var(--surface-card);
  border-left-width: 4px;
  border-left-style: solid;
  border-left-color: var(--callToAction);
  border-radius: 6px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 16px;
  padding-right: 16px;
}
```

[00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-banner-error

```css
.psc-form-banner-error {
  border-left-color: var(--error);
  background-color: color-mix(in srgb, var(--error) 10%, var(--surface-card));
}
```

[00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### form-banner-ok

```css
.psc-form-banner-ok {
  border-left-color: var(--sts-run, #228B22);
}
```

[00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md)

### form-btn

```css
.psc-form-btn {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border-strong);
  border-radius: 4px;
  padding-left: 16px;
  padding-right: 16px;
}
```

<details>
<summary>Used in 17 views</summary>

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [01\_Popups/Reports/DownloadMenu](./views/01-popups/reports/downloadmenu.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [01\_Popups/Reports/\_Assets/SavedListRow](./views/01-popups/reports/assets/savedlistrow.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

</details>

### form-btn-primary

```css
.psc-form-btn-primary {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--neutral-10);
  background-color: var(--callToAction);
  border-width: 1px;
  border-style: solid;
  border-color: var(--callToAction);
  border-radius: 4px;
  padding-left: 20px;
  padding-right: 20px;
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-calc

```css
.psc-form-calc {
  font-family: sans-serif;
  font-size: 15px;
  font-weight: 700;
  color: var(--callToAction);
}
```

[00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md)

### form-card

```css
.psc-form-card {
  background-color: var(--surface-card);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
}
```

<details>
<summary>Used in 14 views</summary>

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/Reports/DownloadMenu](./views/01-popups/reports/downloadmenu.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

</details>

### form-check

```css
.psc-form-check {
  font-family: sans-serif;
  font-size: 13px;
  color: var(--text);
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/UMAdjustRow](./views/00-pages/boars-head/operations/admin/umadjustrow.md), [00\_Pages/Boars Head/Operations/\_Assets/AuditLogCell](./views/00-pages/boars-head/operations/assets/auditlogcell.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [01\_Popups/Reports/\_Assets/CheckItem](./views/01-popups/reports/assets/checkitem.md), [01\_Popups/Reports/\_Assets/SectionItem](./views/01-popups/reports/assets/sectionitem.md)

### form-hint

```css
.psc-form-hint {
  font-family: sans-serif;
  font-size: 11px;
  color: var(--text-muted);
}
```

[00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/TwoLineCell](./views/00-pages/boars-head/operations/outofservice/assets/twolinecell.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-input

```css
.psc-form-input {
  font-family: sans-serif;
  font-size: 13px;
  color: var(--text);
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border-strong);
  border-radius: 4px;
  box-sizing: border-box;
}
```

<details>
<summary>Used in 15 views</summary>

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/UMAdjustRow](./views/00-pages/boars-head/operations/admin/umadjustrow.md), [00\_Pages/Boars Head/Operations/\_Admin/UMContactRow](./views/00-pages/boars-head/operations/admin/umcontactrow.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [01\_Popups/Reports/\_Assets/SectionItem](./views/01-popups/reports/assets/sectionitem.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

</details>

### form-input-required

```css
.psc-form-input-required {
  border-color: var(--error);
  box-shadow: 0 0 0 1px var(--error);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### form-label

```css
.psc-form-label {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Boars Head/Operations/\_Admin/UMAdjustRow](./views/00-pages/boars-head/operations/admin/umadjustrow.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-note

```css
.psc-form-note {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  background-color: var(--surface-page);
  border-radius: 4px;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 12px;
  padding-right: 12px;
  white-space: normal;
}
```

[00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-required-marker

```css
.psc-form-required-marker {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--error);
  margin-left: 3px;
  line-height: 1;
}
```

[00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md)

### form-row-label

```css
.psc-form-row-label {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
  white-space: nowrap;
}
```

[00\_Pages/Boars Head/Operations/OutOfService/\_Assets/TwoLineCell](./views/00-pages/boars-head/operations/outofservice/assets/twolinecell.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md)

### form-section-head

```css
.psc-form-section-head {
  padding-top: 12px;
  padding-bottom: 12px;
  padding-left: 20px;
  padding-right: 20px;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: var(--border);
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md)

### form-section-title

```css
.psc-form-section-title {
  font-family: sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-status

```css
.psc-form-status {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-status-error

```css
.psc-form-status-error {
  color: var(--error);
}
```

[00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [98\_Configuration/TicketRouting](./views/98-configuration/ticketrouting.md)

### form-subtitle

```css
.psc-form-subtitle {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 400;
  color: var(--text-muted);
}
```

[00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/PlcOverview](./views/00-pages/groveport/operations/plcoverview.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md)

### form-th

```css
.psc-form-th {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  white-space: normal;
  line-height: 1.2;
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [01\_Popups/Reports/\_Assets/CheckItem](./views/01-popups/reports/assets/checkitem.md), [01\_Popups/Reports/\_Assets/PreviewSection](./views/01-popups/reports/assets/previewsection.md), [01\_Popups/Reports/\_Assets/SummaryLine](./views/01-popups/reports/assets/summaryline.md)

### form-title

```css
.psc-form-title {
  font-family: sans-serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
}
```

[00\_Pages/Boars Head/Operations/AuditLog](./views/00-pages/boars-head/operations/auditlog.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](./views/00-pages/boars-head/operations/usermanagement/usermanagement.md), [00\_Pages/Boars Head/Operations/\_Admin/NewRole](./views/00-pages/boars-head/operations/admin/newrole.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/PlcOverview](./views/00-pages/groveport/operations/plcoverview.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md)

## fp

### fp-card

```css
.psc-fp-card {
  background-color: var(--surface-card);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
  padding-top: 10px;
  padding-bottom: 12px;
  padding-left: 16px;
  padding-right: 16px;
  box-sizing: border-box;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-card-title

```css
.psc-fp-card-title {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  white-space: nowrap;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Interlocks](./views/01-popups/00-faceplates/assets/tankoverview/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-gauge-alarm

```css
.psc-fp-gauge-alarm {
  background-color: var(--status-level-critical);
  border-radius: 3px;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-gauge-off

```css
.psc-fp-gauge-off {
  background-color: var(--status-off);
  border-radius: 3px;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-gauge-ok

```css
.psc-fp-gauge-ok {
  background-color: var(--status-cooling);
  border-radius: 3px;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-gauge-track

```css
.psc-fp-gauge-track {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border-strong);
  border-radius: 4px;
  box-sizing: border-box;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-gauge-warn

```css
.psc-fp-gauge-warn {
  background-color: var(--status-level-warning);
  border-radius: 3px;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-hero

```css
.psc-fp-hero {
  font-family: sans-serif;
  font-size: 30px;
  font-weight: 700;
  line-height: 36px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-kpi

```css
.psc-fp-kpi {
  font-family: sans-serif;
  font-size: 22px;
  font-weight: 700;
  line-height: 28px;
  color: var(--callToAction);
  white-space: nowrap;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-mark

```css
.psc-fp-mark {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-name

```css
.psc-fp-name {
  font-family: sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-pill

```css
.psc-fp-pill {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 700;
  border-radius: 12px;
  padding-top: 3px;
  padding-bottom: 3px;
  padding-left: 10px;
  padding-right: 10px;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 18px;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/TankOverview](./views/01-popups/00-faceplates/tankoverview.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-pill-btn

```css
.psc-fp-pill-btn {
  border-width: 0px;
  font-weight: 700;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-row-label

```css
.psc-fp-row-label {
  font-family: sans-serif;
  font-size: 13px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-row-value

```css
.psc-fp-row-value {
  font-family: sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-scale

```css
.psc-fp-scale {
  font-family: sans-serif;
  font-size: 12px;
  color: var(--text-muted);
  white-space: nowrap;
  text-align: right;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-sub

```css
.psc-fp-sub {
  font-family: sans-serif;
  font-size: 12px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-text-alarm

```css
.psc-fp-text-alarm {
  color: var(--status-level-critical);
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-text-normal

```css
.psc-fp-text-normal {
  color: var(--status-cooling);
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-text-ok

```css
.psc-fp-text-ok {
  color: var(--sts-run, #228B22);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-text-warn

```css
.psc-fp-text-warn {
  color: var(--warning);
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-tick-alarm

```css
.psc-fp-tick-alarm {
  background-color: var(--status-level-critical);
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-tick-warn

```css
.psc-fp-tick-warn {
  background-color: var(--status-level-warning);
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-tile

```css
.psc-fp-tile {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 14px;
  padding-right: 14px;
  box-sizing: border-box;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

### fp-title-sub

```css
.psc-fp-title-sub {
  font-family: sans-serif;
  font-size: 13px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

[01\_Popups/00\_Faceplates/DiscreteInput](./views/01-popups/00-faceplates/discreteinput.md), [01\_Popups/00\_Faceplates/TankOverview](./views/01-popups/00-faceplates/tankoverview.md)

### fp-tone-accent

```css
.psc-fp-tone-accent {
  background-color: var(--callToAction);
  color: var(--neutral-10);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-tone-alarm

```css
.psc-fp-tone-alarm {
  background-color: var(--status-level-critical);
  color: #FFFFFF;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-tone-muted

```css
.psc-fp-tone-muted {
  background-color: var(--surface-sunken);
  color: var(--text-muted);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-tone-off

```css
.psc-fp-tone-off {
  background-color: var(--status-off);
  color: #FFFFFF;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-tone-ok

```css
.psc-fp-tone-ok {
  background-color: var(--sts-run, #228B22);
  color: #FFFFFF;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-tone-warn

```css
.psc-fp-tone-warn {
  background-color: var(--status-level-warning);
  color: #161616;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### fp-unit

```css
.psc-fp-unit {
  font-family: sans-serif;
  font-size: 13px;
  color: var(--text-muted);
  white-space: nowrap;
}
```

[01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md)

## fs

### fs-10

```css
.psc-fs-10 {
  font-size: 10px;
}
```

[00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Utility/OverviewStatusTile](./views/00-pages/groveport/utility/overviewstatustile.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md)

### fs-11

```css
.psc-fs-11 {
  font-size: 11px;
}
```

<details>
<summary>Used in 42 views</summary>

[00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/CommentEntry](./views/00-pages/boars-head/operations/outofservice/assets/commententry.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapStatusBar](./views/00-pages/groveport/shared/cg/ahuevapstatusbar.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](./views/02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](./views/02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/ExhaustFan](./views/02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Pump](./views/02-components/01-devices/pump.md), [02\_Components/01\_Devices/SafetyRelay](./views/02-components/01-devices/safetyrelay.md), [02\_Components/01\_Devices/Sensor](./views/02-components/01-devices/sensor.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md), [02\_Components/03\_PLC/PointRow](./views/02-components/03-plc/pointrow.md), [03\_Elements/01\_Status/StatusDot](./views/03-elements/01-status/statusdot.md), [03\_Elements/03\_Table/DisplayTrend](./views/03-elements/03-table/displaytrend.md), [03\_Elements/03\_Table/Numeric](./views/03-elements/03-table/numeric.md), [98\_Configuration/ComponentPreview/VesselGeneric](./views/98-configuration/componentpreview/vesselgeneric.md), [98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

</details>

### fs-12

```css
.psc-fs-12 {
  font-size: 12px;
}
```

<details>
<summary>Used in 35 views</summary>

[00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewStatusTile](./views/00-pages/groveport/utility/overviewstatustile.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapStatusBar](./views/00-pages/groveport/shared/cg/ahuevapstatusbar.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/\_Assets/SavedListRow](./views/01-popups/reports/assets/savedlistrow.md), [02\_Components/01\_Devices/SafetyRelay](./views/02-components/01-devices/safetyrelay.md), [02\_Components/02\_Widgets/Safetys](./views/02-components/02-widgets/safetys.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [02\_Components/03\_PLC/PointRow](./views/02-components/03-plc/pointrow.md), [03\_Elements/03\_Table/CgHit](./views/03-elements/03-table/cghit.md)

</details>

### fs-13

```css
.psc-fs-13 {
  font-size: 13px;
}
```

<details>
<summary>Used in 17 views</summary>

[00\_Pages/00\_Docked/\_Assets/User](./views/00-pages/00-docked/assets/user.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./views/00-pages/groveport/shared/cg/ahuevapdisplay.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md)

</details>

### fs-14

```css
.psc-fs-14 {
  font-size: 14px;
}
```

<details>
<summary>Used in 23 views</summary>

[00\_Pages/Boars Head/LandingPage/PlantPlaceholder](./views/00-pages/boars-head/landingpage/plantplaceholder.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapHistory](./views/00-pages/groveport/shared/cg/ahuevaphistory.md), [02\_Components/01\_Devices/Evaporator](./views/02-components/01-devices/evaporator.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [02\_Components/03\_PLC/ModuleHover](./views/02-components/03-plc/modulehover.md)

</details>

### fs-15

```css
.psc-fs-15 {
  font-size: 15px;
}
```

[00\_Pages/Boars Head/Devices/DetailsOverview](./views/00-pages/boars-head/devices/detailsoverview.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewKpis](./views/00-pages/groveport/utility/overviewkpis.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md)

### fs-16

```css
.psc-fs-16 {
  font-size: 16px;
}
```

<details>
<summary>Used in 13 views</summary>

[00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/Utility/OverviewKpis](./views/00-pages/groveport/utility/overviewkpis.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/03\_PLC/ModuleHover](./views/02-components/03-plc/modulehover.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md), [98\_Configuration/ComponentPreview/Condenser-SafetyRelay](./views/98-configuration/componentpreview/condenser-safetyrelay.md), [98\_Configuration/ComponentPreview/VesselGeneric](./views/98-configuration/componentpreview/vesselgeneric.md)

</details>

### fs-18

```css
.psc-fs-18 {
  font-size: 18px;
}
```

[00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./views/00-pages/groveport/shared/cg/ahuevapdisplay.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md)

### fs-20

```css
.psc-fs-20 {
  font-size: 20px;
}
```

<details>
<summary>Used in 31 views</summary>

[00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](./views/00-pages/groveport/machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](./views/00-pages/groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md)

</details>

### fs-22

```css
.psc-fs-22 {
  font-size: 22px;
}
```

<details>
<summary>Used in 14 views</summary>

[00\_Pages/Boars Head/LandingPage/PlantPlaceholder](./views/00-pages/boars-head/landingpage/plantplaceholder.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md)

</details>

### fs-9

```css
.psc-fs-9 {
  font-size: 9px;
}
```

<details>
<summary>Used in 13 views</summary>

[00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md)

</details>

## fw

### fw-400

```css
.psc-fw-400 {
  font-weight: 400;
}
```

[00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [02\_Components/01\_Devices/SafetyRelay](./views/02-components/01-devices/safetyrelay.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md), [02\_Components/03\_PLC/PointRow](./views/02-components/03-plc/pointrow.md), [98\_Configuration/ComponentPreview/VesselGeneric](./views/98-configuration/componentpreview/vesselgeneric.md)

### fw-600

```css
.psc-fw-600 {
  font-weight: 600;
}
```

<details>
<summary>Used in 41 views</summary>

[00\_Pages/00\_Docked/\_Assets/IntegratorContact](./views/00-pages/00-docked/assets/integratorcontact.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Operations/Forms/DailyRounds](./views/00-pages/groveport/operations/forms/dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./views/00-pages/groveport/operations/forms/shiftlog.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewKpis](./views/00-pages/groveport/utility/overviewkpis.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapHistory](./views/00-pages/groveport/shared/cg/ahuevaphistory.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [02\_Components/01\_Devices/Condenser](./views/02-components/01-devices/condenser.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md), [02\_Components/03\_PLC/ModuleHover](./views/02-components/03-plc/modulehover.md), [02\_Components/03\_PLC/PointRow](./views/02-components/03-plc/pointrow.md), [98\_Configuration/TicketLogger](./views/98-configuration/ticketlogger.md)

</details>

### fw-700

```css
.psc-fw-700 {
  font-weight: 700;
}
```

<details>
<summary>Used in 89 views</summary>

[00\_Pages/00\_Docked/\_Assets/PlcWriteLock](./views/00-pages/00-docked/assets/plcwritelock.md), [00\_Pages/Boars Head/Alarms/Journal](./views/00-pages/boars-head/alarms/journal.md), [00\_Pages/Boars Head/Alarms/Summary](./views/00-pages/boars-head/alarms/summary.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/DetailsOverview](./views/00-pages/boars-head/devices/detailsoverview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/LandingPage/PlantPlaceholder](./views/00-pages/boars-head/landingpage/plantplaceholder.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/CommentEntry](./views/00-pages/boars-head/operations/outofservice/assets/commententry.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Overview](./views/00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](./views/00-pages/groveport/machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](./views/00-pages/groveport/machine-room/utility/safetyrelay/overview.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md), [00\_Pages/Groveport/Operations/Forms/History](./views/00-pages/groveport/operations/forms/history.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/Site/Overview](./views/00-pages/groveport/site/overview.md), [00\_Pages/Groveport/Site/OverviewClassic](./views/00-pages/groveport/site/overviewclassic.md), [00\_Pages/Groveport/Site/OverviewExecutive](./views/00-pages/groveport/site/overviewexecutive.md), [00\_Pages/Groveport/Utility/Overview](./views/00-pages/groveport/utility/overview.md), [00\_Pages/Groveport/Utility/OverviewKpis](./views/00-pages/groveport/utility/overviewkpis.md), [00\_Pages/Groveport/Utility/OverviewStatusTile](./views/00-pages/groveport/utility/overviewstatustile.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./views/00-pages/groveport/shared/cg/ahuevapdisplay.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./views/00-pages/groveport/shared/cg/ahuevappanel.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapStatusBar](./views/00-pages/groveport/shared/cg/ahuevapstatusbar.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./views/01-popups/00-faceplates/assets/tank/controls.md), [02\_Components/00\_Controls/InterlockButton](./views/02-components/00-controls/interlockbutton.md), [02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](./views/02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](./views/02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](./views/02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](./views/02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/LTU](./views/02-components/01-devices/ltu.md), [02\_Components/01\_Devices/Pump](./views/02-components/01-devices/pump.md), [02\_Components/01\_Devices/SafetyRelay](./views/02-components/01-devices/safetyrelay.md), [02\_Components/01\_Devices/Sensor](./views/02-components/01-devices/sensor.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [02\_Components/02\_Widgets/Safetys](./views/02-components/02-widgets/safetys.md), [02\_Components/02\_Widgets/SiteCard](./views/02-components/02-widgets/sitecard.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [02\_Components/03\_PLC/ModuleHover](./views/02-components/03-plc/modulehover.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md), [02\_Components/03\_PLC/PointRow](./views/02-components/03-plc/pointrow.md), [03\_Elements/01\_Status/StatusDot](./views/03-elements/01-status/statusdot.md), [03\_Elements/03\_Table/StateText](./views/03-elements/03-table/statetext.md), [98\_Configuration/ComponentPreview/Condenser-SafetyRelay](./views/98-configuration/componentpreview/condenser-safetyrelay.md), [98\_Configuration/ComponentPreview/VesselGeneric](./views/98-configuration/componentpreview/vesselgeneric.md), [98\_Configuration/IntegrationSection](./views/98-configuration/integrationsection.md), [98\_Configuration/TicketLoggerSettings](./views/98-configuration/ticketloggersettings.md)

</details>

## icon

### icon-header

```css
.psc-icon-header {
  overflow: visible;
}
```

[02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](./views/02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](./views/02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](./views/02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](./views/02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Pump](./views/02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](./views/02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](./views/02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [03\_Elements/01\_Status/IconHeader](./views/03-elements/01-status/iconheader.md)

## kpi

### kpi-value

```css
.psc-kpi-value {
  color: var(--callToAction);
  font-family: Bahnschrift, 'Segoe UI', sans-serif;
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.15;
}
```

[00\_Pages/Groveport/Domains/EPMS](./views/00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](./views/00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](./views/00-pages/groveport/domains/utility.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md)

## nav

### nav-clock

```css
.psc-nav-clock {
  color: var(--text-nav-muted);
  font-family: Bahnschrift, 'Segoe UI', sans-serif;
  font-size: 14px;
  padding: 6px 8px 8px;
  text-align: center;
  white-space: nowrap;
}
```

[00\_Pages/00\_Docked/Navigation](./views/00-pages/00-docked/navigation.md)

## plant

### plant-feature-title

```css
.psc-plant-feature-title {
  color: var(--text);
  font-family: Bahnschrift, 'Segoe UI', sans-serif;
}
```

<details>
<summary>Used in 14 views</summary>

[00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapHistory](./views/00-pages/groveport/shared/cg/ahuevaphistory.md), [02\_Components/02\_Widgets/KPI](./views/02-components/02-widgets/kpi.md), [02\_Components/02\_Widgets/MetricCard](./views/02-components/02-widgets/metriccard.md)

</details>

## prod

### prod-device-tile

```css
.psc-prod-device-tile {
  cursor: pointer;
}
```

[00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md)

## rcp1

### rcp1-sim-label

```css
.psc-rcp1-sim-label {
  color: inherit;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### rcp1-sim-label-on

```css
.psc-rcp1-sim-label-on {
  color: var(--text);
}
```

Not used in any view's static classes (may be set by a binding or a script).

## report

### report-advanced

```css
.psc-report-advanced {
  background-color: var(--surface-card);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
  box-sizing: border-box;
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-advanced-open

```css
.psc-report-advanced-open {
  background-color: var(--callToActionHighlight);
  border-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### report-bar-bottom

```css
.psc-report-bar-bottom {
  background-color: var(--surface-card);
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: var(--border);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-bar-mid

```css
.psc-report-bar-mid {
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: var(--border);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-bar-top

```css
.psc-report-bar-top {
  background-color: var(--surface-card);
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: var(--border);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-choice

```css
.psc-report-choice {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
  box-sizing: border-box;
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [01\_Popups/Reports/\_Assets/ChoiceTile](./views/01-popups/reports/assets/choicetile.md), [01\_Popups/Reports/\_Assets/StartTile](./views/01-popups/reports/assets/starttile.md)

### report-choice-btn

```css
.psc-report-choice-btn {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-choice-detail

```css
.psc-report-choice-detail {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 400;
  color: var(--text-muted);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [01\_Popups/Reports/\_Assets/ChoiceTile](./views/01-popups/reports/assets/choicetile.md), [01\_Popups/Reports/\_Assets/PreviewSection](./views/01-popups/reports/assets/previewsection.md), [01\_Popups/Reports/\_Assets/SavedRow](./views/01-popups/reports/assets/savedrow.md), [01\_Popups/Reports/\_Assets/SectionItem](./views/01-popups/reports/assets/sectionitem.md), [01\_Popups/Reports/\_Assets/StartTile](./views/01-popups/reports/assets/starttile.md)

### report-choice-label

```css
.psc-report-choice-label {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md), [01\_Popups/Reports/\_Assets/ChoiceTile](./views/01-popups/reports/assets/choicetile.md), [01\_Popups/Reports/\_Assets/StartTile](./views/01-popups/reports/assets/starttile.md)

### report-choice-selected

```css
.psc-report-choice-selected {
  background-color: var(--callToActionHighlight);
  border-color: var(--callToAction);
  box-shadow: inset 0 0 0 1px var(--callToAction);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-heading

```css
.psc-report-heading {
  font-family: sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
}
```

[00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-hint

```css
.psc-report-hint {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 400;
  color: var(--text-muted);
  line-height: 1.4;
}
```

[00\_Pages/Groveport/Operations/ReportsBuilder](./views/00-pages/groveport/operations/reportsbuilder.md), [00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-icon-box

```css
.psc-report-icon-box {
  background-color: var(--surface-page);
  border-radius: 6px;
}
```

[01\_Popups/Reports/\_Assets/SourceCard](./views/01-popups/reports/assets/sourcecard.md), [01\_Popups/Reports/\_Assets/StartCard](./views/01-popups/reports/assets/startcard.md)

### report-icon-box-selected

```css
.psc-report-icon-box-selected {
  background-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### report-kpi

```css
.psc-report-kpi {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
  box-sizing: border-box;
}
```

[01\_Popups/Reports/\_Assets/PreviewCard](./views/01-popups/reports/assets/previewcard.md)

### report-kpi-detail

```css
.psc-report-kpi-detail {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 400;
  color: var(--text-muted);
}
```

[01\_Popups/Reports/\_Assets/PreviewCard](./views/01-popups/reports/assets/previewcard.md)

### report-kpi-label

```css
.psc-report-kpi-label {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
```

[01\_Popups/Reports/\_Assets/PreviewCard](./views/01-popups/reports/assets/previewcard.md)

### report-kpi-value

```css
.psc-report-kpi-value {
  font-family: sans-serif;
  font-size: 24px;
  font-weight: 700;
  color: var(--text);
}
```

[01\_Popups/Reports/\_Assets/PreviewCard](./views/01-popups/reports/assets/previewcard.md)

### report-row

```css
.psc-report-row {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 4px;
  box-sizing: border-box;
}
```

[01\_Popups/Reports/\_Assets/SavedListRow](./views/01-popups/reports/assets/savedlistrow.md), [01\_Popups/Reports/\_Assets/SavedRow](./views/01-popups/reports/assets/savedrow.md)

### report-row-name

```css
.psc-report-row-name {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}
```

[01\_Popups/Reports/\_Assets/PreviewChart](./views/01-popups/reports/assets/previewchart.md), [01\_Popups/Reports/\_Assets/SavedListRow](./views/01-popups/reports/assets/savedlistrow.md), [01\_Popups/Reports/\_Assets/SavedRow](./views/01-popups/reports/assets/savedrow.md)

### report-step-dot

```css
.psc-report-step-dot {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border-strong);
  border-radius: 14px;
  box-sizing: border-box;
  cursor: pointer;
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-step-dot-on

```css
.psc-report-step-dot-on {
  background-color: var(--callToAction);
  border-color: var(--callToAction);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-step-label

```css
.psc-report-step-label {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-muted);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-step-label-current

```css
.psc-report-step-label-current {
  font-weight: 700;
  color: var(--text);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-step-label-done

```css
.psc-report-step-label-done {
  color: var(--text);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-step-line

```css
.psc-report-step-line {
  background-color: var(--border);
  border-radius: 1px;
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-step-line-done

```css
.psc-report-step-line-done {
  background-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### report-step-num

```css
.psc-report-step-num {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: var(--text-muted);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-subtitle

```css
.psc-report-subtitle {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 400;
  color: var(--text-muted);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-sum-value

```css
.psc-report-sum-value {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
}
```

[01\_Popups/Reports/\_Assets/SummaryLine](./views/01-popups/reports/assets/summaryline.md)

### report-surface

```css
.psc-report-surface {
  background-color: var(--surface-page);
  font-family: sans-serif;
}
```

[01\_Popups/Reports/RenameReport](./views/01-popups/reports/renamereport.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-tab

```css
.psc-report-tab {
  font-family: sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-muted);
  padding-bottom: 6px;
  border-bottom-width: 2px;
  border-bottom-style: solid;
  border-bottom-color: transparent;
}
```

[00\_Pages/Groveport/Operations/ReportsSaved](./views/00-pages/groveport/operations/reportssaved.md), [01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

### report-tab-active

```css
.psc-report-tab-active {
  font-weight: 700;
  color: var(--callToAction);
  border-bottom-color: var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### report-tile

```css
.psc-report-tile {
  background-color: var(--input);
  border-width: 1px;
  border-style: solid;
  border-color: var(--border);
  border-radius: 6px;
  box-sizing: border-box;
}
```

[01\_Popups/Reports/\_Assets/SourceCard](./views/01-popups/reports/assets/sourcecard.md), [01\_Popups/Reports/\_Assets/StartCard](./views/01-popups/reports/assets/startcard.md)

### report-tile-desc

```css
.psc-report-tile-desc {
  font-family: sans-serif;
  font-size: 12px;
  font-weight: 400;
  color: var(--text-muted);
}
```

[01\_Popups/Reports/\_Assets/SourceCard](./views/01-popups/reports/assets/sourcecard.md), [01\_Popups/Reports/\_Assets/StartCard](./views/01-popups/reports/assets/startcard.md)

### report-tile-meta

```css
.psc-report-tile-meta {
  font-family: sans-serif;
  font-size: 11px;
  font-weight: 500;
  color: var(--text-muted);
}
```

[01\_Popups/Reports/\_Assets/SourceCard](./views/01-popups/reports/assets/sourcecard.md), [01\_Popups/Reports/\_Assets/StartCard](./views/01-popups/reports/assets/startcard.md)

### report-tile-selected

```css
.psc-report-tile-selected {
  background-color: var(--callToActionHighlight);
  border-color: var(--callToAction);
  box-shadow: inset 0 0 0 1px var(--callToAction);
}
```

Not used in any view's static classes (may be set by a binding or a script).

### report-tile-title

```css
.psc-report-tile-title {
  font-family: sans-serif;
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}
```

[01\_Popups/Reports/\_Assets/SourceCard](./views/01-popups/reports/assets/sourcecard.md), [01\_Popups/Reports/\_Assets/StartCard](./views/01-popups/reports/assets/startcard.md)

### report-title

```css
.psc-report-title {
  font-family: sans-serif;
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
}
```

[01\_Popups/Reports/ReportBuilder](./views/01-popups/reports/reportbuilder.md)

## status

### status-dot-blink

```css
.psc-status-dot-blink {

}
/* {"animation": {"direction": "normal", "duration": "1s", "iterationCount": "infinite", "keyframes": {"0%": {"backgroundColor": "var(--status-level-critical)"}, "100%": {"backgroundColor": "var(--sta... */
```

[03\_Elements/01\_Status/StatusDot](./views/03-elements/01-status/statusdot.md)

## tank

### tank-level-text-critical

```css
.psc-tank-level-text-critical {
  background-color: transparent;
  color: var(--status-level-critical);
}
```

[02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md), [03\_Elements/03\_Table/StateText](./views/03-elements/03-table/statetext.md)

### tank-level-text-warning

```css
.psc-tank-level-text-warning {
  background-color: transparent;
  color: var(--status-level-warning);
}
```

[02\_Components/01\_Devices/Tank](./views/02-components/01-devices/tank.md)

### tank-sw-label

```css
.psc-tank-sw-label {
  color: var(--neutral-60);
}
```

Not used in any view's static classes (may be set by a binding or a script).

## text

### text-cta

```css
.psc-text-cta {
  color: var(--cta);
}
```

[00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md)

### text-muted

```css
.psc-text-muted {
  color: var(--text-muted);
}
```

<details>
<summary>Used in 30 views</summary>

[00\_Pages/00\_Docked/\_Assets/IntegratorContact](./views/00-pages/00-docked/assets/integratorcontact.md), [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](./views/00-pages/boars-head/operations/outofservice/outofservicelog.md), [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/CommentEntry](./views/00-pages/boars-head/operations/outofservice/assets/commententry.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d](./views/00-pages/groveport/machine-room/utility/plcrack/rack3d.md), [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Relay3d](./views/00-pages/groveport/machine-room/utility/safetyrelay/relay3d.md), [00\_Pages/Groveport/Operations/Forms/PidVerification](./views/00-pages/groveport/operations/forms/pidverification.md), [00\_Pages/Groveport/Production/Level1/Overview](./views/00-pages/groveport/production/level1/overview.md), [00\_Pages/Groveport/Production/Level2/Forming](./views/00-pages/groveport/production/level2/forming.md), [00\_Pages/Groveport/Production/Level2/Kpis](./views/00-pages/groveport/production/level2/kpis.md), [00\_Pages/Groveport/Production/Level2/Packaging](./views/00-pages/groveport/production/level2/packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./views/00-pages/groveport/production/level2/prep.md), [00\_Pages/Groveport/Production/Level3/Handtman](./views/00-pages/groveport/production/level3/handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./views/00-pages/groveport/production/level3/hopper.md), [00\_Pages/Groveport/Production/Level3/Kpis](./views/00-pages/groveport/production/level3/kpis.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./views/00-pages/groveport/production/level3/lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./views/00-pages/groveport/production/level3/loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./views/00-pages/groveport/production/level3/rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./views/00-pages/groveport/production/level3/shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./views/00-pages/groveport/production/level3/vatdumper.md), [01\_Popups/00\_Faceplates/Alerts/OutOfService](./views/01-popups/00-faceplates/alerts/outofservice.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/Configuration](./views/01-popups/00-faceplates/assets/configuration/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./views/01-popups/00-faceplates/assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./views/01-popups/00-faceplates/assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./views/01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./views/01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./views/01-popups/00-faceplates/assets/tank/configuration.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [02\_Components/03\_PLC/PlcCard](./views/02-components/03-plc/plccard.md), [02\_Components/03\_PLC/PointRow](./views/02-components/03-plc/pointrow.md)

</details>

### text-ok

```css
.psc-text-ok {
  color: #2E7D32;
}
```

[00\_Pages/Boars Head/Operations/RolesPermissions](./views/00-pages/boars-head/operations/rolespermissions.md)

## theme

### theme-toggle

```css
.psc-theme-toggle {
  border-width: 1px;
  border-style: solid;
  border-color: var(--border-strong);
  border-radius: 10px;
  overflow: hidden;
}
```

<details>
<summary>Used in 19 views</summary>

[00\_Pages/00\_Docked/\_Assets/ChangeTheme](./views/00-pages/00-docked/assets/changetheme.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md)

</details>

### theme-toggle-option

```css
.psc-theme-toggle-option {
  color: var(--text);
  font-family: Bahnschrift, 'Segoe UI', sans-serif;
  font-size: 12px;
  padding: 4px 6px;
}
```

<details>
<summary>Used in 19 views</summary>

[00\_Pages/00\_Docked/\_Assets/ChangeTheme](./views/00-pages/00-docked/assets/changetheme.md), [00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md)

</details>

### theme-toggle-option-selected

```css
.psc-theme-toggle-option-selected {
  background-color: var(--neutral-100);
  color: var(--text-inverse);
}
```

<details>
<summary>Used in 18 views</summary>

[00\_Pages/Boars Head/Compressors/Overview](./views/00-pages/boars-head/compressors/overview.md), [00\_Pages/Boars Head/Devices/Overview](./views/00-pages/boars-head/devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./views/00-pages/boars-head/exhaustfans/overview.md), [00\_Pages/Boars Head/Pumps/Overview](./views/00-pages/boars-head/pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./views/00-pages/boars-head/sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./views/00-pages/boars-head/tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./views/00-pages/boars-head/valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./views/00-pages/groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./views/00-pages/groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](./views/00-pages/groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](./views/00-pages/groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](./views/00-pages/groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./views/00-pages/groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](./views/00-pages/groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](./views/00-pages/groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](./views/00-pages/groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](./views/00-pages/groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](./views/00-pages/groveport/machine-room/utility/valves/overview.md)

</details>

## value

### value-alarm

```css
.psc-value-alarm {
  color: var(--error);
  font-weight: 700;
}
```

Not used in any view's static classes (may be set by a binding or a script).

### value-bad

```css
.psc-value-bad {
  color: var(--neutral-60);
  font-style: italic;
}
```

<details>
<summary>Used in 13 views</summary>

[00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](./views/00-pages/groveport/machine-room/utility/plcrack/overview.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./views/01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./views/01-popups/00-faceplates/assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./views/01-popups/00-faceplates/assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./views/01-popups/00-faceplates/assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./views/01-popups/00-faceplates/assets/tankoverview/overview.md), [02\_Components/01\_Devices/Compressor](./views/02-components/01-devices/compressor.md), [02\_Components/03\_PLC/ModuleDetail](./views/02-components/03-plc/moduledetail.md), [03\_Elements/00\_Control/AnalogInput](./views/03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/MultiStateInput](./views/03-elements/00-control/multistateinput.md), [03\_Elements/00\_Control/StringInput](./views/03-elements/00-control/stringinput.md), [03\_Elements/00\_Control/TimeInput](./views/03-elements/00-control/timeinput.md), [03\_Elements/03\_Table/Boolean](./views/03-elements/03-table/boolean.md)

</details>
