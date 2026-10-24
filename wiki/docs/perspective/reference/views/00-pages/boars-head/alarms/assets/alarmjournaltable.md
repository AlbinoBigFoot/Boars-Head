---
title: "AlarmJournalTable"
sidebar_label: "AlarmJournalTable"
description: "Perspective view 00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable (Asset (embedded piece)): 2 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable", "AlarmJournalTable"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Alarms &gt; \_Assets &gt; AlarmJournalTable |
| Root | `ia.container.flex`, height 600, width 960 |
| Size | 2 components, 3 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T05:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `sourceFilter` | `"*"` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.alarmjournaltable x1.

```text
root  ia.container.flex  [2 bindings]
  AlarmJournalTable  ia.display.alarmjournaltable  [1 binding]
```

## Bindings

3 bindings: expr-struct 2, property 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../common-patterns.md#pattern-1).

**`root/AlarmJournalTable`**

- `props.filter.conditions.source`: property `view.params.sourceFilter`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Alarms/Journal](../journal.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
