---
title: "AnalogValue"
sidebar_label: "AnalogValue"
description: "Perspective view 03_Elements/00_Control/AnalogValue (Element (small reusable part)): 2 components, 7 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/00_Control/AnalogValue", "AnalogValue"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/00_Control/AnalogValue`.

| | |
|---|---|
| View path | `03_Elements/00_Control/AnalogValue` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/00_Control/AnalogValue/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 00\_Control &gt; AnalogValue |
| Root | `ia.container.flex`, height 20, width 100 |
| Size | 2 components, 7 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-28T23:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `permissions` | `true` | input |
| `setpoint` | `true` | input |
| `spacing` | `{"center": true, "data": 0, "engUnit": 30}` | input |
| `tagPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Numeric  ia.display.view  [5 bindings; view: 03_Elements/00_Control/_Assets/Numeric]
```

## Bindings

7 bindings: property 4, expr-struct 2, expr 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/Numeric`**

- `position.grow`: expression

```js
if({view.params.spacing.center},
	0,
	1)
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

- `props.params.permissions`: property `view.params.permissions`

- `props.params.setpoint`: property `view.params.setpoint`

- `props.params.spacing.center`: property `view.params.spacing.center`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [03\_Elements/00\_Control/\_Assets/Numeric](./assets/numeric.md)
