---
title: "NamePlot"
sidebar_label: "NamePlot"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/NamePlot (Asset (embedded piece)): 8 components, 3 bindings, 2 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/NamePlot", "NamePlot"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/NamePlot`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/NamePlot` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/NamePlot/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; NamePlot |
| Root | `ia.container.flex`, height 200, width 360 |
| Size | 8 components, 3 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-28T03:30:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `plotName` | `""` | |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x2, ia.input.button x2, ia.input.text-field x1.

```text
root  ia.container.flex  [2 bindings]
  Title  ia.display.label
  PlotName  ia.container.flex
    Label  ia.display.label
    TextField  ia.input.text-field  [1 binding]
  Buttons  ia.container.flex
    Cancel  ia.input.button  [1 event]
    Confirm  ia.input.button  [1 event]
```

## Bindings

3 bindings: expr-struct 2, property 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/PlotName/TextField`**

- `props.text`: property `view.custom.plotName` (bidirectional)

## Event Scripts And Handlers

- **`root/Buttons/Cancel`** `component.onActionPerformed`, script action, scope `G`

```python
shared.AdhocTrend.close_name_plot_popup()
```

- **`root/Buttons/Confirm`** `component.onActionPerformed`, script action, scope `G`

```python
from shared import Alerts

ok, msg, plots = shared.AdhocTrend.confirm_add_plot(
    self.session.custom.AdhocTrend,
    self.view.custom.plotName
)
if not ok:
    Alerts.showAlert(
        state="warning",
        title="Missing Name",
        message=msg,
        showCloseBtn=True,
        btnTextPrimary="OK",
        btnActionPrimary="closeAlert"
    )
    return
self.session.custom.AdhocTrend.plots = plots
shared.AdhocTrend.close_name_plot_popup()
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.AdhocTrend.confirm\_add\_plot](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

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
