---
title: "MetricCard"
sidebar_label: "MetricCard"
description: "Perspective view 02_Components/02_Widgets/MetricCard (Reusable component): 6 components, 8 bindings, 0 event scripts."
generated: true
keywords: ["02_Components/02_Widgets/MetricCard", "MetricCard"]
---

:::note

:::


**Reusable component**: `02_Components/02_Widgets/MetricCard`.

| | |
|---|---|
| View path | `02_Components/02_Widgets/MetricCard` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/02_Widgets/MetricCard/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 02\_Widgets &gt; MetricCard |
| Root | `ia.container.flex`, height 140, width 300 |
| Size | 6 components, 8 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T17:55:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `title` | `"Metric"` | input |
| `value` | `"—"` | input |
| `unit` | `""` | input |
| `category` | `""` | input |

## Component Tree

Component types: ia.display.label x4, ia.container.flex x2.

```text
root  ia.container.flex  [2 bindings]
  Category  ia.display.label  [2 bindings]
  Title  ia.display.label  [1 binding]
  ValueRow  ia.container.flex
    Value  ia.display.label  [1 binding]
    Unit  ia.display.label  [2 bindings]
```

## Bindings

8 bindings: expr 4, property 4.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/Category`**

- `props.text`: property `view.params.category`

- `meta.visible`: expression

```js
len(coalesce({view.params.category}, '')) > 0
```


**`root/Title`**

- `props.text`: property `view.params.title`

**`root/ValueRow/Value`**

- `props.text`: property `view.params.value`

**`root/ValueRow/Unit`**

- `props.text`: property `view.params.unit`

- `meta.visible`: expression

```js
len(coalesce({view.params.unit}, '')) > 0
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `Fonts/LiveDataEntry` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `plant-feature-card` | 1 | stylesheet |
| `plant-feature-title` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
