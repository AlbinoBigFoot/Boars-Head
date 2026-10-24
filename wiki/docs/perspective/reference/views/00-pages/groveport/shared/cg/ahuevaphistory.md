---
title: "AhuEvapHistory"
sidebar_label: "AhuEvapHistory"
description: "Perspective view 00_Pages/Groveport/_Shared/CG/AhuEvapHistory (Page piece (not routed)): 13 components, 10 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/_Shared/CG/AhuEvapHistory", "AhuEvapHistory"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/_Shared/CG/AhuEvapHistory`.

| | |
|---|---|
| View path | `00_Pages/Groveport/_Shared/CG/AhuEvapHistory` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/_Shared/CG/AhuEvapHistory/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; \_Shared &gt; CG &gt; AhuEvapHistory |
| Root | `ia.container.flex`, width 487, height 1057 |
| Size | 13 components, 10 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-01T06:57:41Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `payload` | `{"rows": [], "series": [], "statusHrsDft": [0, 0, 0, 0, 0], "status...` | bound (expr-struct) |
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x5, ia.display.label x3, kyvislabs.display.apexchart x3, ia.container.tab x1, ia.display.table x1.

<details>
<summary>Component tree (13 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  ZatCard  ia.container.flex
    Title  ia.display.label
    ZatChart  kyvislabs.display.apexchart  [1 binding]
  DwellCard  ia.container.flex
    DwellTabs  ia.container.tab
      PanelDwellStatus  ia.container.flex
        DwellTitle  ia.display.label
        DwellChartMain  kyvislabs.display.apexchart  [2 bindings]
      PanelDwellDefrost  ia.container.flex
        DwellDftTitle  ia.display.label
        DwellChartDft  kyvislabs.display.apexchart  [2 bindings]
  Summary  ia.display.table  [1 binding]
```

</details>

## Bindings

10 bindings: property 5, expr 3, expr-struct 2.

**`(view)`**

- `custom.payload`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
tick: now(60000)
```

waitOnAll: `True`

Transform 1, script:

```python
out = {'series': [], 'statusHrsMainCategories': ['CLG', 'DFT', 'IDLE', 'STOP', 'FLT'],
    'statusHrsMain': [0, 0, 0, 0, 0], 'statusHrsDftCategories': ['DFT', 'DFT PD', 'DFT HG', 'DFT BLD', 'DFT FD'],
    'statusHrsDft': [0, 0, 0, 0, 0], 'rows': []}
try:
    tagPath = str(value.get('tagPath') or '').strip()
except:
    tagPath = ''
if not tagPath:
    return out
try:
    return shared.UtilityMetrics.cg(tagPath, 12)
except:
    return out
```


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/ZatCard/ZatChart`**

- `props.series`: structured expression (expr-struct), then script transform

```js
payload: {view.custom.payload}
```

waitOnAll: `True`

Transform 1, script:

```python
p = value.get('payload') if hasattr(value, 'get') else None
if not p:
    return []
out = []
for item in (p.get('series') or []):
    data = item.get('data')
    if isinstance(data, (list, tuple)) or hasattr(data, '__len__') and not hasattr(data, 'getRowCount'):
        pts = [[a[0], a[1]] for a in data if a is not None and len(a) >= 2]
        if pts:
            out.append({'name': item.get('name', 'Zone Air Temp'), 'data': pts})
        continue
    try:
        cols = list(data.getColumnNames())
    except:
        continue
    t_idx = cols.index('t_stamp') if 't_stamp' in cols else 0
    v_idx = cols.index('Temp') if 'Temp' in cols else (1 if len(cols) > 1 else -1)
    if v_idx < 0:
        continue
    pts = []
    for r in range(data.getRowCount()):
        ts = data.getValueAt(r, t_idx)
        v = data.getValueAt(r, v_idx)
        if ts is None or v is None:
            continue
        try:
            pts.append([system.date.toMillis(ts), round(float(v), 2)])
        except:
            pass
    if pts:
        out.append({'name': item.get('name', 'Zone Air Temp'), 'data': pts})
return out
```


**`root/DwellCard/DwellTabs/PanelDwellStatus/DwellChartMain`**

- `props.options.xaxis.categories`: property `view.custom.payload.statusHrsMainCategories`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `props.series`: property `view.custom.payload.statusHrsMain`, then script transform

Transform 1, script:

```python
d = list(value or [])
if not any(x for x in d if x):
    return []
while len(d) < 5:
    d.append(0)
return [{'name': 'Hours', 'data': d[:5]}]
```


**`root/DwellCard/DwellTabs/PanelDwellDefrost/DwellChartDft`**

- `props.options.xaxis.categories`: property `view.custom.payload.statusHrsDftCategories`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `props.series`: property `view.custom.payload.statusHrsDft`, then script transform

Transform 1, script:

```python
d = list(value or [])
if not any(x for x in d if x):
    return []
while len(d) < 5:
    d.append(0)
return [{'name': 'Hours', 'data': d[:5]}]
```


**`root/Summary`**

- `props.data`: property `view.custom.payload.rows`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.UtilityMetrics.cg](../../../../../../../scripting/reference/modules/shared-utilitymetrics.md).

## Related Views

**Embedded in** (1): [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./ahuevapdisplay.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `Fonts/Title` | 1 | style class |
| `ahu-evap-history-card` | 2 | stylesheet |
| `container-card` | 2 | stylesheet |
| `container-card-border` | 2 | stylesheet |
| `fs-14` | 2 | style class |
| `fw-600` | 2 | style class |
| `kpi-domain-tabs` | 1 | stylesheet |
| `plant-feature-title` | 1 | style class |
| `utility-dwell-chart` | 2 | stylesheet |
| `utility-kpi-chart` | 2 | stylesheet |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
