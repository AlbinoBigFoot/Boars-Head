---
title: "Condenser-SafetyRelay"
sidebar_label: "Condenser-SafetyRelay"
description: "Perspective view 98_Configuration/ComponentPreview/Condenser-SafetyRelay (Configuration / tool view): 27 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["98_Configuration/ComponentPreview/Condenser-SafetyRelay", "Condenser-SafetyRelay"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/ComponentPreview/Condenser-SafetyRelay`.

| | |
|---|---|
| View path | `98_Configuration/ComponentPreview/Condenser-SafetyRelay` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/ComponentPreview/Condenser-SafetyRelay/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; ComponentPreview &gt; Condenser-SafetyRelay |
| Root | `ia.container.flex`, width 1900, height 1400 |
| Size | 27 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Component Tree

Component types: ia.display.view x17, ia.container.flex x7, ia.display.label x3.

<details>
<summary>Component tree (27 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Condenser-3Fans  ia.container.flex
    Title  ia.display.label
    Row  ia.container.flex
      Unknown  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Stopped  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Running  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Starting  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Stopping  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Disabled  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      CommLoss  ia.display.view  [view: 02_Components/01_Devices/Condenser]
  Condenser-2Fans  ia.container.flex
    Title  ia.display.label
    Row  ia.container.flex
      Unknown  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Stopped  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Running  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Starting  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Stopping  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      Disabled  ia.display.view  [view: 02_Components/01_Devices/Condenser]
      CommLoss  ia.display.view  [view: 02_Components/01_Devices/Condenser]
  SafetyRelay  ia.container.flex
    Title  ia.display.label
    Row  ia.container.flex
      Normal  ia.display.view  [view: 02_Components/01_Devices/SafetyRelay]
      Fault  ia.display.view  [view: 02_Components/01_Devices/SafetyRelay]
      CommLoss  ia.display.view  [view: 02_Components/01_Devices/SafetyRelay]
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

**Embeds** (2): [02\_Components/01\_Devices/Condenser](../../02-components/01-devices/condenser.md), [02\_Components/01\_Devices/SafetyRelay](../../02-components/01-devices/safetyrelay.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 3 | style class |
| `bg-page` | 1 | style class |
| `fs-16` | 3 | style class |
| `fw-700` | 3 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
