---
title: "AhuEvapStatusBar"
sidebar_label: "AhuEvapStatusBar"
description: "Perspective view 00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar (Page piece (not routed)): 5 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar", "AhuEvapStatusBar"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar`.

| | |
|---|---|
| View path | `00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; \_Shared &gt; CG &gt; AhuEvapStatusBar |
| Root | `ia.container.flex`, height 28, width 440 |
| Size | 5 components, 6 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-01T04:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | |
| `title` | `""` | |
| `color` | `"#1E88E5"` | |
| `pct` | `50` | |
| `hours` | `0` | |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x2.

```text
root  ia.container.flex  [2 bindings]
  Lbl  ia.display.label  [1 binding]
  Track  ia.container.flex
    Fill  ia.container.flex  [2 bindings]
  Hrs  ia.display.label  [1 binding]
```

## Bindings

6 bindings: expr 4, property 2.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Lbl`**

- `props.text`: property `view.params.label`

**`root/Track/Fill`**

- `position.basis`: expression

```js
string({view.params.pct}) + '%'
```


- `props.style.backgroundColor`: property `view.params.color`

**`root/Hrs`**

- `props.text`: expression

```js
numberFormat({view.params.hours}, '0.00') + 'h'
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `fs-11` | 1 | style class |
| `fs-12` | 1 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
