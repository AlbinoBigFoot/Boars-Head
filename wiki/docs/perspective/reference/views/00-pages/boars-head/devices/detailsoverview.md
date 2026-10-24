---
title: "DetailsOverview"
sidebar_label: "DetailsOverview"
description: "Perspective view 00_Pages/Boars Head/Devices/DetailsOverview (Page piece (not routed)): 17 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Devices/DetailsOverview", "DetailsOverview"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Devices/DetailsOverview`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Devices/DetailsOverview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Devices/DetailsOverview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Devices &gt; DetailsOverview |
| Root | `ia.container.flex`, height 800, width 1200 |
| Size | 17 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T15:50:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x7, ia.display.label x5, ia.display.view x5.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  TablesGrid  ia.container.flex
    Evaporators  ia.container.flex
      Title  ia.display.label
      UnitOverview  ia.display.view  [view: 00_Pages/Boars Head/Unit/Overview]
    Compressors  ia.container.flex
      Title  ia.display.label
      UnitOverview  ia.display.view  [view: 00_Pages/Boars Head/Unit/Overview]
    CoolingTowers  ia.container.flex
      Title  ia.display.label
      UnitOverview  ia.display.view  [view: 00_Pages/Boars Head/Unit/Overview]
    Pumps  ia.container.flex
      Title  ia.display.label
      UnitOverview  ia.display.view  [view: 00_Pages/Boars Head/Unit/Overview]
    ExhaustFans  ia.container.flex
      Title  ia.display.label
      UnitOverview  ia.display.view  [view: 00_Pages/Boars Head/Unit/Overview]
```

</details>

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/Boars Head/Unit/Overview](../unit/overview.md)

**Opened or named by** (1): [00\_Pages/Boars Head/Devices/Overview](./overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 5 | style class |
| `container-card` | 10 | stylesheet |
| `fs-15` | 5 | style class |
| `fw-700` | 5 | style class |
| `unit-overview-grid` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
