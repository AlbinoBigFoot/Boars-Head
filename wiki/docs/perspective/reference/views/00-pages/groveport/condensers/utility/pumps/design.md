---
title: "Design"
sidebar_label: "Design"
description: "Perspective view 00_Pages/Groveport/Condensers/Utility/Pumps/Design (Page piece (not routed)): 5 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Condensers/Utility/Pumps/Design", "Design"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Condensers/Utility/Pumps/Design`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Condensers/Utility/Pumps/Design` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Condensers/Utility/Pumps/Design/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Condensers &gt; Utility &gt; Pumps &gt; Design |
| Root | `ia.container.flex`, height 720, width 1280 |
| Size | 5 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Boars_Head/GrovePort/Condensers/Pumps"` | input |

## Component Tree

Component types: ia.display.view x3, ia.container.flex x2.

```text
root  ia.container.flex  [2 bindings]
  DeviceRow  ia.container.flex
    Sump_Pump_1  ia.display.view  [view: 02_Components/01_Devices/Pump]
    Sump_Pump_2  ia.display.view  [view: 02_Components/01_Devices/Pump]
    Sump_Pump_3  ia.display.view  [view: 02_Components/01_Devices/Pump]
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

**Embeds** (1): [02\_Components/01\_Devices/Pump](../../../../../02-components/01-devices/pump.md)

**Opened or named by** (1): [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](./overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `themed-scroll` | 1 | stylesheet |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
