---
title: "Pen"
sidebar_label: "Pen"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/Pen (Asset (embedded piece)): 4 components, 7 bindings, 1 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/Pen", "Pen"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/Pen`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/Pen` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Pen/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; Pen |
| Root | `ia.container.flex`, height 24, width 200 |
| Size | 4 components, 7 bindings, 0 event handlers, 1 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:35:03Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `color` | `""` | input |
| `justify` | `"flex-start"` | input |
| `penName` | `""` | input |
| `plotId` | `"p0"` | input |
| `tagPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1, ia.display.label x1, ia.input.dropdown x1.

```text
root  ia.container.flex  [3 bindings]
  Icon  ia.display.icon  [1 binding]
  Label  ia.display.label  [1 binding]
  PlotSelect  ia.input.dropdown  [2 bindings]
```

## Bindings

7 bindings: property 5, expr-struct 2.

**`root`**

- `props.justify`: property `view.params.justify`

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Icon`**

- `props.color`: property `view.params.color`

**`root/Label`**

- `props.text`: property `view.params.penName`

**`root/PlotSelect`**

- `props.options`: property `session.custom.AdhocTrend.plots`, then script transform

Transform 1, script:

```python
return shared.AdhocTrend.plot_dropdown_options(value)
```


- `props.value`: property `view.params.plotId`, then script transform

Transform 1, script:

```python
return str(value) if value not in (None, '') else 'p0'
```


## Event Scripts And Handlers

- **`root/PlotSelect`** change script on `props.value`

```python
if currentValue.value in (None, ''):
    return
key = self.view.params.tagPath
if key in (None, ''):
    key = self.view.params.penName
penPlots = shared.AdhocTrend.move_pen(self.session.custom.AdhocTrend, key, currentValue.value)
self.session.custom.AdhocTrend.penPlots = penPlots
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.AdhocTrend.move\_pen](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plot\_dropdown\_options](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [98\_Configuration/AdhocTrend/Trend](../trend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `adhoc-trend-pen-plot-select` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
