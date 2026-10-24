---
title: "OverviewClassic"
sidebar_label: "OverviewClassic"
description: "Perspective view 00_Pages/Groveport/Site/OverviewClassic (Page): 219 components, 43 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Site/OverviewClassic", "OverviewClassic", "/plants/groveport/classic"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Site/OverviewClassic`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Site/OverviewClassic` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Site/OverviewClassic/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Site &gt; OverviewClassic |
| Routes | `/plants/groveport/classic` (Groveport Classic Overview) |
| Root | `ia.container.flex`, width 1400, height 900 |
| Size | 219 components, 43 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T18:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagRoot` | `"[default]KPI/Groveport/Site"` | |

## Component Tree

Component types: ia.display.label x138, ia.container.flex x75, kyvislabs.display.apexchart x5, ia.container.tab x1.

<details>
<summary>Component tree (219 components)</summary>

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
        KwhChart  kyvislabs.display.apexchart
      EpmsMetering  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        Hint  ia.display.label
        Counts  ia.container.flex
          L  ia.display.label
          V  ia.display.label  [1 binding]
        MeterGrid  ia.container.flex
          ColA  ia.container.flex
            MeterFreezer  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
            MeterSuperChill  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
            MeterClub  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
            MeterPalletizing  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
          ColB  ia.container.flex
            MeterEastPH  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
            MeterWestPH  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
            MeterDock  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
            MeterMachineRoom  ia.container.flex
              Area  ia.display.label
              Status  ia.display.label  [1 binding]
              Kwh  ia.display.label  [1 binding]
              KwhUnit  ia.display.label
              Therm  ia.display.label  [1 binding]
              ThermUnit  ia.display.label
      EpmsYoy  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        YoyKwh  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
            Status  ia.display.label
          Chart  kyvislabs.display.apexchart
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
        TempChart  kyvislabs.display.apexchart
      UtilityYoy  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Status  ia.display.label
        YoyTherm  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
            Status  ia.display.label
          Chart  kyvislabs.display.apexchart
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
          Chart  kyvislabs.display.apexchart
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
              AvgVal  ia.display.label  [1 binding]
              AvgUnit  ia.display.label
            Baseline  ia.display.label  [1 binding]
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
              AvgVal  ia.display.label  [1 binding]
              AvgUnit  ia.display.label
            Baseline  ia.display.label  [1 binding]
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
        StatusTag  ia.display.label  [1 binding]
```

</details>

## Bindings

43 bindings: expr 43.

<details>
<summary>All 43 bindings, grouped by component</summary>

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
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringCoveragePct')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringCoveragePct')), null), 0), '0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/Counts/V`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringInstalledCount')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringInstalledCount')), null), 0), '0') + ' / ' + numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringPlannedCount')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/MeteringPlannedCount')), null), 8), '0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterFreezer/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Freezer' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Freezer' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterFreezer/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Freezer' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Freezer' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterFreezer/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Freezer' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Freezer' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterSuperChill/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/SuperChill' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/SuperChill' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterSuperChill/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/SuperChill' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/SuperChill' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterSuperChill/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/SuperChill' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/SuperChill' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterClub/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Club' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Club' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterClub/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Club' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Club' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterClub/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Club' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Club' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterPalletizing/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Palletizing' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Palletizing' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterPalletizing/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Palletizing' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Palletizing' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColA/MeterPalletizing/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Palletizing' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Palletizing' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterEastPH/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/East PH' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/East PH' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterEastPH/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/East PH' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/East PH' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterEastPH/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/East PH' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/East PH' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterWestPH/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/West PH' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/West PH' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterWestPH/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/West PH' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/West PH' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterWestPH/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/West PH' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/West PH' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterDock/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Dock' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Dock' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterDock/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Dock' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Dock' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterDock/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Dock' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Dock' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterMachineRoom/Status`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Machine Room' + '/Status')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Machine Room' + '/Status')), null), 'Planned')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterMachineRoom/Kwh`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Machine Room' + '/kWh')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Machine Room' + '/kWh')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelEPMS/EpmsMetering/MeterGrid/ColB/MeterMachineRoom/Therm`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Machine Room' + '/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/Metering/Machine Room' + '/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelUtility/Pens/PenTherm/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/Therm')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/Therm')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelUtility/Pens/PenH2O/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/H2O')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/H2O')), null), 0), '#,##0')
```


**`root/DomainTabs/PanelUtility/Pens/PenCO2/Row/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/CO2')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/Utility/CO2')), null), 0), '#,##0')
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


**`root/DomainTabs/PanelProduction/ProdLineBreak/Blocks/BlockCascade/AvgRow/AvgVal`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Cascade' + '/RestartAvgMin')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Cascade' + '/RestartAvgMin')), null), 0), '0.0')
```


**`root/DomainTabs/PanelProduction/ProdLineBreak/Blocks/BlockCascade/Baseline`**

- `props.text`: expression

```js
'Baseline: ' + coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Cascade' + '/BaselineMonth')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Cascade' + '/BaselineMonth')), null), '—')
```


**`root/DomainTabs/PanelProduction/ProdLineBreak/Blocks/BlockEneroi/AvgRow/AvgVal`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Eneroi' + '/RestartAvgMin')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Eneroi' + '/RestartAvgMin')), null), 0), '0.0')
```


**`root/DomainTabs/PanelProduction/ProdLineBreak/Blocks/BlockEneroi/Baseline`**

- `props.text`: expression

```js
'Baseline: ' + coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Eneroi' + '/BaselineMonth')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/LineBreak/Eneroi' + '/BaselineMonth')), null), '—')
```


**`root/DomainTabs/PanelProduction/ProdInnovative/StatusTag`**

- `props.text`: expression

```js
coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/InnovativeStatus')), null, tag(coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site') + '/ComingOnline/InnovativeStatus')), null), 'Future')
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Style Classes

<details>
<summary>24 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Heading` | 14 | stylesheet |
| `Fonts/Label` | 94 | style class |
| `Fonts/LiveDataEntry` | 30 | style class |
| `bg-page` | 1 | style class |
| `container-card` | 15 | stylesheet |
| `container-card-border` | 15 | stylesheet |
| `fs-11` | 27 | style class |
| `fs-12` | 20 | style class |
| `fs-13` | 63 | style class |
| `fs-14` | 5 | style class |
| `fs-15` | 9 | style class |
| `fs-20` | 2 | style class |
| `fs-22` | 12 | style class |
| `fw-600` | 43 | style class |
| `fw-700` | 1 | style class |
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

<details>
<summary>29 relative member paths</summary>

`/BaselineMonth`, `/ComingOnline/InnovativeStatus`, `/ComingOnline/LineBreak/Cascade`, `/ComingOnline/LineBreak/Eneroi`, `/ComingOnline/Metering/Club`, `/ComingOnline/Metering/Dock`, `/ComingOnline/Metering/East PH`, `/ComingOnline/Metering/Freezer`, `/ComingOnline/Metering/Machine Room`, `/ComingOnline/Metering/Palletizing`, `/ComingOnline/Metering/SuperChill`, `/ComingOnline/Metering/West PH`, `/ComingOnline/MeteringCoveragePct`, `/ComingOnline/MeteringInstalledCount`, `/ComingOnline/MeteringPlannedCount`, `/EPMS/Avg3Yr`, `/EPMS/Kvar`, `/EPMS/kWh`, `/Production/ProdVol`, `/Production/ProdVolAvg7d`, `/Production/kWhPerLb`, `/RestartAvgMin`, `/Status`, `/Therm`, `/Utility/AmbientAvgF`, `/Utility/CO2`, `/Utility/H2O`, `/Utility/Therm`, `/kWh`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
