---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview (Page): 42 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview", "Overview", "/rupture-disks"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Machine Room &gt; Utility &gt; RuptureDisks &gt; Overview |
| Routes | `/rupture-disks` (Rupture Disks) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 42 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-21T12:00:00Z by the Designer |

## Component Tree

Component types: ia.display.view x34, ia.container.flex x7, ia.display.label x1.

<details>
<summary>Component tree (42 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Title  ia.display.label
  Grid  ia.container.flex
    Column1  ia.container.flex
      PS01  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS02  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS03  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS04  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS05  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS06  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS07  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS08  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    Column2  ia.container.flex
      PS09  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS10  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS14  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS15  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS16  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS17  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS18  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS19  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    Column3  ia.container.flex
      PS20  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS21  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS22  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS23  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS24  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS25  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS26  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS27  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    Column4  ia.container.flex
      PS28  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS29  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS30  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS31  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS32  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS33  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS34  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS35  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    Column5  ia.container.flex
      PS36  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
      PS37  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
```

</details>

## Bindings

2 bindings: expr 2.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../../common-patterns.md#pattern-2).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/Groveport/Utility/OverviewStatusTile](../../../utility/overviewstatustile.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 1 | style class |
| `bg-page` | 1 | style class |
| `fs-20` | 1 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
