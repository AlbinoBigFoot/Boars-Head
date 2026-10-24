---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls (Asset (embedded piece)): 44 components, 31 bindings, 5 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; DischargeSequence &gt; Controls |
| Root | `ia.container.flex`, height 600, width 1140 |
| Size | 44 components, 31 bindings, 5 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `sensorPax` | `""` | bound (expr) |
| `levelPax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x20, ia.container.flex x19, ia.display.view x5.

<details>
<summary>Component tree (44 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Columns  ia.container.flex
    Left  ia.container.flex
      SequenceSection  ia.container.flex
        SequenceSectionTitle  ia.display.label
        SequenceRows  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
      PressureSection  ia.container.flex
        PressureSectionTitle  ia.display.label
        Actual  ia.container.flex
          Lbl  ia.display.label  [2 bindings]
          Val  ia.display.label  [3 bindings; 1 event]
        Target  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings]
    Middle  ia.container.flex
      SumpSection  ia.container.flex
        SumpSectionTitle  ia.display.label
        SumpRows  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
      ModeSection  ia.container.flex
        ModeSectionTitle  ia.display.label
        ModeRows  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
      TimeSection  ia.container.flex
        TimeSectionTitle  ia.display.label
        StartLeft  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings]
        StopLeft  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings]
      SensorSection  ia.container.flex
        SensorSectionTitle  ia.display.label
        Level  ia.container.flex  [1 event]
          Lbl  ia.display.label  [2 bindings]
          Val  ia.display.label  [3 bindings; 1 event]
        Pressure  ia.container.flex  [1 event]
          Lbl  ia.display.label  [2 bindings]
          Val  ia.display.label  [3 bindings; 1 event]
    Right  ia.container.flex
      SlowSection  ia.container.flex
        SlowSectionTitle  ia.display.label
        SlowRows  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
      FastSection  ia.container.flex
        FastSectionTitle  ia.display.label
        FastRows  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
```

</details>

## Bindings

31 bindings: expr 26, property 5.

<details>
<summary>All 31 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.sensorPax`: expression

```js
if(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') = '', '', case(toStr(coalesce(try(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/DIn.Enabled')), false), false), 'DIn', ''), ''))
```


- `custom.levelPax`: expression

```js
if(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') = '', '', case(toStr(coalesce(try(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/DIn.Enabled')), false), false), 'DIn', ''), ''))
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Columns/Left/SequenceSection/SequenceRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Columns/Left/PressureSection/Actual/Lbl`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', 'Actual Pressure (' + coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), ''), '') + ')')))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label Fonts/Label value-bad', 'faceplate-kpi-label Fonts/Label')))))))))))))))
```


**`root/Columns/Left/PressureSection/Actual/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val')), true), true)), '—', if(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') = '', '—', coalesce(try(numberFormat(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val'), '#,##0.0') + ' ' + coalesce(try(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val.EngUnit'), ''), ''), null), '—'))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val')), true), true)), 'Fonts/Value value-bad', 'Fonts/Value'))))))))))))))))
```


- `custom.trendPath`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val'
```


**`root/Columns/Left/PressureSection/Target/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/PlcFixedSP'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/PlcFixedSP' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcFixedSP')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Middle/SumpSection/SumpRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Columns/Middle/ModeSection/ModeRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Columns/Middle/TimeSection/StartLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft'), '#,##0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StartTimeLeft')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Middle/TimeSection/StopLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft'), '#,##0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seqr/Sts_StopTimeLeft')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Middle/SensorSection/Level/Lbl`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), '—', coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), ''), ''))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelLabel/Value')), true), true), 'faceplate-kpi-label Fonts/Label value-bad', 'faceplate-kpi-label Fonts/Label')))))))))))))))
```


**`root/Columns/Middle/SensorSection/Level/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), '—', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/' + {view.custom.levelPax} + '/Val')), true), true)), '—', if(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') = '', '—', coalesce(try(numberFormat(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/' + {view.custom.levelPax} + '/Val'), '#,##0.00') + ' ' + coalesce(try(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/' + {view.custom.levelPax} + '/Val.EngUnit'), ''), ''), null), '—'))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/' + {view.custom.levelPax} + '/Val')), true), true)), 'Fonts/Value value-bad', 'Fonts/Value'))))))))))))))))
```


- `custom.trendPath`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_LevelPath/Value')), ''), '') + '/' + {view.custom.levelPax} + '/Val'
```


**`root/Columns/Middle/SensorSection/Pressure/Lbl`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), '—', coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), ''), ''))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorLabel/Value')), true), true), 'faceplate-kpi-label Fonts/Label value-bad', 'faceplate-kpi-label Fonts/Label')))))))))))))))
```


**`root/Columns/Middle/SensorSection/Pressure/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val')), true), true)), '—', if(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') = '', '—', coalesce(try(numberFormat(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val'), '#,##0.00') + ' ' + coalesce(try(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val.EngUnit'), ''), ''), null), '—'))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val')), true), true)), 'Fonts/Value value-bad', 'Fonts/Value'))))))))))))))))
```


- `custom.trendPath`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val'
```


**`root/Columns/Right/SlowSection/SlowRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Columns/Right/FastSection/FastRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

</details>

## Event Scripts And Handlers

- **`root/Columns/Left/PressureSection/Actual/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{this.custom.trendPath}')
```

- **`root/Columns/Middle/SensorSection/Level`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
p = system.tag.readBlocking([base + '/Cfg_LevelPath/Value'])[0].value
if p:
    Navigation.Faceplate.openDevice(str(p), str(self.getChild('Lbl').props.text or ''))
```

- **`root/Columns/Middle/SensorSection/Level/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{this.custom.trendPath}')
```

- **`root/Columns/Middle/SensorSection/Pressure`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
p = system.tag.readBlocking([base + '/Cfg_SensorPath/Value'])[0].value
if p:
    Navigation.Faceplate.openDevice(str(p), str(self.getChild('Lbl').props.text or ''))
```

- **`root/Columns/Middle/SensorSection/Pressure/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{this.custom.trendPath}')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](../configuration/configsection.md)

**Embedded in** (1): [01\_Popups/00\_Faceplates/DischargeSequence](../../dischargesequence.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 14 | style class |
| `Fonts/Value` | 6 | style class |
| `faceplate-hover` | 2 | stylesheet |
| `faceplate-kpi-label` | 6 | style class |
| `faceplate-kpi-row` | 6 | stylesheet |
| `faceplate-section` | 8 | style class |
| `faceplate-section-card` | 8 | style class |
| `faceplate-section-title` | 8 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>14 relative member paths</summary>

`.EngUnit`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_LevelLabel/Value`, `/Cfg_LevelPath/Value`, `/Cfg_SensorLabel/Value`, `/Cfg_SensorPath/Value`, `/DIn.Enabled`, `/PlcFixedSP`, `/Seqr/Sts_StartTimeLeft`, `/Seqr/Sts_StopTimeLeft`, `/Val`, `/Val.EngUnit`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
