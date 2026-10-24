---
title: "PenPlot"
sidebar_label: "PenPlot"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/PenPlot (Asset (embedded piece)): 2 components, 4 bindings, 1 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/PenPlot", "PenPlot"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/PenPlot`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/PenPlot` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenPlot/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; PenPlot |
| Root | `ia.container.flex`, height 28, width 96 |
| Size | 2 components, 4 bindings, 0 event handlers, 1 change scripts, 1 message handlers |
| Last saved | 2026-07-28T03:10:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `row` | `0` | input |
| `rowData` | `{}` | input |

## Component Tree

Component types: ia.container.flex x1, ia.input.dropdown x1.

```text
root  ia.container.flex  [2 bindings]
  Plot  ia.input.dropdown  [2 bindings]
```

## Bindings

4 bindings: expr-struct 2, property 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Plot`**

- `props.options`: property `session.custom.AdhocTrend.plots`, then script transform

Transform 1, script:

```python
return shared.AdhocTrend.plot_dropdown_options(value)
```


- `props.value`: property `view.params.rowData.plotId`, then script transform

Transform 1, script:

```python
return str(value) if value not in (None, '') else 'p0'
```


## Event Scripts And Handlers

- **`root/Plot`** change script on `props.value`

```python
if currentValue.value in (None, ''):
    return
cfg = self.session.custom.AdhocTrend
row = self.view.params.rowData
key = None
try:
    key = row.tagPath
except:
    pass
if key in (None, ''):
    try:
        key = row.alias
    except:
        key = self.view.params.row
penPlots = shared.AdhocTrend.move_pen(cfg, key, currentValue.value)
self.session.custom.AdhocTrend.penPlots = penPlots
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.AdhocTrend.move\_pen](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plot\_dropdown\_options](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [98\_Configuration/AdhocTrend/Trend](../trend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `adhoc-trend-pen-plot-select` | 1 | stylesheet |
| `adhoc-trend-pen-plot-wrap` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
