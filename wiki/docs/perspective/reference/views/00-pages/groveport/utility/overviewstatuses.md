---
title: "OverviewStatuses"
sidebar_label: "OverviewStatuses"
description: "Perspective view 00_Pages/Groveport/Utility/OverviewStatuses (Page piece (not routed)): 13 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Utility/OverviewStatuses", "OverviewStatuses"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Utility/OverviewStatuses`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Utility/OverviewStatuses` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Utility/OverviewStatuses/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Utility &gt; OverviewStatuses |
| Root | `ia.container.flex`, height 900, width 168 |
| Size | 13 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-21T12:00:00Z by the Designer |

## Component Tree

Component types: ia.display.view x12, ia.container.flex x1.

<details>
<summary>Component tree (13 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  AD06  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  FD03  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  AD05  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  FD04  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  AD07  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  FD05  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  AD08  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  AD01  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  AD03  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  AD02  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  FD01  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
  AD04  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
```

</details>

## Bindings

2 bindings: expr 2.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/Groveport/Utility/OverviewStatusTile](./overviewstatustile.md)

**Embedded in** (1): [00\_Pages/Groveport/Utility/Overview](./overview.md)
