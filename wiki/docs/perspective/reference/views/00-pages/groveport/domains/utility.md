---
title: "Utility"
sidebar_label: "Utility"
description: "Perspective view 00_Pages/Groveport/Domains/Utility (Page piece (not routed)): 36 components, 14 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Domains/Utility", "Utility"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Domains/Utility`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Domains/Utility` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Domains/Utility/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Domains &gt; Utility |
| Root | `ia.container.flex`, height 720, width 1200 |
| Size | 36 components, 14 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T18:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `area` | `"Freezer"` | input |

## Component Tree

Component types: ia.display.label x16, ia.container.flex x13, ia.display.view x6, ia.input.dropdown x1.

<details>
<summary>Component tree (36 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  DomainCard  ia.container.flex
    LabelTimeRange  ia.container.flex
      CardTitle  ia.display.label  [1 binding]
      timeRange  ia.input.dropdown
    Data  ia.container.flex
      Left  ia.container.flex
        Hero  ia.container.flex
          HL  ia.display.label
          HV  ia.container.flex
            Val  ia.display.label  [1 binding]
            U  ia.display.label
        H2O  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
        CO2  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
        AmbAvg  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
        AmbMax  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
      Right  ia.container.flex
        PrimarySpark  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
  MetricGrid  ia.container.flex
    Therm  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    H2O  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    CO2  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    AmbAvg  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    AmbMax  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
```

</details>

## Bindings

14 bindings: expr 14.

<details>
<summary>All 14 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/DomainCard/LabelTimeRange/CardTitle`**

- `props.text`: expression

```js
'Utility — ' + coalesce({view.params.area}, 'Freezer')
```


**`root/DomainCard/Data/Left/Hero/HV/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/Therm')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/Therm')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/H2O/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/H2O')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/H2O')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/CO2/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/CO2')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/CO2')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/AmbAvg/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/AmbientAvgF')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/AmbientAvgF')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/AmbMax/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/AmbientMaxF')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/AmbientMaxF')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Right/PrimarySpark`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/Therm'
```


**`root/MetricGrid/Therm`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/Therm'
```


**`root/MetricGrid/H2O`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/H2O'
```


**`root/MetricGrid/CO2`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/CO2'
```


**`root/MetricGrid/AmbAvg`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/AmbientAvgF'
```


**`root/MetricGrid/AmbMax`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Utility/AmbientMaxF'
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [02\_Components/02\_Widgets/KPI](../../../02-components/02-widgets/kpi.md)

## Style Classes

<details>
<summary>15 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 10 | style class |
| `Fonts/LiveDataEntry` | 5 | style class |
| `Fonts/Title` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 5 | style class |
| `fs-12` | 4 | style class |
| `fs-13` | 4 | style class |
| `fs-15` | 1 | style class |
| `fw-600` | 4 | style class |
| `fw-700` | 1 | style class |
| `kpi-dashboard-grid` | 1 | stylesheet |
| `kpi-dashboard-page` | 1 | stylesheet |
| `kpi-value` | 1 | style class |
| `overview-card` | 1 | stylesheet |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]KPI/Groveport/`

Member paths appended to a base path in expressions (relative):

`/Utility/AmbientAvgF`, `/Utility/AmbientMaxF`, `/Utility/CO2`, `/Utility/H2O`, `/Utility/Therm`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
