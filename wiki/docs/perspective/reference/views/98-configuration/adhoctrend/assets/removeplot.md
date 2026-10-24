---
title: "RemovePlot"
sidebar_label: "RemovePlot"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/RemovePlot (Asset (embedded piece)): 8 components, 4 bindings, 2 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/RemovePlot", "RemovePlot"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/RemovePlot`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/RemovePlot` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/RemovePlot/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; RemovePlot |
| Root | `ia.container.flex`, height 220, width 360 |
| Size | 8 components, 4 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-28T04:40:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `plotId` | `""` | |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x2, ia.input.button x2, ia.input.dropdown x1.

```text
root  ia.container.flex  [2 bindings]
  Title  ia.display.label
  PlotSelect  ia.container.flex
    Label  ia.display.label
    Dropdown  ia.input.dropdown  [2 bindings]
  Buttons  ia.container.flex
    Cancel  ia.input.button  [1 event]
    Confirm  ia.input.button  [1 event]
```

## Bindings

4 bindings: expr-struct 2, property 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/PlotSelect/Dropdown`**

- `props.options`: property `session.custom.AdhocTrend.plots`, then script transform

Transform 1, script:

```python
return shared.AdhocTrend.remove_plot_dropdown_options(self.session.custom.AdhocTrend)
```


- `props.value`: property `view.custom.plotId` (bidirectional)

## Event Scripts And Handlers

- **`root/Buttons/Cancel`** `component.onActionPerformed`, script action, scope `G`

```python
shared.AdhocTrend.close_remove_plot_popup()
```

- **`root/Buttons/Confirm`** `component.onActionPerformed`, script action, scope `G`

```python
from shared import Alerts

ok, msg, plots, penPlots = shared.AdhocTrend.confirm_remove_plot(
    self.session.custom.AdhocTrend,
    self.view.custom.plotId
)
if not ok:
    Alerts.showAlert(
        state="warning",
        title="Cannot Remove Plot",
        message=msg,
        showCloseBtn=True,
        btnTextPrimary="OK",
        btnActionPrimary="closeAlert"
    )
    return
self.session.custom.AdhocTrend.plots = plots
self.session.custom.AdhocTrend.penPlots = penPlots
shared.AdhocTrend.close_remove_plot_popup()
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.AdhocTrend.confirm\_remove\_plot](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.remove\_plot\_dropdown\_options](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Named in project scripts**: [shared.AdhocTrend](../../../../../../scripting/reference/modules/shared-adhoctrend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 2 | style class |
| `Fonts/Value` | 1 | style class |
| `adhoc-trend-save-dialog` | 1 | stylesheet |
| `adhoc-trend-save-label` | 1 | stylesheet |
| `adhoc-trend-save-title` | 1 | stylesheet |
| `bg-component` | 1 | stylesheet |
| `container-button` | 2 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
