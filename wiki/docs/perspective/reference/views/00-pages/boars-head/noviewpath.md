---
title: "NoViewPath"
sidebar_label: "NoViewPath"
description: "Perspective view 00_Pages/Boars Head/NoViewPath (Page): 2 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/NoViewPath", "NoViewPath", "/no-view"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/NoViewPath`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/NoViewPath` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/NoViewPath/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; NoViewPath |
| Routes | `/no-view` (No View) |
| Root | `ia.container.flex`, no default size |
| Size | 2 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T04:11:57Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `data` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1.

```text
root  ia.container.flex  [2 bindings]
  Label  ia.display.label
```

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (18): [00\_Pages/Boars Head/Compressors/Overview](./compressors/overview.md), [00\_Pages/Boars Head/Devices/Overview](./devices/overview.md), [00\_Pages/Boars Head/ExhaustFans/Overview](./exhaustfans/overview.md), [00\_Pages/Boars Head/Pumps/Overview](./pumps/overview.md), [00\_Pages/Boars Head/Sensors/Overview](./sensors/overview.md), [00\_Pages/Boars Head/Tanks/Overview](./tanks/overview.md), [00\_Pages/Boars Head/Valves/Overview](./valves/overview.md), [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Overview](../groveport/condensers/utility/condenserfans/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Overview](../groveport/condensers/utility/pumps/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Overview](../groveport/condensers/utility/sensors/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Overview](../groveport/condensers/utility/tanks/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Overview](../groveport/condensers/utility/valves/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Compressors/Overview](../groveport/machine-room/utility/compressors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview](../groveport/machine-room/utility/exhaustfans/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Pumps/Overview](../groveport/machine-room/utility/pumps/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Sensors/Overview](../groveport/machine-room/utility/sensors/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Tanks/Overview](../groveport/machine-room/utility/tanks/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Valves/Overview](../groveport/machine-room/utility/valves/overview.md)
