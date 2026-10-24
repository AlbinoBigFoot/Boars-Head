---
title: "DiscreteInput"
sidebar_label: "DiscreteInput"
description: "Perspective view 01_Popups/00_Faceplates/DiscreteInput (Popup / faceplate): 66 components, 94 bindings, 10 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/DiscreteInput", "DiscreteInput"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/DiscreteInput`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/DiscreteInput` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/DiscreteInput/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; DiscreteInput |
| Root | `ia.container.flex`, height 600, width 600 |
| Size | 66 components, 94 bindings, 10 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-24T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `popupId` | `""` | input |
| `tagPath` | `""` | input |
| `title` | `""` | input |

## Custom properties

<details>
<summary>20 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `selected` | `"Status"` | |
| `root` | `null` | bound (expr) |
| `pax` | `null` | bound (expr) |
| `ok` | `null` | bound (expr) |
| `sts` | `null` | bound (expr) |
| `pv` | `null` | bound (expr) |
| `tgt` | `null` | bound (expr) |
| `subst` | `null` | bound (expr) |
| `msubst` | `null` | bound (expr) |
| `dis` | `null` | bound (expr) |
| `nosubst` | `null` | bound (expr) |
| `t0` | `null` | bound (expr) |
| `t1` | `null` | bound (expr) |
| `lbl` | `null` | bound (expr) |
| `desc` | `null` | bound (expr) |
| `tone` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roConfiguration` | `true` | bound (expr) |
| `tipConfiguration` | `""` | bound (expr) |
| `paxRoot` | `""` | bound (expr) |

</details>

## Component Tree

Component types: ia.container.flex x27, ia.display.label x18, ia.display.view x11, ia.input.button x9, ia.display.icon x1.

<details>
<summary>Component tree (66 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    Title  ia.display.label  [1 binding]
    Sub  ia.display.label  [1 binding]
    State  ia.display.label  [3 bindings]
    Comm  ia.display.label  [3 bindings]
    Close  ia.display.icon  [1 event]
  Content  ia.container.flex
    Tabs  ia.container.flex
      Status  ia.input.button  [2 bindings; 1 event]
      Configuration  ia.input.button  [2 bindings; 1 event]
      Alarm Configuration  ia.input.button  [2 bindings; 1 event]
      Alarms  ia.input.button  [2 bindings; 1 event]
    Body  ia.container.flex
      Status  ia.container.flex  [1 binding]
        State  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Value  ia.display.label  [2 bindings]
          Normal  ia.display.label  [1 binding]
        Input  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          PvFromInput  ia.container.flex
            Lbl  ia.display.label
            Val  ia.display.label  [2 bindings]
          Source  ia.container.flex
            Lbl  ia.display.label
            Source  ia.container.flex
              Input  ia.input.button  [5 bindings; 1 event]
              Substitute  ia.input.button  [5 bindings; 1 event]
          SubstValue  ia.container.flex  [1 binding]
            Lbl  ia.display.label
            SubstValue  ia.container.flex
              Value0  ia.input.button  [5 bindings; 1 event]
              Value1  ia.input.button  [5 bindings; 1 event]
        Alarm  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          TargetDisagree  ia.container.flex
            Lbl  ia.display.label
            State  ia.display.label  [2 bindings]
            Reset  ia.input.button  [3 bindings; 1 event]
      Configuration  ia.container.flex  [1 binding]
        Processing  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Debounce  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
        Ident  ia.container.flex  [1 binding]
          Head  ia.container.flex
            Title  ia.display.label
          Desc  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
          Label  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
          Tag  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
          Text0  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
          Text1  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
        Options  ia.container.flex  [1 binding]
          Head  ia.container.flex
            Title  ia.display.label
          NoSubst  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
          PCmdClear  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
          NormText  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
      AlarmConfiguration  ia.container.flex  [1 binding]
        AlarmConfig  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/AlarmConfiguration]
      Alarms  ia.container.flex  [1 binding]
        AlarmList  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Alarms]
```

</details>

## Bindings

94 bindings: expr 88, property 6.

<details>
<summary>All 94 bindings, grouped by component</summary>

**`(view)`**

- `custom.root`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', if(toStr(coalesce(try(tag({view.params.tagPath} + '.TypeId'), ''), '')) = 'Devices/DiscreteInput', {view.params.tagPath} + '/DIn', if(case(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', '') != '', left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '/' + case(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', ''), {view.params.tagPath})))
```


- `custom.pax`: expression

```js
if(if(coalesce({view.params.tagPath}, '') = '', '', case(toStr(coalesce(try(tag({view.params.tagPath} + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/DIn.Enabled')), false), false), 'DIn', ''), '')) = 'DIn', 'DIn', if(coalesce({view.params.tagPath}, '') != '' && case(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', '') != '' && case(toStr(coalesce(try(tag(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '/DIn.Enabled')), false), false), 'DIn', ''), '') = 'Tank', 'DIn', ''))
```


- `custom.ok`: expression

```js
{view.custom.root} != '' && coalesce(try(isGood(tag({view.custom.root} + '/Sts')), false), false)
```


- `custom.sts`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Sts')), false), false), toBoolean(tag({view.custom.root} + '/Sts')), null)
```


- `custom.pv`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Sts_PV')), false), false), toBoolean(tag({view.custom.root} + '/Sts_PV')), null)
```


- `custom.tgt`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Inp_Target')), false), false), toBoolean(tag({view.custom.root} + '/Inp_Target')), null)
```


- `custom.subst`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Sts_SubstPV')), false), false), toBoolean(tag({view.custom.root} + '/Sts_SubstPV')), null)
```


- `custom.msubst`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/MSet_SubstPV')), false), false), toBoolean(tag({view.custom.root} + '/MSet_SubstPV')), null)
```


- `custom.dis`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Sts_TgtDisagree')), false), false), toBoolean(tag({view.custom.root} + '/Sts_TgtDisagree')), null)
```


- `custom.nosubst`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Cfg_NoSubstPV')), false), false), toBoolean(tag({view.custom.root} + '/Cfg_NoSubstPV')), null)
```


- `custom.t0`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Cfg_0StText')), false), false), toStr(tag({view.custom.root} + '/Cfg_0StText')), null)
```


- `custom.t1`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Cfg_1StText')), false), false), toStr(tag({view.custom.root} + '/Cfg_1StText')), null)
```


- `custom.lbl`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Cfg_Label')), false), false), coalesce(toStr(tag({view.custom.root} + '/Cfg_Label')), ''), '')
```


- `custom.desc`: expression

```js
if(coalesce(try(isGood(tag({view.custom.root} + '/Cfg_Desc')), false), false), coalesce(toStr(tag({view.custom.root} + '/Cfg_Desc')), ''), '')
```


- `custom.tone`: expression

```js
if(isNull({view.custom.sts}) || isNull({view.custom.tgt}), 'off', if({view.custom.sts} = {view.custom.tgt}, 'ok', 'alarm'))
```


- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../common-patterns.md#pattern-8).

- `custom.roConfiguration`: expression

```js
coalesce({session.custom.EngineeringReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), true)
```


- `custom.tipConfiguration`: expression

```js
if(!coalesce({session.custom.EngineeringReadOnly}, true) && coalesce({view.custom.roConfiguration}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), 'Setpoint', 'Configuration') + ' (Roles & Permissions)', '')
```


- `custom.paxRoot`: expression

```js
if(if(coalesce({view.params.tagPath}, '') = '', '', case(toStr(coalesce(try(tag({view.params.tagPath} + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/DIn.Enabled')), false), false), 'DIn', ''), '')) = 'DIn', {view.params.tagPath} + '/DIn', if(coalesce({view.params.tagPath}, '') = '' || case(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', '') = '', '', left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '/' + case(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', '')))
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/Header/Title`**

- `props.text`: expression

```js
if({view.custom.lbl} != '', if(({view.custom.desc} != '' && {view.custom.desc} != 'Discrete Input' && {view.custom.desc} != {view.custom.lbl}) && indexOf({view.custom.desc}, {view.custom.lbl}) >= 0, {view.custom.desc}, {view.custom.lbl}), if(coalesce({view.params.title}, '') != '', coalesce({view.params.title}, ''), 'Discrete Input'))
```


**`root/Header/Sub`**

- `props.text`: expression

```js
if({view.custom.lbl} != '' && ({view.custom.desc} != '' && {view.custom.desc} != 'Discrete Input' && {view.custom.desc} != {view.custom.lbl}) && indexOf({view.custom.desc}, {view.custom.lbl}) < 0, {view.custom.desc}, '')
```


**`root/Header/State`**

- `props.text`: expression

```js
if(isNull({view.custom.sts}), '—', if(toBoolean({view.custom.sts}), if(coalesce({view.custom.t1}, '') = '', 'On', {view.custom.t1}), if(coalesce({view.custom.t0}, '') = '', 'Off', {view.custom.t0})))
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + {view.custom.tone}
```


- `position.display`: expression

```js
coalesce({view.custom.ok}, false)
```


**`root/Header/Comm`**

- `props.text`: expression

```js
'Comm Loss'
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + 'alarm'
```


- `position.display`: expression

```js
{view.custom.root} != '' && !coalesce({view.custom.ok}, false)
```


**`root/Content/Tabs/Status`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

**`root/Content/Tabs/Configuration`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

**`root/Content/Tabs/Alarm Configuration`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

**`root/Content/Tabs/Alarms`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

**`root/Content/Body/Status`**

- `position.display`: expression

```js
{view.custom.selected} = 'Status'
```


**`root/Content/Body/Status/State/Value`**

- `props.text`: expression

```js
if(isNull({view.custom.sts}), '—', if(toBoolean({view.custom.sts}), if(coalesce({view.custom.t1}, '') = '', 'On', {view.custom.t1}), if(coalesce({view.custom.t0}, '') = '', 'Off', {view.custom.t0})))
```


- `props.style.classes`: expression

```js
'fp-hero ' + case({view.custom.tone}, 'ok', 'fp-text-ok', 'alarm', 'fp-text-alarm', 'value-bad')
```


**`root/Content/Body/Status/State/Normal`**

- `props.text`: expression

```js
'Normal State: ' + if(isNull({view.custom.tgt}), '—', if(toBoolean({view.custom.tgt}), if(coalesce({view.custom.t1}, '') = '', 'On', {view.custom.t1}), if(coalesce({view.custom.t0}, '') = '', 'Off', {view.custom.t0})))
```


**`root/Content/Body/Status/Input/PvFromInput/Val`**

- `props.text`: expression

```js
if(isNull({view.custom.pv}), '—', if(toBoolean({view.custom.pv}), if(coalesce({view.custom.t1}, '') = '', 'On', {view.custom.t1}), if(coalesce({view.custom.t0}, '') = '', 'Off', {view.custom.t0})))
```


- `props.style.classes`: expression

```js
if(isNull({view.custom.pv}), 'fp-row-value value-bad', 'fp-row-value')
```


**`root/Content/Body/Status/Input/Source/Source/Input`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roConfiguration}, false) && {view.custom.root} != '' && coalesce({view.custom.pax}, '') = '' && true && !coalesce((!isNull({view.custom.subst}) && !{view.custom.subst}), false)
```


- `props.style.classes`: expression

```js
if(coalesce((!isNull({view.custom.subst}) && !{view.custom.subst}), false), 'form-btn-primary', 'form-btn')
```


- `props.text`: expression

```js
'Input'
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Status/Input/Source/Source/Substitute`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roConfiguration}, false) && {view.custom.root} != '' && coalesce({view.custom.pax}, '') = '' && !coalesce({view.custom.nosubst}, false) && !coalesce(coalesce({view.custom.subst}, false), false)
```


- `props.style.classes`: expression

```js
if(coalesce(coalesce({view.custom.subst}, false), false), 'form-btn-primary', 'form-btn')
```


- `props.text`: expression

```js
'Substitute'
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Status/Input/SubstValue`**

- `position.display`: expression

```js
!coalesce({view.custom.nosubst}, false)
```


**`root/Content/Body/Status/Input/SubstValue/SubstValue/Value0`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roConfiguration}, false) && {view.custom.root} != '' && coalesce({view.custom.pax}, '') = '' && true && !coalesce((!isNull({view.custom.msubst}) && !{view.custom.msubst}), false)
```


- `props.style.classes`: expression

```js
if(coalesce((!isNull({view.custom.msubst}) && !{view.custom.msubst}), false), 'form-btn-primary', 'form-btn')
```


- `props.text`: expression

```js
if(coalesce({view.custom.t0}, '') = '', 'Off', {view.custom.t0})
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Status/Input/SubstValue/SubstValue/Value1`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roConfiguration}, false) && {view.custom.root} != '' && coalesce({view.custom.pax}, '') = '' && true && !coalesce(coalesce({view.custom.msubst}, false), false)
```


- `props.style.classes`: expression

```js
if(coalesce(coalesce({view.custom.msubst}, false), false), 'form-btn-primary', 'form-btn')
```


- `props.text`: expression

```js
if(coalesce({view.custom.t1}, '') = '', 'On', {view.custom.t1})
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Status/Alarm/TargetDisagree/State`**

- `props.text`: expression

```js
if(isNull({view.custom.dis}), '—', if({view.custom.dis}, 'Active', 'Normal'))
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + if(isNull({view.custom.dis}), 'muted', if({view.custom.dis}, 'alarm', 'muted'))
```


**`root/Content/Body/Status/Alarm/TargetDisagree/Reset`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roConfiguration}, false) && {view.custom.root} != '' && coalesce({view.custom.pax}, '') = '' && coalesce({view.custom.dis}, false)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Content/Body/Configuration`**

- `position.display`: expression

```js
{view.custom.selected} = 'Configuration'
```


**`root/Content/Body/Configuration/Processing/Debounce`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_Debounce')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Ident`**

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Content/Body/Configuration/Ident/Desc`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_Desc')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Ident/Label`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_Label')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Ident/Tag`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_Tag')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Ident/Text0`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_0StText')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Ident/Text1`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_1StText')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Options`**

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Content/Body/Configuration/Options/NoSubst`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_NoSubstPV')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Options/PCmdClear`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_PCmdClear')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/Configuration/Options/NormText`**

- `props.params.tagPath`: expression

```js
if({view.custom.root} = '', '', {view.custom.root} + '/Cfg_NormTextVis')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Content/Body/AlarmConfiguration`**

- `position.display`: expression

```js
{view.custom.selected} = 'Alarm Configuration'
```


**`root/Content/Body/AlarmConfiguration/AlarmConfig`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/Content/Body/Alarms`**

- `position.display`: expression

```js
{view.custom.selected} = 'Alarms'
```


**`root/Content/Body/Alarms/AlarmList`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

</details>

## Event Scripts And Handlers

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
pid = str(self.view.params.popupId or '').strip()
if pid:
    system.perspective.closePopup(pid)
```

- **`root/Content/Tabs/Status`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Configuration`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Alarm Configuration`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Alarms`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Body/Status/Input/Source/Source/Input`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.root
if not base:
    return
path = base + '/MCmd_InpPV'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Use Input PV',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Status/Input/Source/Source/Substitute`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.root
if not base:
    return
path = base + '/MCmd_SubstPV'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Use Substitute PV',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Status/Input/SubstValue/SubstValue/Value0`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.root
if not base:
    return
path = base + '/MSet_SubstPV'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Substitute PV',
    tagPath=path,
    newValue=False,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Status/Input/SubstValue/SubstValue/Value1`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.root
if not base:
    return
path = base + '/MSet_SubstPV'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Substitute PV',
    tagPath=path,
    newValue=True,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Content/Body/Status/Alarm/TargetDisagree/Reset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.custom.root
if not base:
    return
path = base + '/OCmd_ResetAckAll'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Reset / Ack',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (3): [01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./assets/alarmconfiguration.md), [01\_Popups/00\_Faceplates/\_Assets/Alarms](./assets/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](./assets/configuration/configfield.md)

**Opened or named by** (2): [00\_Pages/Groveport/Utility/OverviewStatusTile](../../00-pages/groveport/utility/overviewstatustile.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./assets/discreteinputs.md)

**Named in project scripts**: [Navigation.Faceplate](../../../../../scripting/reference/modules/navigation-faceplate.md)

## Style Classes

<details>
<summary>28 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 3 | style class |
| `Fonts/Title` | 1 | style class |
| `bg-component` | 1 | stylesheet |
| `bg-header` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `config-field-label` | 3 | stylesheet |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `container-icon` | 1 | stylesheet |
| `faceplate` | 1 | stylesheet |
| `faceplate-body` | 1 | stylesheet |
| `faceplate-buttons-4` | 1 | stylesheet |
| `faceplate-close` | 1 | stylesheet |
| `faceplate-content` | 1 | stylesheet |
| `faceplate-header` | 1 | stylesheet |
| `faceplate-tabs-vertical` | 3 | stylesheet |
| `faceplate-title` | 1 | style class |
| `form-btn` | 5 | style class |
| `fp-card` | 6 | style class |
| `fp-card-title` | 6 | style class |
| `fp-hero` | 1 | style class |
| `fp-name` | 1 | style class |
| `fp-pill` | 3 | style class |
| `fp-row-value` | 1 | style class |
| `fp-sub` | 1 | style class |
| `fp-title-sub` | 1 | style class |
| `faceplate-button` | bound | stylesheet |
| `faceplate-button-selected` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>23 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_0StText`, `/Cfg_1StText`, `/Cfg_Debounce`, `/Cfg_Desc`, `/Cfg_Label`, `/Cfg_NoSubstPV`, `/Cfg_NormTextVis`, `/Cfg_PCmdClear`, `/Cfg_Tag`, `/DIn`, `/DIn.Enabled`, `/Inp_Target`, `/MCmd_InpPV`, `/MCmd_SubstPV`, `/MSet_SubstPV`, `/OCmd_ResetAckAll`, `/Sts`, `/Sts_PV`, `/Sts_SubstPV`, `/Sts_TgtDisagree`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
