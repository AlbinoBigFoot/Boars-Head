---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Site/Overview (Page): 235 components, 13 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Site/Overview", "Overview", "/plants/groveport"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Site/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Site/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Site/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Site &gt; Overview |
| Routes | `/plants/groveport` (Groveport Site Overview) |
| Root | `ia.container.flex`, width 1400, height 900 |
| Size | 235 components, 13 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T18:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagRoot` | `"[default]KPI/Groveport/Site"` | |

## Component Tree

Component types: ia.display.label x144, ia.container.flex x85, kyvislabs.display.apexchart x5, ia.container.tab x1.

<details>
<summary>Component tree (235 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  TitleBlock  ia.container.flex
    Title  ia.display.label
    Subtitle  ia.display.label
  DomainTabs  ia.container.tab
    PanelEPMS  ia.container.flex
      Sub  ia.display.label
      Pens  ia.container.flex
        PenKwh  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenKvar  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenAvg3  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenMeter  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
      CardKwh  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Sub  ia.display.label
        KwhChart  ia.container.flex
          KwhChartApex  kyvislabs.display.apexchart
      EpmsMetering  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        Hint  ia.display.label
        Counts  ia.container.flex
          L  ia.display.label
          V  ia.display.label
        MeterGrid  ia.container.flex
          ColA  ia.container.flex
            MeterFreezer  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
            MeterSuperChill  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
            MeterClub  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
            MeterPalletizing  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
          ColB  ia.container.flex
            MeterEastPH  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
            MeterWestPH  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
            MeterDock  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
            MeterMachineRoom  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label
              Kwh  ia.display.label
              KwhUnit  ia.display.label
              Therm  ia.display.label
              ThermUnit  ia.display.label
      EpmsYoy  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        YoyKwh  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
            Status  ia.display.label
          ChartShell  ia.container.flex
            ChartApex  kyvislabs.display.apexchart
    PanelUtility  ia.container.flex
      Sub  ia.display.label
      Pens  ia.container.flex
        PenTherm  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenH2O  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenCO2  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenTemp  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
      CardTemp  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Sub  ia.display.label
        TempChart  ia.container.flex
          TempChartApex  kyvislabs.display.apexchart
      UtilityYoy  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        YoyTherm  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
            Status  ia.display.label
          ChartShell  ia.container.flex
            ChartApex  kyvislabs.display.apexchart
    PanelProduction  ia.container.flex
      Sub  ia.display.label
      Pens  ia.container.flex
        PenProd  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenProd7d  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
        PenIntensity  ia.container.flex
          Lbl  ia.display.label
          Row  ia.container.flex
            Val  ia.display.label  [1 binding]
            Unit  ia.display.label
      ProdYoy  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        YoyProd  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
            Status  ia.display.label
          ChartShell  ia.container.flex
            ChartApex  kyvislabs.display.apexchart
      ProdLineBreak  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        Hint  ia.display.label
        Blocks  ia.container.flex
          BlockCascade  ia.container.flex
            Title  ia.display.label
            AvgRow  ia.container.flex
              AvgLbl  ia.display.label
              AvgVal  ia.display.label
              AvgUnit  ia.display.label
            Baseline  ia.display.label
            Ref  ia.display.label
            Row0  ia.container.flex
              Site  ia.display.label
              Month  ia.display.label
            Row1  ia.container.flex
              Site  ia.display.label
              Month  ia.display.label
            Row2  ia.container.flex
              Site  ia.display.label
              Month  ia.display.label
          BlockEneroi  ia.container.flex
            Title  ia.display.label
            AvgRow  ia.container.flex
              AvgLbl  ia.display.label
              AvgVal  ia.display.label
              AvgUnit  ia.display.label
            Baseline  ia.display.label
            Ref  ia.display.label
            Row0  ia.container.flex
              Site  ia.display.label
              Month  ia.display.label
            Row1  ia.container.flex
              Site  ia.display.label
              Month  ia.display.label
            Row2  ia.container.flex
              Site  ia.display.label
              Month  ia.display.label
      ProdInnovative  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        Body  ia.display.label
        InnovMetrics  ia.container.flex
          Init  ia.container.flex
            L  ia.display.label
            V  ia.display.label
          Sav  ia.container.flex
            L  ia.display.label
            Row  ia.container.flex
              V  ia.display.label
              U  ia.display.label
          Pilot  ia.container.flex
            L  ia.display.label
            V  ia.display.label
```

</details>

## Bindings

13 bindings: expr 13.

<details>
<summary>All 13 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/DomainTabs/PanelEPMS/Pens/PenKwh/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/EPMS/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/EPMS/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/Pens/PenKvar/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/EPMS/Kvar')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/EPMS/Kvar')), null), 0), '#,##0.0')
```


**`root/DomainTabs/PanelEPMS/Pens/PenAvg3/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/EPMS/Avg3Yr')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/EPMS/Avg3Yr')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/Pens/PenMeter/Row/Val`**

- `props.text`: expression

```js
'75'
```


**`root/DomainTabs/PanelUtility/Pens/PenTherm/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/Therm')), null), 28450), '#,##0')
```


**`root/DomainTabs/PanelUtility/Pens/PenH2O/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/H2O')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/H2O')), null), 1260), '#,##0')
```


**`root/DomainTabs/PanelUtility/Pens/PenCO2/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/CO2')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/CO2')), null), 41200), '#,##0')
```


**`root/DomainTabs/PanelUtility/Pens/PenTemp/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/AmbientAvgF')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/AmbientAvgF')), null), 0), '0')
```


**`root/DomainTabs/PanelProduction/Pens/PenProd/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/ProdVol')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/ProdVol')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelProduction/Pens/PenProd7d/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/ProdVolAvg7d')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/ProdVolAvg7d')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelProduction/Pens/PenIntensity/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/kWhPerLb')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Production/kWhPerLb')), null), 0), '0.0')
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Style Classes

<details>
<summary>25 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Heading` | 14 | stylesheet |
| `Fonts/Label` | 98 | style class |
| `Fonts/LiveDataEntry` | 32 | style class |
| `bg-page` | 1 | style class |
| `container-card` | 14 | stylesheet |
| `container-card-border` | 14 | stylesheet |
| `fs-11` | 30 | style class |
| `fs-12` | 20 | style class |
| `fs-13` | 63 | style class |
| `fs-14` | 6 | style class |
| `fs-15` | 9 | style class |
| `fs-20` | 2 | style class |
| `fs-22` | 14 | style class |
| `fw-600` | 46 | style class |
| `fw-700` | 1 | style class |
| `kpi-chart-shell` | 5 | stylesheet |
| `kpi-coming-chart` | 3 | stylesheet |
| `kpi-coming-meter-row` | 8 | stylesheet |
| `kpi-coming-subcard` | 2 | stylesheet |
| `kpi-dashboard-chart-card` | 2 | stylesheet |
| `kpi-dashboard-page` | 1 | stylesheet |
| `kpi-domain-panel` | 3 | stylesheet |
| `kpi-domain-subsection` | 6 | stylesheet |
| `kpi-domain-tabs` | 1 | stylesheet |
| `kpi-hero-pen` | 11 | stylesheet |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]KPI/Groveport/Site`

Member paths appended to a base path in expressions (relative):

`/EPMS/Avg3Yr`, `/EPMS/Kvar`, `/EPMS/kWh`, `/Production/ProdVol`, `/Production/ProdVolAvg7d`, `/Production/kWhPerLb`, `/Utility/AmbientAvgF`, `/Utility/CO2`, `/Utility/H2O`, `/Utility/Therm`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
