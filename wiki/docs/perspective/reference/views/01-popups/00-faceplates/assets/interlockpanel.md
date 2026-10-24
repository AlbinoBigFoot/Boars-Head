---
title: "InterlockPanel"
sidebar_label: "InterlockPanel"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/InterlockPanel (Asset (embedded piece)): 267 components, 807 bindings, 87 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/InterlockPanel", "InterlockPanel"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/InterlockPanel`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/InterlockPanel` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/InterlockPanel/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; InterlockPanel |
| Root | `ia.container.flex`, height 632, width 560 |
| Size | 267 components, 807 bindings, 87 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-25T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `vertical` | `true` | input |

## Custom properties

<details>
<summary>53 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `selected` | `"Home"` | |
| `engPage` | `1` | |
| `pax` | `""` | bound (expr) |
| `paxRoot` | `""` | bound (expr) |
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
| `qg25` | `null` | bound (expr) |
| `qg26` | `null` | bound (expr) |
| `qg27` | `null` | bound (expr) |
| `qg28` | `null` | bound (expr) |
| `qg29` | `null` | bound (expr) |
| `qg30` | `null` | bound (expr) |
| `qg31` | `null` | bound (expr) |
| `qg32` | `null` | bound (expr) |
| `qg33` | `null` | bound (expr) |
| `qg34` | `null` | bound (expr) |
| `qg35` | `null` | bound (expr) |
| `qg36` | `null` | bound (expr) |
| `qg37` | `null` | bound (expr) |
| `qg38` | `null` | bound (expr) |
| `qg39` | `null` | bound (expr) |
| `qg40` | `null` | bound (expr) |
| `qg41` | `null` | bound (expr) |
| `qg42` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roConfiguration` | `true` | bound (expr) |
| `tipConfiguration` | `""` | bound (expr) |
| `roInterlocks` | `true` | bound (expr) |
| `tipInterlocks` | `""` | bound (expr) |
| `qg43` | `null` | bound (expr) |

</details>

## Component Tree

Component types: ia.container.flex x82, ia.display.icon x81, ia.display.label x80, ia.display.view x17, ia.input.button x7.

<details>
<summary>Component tree (267 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Content  ia.container.flex  [2 bindings]
    Tabs  ia.container.flex  [5 bindings]
      Home  ia.input.button  [3 bindings; 1 event]
      Maintenance  ia.input.button  [3 bindings; 1 event]
      Engineering  ia.input.button  [4 bindings; 1 event]
    Body  ia.container.flex
      Home  ia.container.flex  [5 bindings]
        StatusRow  ia.container.flex
          IntlkIcon  ia.display.icon  [2 bindings]
          BypassState  ia.display.label  [1 binding]
          Spacer  ia.container.flex
          BtnReset  ia.input.button  [4 bindings; 1 event]
        Conditions  ia.container.flex
          ConditionsTitle  ia.display.label  [1 binding]
          Empty  ia.display.label  [1 binding]
          Cond00  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond01  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond02  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond03  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond04  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond05  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond06  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond07  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond08  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond09  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond10  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond11  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond12  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond13  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond14  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
          Cond15  ia.container.flex  [3 bindings]
            Mark  ia.display.icon  [2 bindings]
            Cond  ia.display.label  [1 binding]
        Legend  ia.display.label
      Maintenance  ia.container.flex  [5 bindings]
        Bypass  ia.container.flex
          BypassTitle  ia.display.label
          ColHdr  ia.container.flex
            HCond  ia.display.label
            HBypass  ia.display.label
          Cond00  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond01  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond02  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond03  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond04  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond05  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond06  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond07  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond08  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond09  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond10  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond11  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond12  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond13  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond14  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
          Cond15  ia.container.flex  [1 binding]
            Cond  ia.display.label  [1 binding]
            Bypass  ia.display.icon  [6 bindings; 1 event]
        Hint  ia.display.label
      Engineering  ia.container.flex  [5 bindings]
        PageRow  ia.container.flex  [1 binding]
          Page1  ia.input.button  [2 bindings; 1 event]
          Page2  ia.input.button  [2 bindings; 1 event]
          Page3  ia.input.button  [2 bindings; 1 event]
        Page1  ia.container.flex  [5 bindings]
          General  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
        Page2Title  ia.display.label  [1 binding]
        Page2  ia.container.flex  [5 bindings]
          ColHdr  ia.container.flex
            HCond  ia.display.label
            HOk  ia.display.label
            HByp  ia.display.label
            HLatch  ia.display.label
          Cond00  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond01  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond02  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond03  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond04  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond05  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond06  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond07  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond08  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond09  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond10  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond11  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond12  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond13  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond14  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
          Cond15  ia.container.flex  [1 binding]
            CondText  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
            OkState  ia.display.label  [4 bindings; 1 event]
            CanBypass  ia.display.icon  [6 bindings; 1 event]
            MustReset  ia.display.icon  [6 bindings; 1 event]
        Page3Title  ia.display.label  [1 binding]
        Page3  ia.container.flex  [5 bindings]
          ColHdr  ia.container.flex
            HNav  ia.display.label
            HCond  ia.display.label
          Cond00  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond01  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond02  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond03  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond04  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond05  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond06  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond07  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond08  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond09  ia.container.flex  [1 binding]
            HasNav  ia.display.icon  [6 bindings; 1 event]
            Cond  ia.display.label  [1 binding]
          Cond10  ia.container.flex  [1 binding]
... 17 more components (see the Designer)
```

</details>

## Bindings

807 bindings: expr 803, property 4.

<details>
<summary>All 807 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression

```js
if(right(coalesce({view.params.tagPath}, ''), 10) = '/Interlock', case(toStr(coalesce(try(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/DIn.Enabled')), false), false), 'DIn', ''), ''), '')
```


- `custom.paxRoot`: expression

```js
if(right(coalesce({view.params.tagPath}, ''), 10) = '/Interlock', left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/Intlk', '')
```


- `custom.qg0`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Sts_IntlkOK')), tag({view.custom.paxRoot} + '/Sts_IntlkOK'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Sts_BypActive')), tag({view.custom.paxRoot} + '/Sts_BypActive'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Rdy_Reset')), tag({view.custom.paxRoot} + '/Rdy_Reset'), null), null)
```


- `custom.qg3`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_Desc')), tag({view.custom.paxRoot} + '/Cfg_Desc'), null), null)
```


- `custom.qg4`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_Tag')), tag({view.custom.paxRoot} + '/Cfg_Tag'), null), null)
```


- `custom.qg5`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_0_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_0_'), null), null)
```


- `custom.qg6`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Sts_Intlk')), tag({view.custom.paxRoot} + '/Sts_Intlk'), null), null)
```


- `custom.qg7`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_1_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_1_'), null), null)
```


- `custom.qg8`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_2_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_2_'), null), null)
```


- `custom.qg9`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_3_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_3_'), null), null)
```


- `custom.qg10`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_4_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_4_'), null), null)
```


- `custom.qg11`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_5_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_5_'), null), null)
```


- `custom.qg12`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_6_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_6_'), null), null)
```


- `custom.qg13`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_7_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_7_'), null), null)
```


- `custom.qg14`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_8_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_8_'), null), null)
```


- `custom.qg15`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_9_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_9_'), null), null)
```


- `custom.qg16`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_10_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_10_'), null), null)
```


- `custom.qg17`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_11_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_11_'), null), null)
```


- `custom.qg18`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_12_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_12_'), null), null)
```


- `custom.qg19`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_13_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_13_'), null), null)
```


- `custom.qg20`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_14_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_14_'), null), null)
```


- `custom.qg21`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_15_')), tag({view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_15_'), null), null)
```


- `custom.qg22`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Sts_FirstOut')), tag({view.custom.paxRoot} + '/Sts_FirstOut'), null), null)
```


- `custom.qg23`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass00')), tag({view.custom.paxRoot} + '/MSet_Bypass00'), null), null)
```


- `custom.qg24`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_Bypassable')), tag({view.custom.paxRoot} + '/Cfg_Bypassable'), null), null)
```


- `custom.qg25`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass01')), tag({view.custom.paxRoot} + '/MSet_Bypass01'), null), null)
```


- `custom.qg26`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass02')), tag({view.custom.paxRoot} + '/MSet_Bypass02'), null), null)
```


- `custom.qg27`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass03')), tag({view.custom.paxRoot} + '/MSet_Bypass03'), null), null)
```


- `custom.qg28`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass04')), tag({view.custom.paxRoot} + '/MSet_Bypass04'), null), null)
```


- `custom.qg29`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass05')), tag({view.custom.paxRoot} + '/MSet_Bypass05'), null), null)
```


- `custom.qg30`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass06')), tag({view.custom.paxRoot} + '/MSet_Bypass06'), null), null)
```


- `custom.qg31`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass07')), tag({view.custom.paxRoot} + '/MSet_Bypass07'), null), null)
```


- `custom.qg32`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass08')), tag({view.custom.paxRoot} + '/MSet_Bypass08'), null), null)
```


- `custom.qg33`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass09')), tag({view.custom.paxRoot} + '/MSet_Bypass09'), null), null)
```


- `custom.qg34`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass10')), tag({view.custom.paxRoot} + '/MSet_Bypass10'), null), null)
```


- `custom.qg35`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass11')), tag({view.custom.paxRoot} + '/MSet_Bypass11'), null), null)
```


- `custom.qg36`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass12')), tag({view.custom.paxRoot} + '/MSet_Bypass12'), null), null)
```


- `custom.qg37`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass13')), tag({view.custom.paxRoot} + '/MSet_Bypass13'), null), null)
```


- `custom.qg38`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass14')), tag({view.custom.paxRoot} + '/MSet_Bypass14'), null), null)
```


- `custom.qg39`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/MSet_Bypass15')), tag({view.custom.paxRoot} + '/MSet_Bypass15'), null), null)
```


- `custom.qg40`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_OKState')), tag({view.custom.paxRoot} + '/Cfg_OKState'), null), null)
```


- `custom.qg41`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_Latched')), tag({view.custom.paxRoot} + '/Cfg_Latched'), null), null)
```


- `custom.qg42`: expression

```js
try(if(isGood(tag({view.custom.paxRoot} + '/Cfg_HasNav')), tag({view.custom.paxRoot} + '/Cfg_HasNav'), null), null)
```


- `custom.permDevice`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', coalesce(try(lookup({view.custom.qg43}, toStr(coalesce(try(tag({view.params.tagPath} + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg43}, toStr(coalesce(try(tag(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg43}, toStr(coalesce(try(tag(left(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')), lastIndexOf(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')), '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), ''))
```


- `custom.roConfiguration`: expression

```js
coalesce({session.custom.EngineeringReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), true)
```


- `custom.tipConfiguration`: expression

```js
if(!coalesce({session.custom.EngineeringReadOnly}, true) && coalesce({view.custom.roConfiguration}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), 'Setpoint', 'Configuration') + ' (Roles & Permissions)', '')
```


- `custom.roInterlocks`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Interlocks'], null), true)
```


- `custom.tipInterlocks`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roInterlocks}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Interlocks' + ' (Roles & Permissions)', '')
```


- `custom.qg43`: expression

```js
try(if(isGood(tag('[default]_Config/Security/DeviceTypes')), tag('[default]_Config/Security/DeviceTypes'), null), null)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Content`**

- `props.direction`: expression

```js
if(coalesce({view.params.vertical}, true), 'row', 'column')
```


- `props.style.classes`: expression

```js
if(coalesce({view.params.vertical}, true), 'faceplate-content faceplate-tabs-vertical', 'faceplate-content')
```


**`root/Content/Tabs`**

- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '144px', '48px')
```


- `props.direction`: expression

```js
if(coalesce({view.params.vertical}, true), 'column', 'row')
```


- `props.alignItems`: expression

```js
if(coalesce({view.params.vertical}, true), 'stretch', 'flex-end')
```


- `props.style.classes`: expression

```js
'faceplate-buttons-3' + if(coalesce({view.params.vertical}, true), ' faceplate-tabs-vertical', '')
```


- `position.display`: expression

```js
coalesce({view.params.vertical}, true)
```


**`root/Content/Tabs/Home`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '68px', '112px')
```


**`root/Content/Tabs/Maintenance`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '68px', '112px')
```


**`root/Content/Tabs/Engineering`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '68px', '112px')
```


- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Content/Body/Home`**

- `position.display`: expression

```js
!coalesce({view.params.vertical}, true) || ({view.custom.selected} = 'Home')
```


- `position.grow`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '0px', 'auto')
```


- `position.shrink`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `props.style.overflow`: expression

```js
if(coalesce({view.params.vertical}, true), 'hidden auto', 'visible')
```


**`root/Content/Body/Home/StatusRow/IntlkIcon`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), false), 'material/check_circle', 'material/error')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), false), '#2E7D32', 'var(--status-level-critical)')
```


**`root/Content/Body/Home/StatusRow/BypassState`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false), 'Bypassed', 'Enabled'))
```


**`root/Content/Body/Home/StatusRow/BtnReset`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roInterlocks}, false) && !({view.params.tagPath} = '') && coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Home/Conditions/ConditionsTitle`**

- `props.text`: expression

```js
if(coalesce(try(toStr({view.custom.qg3}), ''), '') != '', if(coalesce(try(toStr({view.custom.qg4}), ''), '') != '', coalesce(try(toStr({view.custom.qg4}), ''), '') + ' - ' + coalesce(try(toStr({view.custom.qg3}), ''), ''), coalesce(try(toStr({view.custom.qg3}), ''), '')), if(coalesce(try(toStr({view.custom.qg4}), ''), '') != '', coalesce(try(toStr({view.custom.qg4}), ''), ''), 'Interlocks'))
```


**`root/Content/Body/Home/Conditions/Empty`**

- `position.display`: expression

```js
!(((coalesce(try(toStr({view.custom.qg5}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 0) = 1)) || ((coalesce(try(toStr({view.custom.qg7}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 1) = 1)) || ((coalesce(try(toStr({view.custom.qg8}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 2) = 1)) || ((coalesce(try(toStr({view.custom.qg9}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 3) = 1)) || ((coalesce(try(toStr({view.custom.qg10}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 4) = 1)) || ((coalesce(try(toStr({view.custom.qg11}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 5) = 1)) || ((coalesce(try(toStr({view.custom.qg12}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 6) = 1)) || ((coalesce(try(toStr({view.custom.qg13}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 7) = 1)) || ((coalesce(try(toStr({view.custom.qg14}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 8) = 1)) || ((coalesce(try(toStr({view.custom.qg15}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 9) = 1)) || ((coalesce(try(toStr({view.custom.qg16}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 10) = 1)) || ((coalesce(try(toStr({view.custom.qg17}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 11) = 1)) || ((coalesce(try(toStr({view.custom.qg18}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 12) = 1)) || ((coalesce(try(toStr({view.custom.qg19}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 13) = 1)) || ((coalesce(try(toStr({view.custom.qg20}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 14) = 1)) || ((coalesce(try(toStr({view.custom.qg21}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 15) = 1)))
```


**`root/Content/Body/Home/Conditions/Cond00`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg5}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 0) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 0) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 0) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond00/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 0) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 0) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond00/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg5}), ''), '') != ''), coalesce(try(toStr({view.custom.qg5}), ''), ''), 'Condition 00 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond01`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg7}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 1) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 1) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 1) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond01/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 1) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 1) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond01/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg7}), ''), '') != ''), coalesce(try(toStr({view.custom.qg7}), ''), ''), 'Condition 01 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond02`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg8}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 2) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 2) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 2) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond02/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 2) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 2) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond02/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg8}), ''), '') != ''), coalesce(try(toStr({view.custom.qg8}), ''), ''), 'Condition 02 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond03`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg9}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 3) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 3) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 3) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond03/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 3) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 3) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond03/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg9}), ''), '') != ''), coalesce(try(toStr({view.custom.qg9}), ''), ''), 'Condition 03 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond04`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg10}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 4) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 4) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 4) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond04/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 4) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 4) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond04/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg10}), ''), '') != ''), coalesce(try(toStr({view.custom.qg10}), ''), ''), 'Condition 04 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond05`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg11}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 5) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 5) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 5) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond05/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 5) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 5) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond05/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg11}), ''), '') != ''), coalesce(try(toStr({view.custom.qg11}), ''), ''), 'Condition 05 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond06`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg12}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 6) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 6) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 6) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond06/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 6) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 6) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond06/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg12}), ''), '') != ''), coalesce(try(toStr({view.custom.qg12}), ''), ''), 'Condition 06 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond07`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg13}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 7) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 7) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 7) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond07/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 7) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 7) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond07/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg13}), ''), '') != ''), coalesce(try(toStr({view.custom.qg13}), ''), ''), 'Condition 07 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond08`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg14}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 8) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 8) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 8) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond08/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 8) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 8) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond08/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg14}), ''), '') != ''), coalesce(try(toStr({view.custom.qg14}), ''), ''), 'Condition 08 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond09`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg15}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 9) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 9) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 9) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond09/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 9) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 9) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond09/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg15}), ''), '') != ''), coalesce(try(toStr({view.custom.qg15}), ''), ''), 'Condition 09 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond10`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg16}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 10) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 10) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 10) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond10/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 10) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 10) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond10/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg16}), ''), '') != ''), coalesce(try(toStr({view.custom.qg16}), ''), ''), 'Condition 10 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond11`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg17}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 11) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 11) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 11) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond11/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 11) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 11) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond11/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg17}), ''), '') != ''), coalesce(try(toStr({view.custom.qg17}), ''), ''), 'Condition 11 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond12`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg18}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 12) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 12) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 12) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond12/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 12) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 12) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond12/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg18}), ''), '') != ''), coalesce(try(toStr({view.custom.qg18}), ''), ''), 'Condition 12 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond13`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg19}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 13) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 13) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 13) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond13/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 13) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 13) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond13/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg19}), ''), '') != ''), coalesce(try(toStr({view.custom.qg19}), ''), ''), 'Condition 13 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond14`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg20}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 14) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 14) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 14) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond14/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 14) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 14) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond14/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg20}), ''), '') != ''), coalesce(try(toStr({view.custom.qg20}), ''), ''), 'Condition 14 (No Description)')
```


**`root/Content/Body/Home/Conditions/Cond15`**

- `position.display`: expression

```js
((coalesce(try(toStr({view.custom.qg21}), ''), '') != '') || (getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 15) = 1))
```


- `props.style.backgroundColor`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 15) = 1), '#FFF176', '')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg22}), 0), 0), 15) = 1), '#000000', '')
```


**`root/Content/Body/Home/Conditions/Cond15/Mark`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 15) = 1), 'material/close', 'material/check')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg6}), 0), 0), 15) = 1), 'var(--status-level-critical)', '#2E7D32')
```


**`root/Content/Body/Home/Conditions/Cond15/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg21}), ''), '') != ''), coalesce(try(toStr({view.custom.qg21}), ''), ''), 'Condition 15 (No Description)')
```


**`root/Content/Body/Maintenance`**

- `position.display`: expression

```js
!coalesce({view.params.vertical}, true) || ({view.custom.selected} = 'Maintenance')
```


- `position.grow`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '0px', 'auto')
```


- `position.shrink`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `props.style.overflow`: expression

```js
if(coalesce({view.params.vertical}, true), 'hidden auto', 'visible')
```


**`root/Content/Body/Maintenance/Bypass/Cond00`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg5}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond00/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg5}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond00/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg23}), null, {view.custom.qg23}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg23}), null, {view.custom.qg23}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 0) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 0) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 0) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond01`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg7}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond01/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg7}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond01/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg25}), null, {view.custom.qg25}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg25}), null, {view.custom.qg25}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 1) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 1) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 1) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond02`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg8}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond02/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg8}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond02/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg26}), null, {view.custom.qg26}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg26}), null, {view.custom.qg26}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 2) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 2) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 2) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond03`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg9}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond03/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg9}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond03/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg27}), null, {view.custom.qg27}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg27}), null, {view.custom.qg27}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 3) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 3) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 3) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond04`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg10}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond04/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg10}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond04/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg28}), null, {view.custom.qg28}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg28}), null, {view.custom.qg28}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 4) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 4) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 4) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond05`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg11}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond05/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg11}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond05/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg29}), null, {view.custom.qg29}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg29}), null, {view.custom.qg29}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 5) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 5) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 5) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond06`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg12}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond06/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg12}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond06/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg30}), null, {view.custom.qg30}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg30}), null, {view.custom.qg30}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 6) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 6) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 6) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond07`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg13}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond07/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg13}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond07/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg31}), null, {view.custom.qg31}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg31}), null, {view.custom.qg31}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 7) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 7) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 7) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond08`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg14}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond08/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg14}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond08/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg32}), null, {view.custom.qg32}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg32}), null, {view.custom.qg32}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 8) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 8) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 8) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond09`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg15}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond09/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg15}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond09/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg33}), null, {view.custom.qg33}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg33}), null, {view.custom.qg33}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 9) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 9) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 9) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond10`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg16}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond10/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg16}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond10/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg34}), null, {view.custom.qg34}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg34}), null, {view.custom.qg34}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 10) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 10) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 10) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond11`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg17}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond11/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg17}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond11/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg35}), null, {view.custom.qg35}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg35}), null, {view.custom.qg35}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 11) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 11) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 11) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond12`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg18}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond12/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg18}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond12/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg36}), null, {view.custom.qg36}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg36}), null, {view.custom.qg36}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 12) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 12) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 12) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond13`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg19}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond13/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg19}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond13/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg37}), null, {view.custom.qg37}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg37}), null, {view.custom.qg37}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 13) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 13) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 13) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond14`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg20}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond14/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg20}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond14/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg38}), null, {view.custom.qg38}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg38}), null, {view.custom.qg38}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 14) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 14) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 14) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Maintenance/Bypass/Cond15`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg21}), ''), '') != '')
```


**`root/Content/Body/Maintenance/Bypass/Cond15/Cond`**

- `props.text`: expression

```js
coalesce(try(toStr({view.custom.qg21}), ''), '')
```


**`root/Content/Body/Maintenance/Bypass/Cond15/Bypass`**

- `props.path`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg39}), null, {view.custom.qg39}), null), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg39}), null, {view.custom.qg39}), null), false), '#2E7D32', if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 15) = 1)), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 15) = 1)), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if((!coalesce({view.custom.roInterlocks}, false) && (getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 15) = 1)), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/Content/Body/Engineering`**

- `position.display`: expression

```js
(!coalesce({view.params.vertical}, true) || ({view.custom.selected} = 'Engineering')) && coalesce({session.custom.EngineeringView}, false)
```


- `position.grow`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '0px', 'auto')
```


- `position.shrink`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `props.style.overflow`: expression

```js
if(coalesce({view.params.vertical}, true), 'hidden auto', 'visible')
```


**`root/Content/Body/Engineering/PageRow`**

- `position.display`: expression

```js
coalesce({view.params.vertical}, true)
```


**`root/Content/Body/Engineering/PageRow/Page1`**

- `props.enabled`: expression

```js
true
```


- `props.style.classes`: expression

```js
if({view.custom.engPage} = 1, 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


**`root/Content/Body/Engineering/PageRow/Page2`**

- `props.enabled`: expression

```js
true
```


- `props.style.classes`: expression

```js
if({view.custom.engPage} = 2, 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


**`root/Content/Body/Engineering/PageRow/Page3`**

- `props.enabled`: expression

```js
true
```


- `props.style.classes`: expression

```js
if({view.custom.engPage} = 3, 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


**`root/Content/Body/Engineering/Page1`**

- `position.display`: expression

```js
!coalesce({view.params.vertical}, true) || ({view.custom.engPage} = 1)
```


- `position.grow`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '0px', 'auto')
```


- `position.shrink`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `props.style.overflow`: expression

```js
if(coalesce({view.params.vertical}, true), 'hidden auto', 'visible')
```


**`root/Content/Body/Engineering/Page1/General`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../common-patterns.md#pattern-5).

**`root/Content/Body/Engineering/Page2Title`**

- `position.display`: expression

```js
!coalesce({view.params.vertical}, true)
```


**`root/Content/Body/Engineering/Page2`**

- `position.display`: expression

```js
!coalesce({view.params.vertical}, true) || ({view.custom.engPage} = 2)
```


- `position.grow`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '0px', 'auto')
```


- `position.shrink`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `props.style.overflow`: expression

```js
if(coalesce({view.params.vertical}, true), 'hidden auto', 'visible')
```


**`root/Content/Body/Engineering/Page2/Cond00`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg5}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond00/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_0_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond00/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 0) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 0) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond00/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 0) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 0) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond00/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 0) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 0) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond01`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg7}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond01/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_1_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond01/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 1) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 1) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond01/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 1) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 1) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond01/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 1) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 1) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond02`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg8}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond02/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_2_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond02/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 2) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 2) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond02/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 2) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 2) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond02/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 2) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 2) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond03`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg9}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond03/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_3_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond03/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 3) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 3) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond03/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 3) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 3) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond03/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 3) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 3) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond04`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg10}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond04/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_4_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond04/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 4) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 4) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond04/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 4) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 4) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond04/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 4) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 4) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond05`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg11}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond05/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_5_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond05/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 5) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 5) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond05/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 5) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 5) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond05/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 5) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 5) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond06`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg12}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond06/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_6_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond06/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 6) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 6) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond06/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 6) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 6) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond06/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 6) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 6) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond07`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg13}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond07/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_7_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond07/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 7) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 7) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond07/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 7) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 7) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond07/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 7) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 7) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond08`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg14}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond08/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_8_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond08/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 8) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 8) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond08/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 8) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 8) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond08/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 8) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 8) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond09`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg15}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond09/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_9_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond09/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 9) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 9) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond09/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 9) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 9) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond09/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 9) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 9) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond10`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg16}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond10/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_10_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond10/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 10) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 10) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond10/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 10) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 10) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond10/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 10) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 10) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond11`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg17}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond11/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_11_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond11/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 11) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 11) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond11/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 11) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 11) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond11/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 11) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 11) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond12`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg18}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond12/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_12_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond12/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 12) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 12) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond12/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 12) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 12) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond12/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 12) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 12) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond13`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg19}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond13/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_13_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond13/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 13) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 13) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond13/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 13) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 13) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond13/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 13) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 13) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond14`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg20}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond14/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_14_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond14/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 14) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 14) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond14/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 14) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 14) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond14/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 14) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 14) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond15`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg21}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page2/Cond15/CondText`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.custom.paxRoot} + '/Cfg_CondTxt/Cfg_CondTxt_15_')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond15/OkState`**

- `props.text`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 15) = 1), '1', '0')
```


- `props.style.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg40}), 0), 0), 15) = 1), '#2E7D32', 'var(--text-muted)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond15/CanBypass`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 15) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg24}), 0), 0), 15) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page2/Cond15/MustReset`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 15) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg41}), 0), 0), 15) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3Title`**

- `position.display`: expression

```js
!coalesce({view.params.vertical}, true)
```


**`root/Content/Body/Engineering/Page3`**

- `position.display`: expression

```js
!coalesce({view.params.vertical}, true) || ({view.custom.engPage} = 3)
```


- `position.grow`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `position.basis`: expression

```js
if(coalesce({view.params.vertical}, true), '0px', 'auto')
```


- `position.shrink`: expression

```js
if(coalesce({view.params.vertical}, true), 1, 0)
```


- `props.style.overflow`: expression

```js
if(coalesce({view.params.vertical}, true), 'hidden auto', 'visible')
```


**`root/Content/Body/Engineering/Page3/Cond00`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg5}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond00/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 0) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 0) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond00/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg5}), ''), '') != ''), coalesce(try(toStr({view.custom.qg5}), ''), ''), 'Condition 00')
```


**`root/Content/Body/Engineering/Page3/Cond01`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg7}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond01/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 1) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 1) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond01/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg7}), ''), '') != ''), coalesce(try(toStr({view.custom.qg7}), ''), ''), 'Condition 01')
```


**`root/Content/Body/Engineering/Page3/Cond02`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg8}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond02/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 2) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 2) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond02/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg8}), ''), '') != ''), coalesce(try(toStr({view.custom.qg8}), ''), ''), 'Condition 02')
```


**`root/Content/Body/Engineering/Page3/Cond03`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg9}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond03/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 3) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 3) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond03/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg9}), ''), '') != ''), coalesce(try(toStr({view.custom.qg9}), ''), ''), 'Condition 03')
```


**`root/Content/Body/Engineering/Page3/Cond04`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg10}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond04/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 4) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 4) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond04/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg10}), ''), '') != ''), coalesce(try(toStr({view.custom.qg10}), ''), ''), 'Condition 04')
```


**`root/Content/Body/Engineering/Page3/Cond05`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg11}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond05/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 5) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 5) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond05/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg11}), ''), '') != ''), coalesce(try(toStr({view.custom.qg11}), ''), ''), 'Condition 05')
```


**`root/Content/Body/Engineering/Page3/Cond06`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg12}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond06/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 6) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 6) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond06/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg12}), ''), '') != ''), coalesce(try(toStr({view.custom.qg12}), ''), ''), 'Condition 06')
```


**`root/Content/Body/Engineering/Page3/Cond07`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg13}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond07/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 7) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 7) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond07/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg13}), ''), '') != ''), coalesce(try(toStr({view.custom.qg13}), ''), ''), 'Condition 07')
```


**`root/Content/Body/Engineering/Page3/Cond08`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg14}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond08/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 8) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 8) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond08/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg14}), ''), '') != ''), coalesce(try(toStr({view.custom.qg14}), ''), ''), 'Condition 08')
```


**`root/Content/Body/Engineering/Page3/Cond09`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg15}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond09/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 9) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 9) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond09/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg15}), ''), '') != ''), coalesce(try(toStr({view.custom.qg15}), ''), ''), 'Condition 09')
```


**`root/Content/Body/Engineering/Page3/Cond10`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg16}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond10/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 10) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 10) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond10/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg16}), ''), '') != ''), coalesce(try(toStr({view.custom.qg16}), ''), ''), 'Condition 10')
```


**`root/Content/Body/Engineering/Page3/Cond11`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg17}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond11/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 11) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 11) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond11/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg17}), ''), '') != ''), coalesce(try(toStr({view.custom.qg17}), ''), ''), 'Condition 11')
```


**`root/Content/Body/Engineering/Page3/Cond12`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg18}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond12/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 12) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 12) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond12/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg18}), ''), '') != ''), coalesce(try(toStr({view.custom.qg18}), ''), ''), 'Condition 12')
```


**`root/Content/Body/Engineering/Page3/Cond13`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg19}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond13/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 13) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 13) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond13/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg19}), ''), '') != ''), coalesce(try(toStr({view.custom.qg19}), ''), ''), 'Condition 13')
```


**`root/Content/Body/Engineering/Page3/Cond14`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg20}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond14/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 14) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 14) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond14/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg20}), ''), '') != ''), coalesce(try(toStr({view.custom.qg20}), ''), ''), 'Condition 14')
```


**`root/Content/Body/Engineering/Page3/Cond15`**

- `position.display`: expression

```js
(coalesce(try(toStr({view.custom.qg21}), ''), '') != '')
```


**`root/Content/Body/Engineering/Page3/Cond15/HasNav`**

- `props.path`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 15) = 1), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if((getBit(coalesce(try(toInt({view.custom.qg42}), 0), 0), 15) = 1), '#2E7D32', if(!coalesce({view.custom.roConfiguration}, false), 'var(--text)', 'var(--text-muted)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `props.style.cursor`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 'pointer', 'not-allowed')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Engineering/Page3/Cond15/Cond`**

- `props.text`: expression

```js
if((coalesce(try(toStr({view.custom.qg21}), ''), '') != ''), coalesce(try(toStr({view.custom.qg21}), ''), ''), 'Condition 15')
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 88 event actions, change scripts and handlers</summary>

- **`root/Content/Tabs/Home`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Maintenance`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Engineering`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Body/Home/StatusRow/BtnReset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/OCmd_Reset'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Reset',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond00/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass00'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 00',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond01/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass01'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 01',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond02/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass02'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 02',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond03/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass03'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 03',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond04/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass04'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 04',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond05/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass05'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 05',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond06/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass06'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 06',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond07/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass07'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 07',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond08/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass08'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 08',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond09/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass09'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 09',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond10/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass10'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 10',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond11/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass11'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 11',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond12/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass12'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 12',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond13/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass13'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 13',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond14/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass14'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 14',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Maintenance/Bypass/Cond15/Bypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roInterlocks:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/MSet_Bypass15'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Interlock Bypass 15',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/PageRow/Page1`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.engPage = 1
```

- **`root/Content/Body/Engineering/PageRow/Page2`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.engPage = 2
```

- **`root/Content/Body/Engineering/PageRow/Page3`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.engPage = 3
```

- **`root/Content/Body/Engineering/Page2/Cond00/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 00',
    tagPath=path,
    newValue=cur ^ (1 << 0),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond00/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 00',
    tagPath=path,
    newValue=cur ^ (1 << 0),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond00/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 00',
    tagPath=path,
    newValue=cur ^ (1 << 0),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond01/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 01',
    tagPath=path,
    newValue=cur ^ (1 << 1),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond01/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 01',
    tagPath=path,
    newValue=cur ^ (1 << 1),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond01/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 01',
    tagPath=path,
    newValue=cur ^ (1 << 1),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond02/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 02',
    tagPath=path,
    newValue=cur ^ (1 << 2),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond02/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 02',
    tagPath=path,
    newValue=cur ^ (1 << 2),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond02/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 02',
    tagPath=path,
    newValue=cur ^ (1 << 2),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond03/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 03',
    tagPath=path,
    newValue=cur ^ (1 << 3),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond03/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 03',
    tagPath=path,
    newValue=cur ^ (1 << 3),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond03/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 03',
    tagPath=path,
    newValue=cur ^ (1 << 3),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond04/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 04',
    tagPath=path,
    newValue=cur ^ (1 << 4),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond04/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 04',
    tagPath=path,
    newValue=cur ^ (1 << 4),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond04/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 04',
    tagPath=path,
    newValue=cur ^ (1 << 4),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond05/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 05',
    tagPath=path,
    newValue=cur ^ (1 << 5),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond05/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 05',
    tagPath=path,
    newValue=cur ^ (1 << 5),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond05/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 05',
    tagPath=path,
    newValue=cur ^ (1 << 5),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond06/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 06',
    tagPath=path,
    newValue=cur ^ (1 << 6),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond06/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 06',
    tagPath=path,
    newValue=cur ^ (1 << 6),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond06/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 06',
    tagPath=path,
    newValue=cur ^ (1 << 6),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond07/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 07',
    tagPath=path,
    newValue=cur ^ (1 << 7),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond07/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 07',
    tagPath=path,
    newValue=cur ^ (1 << 7),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond07/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 07',
    tagPath=path,
    newValue=cur ^ (1 << 7),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond08/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 08',
    tagPath=path,
    newValue=cur ^ (1 << 8),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond08/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 08',
    tagPath=path,
    newValue=cur ^ (1 << 8),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond08/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 08',
    tagPath=path,
    newValue=cur ^ (1 << 8),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond09/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 09',
    tagPath=path,
    newValue=cur ^ (1 << 9),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond09/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 09',
    tagPath=path,
    newValue=cur ^ (1 << 9),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond09/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 09',
    tagPath=path,
    newValue=cur ^ (1 << 9),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond10/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 10',
    tagPath=path,
    newValue=cur ^ (1 << 10),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond10/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 10',
    tagPath=path,
    newValue=cur ^ (1 << 10),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond10/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 10',
    tagPath=path,
    newValue=cur ^ (1 << 10),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond11/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 11',
    tagPath=path,
    newValue=cur ^ (1 << 11),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond11/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 11',
    tagPath=path,
    newValue=cur ^ (1 << 11),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond11/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 11',
    tagPath=path,
    newValue=cur ^ (1 << 11),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond12/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 12',
    tagPath=path,
    newValue=cur ^ (1 << 12),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond12/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 12',
    tagPath=path,
    newValue=cur ^ (1 << 12),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond12/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 12',
    tagPath=path,
    newValue=cur ^ (1 << 12),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond13/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 13',
    tagPath=path,
    newValue=cur ^ (1 << 13),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond13/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 13',
    tagPath=path,
    newValue=cur ^ (1 << 13),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond13/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 13',
    tagPath=path,
    newValue=cur ^ (1 << 13),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond14/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 14',
    tagPath=path,
    newValue=cur ^ (1 << 14),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond14/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 14',
    tagPath=path,
    newValue=cur ^ (1 << 14),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond14/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 14',
    tagPath=path,
    newValue=cur ^ (1 << 14),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond15/OkState`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_OKState'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock OK State 15',
    tagPath=path,
    newValue=cur ^ (1 << 15),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond15/CanBypass`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Bypassable'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Can Bypass 15',
    tagPath=path,
    newValue=cur ^ (1 << 15),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page2/Cond15/MustReset`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_Latched'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Must Reset 15',
    tagPath=path,
    newValue=cur ^ (1 << 15),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond00/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 00',
    tagPath=path,
    newValue=cur ^ (1 << 0),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond01/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 01',
    tagPath=path,
    newValue=cur ^ (1 << 1),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond02/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 02',
    tagPath=path,
    newValue=cur ^ (1 << 2),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond03/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 03',
    tagPath=path,
    newValue=cur ^ (1 << 3),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond04/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 04',
    tagPath=path,
    newValue=cur ^ (1 << 4),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond05/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 05',
    tagPath=path,
    newValue=cur ^ (1 << 5),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond06/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 06',
    tagPath=path,
    newValue=cur ^ (1 << 6),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond07/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 07',
    tagPath=path,
    newValue=cur ^ (1 << 7),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond08/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 08',
    tagPath=path,
    newValue=cur ^ (1 << 8),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond09/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 09',
    tagPath=path,
    newValue=cur ^ (1 << 9),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond10/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 10',
    tagPath=path,
    newValue=cur ^ (1 << 10),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond11/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 11',
    tagPath=path,
    newValue=cur ^ (1 << 11),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond12/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 12',
    tagPath=path,
    newValue=cur ^ (1 << 12),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond13/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 13',
    tagPath=path,
    newValue=cur ^ (1 << 13),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond14/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 14',
    tagPath=path,
    newValue=cur ^ (1 << 14),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Engineering/Page3/Cond15/HasNav`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if not self.props.style.cursor == 'pointer':
    return
if self.view.custom.roConfiguration:
    return
base = self.view.custom.paxRoot
if not base:
    return
path = base + '/Cfg_HasNav'
cur = int(system.tag.readBlocking([path])[0].value or 0)
shared.Alerts.confirmApplyWrite(
    label='Interlock Allow Navigation 15',
    tagPath=path,
    newValue=cur ^ (1 << 15),
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (2): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](./configuration/configsection.md), [03\_Elements/00\_Control/StringInput](../../../03-elements/00-control/stringinput.md)

**Embedded in** (5): [01\_Popups/00\_Faceplates/Interlock](../interlock.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Interlocks](./compressor/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Interlocks](./evaporator/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Interlocks](./pump/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Interlocks](./tankoverview/interlocks.md)

## Style Classes

<details>
<summary>16 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 52 | style class |
| `Fonts/Value` | 32 | style class |
| `faceplate-body` | 1 | stylesheet |
| `faceplate-cmd-btn` | 4 | style class |
| `faceplate-cmd-row` | 1 | stylesheet |
| `faceplate-cmd-row-fill` | 1 | stylesheet |
| `faceplate-content` | 1 | stylesheet |
| `faceplate-interlock-colhdr` | 3 | stylesheet |
| `faceplate-section` | 2 | style class |
| `faceplate-section-card` | 2 | style class |
| `faceplate-section-title` | 4 | style class |
| `fw-700` | 7 | style class |
| `text-muted` | 3 | style class |
| `faceplate-button` | bound | stylesheet |
| `faceplate-button-selected` | bound | stylesheet |
| `faceplate-cmd-btn-active` | bound | style class |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>49 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_Bypassable`, `/Cfg_CondTxt/Cfg_CondTxt_0_`, `/Cfg_CondTxt/Cfg_CondTxt_10_`, `/Cfg_CondTxt/Cfg_CondTxt_11_`, `/Cfg_CondTxt/Cfg_CondTxt_12_`, `/Cfg_CondTxt/Cfg_CondTxt_13_`, `/Cfg_CondTxt/Cfg_CondTxt_14_`, `/Cfg_CondTxt/Cfg_CondTxt_15_`, `/Cfg_CondTxt/Cfg_CondTxt_1_`, `/Cfg_CondTxt/Cfg_CondTxt_2_`, `/Cfg_CondTxt/Cfg_CondTxt_3_`, `/Cfg_CondTxt/Cfg_CondTxt_4_`, `/Cfg_CondTxt/Cfg_CondTxt_5_`, `/Cfg_CondTxt/Cfg_CondTxt_6_`, `/Cfg_CondTxt/Cfg_CondTxt_7_`, `/Cfg_CondTxt/Cfg_CondTxt_8_`, `/Cfg_CondTxt/Cfg_CondTxt_9_`, `/Cfg_Desc`, `/Cfg_HasNav`, `/Cfg_Latched`, `/Cfg_OKState`, `/Cfg_Tag`, `/DIn.Enabled`, `/Intlk`, `/MSet_Bypass00`, `/MSet_Bypass01`, `/MSet_Bypass02`, `/MSet_Bypass03`, `/MSet_Bypass04`, `/MSet_Bypass05`, `/MSet_Bypass06`, `/MSet_Bypass07`, `/MSet_Bypass08`, `/MSet_Bypass09`, `/MSet_Bypass10`, `/MSet_Bypass11`, `/MSet_Bypass12`, `/MSet_Bypass13`, `/MSet_Bypass14`, `/MSet_Bypass15`, `/OCmd_Reset`, `/Rdy_Reset`, `/Sts_BypActive`, `/Sts_FirstOut`, `/Sts_Intlk`, `/Sts_IntlkOK`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
