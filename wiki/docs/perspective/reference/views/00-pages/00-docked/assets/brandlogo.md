---
title: "BrandLogo"
sidebar_label: "BrandLogo"
description: "Perspective view 00_Pages/00_Docked/_Assets/BrandLogo (Asset (embedded piece)): 3 components, 5 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/BrandLogo", "BrandLogo"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/BrandLogo`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/BrandLogo` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/BrandLogo/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; BrandLogo |
| Root | `ia.container.flex`, width 176, height 30 |
| Size | 3 components, 5 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-22T16:26:11Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `collapsible` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `logo` | `{"dark": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkgAAABkCAM...` | |

## Component Tree

Component types: ia.display.image x2, ia.container.flex x1.

```text
root  ia.container.flex  [2 bindings]
  Lockup  ia.display.image  [1 binding]
  Mark  ia.display.image  [2 bindings]
```

## Bindings

5 bindings: expr 4, property 1.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Lockup`**

- `props.source`: expression

```js
if(left(lower(coalesce({session.props.theme}, '')), 4) = 'dark', {view.custom.logo.dark}, {view.custom.logo.light})
```


**`root/Mark`**

- `props.source`: property `view.custom.logo.mark`

- `position.display`: expression

```js
coalesce({view.params.collapsible}, false)
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [00\_Pages/00\_Docked/Header](../header.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `brand-logo-full` | 1 | stylesheet |
| `brand-logo-mark` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
