---
title: "CG-B2"
sidebar_label: "CG-B2"
description: "Perspective view 00_Pages/Groveport/SuperChill/Utility/CG-B2 (Page): 2 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/SuperChill/Utility/CG-B2", "CG-B2", "/cg-b2"]
---

:::note

:::


**Page**: `00_Pages/Groveport/SuperChill/Utility/CG-B2`.

| | |
|---|---|
| View path | `00_Pages/Groveport/SuperChill/Utility/CG-B2` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/SuperChill/Utility/CG-B2/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; SuperChill &gt; Utility &gt; CG-B2 |
| Routes | `/cg-b2` (CG-B2) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 2 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-31T22:00:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  AhuEvapDisplay  ia.display.view  [view: 00_Pages/Groveport/_Shared/CG/AhuEvapDisplay]
```

## Bindings

2 bindings: expr 2.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](../../shared/cg/ahuevapdisplay.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
