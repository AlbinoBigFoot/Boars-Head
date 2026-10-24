---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Tank/Controls (Asset (embedded piece)): 64 components, 94 bindings, 9 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Tank/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Tank/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Tank/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Tank/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Tank &gt; Controls |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 64 components, 94 bindings, 9 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

<details>
<summary>35 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `pump1Pax` | `""` | bound (expr) |
| `pump2Pax` | `""` | bound (expr) |
| `sensorSLPax` | `""` | bound (expr) |
| `sensorSSPax` | `""` | bound (expr) |
| `qg0` | `null` | bound (expr) |
| `qg1` | `null` | bound (expr) |
| `qg2` | `null` | bound (expr) |
| `qg3` | `null` | bound (expr) |
| `qg4` | `null` | bound (expr) |
| `qg5` | `null` | bound (expr) |
| `qg6` | `null` | bound (expr) |
| `qg7` | `null` | bound (expr) |
| `qg8` | `null` | bound (expr) |
| `qg9` | `null` | bound (expr) |
| `qg10` | `null` | bound (expr) |
| `qg11` | `null` | bound (expr) |
| `qg12` | `null` | bound (expr) |
| `qg13` | `null` | bound (expr) |
| `qg14` | `null` | bound (expr) |
| `qg15` | `null` | bound (expr) |
| `qg16` | `null` | bound (expr) |
| `qg17` | `null` | bound (expr) |
| `qg18` | `null` | bound (expr) |
| `qg19` | `null` | bound (expr) |
| `qg20` | `null` | bound (expr) |
| `qg21` | `null` | bound (expr) |
| `qg22` | `null` | bound (expr) |
| `qg23` | `null` | bound (expr) |
| `qg24` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |
| `roMode` | `true` | bound (expr) |
| `tipMode` | `""` | bound (expr) |

</details>

## Component Tree

Component types: ia.display.label x32, ia.container.flex x24, ia.input.button x7, ia.display.view x1.

<details>
<summary>Component tree (64 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  AinHome  ia.container.flex
    AinHomeTitle  ia.display.label
    ModeRow  ia.container.flex
      Mode  ia.display.label  [1 binding]
      Spacer  ia.container.flex
      BtnLock  ia.input.button  [4 bindings; 1 event]
      BtnUnlock  ia.input.button  [3 bindings; 1 event]
      BtnReset  ia.input.button  [4 bindings; 1 event]
    Gauge  ia.container.flex
      Scale  ia.container.flex
        Max  ia.display.label  [1 binding]
        Min  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [2 bindings]
      Limits  ia.container.flex
        HH  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
        H  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
        PV  ia.container.flex  [1 binding]
          Val  ia.display.label  [1 binding; 1 event]
          EU  ia.display.label  [1 binding]
        L  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
        LL  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
    Comm  ia.display.label  [2 bindings; 1 event]
  StatusSection  ia.container.flex  [1 binding]
    StatusSectionTitle  ia.display.label
    PumpAlarms  ia.container.flex
      Pump1Alm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Pump2Alm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
    SuctionPress  ia.container.flex  [1 binding]
      Lbl  ia.display.label  [1 binding]
      Val  ia.display.label  [1 binding]
    PumpsPress  ia.container.flex  [1 binding]
      Lbl  ia.display.label  [1 binding]
      Val  ia.display.label  [1 binding]
  PumpsSection  ia.container.flex  [1 binding]
    PumpsSectionTitle  ia.display.label
    LeadLbl  ia.display.label
    LeadRow  ia.container.flex
      Lead1  ia.input.button  [4 bindings; 1 event]
      Lead2  ia.input.button  [4 bindings; 1 event]
    StartPress  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
    IntlkRow  ia.container.flex
      Pump1Intlk  ia.input.button  [3 bindings; 1 event]
      Pump2Intlk  ia.input.button  [3 bindings; 1 event]
  LegendSection  ia.container.flex  [1 binding]
    LegendSectionTitle  ia.display.label
    L0  ia.display.label
    L1  ia.display.label
    L2  ia.display.label
    L3  ia.display.label
    L4  ia.display.label
```

</details>

## Bindings

94 bindings: expr 93, property 1.

<details>
<summary>All 94 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.pump1Pax`: expression

```js
case(toStr(coalesce(try(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '/DIn.Enabled')), false), false), 'DIn', ''), '')
```


- `custom.pump2Pax`: expression

```js
case(toStr(coalesce(try(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2') + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2') + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2') + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2') + '/DIn.Enabled')), false), false), 'DIn', ''), '')
```


- `custom.sensorSLPax`: expression

```js
case(toStr(coalesce(try(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '/DIn.Enabled')), false), false), 'DIn', ''), '')
```


- `custom.sensorSSPax`: expression

```js
case(toStr(coalesce(try(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '/DIn.Enabled')), false), false), 'DIn', ''), '')
```


- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Oper')), tag({view.params.tagPath} + '/LvlAIn/Sts_Oper'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Mode/Sts_ProgOperLock')), tag({view.params.tagPath} + '/LvlAIn/Mode/Sts_ProgOperLock'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Fail')), tag({view.params.tagPath} + '/LvlAIn/Sts_Fail'), null), null)
```


- `custom.qg3`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_HiHi')), tag({view.params.tagPath} + '/LvlAIn/Sts_HiHi'), null), null)
```


- `custom.qg4`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Hi')), tag({view.params.tagPath} + '/LvlAIn/Sts_Hi'), null), null)
```


- `custom.qg5`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Lo')), tag({view.params.tagPath} + '/LvlAIn/Sts_Lo'), null), null)
```


- `custom.qg6`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_LoLo')), tag({view.params.tagPath} + '/LvlAIn/Sts_LoLo'), null), null)
```


- `custom.qg7`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMax')), tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMax'), null), null)
```


- `custom.qg8`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMin')), tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMin'), null), null)
```


- `custom.qg9`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Val')), tag({view.params.tagPath} + '/LvlAIn/Val'), null), null)
```


- `custom.qg10`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_HiHiLim')), tag({view.params.tagPath} + '/LvlAIn/Val_HiHiLim'), null), null)
```


- `custom.qg11`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_HiLim')), tag({view.params.tagPath} + '/LvlAIn/Val_HiLim'), null), null)
```


- `custom.qg12`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_EU')), tag({view.params.tagPath} + '/LvlAIn/Cfg_EU'), null), null)
```


- `custom.qg13`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Val' + '.EngUnit')), tag({view.params.tagPath} + '/LvlAIn/Val' + '.EngUnit'), null), null)
```


- `custom.qg14`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_LoLim')), tag({view.params.tagPath} + '/LvlAIn/Val_LoLim'), null), null)
```


- `custom.qg15`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_LoLoLim')), tag({view.params.tagPath} + '/LvlAIn/Val_LoLoLim'), null), null)
```


- `custom.qg16`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Pump1Alm/Sts')), tag({view.params.tagPath} + '/Pump1Alm/Sts'), null), null)
```


- `custom.qg17`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Pump2Alm/Sts')), tag({view.params.tagPath} + '/Pump2Alm/Sts'), null), null)
```


- `custom.qg18`: expression

```js
try(if(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '/AIn/Val')), tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '/AIn/Val'), null), null)
```


- `custom.qg19`: expression

```js
try(if(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '/AIn/Val' + '.EngUnit')), tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-Pumps Pressure') + '/AIn/Val' + '.EngUnit'), null), null)
```


- `custom.qg20`: expression

```js
try(if(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '/AIn/Val')), tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '/AIn/Val'), null), null)
```


- `custom.qg21`: expression

```js
try(if(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '/AIn/Val' + '.EngUnit')), tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure') + '/AIn/Val' + '.EngUnit'), null), null)
```


- `custom.qg22`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LeadPump')), tag({view.params.tagPath} + '/LeadPump'), null), null)
```


- `custom.qg23`: expression

```js
try(if(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '/Intlk/Sts_IntlkOK')), tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '/Intlk/Sts_IntlkOK'), null), null)
```


- `custom.qg24`: expression

```js
try(if(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2') + '/Intlk/Sts_IntlkOK')), tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2') + '/Intlk/Sts_IntlkOK'), null), null)
```


- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roCommand`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Command'], null), true)
```


- `custom.tipCommand`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roCommand}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Command' + ' (Roles & Permissions)', '')
```


- `custom.roMode`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Mode'], null), true)
```


- `custom.tipMode`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roMode}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Mode' + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/AinHome/ModeRow/Mode`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', if(coalesce(try(toBoolean({view.custom.qg0}), false), false), 'Operator', 'Program'))
```


**`root/AinHome/ModeRow/BtnLock`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roMode}, false) && !({view.params.tagPath} = '') && !coalesce(try(toBoolean({view.custom.qg1}), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if(coalesce(try(toBoolean({view.custom.qg1}), false), false), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/AinHome/ModeRow/BtnUnlock`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roMode}, false) && !({view.params.tagPath} = '') && coalesce(try(toBoolean({view.custom.qg1}), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/AinHome/ModeRow/BtnReset`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '') && (coalesce(try(toBoolean({view.custom.qg2}), false), false) || coalesce(try(toBoolean({view.custom.qg3}), false), false) || coalesce(try(toBoolean({view.custom.qg4}), false), false) || coalesce(try(toBoolean({view.custom.qg5}), false), false) || coalesce(try(toBoolean({view.custom.qg6}), false), false))) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if((coalesce(try(toBoolean({view.custom.qg2}), false), false) || coalesce(try(toBoolean({view.custom.qg3}), false), false) || coalesce(try(toBoolean({view.custom.qg4}), false), false) || coalesce(try(toBoolean({view.custom.qg5}), false), false) || coalesce(try(toBoolean({view.custom.qg6}), false), false)), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/AinHome/Gauge/Scale/Max`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat({view.custom.qg7}, '#,##0.00'), null), '—'))
```


**`root/AinHome/Gauge/Scale/Min`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat({view.custom.qg8}, '#,##0.00'), null), '—'))
```


**`root/AinHome/Gauge/Bar/Fill`**

- `position.basis`: expression

```js
toStr(max(0, min(100, (coalesce(try(toFloat({view.custom.qg9}), 0), 0) - coalesce(try(toFloat({view.custom.qg8}), 0), 0)) / if(coalesce(try(toFloat({view.custom.qg7}), 100), 100) - coalesce(try(toFloat({view.custom.qg8}), 0), 0) = 0, 1, coalesce(try(toFloat({view.custom.qg7}), 100), 100) - coalesce(try(toFloat({view.custom.qg8}), 0), 0)) * 100))) + '%'
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try(toBoolean({view.custom.qg3}), false), false) || coalesce(try(toBoolean({view.custom.qg6}), false), false), 'var(--status-level-critical)', if(coalesce(try(toBoolean({view.custom.qg4}), false), false) || coalesce(try(toBoolean({view.custom.qg5}), false), false), '#F9A825', 'var(--status-cooling)'))
```


**`root/AinHome/Gauge/Limits/HH`**

- `props.style.color`: expression

```js
if(coalesce(try(toBoolean({view.custom.qg3}), false), false), 'var(--status-level-critical)', '')
```


**`root/AinHome/Gauge/Limits/HH/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat({view.custom.qg10})) >= 1e30, false), false), null, {view.custom.qg10}), '#,##0.00'), null), '—'))
```


**`root/AinHome/Gauge/Limits/H`**

- `props.style.color`: expression

```js
if(coalesce(try(toBoolean({view.custom.qg4}), false), false), 'var(--status-level-critical)', '')
```


**`root/AinHome/Gauge/Limits/H/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat({view.custom.qg11})) >= 1e30, false), false), null, {view.custom.qg11}), '#,##0.00'), null), '—'))
```


**`root/AinHome/Gauge/Limits/PV`**

- `props.style.color`: expression

```js
if(coalesce(try(toBoolean({view.custom.qg3}), false), false) || coalesce(try(toBoolean({view.custom.qg6}), false), false), 'var(--status-level-critical)', if(coalesce(try(toBoolean({view.custom.qg4}), false), false) || coalesce(try(toBoolean({view.custom.qg5}), false), false), '#F9A825', 'var(--status-cooling)'))
```


**`root/AinHome/Gauge/Limits/PV/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat({view.custom.qg9}, '#,##0.00'), null), '—'))
```


**`root/AinHome/Gauge/Limits/PV/EU`**

- `props.text`: expression

```js
if(coalesce(try(toStr({view.custom.qg12}), ''), '') != '', coalesce(try(toStr({view.custom.qg12}), ''), ''), coalesce(try({view.custom.qg13}, ''), ''))
```


**`root/AinHome/Gauge/Limits/L`**

- `props.style.color`: expression

```js
if(coalesce(try(toBoolean({view.custom.qg5}), false), false), 'var(--status-level-critical)', '')
```


**`root/AinHome/Gauge/Limits/L/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat({view.custom.qg14})) >= 1e30, false), false), null, {view.custom.qg14}), '#,##0.00'), null), '—'))
```


**`root/AinHome/Gauge/Limits/LL`**

- `props.style.color`: expression

```js
if(coalesce(try(toBoolean({view.custom.qg6}), false), false), 'var(--status-level-critical)', '')
```


**`root/AinHome/Gauge/Limits/LL/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat({view.custom.qg15})) >= 1e30, false), false), null, {view.custom.qg15}), '#,##0.00'), null), '—'))
```


**`root/AinHome/Comm`**

- `props.text`: expression

```js
if(try(isNull({view.custom.qg9}), true), 'Comm Loss', if(coalesce(try(toBoolean({view.custom.qg2}), false), false), 'Input Failure', 'Comm OK'))
```


- `props.style.color`: expression

```js
if(try(isNull({view.custom.qg9}), true) || coalesce(try(toBoolean({view.custom.qg2}), false), false), 'var(--status-level-critical)', 'var(--text-muted)')
```


**`root/StatusSection`**

- `position.display`: expression

```js
!({view.params.tagPath} = '') && try(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '.TypeId')), false)
```


**`root/StatusSection/PumpAlarms/Pump1Alm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', if(coalesce(try(if(isNull({view.custom.qg16}), null, {view.custom.qg16}), null), false), 'ALARM', 'OK'))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(isNull({view.custom.qg16}), null, {view.custom.qg16}), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'))
```


**`root/StatusSection/PumpAlarms/Pump2Alm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', if(coalesce(try(if(isNull({view.custom.qg17}), null, {view.custom.qg17}), null), false), 'ALARM', 'OK'))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(isNull({view.custom.qg17}), null, {view.custom.qg17}), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'))
```


**`root/StatusSection/SuctionPress`**

- `position.display`: expression

```js
coalesce({view.custom.pax}, '') != 'Tank' || coalesce(try(toBoolean(tag({view.params.tagPath} + '/PressAIn.Enabled')), false), false)
```


**`root/StatusSection/SuctionPress/Lbl`**

- `props.text`: expression

```js
left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SS-PT' + if(left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) = 'H', '2', '1')
```


**`root/StatusSection/SuctionPress/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat({view.custom.qg18}, '#,##0.00') + ' ' + coalesce(try({view.custom.qg19}, ''), ''), null), '—'))
```


**`root/StatusSection/PumpsPress`**

- `position.display`: expression

```js
coalesce({view.custom.pax}, '') != 'Tank' || coalesce(try(toBoolean(tag({view.params.tagPath} + '/PressAIn.Enabled')), false), false)
```


**`root/StatusSection/PumpsPress/Lbl`**

- `props.text`: expression

```js
left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure'
```


**`root/StatusSection/PumpsPress/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat({view.custom.qg20}, '#,##0.00') + ' ' + coalesce(try({view.custom.qg21}, ''), ''), null), '—'))
```


**`root/PumpsSection`**

- `position.display`: expression

```js
!({view.params.tagPath} = '') && try(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '.TypeId')), false)
```


**`root/PumpsSection/LeadRow/Lead1`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '')) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if(coalesce(try(toInt({view.custom.qg22}), 0), 0) = 1, 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/PumpsSection/LeadRow/Lead2`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '')) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if(coalesce(try(toInt({view.custom.qg22}), 0), 0) = 2, 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/PumpsSection/StartPress`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/PumpsSection/IntlkRow/Pump1Intlk`**

- `props.enabled`: expression

```js
!({view.params.tagPath} = '')
```


- `props.text`: expression

```js
'Pump #1 Interlocks' + if(coalesce(try({view.custom.qg23}, false), false), ' · OK', ' · Interlocked')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try({view.custom.qg23}, false), false), '#2E7D32', 'var(--status-level-critical)')
```


**`root/PumpsSection/IntlkRow/Pump2Intlk`**

- `props.enabled`: expression

```js
!({view.params.tagPath} = '')
```


- `props.text`: expression

```js
'Pump #2 Interlocks' + if(coalesce(try({view.custom.qg24}, false), false), ' · OK', ' · Interlocked')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try({view.custom.qg24}, false), false), '#2E7D32', 'var(--status-level-critical)')
```


**`root/LegendSection`**

- `position.display`: expression

```js
!({view.params.tagPath} = '') && try(isGood(tag((substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1') + '.TypeId')), false)
```

</details>

## Event Scripts And Handlers

- **`root/AinHome/ModeRow/BtnLock`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/Mode/OCmd_AcqLock'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Operator Lock',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/AinHome/ModeRow/BtnUnlock`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/Mode/OCmd_UnlockRel'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Operator Unlock',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/AinHome/ModeRow/BtnReset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/OCmd_Reset'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Reset / Ack',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/AinHome/Gauge/Limits/PV/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/LvlAIn/Val')
```

- **`root/AinHome/Comm`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/LvlAIn/Val')
```

- **`root/PumpsSection/LeadRow/Lead1`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LeadPump'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Lead Pump',
    tagPath=path,
    newValue=1,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/PumpsSection/LeadRow/Lead2`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LeadPump'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Lead Pump',
    tagPath=path,
    newValue=2,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/PumpsSection/IntlkRow/Pump1Intlk`** `component.onActionPerformed`, script action, scope `G`

```python
base = str(self.view.params.tagPath or '')
if '/Tanks/' not in base:
    return
name = base.split('/')[-1]
pump = base.split('/Tanks/')[0] + '/Pumps/' + name[:-1] + 'LR-Pump 1'
shared.Alerts.showFaceplate(tagPath=pump, deviceType='Pump', title=pump.split('/')[-1],
    initialTab='Interlocks')
```

- **`root/PumpsSection/IntlkRow/Pump2Intlk`** `component.onActionPerformed`, script action, scope `G`

```python
base = str(self.view.params.tagPath or '')
if '/Tanks/' not in base:
    return
name = base.split('/')[-1]
pump = base.split('/Tanks/')[0] + '/Pumps/' + name[:-1] + 'LR-Pump 2'
shared.Alerts.showFaceplate(tagPath=pump, deviceType='Pump', title=pump.split('/')[-1],
    initialTab='Interlocks')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](../configuration/configsection.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

<details>
<summary>17 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 29 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 7 | style class |
| `faceplate-cmd-btn` | 7 | style class |
| `faceplate-cmd-row` | 2 | stylesheet |
| `faceplate-cmd-row-fill` | 2 | stylesheet |
| `faceplate-fault-chip` | 2 | style class |
| `faceplate-fault-chips` | 1 | stylesheet |
| `faceplate-fault-code` | 2 | style class |
| `faceplate-fault-state` | 2 | stylesheet |
| `faceplate-kpi-label` | 2 | style class |
| `faceplate-kpi-row` | 2 | stylesheet |
| `faceplate-section` | 4 | style class |
| `faceplate-section-card` | 4 | style class |
| `faceplate-section-title` | 4 | style class |
| `fw-700` | 8 | style class |
| `faceplate-cmd-btn-active` | bound | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>31 relative member paths</summary>

`.EngUnit`, `.TypeId`, `/AIn.Enabled`, `/AIn/Val`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Intlk/Sts_IntlkOK`, `/LeadPump`, `/LvlAIn/Cfg_EU`, `/LvlAIn/Cfg_PVEUMax`, `/LvlAIn/Cfg_PVEUMin`, `/LvlAIn/Mode/OCmd_AcqLock`, `/LvlAIn/Mode/OCmd_UnlockRel`, `/LvlAIn/Mode/Sts_ProgOperLock`, `/LvlAIn/OCmd_Reset`, `/LvlAIn/Sts_Fail`, `/LvlAIn/Sts_Hi`, `/LvlAIn/Sts_HiHi`, `/LvlAIn/Sts_Lo`, `/LvlAIn/Sts_LoLo`, `/LvlAIn/Sts_Oper`, `/LvlAIn/Val`, `/LvlAIn/Val_HiHiLim`, `/LvlAIn/Val_HiLim`, `/LvlAIn/Val_LoLim`, `/LvlAIn/Val_LoLoLim`, `/PressAIn.Enabled`, `/Pump1Alm/Sts`, `/Pump2Alm/Sts`, `/Pumps/`, `/Sensors/`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
