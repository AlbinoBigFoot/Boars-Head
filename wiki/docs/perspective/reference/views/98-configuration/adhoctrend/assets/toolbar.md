---
title: "ToolBar"
sidebar_label: "ToolBar"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/ToolBar (Asset (embedded piece)): 25 components, 17 bindings, 2 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/ToolBar", "ToolBar"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/ToolBar`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/ToolBar` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/ToolBar/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; ToolBar |
| Root | `ia.container.flex`, height 320, width 300 |
| Size | 25 components, 17 bindings, 1 event handlers, 1 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:35:03Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `faceplateShell` | `false` | input |

## Component Tree

Component types: ia.container.flex x9, ia.display.label x8, ia.input.dropdown x5, ia.input.date-time-input x2, ia.input.button x1.

<details>
<summary>Component tree (25 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Label  ia.display.label  [1 binding]
  ChartMode  ia.container.flex
    Label  ia.display.label
    timeRange  ia.input.dropdown  [1 binding]
  ChartRealtimeRange  ia.container.flex  [1 binding]
    Label  ia.display.label
    timeRange  ia.input.dropdown  [1 binding]
  StartDate  ia.container.flex  [1 binding]
    Label  ia.display.label
    startDate  ia.input.date-time-input  [3 bindings]
  EndDate  ia.container.flex  [1 binding]
    Label  ia.display.label
    endDate  ia.input.date-time-input  [2 bindings]
  PointCount  ia.container.flex
    Label  ia.display.label
    pointCount  ia.input.dropdown  [1 binding]
  Aggregation  ia.container.flex
    Label  ia.display.label
    aggregation  ia.input.dropdown  [1 binding]
  ChartType  ia.container.flex
    Label  ia.display.label
    chartType  ia.input.dropdown  [1 binding]
  Buttons  ia.container.flex  [1 binding]
    CloseButton  ia.input.button  [1 event]
```

</details>

## Bindings

17 bindings: property 12, expr 3, expr-struct 2.

<details>
<summary>All 17 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Label`**

- `meta.visible`: property `view.params.faceplateShell`, then expression transform

Transform 1, expression:

```js
!coalesce({value}, false)
```


**`root/ChartMode/timeRange`**

- `props.value`: property `session.custom.AdhocTrend.realtime` (bidirectional)

**`root/ChartRealtimeRange`**

- `position.display`: property `session.custom.AdhocTrend.realtime`

**`root/ChartRealtimeRange/timeRange`**

- `props.value`: property `session.custom.AdhocTrend.timeRange` (bidirectional)

**`root/StartDate`**

- `position.display`: property `session.custom.AdhocTrend.realtime`, then expression transform

Transform 1, expression:

```js
!{value}
```


**`root/StartDate/startDate`**

- `props.maxDate`: expression

```js
now(30000)
```


- `props.minDate`: expression

```js
dateArithmetic(now(0),-6,"month")
```


- `props.value`: property `session.custom.AdhocTrend.startDate` (bidirectional)

**`root/EndDate`**

- `position.display`: property `session.custom.AdhocTrend.realtime`, then expression transform

Transform 1, expression:

```js
!{value}
```


**`root/EndDate/endDate`**

- `props.maxDate`: expression

```js
now(30000)
```


- `props.value`: property `session.custom.AdhocTrend.endDate` (bidirectional)

**`root/PointCount/pointCount`**

- `props.value`: property `session.custom.AdhocTrend.pointCount` (bidirectional)

**`root/Aggregation/aggregation`**

- `props.value`: property `session.custom.AdhocTrend.aggregate` (bidirectional)

**`root/ChartType/chartType`**

- `props.value`: property `session.custom.AdhocTrend.chartType` (bidirectional)

**`root/Buttons`**

- `meta.visible`: property `view.params.faceplateShell`, then expression transform

Transform 1, expression:

```js
!coalesce({value}, false)
```

</details>

## Event Scripts And Handlers

- **`root/Buttons/CloseButton`** `component.onActionPerformed`, script action, scope `G`

```python
from shared import Alerts
Alerts.closeAdhocTrendConfig()
```

- **`root/StartDate/startDate`** change script on `props.value`

```python
self.session.custom.AdhocTrend.startDate = currentValue.value
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [01\_Popups/00\_Faceplates/AdhocTrendConfig](../../../01-popups/00-faceplates/adhoctrendconfig.md)

**Opened or named by** (1): [98\_Configuration/AdhocTrend/Trend](../trend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Colors/Component` | 5 | no rule found |
| `Container/Card` | 5 | no rule found |
| `Fonts/Button` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `adhoc-trend-config-toolbar` | 1 | stylesheet |
| `bg-container` | 1 | stylesheet |
| `container-button` | 1 | style class |
| `container-card` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
