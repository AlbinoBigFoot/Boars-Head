---
title: "Override"
sidebar_label: "Override"
description: "Perspective view 03_Elements/01_Status/Icons/Override (Element (small reusable part)): 2 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/Icons/Override", "Override"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/Icons/Override`.

| | |
|---|---|
| View path | `03_Elements/01_Status/Icons/Override` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/Icons/Override/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; Icons &gt; Override |
| Root | `ia.container.flex`, no default size |
| Size | 2 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T20:00:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [2 bindings]
  SVG  ia.shapes.svg
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

**Embedded in** (2): [00\_Pages/00\_Docked/Legend](../../../00-pages/00-docked/legend.md), [03\_Elements/01\_Status/IconHeader](../iconheader.md)
