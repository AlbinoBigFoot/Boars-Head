---
title: "Kpis"
sidebar_label: "Kpis"
description: "Perspective view 00_Pages/Groveport/Production/Level3/Kpis (Page piece (not routed)): 23 components, 12 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Production/Level3/Kpis", "Kpis"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Production/Level3/Kpis`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Production/Level3/Kpis` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Production/Level3/Kpis/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Production &gt; Level3 &gt; Kpis |
| Root | `ia.container.flex`, height 1016, width 500 |
| Size | 23 components, 12 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-13T19:59:06Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `unitId` | `"VD"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `metrics` | `{}` | bound (expr-struct) |

## Component Tree

Component types: ia.display.label x14, ia.container.flex x8, kyvislabs.display.apexchart x1.

<details>
<summary>Component tree (23 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  RailTitle  ia.display.label  [1 binding]
  KpiGrid  ia.container.flex
    RunStatus  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
    Rate  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
    OEE  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
    Alarms  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
    Reject  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
    RunHrs  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
  TrendTitle  ia.display.label
  UnitTrend  kyvislabs.display.apexchart  [2 bindings]
```

</details>

## Bindings

12 bindings: expr 7, property 4, expr-struct 1.

**`(view)`**

- `custom.metrics`: structured expression (expr-struct), then script + expression transform

```js
tick: now(60000)
unitId: {view.params.unitId}
U_Rate: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Rate/Value')), false), false), try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Rate/Value')), null), null)
U_OEE: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/OEE/Value')), false), false), try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/OEE/Value')), null), null)
U_Reject: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Reject/Value')), false), false), try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Reject/Value')), null), null)
U_Status: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Status/Value')), false), false), try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Status/Value')), null), null)
```

waitOnAll: `True`

Transform 1, script:

```python

# the custom report engine shared.Reports uses the same functions)
return shared.ProductionMetrics.l3(value)
```

Transform 2, expression:

```js
if((coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Rate/Value')), false), false) || coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/OEE/Value')), false), false) || coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Reject/Value')), false), false) || coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/' + {view.params.unitId} + '/Status/Value')), false), false)), {value}, null)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/RailTitle`**

- `props.text`: property `view.custom.metrics.unitName`

**`root/KpiGrid/RunStatus/Value`**

- `props.text`: property `view.custom.metrics.runStatus`

**`root/KpiGrid/Rate/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.rate}, 0), '#,##0') + ' lb/hr'
```


**`root/KpiGrid/OEE/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.oee}, 0), '#,##0') + ' %'
```


**`root/KpiGrid/Alarms/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.alarms}, 0), '#,##0')
```


**`root/KpiGrid/Reject/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.rejectPct}, 0), '#,##0') + ' %'
```


**`root/KpiGrid/RunHrs/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.runHours}, 0), '#,##0') + ' hr'
```


**`root/UnitTrend`**

- `props.series`: property `view.custom.metrics.unitTrend`, then script transform

Transform 1, script:

```python
d = list(value or [])
return [{'name': 'Rate', 'data': d}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.unitTrendLabels`, then script transform

Transform 1, script:

```python
return list(value or [])
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.ProductionMetrics.l3](../../../../../../../scripting/reference/modules/shared-productionmetrics.md), [shared.Reports](../../../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Embedded in** (7): [00\_Pages/Groveport/Production/Level3/Handtman](./handtman.md), [00\_Pages/Groveport/Production/Level3/Hopper](./hopper.md), [00\_Pages/Groveport/Production/Level3/LazySusan](./lazysusan.md), [00\_Pages/Groveport/Production/Level3/Loaders](./loaders.md), [00\_Pages/Groveport/Production/Level3/RollStock](./rollstock.md), [00\_Pages/Groveport/Production/Level3/ShrinkTunnel](./shrinktunnel.md), [00\_Pages/Groveport/Production/Level3/VatDumper](./vatdumper.md)

## Style Classes

<details>
<summary>13 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 7 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 6 | style class |
| `container-card` | 7 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 7 | style class |
| `fs-14` | 1 | style class |
| `fs-20` | 6 | style class |
| `fw-600` | 7 | style class |
| `fw-700` | 7 | style class |
| `text-muted` | 6 | style class |
| `utility-kpi-chart` | 1 | stylesheet |
| `utility-kpi-rail` | 1 | stylesheet |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]Boars_Head/GrovePort/Production/FCM/`

Member paths appended to a base path in expressions (relative):

`/OEE/Value`, `/Rate/Value`, `/Reject/Value`, `/Status/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
