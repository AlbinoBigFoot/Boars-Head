---
title: "PenEnable"
sidebar_label: "PenEnable"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/PenEnable (Asset (embedded piece)): 2 components, 3 bindings, 1 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/PenEnable", "PenEnable"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/PenEnable`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/PenEnable` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenEnable/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; PenEnable |
| Root | `ia.container.flex`, height 30, width 30 |
| Size | 2 components, 3 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:35:03Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `row` | `""` | input |
| `rowData` | `""` | input |
| `value` | `true` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1.

```text
root  ia.container.flex  [2 bindings]
  Icon  ia.display.icon  [1 binding; 1 event]
```

## Bindings

3 bindings: expr-struct 2, property 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Icon`**

- `props.path`: property `view.params.value`, then expression transform

Transform 1, expression:

```js
if({value},
	'material/check_box',
	'material/check_box_outline_blank'
)
```


## Event Scripts And Handlers

- **`root/Icon`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage('AdhocTrendDisableRow',payload={'row':self.view.params.row,'penName':self.view.params.rowData.penName},scope="page")
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [98\_Configuration/AdhocTrend/Trend](../trend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Colors/Icon` | 1 | no rule found |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
