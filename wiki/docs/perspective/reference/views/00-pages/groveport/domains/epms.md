---
title: "EPMS"
sidebar_label: "EPMS"
description: "Perspective view 00_Pages/Groveport/Domains/EPMS (Page piece (not routed)): 31 components, 12 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Domains/EPMS", "EPMS"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Domains/EPMS`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Domains/EPMS` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Domains/EPMS/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Domains &gt; EPMS |
| Root | `ia.container.flex`, height 720, width 1200 |
| Size | 31 components, 12 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T18:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `area` | `"Freezer"` | input |

## Component Tree

Component types: ia.display.label x13, ia.container.flex x12, ia.display.view x5, ia.input.dropdown x1.

<details>
<summary>Component tree (31 components)</summary>

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
        Kvar  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
        Avg3  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
        Avg7  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [1 binding]
          Unit  ia.display.label
      Right  ia.container.flex
        PrimarySpark  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
  MetricGrid  ia.container.flex
    kWh  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    Kvar  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    Avg3  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
    Avg7  ia.display.view  [1 binding; view: 02_Components/02_Widgets/KPI]
```

</details>

## Bindings

12 bindings: expr 12.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/DomainCard/LabelTimeRange/CardTitle`**

- `props.text`: expression

```js
'EPMS — ' + coalesce({view.params.area}, 'Freezer')
```


**`root/DomainCard/Data/Left/Hero/HV/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/kWh')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/kWh')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/Kvar/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Kvar')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Kvar')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/Avg3/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Avg3Yr')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Avg3Yr')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Left/Avg7/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Avg7Yr')), null, tag('[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Avg7Yr')), null), 0), '#,##0.#')
```


**`root/DomainCard/Data/Right/PrimarySpark`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/kWh'
```


**`root/MetricGrid/kWh`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/kWh'
```


**`root/MetricGrid/Kvar`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Kvar'
```


**`root/MetricGrid/Avg3`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Avg3Yr'
```


**`root/MetricGrid/Avg7`**

- `props.params.tagPath`: expression

```js
'[default]KPI/Groveport/' + coalesce({view.params.area}, 'Freezer') + '/EPMS/Avg7Yr'
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
| `Fonts/Label` | 8 | style class |
| `Fonts/LiveDataEntry` | 4 | style class |
| `Fonts/Title` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 4 | style class |
| `fs-12` | 3 | style class |
| `fs-13` | 3 | style class |
| `fs-15` | 1 | style class |
| `fw-600` | 3 | style class |
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

`/EPMS/Avg3Yr`, `/EPMS/Avg7Yr`, `/EPMS/Kvar`, `/EPMS/kWh`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
