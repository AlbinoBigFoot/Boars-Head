---
title: "Tags"
sidebar_label: "Tags"
description: "Perspective view 98_Configuration/Tools/L5K/Tags (Configuration / tool view): 2 components, 3 bindings, 1 event scripts."
generated: true
keywords: ["98_Configuration/Tools/L5K/Tags", "Tags"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/Tools/L5K/Tags`.

| | |
|---|---|
| View path | `98_Configuration/Tools/L5K/Tags` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/Tools/L5K/Tags/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; Tools &gt; L5K &gt; Tags |
| Root | `ia.container.flex`, no default size |
| Size | 2 components, 3 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2025-07-29T15:58:24Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `tags` | `[]` | inout |

## Component Tree

Component types: ia.container.flex x1, ia.display.table x1.

```text
root  ia.container.flex  [2 bindings]
  Table  ia.display.table  [1 binding; 1 event]
```

## Bindings

3 bindings: expr-struct 2, property 1.

**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

**`root/Table`**

- `props.data`: property `view.params.tags` (bidirectional)

## Event Scripts And Handlers

- **`root/Table`** `component.onEditCellCommit`, script action, scope `G`

```python
self.props.data[event.row][event.column] = event.value
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [98\_Configuration/Tools/L5K/Parser](./parser.md)
