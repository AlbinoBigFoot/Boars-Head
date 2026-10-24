---
title: "Production"
sidebar_label: "Production"
description: "Perspective view 00_Pages/Groveport/Domains/Production (Page piece (not routed)): 26 components, 10 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Domains/Production", "Production"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Domains/Production`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Domains/Production` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Domains/Production/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Domains &gt; Production |
| Root | `ia.container.flex`, height 720, width 1200 |
| Size | 26 components, 10 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T18:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `area` | `"Freezer"` | input |

## Component Tree

Component types: ia.container.flex x11, ia.display.label x10, ia.display.view x4, ia.input.dropdown x1.

<details>
<summary>Component tree (26 components)</summary>

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
        Avg7d  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
        Intensity  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
      Right  ia.container.flex
        PrimarySpark  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
  MetricGrid  ia.container.flex
    ProdVol  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    Avg7d  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    Intensity  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
```

</details>

## Bindings

10 bindings: expr 10.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/DomainCard/LabelTimeRange/CardTitle`**

- `props.text`: expression

```js
'Production — ' + coalesce({view.params.area}, 'Freezer')
```


**`root/DomainCard/Data/Left/Hero/HV/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/ProdVol')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/ProdVol')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/Avg7d/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/ProdVolAvg7d')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/ProdVolAvg7d')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/Intensity/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/kWhPerLb')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/kWhPerLb')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Right/PrimarySpark`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/ProdVol'
```


**`root/MetricGrid/ProdVol`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/ProdVol'
```


**`root/MetricGrid/Avg7d`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/ProdVolAvg7d'
```


**`root/MetricGrid/Intensity`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/Production/kWhPerLb'
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [02\_Components/02\_Widgets/KPI](../../../02-components/02-widgets/kpi.md)

**Opened or named by** (1): [00\_Pages/Groveport/Area/DomainKpis](../area/domainkpis.md)

## Style Classes

<details>
<summary>15 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 6 | style class |
| `Fonts/LiveDataEntry` | 3 | style class |
| `Fonts/Title` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 3 | style class |
| `fs-12` | 2 | style class |
| `fs-13` | 2 | style class |
| `fs-15` | 1 | style class |
| `fw-600` | 2 | style class |
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

`/Production/ProdVol`, `/Production/ProdVolAvg7d`, `/Production/kWhPerLb`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
