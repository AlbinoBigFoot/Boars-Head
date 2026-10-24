---
title: "DoorStatus"
sidebar_label: "DoorStatus"
description: "Perspective view 03_Elements/01_Status/Icons/DoorStatus (Element (small reusable part)): 3 components, 9 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/Icons/DoorStatus", "DoorStatus"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/Icons/DoorStatus`.

| | |
|---|---|
| View path | `03_Elements/01_Status/Icons/DoorStatus` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/Icons/DoorStatus/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; Icons &gt; DoorStatus |
| Root | `ia.container.flex`, height 85, width 72 |
| Size | 3 components, 9 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T20:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `quality` | `"Uncertain_InitialValue"` | bound (expr) |
| `tagValue` | `""` | bound (expr) |

## Component Tree

Component types: ia.shapes.svg x2, ia.container.flex x1.

```text
root  ia.container.flex  [2 bindings]
  door-open  ia.shapes.svg  [1 binding]
  door-closed  ia.shapes.svg  [4 bindings]
```

## Bindings

9 bindings: expr 5, expr-struct 2, property 2.

**`(view)`**

- `custom.quality`: expression

```js
qualityOf(tag({view.params.tagPath}))
```


- `custom.tagValue`: expression

```js
if({view.custom.quality} = 'Good',
   tag({view.params.tagPath}),
   '')
```


**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/door-open`**

- `position.display`: expression

```js
if({view.custom.quality} = 'Good',
   !{view.custom.tagValue},
   False)
```


**`root/door-closed`**

- `custom.fill`: expression

```js
if({view.custom.quality} = 'Good',
   'var(--success)',
   'var(--icon)')
```


- `position.display`: expression

```js
{view.custom.tagValue} || {view.custom.quality} != 'Good'
```


- `props.elements[0].fill.paint`: property `this.custom.fill`

- `props.elements[1].fill.paint`: property `this.custom.fill`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).
