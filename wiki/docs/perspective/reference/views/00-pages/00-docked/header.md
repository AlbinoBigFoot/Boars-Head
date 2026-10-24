---
title: "Header"
sidebar_label: "Header"
description: "Perspective view 00_Pages/00_Docked/Header (Docked view): 19 components, 14 bindings, 8 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/Header", "Header"]
---

:::note

:::


**Docked view**: `00_Pages/00_Docked/Header`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/Header` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/Header/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; Header |
| Docked | shared top dock app-header (visible) |
| Root | `ia.container.flex`, height 48, width 1200 |
| Size | 19 components, 14 bindings, 7 event handlers, 1 change scripts, 1 message handlers |
| Last saved | 2026-07-25T07:26:16Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `localRouteGuard` | `""` | bound (expr), change script |

## Component Tree

Component types: ia.container.flex x8, ia.display.view x7, ia.display.icon x3, ia.display.label x1.

<details>
<summary>Component tree (19 components)</summary>

```text
root  ia.container.flex  [3 bindings; 1 event]
  NavMenu  ia.container.flex  [1 event]
    Icon  ia.display.icon
  BrandLogo  ia.display.view  [1 event; view: 00_Pages/00_Docked/_Assets/BrandLogo]
  PlcWriteLock  ia.display.view  [1 binding; view: 00_Pages/00_Docked/_Assets/PlcWriteLock]
  Spacer  ia.container.flex
  IntegratorBadge  ia.container.flex
    Badge  ia.container.flex  [1 event]
      Logo  ia.display.view  [view: 00_Pages/00_Docked/_Assets/IntegratorLogo]
    Divider  ia.container.flex
  PermBadge  ia.container.flex  [4 bindings; 2 events]
    Icon  ia.display.icon  [1 binding]
  User  ia.display.view  [view: 00_Pages/00_Docked/_Assets/User]
  OosNotification  ia.display.view  [1 binding; view: 00_Pages/00_Docked/_Assets/OosNotification]
  AlarmNotification  ia.display.view  [view: 00_Pages/00_Docked/_Assets/AlarmNotification]
  TrendButton  ia.container.flex  [1 binding; 1 event]
    Icon  ia.display.icon
    Badge  ia.display.label  [2 bindings]
  UserSettings  ia.display.view  [view: 00_Pages/00_Docked/_Assets/UserSettings]
```

</details>

## Bindings

14 bindings: expr 7, property 5, expr-struct 2.

<details>
<summary>All 14 bindings, grouped by component</summary>

**`(view)`**

- `custom.localRouteGuard`: expression

```js
if(toBoolean(coalesce(try(tag('[default]_Config/DemoEnterpriseNav'), true), true)), '',
  if(indexOf('|/|/enterprise|/plants/groveport|/plants/groveport/classic|/plants/groveport/executive|/plants/new-castle|/plants/forrest-city|/plants/petersburg|/plants/holland|/plants/groveport/production-overview|/plants/groveport/production/level-2/prep|/plants/groveport/production/level-2/forming|/plants/groveport/production/level-2/packaging|/plants/groveport/production/vat-dumper|/plants/groveport/production/hopper|/plants/groveport/production/handtman|/plants/groveport/production/loaders|/plants/groveport/production/roll-stock|/plants/groveport/production/shrink-tunnel|/plants/groveport/production/lazy-susan|/plants/groveport/freezer/epms|/plants/groveport/freezer/production|/plants/groveport/superchill/epms|/plants/groveport/superchill/production|/plants/groveport/club/epms|/plants/groveport/club/production|/plants/groveport/palletizing/epms|/plants/groveport/palletizing/production|/plants/groveport/east-ph/epms|/plants/groveport/east-ph/production|/plants/groveport/west-ph/epms|/plants/groveport/west-ph/production|/plants/groveport/dock/epms|/plants/groveport/dock/production|/plants/groveport/machine-room/epms|/plants/groveport/machine-room/production|', '|' + coalesce({page.props.path}, '') + '|') >= 0, '/plants/groveport/utility-overview', ''))
```


**`root`**

- `props.style.classes`: expression

```js
if(coalesce({session.props.animations}, true), 'app-header', 'app-header animations-off')
```


- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/PlcWriteLock`**

- `position.display`: expression

```js
!coalesce(try(toBoolean(tag('[default]_Config/PlcWriteLock/Locked')), true), true)
```


**`root/PermBadge`**

- `meta.visible`: property `session.props.auth.authenticated`

- `meta.tooltip.enabled`: property `session.props.auth.authenticated`

- `meta.tooltip.text`: property `session.props.auth.user.roles`, then script transform

Transform 1, script:

```python
roles = []
if value is not None:
    try:
        roles = [str(r) for r in value]
    except:
        roles = [str(value)]
if not roles:
    return 'Roles: (none)'
return 'Roles: ' + ', '.join(roles)
```


- `props.style.classes`: property `session.custom.ReadOnly`, then expression transform

Transform 1, expression:

```js
if({value}, 'perm-badge perm-badge-read header-icon', 'perm-badge perm-badge-write header-icon')
```


**`root/PermBadge/Icon`**

- `props.path`: property `session.custom.ReadOnly`, then expression transform

Transform 1, expression:

```js
if({value}, 'material/lock', 'material/lock_open')
```


**`root/OosNotification`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.OutOfService.View}, false)
```


**`root/TrendButton`**

- `meta.tooltip.text`: expression

```js
if(coalesce(try(len({session.custom.AdhocTrend.tags}), 0), 0) > 0, 'Trending (' + toStr(len({session.custom.AdhocTrend.tags})) + ' Pens)', 'Trending')
```


**`root/TrendButton/Badge`**

- `props.text`: expression

```js
toStr(coalesce(try(len({session.custom.AdhocTrend.tags}), 0), 0))
```


- `meta.visible`: expression

```js
coalesce(try(len({session.custom.AdhocTrend.tags}), 0), 0) > 0
```

</details>

## Event Scripts And Handlers

- **`root`** `system.onStartup`, script action, scope `G`

```python
# Stock light/dark omit BH tokens; always land on *-cool / *-warm aliases.
try:
    t = str(self.session.props.theme or '').strip().lower()
    if t == 'light' or t == '':
        self.session.props.theme = 'light-cool'
    elif t == 'dark':
        self.session.props.theme = 'dark-cool'
except:
    pass
enabled = True
try:
    enabled = bool(self.session.props.animations)
except:
    enabled = True
try:
    js = ("document.documentElement.classList.remove('animations-off');" if enabled else "document.documentElement.classList.add('animations-off');")
    if hasattr(system.perspective, 'runJavaScriptAsync'):
        system.perspective.runJavaScriptAsync(js)
    elif hasattr(system.perspective, 'runJavaScript'):
        system.perspective.runJavaScript(js)
except:
    pass
```

- **`root/NavMenu`** `dom.onClick`, script action, scope `G`

```python
# Toggle shared left dock id plant-nav (00_Pages/00_Docked/Navigation).
# One-shot command — script is appropriate (no expression equivalent).
#
# PARKED (responsive): Later bind this control visibility (and/or restore
# sharedDocks.left handle) from page width vs autoBreakpoint 768 —
# hamburger on narrow viewports; persistent left nav on wide. See
# docs/handoff/HANDOFF.md parked note 2026-08-21 nav hamburger.
system.perspective.toggleDock('plant-nav')
```

- **`root/BrandLogo`** `dom.onClick`, nav action, scope `C`: navigate to `/`

- **`root/IntegratorBadge/Badge`** `dom.onClick`, popup action, scope `C`: toggle popup `integratorContact`, view [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./assets/integratorcontact.md)

- **`root/PermBadge`** `dom.onClick`, script action, scope `G`

```python
# Touch / click: show roles without hover (phones/tablets)
self.requestTooltip()
```

- **`root/PermBadge`** `dom.onTouchStart`, script action, scope `G`

```python
self.requestTooltip()
```

- **`root/TrendButton`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/trending')
```

- **`(view)`** change script on `custom.localRouteGuard`

```python
# local-groveport-mode: the expression is the Utility Overview while [default]_Config/DemoEnterpriseNav is off and the
# page is '/' or an enterprise-only route ('' otherwise); navigate is a one-shot command.
target = currentValue.value if currentValue is not None else None
if target and str(self.page.props.path or '') != str(target):
    system.perspective.navigate(page=str(target))
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (7): [00\_Pages/00\_Docked/\_Assets/AlarmNotification](./assets/alarmnotification.md), [00\_Pages/00\_Docked/\_Assets/BrandLogo](./assets/brandlogo.md), [00\_Pages/00\_Docked/\_Assets/IntegratorLogo](./assets/integratorlogo.md), [00\_Pages/00\_Docked/\_Assets/OosNotification](./assets/oosnotification.md), [00\_Pages/00\_Docked/\_Assets/PlcWriteLock](./assets/plcwritelock.md), [00\_Pages/00\_Docked/\_Assets/User](./assets/user.md), [00\_Pages/00\_Docked/\_Assets/UserSettings](./assets/usersettings.md)

**Opens or names** (popups, scripts, expressions): [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./assets/integratorcontact.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `brand-logo-slot` | 1 | stylesheet |
| `color-icon` | 3 | style class |
| `header-icon` | 3 | stylesheet |
| `header-icon-trend` | 1 | stylesheet |
| `integrator-badge` | 1 | stylesheet |
| `integrator-divider` | 1 | stylesheet |
| `integrator-logo-slot` | 1 | stylesheet |
| `nav-menu-btn` | 2 | stylesheet |
| `perm-badge` | 1 | stylesheet |
| `perm-badge-write` | 1 | stylesheet |
| `trend-badge` | 1 | stylesheet |
| `perm-badge-read` | bound | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `[default]_Config/DemoEnterpriseNav`
- `[default]_Config/DemoEnterpriseNav is off and the`
- `[default]_Config/PlcWriteLock/Locked`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
