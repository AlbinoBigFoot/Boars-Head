---
title: Perspective Scripting
sidebar_position: 6
description: Session props and their bindings, view / component events, message handlers and the message patterns of the BH HMI (page-scoped menus with a sender filter, Alert popup actions).
sources:
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/Alert/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/ContextMenu/view.json
last_verified: 2026-10-24
---

# Perspective Scripting

This page covers the **scripting side** of Perspective: where scripts hang on views, the session props that
every script relies on, and the message patterns. Views, bindings and styling themselves are documented in
[Perspective](../perspective/index.md).

## Binding first, script last

The project rule is to prefer, in order: **Expression** > **Structured expression
(`expr-struct`)** > **Expression transform** > script transform / event script only when nothing else works. A
count over the 300 views (2026-10-23): about 4,000 expression bindings, 390 expr-struct bindings, 56 tag bindings,
a handful of query bindings and about 1,000 script blocks (events, message handlers, custom methods, script
transforms). Scripts are for **one-shot commands** (writes, navigation, popups, downloads), confirmations, and
calls into `shared.*` that need the gateway (SQL, permissions).

Null safety in expressions: `coalesce({view.custom.x}, '') = 'literal'` instead of `{view.custom.x} = 'literal'`
(a null makes the whole binding an error, with a red overlay). Use the Integration Toolkit functions `try()`,
`isGood()`, `coalesce()`, `tag()` for quality-safe reads.

## Where scripts hang on a view

| Hook | Designer | Typical BH use |
|---|---|---|
| Component event (`events.dom.onClick`, `events.component.onActionPerformed` ...) | select component > **Configure Events** | button commands, opening faceplates, navigation |
| Script transform on a binding | binding editor > **Add Transform > Script** | turning a query / struct into the shape a table needs (`shared.Reports.builderModel`) |
| Property change script | right-click a property > **Edit Change Script** | the Header's `custom.localRouteGuard` (navigates in local mode), MultiStateInput's snap-back-and-confirm |
| Message handler | component or view > **Configure Scripts > Message Handlers** | receiving `writeValue`, `oosToggle`, `rptEdit` ... (below) |
| Custom method | **Configure Scripts > Custom Methods** | helpers local to one view (255 views have some) |
| View `onStartup` | root > **Configure Events > lifecycle** | 10 views: Header, Roles & Permissions, the four Operations Forms pages, Faceplate shell, Report Builder, Numeric input, Adhoc Trend |

There are **no session event scripts** (Session Events: startup / shutdown / page startup) in the project. Per-user
state is computed by **session props bindings** instead.

## Session props (`session.custom.*`)

Defined in **Project Browser > Perspective > Session Props**
(`com.inductiveautomation.perspective/session-props/props.json`). Every security prop is **PROTECTED**: the browser
can read it but cannot change it, so a script can trust it.

| Prop | Binding | Used for |
|---|---|---|
| `custom.Permissions` | expr-struct `{matrix: tag('[default]_Config/RolesPermissions'), roles: session.props.auth.user.roles, full: tag(.../FullPermissionRoles), inherits: tag(.../RoleInherits)}` + script transform `shared.Security.permissions(...)` | `{Device: {Action: bool}}` for this user; re-evaluates on login and when the matrix changes |
| `custom.ReadOnly` | `!coalesce({session.custom.Permissions.Faceplates.Operate}, false)` | disables every write control |
| `custom.CanOpenFaceplates` | `Permissions.Faceplates.Open` | hover outline + faceplate opening |
| `custom.EngineeringView` / `custom.EngineeringReadOnly` | `Permissions.Engineering.View` / `ReadOnly or !Engineering.Edit` | Engineering tabs and cards |
| `custom.AlarmConfigReadOnly` | `ReadOnly or !AlarmConfiguration.Edit` | faceplate Alarm Configuration rows |
| `custom.Administrator` | user holds a role in `_Config/Security/AdminRoles` | admin pages, legacy `adminOnly` nav items |
| `custom.TicketLogAccess` | matrix row `TicketLogger/Use` (every role) AND (Monday `Connected` OR the `DryRun` tag) | Ticket Logger menu and Send |
| `custom.TicketLogSettings` / `custom.IntegrationAccess` | matrix row `TicketLogger/Settings` (OneShot only, a restricted row) | Ticket Logger settings gear, Integrations settings |
| `custom.AdhocTrend` | (not bound; written by scripts) | the trend basket: `tags`, `plots`, `penPlots` (see [Trending](../features/trending.md)) |
| `custom.trend`, `custom.trendTools` | basket summary; trend tool state (drag mode, Auto-Scale Y, zoom window) | header badge; the synced trend tool row |

In view expressions read them as `{session.custom.ReadOnly}`; in scripts as `self.session.custom.ReadOnly`.
Server-side checks should still call `shared.Security.require(...)`: the session props drive the UI, the library
call is the enforcement.

## Messages

A **message** is a named event with a payload: `system.perspective.sendMessage(type, payload, scope)`; any view or
component with a handler for that type, listening on that scope (`view`, `page` or `session`), runs its script.
The generated [Perspective Messages reference](./reference/messages.md) lists every type with its senders and
handlers.

### Pattern 1: one right-click menu, many components (sender filter)

Every BH view has a right-click menu (`meta.contextMenu`, shared by the Ticket Logger and the Out Of Service items). A context-menu item can only send a message, and the message goes to the whole
**page**, so every component on the page hears it. The payload therefore carries `sender: self.view.id`, and each
handler starts with:

```python
sender = payload.get('sender')
if sender and sender != self.view.id:
    return        # not the component that was right-clicked
```

Messages using this pattern: `ticketLog` (about 250 views), `oosToggle`, `oosHistory`.

### Pattern 2: Alert popup buttons are messages

`shared.Alerts.showAlert(..., btnActionPrimary="writeValue", btnActionSecondary="cancel", payload={...})` opens the
standard Alert popup. Its buttons send the named message to the page with the payload. `writeValue` is special:
the popup performs the audited write itself and adds `alreadyWritten = true` (see
[Write Paths](./write-path.md)). Other actions are plain confirmations handled by the page that opened the popup:
`opsFormsSubmitDailyRounds`, `opsFormsSubmitShiftLog`, `opsFormsPidComplete`, `removeUser`, `removeRole`,
`rptDeleteTemplate`, `TrendDeleteConfirm` and so on.

### Pattern 3: page-local event bus

Some complex views talk to their own children with page messages: the Report Builder (`rptEdit`: every tile,
checkbox and field sends an edit that `shared.Reports.applyEdit` merges into `view.custom.def`), the PLC rack
(`plcRackHover`, `plcRackSelect`), the Utility Overview (`UtilityOverviewHighlight`), User Management
(`userManagementChangeViews`, `userManagementRefreshTables`, `UserManagement_*`).

### Pattern 4: gateway to session

`shared.OutOfService` sends `oosChanged` to the calling session after a take / return so the header badge and the
log page refresh at once (other sessions poll every 30 to 60 s). `shared.Globe.relay` turns a WebDev POST into a
page-scoped `globeHover` / `globeNavigate` for exactly one session and page.

## Popups

Open popups through the helpers so geometry, ids and permissions stay consistent:

| Helper | Opens |
|---|---|
| `shared.Alerts.showAlert(...)` | the standard Alert / confirm popup (`alertDialog`) |
| `shared.Alerts.showFaceplate(tagPath, deviceType, ...)` | the tabbed Faceplate shell (`Navigation.Faceplate.openFaceplate`, checks `Faceplates/Open`) |
| `Navigation.Faceplate.openDevice(tagPath)` | the right faceplate for any device instance |
| `shared.OutOfService.openDialog(...)` | the Out Of Service memo dialog |
| `shared.Reports.open(sourceId, context)` | the Report Builder, sized to the caller's viewport |
| `shared.PlcRack.openCard(...)` | one PLC rack card as a pop-out |
| `shared.Alerts.showAdhocTrend()` | the Adhoc Trend faceplate (bottom right) |
