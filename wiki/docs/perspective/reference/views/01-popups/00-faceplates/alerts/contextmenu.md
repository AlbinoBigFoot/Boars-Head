---
title: "ContextMenu"
sidebar_label: "ContextMenu"
description: "Perspective view 01_Popups/00_Faceplates/Alerts/ContextMenu (Popup / faceplate): 5 components, 15 bindings, 5 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Alerts/ContextMenu", "ContextMenu"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Alerts/ContextMenu`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Alerts/ContextMenu` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/ContextMenu/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Alerts &gt; ContextMenu |
| Root | `ia.container.flex`, height 152, width 180 |
| Size | 5 components, 15 bindings, 5 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:51:20Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `discrete` | `false` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `inArray` | `false` | bound (expr-struct) |

## Component Tree

Component types: ia.display.view x4, ia.container.flex x1.

```text
root  ia.container.flex  [2 bindings; 1 event]
  TicketLogger  ia.display.view  [2 bindings; 1 event; view: 01_Popups/00_Faceplates/Alerts/Menu]
  AddToTrend  ia.display.view  [3 bindings; 1 event; view: 01_Popups/00_Faceplates/Alerts/Menu]
  RemoveToTrend  ia.display.view  [3 bindings; 1 event; view: 01_Popups/00_Faceplates/Alerts/Menu]
  OpenTrend  ia.display.view  [3 bindings; 1 event; view: 01_Popups/00_Faceplates/Alerts/Menu]
```

## Bindings

15 bindings: property 10, expr 4, expr-struct 1.

<details>
<summary>All 15 bindings, grouped by component</summary>

**`(view)`**

- `custom.inArray`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
tags: {session.custom.AdhocTrend.tags}
```

waitOnAll: `True`

Transform 1, script:

```python
if value.tagPath != '' and len(value.tags) > 0:
    if value.tagPath in value.tags:
        return True
return False
```


- `props.defaultSize.height`: expression

```js
if({session.custom.TicketLogAccess}, 152, 120)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/TicketLogger`**

- `meta.visible`: property `session.custom.TicketLogAccess`

- `position.basis`: expression

```js
if({session.custom.TicketLogAccess}, "32px", "0px")
```


**`root/AddToTrend`**

- `props.params.classes`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if(!{value},
	"container-item Fonts/Header",
	"container-item bg-disabled Fonts/BadData"
)
```


- `props.params.cursor`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if(!{value},
	"pointer",
	"auto"
)
```


- `props.params.fontWeight`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if(!{value},
	"500",
	"normal"
)
```


**`root/RemoveToTrend`**

- `props.params.classes`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if({value},
	"container-item Fonts/Header",
	"container-item bg-disabled Fonts/BadData"
)
```


- `props.params.cursor`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if({value},
	"pointer",
	"auto"
)
```


- `props.params.fontWeight`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if({value},
	"500",
	"normal"
)
```


**`root/OpenTrend`**

- `props.params.classes`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if({value},
	"container-item Fonts/Header",
	"container-item bg-disabled Fonts/BadData"
)
```


- `props.params.cursor`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if({value},
	"pointer",
	"auto"
)
```


- `props.params.fontWeight`: property `view.custom.inArray`, then expression transform

Transform 1, expression:

```js
if({value},
	"500",
	"normal"
)
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onMouseLeave`, popup action, scope `C`: close popup `ContextMenu`, view [01\_Popups/00\_Faceplates/Alerts/ContextMenu](./contextmenu.md)

- **`root/TicketLogger`** `dom.onClick`, script action, scope `G`

```python
tagPath = self.view.params.tagPath
viewName = self.view.id.split('@')[0]
shared.Alerts.contextMenuTicketLog(tagPath, viewName)
system.perspective.closePopup('ContextMenu')
```

- **`root/AddToTrend`** `dom.onClick`, script action, scope `G`

```python
if len(self.session.custom.AdhocTrend.tags) < 10:
    tagPath = self.view.params.tagPath
    if tagPath not in self.session.custom.AdhocTrend.tags:
        self.session.custom.AdhocTrend.tags.append(tagPath)
        _pid, plots, penPlots = shared.AdhocTrend.route_new_pen(self.session.custom.AdhocTrend, tagPath)
        self.session.custom.AdhocTrend.plots = plots
        self.session.custom.AdhocTrend.penPlots = penPlots
    shared.Alerts.showAdhocTrend()
    system.perspective.closePopup('ContextMenu')
else:
    shared.Alerts.showAlert(state="warning",title="Adhoc Trending",message='You have exceeded the limit of 10 tags, Please remove tags that are not required from the trend.',showCloseBtn=False,btnTextPrimary="Okay",btnTextSecondary="",btnActionPrimary="",btnActionSecondary="",payload={})
```

- **`root/RemoveToTrend`** `dom.onClick`, script action, scope `G`

```python
tagPath = self.view.params.tagPath
if tagPath in self.session.custom.AdhocTrend.tags:
    self.session.custom.AdhocTrend.tags.remove(tagPath)
    system.perspective.closePopup('ContextMenu')
```

- **`root/OpenTrend`** `dom.onClick`, script action, scope `G`

```python
tagPath = self.view.params.tagPath
if tagPath in self.session.custom.AdhocTrend.tags:
    shared.Alerts.showAdhocTrend()
    system.perspective.closePopup('ContextMenu')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.AdhocTrend.route\_new\_pen](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/Alerts/Menu](./menu.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-component` | 1 | stylesheet |
| `container-card` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
