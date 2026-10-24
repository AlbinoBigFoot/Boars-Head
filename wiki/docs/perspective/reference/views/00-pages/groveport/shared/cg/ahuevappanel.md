---
title: "AhuEvapPanel"
sidebar_label: "AhuEvapPanel"
description: "Perspective view 00_Pages/Groveport/_Shared/CG/AhuEvapPanel (Page piece (not routed)): 107 components, 152 bindings, 13 event scripts."
generated: true
keywords: ["00_Pages/Groveport/_Shared/CG/AhuEvapPanel", "AhuEvapPanel"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/_Shared/CG/AhuEvapPanel`.

| | |
|---|---|
| View path | `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/_Shared/CG/AhuEvapPanel/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; \_Shared &gt; CG &gt; AhuEvapPanel |
| Root | `ia.container.flex`, width 1332, height 392 |
| Size | 107 components, 152 bindings, 13 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-08-31T20:45:00Z by the Designer |

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
| `roSetpoint` | `true` | bound (expr) |
| `tipSetpoint` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x43, ia.display.label x37, ia.display.view x17, ia.input.button x10.

<details>
<summary>Component tree (107 components)</summary>

```text
root  ia.container.flex
  CardControls  ia.container.flex
    Title  ia.display.label
    State  ia.container.flex
      Lbl  ia.display.label
      StatePill  ia.display.label  [3 bindings]
    Enable  ia.container.flex
      BtnEnable  ia.input.button  [8 bindings; 1 event]
    DefrostLbl  ia.display.label
    Defrost  ia.container.flex
      BtnStartDefrost  ia.input.button  [4 bindings; 1 event]
      BtnStopDefrost  ia.input.button  [4 bindings; 1 event]
    SetBack  ia.container.flex
      BtnSetback  ia.input.button  [8 bindings; 1 event]
    InterlockLbl  ia.display.label
    Interlock  ia.container.flex
      InterlockBtn  ia.display.view  [1 binding; view: 02_Components/00_Controls/InterlockButton]
  CardDefrost  ia.container.flex
    Title  ia.display.label
    Mode  ia.container.flex
      Lbl  ia.display.label
      ModeSeg  ia.container.flex
        Opt0  ia.input.button  [7 bindings; 1 event]
        Opt1  ia.input.button  [7 bindings; 1 event]
        Opt2  ia.input.button  [7 bindings; 1 event]
      CurrentMode  ia.display.label  [3 bindings]
    Fans  ia.container.flex
      Lbl  ia.display.label
      FansSeg  ia.container.flex
        Opt0  ia.input.button  [7 bindings; 1 event]
        Opt1  ia.input.button  [7 bindings; 1 event]
        Opt2  ia.input.button  [7 bindings; 1 event]
    Groups  ia.container.flex
      ToDSchedule  ia.container.flex  [1 binding]
        Header  ia.container.flex
          Title  ia.display.label
        Def1stTOD  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/TimeInput]
        Def2ndTOD  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/TimeInput]
        Def3rdTOD  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/TimeInput]
        Def4thTOD  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/TimeInput]
      CoolingSchedule  ia.container.flex  [1 binding]
        Header  ia.container.flex
          Title  ia.display.label
        CoolingLeft  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings; 1 event]
        CoolingSP  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      RuntimeSchedule  ia.container.flex  [1 binding]
        Header  ia.container.flex
          Title  ia.display.label
        RuntimeLeft  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.label  [2 bindings; 1 event]
        RuntimeSP  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      StepTimers  ia.container.flex
        Header  ia.container.flex
          Title  ia.display.label
        PumpOut  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        MainHotGas  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        Bleed  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
        FanDelay  ia.container.flex
          Lbl  ia.display.label
          Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
  CardTemperature  ia.container.flex
    Title  ia.display.label
    ZoneAirTemp  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    TargetSP  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
    Deadband  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
    Setback  ia.container.flex
      Header  ia.container.flex
        Title  ia.display.label
      SBMin  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      SBMax  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
      SBStart  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/TimeInput]
      SBStop  ia.container.flex
        Lbl  ia.display.label
        Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/TimeInput]
```

</details>

## Bindings

152 bindings: expr 152.

<details>
<summary>All 152 bindings, grouped by component</summary>

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


- `custom.roSetpoint`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), true)
```


- `custom.tipSetpoint`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roSetpoint}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), 'Configuration', 'Setpoint') + ' (Roles & Permissions)', '')
```


**`root/CardControls/State/StatePill`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/HmiStatus')), true), true), '—', case(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)), 0, 'Off', 1, 'Cooling', 2, 'Defrost', 3, 'Fault', 4, 'Manual', 5, 'Idle', 6, 'Defrost · Pump Down', 7, 'Defrost · Hot Gas', 8, 'Defrost · Bleed', 9, 'Defrost · Fan Delay', 'Unknown'))
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false), if((if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) = 2 || (if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) >= 6 && if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) <= 9)), 'var(--status-defrost)', case(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)), 1, 'var(--status-cooling)', 5, 'var(--status-idle)', 3, 'var(--status-level-critical)', 'var(--status-off)')), 'var(--neutral-30)')
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/HmiStatus')), true), true), 'Fonts/Label value-bad', 'Fonts/Label')
```


**`root/CardControls/Enable/BtnEnable`**

- `props.enabled`: expression

```js
((!{view.custom.roCommand} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), false), false)
```


- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), '—', if(if({view.params.tagPath} = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/HMIEnable')), false), false)), 'Evaporator Enabled', 'Evaporator Disabled'))
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), false), false), if(if({view.params.tagPath} = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/HMIEnable')), false), false)), '#2E7D32', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), false), false), if(if({view.params.tagPath} = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/HMIEnable')), false), false)), '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/HMIEnable')), true), true), 'faceplate-cmd-btn Fonts/Label value-bad', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/CardControls/Defrost/BtnStartDefrost`**

- `props.enabled`: expression

```js
((!{view.custom.roCommand} && !({view.params.tagPath} = '') && !(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) = 2 || (if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) >= 6 && if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) <= 9))) && coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/CardControls/Defrost/BtnStopDefrost`**

- `props.enabled`: expression

```js
((!{view.custom.roCommand} && !({view.params.tagPath} = '') && (if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) = 2 || (if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) >= 6 && if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/HmiStatus')), -1)) <= 9))) && coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/HmiStatus')), false), false)
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/CardControls/SetBack/BtnSetback`**

- `props.enabled`: expression

```js
((!{view.custom.roCommand} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), false), false)
```


- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), '—', if(if({view.params.tagPath} = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/SB_Enable')), false), false)), 'Set Back Enabled', 'Set Back Disabled'))
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), false), false), if(if({view.params.tagPath} = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/SB_Enable')), false), false)), '#2E7D32', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), false), false), if(if({view.params.tagPath} = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/SB_Enable')), false), false)), '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/SB_Enable')), true), true), 'faceplate-cmd-btn Fonts/Label value-bad', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/CardControls/Interlock/InterlockBtn`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + "/Interlock")
```


**`root/CardDefrost/Mode/ModeSeg/Opt0`**

- `props.enabled`: expression

```js
((!{view.custom.roSetpoint} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false)
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 0, '#1E88E5', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 0, '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.text`: expression

```js
try(lookup({[default]_Config/Enums/Evaporator/DefrostStartMode}, toInt(0), 'ToD', 'value', 'short'), 'ToD')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Mode/ModeSeg/Opt1`**

- `props.enabled`: expression

```js
((!{view.custom.roSetpoint} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false)
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 1, '#1E88E5', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 1, '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.text`: expression

```js
try(lookup({[default]_Config/Enums/Evaporator/DefrostStartMode}, toInt(1), 'Cooling', 'value', 'short'), 'Cooling')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Mode/ModeSeg/Opt2`**

- `props.enabled`: expression

```js
((!{view.custom.roSetpoint} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false)
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 2, '#1E88E5', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 2, '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.text`: expression

```js
try(lookup({[default]_Config/Enums/Evaporator/DefrostStartMode}, toInt(2), 'Runtime', 'value', 'short'), 'Runtime')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Mode/CurrentMode`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), '—', if({view.params.tagPath} = '', '', try('Current Mode: ' + lookup({[default]_Config/Enums/Evaporator/DefrostStartMode}, toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), toStr(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode'))), 'value', 'label'), '')))
```


- `position.display`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), if({view.params.tagPath} = '', false, try(!toBoolean(lookup({[default]_Config/Enums/Evaporator/DefrostStartMode}, toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false, 'value', 'selectable')), false)), false)
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), true), true), 'Fonts/Label fs-13 fw-600 value-bad', 'Fonts/Label fs-13 fw-600')
```


**`root/CardDefrost/Fans/FansSeg/Opt0`**

- `props.enabled`: expression

```js
((!{view.custom.roSetpoint} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false)
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1)) = 0, '#1E88E5', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1)) = 0, '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.text`: expression

```js
try(lookup({[default]_Config/Enums/Evaporator/CycleFans}, toInt(0), 'Off', 'value', 'short'), 'Off')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Fans/FansSeg/Opt1`**

- `props.enabled`: expression

```js
((!{view.custom.roSetpoint} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false)
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1)) = 1, '#1E88E5', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1)) = 1, '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.text`: expression

```js
try(lookup({[default]_Config/Enums/Evaporator/CycleFans}, toInt(1), 'Cycle', 'value', 'short'), 'Cycle')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Fans/FansSeg/Opt2`**

- `props.enabled`: expression

```js
((!{view.custom.roSetpoint} && !({view.params.tagPath} = '')) && coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.enabled`: expression

```js
!({view.params.tagPath} = '') && !coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false)
```


- `props.style.backgroundColor`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1)) = 2, '#1E88E5', 'var(--surface-container)'), 'var(--surface-container)')
```


- `props.style.color`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), false), false), if(if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_CycFans')), -1)) = 2, '#ffffff', 'var(--text)'), 'var(--neutral-60)')
```


- `props.text`: expression

```js
try(lookup({[default]_Config/Enums/Evaporator/CycleFans}, toInt(2), 'On', 'value', 'short'), 'On')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/ToDSchedule`**

- `position.display`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), {view.params.tagPath} = '' || if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 0 || if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = -1, false)
```


**`root/CardDefrost/Groups/ToDSchedule/Def1stTOD/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_Def1stTOD')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/ToDSchedule/Def2ndTOD/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_Def2ndTOD')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/ToDSchedule/Def3rdTOD/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_Def3rdTOD')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/ToDSchedule/Def4thTOD/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_Def4thTOD')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/CoolingSchedule`**

- `position.display`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), !({view.params.tagPath} = '') && if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 1, false)
```


**`root/CardDefrost/Groups/CoolingSchedule/CoolingLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), '—', if({view.params.tagPath} = '', '--', if(try(isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), false), numberFormat(toFloat(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), '#,##0.0') + ' min', '--')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_CoolingTime')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')
```


**`root/CardDefrost/Groups/CoolingSchedule/CoolingSP/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_CoolingTime')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/RuntimeSchedule`**

- `position.display`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), false), false), !({view.params.tagPath} = '') && if({view.params.tagPath} = '', -1, try(toInt(tag({view.params.tagPath} + '/CG/Cfg_DefrostStartMode')), -1)) = 2, false)
```


**`root/CardDefrost/Groups/RuntimeSchedule/RuntimeLeft/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), '—', if({view.params.tagPath} = '', '--', if(try(isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), false), numberFormat(toFloat(tag({view.params.tagPath} + '/CG/Val_RunTime')), '#,##0.0') + ' min', '--')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/CG/Val_RunTime')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')
```


**`root/CardDefrost/Groups/RuntimeSchedule/RuntimeSP/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_RunTime')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/StepTimers/PumpOut/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_PumpOut')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/StepTimers/MainHotGas/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_MainHotGas')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/StepTimers/Bleed/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_Bleed')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardDefrost/Groups/StepTimers/FanDelay/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_FanDelay')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardTemperature/ZoneAirTemp/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), '—', if({view.params.tagPath} = '', '--', if(try(isGood(tag({view.params.tagPath} + '/ZAT/Val')), false), numberFormat(toFloat(tag({view.params.tagPath} + '/ZAT/Val')), '#,##0.0') + ' °F', '--')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/ZAT/Val')), true), true), 'Fonts/Value value-bad', if((coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/TooHot')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/TooCold')), false), false)), 'Fonts/Value value-alarm', 'Fonts/Value'))
```


**`root/CardTemperature/TargetSP/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_ZoneAirTemp')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardTemperature/Deadband/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/Cfg_ZoneAirTempDB')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardTemperature/Setback/SBMin/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/ZAT_MinSet')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardTemperature/Setback/SBMax/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/ZAT_MaxSet')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardTemperature/Setback/SBStart/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/SB_StartTime')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/CardTemperature/Setback/SBStop/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + '/CG/SB_StopTime')
```


- `props.params.permission`: expression

```js
(!{view.custom.roSetpoint}) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 13 event actions, change scripts and handlers</summary>

- **`root/CardControls/Enable/BtnEnable`** `component.onActionPerformed`, script action, scope `G`

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
    label='Enable Evaporator',
    tagPath=path,
    newValue=not bool(cur),
    oldValue=bool(cur),
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CardControls/Defrost/BtnStartDefrost`** `component.onActionPerformed`, script action, scope `G`

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

- **`root/CardControls/Defrost/BtnStopDefrost`** `component.onActionPerformed`, script action, scope `G`

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

- **`root/CardControls/SetBack/BtnSetback`** `component.onActionPerformed`, script action, scope `G`

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

- **`root/CardDefrost/Mode/ModeSeg/Opt0`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roSetpoint:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/Cfg_DefrostStartMode'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Defrost Mode',
    tagPath=path,
    newValue=0,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CardDefrost/Mode/ModeSeg/Opt1`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roSetpoint:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/Cfg_DefrostStartMode'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Defrost Mode',
    tagPath=path,
    newValue=1,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CardDefrost/Mode/ModeSeg/Opt2`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roSetpoint:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/Cfg_DefrostStartMode'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Defrost Mode',
    tagPath=path,
    newValue=2,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CardDefrost/Fans/FansSeg/Opt0`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roSetpoint:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/Cfg_CycFans'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Cycle Fans',
    tagPath=path,
    newValue=0,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CardDefrost/Fans/FansSeg/Opt1`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roSetpoint:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/Cfg_CycFans'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Cycle Fans',
    tagPath=path,
    newValue=1,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CardDefrost/Fans/FansSeg/Opt2`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roSetpoint:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/CG/Cfg_CycFans'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Cycle Fans',
    tagPath=path,
    newValue=2,
    oldValue=cur,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/CardDefrost/Groups/CoolingSchedule/CoolingLeft/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/CG/Val_CoolingTime')
```

- **`root/CardDefrost/Groups/RuntimeSchedule/RuntimeLeft/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/CG/Val_RunTime')
```

- **`root/CardTemperature/ZoneAirTemp/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/ZAT/Val')
```

</details>

## Related Views

**Embeds** (3): [02\_Components/00\_Controls/InterlockButton](../../../../02-components/00-controls/interlockbutton.md), [03\_Elements/00\_Control/AnalogInput](../../../../03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/TimeInput](../../../../03-elements/00-control/timeinput.md)

**Embedded in** (1): [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](./ahuevapdisplay.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 44 | style class |
| `Fonts/Value` | 3 | style class |
| `bg-page` | 1 | style class |
| `cg-panel` | 1 | stylesheet |
| `faceplate-cmd-btn` | 10 | style class |
| `faceplate-section` | 3 | style class |
| `faceplate-section-card` | 3 | style class |
| `faceplate-section-title` | 3 | style class |
| `fs-13` | 1 | style class |
| `fw-600` | 1 | style class |
| `fw-700` | 7 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Enums/Evaporator/CycleFans`
- `[default]_Config/Enums/Evaporator/DefrostStartMode`
- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>33 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/CG/Cfg_Bleed`, `/CG/Cfg_CoolingTime`, `/CG/Cfg_CycFans`, `/CG/Cfg_Def1stTOD`, `/CG/Cfg_Def2ndTOD`, `/CG/Cfg_Def3rdTOD`, `/CG/Cfg_Def4thTOD`, `/CG/Cfg_DefrostStartMode`, `/CG/Cfg_FanDelay`, `/CG/Cfg_MainHotGas`, `/CG/Cfg_PumpOut`, `/CG/Cfg_RunTime`, `/CG/Cfg_ZoneAirTemp`, `/CG/Cfg_ZoneAirTempDB`, `/CG/HMIEnable`, `/CG/HMIStartDefrost`, `/CG/HMIStopDefrost`, `/CG/SB_Enable`, `/CG/SB_StartTime`, `/CG/SB_StopTime`, `/CG/TooCold`, `/CG/TooHot`, `/CG/Val_CoolingTime`, `/CG/Val_RunTime`, `/CG/ZAT_MaxSet`, `/CG/ZAT_MinSet`, `/DIn.Enabled`, `/HmiStatus`, `/Interlock`, `/ZAT/Val`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
