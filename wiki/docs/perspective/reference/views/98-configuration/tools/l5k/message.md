---
title: "Message"
sidebar_label: "Message"
description: "Perspective view 98_Configuration/Tools/L5K/Message (Configuration / tool view): 3 components, 5 bindings, 0 event scripts."
generated: true
keywords: ["98_Configuration/Tools/L5K/Message", "Message"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/Tools/L5K/Message`.

| | |
|---|---|
| View path | `98_Configuration/Tools/L5K/Message` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/Tools/L5K/Message/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; Tools &gt; L5K &gt; Message |
| Root | `ia.container.coord`, height 166, width 314 |
| Size | 3 components, 5 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2025-07-29T15:10:31Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `error` | `true` | input |
| `message` | `"Test message"` | input |

## Component Tree

Component types: ia.container.coord x1, ia.display.label x1, ia.display.icon x1.

```text
root  ia.container.coord  [2 bindings]
  Label  ia.display.label  [2 bindings]
  Icon  ia.display.icon  [1 binding]
```

## Bindings

5 bindings: expr-struct 2, expr 2, property 1.

**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

**`root/Label`**

- `props.style.color`: expression

```js
if({view.params.error}, "#AC0000", "#008000")
```


- `props.text`: property `view.params.message`

**`root/Icon`**

- `props.path`: expression

```js
if({view.params.error}, "material/error", "material/message")
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [98\_Configuration/Tools/L5K/Parser](./parser.md)
