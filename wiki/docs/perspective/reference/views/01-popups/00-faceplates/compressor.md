---
title: "Compressor"
sidebar_label: "Compressor"
description: "Perspective view 01_Popups/00_Faceplates/Compressor (Popup / faceplate): 2 components, 5 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Compressor", "Compressor"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Compressor`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Compressor` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Compressor/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Compressor |
| Root | `ia.container.flex`, height 640, width 560 |
| Size | 2 components, 5 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T16:12:37Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `webGuiUrl` | `""` | input |
| `showInterlocks` | `true` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  FaceplateShell  ia.display.view  [3 bindings; view: 01_Popups/00_Faceplates/Faceplate]
```

## Bindings

5 bindings: property 3, expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/FaceplateShell`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

- `props.params.webGuiUrl`: property `view.params.webGuiUrl`

- `props.params.showInterlocks`: property `view.params.showInterlocks`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/Faceplate](./faceplate.md)
