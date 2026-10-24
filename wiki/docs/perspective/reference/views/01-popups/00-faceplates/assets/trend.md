---
title: "Trend"
sidebar_label: "Trend"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Trend (Asset (embedded piece)): 25 components, 39 bindings, 15 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Trend", "Trend"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Trend`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Trend` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Trend/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Trend |
| Root | `ia.container.flex`, height 420, width 860 |
| Size | 25 components, 39 bindings, 12 event handlers, 3 change scripts, 1 message handlers |
| Last saved | 2026-07-30T18:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `hiddenTags` | `""` | input |
| `tagPath` | `""` | input |

## Custom properties

<details>
<summary>15 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `chartDataAnalog` | `null` | bound (expr-struct) |
| `hours` | `1` | change script |
| `penOptions` | `[]` | bound (expr-struct) |
| `selectedPens` | `null` | |
| `defaultPens` | `[]` | bound (expr-struct), change script |
| `ain` | `0` | bound (expr) |
| `pax` | `""` | bound (expr) |
| `dragMode` | `"time"` | |
| `autoY` | `true` | |
| `zoomMin` | `null` | |
| `zoomMax` | `null` | |
| `zoomResetAt` | `null` | |
| `zoomKind` | `null` | |
| `zoomHoldMin` | `null` | |
| `zoomHoldMax` | `null` | |

</details>

## Component Tree

Component types: ia.container.flex x9, ia.display.label x7, ia.input.button x4, ia.input.dropdown x2, kyvislabs.display.apexchart x2, ia.input.toggle-switch x1.

<details>
<summary>Component tree (25 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Toolbar  ia.container.flex
    Pens  ia.input.dropdown  [2 bindings]
    Hours  ia.input.dropdown  [1 binding]
  ChartTools  ia.container.flex  [1 binding]
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
  EmptyHint  ia.display.label  [1 binding]
  AnalogChart  kyvislabs.display.apexchart  [9 bindings; 3 events]
  AnalogChartPan  kyvislabs.display.apexchart  [8 bindings; 3 events]
```

</details>

## Bindings

39 bindings: expr 28, expr-struct 6, property 5.

<details>
<summary>All 39 bindings, grouped by component</summary>

**`(view)`**

- `custom.chartDataAnalog`: structured expression (expr-struct), then script transform

```js
hours: {view.custom.hours}
selectedPens: {view.custom.selectedPens}
tick: if(coalesce({view.custom.hours}, 1) <= 24 && coalesce({view.custom.dragMode}, 'time') != 'area', now(15000), 0)
```

waitOnAll: `True`

Transform 1, script:

```python
result = None
selected = value.get('selectedPens') if hasattr(value, 'get') else None
hours = value.get('hours') if hasattr(value, 'get') else 1
if selected is None:
    return result
if isinstance(selected, (str, unicode)):
    selected = [selected] if selected else []
try:
    hours = int(hours) if hours is not None else 1
except:
    hours = 1
if hours <= 0:
    hours = 1

paths = []
aliases = []
seen = set()
for item in selected:
    path = str(item or '').strip()
    if not path or path in seen:
        continue
    seen.add(path)
    paths.append(path)
    leaf = path.rsplit('/', 1)[-1]
    parts = path.split('/')
    if len(parts) >= 3 and leaf.upper() == 'VALUE' and parts[-2].upper() == 'VALUE':
        alias = parts[-3]
    elif len(parts) >= 2 and leaf.upper() == 'VALUE':
        alias = parts[-2]
    else:
        alias = (parts[-2] + ' ' + leaf) if len(parts) >= 2 else leaf  # pax-bindings: PAX member
    aliases.append(alias)

if not paths:
    return result

end = system.date.now()
start = system.date.addHours(end, -hours)
try:
    result = system.tag.queryTagHistory(
# ... 11 more line(s): see the view.json
```


- `custom.penOptions`: structured expression (expr-struct), then script transform

```js
hiddenTags: {view.params.hiddenTags}
tagPath: {view.params.tagPath}
defaultPens: {view.custom.defaultPens}
```

waitOnAll: `True`

Transform 1, script:

```python
result = []
tag_path = value.get('tagPath', '') if hasattr(value, 'get') else ''
hiddenTagsInput = value.get('hiddenTags', '') if hasattr(value, 'get') else ''
if tag_path:
    tag_path = str(tag_path).rstrip('/')
if not tag_path:
    return result

hidden_set = set()
try:
    text = str(hiddenTagsInput or '')
    if text:
        text = text.replace(';', ',')
        for item in text.split(','):
            item = item.strip()
            if item:
                hidden_set.add(item)
except Exception:
    pass

def isHidden(fullPath):
    if not hidden_set:
        return False
    stripped = fullPath.split(']', 1)[-1] if ']' in fullPath else fullPath
    norm = stripped.replace(chr(92), '/')
    if fullPath in hidden_set or stripped in hidden_set or norm in hidden_set:
        return True
    norm_slash = '/' + norm.strip('/') + '/'
    for h in hidden_set:
        hh = str(h).replace(chr(92), '/')
        if hh.endswith('/'):
            seg = hh.strip('/')
            if not seg:
                continue
            if ('/' + seg + '/') in norm_slash:
                return True
            if norm.strip('/') == seg or norm.strip('/').startswith(seg + '/'):
                return True
        else:
            if norm.endswith('/' + hh) or norm.split('/')[-1] == hh:
# ... 126 more line(s): see the view.json
```


- `custom.defaultPens`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.FaceplateTrend.defaultPens(value.get('tagPath'))
```


- `custom.ain`: expression

```js
if(try(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), false),
	if(len(where(coalesce({view.custom.selectedPens}, asList()), replace(toStr(it()), '[default]', '') = replace(toStr({view.params.tagPath} + '/AIn/Val'), '[default]', ''))) = 0, 0,
		if(len(coalesce({view.custom.selectedPens}, asList())) = 1, 2, 1)),
	0)
```


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
tagPath: 
```

waitOnAll: `True`

Transform 1, script:

```python
tagPath = ''
try:
    tagPath = self.view.params.tagPath
except:
    pass
if tagPath is None or str(tagPath).strip() == '':
    tagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]
items = [
          {
            "text": "Ticket Logger",
            "icon": {
              "path": "material/info",
              "color": "--neutral-80",
              "style": {}
            },
            "style": {
              "classes": "bg-component Fonts/Value",
              "height": 24,
              "width": 120
            },
            "type": "message",
            "children": [],
            "link": {
              "url": "",
              "target": "self"
            },
            "method": {
              "name": "",
              "params": {}
            },
            "message": {
              "type": "ticketLog",
              "payload": {
                "tagPath": tagPath,
                "viewName": self.view.id.split('@')[0], 'sender': self.view.id
              },
              "scope": "page"
            }
          }
        ]
# ... 1 more line(s): see the view.json
```


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Toolbar/Pens`**

- `props.options`: property `view.custom.penOptions`

- `props.value`: expression

```js
if(try(len({view.custom.selectedPens}), 0) > 0, {view.custom.selectedPens}, null)
```


**`root/Toolbar/Hours`**

- `props.value`: property `view.custom.hours` (bidirectional)

**`root/ChartTools`**

- `position.display`: expression

```js
try(len({view.custom.selectedPens}), 0) > 0
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


**`root/EmptyHint`**

- `position.display`: expression

```js
try(len({view.custom.selectedPens}), 0) = 0
```


**`root/AnalogChart`**

- `position.display`: expression

```js
(try(len({view.custom.selectedPens}), 0) > 0) && if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) != 'pan'
```


- `props.series`: structured expression (expr-struct), then script transform

```js
chartData: {view.custom.chartDataAnalog}
selectedPens: {view.custom.selectedPens}
penOptions: {view.custom.penOptions}
```

waitOnAll: `True`

Transform 1, script:

```python
selected = value.get('selectedPens') or []
data = value.get('chartData')
labels = {}
for opt in value.get('penOptions') or []:
    try:
        labels[str(opt['value'])] = str(opt['label'])
    except:
        pass
series = []
if data is None:
    return series
try:
    row_count = data.getRowCount()
except:
    row_count = 0
if row_count <= 0:
    return series
try:
    col_names = shared.TrendContext.columns(data)
except:
    try:
        col_names = [data.getColumnName(i) for i in range(data.getColumnCount())]
    except:
        return series

def add_series(name, column):
    if column not in col_names or column == 't_stamp':
        return
    try:
        filtered = shared.TrendContext.points(data, column)
    except:
        return
    series.append({'name': name or column, 'data': filtered})

used = set()
if isinstance(selected, (str, unicode)):
    selected = [selected] if selected else []
for item in selected or []:
    path = str(item or '')
    leaf = path.rsplit('/', 1)[-1]
# ... 25 more line(s): see the view.json
```


- `props.options.annotations`: expression

```js
asMap('yaxis', if({view.custom.ain} > 0,
	where(asList(asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_HiHiLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_HiHiLim')), null), null), 'borderColor', '#E53935', 'strokeDashArray', 0, 'label', asMap('text', 'HH', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#E53935', 'background', 'transparent', 'fontSize', '11px'))),
		asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_HiLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_HiLim')), null), null), 'borderColor', '#F9A825', 'strokeDashArray', 0, 'label', asMap('text', 'H', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#F9A825', 'background', 'transparent', 'fontSize', '11px'))),
		asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_LoLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_LoLim')), null), null), 'borderColor', '#F9A825', 'strokeDashArray', 0, 'label', asMap('text', 'L', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#F9A825', 'background', 'transparent', 'fontSize', '11px'))),
		asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_LoLoLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_LoLoLim')), null), null), 'borderColor', '#E53935', 'strokeDashArray', 0, 'label', asMap('text', 'LL', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#E53935', 'background', 'transparent', 'fontSize', '11px')))),
		!isNull(it()['y'])),
	asList()))
```


- `props.options.yaxis`: expression

```js
if({view.custom.ain} = 2,
	asList(asMap('decimalsInFloat', 2, 'opposite', false, 'title', asMap('text', '', 'style', asMap('fontFamily', 'Poppins', 'fontWeight', 400)), 'tickAmount', 4,
		'min', coalesce(try(if(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), null), null), 0), 'max', coalesce(try(if(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), null), null), 100))),
	asList(asMap('decimalsInFloat', 1, 'opposite', false, 'title', asMap('text', '', 'style', asMap('fontFamily', 'Poppins', 'fontWeight', 400)))))
```


- `props.options.chart.zoom.type`: expression

```js
if(if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'area', 'xy', 'x')
```


- `props.options.chart.zoom.autoScaleYaxis`: expression

```js
coalesce({view.custom.autoY}, true)
```


- `props.options.xaxis.min`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMin}, coalesce({view.custom.zoomMin}, toMillis(addHours(now(15000), -coalesce({view.custom.hours}, 1)))))
```


- `props.options.xaxis.max`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMax}, coalesce({view.custom.zoomMax}, toMillis(now(15000))))
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


**`root/AnalogChartPan`**

- `position.display`: expression

```js
(try(len({view.custom.selectedPens}), 0) > 0) && if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({view.custom.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'pan'
```


- `props.series`: property `../AnalogChart.props.series`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `props.options.annotations`: expression

```js
asMap('yaxis', if({view.custom.ain} > 0,
	where(asList(asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_HiHiLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_HiHiLim')), null), null), 'borderColor', '#E53935', 'strokeDashArray', 0, 'label', asMap('text', 'HH', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#E53935', 'background', 'transparent', 'fontSize', '11px'))),
		asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_HiLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_HiLim')), null), null), 'borderColor', '#F9A825', 'strokeDashArray', 0, 'label', asMap('text', 'H', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#F9A825', 'background', 'transparent', 'fontSize', '11px'))),
		asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_LoLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_LoLim')), null), null), 'borderColor', '#F9A825', 'strokeDashArray', 0, 'label', asMap('text', 'L', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#F9A825', 'background', 'transparent', 'fontSize', '11px'))),
		asMap('y', try(if(isGood(tag({view.params.tagPath} + '/AIn/Val_LoLoLim')), toFloat(tag({view.params.tagPath} + '/AIn/Val_LoLoLim')), null), null), 'borderColor', '#E53935', 'strokeDashArray', 0, 'label', asMap('text', 'LL', 'borderWidth', 0, 'position', 'left', 'textAnchor', 'start', 'offsetX', 4, 'style', asMap('color', '#E53935', 'background', 'transparent', 'fontSize', '11px')))),
		!isNull(it()['y'])),
	asList()))
```


- `props.options.yaxis`: expression

```js
if({view.custom.ain} = 2,
	asList(asMap('decimalsInFloat', 2, 'opposite', false, 'title', asMap('text', '', 'style', asMap('fontFamily', 'Poppins', 'fontWeight', 400)), 'tickAmount', 4,
		'min', coalesce(try(if(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), null), null), 0), 'max', coalesce(try(if(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), null), null), 100))),
	asList(asMap('decimalsInFloat', 1, 'opposite', false, 'title', asMap('text', '', 'style', asMap('fontFamily', 'Poppins', 'fontWeight', 400)))))
```


- `props.options.chart.zoom.autoScaleYaxis`: expression

```js
coalesce({view.custom.autoY}, true)
```


- `props.options.xaxis.min`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMin}, coalesce({view.custom.zoomMin}, toMillis(addHours(now(15000), -coalesce({view.custom.hours}, 1)))))
```


- `props.options.xaxis.max`: expression

```js
if(coalesce({view.custom.zoomKind}, '') = 'area', {view.custom.zoomHoldMax}, coalesce({view.custom.zoomMax}, toMillis(now(15000))))
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

<details>
<summary>All 16 event actions, change scripts and handlers</summary>

- **`root/ChartTools/Row/DragMode/ModeZoomTime`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.dragMode = 'time'
self.view.custom.zoomKind = 'time'
```

- **`root/ChartTools/Row/DragMode/ModeZoomArea`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.dragMode = 'area'
self.view.custom.zoomKind = 'time'
```

- **`root/ChartTools/Row/DragMode/ModePan`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.dragMode = 'pan'
self.view.custom.zoomKind = 'time'
```

- **`root/ChartTools/Row/AutoScale`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.autoY = not bool(self.view.custom.autoY)
```

- **`root/ChartTools/Row/ResetZoom`** `component.onActionPerformed`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['AnalogChart', 'AnalogChartPan'])
```

- **`root/ChartTools/Row/ZoomChip`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['AnalogChart', 'AnalogChartPan'])
```

- **`root/AnalogChart`** `component.zoomedHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, False, self)
```

- **`root/AnalogChart`** `component.scrolledHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, False, self)
```

- **`root/AnalogChart`** `dom.onDoubleClick`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['AnalogChart', 'AnalogChartPan'])
```

- **`root/AnalogChartPan`** `component.zoomedHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, False, self)
```

- **`root/AnalogChartPan`** `component.scrolledHandler`, script action, scope `G`

```python
shared.TrendContext.chart_zoomed(self.view, event, False, self)
```

- **`root/AnalogChartPan`** `dom.onDoubleClick`, script action, scope `G`

```python
shared.TrendContext.chart_reset(self.view, ['AnalogChart', 'AnalogChartPan'])
```

- **`(view)`** change script on `custom.hours`

```python
self.custom.zoomMin = None
self.custom.zoomMax = None
```

- **`(view)`** change script on `custom.defaultPens`

```python
pens = currentValue.value if currentValue is not None else None
if not pens:
    return
cur = self.custom.selectedPens
try:
    empty = cur is None or len(cur) == 0
except:
    empty = True
if empty:
    self.custom.selectedPens = [str(getattr(p, 'value', p)) for p in pens]
```

- **`root/Toolbar/Pens`** change script on `props.value`

```python
if str(origin) != 'Browser':
    return
v = currentValue.value if currentValue is not None else None
if v is None:
    self.view.custom.selectedPens = None
    return
try:
    n = len(v)
except:
    n = 0
self.view.custom.selectedPens = None if n == 0 else v
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.FaceplateTrend.defaultPens](../../../../../../scripting/reference/modules/shared-faceplatetrend.md), [shared.Pax.part](../../../../../../scripting/reference/modules/shared-pax.md), [shared.TrendContext.columns](../../../../../../scripting/reference/modules/shared-trendcontext.md), [shared.TrendContext.points](../../../../../../scripting/reference/modules/shared-trendcontext.md).

## Related Views

**Opened or named by** (2): [01\_Popups/00\_Faceplates/Faceplate](../faceplate.md), [01\_Popups/00\_Faceplates/TankOverview](../tankoverview.md)

## Style Classes

<details>
<summary>20 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `faceplate-trend-chart` | 2 | stylesheet |
| `faceplate-trend-empty` | 1 | stylesheet |
| `trend-chart` | 2 | stylesheet |
| `trend-divider` | 2 | stylesheet |
| `trend-hint` | 1 | stylesheet |
| `trend-seg` | 3 | stylesheet |
| `trend-seg-group` | 1 | stylesheet |
| `trend-switch` | 1 | stylesheet |
| `trend-switch-box` | 1 | stylesheet |
| `trend-switch-label` | 1 | stylesheet |
| `trend-switch-state` | 1 | stylesheet |
| `trend-tool-btn` | 1 | stylesheet |
| `trend-tools` | 1 | stylesheet |
| `trend-tools-compact` | 1 | stylesheet |
| `trend-tools-row` | 1 | stylesheet |
| `trend-zoom-chip` | 1 | stylesheet |
| `trend-zoom-chip-link` | 1 | stylesheet |
| `trend-zoom-chip-text` | 2 | stylesheet |
| `trend-seg-on` | bound | stylesheet |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>15 relative member paths</summary>

`.DataType`, `.Enabled`, `.HistoryEnabled`, `.TypeId`, `.metadata`, `/AIn.Enabled`, `/AIn/Cfg_PVEUMax`, `/AIn/Cfg_PVEUMin`, `/AIn/Val`, `/AIn/Val_HiHiLim`, `/AIn/Val_HiLim`, `/AIn/Val_LoLim`, `/AIn/Val_LoLoLim`, `/AInRef.Enabled`, `/DIn.Enabled`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
