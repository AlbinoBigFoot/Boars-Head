---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Production/Level1/Overview (Page): 149 components, 110 bindings, 38 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Production/Level1/Overview", "Overview", "/plants/groveport/production-overview"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Production/Level1/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Production/Level1/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Production/Level1/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Production &gt; Level1 &gt; Overview |
| Routes | `/plants/groveport/production-overview` (Groveport Production Overview) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 149 components, 110 bindings, 38 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-13T20:26:59Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `metrics` | `{}` | bound (expr-struct) |
| `selectedUnit` | `""` | |
| `selectedUnitName` | `""` | |
| `dayOffset` | `0` | |
| `shiftSel` | `""` | |
| `dtMode` | `"pareto"` | |
| `dtDetail` | `""` | |

## Component Tree

Component types: ia.display.label x84, ia.container.flex x47, ia.display.table x9, kyvislabs.display.apexchart x5, ia.container.coord x1, ia.input.dropdown x1, ia.input.button x1, ia.display.icon x1.

<details>
<summary>Component tree (149 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Draw  ia.container.coord  [1 binding]
    Title  ia.display.label  [1 binding]
    BackToLine  ia.container.flex  [1 binding; 1 event]
      BackLbl  ia.display.label
    DaySelector  ia.input.dropdown  [1 binding]
    GenerateReport  ia.input.button  [1 binding; 1 event]
    ShiftTab_ALL  ia.container.flex  [2 bindings; 1 event]
      Lbl  ia.display.label  [1 binding]
    ShiftTab_A  ia.container.flex  [2 bindings; 1 event]
      Lbl  ia.display.label  [1 binding]
    ShiftTab_B  ia.container.flex  [2 bindings; 1 event]
      Lbl  ia.display.label  [1 binding]
    ShiftTab_C  ia.container.flex  [2 bindings; 1 event]
      Lbl  ia.display.label  [1 binding]
    LineBanner  ia.container.flex
      Banner_0  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_1  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_2  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_3  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_4  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_5  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_6  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_7  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_8  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_9  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
      Banner_10  ia.container.flex
        L  ia.display.label
        V  ia.display.label  [1 binding]
    ZoneBand_Prep  ia.container.flex
      ZoneLabel  ia.display.label
      ZoneStat  ia.display.label  [1 binding]
    ZoneBand_Forming  ia.container.flex
      ZoneLabel  ia.display.label
      ZoneStat  ia.display.label  [1 binding]
    ZoneBand_Packaging  ia.container.flex
      ZoneLabel  ia.display.label
      ZoneStat  ia.display.label  [1 binding]
    Arrow_0  ia.display.label
    Arrow_1  ia.display.label
    Arrow_2  ia.display.label
    Arrow_3  ia.display.label
    Arrow_4  ia.display.label
    Arrow_5  ia.display.label
    VD  ia.container.flex  [1 binding; 2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    HOP  ia.container.flex  [1 binding; 2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    HND  ia.container.flex  [1 binding; 2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    LDR  ia.container.flex  [1 binding; 2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    RSM  ia.container.flex  [1 binding; 2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    ST  ia.container.flex  [1 binding; 2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    LS  ia.container.flex  [1 binding; 2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    CardOee  ia.container.flex
      CardTitle  ia.display.label
      OeeChart  kyvislabs.display.apexchart  [2 bindings]
    CardRateTrend  ia.container.flex
      CardTitle  ia.display.label
      RateTrend  kyvislabs.display.apexchart  [1 binding]
    CardPareto  ia.container.flex
      DtHeader  ia.container.flex
        CardTitle  ia.display.label  [1 binding]
        DtBack  ia.container.flex  [3 bindings; 1 event]
          Lbl  ia.display.label  [1 binding]
        DtTabs  ia.container.flex  [1 binding]
          TabPareto  ia.container.flex  [2 bindings; 1 event]
            Lbl  ia.display.label  [1 binding]
          TabTrend  ia.container.flex  [2 bindings; 1 event]
            Lbl  ia.display.label  [1 binding]
      DtBody  ia.container.flex
        ParetoChart  kyvislabs.display.apexchart  [3 bindings; 1 event]
        DtTimeSeries  kyvislabs.display.apexchart  [2 bindings]
        DtDetailTable  ia.display.table  [2 bindings]
    CardTis  ia.container.flex
      CardTitle  ia.display.label
      TisChart  kyvislabs.display.apexchart  [1 binding]
    CardZone  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      ZoneTable  ia.display.table  [1 binding]
    CardEquip  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      UnitTable  ia.display.table  [1 binding]
    CardAlarms  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      AlarmTable  ia.display.table  [1 binding]
    CardAlarmSummary  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      AlarmSummaryTable  ia.display.table  [1 binding]
    CardSignals  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      SignalTable  ia.display.table  [1 binding]
    CardShifts  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      ShiftTable  ia.display.table  [1 binding]
    CardDevAlarms  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      DevAlarmTable  ia.display.table  [1 binding]
    CardDevAlarmSummary  ia.container.flex  [1 binding]
      CardTitle  ia.display.label
      DevAlarmSummaryTable  ia.display.table  [1 binding]
    ShiftPendingOverlay  ia.container.flex  [1 binding]
      PendingIcon  ia.display.icon
      PendingNote  ia.display.label  [1 binding]
```

</details>

## Bindings

110 bindings: expr 91, property 17, expr-struct 2.

<details>
<summary>All 110 bindings, grouped by component</summary>

**`(view)`**

- `custom.metrics`: structured expression (expr-struct), then script transform

```js
tick: now(60000)
sel: {view.custom.selectedUnit}
day: {view.custom.dayOffset}
shift: {view.custom.shiftSel}
dtRe: {view.custom.dtDetail}
L_Rate: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Rate/Value')), null)
L_Availability: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Availability/Value')), null)
L_Performance: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Performance/Value')), null)
L_Quality: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Quality/Value')), null)
L_Yield: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Yield/Value')), null)
L_Reject: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Reject/Value')), null)
L_Uptime: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Uptime/Value')), null)
L_Cases: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Line/Cases/Value')), null)
Z_Prep_Rate: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/Prep/Rate/Value')), null)
Z_Prep_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/Prep/OEE/Value')), null)
Z_Forming_Rate: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/Forming/Rate/Value')), null)
Z_Forming_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/Forming/OEE/Value')), null)
Z_Packaging_Rate: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/Packaging/Rate/Value')), null)
Z_Packaging_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/Packaging/OEE/Value')), null)
U_VD_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/OEE/Value')), null)
U_VD_Reject: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Reject/Value')), null)
U_VD_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), null)
U_HOP_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/OEE/Value')), null)
U_HOP_Reject: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Reject/Value')), null)
U_HOP_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), null)
U_HND_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/OEE/Value')), null)
U_HND_Reject: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Reject/Value')), null)
U_HND_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value')), null)
U_LDR_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/OEE/Value')), null)
U_LDR_Reject: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Reject/Value')), null)
U_LDR_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value')), null)
U_RSM_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/OEE/Value')), null)
U_RSM_Reject: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Reje
// ... truncated (3709 characters in total): see the view.json
```

waitOnAll: `True`

Transform 1, script:

```python

# the custom report engine shared.Reports uses the same functions)
return shared.ProductionMetrics.l1(value)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Draw`**

- `props.style.transform`: structured expression (expr-struct), then script transform

```js
scale: {view.params.Scale}
defaultViewHeight: {view.props.defaultSize.height}
defaultViewWidth: {view.props.defaultSize.width}
primaryViewHeight: {page.props.dimensions.primaryView.height}
primaryViewWidth: {page.props.dimensions.primaryView.width}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.Scale.cssTransform(value)
```


**`root/Draw/Title`**

- `props.text`: expression

```js
coalesce({view.custom.metrics.scopeName}, 'FCM Chipotle Chicken Line')
```


**`root/Draw/BackToLine`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') != '', 'flex', 'none')
```


**`root/Draw/DaySelector`**

- `props.value`: property `view.custom.dayOffset` (bidirectional)

**`root/Draw/GenerateReport`**

- `props.enabled`: expression

```js
coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/Draw/ShiftTab_ALL`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = '', '#1E88E5', 'var(--surface-card)')
```


- `props.style.borderColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = '', '#1E88E5', 'var(--border)')
```


**`root/Draw/ShiftTab_ALL/Lbl`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = '', '#ffffff', 'var(--neutral-90)')
```


**`root/Draw/ShiftTab_A`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'A', '#1E88E5', 'var(--surface-card)')
```


- `props.style.borderColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'A', '#1E88E5', 'var(--border)')
```


**`root/Draw/ShiftTab_A/Lbl`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'A', '#ffffff', 'var(--neutral-90)')
```


**`root/Draw/ShiftTab_B`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'B', '#1E88E5', 'var(--surface-card)')
```


- `props.style.borderColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'B', '#1E88E5', 'var(--border)')
```


**`root/Draw/ShiftTab_B/Lbl`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'B', '#ffffff', 'var(--neutral-90)')
```


**`root/Draw/ShiftTab_C`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'C', '#1E88E5', 'var(--surface-card)')
```


- `props.style.borderColor`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'C', '#1E88E5', 'var(--border)')
```


**`root/Draw/ShiftTab_C/Lbl`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.shiftSel}, '') = 'C', '#ffffff', 'var(--neutral-90)')
```


**`root/Draw/LineBanner/Banner_0/V`**

- `props.text`: expression

```js
'●  ' + coalesce({view.custom.metrics.lineState}, '--')
```


**`root/Draw/LineBanner/Banner_1/V`**

- `props.text`: expression

```js
'Shift ' + coalesce({view.custom.metrics.shift}, '--')
```


**`root/Draw/LineBanner/Banner_2/V`**

- `props.text`: expression

```js
coalesce({view.custom.metrics.runTime}, '--')
```


**`root/Draw/LineBanner/Banner_3/V`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.lineRate}, 0), '#,##0') + ' lb/hr'
```


**`root/Draw/LineBanner/Banner_4/V`**

- `props.text`: expression

```js
if({view.custom.metrics.rateVsTarget} >= 0, '+', '') + numberFormat(coalesce({view.custom.metrics.rateVsTarget}, 0), '#,##0.0') + '%'
```


**`root/Draw/LineBanner/Banner_5/V`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.oee}, 0), '#,##0.0') + '%'
```


**`root/Draw/LineBanner/Banner_6/V`**

- `props.text`: expression

```js
coalesce({view.custom.metrics.throughputLabel}, '--')
```


**`root/Draw/LineBanner/Banner_7/V`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.yieldPct}, 0), '#,##0.0') + '%'
```


**`root/Draw/LineBanner/Banner_8/V`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.rejectPct}, 0), '#,##0.00') + '%'
```


**`root/Draw/LineBanner/Banner_9/V`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.uptimePct}, 0), '#,##0.0') + '%'
```


**`root/Draw/LineBanner/Banner_10/V`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.activeAlarms}, 0), '#,##0')
```


**`root/Draw/ZoneBand_Prep/ZoneStat`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.zoneRateSeries[0]}, 0), '#,##0') + ' lb/hr   •   OEE ' + numberFormat(coalesce({view.custom.metrics.zoneOeeSeries[0]}, 0), '#,##0.0') + '%'
```


**`root/Draw/ZoneBand_Forming/ZoneStat`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.zoneRateSeries[1]}, 0), '#,##0') + ' lb/hr   •   OEE ' + numberFormat(coalesce({view.custom.metrics.zoneOeeSeries[1]}, 0), '#,##0.0') + '%'
```


**`root/Draw/ZoneBand_Packaging/ZoneStat`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.zoneRateSeries[2]}, 0), '#,##0') + ' lb/hr   •   OEE ' + numberFormat(coalesce({view.custom.metrics.zoneOeeSeries[2]}, 0), '#,##0.0') + '%'
```


**`root/Draw/VD`**

- `props.style.outline`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = 'VD', '2px solid var(--cta)', '1px solid var(--border)')
```


**`root/Draw/VD/Sub`**

- `position.display`: expression

```js
'' != ''
```


**`root/Draw/VD/RunStatus`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.VD.OEE}, 0), '#,##0.0') + '%')
```


- `props.style.color`: expression

```js
if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.VD.OEE}, 0), '#,##0.0') + '%')) = 'Fault', '#C62828', if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.VD.OEE}, 0), '#,##0.0') + '%')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/VD/Rate`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value'), 90), '#,##0')) + ' lb/hr', numberFormat(coalesce({view.custom.metrics.unitById.VD.Rate}, 0), '#,##0') + ' lb/hr')
```


**`root/Draw/HOP`**

- `props.style.outline`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = 'HOP', '2px solid var(--cta)', '1px solid var(--border)')
```


**`root/Draw/HOP/Sub`**

- `position.display`: expression

```js
'' != ''
```


**`root/Draw/HOP/RunStatus`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.HOP.OEE}, 0), '#,##0.0') + '%')
```


- `props.style.color`: expression

```js
if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.HOP.OEE}, 0), '#,##0.0') + '%')) = 'Fault', '#C62828', if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.HOP.OEE}, 0), '#,##0.0') + '%')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/HOP/Rate`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value'), 97), '#,##0')) + ' lb/hr', numberFormat(coalesce({view.custom.metrics.unitById.HOP.Rate}, 0), '#,##0') + ' lb/hr')
```


**`root/Draw/HND`**

- `props.style.outline`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = 'HND', '2px solid var(--cta)', '1px solid var(--border)')
```


**`root/Draw/HND/Sub`**

- `position.display`: expression

```js
'' != ''
```


**`root/Draw/HND/RunStatus`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.HND.OEE}, 0), '#,##0.0') + '%')
```


- `props.style.color`: expression

```js
if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.HND.OEE}, 0), '#,##0.0') + '%')) = 'Fault', '#C62828', if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.HND.OEE}, 0), '#,##0.0') + '%')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/HND/Rate`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Rate/Value'), 83), '#,##0')) + ' lb/hr', numberFormat(coalesce({view.custom.metrics.unitById.HND.Rate}, 0), '#,##0') + ' lb/hr')
```


**`root/Draw/LDR`**

- `props.style.outline`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = 'LDR', '2px solid var(--cta)', '1px solid var(--border)')
```


**`root/Draw/LDR/Sub`**

- `position.display`: expression

```js
'Net Applied' != ''
```


**`root/Draw/LDR/RunStatus`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.LDR.OEE}, 0), '#,##0.0') + '%')
```


- `props.style.color`: expression

```js
if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.LDR.OEE}, 0), '#,##0.0') + '%')) = 'Fault', '#C62828', if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.LDR.OEE}, 0), '#,##0.0') + '%')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/LDR/Rate`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Rate/Value'), 92), '#,##0')) + ' lb/hr', numberFormat(coalesce({view.custom.metrics.unitById.LDR.Rate}, 0), '#,##0') + ' lb/hr')
```


**`root/Draw/RSM`**

- `props.style.outline`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = 'RSM', '2px solid var(--cta)', '1px solid var(--border)')
```


**`root/Draw/RSM/Sub`**

- `position.display`: expression

```js
'Vacuum Sealed' != ''
```


**`root/Draw/RSM/RunStatus`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.RSM.OEE}, 0), '#,##0.0') + '%')
```


- `props.style.color`: expression

```js
if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.RSM.OEE}, 0), '#,##0.0') + '%')) = 'Fault', '#C62828', if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.RSM.OEE}, 0), '#,##0.0') + '%')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/RSM/Rate`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value'), 107), '#,##0')) + ' lb/hr', numberFormat(coalesce({view.custom.metrics.unitById.RSM.Rate}, 0), '#,##0') + ' lb/hr')
```


**`root/Draw/ST`**

- `props.style.outline`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = 'ST', '2px solid var(--cta)', '1px solid var(--border)')
```


**`root/Draw/ST/Sub`**

- `position.display`: expression

```js
'' != ''
```


**`root/Draw/ST/RunStatus`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.ST.OEE}, 0), '#,##0.0') + '%')
```


- `props.style.color`: expression

```js
if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.ST.OEE}, 0), '#,##0.0') + '%')) = 'Fault', '#C62828', if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.ST.OEE}, 0), '#,##0.0') + '%')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/ST/Rate`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value'), 92), '#,##0')) + ' lb/hr', numberFormat(coalesce({view.custom.metrics.unitById.ST.Rate}, 0), '#,##0') + ' lb/hr')
```


**`root/Draw/LS`**

- `props.style.outline`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = 'LS', '2px solid var(--cta)', '1px solid var(--border)')
```


**`root/Draw/LS/Sub`**

- `position.display`: expression

```js
'Placed On Trees' != ''
```


**`root/Draw/LS/RunStatus`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.LS.OEE}, 0), '#,##0.0') + '%')
```


- `props.style.color`: expression

```js
if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.LS.OEE}, 0), '#,##0.0') + '%')) = 'Fault', '#C62828', if((if(coalesce({view.custom.dayOffset}, 0) = 0, (if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 3, 'Fault', 'Idle')), 'Running')), 'OEE ' + numberFormat(coalesce({view.custom.metrics.unitById.LS.OEE}, 0), '#,##0.0') + '%')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/LS/Rate`**

- `props.text`: expression

```js
if(coalesce({view.custom.dayOffset}, 0) = 0, (numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value'), 99), '#,##0')) + ' lb/hr', numberFormat(coalesce({view.custom.metrics.unitById.LS.Rate}, 0), '#,##0') + ' lb/hr')
```


**`root/Draw/CardOee/OeeChart`**

- `props.series`: property `view.custom.metrics.oeeComponents`, then script transform

Transform 1, script:

```python
d = list(value or [])
return [{'name': '%', 'data': d}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.oeeComponentLabels`, then script transform

Transform 1, script:

```python
return list(value or [])
```


**`root/Draw/CardRateTrend/RateTrend`**

- `props.series`: property `view.custom.metrics.rateSeries`, then script transform

Transform 1, script:

```python
return list(value or [])
```


**`root/Draw/CardPareto/DtHeader/CardTitle`**

- `props.text`: expression

```js
'Downtime' + if(coalesce({view.custom.dtMode}, '') = 'detail', ' — ' + coalesce({view.custom.dtDetail}, ''), '')
```


**`root/Draw/CardPareto/DtHeader/DtBack`**

- `props.style.backgroundColor`: expression

```js
if(false, '#1E88E5', 'var(--surface-card)')
```


- `props.style.borderColor`: expression

```js
if(false, '#1E88E5', 'var(--border)')
```


- `position.display`: expression

```js
coalesce({view.custom.dtMode}, 'pareto') = 'detail'
```


**`root/Draw/CardPareto/DtHeader/DtBack/Lbl`**

- `props.style.color`: expression

```js
if(false, '#ffffff', 'var(--neutral-90)')
```


**`root/Draw/CardPareto/DtHeader/DtTabs`**

- `position.display`: expression

```js
coalesce({view.custom.dtMode}, 'pareto') != 'detail'
```


**`root/Draw/CardPareto/DtHeader/DtTabs/TabPareto`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({view.custom.dtMode}, 'pareto') = 'pareto', '#1E88E5', 'var(--surface-card)')
```


- `props.style.borderColor`: expression

```js
if(coalesce({view.custom.dtMode}, 'pareto') = 'pareto', '#1E88E5', 'var(--border)')
```


**`root/Draw/CardPareto/DtHeader/DtTabs/TabPareto/Lbl`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.dtMode}, 'pareto') = 'pareto', '#ffffff', 'var(--neutral-90)')
```


**`root/Draw/CardPareto/DtHeader/DtTabs/TabTrend`**

- `props.style.backgroundColor`: expression

```js
if(coalesce({view.custom.dtMode}, 'pareto') = 'trend', '#1E88E5', 'var(--surface-card)')
```


- `props.style.borderColor`: expression

```js
if(coalesce({view.custom.dtMode}, 'pareto') = 'trend', '#1E88E5', 'var(--border)')
```


**`root/Draw/CardPareto/DtHeader/DtTabs/TabTrend/Lbl`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.dtMode}, 'pareto') = 'trend', '#ffffff', 'var(--neutral-90)')
```


**`root/Draw/CardPareto/DtBody/ParetoChart`**

- `props.series`: property `view.custom.metrics.dtValues`, then script transform

Transform 1, script:

```python
d = list(value or [])
return [{'name': 'Minutes', 'data': d}]
```


- `props.options.xaxis.categories`: property `view.custom.metrics.dtLabels`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `position.display`: expression

```js
coalesce({view.custom.dtMode}, 'pareto') = 'pareto'
```


**`root/Draw/CardPareto/DtBody/DtTimeSeries`**

- `props.series`: property `view.custom.metrics.dtSeries`, then script transform

Transform 1, script:

```python
return list(value or [])
```


- `position.display`: expression

```js
coalesce({view.custom.dtMode}, 'pareto') = 'trend'
```


**`root/Draw/CardPareto/DtBody/DtDetailTable`**

- `props.data`: property `view.custom.metrics.dtEvents`

- `position.display`: expression

```js
coalesce({view.custom.dtMode}, 'pareto') = 'detail'
```


**`root/Draw/CardTis/TisChart`**

- `props.series`: property `view.custom.metrics.tisValues`, then script transform

Transform 1, script:

```python
return list(value or [])
```


**`root/Draw/CardZone`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = '', 'flex', 'none')
```


**`root/Draw/CardZone/ZoneTable`**

- `props.data`: property `view.custom.metrics.zones`

**`root/Draw/CardEquip`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = '', 'flex', 'none')
```


**`root/Draw/CardEquip/UnitTable`**

- `props.data`: property `view.custom.metrics.units`

**`root/Draw/CardAlarms`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = '' && coalesce({view.custom.dayOffset}, 0) = 0, 'flex', 'none')
```


**`root/Draw/CardAlarms/AlarmTable`**

- `props.data`: property `view.custom.metrics.alarms`

**`root/Draw/CardAlarmSummary`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') = '' && coalesce({view.custom.dayOffset}, 0) != 0, 'flex', 'none')
```


**`root/Draw/CardAlarmSummary/AlarmSummaryTable`**

- `props.data`: property `view.custom.metrics.alarmSummary`

**`root/Draw/CardSignals`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') != '', 'flex', 'none')
```


**`root/Draw/CardSignals/SignalTable`**

- `props.data`: property `view.custom.metrics.dSignals`

**`root/Draw/CardShifts`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') != '', 'flex', 'none')
```


**`root/Draw/CardShifts/ShiftTable`**

- `props.data`: property `view.custom.metrics.dShifts`

**`root/Draw/CardDevAlarms`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') != '' && coalesce({view.custom.dayOffset}, 0) = 0, 'flex', 'none')
```


**`root/Draw/CardDevAlarms/DevAlarmTable`**

- `props.data`: property `view.custom.metrics.dAlarms`

**`root/Draw/CardDevAlarmSummary`**

- `props.style.display`: expression

```js
if(coalesce({view.custom.selectedUnit}, '') != '' && coalesce({view.custom.dayOffset}, 0) != 0, 'flex', 'none')
```


**`root/Draw/CardDevAlarmSummary/DevAlarmSummaryTable`**

- `props.data`: property `view.custom.metrics.alarmSummary`

**`root/Draw/ShiftPendingOverlay`**

- `props.style.display`: expression

```js
if({view.custom.metrics.shiftPending} = true, 'flex', 'none')
```


**`root/Draw/ShiftPendingOverlay/PendingNote`**

- `props.text`: expression

```js
coalesce({view.custom.metrics.shiftNote}, 'Shift has not started yet')
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 39 event actions, change scripts and handlers</summary>

- **`root/Draw/BackToLine`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = ''
self.view.custom.selectedUnitName = ''
```

- **`root/Draw/GenerateReport`** `component.onActionPerformed`, script action, scope `G`

```python
# Report builder, pre-filled from this dashboard (scope / shift / day)
sel = self.view.custom.selectedUnit or ''
shared.Reports.open('production', {
    'scope': ['unit:' + sel] if sel else ['line'],
    'shifts': [self.view.custom.shiftSel] if self.view.custom.shiftSel else [],
    'dayOffset': self.view.custom.dayOffset or 0,
    'origin': 'Production Overview',
})
```

- **`root/Draw/ShiftTab_ALL`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.shiftSel = ''
```

- **`root/Draw/ShiftTab_A`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.shiftSel = 'A'
```

- **`root/Draw/ShiftTab_B`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.shiftSel = 'B'
```

- **`root/Draw/ShiftTab_C`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.shiftSel = 'C'
```

- **`root/Draw/VD`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = 'VD'
self.view.custom.selectedUnitName = 'Vat Dumper'
```

- **`root/Draw/VD`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value')
```

- **`root/Draw/VD/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')
```

- **`root/Draw/VD/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value')
```

- **`root/Draw/HOP`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = 'HOP'
self.view.custom.selectedUnitName = 'Hopper'
```

- **`root/Draw/HOP`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value')
```

- **`root/Draw/HOP/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')
```

- **`root/Draw/HOP/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value')
```

- **`root/Draw/HND`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = 'HND'
self.view.custom.selectedUnitName = 'Handtman'
```

- **`root/Draw/HND`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HND/Rate/Value')
```

- **`root/Draw/HND/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value')
```

- **`root/Draw/HND/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HND/Rate/Value')
```

- **`root/Draw/LDR`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = 'LDR'
self.view.custom.selectedUnitName = 'Loaders'
```

- **`root/Draw/LDR`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LDR/Rate/Value')
```

- **`root/Draw/LDR/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value')
```

- **`root/Draw/LDR/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LDR/Rate/Value')
```

- **`root/Draw/RSM`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = 'RSM'
self.view.custom.selectedUnitName = 'Roll Stock'
```

- **`root/Draw/RSM`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value')
```

- **`root/Draw/RSM/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')
```

- **`root/Draw/RSM/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value')
```

- **`root/Draw/ST`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = 'ST'
self.view.custom.selectedUnitName = 'Shrink Tunnel'
```

- **`root/Draw/ST`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value')
```

- **`root/Draw/ST/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')
```

- **`root/Draw/ST/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value')
```

- **`root/Draw/LS`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedUnit = 'LS'
self.view.custom.selectedUnitName = 'Lazy Susan'
```

- **`root/Draw/LS`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value')
```

- **`root/Draw/LS/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')
```

- **`root/Draw/LS/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value')
```

- **`root/Draw/CardPareto/DtHeader/DtBack`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.dtMode = 'pareto'
self.view.custom.dtDetail = ''
```

- **`root/Draw/CardPareto/DtHeader/DtTabs/TabPareto`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.dtMode = 'pareto'
self.view.custom.dtDetail = ''
```

- **`root/Draw/CardPareto/DtHeader/DtTabs/TabTrend`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.dtMode = 'trend'
self.view.custom.dtDetail = ''
```

- **`root/Draw/CardPareto/DtBody/ParetoChart`** `component.dataPointSelectionHandler`, script action, scope `G`

```python
idx = -1
try:
    idx = int(event.dataPointIndex)
except:
    try:
        idx = int(event['dataPointIndex'])
    except:
        idx = -1
labels = []
try:
    labels = list(self.view.custom.metrics.dtLabels or [])
except:
    labels = []
if idx < 0 or idx >= len(labels):
    return
self.view.custom.dtDetail = str(labels[idx])
self.view.custom.dtMode = 'detail'
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.ProductionMetrics.l1](../../../../../../../scripting/reference/modules/shared-productionmetrics.md), [shared.Reports](../../../../../../../scripting/reference/modules/shared-reports.md), [shared.Scale.cssTransform](../../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

## Style Classes

<details>
<summary>20 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 73 | style class |
| `Fonts/Title` | 2 | style class |
| `Fonts/Value` | 18 | style class |
| `bg-page` | 1 | style class |
| `container-card` | 25 | stylesheet |
| `container-card-border` | 25 | stylesheet |
| `fs-10` | 14 | style class |
| `fs-12` | 30 | style class |
| `fs-14` | 7 | style class |
| `fs-18` | 17 | style class |
| `fs-22` | 8 | style class |
| `fs-9` | 7 | style class |
| `fw-600` | 14 | style class |
| `fw-700` | 63 | style class |
| `plant-feature-title` | 1 | style class |
| `prod-device-tile` | 7 | style class |
| `text-cta` | 7 | style class |
| `text-muted` | 34 | style class |
| `utility-kpi-chart` | 5 | stylesheet |
| `utility-kpi-table` | 9 | stylesheet |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

<details>
<summary>42 literal tag paths</summary>

- `[default]Boars_Head/GrovePort/Production/FCM/HND/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HND/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HND/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LDR/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LDR/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LDR/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LS/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LS/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Availability/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Cases/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Performance/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Quality/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Uptime/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Line/Yield/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/Reject/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Zones/Forming/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Zones/Forming/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Zones/Packaging/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Zones/Packaging/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Zones/Prep/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Zones/Prep/Rate/Value`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
