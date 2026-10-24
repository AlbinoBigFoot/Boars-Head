---
title: "Details"
sidebar_label: "Details"
description: "Perspective view 00_Pages/Groveport/Machine Room/Utility/Compressors/Details (Page piece (not routed)): 2 components, 4 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Machine Room/Utility/Compressors/Details", "Details"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Machine Room/Utility/Compressors/Details`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Machine Room/Utility/Compressors/Details` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/Compressors/Details/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Machine Room &gt; Utility &gt; Compressors &gt; Details |
| Root | `ia.container.flex`, height 720, width 1280 |
| Size | 2 components, 4 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T20:45:00Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Boars_Head/GrovePort/Machine Room/Compressors"` | input |
| `typeId` | `"Devices/Compressor"` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  TypeTable  ia.display.view  [2 bindings; view: 00_Pages/Boars Head/Devices/TypeTable]
```

## Bindings

4 bindings: expr-struct 2, property 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../../common-patterns.md#pattern-1).

**`root/TypeTable`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../../common-patterns.md#pattern-5).

- `props.params.typeId`: property `view.params.typeId`. Common pattern, see [pattern-7](../../../../../../common-patterns.md#pattern-7).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/Boars Head/Devices/TypeTable](../../../../boars-head/devices/typetable.md)

**Opened or named by** (2): [00\_Pages/Boars Head/Compressors/Overview](../../../../boars-head/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](./overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
