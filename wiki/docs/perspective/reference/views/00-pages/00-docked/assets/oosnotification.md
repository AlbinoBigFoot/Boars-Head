---
title: "OosNotification"
sidebar_label: "OosNotification"
description: "Perspective view 00_Pages/00_Docked/_Assets/OosNotification (Asset (embedded piece)): 3 components, 7 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/OosNotification", "OosNotification"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/OosNotification`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/OosNotification` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/OosNotification/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; OosNotification |
| Root | `ia.container.flex`, height 36, width 36 |
| Size | 3 components, 7 bindings, 1 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `count` | `0` | bound (query) |
| `bump` | `0` | |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1, ia.display.label x1.

```text
root  ia.container.flex  [4 bindings; 1 event]
  Icon  ia.display.icon
  Count  ia.display.label  [2 bindings]
```

## Bindings

7 bindings: expr 6, query 1.

**`(view)`**

- `custom.count`: named query

Named query `OutOfService/OpenCount`, return format `scalar`

```js
allowed: if(coalesce({session.custom.Permissions.OutOfService.View}, false), 1, 0)
refresh: toMillis(now(30000)) + coalesce({view.custom.bump}, 0)
```


**`root`**

- `meta.tooltip.text`: expression

```js
'Out Of Service Log - ' + if(coalesce(try(toInt({view.custom.count}), 0), 0) = 0, 'No Devices Out Of Service', toStr(coalesce(try(toInt({view.custom.count}), 0), 0)) + ' Device' + if(coalesce(try(toInt({view.custom.count}), 0), 0) = 1, '', 's') + ' Out Of Service')
```


- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Count`**

- `props.text`: expression

```js
if(coalesce(try(toInt({view.custom.count}), 0), 0) > 99, '99+', toStr(coalesce(try(toInt({view.custom.count}), 0), 0)))
```


- `meta.visible`: expression

```js
coalesce(try(toInt({view.custom.count}), 0), 0) > 0
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/operations/out-of-service')
```

- **`root`** message handler `oosChanged` (scope: session)

```python
# Out Of Service change in this session (shared.OutOfService): requery now, not at the next 30 s poll
self.view.custom.bump = (self.view.custom.bump or 0) + 1
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.OutOfService](../../../../../../scripting/reference/modules/shared-outofservice.md).

## Related Views

**Embedded in** (1): [00\_Pages/00\_Docked/Header](../header.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `color-icon` | 1 | style class |
| `header-alarm-count` | 1 | stylesheet |
| `header-icon` | 1 | stylesheet |
| `header-oos-count` | 1 | stylesheet |
| `nav-menu-btn` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Named queries: `OutOfService/OpenCount`.

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
