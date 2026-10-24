---
title: "Interlocks"
sidebar_label: "Interlocks"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks (Asset (embedded piece)): 2 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks", "Interlocks"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Evaporator &gt; Interlocks |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 2 components, 3 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-25T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Panel  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/InterlockPanel]
```

## Bindings

3 bindings: expr 3.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Panel`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/Interlock')
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](../interlockpanel.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/Interlock`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
