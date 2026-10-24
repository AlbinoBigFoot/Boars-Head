---
title: "Design"
sidebar_label: "Design"
description: "Perspective view 00_Pages/Boars Head/Tanks/Design (Page piece (not routed)): 5 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Tanks/Design", "Design"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Tanks/Design`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Tanks/Design` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Tanks/Design/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Tanks &gt; Design |
| Root | `ia.container.flex`, height 720, width 1280 |
| Size | 5 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T20:45:00Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Boars_Head/GrovePort/Machine Room/Tanks"` | input |

## Component Tree

Component types: ia.display.view x3, ia.container.flex x2.

```text
root  ia.container.flex  [2 bindings]
  DeviceRow  ia.container.flex
    HTR  ia.display.view  [view: 02_Components/01_Devices/Tank]
    HPR  ia.display.view  [view: 02_Components/01_Devices/Tank]
    LTR  ia.display.view  [view: 02_Components/01_Devices/Tank]
```

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [02\_Components/01\_Devices/Tank](../../../02-components/01-devices/tank.md)

**Opened or named by** (2): [00\_Pages/Boars Head/Tanks/Overview](./overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](../../groveport/machine-room/utility/tanks/overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `themed-scroll` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
