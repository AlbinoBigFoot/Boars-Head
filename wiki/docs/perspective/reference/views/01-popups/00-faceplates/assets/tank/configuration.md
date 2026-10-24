---
title: "Configuration"
sidebar_label: "Configuration"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Tank/Configuration (Asset (embedded piece)): 85 components, 126 bindings, 6 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Tank/Configuration", "Configuration"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Tank/Configuration`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Tank/Configuration` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Tank/Configuration/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Tank &gt; Configuration |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 85 components, 126 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-24T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

<details>
<summary>13 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `qg0` | `null` | bound (expr) |
| `qg1` | `null` | bound (expr) |
| `qg2` | `null` | bound (expr) |
| `qg3` | `null` | bound (expr) |
| `qg4` | `null` | bound (expr) |
| `qg5` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roConfiguration` | `true` | bound (expr) |
| `tipConfiguration` | `""` | bound (expr) |
| `roSetpoint` | `true` | bound (expr) |
| `tipSetpoint` | `""` | bound (expr) |
| `qg6` | `null` | bound (expr) |

</details>

## Component Tree

Component types: ia.display.label x30, ia.container.flex x29, ia.display.view x20, ia.display.icon x5, ia.input.button x1.

<details>
<summary>Component tree (85 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Left  ia.container.flex
    AinMaint  ia.container.flex
      AinMaintTitle  ia.display.label
      Raw  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.label  [1 binding; 1 event]
      Head  ia.container.flex
        H0  ia.display.label
        H1  ia.display.label
        H2  ia.display.label
      Fail  ia.container.flex
        Lbl  ia.display.label
        Lims  ia.container.flex
          Hi  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
          Lo  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Db  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      HiHi  ia.container.flex
        Lbl  ia.display.label
        Thr  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Db  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      Hi  ia.container.flex
        Lbl  ia.display.label
        Thr  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Db  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      Lo  ia.container.flex
        Lbl  ia.display.label
        Thr  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Db  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      LoLo  ia.container.flex
        Lbl  ia.display.label
        Thr  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Db  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      SetTrack  ia.container.flex
        Chk  ia.display.icon  [5 bindings; 1 event]
        Lbl  ia.display.label
  Right  ia.container.flex
    AinIdent  ia.container.flex  [1 binding]
      AinIdentTitle  ia.display.label
      Desc  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
      Label  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
      Tag  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
    AinScaling  ia.container.flex  [1 binding]
      AinScalingTitle  ia.display.label
      Head  ia.container.flex
        H0  ia.display.label
        H1  ia.display.label
        H2  ia.display.label
      Max  ia.container.flex
        Lbl  ia.display.label
        Raw  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Eu  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      Min  ia.container.flex
        Lbl  ia.display.label
        Raw  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Eu  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      Units  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
    AinOptions  ia.container.flex  [1 binding]
      AinOptionsTitle  ia.display.label
      HasChan  ia.container.flex
        Chk  ia.display.icon  [5 bindings; 1 event]
        Lbl  ia.display.label
      Subst  ia.container.flex
        Chk  ia.display.icon  [5 bindings; 1 event]
        Lbl  ia.display.label
      PCmdClear  ia.container.flex
        Chk  ia.display.icon  [5 bindings; 1 event]
        Lbl  ia.display.label
      DefaultMode  ia.container.flex
        DefaultState  ia.container.flex
          Icon  ia.display.icon  [1 binding]
          State  ia.display.label  [1 binding]
        DefToggle  ia.input.button  [5 bindings; 1 event]
      ModeHint  ia.display.label
      Filter  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
```

</details>

## Bindings

126 bindings: expr 126.

<details>
<summary>All 126 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_InpPV')), tag({view.params.tagPath} + '/LvlAIn/Val_InpPV'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_SetTrack')), tag({view.params.tagPath} + '/LvlAIn/Cfg_SetTrack'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_HasChanObj')), tag({view.params.tagPath} + '/LvlAIn/Cfg_HasChanObj'), null), null)
```


- `custom.qg3`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_NoSubstPV')), tag({view.params.tagPath} + '/LvlAIn/Cfg_NoSubstPV'), null), null)
```


- `custom.qg4`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_PCmdClear')), tag({view.params.tagPath} + '/LvlAIn/Cfg_PCmdClear'), null), null)
```


- `custom.qg5`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/LvlAIn/Mode/Cfg_ProgDefault')), tag({view.params.tagPath} + '/LvlAIn/Mode/Cfg_ProgDefault'), null), null)
```


- `custom.permDevice`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', coalesce(try(lookup({view.custom.qg6}, toStr(coalesce(try(tag({view.params.tagPath} + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg6}, toStr(coalesce(try(tag(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg6}, toStr(coalesce(try(tag(left(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')), lastIndexOf(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')), '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), ''))
```


- `custom.roConfiguration`: expression

```js
coalesce({session.custom.EngineeringReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), true)
```


- `custom.tipConfiguration`: expression

```js
if(!coalesce({session.custom.EngineeringReadOnly}, true) && coalesce({view.custom.roConfiguration}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), 'Setpoint', 'Configuration') + ' (Roles & Permissions)', '')
```


- `custom.roSetpoint`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), true)
```


- `custom.tipSetpoint`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roSetpoint}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), 'Configuration', 'Setpoint') + ' (Roles & Permissions)', '')
```


- `custom.qg6`: expression

```js
try(if(isGood(tag('[default]_Config/Security/DeviceTypes')), tag('[default]_Config/Security/DeviceTypes'), null), null)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Left/AinMaint/Raw/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', coalesce(try(numberFormat({view.custom.qg0}, '#,##0.00'), null), '—'))
```


**`root/Left/AinMaint/Fail/Lims/Hi`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_FailHiLim')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/Fail/Lims/Lo`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_FailLoLim')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/Fail/Db`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_FailDB')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/HiHi/Thr`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Val_HiHiLim')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/HiHi/Db`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_HiHiDB')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/Hi/Thr`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Val_HiLim')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/Hi/Db`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_HiDB')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/Lo/Thr`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Val_LoLim')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/Lo/Db`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_LoDB')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/LoLo/Thr`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Val_LoLoLim')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/LoLo/Db`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_LoLoDB')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roSetpoint}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Left/AinMaint/SetTrack/Chk`**

- `props.path`: expression

```js
if(!coalesce(try(!isNull({view.custom.qg1}), false), false), 'material/indeterminate_check_box', if(coalesce(try(toBoolean({view.custom.qg1}), false), false), 'material/check_box', 'material/check_box_outline_blank'))
```


- `props.color`: expression

```js
if(!coalesce(try(!isNull({view.custom.qg1}), false), false), 'var(--neutral-60)', if(coalesce(try(toBoolean({view.custom.qg1}), false), false), '#2E7D32', 'var(--text)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roSetpoint}, false), 1, 0.45)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/Right/AinIdent`**

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Right/AinIdent/Desc/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_Desc')
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


**`root/Right/AinIdent/Label/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_Label')
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


**`root/Right/AinIdent/Tag/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_Tag')
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


**`root/Right/AinScaling`**

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Right/AinScaling/Max/Raw`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_InpRawMax')
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


**`root/Right/AinScaling/Max/Eu`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_PVEUMax')
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


**`root/Right/AinScaling/Min/Raw`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_InpRawMin')
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


**`root/Right/AinScaling/Min/Eu`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_PVEUMin')
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


**`root/Right/AinScaling/Units/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_EU')
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


**`root/Right/AinOptions`**

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Right/AinOptions/HasChan/Chk`**

- `props.path`: expression

```js
if(!coalesce(try(!isNull({view.custom.qg2}), false), false), 'material/indeterminate_check_box', if(coalesce(try(toBoolean({view.custom.qg2}), false), false), 'material/check_box', 'material/check_box_outline_blank'))
```


- `props.color`: expression

```js
if(!coalesce(try(!isNull({view.custom.qg2}), false), false), 'var(--neutral-60)', if(coalesce(try(toBoolean({view.custom.qg2}), false), false), '#2E7D32', 'var(--text)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Right/AinOptions/Subst/Chk`**

- `props.path`: expression

```js
if(!coalesce(try(toBoolean({view.custom.qg3}), false), false), 'material/check_box', 'material/check_box_outline_blank')
```


- `props.color`: expression

```js
if(!coalesce(try(toBoolean({view.custom.qg3}), false), false), '#2E7D32', 'var(--text)')
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Right/AinOptions/PCmdClear/Chk`**

- `props.path`: expression

```js
if(!coalesce(try(!isNull({view.custom.qg4}), false), false), 'material/indeterminate_check_box', if(coalesce(try(toBoolean({view.custom.qg4}), false), false), 'material/check_box', 'material/check_box_outline_blank'))
```


- `props.color`: expression

```js
if(!coalesce(try(!isNull({view.custom.qg4}), false), false), 'var(--neutral-60)', if(coalesce(try(toBoolean({view.custom.qg4}), false), false), '#2E7D32', 'var(--text)'))
```


- `props.style.opacity`: expression

```js
if(!coalesce({view.custom.roConfiguration}, false), 1, 0.45)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Right/AinOptions/DefaultMode/DefaultState/Icon`**

- `props.path`: expression

```js
if(!coalesce(try(toBoolean({view.custom.qg5}), false), false), 'material/person', 'material/memory')
```


**`root/Right/AinOptions/DefaultMode/DefaultState/State`**

- `props.text`: expression

```js
if(!coalesce(try(toBoolean({view.custom.qg5}), false), false), 'Default Mode  ·  Operator', 'Default Mode  ·  Program')
```


**`root/Right/AinOptions/DefaultMode/DefToggle`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roConfiguration}, false) && !({view.params.tagPath} = '')) && coalesce({view.custom.pax}, '') = ''
```


- `props.text`: expression

```js
if(!coalesce(try(toBoolean({view.custom.qg5}), false), false), 'Make Program Default', 'Make Operator Default')
```


- `props.image.icon.path`: expression

```js
if(!coalesce(try(toBoolean({view.custom.qg5}), false), false), 'material/memory', 'material/person')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Right/AinOptions/Filter/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/LvlAIn/Cfg_FiltTC')
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

</details>

## Event Scripts And Handlers

- **`root/Left/AinMaint/Raw/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/LvlAIn/Val_InpPV')
```

- **`root/Left/AinMaint/SetTrack/Chk`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roSetpoint:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/Cfg_SetTrack'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Bumpless Program/Operator Transition',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Right/AinOptions/HasChan/Chk`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/Cfg_HasChanObj'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Enable Navigation To Input Channel Object',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Right/AinOptions/Subst/Chk`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/Cfg_NoSubstPV'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Allow Selection Of Substitute PV',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Right/AinOptions/PCmdClear/Chk`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/Cfg_PCmdClear'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Clear Program Commands Upon Receipt',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Right/AinOptions/DefaultMode/DefToggle`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roConfiguration:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/LvlAIn/Mode/Cfg_ProgDefault'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Default Mode',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (2): [03\_Elements/00\_Control/AnalogInput](../../../../03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/StringInput](../../../../03-elements/00-control/stringinput.md)

**Opened or named by** (2): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md), [01\_Popups/00\_Faceplates/TankOverview](../../tankoverview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 29 | style class |
| `Fonts/Value` | 2 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `faceplate-interlock-colhdr` | 2 | stylesheet |
| `faceplate-section` | 4 | style class |
| `faceplate-section-card` | 4 | style class |
| `faceplate-section-title` | 4 | style class |
| `fw-700` | 5 | style class |
| `text-muted` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>30 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/LvlAIn/Cfg_Desc`, `/LvlAIn/Cfg_EU`, `/LvlAIn/Cfg_FailDB`, `/LvlAIn/Cfg_FailHiLim`, `/LvlAIn/Cfg_FailLoLim`, `/LvlAIn/Cfg_FiltTC`, `/LvlAIn/Cfg_HasChanObj`, `/LvlAIn/Cfg_HiDB`, `/LvlAIn/Cfg_HiHiDB`, `/LvlAIn/Cfg_InpRawMax`, `/LvlAIn/Cfg_InpRawMin`, `/LvlAIn/Cfg_Label`, `/LvlAIn/Cfg_LoDB`, `/LvlAIn/Cfg_LoLoDB`, `/LvlAIn/Cfg_NoSubstPV`, `/LvlAIn/Cfg_PCmdClear`, `/LvlAIn/Cfg_PVEUMax`, `/LvlAIn/Cfg_PVEUMin`, `/LvlAIn/Cfg_SetTrack`, `/LvlAIn/Cfg_Tag`, `/LvlAIn/Mode/Cfg_ProgDefault`, `/LvlAIn/Val_HiHiLim`, `/LvlAIn/Val_HiLim`, `/LvlAIn/Val_InpPV`, `/LvlAIn/Val_LoLim`, `/LvlAIn/Val_LoLoLim`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
