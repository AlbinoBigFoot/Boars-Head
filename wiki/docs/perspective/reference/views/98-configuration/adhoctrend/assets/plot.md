---
title: "Plot"
sidebar_label: "Plot"
description: "Perspective view 98_Configuration/AdhocTrend/_Assets/Plot (Asset (embedded piece)): 6 components, 44 bindings, 8 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/_Assets/Plot", "Plot"]
---

:::note

:::


**Asset (embedded piece)**: `98_Configuration/AdhocTrend/_Assets/Plot`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/_Assets/Plot` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; \_Assets &gt; Plot |
| Root | `ia.container.flex`, height 2000, width 800 |
| Size | 6 components, 44 bindings, 7 event handlers, 1 change scripts, 2 message handlers |
| Last saved | 2026-07-28T03:10:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `chartHeight` | `400` | input |
| `layoutKey` | `"e"` | input |
| `plotCount` | `1` | input |
| `plotId` | `"p0"` | input |
| `plotKind` | `"analog"` | input |
| `plotTitle` | `"Default"` | input |
| `showToolbar` | `true` | input |
| `canRemove` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `aggregate` | `""` | bound (property) |
| `dataset` | `null` | bound (expr-struct) |
| `endDate` | `null` | bound (property) |
| `historicalDataset` | `null` | bound (tag-history) |
| `key` | `[]` | bound (expr-struct) |
| `pens` | `null` | bound (expr-struct) |
| `pointCount` | `120` | bound (property) |
| `realTime` | `true` | bound (property), change script |
| `realTimeDataset` | `null` | bound (tag-history) |
| `startDate` | `null` | bound (expr-struct) |
| `timeRange` | `1` | bound (property) |

## Component Tree

Component types: ia.container.flex x2, kyvislabs.display.apexchart x2, ia.display.label x1, ia.input.button x1.

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    Title  ia.display.label  [1 binding]
    RemovePlot  ia.input.button  [1 binding; 1 event]
  apexchart  kyvislabs.display.apexchart  [15 bindings; 3 events]
  apexchartPan  kyvislabs.display.apexchart  [14 bindings; 3 events]
```

## Bindings

44 bindings: property 20, expr 14, expr-struct 8, tag-history 2.

<details>
<summary>All 44 bindings, grouped by component</summary>

**`(view)`**

- `custom.aggregate`: property `session.custom.AdhocTrend.aggregate`

- `custom.pointCount`: property `session.custom.AdhocTrend.pointCount`

- `custom.realTime`: property `session.custom.AdhocTrend.realtime`

- `custom.timeRange`: property `session.custom.AdhocTrend.timeRange`

- `custom.startDate`: structured expression (expr-struct), then expression transform

```js
realTime: {view.custom.realTime}
startDate: {session.custom.AdhocTrend.startDate}
```

waitOnAll: `True`

Transform 1, expression:

```js
{value}['startDate']
```


- `custom.endDate`: property `session.custom.AdhocTrend.endDate`

- `custom.pens`: structured expression (expr-struct), then script transform

```js
cfg: {session.custom.AdhocTrend}
plotId: {view.params.plotId}
```

waitOnAll: `True`

Transform 1, script:

```python
if value is None:
    return shared.AdhocTrend.build_pens([], [])
cfg = getattr(value, "cfg", None)
plotId = getattr(value, "plotId", None)
if cfg is None:
    return shared.AdhocTrend.build_pens([], [])
tags = shared.AdhocTrend._cfg_get(cfg, "tags", [])
colors = shared.AdhocTrend._cfg_get(cfg, "colors", shared.AdhocTrend.DEFAULT_COLORS)
penPlots = shared.AdhocTrend.plain_pen_plots(cfg)
plots = shared.AdhocTrend.plain_plots(cfg)
disabled = shared.AdhocTrend.plain_disabled_pens(cfg)
firstId = plots[0]["id"] if plots else "p0"
pens = shared.AdhocTrend.build_pens(tags, colors, penPlots, plots, disabled)
return shared.AdhocTrend.pens_for_plot(pens, penPlots, plotId, firstId)
```


- `custom.key`: structured expression (expr-struct), then script transform

```js
aggregate: {view.custom.aggregate}
pens: {view.custom.pens}
```

waitOnAll: `True`

Transform 1, script:

```python
if value is None:
    return []
pens = getattr(value, "pens", None)
aggregate = getattr(value, "aggregate", "") or ""
return shared.AdhocTrend.build_key(pens, aggregate)
```


- `custom.realTimeDataset`: tag history

```json
{
 "aggregate": "Average",
 "avoidScanClassValidation": true,
 "dateRange": {
  "mostRecent": "{view.custom.timeRange}",
  "mostRecentUnits": "HOUR"
 },
 "enableValueCache": true,
 "ignoreBadQuality": false,
 "polling": {
  "enabled": true,
  "rate": "5"
 },
 "preventInterpolation": false,
 "returnFormat": "Tall",
 "returnSize": {
  "numRows": "{view.custom.pointCount}",
  "type": "FIXED"
 },
 "tags": "{view.custom.key}",
 "valueFormat": "DATASET"
}
```


- `custom.historicalDataset`: tag history

```json
{
 "aggregate": "Average",
 "avoidScanClassValidation": true,
 "dateRange": {
  "startDate": "{view.custom.startDate}",
  "endDate": "{view.custom.endDate}"
 },
 "enableValueCache": true,
 "ignoreBadQuality": false,
 "preventInterpolation": false,
 "returnFormat": "Tall",
 "returnSize": {
  "numRows": "{view.custom.pointCount}",
  "type": "FIXED"
 },
 "tags": "{view.custom.key}",
 "valueFormat": "DATASET"
}
```


- `custom.dataset`: structured expression (expr-struct), then expression transform

```js
historicalDataset: {view.custom.historicalDataset}
realTime: {view.custom.realTime}
realTimeDataset: {view.custom.realTimeDataset}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['realTime'],
	{value}['realTimeDataset'],
	{value}['historicalDataset']
)
```


**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Header/Title`**

- `props.text`: structured expression (expr-struct), then script transform

```js
title: {view.params.plotTitle}
pens: {view.custom.pens}
```

waitOnAll: `True`

Transform 1, script:

```python
try:
    n = value.pens.getRowCount()
except:
    n = 0
return u'%s \u00b7 %d Pen%s' % (value.title or 'Default', n, '' if n == 1 else 's')
```


**`root/Header/RemovePlot`**

- `meta.visible`: expression

```js
coalesce({view.params.canRemove}, false)
```


**`root/apexchart`**

- `props.series`: structured expression (expr-struct), then script transform

```js
dataset: {view.custom.dataset}
pens: {view.custom.pens}
```

waitOnAll: `True`

Transform 1, script:

```python
if value is None:
    return []
dataset = getattr(value, "dataset", None)
pens = getattr(value, "pens", None)
return shared.AdhocTrend.build_series(dataset, pens)
```


- `props.type`: property `session.custom.AdhocTrend.chartType`

- `props.options.tooltip.theme`: property `session.props.theme`

- `props.options.chart.id`: expression

```js
'adhoc-trend-' + coalesce({view.params.plotId}, 'p0')
```


- `props.options.stroke.curve`: property `view.params.plotKind`, then expression transform

Transform 1, expression:

```js
if({value} = 'discrete', 'stepline', 'straight')
```


- `props.options.chart.height`: property `view.params.chartHeight`, then script transform

Transform 1, script:

```python
try:
    h = int(value)
except:
    h = 400
if h < 120:
    h = 120
return h
```


- `props.style.height`: property `view.params.chartHeight`, then script transform

Transform 1, script:

```python
try:
    h = int(value)
except:
    h = 400
if h < 120:
    h = 120
return str(h) + 'px'
```


- `props.options.colors`: property `view.custom.pens`, then script transform

Transform 1, script:

```python
return shared.AdhocTrend.series_color_list(value)
```


- `props.options.chart.zoom.type`: expression

```js
if(if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'area', 'xy', 'x')
```


- `props.options.chart.zoom.autoScaleYaxis`: expression

```js
coalesce(try({session.custom.trendTools.autoScaleY}, false), false)
```


- `meta.visible`: expression

```js
{this.props.options.chart.id} = 'adhoc-trend-' + coalesce({view.params.plotId}, 'p0')
```


- `props.options.xaxis.min`: expression

```js
if(coalesce(try({session.custom.trendTools.zoomKind}, ''), '') = 'area' && coalesce(try({session.custom.trendTools.zoomSrc}, ''), '') = coalesce({view.params.plotId}, 'p0'), try({session.custom.trendTools.zoomHoldMin}, null), coalesce(try({session.custom.trendTools.zoomMin}, null), if(coalesce({view.custom.realTime}, false), toMillis(addHours(now(5000), -coalesce({view.custom.timeRange}, 1))), toMillis({view.custom.startDate}))))
```


- `props.options.xaxis.max`: expression

```js
if(coalesce(try({session.custom.trendTools.zoomKind}, ''), '') = 'area' && coalesce(try({session.custom.trendTools.zoomSrc}, ''), '') = coalesce({view.params.plotId}, 'p0'), try({session.custom.trendTools.zoomHoldMax}, null), coalesce(try({session.custom.trendTools.zoomMax}, null), if(coalesce({view.custom.realTime}, false), toMillis(now(5000)), toMillis({view.custom.endDate}))))
```


- `position.display`: expression

```js
(true) && if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) != 'pan'
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


**`root/apexchartPan`**

- `props.series`: property `../apexchart.props.series`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `props.type`: property `session.custom.AdhocTrend.chartType`

- `props.options.tooltip.theme`: property `session.props.theme`

- `props.options.chart.id`: expression

```js
'adhoc-trend-pan-' + coalesce({view.params.plotId}, 'p0')
```


- `props.options.stroke.curve`: property `view.params.plotKind`, then expression transform

Transform 1, expression:

```js
if({value} = 'discrete', 'stepline', 'straight')
```


- `props.options.chart.height`: property `view.params.chartHeight`, then script transform

Transform 1, script:

```python
try:
    h = int(value)
except:
    h = 400
if h < 120:
    h = 120
return h
```


- `props.style.height`: property `view.params.chartHeight`, then script transform

Transform 1, script:

```python
try:
    h = int(value)
except:
    h = 400
if h < 120:
    h = 120
return str(h) + 'px'
```


- `props.options.colors`: property `view.custom.pens`, then script transform

Transform 1, script:

```python
return shared.AdhocTrend.series_color_list(value)
```


- `props.options.chart.zoom.autoScaleYaxis`: expression

```js
coalesce(try({session.custom.trendTools.autoScaleY}, false), false)
```


- `meta.visible`: expression

```js
{this.props.options.chart.id} = 'adhoc-trend-pan-' + coalesce({view.params.plotId}, 'p0')
```


- `props.options.xaxis.min`: expression

```js
if(coalesce(try({session.custom.trendTools.zoomKind}, ''), '') = 'area' && coalesce(try({session.custom.trendTools.zoomSrc}, ''), '') = coalesce({view.params.plotId}, 'p0'), try({session.custom.trendTools.zoomHoldMin}, null), coalesce(try({session.custom.trendTools.zoomMin}, null), if(coalesce({view.custom.realTime}, false), toMillis(addHours(now(5000), -coalesce({view.custom.timeRange}, 1))), toMillis({view.custom.startDate}))))
```


- `props.options.xaxis.max`: expression

```js
if(coalesce(try({session.custom.trendTools.zoomKind}, ''), '') = 'area' && coalesce(try({session.custom.trendTools.zoomSrc}, ''), '') = coalesce({view.params.plotId}, 'p0'), try({session.custom.trendTools.zoomHoldMax}, null), coalesce(try({session.custom.trendTools.zoomMax}, null), if(coalesce({view.custom.realTime}, false), toMillis(now(5000)), toMillis({view.custom.endDate}))))
```


- `position.display`: expression

```js
(true) && if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'pan'
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

</details>

## Event Scripts And Handlers

- **`root/Header/RemovePlot`** `component.onActionPerformed`, script action, scope `G`

```python
cfg = self.session.custom.AdhocTrend
ok, msg, plots, penPlots = shared.AdhocTrend.remove_plot(cfg, self.view.params.plotId)
if ok:
    cfg.plots = plots
    cfg.penPlots = penPlots
```

- **`root/apexchart`** `component.zoomedHandler`, script action, scope `G`

```python
# trend-context: share the zoom / pan window with every plot (shared.AdhocTrend.zoom_event)
shared.AdhocTrend.zoom_event(self.session, self.view.params.plotId, event, self)
```

- **`root/apexchart`** `component.scrolledHandler`, script action, scope `G`

```python
# trend-context: share the zoom / pan window with every plot (shared.AdhocTrend.zoom_event)
shared.AdhocTrend.zoom_event(self.session, self.view.params.plotId, event, self)
```

- **`root/apexchart`** `dom.onDoubleClick`, script action, scope `G`

```python
shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/apexchartPan`** `component.zoomedHandler`, script action, scope `G`

```python
# trend-context: share the zoom / pan window with every plot (shared.AdhocTrend.zoom_event)
shared.AdhocTrend.zoom_event(self.session, self.view.params.plotId, event, self)
```

- **`root/apexchartPan`** `component.scrolledHandler`, script action, scope `G`

```python
# trend-context: share the zoom / pan window with every plot (shared.AdhocTrend.zoom_event)
shared.AdhocTrend.zoom_event(self.session, self.view.params.plotId, event, self)
```

- **`root/apexchartPan`** `dom.onDoubleClick`, script action, scope `G`

```python
shared.AdhocTrend.zoom_reset(self.session)
```

- **`(view)`** change script on `custom.realTime`

```python
if currentValue is not None and currentValue.value and previousValue is not None and not previousValue.value:
    for name in ('apexchart', 'apexchartPan'):
        try:
            self.rootContainer.getChild(name).resetSeries(True, True)
        except:
            pass
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

- **`root`** message handler `trendZoomReset` (scope: page)

```python
# trend-context: Reset Zoom / double-click on any plot -> every plot drops its own value (XY) zoom too
for name in ('apexchart', 'apexchartPan'):
    try:
        self.getChild(name).resetSeries(True, True)
    except:
        pass
```

Project script calls: [shared.AdhocTrend.DEFAULT\_COLORS](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.\_cfg\_get](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.build\_key](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.build\_pens](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.build\_series](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.pens\_for\_plot](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_disabled\_pens](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_pen\_plots](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_plots](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.remove\_plot](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.series\_color\_list](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.zoom\_event](../../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [98\_Configuration/AdhocTrend/Trend](../trend.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `adhoc-trend-apex` | 2 | stylesheet |
| `adhoc-trend-plot-header` | 1 | stylesheet |
| `adhoc-trend-plot-slot` | 1 | stylesheet |
| `adhoc-trend-plot-title` | 1 | style class |
| `trend-chart` | 2 | stylesheet |
| `trend-tool-btn` | 1 | stylesheet |
| `trend-tool-compact` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
