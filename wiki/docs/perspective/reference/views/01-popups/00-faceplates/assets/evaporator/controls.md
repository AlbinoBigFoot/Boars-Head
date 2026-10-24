---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Evaporator/Controls (Asset (embedded piece)): 79 components, 65 bindings, 16 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Evaporator/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Evaporator/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Evaporator/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Evaporator &gt; Controls |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 79 components, 65 bindings, 16 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x44, ia.container.flex x30, ia.input.button x4, ia.display.view x1.

<details>
<summary>Component tree (79 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  StatusSection  ia.container.flex
    StatusSectionTitle  ia.display.label
    StatusBanner  ia.display.label  [2 bindings]
    StatusChips  ia.container.flex
      Enabled  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Perm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Intlk  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      TooHot  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      TooCold  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
  TempSection  ia.container.flex
    TempSectionTitle  ia.display.label
    Zat  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    Pressure  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings]
    TempInputs  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
  CommandsSection  ia.container.flex
    CommandsSectionTitle  ia.display.label
    EnableRow  ia.container.flex
      BtnEnable  ia.input.button  [5 bindings; 1 event]
      BtnSetBack  ia.input.button  [5 bindings; 1 event]
    DefrostRow  ia.container.flex
      BtnStartDefrost  ia.input.button  [4 bindings; 1 event]
      BtnStopDefrost  ia.input.button  [3 bindings; 1 event]
  DefrostSection  ia.container.flex
    DefrostSectionTitle  ia.display.label
    Mode  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings]
    FanMode  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings]
    TimeLeft  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    CoolingLeft  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    Runtime  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
  DevicesSection  ia.container.flex
    DevicesSectionTitle  ia.display.label
    ValveChips  ia.container.flex
      ValveLiquidSV  ia.container.flex  [1 event]
        Code  ia.display.label
        State  ia.display.label  [2 bindings; 1 event]
      ValveSuctionSV  ia.container.flex  [1 event]
        Code  ia.display.label
        State  ia.display.label  [2 bindings; 1 event]
      ValveHotGasSV  ia.container.flex  [1 event]
        Code  ia.display.label
        State  ia.display.label  [2 bindings; 1 event]
      ValveBleedSV  ia.container.flex  [1 binding; 1 event]
        Code  ia.display.label
        State  ia.display.label  [2 bindings; 1 event]
    FanChips  ia.container.flex
      Fan1  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Fan2  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Fan3  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
```

</details>

## Bindings

65 bindings: expr 64, property 1.

<details>
<summary>All 65 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roCommand`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Command'], null), true)
```


- `custom.tipCommand`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roCommand}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Command' + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/StatusSection/StatusBanner`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', if(try(!isGood(tag({view.params.tagPath} + '/HmiStatus')), true), 'COMM LOSS', case(coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1), 0, 'OFF', 1, 'COOLING', 2, 'DEFROST', 3, 'FAULT', 4, 'MANUAL', 5, 'IDLE', 6, 'DEFROST · PUMP DOWN', 7, 'DEFROST · HOT GAS', 8, 'DEFROST · BLEED', 9, 'DEFROST · FAN DELAY', 'UNKNOWN')))
```


- `props.style.classes`: expression

```js
'Refridgeration_STS faceplate-status-banner sts-' + if({view.params.tagPath} = '', 'UNKNOWN', if(try(!isGood(tag({view.params.tagPath} + '/HmiStatus')), true), 'COMMLOSS', case(coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1), 0, 'OFF', 1, 'COOLING', 2, 'DEFROST', 3, 'FAULT', 4, 'RUNNING', 5, 'IDLE', 6, 'DEFROST', 7, 'DEFROST', 8, 'DEFROST', 9, 'DEFROST', 'UNKNOWN')))
```


**`root/StatusSection/StatusChips/Enabled/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), null, tag({view.params.tagPath} + '/CG/HMIEnable')), null), false), 'ON', 'OFF')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), null, tag({view.params.tagPath} + '/CG/HMIEnable')), null), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-active')))))))))))))))))
```


**`root/StatusSection/StatusChips/Perm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), null, tag({view.params.tagPath} + '/CG/PermOK')), null), true), 'OK', 'NOT OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/PermOK')), null, tag({view.params.tagPath} + '/CG/PermOK')), null), true), 'faceplate-fault-state faceplate-fault-ok', 'faceplate-fault-state faceplate-fault-active')))))))))))))))))
```


**`root/StatusSection/StatusChips/Intlk/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), null, tag({view.params.tagPath} + '/CG/IntlkOK')), null), true), 'OK', 'NOT OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/IntlkOK')), null, tag({view.params.tagPath} + '/CG/IntlkOK')), null), true), 'faceplate-fault-state faceplate-fault-ok', 'faceplate-fault-state faceplate-fault-active')))))))))))))))))
```


**`root/StatusSection/StatusChips/TooHot/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), null, tag({view.params.tagPath} + '/CG/TooHot')), null), false), 'ACTIVE', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/TooHot')), null, tag({view.params.tagPath} + '/CG/TooHot')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/TooCold/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), null, tag({view.params.tagPath} + '/CG/TooCold')), null), false), 'ACTIVE', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/TooCold')), null, tag({view.params.tagPath} + '/CG/TooCold')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/TempSection/Zat/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/ZAT/Val'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/ZAT/Val' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), 'Fonts/Value value-bad', if((coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/TooHot')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/TooCold')), false), false)), 'Fonts/Value value-alarm', 'Fonts/Value'))
```


**`root/TempSection/Pressure/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/_NoPlc/Pressure'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/_NoPlc/Pressure' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/_NoPlc/Pressure')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/TempSection/TempInputs`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/CommandsSection/EnableRow/BtnEnable`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '')) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn value-bad', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), null, tag({view.params.tagPath} + '/CG/HMIEnable')), null), false), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label'))))))))))))))))
```


- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), null, tag({view.params.tagPath} + '/CG/HMIEnable')), null), false), 'Enabled', 'Disabled'))))))))))))))))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/CommandsSection/EnableRow/BtnSetBack`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '')) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn value-bad', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), null, tag({view.params.tagPath} + '/CG/SB_Enable')), null), false), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label'))))))))))))))))
```


- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), null, tag({view.params.tagPath} + '/CG/SB_Enable')), null), false), 'Set Back Enabled', 'Set Back Disabled'))))))))))))))))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/CommandsSection/DefrostRow/BtnStartDefrost`**

- `props.enabled`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false), (!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '') && !(coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) = 2 || (coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) >= 6 && coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) <= 9))) && coalesce({view.custom.pax}, '') = '', false)
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false), if((coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) = 2 || (coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) >= 6 && coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) <= 9)), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label'), '/HmiStatus value-bad')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/CommandsSection/DefrostRow/BtnStopDefrost`**

- `props.enabled`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false), (!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '') && (coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) = 2 || (coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) >= 6 && coalesce(try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1), -1) <= 9))) && coalesce({view.custom.pax}, '') = '', false)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/DefrostSection/Mode/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1), -1) < 0, '—', try(lookup({[default]_Config/Enums/Evaporator/DefrostStartMode}, coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1), -1), toStr(coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1), -1)), 'value', 'label'), toStr(coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1), -1))))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/DefrostSection/FanMode/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1), -1) < 0, '—', try(lookup({[default]_Config/Enums/Evaporator/CycleFans}, coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1), -1), toStr(coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1), -1)), 'value', 'label'), toStr(coalesce(try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1), -1))))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/DefrostSection/TimeLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/CG/Val_TimeLeft'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/CG/Val_TimeLeft' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_TimeLeft')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/DefrostSection/CoolingLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/CG/Val_CoolingTime'), '#,##0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/CG/Val_CoolingTime' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/DefrostSection/Runtime/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/CG/Val_RunTime'), '#,##0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/CG/Val_RunTime' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/DevicesSection/ValveChips/ValveLiquidSV/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} = '', '—', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), -1), -1), 1, 'CLOSED', 2, 'OPEN', 5, 'CLOSING', 6, 'OPENING', 33, 'DISABLED', '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), -1), -1) = 2, 'faceplate-fault-state text-ok', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Liquid SV/Valve/Val_Sts')), -1), -1) = 33, 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/DevicesSection/ValveChips/ValveSuctionSV/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} = '', '—', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), -1), -1), 1, 'CLOSED', 2, 'OPEN', 5, 'CLOSING', 6, 'OPENING', 33, 'DISABLED', '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), -1), -1) = 2, 'faceplate-fault-state text-ok', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Suction SV/Valve/Val_Sts')), -1), -1) = 33, 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/DevicesSection/ValveChips/ValveHotGasSV/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} = '', '—', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), -1), -1), 1, 'CLOSED', 2, 'OPEN', 5, 'CLOSING', 6, 'OPENING', 33, 'DISABLED', '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), -1), -1) = 2, 'faceplate-fault-state text-ok', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Hot Gas SV/Valve/Val_Sts')), -1), -1) = 33, 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/DevicesSection/ValveChips/ValveBleedSV`**

- `position.display`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_HasBleedValve')), false), false), coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/Cfg_HasBleedValve')), null), indexOf(',CG-C1,CG-D1,CG-G2,CG-G3,CG-G4,CG-G5,', ',' + substring(coalesce({view.params.tagPath}, ''), lastIndexOf(coalesce({view.params.tagPath}, ''), '/') + 1) + ',') < 0), false)
```


**`root/DevicesSection/ValveChips/ValveBleedSV/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), '—', if({view.params.tagPath} = '', '—', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), -1), -1), 1, 'CLOSED', 2, 'OPEN', 5, 'CLOSING', 6, 'OPENING', 33, 'DISABLED', '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), -1), -1) = 2, 'faceplate-fault-state text-ok', if(coalesce(try(toInt(tag({view.params.tagPath} + '/Valves/Bleed SV/Valve/Val_Sts')), -1), -1) = 33, 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/DevicesSection/FanChips/Fan1/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Nrdy_Fail'), false), false), 'FAULT', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Sts_Running'), false), false), 'RUN', 'OFF'))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Nrdy_Fail'), false), false), 'faceplate-fault-state faceplate-fault-active', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Sts_Running'), false), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/DevicesSection/FanChips/Fan2/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Nrdy_Fail'), false), false), 'FAULT', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Sts_Running'), false), false), 'RUN', 'OFF'))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Nrdy_Fail'), false), false), 'faceplate-fault-state faceplate-fault-active', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Sts_Running'), false), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/DevicesSection/FanChips/Fan3/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Nrdy_Fail'), false), false), 'FAULT', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Sts_Running'), false), false), 'RUN', 'OFF'))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Fans/Nrdy_Fail')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Nrdy_Fail'), false), false), 'faceplate-fault-state faceplate-fault-active', if(coalesce(try(tag({view.params.tagPath} + '/Fans/Sts_Running'), false), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 17 event actions, change scripts and handlers</summary>

- **`root/TempSection/Zat/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/ZAT/Val')
```

- **`root/CommandsSection/EnableRow/BtnEnable`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/HMIEnable'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Evaporator Enable',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CommandsSection/EnableRow/BtnSetBack`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/SB_Enable'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Set Back',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CommandsSection/DefrostRow/BtnStartDefrost`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/HMIStartDefrost'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Start Defrost',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CommandsSection/DefrostRow/BtnStopDefrost`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/HMIStopDefrost'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Stop Defrost',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/DefrostSection/TimeLeft/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/CG/Val_TimeLeft')
```

- **`root/DefrostSection/CoolingLeft/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/CG/Val_CoolingTime')
```

- **`root/DefrostSection/Runtime/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/CG/Val_RunTime')
```

- **`root/DevicesSection/ValveChips/ValveLiquidSV`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
shared.Alerts.showFaceplate(tagPath=base + '/Valves/Liquid SV', deviceType='Valve',
    title=base.split('/')[-1] + ' Liquid SV')
```

- **`root/DevicesSection/ValveChips/ValveLiquidSV/State`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Valves/Liquid SV/Valve/Val_Sts')
```

- **`root/DevicesSection/ValveChips/ValveSuctionSV`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
shared.Alerts.showFaceplate(tagPath=base + '/Valves/Suction SV', deviceType='Valve',
    title=base.split('/')[-1] + ' Suction SV')
```

- **`root/DevicesSection/ValveChips/ValveSuctionSV/State`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Valves/Suction SV/Valve/Val_Sts')
```

- **`root/DevicesSection/ValveChips/ValveHotGasSV`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
shared.Alerts.showFaceplate(tagPath=base + '/Valves/Hot Gas SV', deviceType='Valve',
    title=base.split('/')[-1] + ' Hot Gas SV')
```

- **`root/DevicesSection/ValveChips/ValveHotGasSV/State`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Valves/Hot Gas SV/Valve/Val_Sts')
```

- **`root/DevicesSection/ValveChips/ValveBleedSV`** `dom.onClick`, script action, scope `G`

```python
base = self.view.params.tagPath
if not base:
    return
shared.Alerts.showFaceplate(tagPath=base + '/Valves/Bleed SV', deviceType='Valve',
    title=base.split('/')[-1] + ' Bleed SV')
```

- **`root/DevicesSection/ValveChips/ValveBleedSV/State`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Valves/Bleed SV/Valve/Val_Sts')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](../configuration/configsection.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

<details>
<summary>18 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 28 | style class |
| `Fonts/Value` | 7 | style class |
| `Refridgeration_STS` | 1 | stylesheet |
| `faceplate-cmd-btn` | 4 | style class |
| `faceplate-cmd-row` | 2 | stylesheet |
| `faceplate-cmd-row-fill` | 2 | stylesheet |
| `faceplate-fault-chip` | 12 | style class |
| `faceplate-fault-chips` | 3 | stylesheet |
| `faceplate-fault-code` | 12 | style class |
| `faceplate-fault-state` | 12 | stylesheet |
| `faceplate-kpi-label` | 7 | style class |
| `faceplate-kpi-row` | 7 | stylesheet |
| `faceplate-section` | 5 | style class |
| `faceplate-section-card` | 5 | style class |
| `faceplate-section-title` | 5 | style class |
| `faceplate-status-banner` | 1 | stylesheet |
| `faceplate-cmd-btn-active` | bound | style class |
| `value-bad` | bound | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Enums/Evaporator/CycleFans`
- `[default]_Config/Enums/Evaporator/DefrostStartMode`
- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>32 relative member paths</summary>

`.EngUnit`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/CG/Cfg_CycFans`, `/CG/Cfg_DefrostStartMode`, `/CG/Cfg_HasBleedValve`, `/CG/HMIEnable`, `/CG/HMIStartDefrost`, `/CG/HMIStopDefrost`, `/CG/IntlkOK`, `/CG/PermOK`, `/CG/SB_Enable`, `/CG/TooCold`, `/CG/TooHot`, `/CG/Val_CoolingTime`, `/CG/Val_RunTime`, `/CG/Val_TimeLeft`, `/DIn.Enabled`, `/Fans/Nrdy_Fail`, `/Fans/Sts_Running`, `/HmiStatus`, `/Valves/Bleed SV`, `/Valves/Bleed SV/Valve/Val_Sts`, `/Valves/Hot Gas SV`, `/Valves/Hot Gas SV/Valve/Val_Sts`, `/Valves/Liquid SV`, `/Valves/Liquid SV/Valve/Val_Sts`, `/Valves/Suction SV`, `/Valves/Suction SV/Valve/Val_Sts`, `/ZAT/Val`, `/_NoPlc/Pressure`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
