---
title: "Design"
sidebar_label: "Design"
description: "Perspective view 00_Pages/Groveport/Condensers/Utility/CondenserFans/Design (Page piece (not routed)): 4 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Condensers/Utility/CondenserFans/Design", "Design"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Condensers/Utility/CondenserFans/Design`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Condensers/Utility/CondenserFans/Design` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Condensers/Utility/CondenserFans/Design/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Condensers &gt; Utility &gt; CondenserFans &gt; Design |
| Root | `ia.container.flex`, height 720, width 1280 |
| Size | 4 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Boars_Head/GrovePort/Condensers/Condensers"` | input |

## Component Tree

Component types: ia.container.flex x2, ia.display.view x2.

```text
root  ia.container.flex  [2 bindings]
  DeviceRow  ia.container.flex
    EC-1A  ia.display.view  [view: 02_Components/01_Devices/Condenser]
    EC-1B  ia.display.view  [view: 02_Components/01_Devices/Condenser]
```

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [02\_Components/01\_Devices/Condenser](../../../../../02-components/01-devices/condenser.md)

**Opened or named by** (1): [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](./overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `themed-scroll` | 1 | stylesheet |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
