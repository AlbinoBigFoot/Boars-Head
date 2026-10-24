---
title: "Sensor"
sidebar_label: "Sensor"
description: "Perspective view 01_Popups/00_Faceplates/Sensor (Popup / faceplate): 2 components, 4 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Sensor", "Sensor"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Sensor`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Sensor` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Sensor/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Sensor |
| Root | `ia.container.flex`, height 640, width 560 |
| Size | 2 components, 4 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T00:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `showInterlocks` | `true` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  FaceplateShell  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/Faceplate]
```

## Bindings

4 bindings: expr-struct 2, property 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/FaceplateShell`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

- `props.params.showInterlocks`: property `view.params.showInterlocks`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/Faceplate](./faceplate.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-pages/00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-pages/00-docked/tempnav.md)
