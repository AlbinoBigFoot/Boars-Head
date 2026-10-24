---
title: "Evaporator"
sidebar_label: "Evaporator"
description: "Perspective view 01_Popups/00_Faceplates/Evaporator (Popup / faceplate): 2 components, 4 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Evaporator", "Evaporator"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Evaporator`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Evaporator` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Evaporator/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Evaporator |
| Opened from the nav tree | Boars Head &gt; Groveport &gt; Freezer &gt; Utility &gt; CG-A1 &gt; Devices &gt; Evaporator<br/>Boars Head &gt; Groveport &gt; Freezer &gt; Utility &gt; CG-A2 &gt; Devices &gt; Evaporator<br/>Boars Head &gt; Groveport &gt; SuperChill &gt; Utility &gt; CG-B1 &gt; Devices &gt; Evaporator<br/>Boars Head &gt; Groveport &gt; SuperChill &gt; Utility &gt; CG-B2 &gt; Devices &gt; Evaporator<br/>Boars Head &gt; Groveport &gt; Club &gt; Utility &gt; CG-C1 &gt; Devices &gt; Evaporator<br/>Boars Head &gt; Groveport &gt; Palletizing &gt; Utility &gt; CG-D1 &gt; Devices &gt; Evaporator<br/>... and 13 more nav items |
| Root | `ia.container.flex`, height 640, width 560 |
| Size | 2 components, 4 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T03:44:26Z by the Designer |

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
