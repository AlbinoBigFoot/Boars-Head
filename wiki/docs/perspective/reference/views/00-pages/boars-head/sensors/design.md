---
title: "Design"
sidebar_label: "Design"
description: "Perspective view 00_Pages/Boars Head/Sensors/Design (Page piece (not routed)): 8 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Sensors/Design", "Design"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Sensors/Design`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Sensors/Design` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Sensors/Design/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Sensors &gt; Design |
| Root | `ia.container.flex`, height 720, width 1280 |
| Size | 8 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T21:30:00Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Boars_Head/GrovePort/Machine Room/Sensors"` | input |

## Component Tree

Component types: ia.display.view x6, ia.container.flex x2.

```text
root  ia.container.flex  [2 bindings]
  DeviceRow  ia.container.flex
    HSS_Pumps_Pressure  ia.display.view  [view: 02_Components/01_Devices/Sensor]
    HSD_Discharge_Pressure  ia.display.view  [view: 02_Components/01_Devices/Sensor]
    HSL_Pumps_Pressure  ia.display.view  [view: 02_Components/01_Devices/Sensor]
    LSS_Pumps_Pressure  ia.display.view  [view: 02_Components/01_Devices/Sensor]
    LSL_Pumps_Pressure  ia.display.view  [view: 02_Components/01_Devices/Sensor]
    Condenser_Sump_Level  ia.display.view  [view: 02_Components/01_Devices/Sensor]
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

**Embeds** (1): [02\_Components/01\_Devices/Sensor](../../../02-components/01-devices/sensor.md)

**Opened or named by** (2): [00\_Pages/Boars Head/Sensors/Overview](./overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](../../groveport/machine-room/utility/sensors/overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `themed-scroll` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
