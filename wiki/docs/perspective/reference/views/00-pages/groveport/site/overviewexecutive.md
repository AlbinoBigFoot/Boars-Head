---
title: "OverviewExecutive"
sidebar_label: "OverviewExecutive"
description: "Perspective view 00_Pages/Groveport/Site/OverviewExecutive (Page): 227 components, 6 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Site/OverviewExecutive", "OverviewExecutive", "/plants/groveport/executive"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Site/OverviewExecutive`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Site/OverviewExecutive` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Site/OverviewExecutive/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Site &gt; OverviewExecutive |
| Routes | `/plants/groveport/executive` (Groveport Executive Overview) |
| Root | `ia.container.flex`, width 1400, height 900 |
| Size | 227 components, 6 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T18:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagRoot` | `"[default]KPI/Groveport/Site"` | |

## Component Tree

Component types: ia.display.label x155, ia.container.flex x67, kyvislabs.display.apexchart x3, ia.input.button x1, ia.container.tab x1.

<details>
<summary>Component tree (227 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    TitleRow  ia.container.flex
      Titles  ia.container.flex
        Title  ia.display.label
        Sub  ia.display.label
      HeaderActions  ia.container.flex
        Horizon  ia.display.label
        BtnClassic  ia.input.button  [1 event]
  Callout  ia.container.flex
    CallTitle  ia.display.label
    CallBody  ia.display.label
  KpiStrip  ia.container.flex
    StatGwh  ia.container.flex
      Lbl  ia.display.label
      Row  ia.container.flex
        Val  ia.display.label
        Unit  ia.display.label
      Hint  ia.display.label
    StatIntensity  ia.container.flex
      Lbl  ia.display.label
      Row  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
      Hint  ia.display.label
    StatTherm  ia.container.flex
      Lbl  ia.display.label
      Row  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
      Hint  ia.display.label
    StatProd  ia.container.flex
      Lbl  ia.display.label
      Row  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
      Hint  ia.display.label
    StatPf  ia.container.flex
      Lbl  ia.display.label
      Row  ia.container.flex
        Val  ia.display.label
        Unit  ia.display.label
      Hint  ia.display.label
    StatMeter  ia.container.flex
      Lbl  ia.display.label
      Row  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
      Hint  ia.display.label
  ExecTabs  ia.container.tab
    PanelExecutive  ia.container.flex
      CardPower  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Pill  ia.display.label
        Blurb  ia.display.label
        KwhChart  ia.container.flex
          KwhChartApex  kyvislabs.display.apexchart
      DualCharts  ia.container.flex
        WrapProd  ia.container.flex
          CardProd  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            Blurb  ia.display.label
            ProdChart  ia.container.flex
              ProdChartApex  kyvislabs.display.apexchart
        WrapTherm  ia.container.flex
          CardTherm  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            Blurb  ia.display.label
            ThermTempChart  ia.container.flex
              ThermTempChartApex  kyvislabs.display.apexchart
    PanelMatrix  ia.container.flex
      MatrixTitle  ia.display.label
      MatrixSub  ia.display.label
      CardTable  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
        TableHead  ia.container.flex
          H0  ia.display.label
          H1  ia.display.label
          H2  ia.display.label
          H3  ia.display.label
          H4  ia.display.label
          H5  ia.display.label
          H6  ia.display.label
          H7  ia.display.label
          H8  ia.display.label
          H9  ia.display.label
          H10  ia.display.label
        Site0  ia.container.flex
          C0  ia.display.label
          C1  ia.display.label
          C2  ia.display.label
          C3  ia.display.label
          C4  ia.display.label
          C5  ia.display.label
          C6  ia.display.label
          C7  ia.display.label
          C8  ia.display.label
          C9  ia.display.label
          C10  ia.display.label
        Site1  ia.container.flex
          C0  ia.display.label
          C1  ia.display.label
          C2  ia.display.label
          C3  ia.display.label
          C4  ia.display.label
          C5  ia.display.label
          C6  ia.display.label
          C7  ia.display.label
          C8  ia.display.label
          C9  ia.display.label
          C10  ia.display.label
        Site2  ia.container.flex
          C0  ia.display.label
          C1  ia.display.label
          C2  ia.display.label
          C3  ia.display.label
          C4  ia.display.label
          C5  ia.display.label
          C6  ia.display.label
          C7  ia.display.label
          C8  ia.display.label
          C9  ia.display.label
          C10  ia.display.label
        Site3  ia.container.flex
          C0  ia.display.label
          C1  ia.display.label
          C2  ia.display.label
          C3  ia.display.label
          C4  ia.display.label
          C5  ia.display.label
          C6  ia.display.label
          C7  ia.display.label
          C8  ia.display.label
          C9  ia.display.label
          C10  ia.display.label
        Site4  ia.container.flex
          C0  ia.display.label
          C1  ia.display.label
          C2  ia.display.label
          C3  ia.display.label
          C4  ia.display.label
          C5  ia.display.label
          C6  ia.display.label
          C7  ia.display.label
          C8  ia.display.label
          C9  ia.display.label
          C10  ia.display.label
        Site5  ia.container.flex
          C0  ia.display.label
          C1  ia.display.label
          C2  ia.display.label
          C3  ia.display.label
          C4  ia.display.label
          C5  ia.display.label
          C6  ia.display.label
          C7  ia.display.label
          C8  ia.display.label
          C9  ia.display.label
          C10  ia.display.label
        Site6  ia.container.flex
          C0  ia.display.label
          C1  ia.display.label
          C2  ia.display.label
          C3  ia.display.label
          C4  ia.display.label
          C5  ia.display.label
          C6  ia.display.label
          C7  ia.display.label
          C8  ia.display.label
          C9  ia.display.label
          C10  ia.display.label
      RestartProtocol  ia.container.flex
        WrapRestart  ia.container.flex
          CardRestart  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
            R1  ia.display.label
            R2  ia.display.label
            R3  ia.display.label
            R4  ia.display.label
            R5  ia.display.label
    PanelInnovations  ia.container.flex
      InnovTitle  ia.display.label
      InnovSub  ia.display.label
      InnovGrid  ia.container.flex
        Innov0  ia.container.flex
          CardInnov0  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            B  ia.display.label
        Innov1  ia.container.flex
          CardInnov1  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            B  ia.display.label
        Innov2  ia.container.flex
          CardInnov2  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            B  ia.display.label
        Innov3  ia.container.flex
          CardInnov3  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            B  ia.display.label
        Innov4  ia.container.flex
          CardInnov4  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            B  ia.display.label
        Innov5  ia.container.flex
          CardInnov5  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
              Pill  ia.display.label
            B  ia.display.label
```

</details>

## Bindings

6 bindings: expr 6.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/KpiStrip/StatIntensity/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/kWhPerLb')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/kWhPerLb')), null), 0), '0.000')
```


**`root/KpiStrip/StatTherm/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/Therm')), null), 0), '#,##0')
```


**`root/KpiStrip/StatProd/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/ProdVol')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/ProdVol')), null), 0), '#,##0')
```


**`root/KpiStrip/StatMeter/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringCoveragePct')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringCoveragePct')), null), 0), '0')
```


## Event Scripts And Handlers

- **`root/Header/TitleRow/HeaderActions/BtnClassic`** `component.onActionPerformed`, script action, scope `G`

```python
Navigation.Nav.navigate({'action': 'page', 'page': '/plants/groveport/classic'})
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Style Classes

<details>
<summary>21 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Heading` | 14 | stylesheet |
| `Fonts/Label` | 136 | style class |
| `Fonts/LiveDataEntry` | 6 | style class |
| `bg-page` | 1 | style class |
| `container-card` | 19 | stylesheet |
| `container-card-border` | 19 | stylesheet |
| `fs-11` | 26 | style class |
| `fs-12` | 99 | style class |
| `fs-13` | 11 | style class |
| `fs-15` | 11 | style class |
| `fs-16` | 2 | style class |
| `fs-20` | 7 | style class |
| `fw-400` | 66 | style class |
| `fw-600` | 23 | style class |
| `fw-700` | 21 | style class |
| `kpi-dashboard-page` | 1 | stylesheet |
| `kpi-domain-tabs` | 1 | stylesheet |
| `kpi-exec-callout` | 1 | stylesheet |
| `kpi-exec-chart` | 3 | stylesheet |
| `kpi-exec-page` | 1 | stylesheet |
| `kpi-exec-stat` | 6 | stylesheet |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]KPI/Groveport/Site`

Member paths appended to a base path in expressions (relative):

`/ComingOnline/MeteringCoveragePct`, `/Production/ProdVol`, `/Production/kWhPerLb`, `/Utility/Therm`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
