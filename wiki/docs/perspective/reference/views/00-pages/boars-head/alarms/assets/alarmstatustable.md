---
title: "AlarmStatusTable"
sidebar_label: "AlarmStatusTable"
description: "Perspective view 00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable (Asset (embedded piece)): 2 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable", "AlarmStatusTable"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Alarms &gt; \_Assets &gt; AlarmStatusTable |
| Root | `ia.container.flex`, height 600, width 960 |
| Size | 2 components, 6 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T14:14:56Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `sourceFilter` | `"*"` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.alarmstatustable x1.

```text
root  ia.container.flex  [2 bindings]
  AlarmStatusTable  ia.display.alarmstatustable  [4 bindings]
```

## Bindings

6 bindings: expr 3, expr-struct 2, property 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../common-patterns.md#pattern-1).

**`root/AlarmStatusTable`**

- `props.filters.active.conditions.source`: property `view.params.sourceFilter`

- `props.enableAcknowledge`: expression

```js
coalesce({session.custom.Permissions.AlarmSummary.Acknowledge}, false)
```


- `props.enableShelve`: expression

```js
coalesce({session.custom.Permissions.AlarmSummary.Shelve}, false)
```


- `props.enableUnshelve`: expression

```js
coalesce({session.custom.Permissions.AlarmSummary.Shelve}, false)
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Alarms/Summary](../summary.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
