---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls (Asset (embedded piece)): 38 components, 29 bindings, 4 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; SuctionSequence &gt; Controls |
| Root | `ia.container.flex`, height 560, width 660 |
| Size | 38 components, 29 bindings, 4 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T20:12:34Z by the Designer |

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

Component types: ia.display.label x18, ia.container.flex x15, ia.display.view x5.

<details>
<summary>Component tree (38 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Columns  ia.container.flex
    Left  ia.container.flex
      PressureSection  ia.container.flex
        PressureSectionTitle  ia.display.label
        Actual  ia.container.flex
          Lbl  ia.display.label  [2 bindings]
          Val  ia.display.label  [3 bindings; 1 event]
        Start  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings; 1 event]
        TargetSet  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
        Stop  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings; 1 event]
        Target  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings; 1 event]
      SequenceSection  ia.container.flex
        SequenceSectionTitle  ia.display.label
        SequenceRows  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
    Right  ia.container.flex
      StartSection  ia.container.flex
        StartSectionTitle  ia.display.label
        StartRows  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
        StartLeft  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings]
      StopSection  ia.container.flex
        StopSectionTitle  ia.display.label
        StopRows  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
        StopLeft  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings]
      NotesSection  ia.container.flex
        NotesSectionTitle  ia.display.label
        Notes  ia.display.label  [2 bindings]
        EnableRow  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
```

</details>

## Bindings

29 bindings: expr 24, property 5.

<details>
<summary>All 29 bindings, grouped by component</summary>

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
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), '—', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val')), true), true)), '—', if(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') = '', '—', coalesce(try(numberFormat(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val'), '#,##0.0') + ' PSIG', null), '—'))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && (coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), true), true) || coalesce(try(!isGood(tag(coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val')), true), true)), 'Fonts/Value value-bad', 'Fonts/Value'))))))))))))))))
```


- `custom.trendPath`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_SensorPath/Value')), ''), '') + '/' + {view.custom.sensorPax} + '/Val'
```


**`root/Columns/Left/PressureSection/Start/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Seq/Start_Pressure'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Seq/Start_Pressure' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Pressure')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Left/PressureSection/TargetSet`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Columns/Left/PressureSection/Stop/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Seq/Stop_Pressure'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Seq/Stop_Pressure' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Pressure')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Left/PressureSection/Target/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Seq/Target_Pressure'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Seq/Target_Pressure' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Target_Pressure')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Left/SequenceSection/SequenceRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `props.params.rowsJson`: expression

```js
if(coalesce(try(toInt(tag({view.params.tagPath} + '/Cfg_Positions/Value')), 4), 4) <= 2, '[{"leaf":"Sequence_Set_1","kind":"numeric","label":"First Compressor"},{"leaf":"Sequence_Set_2","kind":"numeric","label":"Second Compressor"}]', '[{"leaf":"Sequence_Set_1","kind":"numeric","label":"First Compressor"},{"leaf":"Sequence_Set_2","kind":"numeric","label":"Second Compressor"},{"leaf":"Sequence_Set_3","kind":"numeric","label":"Third Compressor"},{"leaf":"Sequence_Set_4","kind":"numeric","label":"Fourth Compressor"}]')
```


**`root/Columns/Right/StartSection/StartRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Columns/Right/StartSection/StartLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Seq/Start_Time_Left'), '#,##0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Seq/Start_Time_Left' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Start_Time_Left')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Right/StopSection/StopRows`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Columns/Right/StopSection/StopLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Seq/Stop_Time_Left'), '#,##0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Seq/Stop_Time_Left' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Seq/Stop_Time_Left')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/Columns/Right/NotesSection/Notes`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), '—', coalesce(try(toStr(tag({view.params.tagPath} + '/Cfg_Notes/Value')), ''), ''))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Cfg_Notes/Value')), true), true), 'Fonts/Label value-bad', 'Fonts/Label')))))))))))))))
```


**`root/Columns/Right/NotesSection/EnableRow`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `meta.visible`: expression

```js
coalesce(try(toBoolean(tag({view.params.tagPath} + '/Cfg_HasEnable/Value')), false), false)
```

</details>

## Event Scripts And Handlers

- **`root/Columns/Left/PressureSection/Actual/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{this.custom.trendPath}')
```

- **`root/Columns/Left/PressureSection/Start/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Seq/Start_Pressure')
```

- **`root/Columns/Left/PressureSection/Stop/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Seq/Stop_Pressure')
```

- **`root/Columns/Left/PressureSection/Target/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Seq/Target_Pressure')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](../configuration/configsection.md)

**Embedded in** (1): [01\_Popups/00\_Faceplates/SuctionSequence](../../suctionsequence.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 12 | style class |
| `Fonts/Value` | 6 | style class |
| `faceplate-kpi-label` | 6 | style class |
| `faceplate-kpi-row` | 6 | stylesheet |
| `faceplate-section` | 5 | style class |
| `faceplate-section-card` | 5 | style class |
| `faceplate-section-title` | 5 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>17 relative member paths</summary>

`.EngUnit`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_HasEnable/Value`, `/Cfg_LevelPath/Value`, `/Cfg_Notes/Value`, `/Cfg_Positions/Value`, `/Cfg_SensorLabel/Value`, `/Cfg_SensorPath/Value`, `/DIn.Enabled`, `/Seq/Start_Pressure`, `/Seq/Start_Time_Left`, `/Seq/Stop_Pressure`, `/Seq/Stop_Time_Left`, `/Seq/Target_Pressure`, `/Val`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
