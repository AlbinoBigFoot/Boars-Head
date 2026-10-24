---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview (Page): 7 components, 0 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview", "Overview", "/safety-relay"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Machine Room &gt; Utility &gt; SafetyRelay &gt; Overview |
| Routes | `/safety-relay` (Safety Relay) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 7 components, 0 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x1, ia.input.button x1, ia.display.view x1.

```text
root  ia.container.flex
  Header  ia.container.flex
    Spacer  ia.container.flex
    Title  ia.display.label
    View3d  ia.input.button  [1 event]
  Body  ia.container.flex
    SafetyRelay  ia.display.view  [view: 02_Components/01_Devices/SafetyRelay]
```

## Event Scripts And Handlers

- **`root/Header/View3d`** `component.onActionPerformed`, script action, scope `G`

```python
# UI navigation only: the read-only 3D safety relay page
system.perspective.navigate('/safety-relay/3d')
```

## Related Views

**Embeds** (1): [02\_Components/01\_Devices/SafetyRelay](../../../../../02-components/01-devices/safetyrelay.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `bg-page` | 1 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `fs-20` | 1 | style class |
| `fw-700` | 1 | style class |
| `safety-relay-zoom` | 1 | stylesheet |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
