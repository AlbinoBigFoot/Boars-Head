---
title: "VesselGeneric"
sidebar_label: "VesselGeneric"
description: "Perspective view 98_Configuration/ComponentPreview/VesselGeneric (Configuration / tool view): 40 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["98_Configuration/ComponentPreview/VesselGeneric", "VesselGeneric"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/ComponentPreview/VesselGeneric`.

| | |
|---|---|
| View path | `98_Configuration/ComponentPreview/VesselGeneric` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/ComponentPreview/VesselGeneric/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; ComponentPreview &gt; VesselGeneric |
| Root | `ia.container.flex`, width 1400, height 900 |
| Size | 40 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Component Tree

Component types: ia.display.label x21, ia.display.view x12, ia.container.flex x4, ia.container.coord x3.

<details>
<summary>Component tree (40 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  VesselGeneric(Figma2x)  ia.container.flex
    Title  ia.display.label
    Native  ia.container.coord
      Horizontal  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      CapH  ia.display.label
      Vertical  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      CapV  ia.display.label
  ScalingInACoordinateContainer  ia.container.flex
    Title  ia.display.label
    Scaling  ia.container.coord
      Box80x40  ia.display.label
      Vessel80x40  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      Cap80x40  ia.display.label
      Box240x120  ia.display.label
      Vessel240x120  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      Cap240x120  ia.display.label
      Box320x80  ia.display.label
      Vessel320x80  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      Cap320x80  ia.display.label
      Box48x84  ia.display.label
      Vessel48x84  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      Cap48x84  ia.display.label
      Box144x252  ia.display.label
      Vessel144x252  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      Cap144x252  ia.display.label
      Box96x120  ia.display.label
      Vessel96x120  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      Cap96x120  ia.display.label
  Labels  ia.container.flex
    Title  ia.display.label
    Labels  ia.container.coord
      LongH  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      CapLH  ia.display.label
      LongV  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      CapLV  ia.display.label
      Leaf  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      CapLeaf  ia.display.label
      Empty  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
      CapEmpty  ia.display.label
```

</details>

## Bindings

2 bindings: expr 2.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [02\_Components/01\_Devices/VesselGeneric](../../02-components/01-devices/vesselgeneric.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 3 | style class |
| `bg-page` | 1 | style class |
| `fs-11` | 12 | style class |
| `fs-16` | 3 | style class |
| `fw-400` | 12 | style class |
| `fw-700` | 3 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
