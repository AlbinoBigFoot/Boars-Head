---
title: "Trend"
sidebar_label: "Trend"
description: "Perspective view 98_Configuration/AdhocTrend/Trend (Page): 55 components, 81 bindings, 24 event scripts."
generated: true
keywords: ["98_Configuration/AdhocTrend/Trend", "Trend", "/trending"]
---

:::note

:::


**Page**: `98_Configuration/AdhocTrend/Trend`.

| | |
|---|---|
| View path | `98_Configuration/AdhocTrend/Trend` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/Trend/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; AdhocTrend &gt; Trend |
| Routes | `/trending` (Adhoc Trend) |
| Root | `ia.container.flex`, height 900, width 1600 |
| Size | 55 components, 81 bindings, 23 event handlers, 1 change scripts, 6 message handlers |
| Last saved | 2026-08-21T20:30:24Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `faceplateMode` | `false` | input |

## Custom properties

<details>
<summary>15 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `aggregate` | `"Average"` | bound (property) |
| `colors` | `["#008FFB", "#34C759", "#FFA726", "#FF4560", "#775DD0", "#1C4E80", ...` | bound (property) |
| `dbTrendConfig` | `{}` | bound (query) |
| `endDate` | `{"$": ["ts", 192, 1787344223974], "$ts": 1787344223974}` | bound (expr-struct) |
| `isConfigUpdated` | `false` | bound (expr-struct) |
| `pens` | `{"$": ["ds", 192, 1787344182090], "$columns": [{"data": [], "name":...` | bound (expr-struct) |
| `pointCount` | `120` | bound (property) |
| `realTime` | `true` | bound (property) |
| `startDate` | `{"$": ["ts", 192, 1787344223974], "$ts": 1787340623974}` | bound (expr-struct) |
| `tags` | `[]` | bound (property) |
| `timeRange` | `1` | bound (expr-struct) |
| `treeVisible` | `false` | |
| `trendId` | `""` | bound (property) |
| `trendName` | `""` | bound (property) |
| `username` | `""` | bound (property) |

</details>

## Component Tree

Component types: ia.container.flex x17, ia.input.button x17, ia.display.label x12, ia.display.icon x2, ia.display.flex-repeater x2, ia.display.tree x1, ia.input.toggle-switch x1, ia.input.checkbox x1, ia.display.table x1, ia.input.text-area x1.

<details>
<summary>Component tree (55 components)</summary>

```text
root  ia.container.flex  [4 bindings; 1 event]
  TagTree  ia.container.flex  [1 binding]
    Label  ia.display.label
    Tree  ia.display.tree  [1 binding; 1 event]
    AddToTrend  ia.input.button  [1 binding; 1 event]
  TrendContainer  ia.container.flex
    Trend  ia.container.flex  [4 bindings]
      TrendName  ia.display.label  [2 bindings]
      PlotToolbar  ia.container.flex
        Icons  ia.container.flex
          tagBrowser  ia.display.icon  [2 bindings; 1 event]
          trendConfig  ia.display.icon  [1 binding; 1 event]
          ChartType  ia.display.label  [2 bindings]
          TimeRange  ia.display.label  [2 bindings]
          StartDate  ia.display.label  [2 bindings]
          EndDate  ia.display.label  [2 bindings]
          Ranges  ia.container.flex  [1 binding]
            Range1H  ia.input.button  [1 binding; 1 event]
            Range8H  ia.input.button  [1 binding; 1 event]
            Range24H  ia.input.button  [1 binding; 1 event]
            Range7D  ia.input.button  [1 binding; 1 event]
          LivePause  ia.input.button  [4 bindings; 1 event]
        Buttons  ia.container.flex  [2 bindings]
          RemovePlot  ia.input.button  [1 binding; 1 event]
          AddPlot  ia.input.button  [1 binding; 1 event]
          SaveTrendConfig  ia.input.button  [2 bindings; 1 event]
          UpdateTrendConfig  ia.input.button  [2 bindings; 1 event]
          ClearPens  ia.input.button  [1 binding; 1 event]
      ChartTools  ia.container.flex  [1 binding]
        Row  ia.container.flex
          DragMode  ia.container.flex
            ModeZoomTime  ia.input.button  [1 binding; 1 event]
            ModeZoomArea  ia.input.button  [1 binding; 1 event]
            ModePan  ia.input.button  [1 binding; 1 event]
          ZoomIn  ia.input.button  [1 event]
          ZoomOut  ia.input.button  [1 event]
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
      Plots  ia.display.flex-repeater  [1 binding; view: 98_Configuration/AdhocTrend/_Assets/Plot]
    Pens  ia.container.flex  [5 bindings]
      Toggle  ia.container.flex
        Toggle  ia.input.checkbox
        Pens  ia.display.flex-repeater  [4 bindings; view: 98_Configuration/AdhocTrend/_Assets/Pen]
      Table  ia.display.table  [2 bindings]
    NoPens  ia.input.text-area  [2 bindings]
```

</details>

## Bindings

81 bindings: property 40, expr-struct 20, expr 20, query 1.

<details>
<summary>All 81 bindings, grouped by component</summary>

**`(view)`**

- `custom.aggregate`: property `session.custom.AdhocTrend.aggregate`

- `custom.colors`: property `session.custom.AdhocTrend.colors`

- `custom.dbTrendConfig`: named query, then script transform

Named query `AdhocTrend/SelectTrendConfigById`, return format `auto`

```js
trendId: {view.custom.trendId}
```

Transform 1, script:

```python
if value is None:
    return {}
try:
    row_count = value.getRowCount()
except:
    return {}
if row_count > 0:
    config_dict = system.util.jsonDecode(value.getValueAt(0, "trend_config"))
    for key in ["startDate", "endDate"]:
        if key in config_dict:
            try:
                config_dict[key] = system.date.parse(config_dict[key])
            except:
                config_dict[key] = system.date.parse(config_dict[key], "MMM d, yyyy, h:mm:ss a")
    config_dict.update({
        "trendId": value.getValueAt(0, "id"),
        "trendName": value.getValueAt(0, "trend_name"),
        "username": value.getValueAt(0, "username"),
        "isShared": value.getValueAt(0, "is_shared")
    })
    return config_dict
return {}
```


- `custom.endDate`: structured expression (expr-struct), then expression transform

```js
endDate: {session.custom.AdhocTrend.endDate}
realTime: {view.custom.realTime}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['realTime'],
	now(1000),
	{value}['endDate']
)
```


- `custom.isConfigUpdated`: structured expression (expr-struct), then script transform

```js
dbTrendConfig: {view.custom.dbTrendConfig}
sessionTrendConfig: {session.custom.AdhocTrend}
sessionUsername: {session.props.auth.user.userName}
```

waitOnAll: `True`

Transform 1, script:

```python
if value is None or getattr(value, "dbTrendConfig", None) is None:
    return False
db_cfg = value.dbTrendConfig
try:
    _ = db_cfg.keys()
except:
    return False

# This recursively digs through arrays (like your tags) and dictionaries,
# permanently deleting the sneaky "quality" and "timestamp" wrappers!
def clean_wrappers(obj):
    try:
        # If it's an Ignition Property Wrapper, drill down into its core value
        if hasattr(obj, "value") and hasattr(obj, "quality"):
            return clean_wrappers(obj.value)
    except: pass
    
    # If it's a standard dictionary that looks like a wrapper, strip it
    if isinstance(obj, dict) or str(type(obj)).find("DictionaryWrapper") > -1:
        if "value" in obj and "quality" in obj:
            return clean_wrappers(obj["value"])
        # Clean all keys inside the dict
        return {k: clean_wrappers(v) for k, v in dict(obj).items() if k not in ['timestamp', 'quality']}
        
    # If it's an array (like your tags list), clean every single item inside it!
    if hasattr(obj, "__iter__") and not isinstance(obj, basestring):
        return [clean_wrappers(item) for item in obj]
        
    return obj

# --- 2. The Extraction ---
# These are the ONLY keys that matter for checking if the chart was modified.
keys_to_check = db_cfg.keys()

# Determine the config got updated only when the logged in user is matching the user who has loaded the trend
if 'username' in keys_to_check:
    if value.sessionUsername == db_cfg.username:
        for key in keys_to_check:
            # Grab the messy block from both the Live Session and the Database Config
            messy_live = value.sessionTrendConfig.get(key)
# ... 14 more line(s): see the view.json
```


- `custom.pens`: structured expression (expr-struct), then script transform

```js
colors: {view.custom.colors}
session: {session.custom.AdhocTrend}
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, script:

```python
rows = []
headers = ["penEnabled", "tagPath", "penName", "alias", "engUnit", "penColor", "plotId", "penAction"]
if value is None:
    return system.dataset.toDataSet(headers, rows)
tags = value.tags if hasattr(value, "tags") else None
colors = value.colors if hasattr(value, "colors") else None
cfg = None
try:
    cfg = self.session.custom.AdhocTrend
except:
    cfg = None
if tags is None or colors is None:
    return system.dataset.toDataSet(headers, rows)
try:
    penPlots = shared.AdhocTrend.plain_pen_plots(cfg)
    plots = shared.AdhocTrend.plain_plots(cfg)
    disabled = shared.AdhocTrend.plain_disabled_pens(cfg)
    return shared.AdhocTrend.build_pens(tags, colors, penPlots, plots, disabled)
except:
    # Fallback: still use Parent Child labels + palette cycling
    palette = shared.AdhocTrend.palette_colors(colors)
    pen_i = 0
    for tag in tags:
        if tag not in (None, ""):
            tag = str(tag)
            histPath = tag if tag.endswith("/Value") else (tag + "/Value")
            penName = shared.AdhocTrend.pen_label(tag)
            alias = shared.AdhocTrend.alias_for(tag)
            engUnit = ""
            try:
                read = system.tag.readBlocking([histPath + ".EngUnit"])
                engUnit = read[0].value if read[0].value not in (None, "") else ""
            except:
                pass
            penColor = shared.AdhocTrend.color_for_index(palette, pen_i)
            rows.append([True, histPath, penName, alias, engUnit, penColor, "p0", ""])
            pen_i += 1
    return system.dataset.toDataSet(headers, rows)
```


- `custom.pointCount`: property `session.custom.AdhocTrend.pointCount`

- `custom.realTime`: property `session.custom.AdhocTrend.realtime`

- `custom.startDate`: structured expression (expr-struct), then expression transform

```js
realTime: {view.custom.realTime}
startDate: {session.custom.AdhocTrend.startDate}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['realTime'],
	dateArithmetic(now(1000), -if(isNull({session.custom.AdhocTrend.timeRange}) || {session.custom.AdhocTrend.timeRange}<=0, 1, {session.custom.AdhocTrend.timeRange}), 'hour'),
	{value}['startDate']
)
```


- `custom.tags`: property `session.custom.AdhocTrend.tags`

- `custom.timeRange`: structured expression (expr-struct), then expression transform

```js
realTime: {view.custom.realTime}
timeRange: {session.custom.AdhocTrend.timeRange}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['realTime'],
	if(isNull({value}['timeRange']) || {value}['timeRange']<=0, 1, {value}['timeRange']),
	1
)
```


- `custom.trendId`: property `session.custom.AdhocTrend.trendId`

- `custom.trendName`: property `session.custom.AdhocTrend.trendName`

- `custom.username`: property `session.custom.AdhocTrend.username`

**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `props.style.classes`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
if(coalesce({value}, false), 'bg-container adhoc-trend-faceplate-embed', 'bg-container')
```


- `props.style.overflow`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
if(coalesce({value}, false), 'hidden', 'visible')
```


**`root/TagTree`**

- `position.display`: structured expression (expr-struct), then expression transform

```js
faceplateMode: {view.params.faceplateMode}
treeVisible: {view.custom.treeVisible}
```

waitOnAll: `True`

Transform 1, expression:

```js
!coalesce({value}['faceplateMode'], false) && {value}['treeVisible']
```


**`root/TagTree/Tree`**

- `position.display`: property `view.custom.treeVisible`

**`root/TagTree/AddToTrend`**

- `position.display`: property `../Tree.props.selectionData`, then script transform

Transform 1, script:

```python
display = False
if len(value) > 0:
    for data in value:
        if 'value' in data.keys():
            if 'hasChildren' in data['value'].keys():
                if data['value']['hasChildren']:
                    display = False
                    break
                else:
                    display = True
return display
```


**`root/TrendContainer/Trend`**

- `position.basis`: structured expression (expr-struct), then expression transform

```js
faceplateMode: {view.params.faceplateMode}
pensCollapsed: {../Pens/Toggle/Toggle.props.selected}
```

waitOnAll: `True`

Transform 1, expression:

```js
'0px'
```


- `position.shrink`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
1
```


- `props.style.height`: structured expression (expr-struct), then expression transform

```js
faceplateMode: {view.params.faceplateMode}
pensCollapsed: {../Pens/Toggle/Toggle.props.selected}
```

waitOnAll: `True`

Transform 1, expression:

```js
if(coalesce({value}['pensCollapsed'], false), '0', '0px')
```


- `props.style.overflow`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
'hidden'
```


**`root/TrendContainer/Trend/TrendName`**

- `meta.visible`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
!coalesce({value}, false)
```


- `position.basis`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
if(coalesce({value}, false), '0px', '22px')
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/tagBrowser`**

- `meta.visible`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
!coalesce({value}, false)
```


- `props.path`: property `view.custom.treeVisible`, then expression transform

Transform 1, expression:

```js
if({value},'material/keyboard_arrow_left','material/local_offer')
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/trendConfig`**

- `meta.visible`: property `view.custom.tags`, then expression transform

Transform 1, expression:

```js
len({value})>0
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/ChartType`**

- `meta.visible`: property `view.custom.tags`, then expression transform

Transform 1, expression:

```js
len({value})>0
```


- `props.text`: property `view.custom.realTime`, then map transform

Transform 1, map (scalar to scalar):

```
true -> "Realtime"
false -> "Historical"
fallback -> ""
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/TimeRange`**

- `meta.visible`: structured expression (expr-struct), then expression transform

```js
realtime: {view.custom.realTime}
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, expression:

```js
{value}['realtime'] && len({value}['tags']) > 0
```


- `props.text`: property `view.custom.timeRange`, then map transform

Transform 1, map (scalar to scalar):

```
1 -> "Last Hour"
3 -> "Last 3 Hours"
6 -> "Last 6 Hours"
12 -> "Last 12 Hours"
24 -> "Last 24 hours"
168 -> "Last Week"
730 -> "Last Month"
2190 -> "Last 3 Months"
4380 -> "Last 6 Months"
fallback -> ""
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/StartDate`**

- `meta.visible`: structured expression (expr-struct), then expression transform

```js
realtime: {view.custom.realTime}
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, expression:

```js
!{value}['realtime'] && len({value}['tags']) > 0
```


- `props.text`: property `view.custom.startDate`, then format + expression transform

Transform 1, format `datetime` `d MMM YYYY h:mm a`

Transform 2, expression:

```js
{value} + " -  "
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/EndDate`**

- `meta.visible`: structured expression (expr-struct), then expression transform

```js
realtime: {view.custom.realTime}
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, expression:

```js
!{value}['realtime'] && len({value}['tags']) > 0
```


- `props.text`: property `view.custom.endDate`, then format transform

Transform 1, format `datetime` `d MMM YYYY h:mm a`


**`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges`**

- `meta.visible`: expression

```js
len(coalesce({view.custom.tags}, asList())) > 0
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range1H`**

- `props.style.classes`: expression

```js
if(coalesce({session.custom.AdhocTrend.realtime}, false) && coalesce({session.custom.AdhocTrend.timeRange}, 1) = 1, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range8H`**

- `props.style.classes`: expression

```js
if(coalesce({session.custom.AdhocTrend.realtime}, false) && coalesce({session.custom.AdhocTrend.timeRange}, 1) = 8, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range24H`**

- `props.style.classes`: expression

```js
if(coalesce({session.custom.AdhocTrend.realtime}, false) && coalesce({session.custom.AdhocTrend.timeRange}, 1) = 24, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range7D`**

- `props.style.classes`: expression

```js
if(coalesce({session.custom.AdhocTrend.realtime}, false) && coalesce({session.custom.AdhocTrend.timeRange}, 1) = 168, 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/TrendContainer/Trend/PlotToolbar/Icons/LivePause`**

- `props.text`: expression

```js
if(coalesce({session.custom.AdhocTrend.realtime}, false), 'Live', 'Paused')
```


- `props.image.icon.path`: expression

```js
if(coalesce({session.custom.AdhocTrend.realtime}, false), 'material/fiber_manual_record', 'material/pause')
```


- `props.style.classes`: expression

```js
if(coalesce({session.custom.AdhocTrend.realtime}, false), 'trend-tool-btn trend-live-on', 'trend-tool-btn')
```


- `meta.visible`: expression

```js
len(coalesce({view.custom.tags}, asList())) > 0
```


**`root/TrendContainer/Trend/PlotToolbar/Buttons`**

- `props.style.classes`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
if(coalesce({value}, false), 'adhoc-trend-toolbar-actions adhoc-trend-toolbar-actions-faceplate', 'adhoc-trend-toolbar-actions')
```


- `props.style.paddingBottom`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
if(coalesce({value}, false), '0px', '0px')
```


**`root/TrendContainer/Trend/PlotToolbar/Buttons/RemovePlot`**

- `meta.visible`: property `view.custom.tags`, then expression transform

Transform 1, expression:

```js
len({value})>0
```


**`root/TrendContainer/Trend/PlotToolbar/Buttons/AddPlot`**

- `meta.visible`: property `view.custom.tags`, then expression transform

Transform 1, expression:

```js
len({value})>0
```


**`root/TrendContainer/Trend/PlotToolbar/Buttons/SaveTrendConfig`**

- `custom.id`: property `session.props.auth.user.id`, then expression transform

Transform 1, expression:

```js
'SaveTrendConfig-' + coalesce(toString({value}), 'anon')
```


- `meta.visible`: structured expression (expr-struct), then expression transform

```js
tags: {session.custom.AdhocTrend.tags}
trendId: {session.custom.AdhocTrend.trendId}
```

waitOnAll: `True`

Transform 1, expression:

```js
len({value}['tags']) > 0 && ({value}['trendId'] = '' || isNull({value}['trendId']))
```


**`root/TrendContainer/Trend/PlotToolbar/Buttons/UpdateTrendConfig`**

- `custom.id`: property `session.props.auth.user.id`, then expression transform

Transform 1, expression:

```js
'SaveTrendConfig-' + coalesce(toString({value}), 'anon')
```


- `meta.visible`: structured expression (expr-struct), then expression transform

```js
tags: {session.custom.AdhocTrend.tags}
trendId: {session.custom.AdhocTrend.trendId}
```

waitOnAll: `True`

Transform 1, expression:

```js
len({value}['tags']) > 0 && {value}['trendId'] != '' && !isNull({value}['trendId'])
```


**`root/TrendContainer/Trend/PlotToolbar/Buttons/ClearPens`**

- `meta.visible`: property `view.custom.tags`, then expression transform

Transform 1, expression:

```js
len({value})>0
```


**`root/TrendContainer/Trend/ChartTools`**

- `position.display`: expression

```js
len(coalesce({view.custom.tags}, asList())) > 0
```


**`root/TrendContainer/Trend/ChartTools/Row/DragMode/ModeZoomTime`**

- `props.style.classes`: expression

```js
if(if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'time', 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/TrendContainer/Trend/ChartTools/Row/DragMode/ModeZoomArea`**

- `props.style.classes`: expression

```js
if(if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'area', 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/TrendContainer/Trend/ChartTools/Row/DragMode/ModePan`**

- `props.style.classes`: expression

```js
if(if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')) = 'pan', 'trend-seg trend-seg-on', 'trend-seg')
```


**`root/TrendContainer/Trend/ChartTools/Row/AutoScale/Switch`**

- `props.selected`: expression

```js
coalesce(try({session.custom.trendTools.autoScaleY}, false), false)
```


**`root/TrendContainer/Trend/ChartTools/Row/AutoScale/State`**

- `props.text`: expression

```js
if(coalesce(try({session.custom.trendTools.autoScaleY}, false), false), 'On', 'Off')
```


- `props.style.classes`: expression

```js
if(coalesce(try({session.custom.trendTools.autoScaleY}, false), false), 'trend-switch-state trend-switch-state-on', 'trend-switch-state')
```


**`root/TrendContainer/Trend/ChartTools/Row/ResetZoom`**

- `props.enabled`: expression

```js
!isNull(try({session.custom.trendTools.zoomMin}, null)) && !isNull(try({session.custom.trendTools.zoomMax}, null))
```


**`root/TrendContainer/Trend/ChartTools/Row/ZoomChip`**

- `meta.visible`: expression

```js
!isNull(try({session.custom.trendTools.zoomMin}, null)) && !isNull(try({session.custom.trendTools.zoomMax}, null))
```


**`root/TrendContainer/Trend/ChartTools/Row/ZoomChip/Range`**

- `props.text`: expression

```js
if(!isNull(try({session.custom.trendTools.zoomMin}, null)) && !isNull(try({session.custom.trendTools.zoomMax}, null)), 'Zoomed: ' + dateFormat(fromMillis(try({session.custom.trendTools.zoomMin}, null)), if(try({session.custom.trendTools.zoomMax}, null) - try({session.custom.trendTools.zoomMin}, null) < 86400000, 'HH:mm', 'MMM d HH:mm')) + ' - ' + dateFormat(fromMillis(try({session.custom.trendTools.zoomMax}, null)), if(try({session.custom.trendTools.zoomMax}, null) - try({session.custom.trendTools.zoomMin}, null) < 86400000, 'HH:mm', 'MMM d HH:mm')), '')
```


**`root/TrendContainer/Trend/ChartTools/Hint`**

- `props.text`: expression

```js
case(if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'area', 'area', if(coalesce(try({session.custom.trendTools.dragMode}, 'time'), 'time') = 'pan', 'pan', 'time')), 'area', 'Drag a box on a chart to zoom into that time and value range', 'pan', 'Drag a chart left or right to move through time', 'Drag across a chart to zoom into that time range') + ' · Scroll to zoom · Double-click to reset'
```


**`root/TrendContainer/Trend/Plots`**

- `props.instances`: structured expression (expr-struct), then script transform

```js
faceplateMode: {view.params.faceplateMode}
pensCollapsed: {../../Pens/Toggle/Toggle.props.selected}
plots: {session.custom.AdhocTrend.plots}
viewportH: {page.props.dimensions.viewport.height}
```

waitOnAll: `True`

Transform 1, script:

```python
instances = []
if value is None:
    return instances
plots = shared.AdhocTrend.plain_plots(value)
n = len(plots)
show_tb = True  # trend-context: every plot keeps its tools
collapsed = False
try:
    collapsed = bool(value["pensCollapsed"])
except:
    collapsed = bool(getattr(value, "pensCollapsed", False))
faceplate = False
try:
    faceplate = bool(value["faceplateMode"])
except:
    faceplate = bool(getattr(value, "faceplateMode", False))
vh = None
try:
    vh = value["viewportH"]
except:
    vh = getattr(value, "viewportH", None)
chart_h = shared.AdhocTrend.plot_chart_height(faceplate, collapsed, n, vh)
layout_key = "c%d" % chart_h if collapsed else "e%d" % chart_h
for i, p in enumerate(plots):
    instances.append({
        "instanceStyle": {"classes": "", "maxHeight": "none", "height": "0", "flex": "1 1 0", "minHeight": 0, "overflow": "hidden"},
        "instancePosition": {"grow": 1, "shrink": 1, "basis": "0px"},
        "plotId": p["id"],
        "plotTitle": p["title"],
        "plotKind": p["kind"],
        "plotCount": n,
        "showToolbar": show_tb,
        "layoutKey": layout_key,
        "chartHeight": chart_h,
        "canRemove": p["id"] != "p0",
    })
return instances
```


**`root/TrendContainer/Pens`**

- `position.basis`: structured expression (expr-struct), then expression transform

```js
faceplateMode: {view.params.faceplateMode}
selected: {./Toggle/Toggle.props.selected}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['selected'],
	'32px',
	if(coalesce({value}['faceplateMode'], false), '200px', '188px')
)
```


- `position.display`: property `view.custom.pens`, then expression transform

Transform 1, expression:

```js
len({value})>0
```


- `position.grow`: structured expression (expr-struct), then expression transform

```js
faceplateMode: {view.params.faceplateMode}
selected: {./Toggle/Toggle.props.selected}
```

waitOnAll: `True`

Transform 1, expression:

```js
0
```


- `position.shrink`: structured expression (expr-struct), then expression transform

```js
faceplateMode: {view.params.faceplateMode}
selected: {./Toggle/Toggle.props.selected}
```

waitOnAll: `True`

Transform 1, expression:

```js
0
```


- `props.style.classes`: structured expression (expr-struct), then expression transform

```js
faceplateMode: {view.params.faceplateMode}
selected: {./Toggle/Toggle.props.selected}
```

waitOnAll: `True`

Transform 1, expression:

```js
if(coalesce({value}['faceplateMode'], false),
	if({value}['selected'], 'container-card adhoc-trend-pens adhoc-trend-pens-faceplate adhoc-trend-pens-collapsed', 'container-card adhoc-trend-pens adhoc-trend-pens-faceplate'),
	if({value}['selected'], 'container-card adhoc-trend-pens adhoc-trend-pens-collapsed', 'container-card adhoc-trend-pens')
)
```


**`root/TrendContainer/Pens/Toggle/Pens`**

- `position.display`: property `../Toggle.props.selected`, then expression transform

Transform 1, expression:

```js
false
```


- `props.elementStyle.minWidth`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
if(coalesce({value}, false), 0, 320)
```


- `props.instances`: property `view.custom.pens`, then script transform

Transform 1, script:

```python
instances = []
if value is None:
    return instances
try:
    if value.getRowCount() <= 0:
        return instances
except:
    return instances
pens = system.dataset.toPyDataSet(value)
for pen in pens:
    if pen["penEnabled"]:
        instances.append({
            "instanceStyle": {"classes": ""},
            "instancePosition": {},
            "color": pen["penColor"],
            "penName": pen["penName"],
            "plotId": pen["plotId"] if "plotId" in pen else "p0",
            "tagPath": pen["tagPath"],
            "justify": "flex-start",
        })
return instances
```


- `props.style.marginBottom`: property `this.props.direction`, then expression transform

Transform 1, expression:

```js
if({value} = 'row',
	'0%',
	'0.1%'
)
```


**`root/TrendContainer/Pens/Table`**

- `position.display`: property `../Toggle/Toggle.props.selected`, then expression transform

Transform 1, expression:

```js
!{value}
```


- `props.data`: property `view.custom.pens`

**`root/TrendContainer/NoPens`**

- `position.basis`: property `view.params.faceplateMode`, then expression transform

Transform 1, expression:

```js
if(coalesce({value}, false), '48px', '10%')
```


- `position.display`: property `../Pens.position.display`, then expression transform

Transform 1, expression:

```js
!{value}
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 30 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
self.view.custom.treeVisible = False
```

- **`root/TagTree/Tree`** `system.onStartup`, script action, scope `G`

```python
from shared import tagsTree
try:
    paths = tagsTree.getHistoricalTags()
    tree = tagsTree.createTree(paths)
except Exception as e:
    system.util.getLogger("AdhocTrend").warn("Historized tag tree failed: %s" % str(e))
    tree = []
self.props.items = tree
```

- **`root/TagTree/AddToTrend`** `component.onActionPerformed`, script action, scope `G`

```python
from shared import Alerts
selectionData = self.getSibling("Tree").props.selectionData
cfg = self.session.custom.AdhocTrend
for data in selectionData:
    if 'value' in data.keys():
        if 'tagPath' in data['value'].keys() and 'hasChildren' in data['value'].keys():
            tagPath = data['value']['tagPath']
            tags = list(cfg.tags) if cfg.tags is not None else []
            if tagPath in tags:
                Alerts.showAlert(state="info",title="Adhoc Trending",message='Tag is already added to the trend.<br><br>TagPath:<br>' + str(tagPath), showCloseBtn=False,btnTextPrimary="Okay",btnTextSecondary="",btnActionPrimary="",btnActionSecondary="",payload={})
            else:
                if len(tags) < 10:
                    tags.append(tagPath)
                    # Reassign lists so pens bindings re-evaluate with fresh labels/colors
                    cfg.tags = tags
                    cfg.colors = shared.AdhocTrend.palette_colors(cfg.colors)
                    _pid, plots, penPlots = shared.AdhocTrend.route_new_pen(cfg, tagPath)
                    cfg.plots = plots
                    cfg.penPlots = penPlots
                else:
                    Alerts.showAlert(state="warning",title="Adhoc Trending",message='You have exceeded the limit of 10 tags, Please remove tags that are not required from the trend.',showCloseBtn=False,btnTextPrimary="Okay",btnTextSecondary="",btnActionPrimary="",btnActionSecondary="",payload={})
```

- **`root/TrendContainer/Trend/PlotToolbar/Icons/tagBrowser`** `dom.onClick`, script action, scope `G`

```python
from shared import tagsTree
showing = not self.view.custom.treeVisible
self.view.custom.treeVisible = showing
tree = self.view.rootContainer.getChild("TagTree").getChild("Tree")
tree.props.selection = []
tree.props.selectionData = []
# Rebuild historized tree when opening (no view.custom.treeItems cache)
if showing:
    tree.props.items = tagsTree.createTree(tagsTree.getHistoricalTags())
```

- **`root/TrendContainer/Trend/PlotToolbar/Icons/trendConfig`** `dom.onClick`, script action, scope `G`

```python
from shared import Alerts
faceplate = False
try:
    faceplate = bool(self.view.params.faceplateMode)
except:
    faceplate = False
if faceplate:
    Alerts.showAdhocTrendConfig()
else:
    system.perspective.openPopup(
        id="AdhocTrendToolBar",
        view="98_Configuration/AdhocTrend/_Assets/ToolBar",
        params={"faceplateShell": False},
        position={"left": 280, "top": 110},
        draggable=True,
        resizable=False,
        showCloseIcon=False,
        modal=True,
        overlayDismiss=False,
        viewportBound=False
    )
```

- **`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range1H`** `component.onActionPerformed`, script action, scope `G`

```python
cfg = self.session.custom.AdhocTrend
cfg.timeRange = 1
cfg.realtime = True
shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range8H`** `component.onActionPerformed`, script action, scope `G`

```python
cfg = self.session.custom.AdhocTrend
cfg.timeRange = 8
cfg.realtime = True
shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range24H`** `component.onActionPerformed`, script action, scope `G`

```python
cfg = self.session.custom.AdhocTrend
cfg.timeRange = 24
cfg.realtime = True
shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/TrendContainer/Trend/PlotToolbar/Icons/Ranges/Range7D`** `component.onActionPerformed`, script action, scope `G`

```python
cfg = self.session.custom.AdhocTrend
cfg.timeRange = 168
cfg.realtime = True
shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/TrendContainer/Trend/PlotToolbar/Icons/LivePause`** `component.onActionPerformed`, script action, scope `G`

```python
cfg = self.session.custom.AdhocTrend
if cfg.realtime:
    end = system.date.now()
    cfg.endDate = end
    cfg.startDate = system.date.addHours(end, -max(int(cfg.timeRange or 1), 1))
    cfg.realtime = False
else:
    cfg.realtime = True
    shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/TrendContainer/Trend/PlotToolbar/Buttons/RemovePlot`** `component.onActionPerformed`, script action, scope `G`

```python
from shared import Alerts
cfg = self.session.custom.AdhocTrend
action, msg, plots, penPlots = shared.AdhocTrend.prompt_remove_plot(cfg)
if action == 'none':
    Alerts.showAlert(state="info", title="Cannot Remove Plot", message=msg, showCloseBtn=True, btnTextPrimary="OK", btnActionPrimary="closeAlert")
elif action == 'error':
    Alerts.showAlert(state="warning", title="Cannot Remove Plot", message=msg, showCloseBtn=True, btnTextPrimary="OK", btnActionPrimary="closeAlert")
elif action == 'removed':
    self.session.custom.AdhocTrend.plots = plots
    self.session.custom.AdhocTrend.penPlots = penPlots
# action == 'prompt' → RemovePlot popup handles confirm
```

- **`root/TrendContainer/Trend/PlotToolbar/Buttons/AddPlot`** `component.onActionPerformed`, script action, scope `G`

```python
# Prompt for plot name; Confirm creates empty named plot, Cancel does nothing.
shared.AdhocTrend.prompt_add_plot()
```

- **`root/TrendContainer/Trend/PlotToolbar/Buttons/SaveTrendConfig`** `component.onActionPerformed`, script action, scope `G`

```python
uid = None
try:
    uid = self.session.props.auth.user.id
except:
    pass
popup_id = "SaveTrendConfig-" + (str(uid) if uid not in (None, "") else "anon")
system.perspective.openPopup(
    id=popup_id,
    view="98_Configuration/AdhocTrend/_Assets/SaveTrendConfig",
    position={"right": 130, "top": 120, "width": 380, "height": 280},
    draggable=False,
    resizable=False,
    showCloseIcon=False,
    modal=False,
    overlayDismiss=False,
    viewportBound=False
)
```

- **`root/TrendContainer/Trend/PlotToolbar/Buttons/UpdateTrendConfig`** `component.onActionPerformed`, script action, scope `G`

```python
uid = None
try:
    uid = self.session.props.auth.user.id
except:
    pass
popup_id = "SaveTrendConfig-" + (str(uid) if uid not in (None, "") else "anon")
system.perspective.openPopup(
    id=popup_id,
    view="98_Configuration/AdhocTrend/_Assets/SaveTrendConfig",
    position={"right": 130, "top": 120, "width": 380, "height": 280},
    draggable=False,
    resizable=False,
    showCloseIcon=False,
    modal=False,
    overlayDismiss=False,
    viewportBound=False
)
```

- **`root/TrendContainer/Trend/PlotToolbar/Buttons/ClearPens`** `component.onActionPerformed`, script action, scope `G`

```python
# Default Adhoc Trend Config
default_config = {
    "tags": [],
    "colors": [
        "#008FFB",
        "#34C759",
        "#FFA726",
        "#FF4560",
        "#775DD0",
        "#1C4E80",
        "#008080",
        "#26C6DA",
        "#4F4F4F",
        "#6C757D"
    ],
    "realtime": True,
    "timeRange": 1,
    "pointCount": 120,
    "chartType": "line",
    "aggregate": "Average",
    "trendId": "",
    "trendName": "",
    "username": "",
    "isShared": True,
    "plots": shared.AdhocTrend.default_plots(),
# ... 6 more line(s): see the view.json
```

- **`root/TrendContainer/Trend/ChartTools/Row/DragMode/ModeZoomTime`** `component.onActionPerformed`, script action, scope `G`

```python
tt = self.session.custom.trendTools
tt.dragMode = 'time'
tt.zoomKind = 'time'
if 'time' == 'area':
    shared.AdhocTrend.pause_live(self.session.custom.AdhocTrend)   # see QUICK_SET_MODE
```

- **`root/TrendContainer/Trend/ChartTools/Row/DragMode/ModeZoomArea`** `component.onActionPerformed`, script action, scope `G`

```python
tt = self.session.custom.trendTools
tt.dragMode = 'area'
tt.zoomKind = 'time'
if 'area' == 'area':
    shared.AdhocTrend.pause_live(self.session.custom.AdhocTrend)   # see QUICK_SET_MODE
```

- **`root/TrendContainer/Trend/ChartTools/Row/DragMode/ModePan`** `component.onActionPerformed`, script action, scope `G`

```python
tt = self.session.custom.trendTools
tt.dragMode = 'pan'
tt.zoomKind = 'time'
if 'pan' == 'area':
    shared.AdhocTrend.pause_live(self.session.custom.AdhocTrend)   # see QUICK_SET_MODE
```

- **`root/TrendContainer/Trend/ChartTools/Row/ZoomIn`** `component.onActionPerformed`, script action, scope `G`

```python
shared.AdhocTrend.zoom_step(self.session, 0.5)
```

- **`root/TrendContainer/Trend/ChartTools/Row/ZoomOut`** `component.onActionPerformed`, script action, scope `G`

```python
shared.AdhocTrend.zoom_step(self.session, 2.0)
```

- **`root/TrendContainer/Trend/ChartTools/Row/AutoScale`** `dom.onClick`, script action, scope `G`

```python
tt = self.session.custom.trendTools
tt.autoScaleY = not bool(shared.AdhocTrend._cfg_get(tt, 'autoScaleY', False))
```

- **`root/TrendContainer/Trend/ChartTools/Row/ResetZoom`** `component.onActionPerformed`, script action, scope `G`

```python
shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/TrendContainer/Trend/ChartTools/Row/ZoomChip`** `dom.onClick`, script action, scope `G`

```python
shared.AdhocTrend.zoom_reset(self.session)
```

- **`root/TagTree/Tree`** change script on `props.items`

```python
# Accordion cleanup only - tree is fully loaded on startup for lab scale
if origin == 'Script':
    return
```

- **`root`** message handler `AdhocTrendDeleteRow` (scope: page)

```python
# Remove pen from tags/colors and clean disabledPens / penPlots.
cfg = self.session.custom.AdhocTrend
row = payload['row']
tags = list(cfg.tags) if cfg.tags is not None else []
tag = tags[row] if row < len(tags) else None
alias = shared.AdhocTrend.alias_for(tag) if tag else None
cfg.tags.pop(row)
colorRemoved = cfg.colors.pop(row)
cfg.colors.insert(row + 1, colorRemoved)
dp = shared.AdhocTrend.plain_disabled_pens(cfg)
pp = shared.AdhocTrend.plain_pen_plots(cfg)
for key in (alias, tag):
    if key not in (None, '') and str(key) in dp:
        del dp[str(key)]
    if key not in (None, '') and str(key) in pp:
        del pp[str(key)]
cfg.disabledPens = dp
cfg.penPlots = pp
```

- **`root`** message handler `AdhocTrendDisableRow` (scope: page)

```python
# Toggle On checkbox - persist in session.disabledPens so charts rebuild.
cfg = self.session.custom.AdhocTrend
pens = self.view.custom.pens
row = payload.get('row')
alias = None
try:
    alias = pens.getValueAt(row, 'alias')
except:
    pass
if alias in (None, ''):
    try:
        alias = pens.getValueAt(row, 'tagPath')
    except:
        alias = payload.get('penName')
disabled = shared.AdhocTrend.toggle_pen_enabled(cfg, alias)
self.session.custom.AdhocTrend.disabledPens = disabled
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

- **`root`** message handler `commitTrendConfig` (scope: page)

```python
try:
    pid = self.getChild("TrendContainer").getChild("Trend").getChild("PlotToolbar").getChild("Buttons").getChild("SaveTrendConfig").custom.id
    system.perspective.closePopup(pid)
except:
    pass
try:
    system.perspective.closePopup("SaveTrendConfig-anon")
except:
    pass
self.view.refreshBinding("custom.dbTrendConfig")
```

- **`root`** message handler `closeAlert` (scope: page)

```python
# implement your handler here
system.perspective.closePopup(id="alertDialog")
```

- **`root`** message handler `AdhocTrendConfigData` (scope: page)

```python
# implement your handler here
self.view.custom.trendId = payload["trendId"]
self.view.custom.trendName = payload["trendName"]
self.view.custom.username = payload["username"]
```

</details>

Project script calls: [shared.AdhocTrend.\_cfg\_get](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.alias\_for](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.build\_pens](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.color\_for\_index](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.default\_plots](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.palette\_colors](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.pen\_label](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_disabled\_pens](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_pen\_plots](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plain\_plots](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.plot\_chart\_height](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.prompt\_remove\_plot](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.route\_new\_pen](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.AdhocTrend.toggle\_pen\_enabled](../../../../../scripting/reference/modules/shared-adhoctrend.md), [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (2): [98\_Configuration/AdhocTrend/\_Assets/Pen](./assets/pen.md) (flex repeater), [98\_Configuration/AdhocTrend/\_Assets/Plot](./assets/plot.md) (flex repeater)

**Opens or names** (popups, scripts, expressions): [98\_Configuration/AdhocTrend/\_Assets/PenColor](./assets/pencolor.md), [98\_Configuration/AdhocTrend/\_Assets/PenDelete](./assets/pendelete.md), [98\_Configuration/AdhocTrend/\_Assets/PenEnable](./assets/penenable.md), [98\_Configuration/AdhocTrend/\_Assets/PenPlot](./assets/penplot.md), [98\_Configuration/AdhocTrend/\_Assets/SaveTrendConfig](./assets/savetrendconfig.md), [98\_Configuration/AdhocTrend/\_Assets/ToolBar](./assets/toolbar.md)

**Embedded in** (1): [01\_Popups/00\_Faceplates/AdhocTrend](../../01-popups/00-faceplates/adhoctrend.md)

**Named in project scripts**: [Navigation.Nav](../../../../../scripting/reference/modules/navigation-nav.md)

## Style Classes

<details>
<summary>45 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 6 | style class |
| `Fonts/Header` | 1 | style class |
| `Fonts/Label` | 7 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `adhoc-trend-action-btn-outline` | 1 | stylesheet |
| `adhoc-trend-add-plot-btn` | 5 | stylesheet |
| `adhoc-trend-chart-host` | 2 | stylesheet |
| `adhoc-trend-clear-btn` | 1 | stylesheet |
| `adhoc-trend-pens-header` | 1 | stylesheet |
| `adhoc-trend-plot-toolbar` | 1 | stylesheet |
| `adhoc-trend-plots` | 1 | stylesheet |
| `adhoc-trend-remove-plot-btn` | 1 | stylesheet |
| `adhoc-trend-save-btn` | 2 | stylesheet |
| `adhoc-trend-tag-browser` | 1 | stylesheet |
| `adhoc-trend-toolbar-icon` | 1 | stylesheet |
| `adhoc-trend-toolbar-label` | 2 | style class |
| `bg-header` | 1 | stylesheet |
| `bg-page` | 1 | style class |
| `color-icon` | 2 | style class |
| `container-button` | 5 | style class |
| `container-icon` | 2 | stylesheet |
| `trend-divider` | 2 | stylesheet |
| `trend-hint` | 1 | stylesheet |
| `trend-seg` | 7 | stylesheet |
| `trend-seg-group` | 2 | stylesheet |
| `trend-switch` | 1 | stylesheet |
| `trend-switch-box` | 1 | stylesheet |
| `trend-switch-label` | 1 | stylesheet |
| `trend-switch-state` | 1 | stylesheet |
| `trend-tool-btn` | 4 | stylesheet |
| `trend-tool-icon` | 2 | stylesheet |
| `trend-tools` | 1 | stylesheet |
| `trend-tools-row` | 1 | stylesheet |
| `trend-zoom-chip` | 1 | stylesheet |
| `trend-zoom-chip-link` | 1 | stylesheet |
| `trend-zoom-chip-text` | 2 | stylesheet |
| `adhoc-trend-pens` | bound | stylesheet |
| `adhoc-trend-pens-collapsed` | bound | stylesheet |
| `adhoc-trend-pens-faceplate` | bound | stylesheet |
| `adhoc-trend-toolbar-actions` | bound | stylesheet |
| `adhoc-trend-toolbar-actions-faceplate` | bound | stylesheet |
| `container-card` | bound | stylesheet |
| `trend-seg-on` | bound | stylesheet |
| `trend-switch-state-on` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Named queries: `AdhocTrend/SelectTrendConfigById`.

Member paths appended to a base path in expressions (relative):

`.EngUnit`, `/Value`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
