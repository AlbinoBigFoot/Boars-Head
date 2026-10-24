---
title: "QuickHistory"
sidebar_label: "QuickHistory"
description: "Perspective view 01_Popups/TrendContext/QuickHistory (Popup / faceplate): 36 components, 41 bindings, 22 event scripts."
generated: true
keywords: ["01_Popups/TrendContext/QuickHistory", "QuickHistory"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/TrendContext/QuickHistory`.

| | |
|---|---|
| View path | `01_Popups/TrendContext/QuickHistory` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/TrendContext/QuickHistory/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; TrendContext &gt; QuickHistory |
| Root | `ia.container.flex`, width 780, height 520 |
| Size | 36 components, 41 bindings, 21 event handlers, 1 change scripts, 0 message handlers |
| Last saved | 2026-10-23T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `label` | `""` | input |
| `units` | `""` | input |
| `hours` | `8` | input |

## Custom properties

<details>
<summary>16 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `hours` | `8` | |
| `live` | `true` | change script |
| `pausedAt` | `null` | |
| `dragMode` | `"time"` | |
| `autoY` | `false` | |
| `zoomMin` | `null` | |
| `zoomMax` | `null` | |
| `zoomKind` | `null` | |
| `zoomHoldMin` | `null` | |
| `zoomHoldMax` | `null` | |
| `zoomResetAt` | `null` | |
| `key` | `[]` | bound (expr) |
| `realTimeDataset` | `null` | bound (tag-history) |
| `historicalDataset` | `null` | bound (tag-history) |
| `startDate` | `null` | bound (expr) |
| `dataset` | `null` | bound (expr) |

</details>

## Component Tree

Component types: ia.container.flex x12, ia.input.button x11, ia.display.label x8, ia.display.icon x2, kyvislabs.display.apexchart x2, ia.input.toggle-switch x1.

<details>
<summary>Component tree (36 components)</summary>

```text
root  ia.container.flex  [1 event]
  Header  ia.container.flex
    Icon  ia.display.icon
    Title  ia.display.label  [1 binding]
    Trend  ia.input.button  [1 binding; 1 event]
    OpenTrend  ia.input.button  [1 event]
    Close  ia.container.flex  [1 event]
      Icon  ia.display.icon
  Tools  ia.container.flex
    RangeLbl  ia.display.label
    Ranges  ia.container.flex
      H1  ia.input.button  [1 binding; 1 event]
      H8  ia.input.button  [1 binding; 1 event]
      H24  ia.input.button  [1 binding; 1 event]
      H168  ia.input.button  [1 binding; 1 event]
    Live  ia.input.button  [3 bindings; 1 event]
  ChartTools  ia.container.flex
    Row  ia.container.flex
      DragMode  ia.container.flex
        ModeZoomTime  ia.input.button  [1 binding; 1 event]
        ModeZoomArea  ia.input.button  [1 binding; 1 event]
        ModePan  ia.input.button  [1 binding; 1 event]
      Div1  ia.container.flex
      AutoScale  ia.container.flex  [1 event]
        Switch  ia.input.toggle-switch  [1 binding]
        Label  ia.display.label
        State  ia.display.label  [2 bindings]
      Div2  ia.container.flex
      ResetZoom  ia.input.button  [1 binding; 1 event]
      ZoomChip  ia.container.flex  [1 binding; 1 event]
        Range  ia.display.label  [1 binding]
        Dot  ia.display.label
        Reset  ia.display.label
    Hint  ia.display.label  [1 binding]
  Chart  kyvislabs.display.apexchart  [9 bindings; 3 events]
  ChartPan  kyvislabs.display.apexchart  [8 bindings; 3 events]
```

</details>

## Bindings

41 bindings: expr 31, property 7, tag-history 2, expr-struct 1.

<details>
<summary>All 41 bindings, grouped by component</summary>

**`(view)`**

- `custom.key`: expression

```js
asList(asMap('aggregate', 'Average', 'alias', 'pen', 'path', coalesce({view.params.tagPath}, '')))
```


- `custom.realTimeDataset`: tag history

```json
{
 "aggregate": "Average",
 "avoidScanClassValidation": true,
 "enableValueCache": true,
 "ignoreBadQuality": false,
 "preventInterpolation": false,
 "returnFormat": "Tall",
 "returnSize": {
  "numRows": "300",
  "type": "FIXED"
 },
 "tags": "{view.custom.key}",
 "valueFormat": "DATASET",
 "dateRange": {
  "mostRecent": "{view.custom.hours}",
  "mostRecentUnits": "HOUR"
 },
 "polling": {
  "enabled": true,
  "rate": "5"
 }
}
```


- `custom.historicalDataset`: tag history

```json
{
 "aggregate": "Average",
 "avoidScanClassValidation": true,
 "enableValueCache": true,
 "ignoreBadQuality": false,
 "preventInterpolation": false,
 "returnFormat": "Tall",
 "returnSize": {
  "numRows": "300",
  "type": "FIXED"
 },
 "tags": "{view.custom.key}",
 "valueFormat": "DATASET",
 "dateRange": {
  "startDate": "{view.custom.startDate}",
  "endDate": "{view.custom.pausedAt}"
 }
}
```


- `custom.startDate`: expression

```js
dateArithmetic(coalesce({view.custom.pausedAt}, now(0)), -coalesce({view.custom.hours}, 8), 'hour')
```


- `custom.dataset`: expression

```js
if(coalesce({view.custom.live}, true), {view.custom.realTimeDataset}, {view.custom.historicalDataset})
```


**`root/Header/Title`**

- `props.text`: expression

```js
'Quick History · ' + coalesce({view.params.label}, '')
```


**`root/Header/Trend`**

- `props.text`: expression

```js
if(indexOf(coalesce({session.custom.trend.key}, ''), '|' + {view.params.tagPath} + '|') >= 0, 'Remove From Trend', 'Add To Trend')
```


**`root/Tools/Ranges/H1`**

- `props.style.classes`: expression

```js
if({view.custom.hours} = 1, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/Tools/Ranges/H8`**

- `props.style.classes`: expression

```js
if({view.custom.hours} = 8, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/Tools/Ranges/H24`**

- `props.style.classes`: expression

```js
if({view.custom.hours} = 24, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/Tools/Ranges/H168`**

- `props.style.classes`: expression

```js
if({view.custom.hours} = 168, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/Tools/Live`**

- `props.text`: expression

```js
if({view.custom.live}, 'Live', 'Paused')
```


- `props.image.icon.path`: expression

```js
if({view.custom.live}, 'material/fiber_manual_record', 'material/pause')
```


- `props.style.classes`: expression

```js
if({view.custom.live}, 'trend-tool-btn trend-live-on', 'trend-tool-btn')
```


**`root/ChartTools/Row/DragMode/ModeZoomTime`**

- `props.style.classes`: expression

```js
if(if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'time', 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/ChartTools/Row/DragMode/ModeZoomArea`**

- `props.style.classes`: expression

```js
if(if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'area', 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/ChartTools/Row/DragMode/ModePan`**

- `props.style.classes`: expression

```js
if(if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'pan', 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/ChartTools/Row/AutoScale/Switch`**

- `props.selected`: expression

```js
coalesce(try({view.custom.autoY}, false), false)
```


**`root/ChartTools/Row/AutoScale/State`**

- `props.text`: expression

```js
if(coalesce(try({view.custom.autoY}, false), false), 'On', 'Off')
```


- `props.style.classes`: expression

```js
if(coalesce(try({view.custom.autoY}, false), false), 'trend-switch-state trend-switch-state-on', 'trend-switch-state')
```


**`root/ChartTools/Row/ResetZoom`**

- `props.enabled`: expression

```js
!isNull(try({view.custom.zoomMin}, null)) && !isNull(try({view.custom.zoomMax}, null))
```


**`root/ChartTools/Row/ZoomChip`**

- `meta.visible`: expression

```js
!isNull(try({view.custom.zoomMin}, null)) && !isNull(try({view.custom.zoomMax}, null))
```


**`root/ChartTools/Row/ZoomChip/Range`**

- `props.text`: expression

```js
if(!isNull(try({view.custom.zoomMin}, null)) && !isNull(try({view.custom.zoomMax}, null)), 'Zoomed: ' + dateFormat(fromMillis(try({view.custom.zoomMin}, null)), if(try({view.custom.zoomMax}, null) - try({view.custom.zoomMin}, null) < 86400000, 'HH:mm', 'MMM d HH:mm')) + ' - ' + dateFormat(fromMillis(try({view.custom.zoomMax}, null)), if(try({view.custom.zoomMax}, null) - try({view.custom.zoomMin}, null) < 86400000, 'HH:mm', 'MMM d HH:mm')), '')
```


**`root/ChartTools/Hint`**

- `props.text`: expression

```js
case(if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')), 'area', 'Drag a box on a chart to zoom into that time and value range', 'pan', 'Drag a chart left or right to move through time', 'Drag across a chart to zoom into that time range') + ' · Scroll to zoom · Double-click to reset'
```


**`root/Chart`**

- `props.series`: structured expression (expr-struct), then script transform

```js
dataset: {view.custom.dataset}
label: {view.params.label}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.TrendContext.quick_series(value.dataset, value.label)
```


- `props.options.tooltip.theme`: property `session.props.theme`

- `props.options.chart.zoom.type`: expression

```js
if(if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'area', 'xy', 'x')
```


- `props.options.chart.zoom.autoScaleYaxis`: expression

```js
coalesce({view.custom.autoY}, false)
```


- `props.options.yaxis.title.text`: property `view.params.units`

- `props.options.xaxis.min`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMin}, coalesce({view.custom.zoomMin}, if(coalesce({view.custom.live}, true), toMillis(addHours(now(5000), -coalesce({view.custom.hours}, 8))), toMillis({view.custom.startDate}))))
```


- `props.options.xaxis.max`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMax}, coalesce({view.custom.zoomMax}, if(coalesce({view.custom.live}, true), toMillis(now(5000)), toMillis(coalesce({view.custom.pausedAt}, now(0))))))
```


- `props.options.chart.toolbar.tools.download`: property `this.props.series`, then script transform

Transform 1, script:

```python
# trend-context: download (export) only with at least one good point (quality rule, docs/trending.md)
try:
    for s in value or []:
        for p in (s['data'] or []):
            try:
                y = p['y']
            except:
                y = p[1]
            if y is not None:
                return True
except:
    pass
return False
```


- `position.display`: expression

```js
(true) && if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) != 'pan'
```


**`root/ChartPan`**

- `props.series`: property `../Chart.props.series`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `props.options.tooltip.theme`: property `session.props.theme`

- `props.options.chart.zoom.autoScaleYaxis`: expression

```js
coalesce({view.custom.autoY}, false)
```


- `props.options.yaxis.title.text`: property `view.params.units`

- `props.options.xaxis.min`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMin}, coalesce({view.custom.zoomMin}, if(coalesce({view.custom.live}, true), toMillis(addHours(now(5000), -coalesce({view.custom.hours}, 8))), toMillis({view.custom.startDate}))))
```


- `props.options.xaxis.max`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMax}, coalesce({view.custom.zoomMax}, if(coalesce({view.custom.live}, true), toMillis(now(5000)), toMillis(coalesce({view.custom.pausedAt}, now(0))))))
```


- `props.options.chart.toolbar.tools.download`: property `this.props.series`, then script transform

Transform 1, script:

```python
# trend-context: download (export) only with at least one good point (quality rule, docs/trending.md)
try:
    for s in value or []:
        for p in (s['data'] or []):
            try:
                y = p['y']
            except:
                y = p[1]
            if y is not None:
                return True
except:
    pass
return False
```


- `position.display`: expression

```js
(true) && if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'pan'
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 22 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
try:
    h = int(self.view.params.hours or 8)
except:
    h = 8
self.view.custom.hours = h
```

- **`root/Header/Trend`** `component.onActionPerformed`, script action, scope `G`

```python
ok, msg = shared.TrendContext.toggle(self.session, self.view.params.tagPath, self.view.params.label)
shared.TrendContext.toast(msg, 'ok' if ok else 'warn')
```

- **`root/Header/OpenTrend`** `component.onActionPerformed`, script action, scope `G`

```python
shared.TrendContext.open_trend()
```

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
system.perspective.closePopup('TrendQuickHistory')
```

- **`root/Tools/Ranges/H1`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.hours = 1
self.view.custom.live = True
self.view.custom.zoomMin = None
self.view.custom.zoomMax = None
```

- **`root/Tools/Ranges/H8`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.hours = 8
self.view.custom.live = True
self.view.custom.zoomMin = None
self.view.custom.zoomMax = None
```

- **`root/Tools/Ranges/H24`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.hours = 24
self.view.custom.live = True
self.view.custom.zoomMin = None
self.view.custom.zoomMax = None
```

- **`root/Tools/Ranges/H168`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.hours = 168
self.view.custom.live = True
self.view.custom.zoomMin = None
self.view.custom.zoomMax = None
```

- **`root/Tools/Live`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.live:
    self.view.custom.pausedAt = system.date.now()
else:
    self.view.custom.zoomMin = None
    self.view.custom.zoomMax = None
self.view.custom.live = not self.view.custom.live
```

- **`root/ChartTools/Row/DragMode/ModeZoomTime`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.dragMode = 'time'
self.view.custom.zoomKind = 'time'
if 'time' == 'area' and self.view.custom.live:
    self.view.custom.pausedAt = system.date.now()
    self.view.custom.live = False
```

- **`root/ChartTools/Row/DragMode/ModeZoomArea`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.dragMode = 'area'
self.view.custom.zoomKind = 'time'
if 'area' == 'area' and self.view.custom.live:
    self.view.custom.pausedAt = system.date.now()
    self.view.custom.live = False
```

- **`root/ChartTools/Row/DragMode/ModePan`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.dragMode = 'pan'
self.view.custom.zoomKind = 'time'
if 'pan' == 'area' and self.view.custom.live:
    self.view.custom.pausedAt = system.date.now()
    self.view.custom.live = False
```

- **`root/ChartTools/Row/AutoScale`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.autoY = not bool(self.view.custom.autoY)
```

- **`root/ChartTools/Row/ResetZoom`** `component.onActionPerformed`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['Chart', 'ChartPan'])
```

- **`root/ChartTools/Row/ZoomChip`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['Chart', 'ChartPan'])
```

- **`root/Chart`** `component.zoomedHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, True, self)
```

- **`root/Chart`** `component.scrolledHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, True, self)
```

- **`root/Chart`** `dom.onDoubleClick`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['Chart', 'ChartPan'])
```

- **`root/ChartPan`** `component.zoomedHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, True, self)
```

- **`root/ChartPan`** `component.scrolledHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, True, self)
```

- **`root/ChartPan`** `dom.onDoubleClick`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['Chart', 'ChartPan'])
```

- **`(view)`** change script on `custom.live`

```python
if currentValue is not None and currentValue.value and previousValue is not None:
    shared.TrendContext.chart_reset(self, ['Chart', 'ChartPan'])
```

</details>

Project script calls: [shared.TrendContext.chart\_reset](../../../../../scripting/reference/modules/shared-trendcontext.md), [shared.TrendContext.quick\_series](../../../../../scripting/reference/modules/shared-trendcontext.md), [shared.TrendContext.toggle](../../../../../scripting/reference/modules/shared-trendcontext.md).

## Related Views

**Named in project scripts**: [shared.TrendContext](../../../../../scripting/reference/modules/shared-trendcontext.md)

## Style Classes

<details>
<summary>26 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 4 | style class |
| `adhoc-trend-apex` | 2 | stylesheet |
| `faceplate-cmd-btn` | 2 | style class |
| `trend-chart` | 2 | stylesheet |
| `trend-ctx-close-btn` | 1 | stylesheet |
| `trend-ctx-icon` | 2 | stylesheet |
| `trend-ctx-menu` | 1 | stylesheet |
| `trend-ctx-path` | 1 | stylesheet |
| `trend-ctx-quick` | 1 | stylesheet |
| `trend-ctx-title` | 1 | stylesheet |
| `trend-divider` | 2 | stylesheet |
| `trend-hint` | 1 | stylesheet |
| `trend-seg` | 7 | stylesheet |
| `trend-seg-group` | 2 | stylesheet |
| `trend-switch` | 1 | stylesheet |
| `trend-switch-box` | 1 | stylesheet |
| `trend-switch-label` | 1 | stylesheet |
| `trend-switch-state` | 1 | stylesheet |
| `trend-tool-btn` | 2 | stylesheet |
| `trend-tools` | 1 | stylesheet |
| `trend-tools-compact` | 1 | stylesheet |
| `trend-tools-row` | 1 | stylesheet |
| `trend-zoom-chip` | 1 | stylesheet |
| `trend-zoom-chip-link` | 1 | stylesheet |
| `trend-zoom-chip-text` | 2 | stylesheet |
| `trend-seg-on` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
