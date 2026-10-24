---
title: "KPI"
sidebar_label: "KPI"
description: "Perspective view 02_Components/02_Widgets/KPI (Reusable component): 18 components, 14 bindings, 0 event scripts."
generated: true
keywords: ["02_Components/02_Widgets/KPI", "KPI"]
---

:::note

:::


**Reusable component**: `02_Components/02_Widgets/KPI`.

| | |
|---|---|
| View path | `02_Components/02_Widgets/KPI` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/02_Widgets/KPI/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 02\_Widgets &gt; KPI |
| Root | `ia.container.flex`, height 280, width 320 |
| Size | 18 components, 14 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T18:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `title` | `"Metric"` | input |
| `category` | `""` | input |
| `unit` | `""` | input |
| `tagPath` | `""` | input |
| `value` | `"—"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `liveNumeric` | `0` | bound (expr) |
| `spark` | `{"avg": "—", "max": "—", "min": "—", "series": []}` | bound (property) |

## Component Tree

Component types: ia.display.label x10, ia.container.flex x7, kyvislabs.display.apexchart x1.

<details>
<summary>Component tree (18 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    Category  ia.display.label  [2 bindings]
    Title  ia.display.label  [1 binding]
  ValueRow  ia.container.flex
    Value  ia.display.label  [1 binding]
    Unit  ia.display.label  [2 bindings]
  Chart  kyvislabs.display.apexchart  [1 binding]
  Metrics  ia.container.flex
    Min  ia.container.flex
      MinLabel  ia.display.label
      MinValue  ia.display.label  [1 binding]
    Max  ia.container.flex
      MaxLabel  ia.display.label
      MaxValue  ia.display.label  [1 binding]
    Avg  ia.container.flex
      AvgLabel  ia.display.label
      AvgValue  ia.display.label  [1 binding]
```

</details>

## Bindings

14 bindings: property 8, expr 6.

<details>
<summary>All 14 bindings, grouped by component</summary>

**`(view)`**

- `custom.liveNumeric`: expression

```js
if(len(coalesce({view.params.tagPath}, '')) > 0, coalesce(try(if(!isGood(tag({view.params.tagPath})), null, tag({view.params.tagPath})), null), 0), try(toFloat(replace(coalesce({view.params.value}, '0'), ',', '')), 0))
```


- `custom.spark`: property `view.custom.liveNumeric`, then script transform

Transform 1, script:

```python
# Real data only: no historian series is wired for the KPI widget (enterprise-only views): flat No Data.
return {'series': [], 'min': u'\u2014', 'max': u'\u2014', 'avg': u'\u2014'}
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/Header/Category`**

- `props.text`: property `view.params.category`

- `meta.visible`: expression

```js
len(coalesce({view.params.category}, '')) > 0
```


**`root/Header/Title`**

- `props.text`: property `view.params.title`

**`root/ValueRow/Value`**

- `props.text`: expression

```js
if(len(coalesce({view.params.tagPath}, '')) > 0, numberFormat(coalesce(try(if(!isGood(tag({view.params.tagPath})), null, tag({view.params.tagPath})), null), 0), '#,##0.#'), coalesce({view.params.value}, '—'))
```


**`root/ValueRow/Unit`**

- `props.text`: property `view.params.unit`

- `meta.visible`: expression

```js
len(coalesce({view.params.unit}, '')) > 0
```


**`root/Chart`**

- `props.series`: property `view.custom.spark.series`, then script transform

Transform 1, script:

```python
return list(value or [])
```


**`root/Metrics/Min/MinValue`**

- `props.text`: property `view.custom.spark.min`

**`root/Metrics/Max/MaxValue`**

- `props.text`: property `view.custom.spark.max`

**`root/Metrics/Avg/AvgValue`**

- `props.text`: property `view.custom.spark.avg`

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (3): [00\_Pages/Groveport/Domains/EPMS](../../00-pages/groveport/domains/epms.md), [00\_Pages/Groveport/Domains/Production](../../00-pages/groveport/domains/production.md), [00\_Pages/Groveport/Domains/Utility](../../00-pages/groveport/domains/utility.md)

## Style Classes

<details>
<summary>14 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 5 | style class |
| `Fonts/LiveDataEntry` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 3 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-13` | 3 | style class |
| `fw-600` | 3 | style class |
| `kpi-card` | 1 | stylesheet |
| `kpi-card-header` | 1 | stylesheet |
| `kpi-chart` | 1 | stylesheet |
| `kpi-metrics` | 1 | stylesheet |
| `kpi-value` | 1 | style class |
| `plant-feature-title` | 1 | style class |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
