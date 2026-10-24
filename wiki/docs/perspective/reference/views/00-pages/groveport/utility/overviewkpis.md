---
title: "OverviewKpis"
sidebar_label: "OverviewKpis"
description: "Perspective view 00_Pages/Groveport/Utility/OverviewKpis (Page piece (not routed)): 28 components, 18 bindings, 8 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Utility/OverviewKpis", "OverviewKpis"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Utility/OverviewKpis`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Utility/OverviewKpis` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Utility/OverviewKpis/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Utility &gt; OverviewKpis |
| Root | `ia.container.flex`, height 1016, width 500 |
| Size | 28 components, 18 bindings, 7 event handlers, 1 change scripts, 1 message handlers |
| Last saved | 2026-08-21T12:00:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `metrics` | `{"avgTemp": null, "categories": [], "cgs": [], "cooling": 0, "count...` | bound (expr) |

## Component Tree

Component types: ia.container.flex x12, ia.display.label x7, kyvislabs.display.apexchart x6, ia.container.tab x2, ia.display.table x1.

<details>
<summary>Component tree (28 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  KpiTabs  ia.container.tab
    PanelOverview  ia.container.flex
      TempCard  ia.container.flex
        TempHeader  ia.container.flex
          TempTitle  ia.display.label
          TempAvg  ia.display.label  [1 binding]
        TempChart  kyvislabs.display.apexchart  [3 bindings; 1 event]
      DwellCard  ia.container.flex
        DwellTabs  ia.container.tab
          PanelDwellStatus  ia.container.flex
            DwellTitle  ia.display.label
            DwellChartMain  kyvislabs.display.apexchart  [2 bindings; 1 event]
          PanelDwellDefrost  ia.container.flex
            DwellDftTitle  ia.display.label
            DwellChartDft  kyvislabs.display.apexchart  [2 bindings; 1 event]
      StatusCard  ia.container.flex
        StatusTitle  ia.display.label
        StatusChart  kyvislabs.display.apexchart  [1 binding; 2 events]
    PanelSections  ia.container.flex
      SectionChartCard  ia.container.flex
        SecChartTitle  ia.display.label
        SectionTempChart  kyvislabs.display.apexchart  [3 bindings; 1 event]
      SectionStatusCard  ia.container.flex
        SecStatusTitle  ia.display.label
        SectionStatusChart  kyvislabs.display.apexchart  [2 bindings; 1 event]
    PanelCGs  ia.container.flex
      CgTable  ia.display.table  [1 binding]
```

</details>

## Bindings

18 bindings: property 12, expr 6.

<details>
<summary>All 18 bindings, grouped by component</summary>

**`(view)`**

- `custom.metrics`: expression, then script transform

```js
now(60000)
```

Transform 1, script:

```python
# Real data only: live reads + historian averages / dwell hours (cached on the gateway). See

return shared.UtilityMetrics.get(24)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/KpiTabs/PanelOverview/TempCard/TempHeader/TempAvg`**

- `props.text`: expression

```js
if(isNull({view.custom.metrics.avgTemp}), 'No Data', numberFormat({view.custom.metrics.avgTemp}, '0.0') + ' °F')
```


**`root/KpiTabs/PanelOverview/TempCard/TempChart`**

- `props.series`: property `view.custom.metrics.temps24`, then script transform

Transform 1, script:

```python
d = list(value or [])
if not any(x is not None for x in d):
    return []
return [{'name': 'Avg F', 'data': d}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.categories`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `props.options.colors`: expression, then script transform

```js
{session.props.theme}
```

Transform 1, script:

```python
t = str(value or 'light-cool')
if t == 'light-warm':
    c = '#C45C26'
elif t == 'dark-warm':
    c = '#E8894F'
elif t in ('dark', 'dark-cool'):
    c = '#53BAED'
else:
    c = '#114599'
return [c]
```


**`root/KpiTabs/PanelOverview/DwellCard/DwellTabs/PanelDwellStatus/DwellChartMain`**

- `props.series`: property `view.custom.metrics.statusHrsMain`, then script transform

Transform 1, script:

```python
d = list(value or [])
if not any(x for x in d if x):
    return []
while len(d) < 5:
    d.append(0)
return [{'name': 'Hours', 'data': d[:5]}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.statusHrsMainCategories`, then script transform

Transform 1, script:

```python
return list(value or [])
```


**`root/KpiTabs/PanelOverview/DwellCard/DwellTabs/PanelDwellDefrost/DwellChartDft`**

- `props.series`: property `view.custom.metrics.statusHrsDft`, then script transform

Transform 1, script:

```python
d = list(value or [])
if not any(x for x in d if x):
    return []
while len(d) < 5:
    d.append(0)
return [{'name': 'Hours', 'data': d[:5]}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.statusHrsDftCategories`, then script transform

Transform 1, script:

```python
return list(value or [])
```


**`root/KpiTabs/PanelOverview/StatusCard/StatusChart`**

- `props.series`: property `view.custom.metrics.counts`, then script transform

Transform 1, script:

```python
c = value or {}
return [
    int(c.get('CLG', 0) or 0),
    int(c.get('DFT', 0) or 0),
    int(c.get('IDLE', 0) or 0),
    int(c.get('STOP', 0) or 0),
    int(c.get('FLT', 0) or 0),
]
```


**`root/KpiTabs/PanelSections/SectionChartCard/SectionTempChart`**

- `props.series`: property `view.custom.metrics.sectionAvgs`, then script transform

Transform 1, script:

```python
d = list(value or [])
if not any(x is not None for x in d):
    return []
return [{'name': 'Avg F', 'data': d}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.sectionNames`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `props.options.colors`: expression, then script transform

```js
{session.props.theme}
```

Transform 1, script:

```python
t = str(value or 'light-cool')
if t == 'light-warm':
    c = '#C45C26'
elif t == 'dark-warm':
    c = '#E8894F'
elif t in ('dark', 'dark-cool'):
    c = '#53BAED'
else:
    c = '#114599'
return [c]
```


**`root/KpiTabs/PanelSections/SectionStatusCard/SectionStatusChart`**

- `props.series`: property `view.custom.metrics.sectionStatusSeries`, then script transform

Transform 1, script:

```python
return list(value or []) or [{'name': '', 'data': []}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.sectionNames`, then script transform

Transform 1, script:

```python
return list(value or [])
```


**`root/KpiTabs/PanelCGs/CgTable`**

- `props.data`: property `view.custom.metrics.cgs`

</details>

## Event Scripts And Handlers

- **`root/KpiTabs/PanelOverview/TempCard/TempChart`** `component.dataPointSelectionHandler`, script action, scope `G`

```python
cats = []
try:
    cats = list(self.view.custom.metrics.categories or [])
except:
    cats = []
idx = -1
try:
    idx = int(event.dataPointIndex)
except:
    try:
        idx = int(event['dataPointIndex'])
    except:
        idx = -1
if idx < 0 or idx >= len(cats):
    return
short = str(cats[idx] or '').strip()
if not short:
    return
cg = short if str(short).upper().startswith('CG-') else ('CG-' + short)
system.perspective.sendMessage(
    'UtilityOverviewHighlight',
    {'action': 'select', 'cg': cg, 'status': '', 'area': ''},
    scope='page'
)
```

- **`root/KpiTabs/PanelOverview/DwellCard/DwellTabs/PanelDwellStatus/DwellChartMain`** `component.dataPointSelectionHandler`, script action, scope `G`

```python
labels = ['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']
try:
    raw = self.view.custom.metrics.statusHrsMainCategories
    if raw:
        labels = list(raw)
except:
    pass
idx = -1
try:
    idx = int(event.dataPointIndex)
except:
    try:
        idx = int(event['dataPointIndex'])
    except:
        idx = -1
if idx < 0 or idx >= len(labels):
    return
system.perspective.sendMessage(
    'UtilityOverviewHighlight',
    {'action': 'statusToggle', 'status': str(labels[idx]), 'cg': '', 'area': ''},
    scope='page'
)
```

- **`root/KpiTabs/PanelOverview/DwellCard/DwellTabs/PanelDwellDefrost/DwellChartDft`** `component.dataPointSelectionHandler`, script action, scope `G`

```python
labels = ['DFT', 'DFT PD', 'DFT HG', 'DFT BLD', 'DFT FD']
try:
    raw = self.view.custom.metrics.statusHrsDftCategories
    if raw:
        labels = list(raw)
except:
    pass
idx = -1
try:
    idx = int(event.dataPointIndex)
except:
    try:
        idx = int(event['dataPointIndex'])
    except:
        idx = -1
if idx < 0 or idx >= len(labels):
    return
system.perspective.sendMessage(
    'UtilityOverviewHighlight',
    {'action': 'statusToggle', 'status': str(labels[idx]), 'cg': '', 'area': ''},
    scope='page'
)
```

- **`root/KpiTabs/PanelOverview/StatusCard/StatusChart`** `component.dataPointSelectionHandler`, script action, scope `G`

```python
labels = ['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']
idx = -1
try:
    idx = int(event.dataPointIndex)
except:
    try:
        idx = int(event['dataPointIndex'])
    except:
        idx = -1
if idx < 0 or idx >= len(labels):
    return
system.perspective.sendMessage(
    'UtilityOverviewHighlight',
    {'action': 'statusToggle', 'status': labels[idx], 'cg': ''},
    scope='page'
)
```

- **`root/KpiTabs/PanelOverview/StatusCard/StatusChart`** `component.legendClickHandler`, script action, scope `G`

```python
labels = ['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']
idx = -1
try:
    idx = int(event.seriesIndex)
except:
    try:
        idx = int(event['seriesIndex'])
    except:
        idx = -1
if idx < 0 or idx >= len(labels):
    return
system.perspective.sendMessage(
    'UtilityOverviewHighlight',
    {'action': 'statusToggle', 'status': labels[idx], 'cg': ''},
    scope='page'
)
```

- **`root/KpiTabs/PanelSections/SectionChartCard/SectionTempChart`** `component.dataPointSelectionHandler`, script action, scope `G`

```python
areas = []
try:
    areas = list(self.view.custom.metrics.sectionNames or [])
except:
    areas = []
idx = -1
try:
    idx = int(event.dataPointIndex)
except:
    try:
        idx = int(event['dataPointIndex'])
    except:
        idx = -1
if idx < 0 or idx >= len(areas):
    return
system.perspective.sendMessage(
    'UtilityOverviewHighlight',
    {'action': 'selectArea', 'area': str(areas[idx]), 'cg': '', 'status': ''},
    scope='page'
)
```

- **`root/KpiTabs/PanelSections/SectionStatusCard/SectionStatusChart`** `component.dataPointSelectionHandler`, script action, scope `G`

```python
series_names = ['CLG', 'DFT', 'IDLE', 'STOP', 'FLT']
areas = []
try:
    areas = list(self.view.custom.metrics.sectionNames or [])
except:
    areas = []
si = -1
di = -1
try:
    si = int(event.seriesIndex)
except:
    try:
        si = int(event['seriesIndex'])
    except:
        si = -1
try:
    di = int(event.dataPointIndex)
except:
    try:
        di = int(event['dataPointIndex'])
    except:
        di = -1
if si < 0 or si >= len(series_names) or di < 0 or di >= len(areas):
    return
system.perspective.sendMessage(
# ... 9 more line(s): see the view.json
```

- **`root/KpiTabs`** change script on `props.currentTabIndex`

```python
idx = -1
try:
    idx = int(currentValue.value)
except:
    try:
        idx = int(currentValue.value.value)
    except:
        idx = -1
# Per Control Group is tab index 2 — leaving it clears CG plant highlight
if idx != 2:
    system.perspective.sendMessage(
        'UtilityOverviewHighlight',
        {'action': 'clear', 'cg': '', 'status': ''},
        scope='page'
    )
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.UtilityMetrics](../../../../../../scripting/reference/modules/shared-utilitymetrics.md), [shared.UtilityMetrics.get](../../../../../../scripting/reference/modules/shared-utilitymetrics.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [03\_Elements/03\_Table/CgHit](../../../03-elements/03-table/cghit.md), [03\_Elements/03\_Table/DisplayTrend](../../../03-elements/03-table/displaytrend.md), [03\_Elements/03\_Table/Numeric](../../../03-elements/03-table/numeric.md)

**Embedded in** (1): [00\_Pages/Groveport/Utility/Overview](./overview.md)

## Style Classes

<details>
<summary>13 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 6 | style class |
| `Fonts/LiveDataEntry` | 1 | style class |
| `container-card` | 7 | stylesheet |
| `container-card-border` | 7 | stylesheet |
| `fs-15` | 1 | style class |
| `fs-16` | 6 | style class |
| `fw-600` | 6 | style class |
| `fw-700` | 1 | style class |
| `kpi-domain-tabs` | 2 | stylesheet |
| `psc-utility-kpi-table` | 1 | no rule found |
| `utility-dwell-chart` | 2 | stylesheet |
| `utility-kpi-chart` | 6 | stylesheet |
| `utility-kpi-rail` | 1 | stylesheet |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
