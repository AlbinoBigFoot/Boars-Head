---
title: "Blank"
sidebar_label: "Blank"
description: "Perspective view 03_Elements/01_Status/NotificationIcons/Blank (Element (small reusable part)): 2 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/NotificationIcons/Blank", "Blank"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/NotificationIcons/Blank`.

| | |
|---|---|
| View path | `03_Elements/01_Status/NotificationIcons/Blank` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/NotificationIcons/Blank/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; NotificationIcons &gt; Blank |
| Root | `ia.container.flex`, height 20, width 20 |
| Size | 2 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T04:25:28Z by the Designer |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1.

```text
root  ia.container.flex  [2 bindings]
  Icon  ia.display.icon
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

**Opened or named by** (2): [03\_Elements/01\_Status/AlarmHeader](../alarmheader.md), [03\_Elements/03\_Table/DeviceLabelAlarmIndicator](../../03-table/devicelabelalarmindicator.md)
