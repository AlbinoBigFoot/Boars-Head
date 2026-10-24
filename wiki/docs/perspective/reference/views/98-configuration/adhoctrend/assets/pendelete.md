---
title: "PenDelete"
sidebar_label: "PenDelete"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/PenDelete (Asset (embedded piece)): 2 components, 2 bindings, 1 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/PenDelete", "PenDelete"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/PenDelete`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/PenDelete` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenDelete/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; PenDelete |
| Root | `ia.container.flex`, height 30, width 60 |
| Size | 2 components, 2 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:35:03Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `row` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.input.button x1.

```text
root  ia.container.flex  [2 bindings]
  Button  ia.input.button  [1 event]
```

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root/Button`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.sendMessage('AdhocTrendDeleteRow',payload={'row':self.view.params.row},scope="page")
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [98\_Configuration/AdhocTrend/Trend](../trend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Container/Button` | 1 | no rule found |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
