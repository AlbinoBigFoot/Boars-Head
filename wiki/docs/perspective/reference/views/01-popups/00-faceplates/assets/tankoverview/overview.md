---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/TankOverview/Overview (Asset (embedded piece)): 90 components, 161 bindings, 11 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/TankOverview/Overview", "Overview"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/TankOverview/Overview`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/TankOverview/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; TankOverview &gt; Overview |
| Root | `ia.container.flex`, height 680, width 940 |
| Size | 90 components, 161 bindings, 11 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-24T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

<details>
<summary>51 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `pax` | `null` | bound (expr) |
| `ok` | `null` | bound (expr) |
| `lvl` | `null` | bound (expr) |
| `eu` | `null` | bound (expr) |
| `lmax` | `null` | bound (expr) |
| `lmin` | `null` | bound (expr) |
| `hh` | `null` | bound (expr) |
| `h` | `null` | bound (expr) |
| `l` | `null` | bound (expr) |
| `ll` | `null` | bound (expr) |
| `sHH` | `null` | bound (expr) |
| `sH` | `null` | bound (expr) |
| `sL` | `null` | bound (expr) |
| `sLL` | `null` | bound (expr) |
| `sFail` | `null` | bound (expr) |
| `tone` | `null` | bound (expr) |
| `state` | `null` | bound (expr) |
| `oper` | `null` | bound (expr) |
| `lock` | `null` | bound (expr) |
| `lvlLabel` | `null` | bound (expr) |
| `pump1` | `null` | bound (expr) |
| `pump2` | `null` | bound (expr) |
| `hasPumps` | `null` | bound (expr) |
| `slPath` | `null` | bound (expr) |
| `pumpP` | `null` | bound (expr) |
| `pumpEU` | `null` | bound (expr) |
| `pumpLabel` | `null` | bound (expr) |
| `hasSuct` | `null` | bound (expr) |
| `suct` | `null` | bound (expr) |
| `suctEU` | `null` | bound (expr) |
| `suctLabel` | `null` | bound (expr) |
| `lead` | `null` | bound (expr) |
| `pump1Run` | `null` | bound (expr) |
| `pump2Run` | `null` | bound (expr) |
| `pump1Alm` | `null` | bound (expr) |
| `pump2Alm` | `null` | bound (expr) |
| `pump1Ilk` | `null` | bound (expr) |
| `pump2Ilk` | `null` | bound (expr) |
| `swHlcoDIn` | `null` | bound (expr) |
| `swHiHiDIn` | `null` | bound (expr) |
| `swOplDIn` | `null` | bound (expr) |
| `swLoLoDIn` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |
| `roMode` | `true` | bound (expr) |
| `tipMode` | `""` | bound (expr) |
| `pump1Pax` | `""` | bound (expr) |
| `pump2Pax` | `""` | bound (expr) |
| `sensorSLPax` | `""` | bound (expr) |
| `sensorSSPax` | `""` | bound (expr) |

</details>

## Component Tree

Component types: ia.container.flex x41, ia.display.label x35, ia.input.button x8, ia.display.view x5, ia.container.coord x1.

<details>
<summary>Component tree (90 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Level  ia.container.flex
    Head  ia.container.flex
      Title  ia.display.label
      Tag  ia.display.label  [1 binding]
    PV  ia.container.flex
      Val  ia.display.label  [2 bindings; 1 event]
      Eu  ia.display.label  [1 binding]
    State  ia.container.flex
      Pill  ia.display.label  [2 bindings]
    Gauge  ia.container.coord
      Track  ia.container.flex
      Fill  ia.container.flex  [4 bindings]
      Max  ia.display.label  [1 binding]
      Min  ia.display.label  [1 binding]
      TickHH  ia.container.flex  [2 bindings]
      LimHH  ia.display.label  [4 bindings]
      TickH  ia.container.flex  [2 bindings]
      LimH  ia.display.label  [4 bindings]
      TickL  ia.container.flex  [2 bindings]
      LimL  ia.display.label  [4 bindings]
      TickLL  ia.container.flex  [2 bindings]
      LimLL  ia.display.label  [4 bindings]
    Mode  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    Commands  ia.container.flex
      Lock  ia.input.button  [4 bindings; 1 event]
      Reset  ia.input.button  [3 bindings; 1 event]
  Right  ia.container.flex
    Switches  ia.container.flex  [1 binding]
      Head  ia.container.flex
        Title  ia.display.label
      Tiles  ia.container.flex
        SwHlcoDIn  ia.display.view  [4 bindings; view: 00_Pages/Groveport/Utility/OverviewStatusTile]
        SwHiHiDIn  ia.display.view  [4 bindings; view: 00_Pages/Groveport/Utility/OverviewStatusTile]
        SwOplDIn  ia.display.view  [4 bindings; view: 00_Pages/Groveport/Utility/OverviewStatusTile]
        SwLoLoDIn  ia.display.view  [4 bindings; view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    Pressures  ia.container.flex  [1 binding]
      Head  ia.container.flex
        Title  ia.display.label
      Kpis  ia.container.flex
        PumpsPressure  ia.container.flex  [1 binding]
          Head  ia.container.flex
            Cap  ia.display.label
            Tag  ia.display.label  [1 binding]
          Value  ia.container.flex
            Val  ia.display.label  [2 bindings; 1 event]
            Eu  ia.display.label  [1 binding]
        SuctionPressure  ia.container.flex  [1 binding]
          Head  ia.container.flex
            Cap  ia.display.label
            Tag  ia.display.label  [1 binding]
          Value  ia.container.flex
            Val  ia.display.label  [2 bindings]
            Eu  ia.display.label  [1 binding]
    Pumps  ia.container.flex  [1 binding]
      Head  ia.container.flex
        Title  ia.display.label
      LeadPump  ia.container.flex
        Lbl  ia.display.label
        Lead  ia.container.flex
          Lead1  ia.input.button  [4 bindings; 1 event]
          Lead2  ia.input.button  [4 bindings; 1 event]
      StartPressure  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
      Cards  ia.container.flex
        Pump1  ia.container.flex
          Head  ia.container.flex
            Name  ia.container.flex
              Cap  ia.display.label
              Val  ia.display.label  [1 binding]
            Lead  ia.display.label  [3 bindings]
          Status  ia.container.flex
            Run  ia.display.label  [2 bindings]
            Alarm  ia.display.label  [2 bindings]
          Buttons  ia.container.flex
            Interlocks  ia.input.button  [3 bindings; 1 event]
            Open  ia.input.button  [1 binding; 1 event]
        Pump2  ia.container.flex
          Head  ia.container.flex
            Name  ia.container.flex
              Cap  ia.display.label
              Val  ia.display.label  [1 binding]
            Lead  ia.display.label  [3 bindings]
          Status  ia.container.flex
            Run  ia.display.label  [2 bindings]
            Alarm  ia.display.label  [2 bindings]
          Buttons  ia.container.flex
            Interlocks  ia.input.button  [3 bindings; 1 event]
            Open  ia.input.button  [1 binding; 1 event]
```

</details>

## Bindings

161 bindings: expr 161.

<details>
<summary>All 161 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.ok`: expression

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val')), false), false)
```


- `custom.lvl`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val')), false), false), toFloat(tag({view.params.tagPath} + '/LvlAIn/Val')), null)
```


- `custom.eu`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_EU')), false), false), if(len(toStr(tag({view.params.tagPath} + '/LvlAIn/Cfg_EU'))) > 0, toStr(tag({view.params.tagPath} + '/LvlAIn/Cfg_EU')), '%'), if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val.EngUnit')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/LvlAIn/Val.EngUnit')), '%'), '%'))
```


- `custom.lmax`: expression

```js
coalesce(if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMax')), false), false), if(abs(toFloat(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMax'))) < 1e30, toFloat(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMax')), null), null), 100)
```


- `custom.lmin`: expression

```js
coalesce(if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMin')), false), false), if(abs(toFloat(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMin'))) < 1e30, toFloat(tag({view.params.tagPath} + '/LvlAIn/Cfg_PVEUMin')), null), null), 0)
```


- `custom.hh`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_HiHiLim')), false), false), if(abs(toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_HiHiLim'))) < 1e30, toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_HiHiLim')), null), null)
```


- `custom.h`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_HiLim')), false), false), if(abs(toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_HiLim'))) < 1e30, toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_HiLim')), null), null)
```


- `custom.l`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_LoLim')), false), false), if(abs(toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_LoLim'))) < 1e30, toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_LoLim')), null), null)
```


- `custom.ll`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val_LoLoLim')), false), false), if(abs(toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_LoLoLim'))) < 1e30, toFloat(tag({view.params.tagPath} + '/LvlAIn/Val_LoLoLim')), null), null)
```


- `custom.sHH`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_HiHi')), false), false), toBoolean(tag({view.params.tagPath} + '/LvlAIn/Sts_HiHi')), null)
```


- `custom.sH`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Hi')), false), false), toBoolean(tag({view.params.tagPath} + '/LvlAIn/Sts_Hi')), null)
```


- `custom.sL`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Lo')), false), false), toBoolean(tag({view.params.tagPath} + '/LvlAIn/Sts_Lo')), null)
```


- `custom.sLL`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_LoLo')), false), false), toBoolean(tag({view.params.tagPath} + '/LvlAIn/Sts_LoLo')), null)
```


- `custom.sFail`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Fail')), false), false), toBoolean(tag({view.params.tagPath} + '/LvlAIn/Sts_Fail')), null)
```


- `custom.tone`: expression

```js
if(!coalesce({view.custom.ok}, false) || isNull({view.custom.lvl}), 'off', if(coalesce({view.custom.sHH}, false) || coalesce({view.custom.sLL}, false) || coalesce({view.custom.sFail}, false), 'alarm', if(coalesce({view.custom.sH}, false) || coalesce({view.custom.sL}, false), 'warn', 'ok')))
```


- `custom.state`: expression

```js
if(!coalesce({view.custom.ok}, false) || isNull({view.custom.lvl}), '—', if(coalesce({view.custom.sFail}, false), 'Input Failure', if(coalesce({view.custom.sHH}, false), 'High-High', if(coalesce({view.custom.sLL}, false), 'Low-Low', if(coalesce({view.custom.sH}, false), 'High', if(coalesce({view.custom.sL}, false), 'Low', 'Normal'))))))
```


- `custom.oper`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Oper')), false), false), toBoolean(tag({view.params.tagPath} + '/LvlAIn/Sts_Oper')), null)
```


- `custom.lock`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Mode/Sts_ProgOperLock')), false), false), toBoolean(tag({view.params.tagPath} + '/LvlAIn/Mode/Sts_ProgOperLock')), null)
```


- `custom.lvlLabel`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Cfg_Label')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/LvlAIn/Cfg_Label')), ''), '')
```


- `custom.pump1`: expression

```js
if(lastIndexOf({view.params.tagPath}, '/Tanks/') < 0, '', substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1')
```


- `custom.pump2`: expression

```js
if(lastIndexOf({view.params.tagPath}, '/Tanks/') < 0, '', substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2')
```


- `custom.hasPumps`: expression

```js
{view.custom.pump1} != '' && coalesce(try(isGood(tag({view.custom.pump1} + '.TypeId')), false), false)
```


- `custom.slPath`: expression

```js
if(lastIndexOf({view.params.tagPath}, '/Tanks/') < 0, '', substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Sensors/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), 1) + 'SL-Pumps Pressure/AIn')
```


- `custom.pumpP`: expression

```js
if(coalesce({view.custom.hasPumps}, false), if(coalesce(try(isGood(tag({view.custom.slPath} + '/Val')), false), false), toFloat(tag({view.custom.slPath} + '/Val')), null), null)
```


- `custom.pumpEU`: expression

```js
if(coalesce(try(isGood(tag({view.custom.slPath} + '/Cfg_EU')), false), false), coalesce(toStr(tag({view.custom.slPath} + '/Cfg_EU')), 'PSIG'), 'PSIG')
```


- `custom.pumpLabel`: expression

```js
if(coalesce(try(isGood(tag({view.custom.slPath} + '/Cfg_Label')), false), false), coalesce(toStr(tag({view.custom.slPath} + '/Cfg_Label')), ''), '')
```


- `custom.hasSuct`: expression

```js
coalesce(try(toBoolean(tag({view.params.tagPath} + '/PressAIn.Enabled')), false), false)
```


- `custom.suct`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/PressAIn/Val')), false), false), toFloat(tag({view.params.tagPath} + '/PressAIn/Val')), null)
```


- `custom.suctEU`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/PressAIn/Cfg_EU')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/PressAIn/Cfg_EU')), 'PSIG'), 'PSIG')
```


- `custom.suctLabel`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/PressAIn/Cfg_Label')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/PressAIn/Cfg_Label')), ''), '')
```


- `custom.lead`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LeadPump')), false), false), toInt(tag({view.params.tagPath} + '/LeadPump')), null)
```


- `custom.pump1Run`: expression

```js
if(coalesce(try(isGood(tag({view.custom.pump1} + '/Motor/Sts_Running')), false), false), toBoolean(tag({view.custom.pump1} + '/Motor/Sts_Running')), null)
```


- `custom.pump2Run`: expression

```js
if(coalesce(try(isGood(tag({view.custom.pump2} + '/Motor/Sts_Running')), false), false), toBoolean(tag({view.custom.pump2} + '/Motor/Sts_Running')), null)
```


- `custom.pump1Alm`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Pump1Alm/Sts')), false), false), toBoolean(tag({view.params.tagPath} + '/Pump1Alm/Sts')), null)
```


- `custom.pump2Alm`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Pump2Alm/Sts')), false), false), toBoolean(tag({view.params.tagPath} + '/Pump2Alm/Sts')), null)
```


- `custom.pump1Ilk`: expression

```js
if(coalesce(try(isGood(tag({view.custom.pump1} + '/Intlk/Sts_IntlkOK')), false), false), toBoolean(tag({view.custom.pump1} + '/Intlk/Sts_IntlkOK')), null)
```


- `custom.pump2Ilk`: expression

```js
if(coalesce(try(isGood(tag({view.custom.pump2} + '/Intlk/Sts_IntlkOK')), false), false), toBoolean(tag({view.custom.pump2} + '/Intlk/Sts_IntlkOK')), null)
```


- `custom.swHlcoDIn`: expression

```js
coalesce(try(toBoolean(tag({view.params.tagPath} + '/HlcoDIn.Enabled')), false), false)
```


- `custom.swHiHiDIn`: expression

```js
coalesce(try(toBoolean(tag({view.params.tagPath} + '/HiHiDIn.Enabled')), false), false)
```


- `custom.swOplDIn`: expression

```js
coalesce(try(toBoolean(tag({view.params.tagPath} + '/OplDIn.Enabled')), false), false)
```


- `custom.swLoLoDIn`: expression

```js
coalesce(try(toBoolean(tag({view.params.tagPath} + '/LoLoDIn.Enabled')), false), false)
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


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Level/Head/Tag`**

- `props.text`: expression

```js
{view.custom.lvlLabel}
```


**`root/Level/PV/Val`**

- `props.text`: expression

```js
if(isNull({view.custom.lvl}), '—', numberFormat({view.custom.lvl}, '#,##0.00'))
```


- `props.style.classes`: expression

```js
'fp-hero ' + case({view.custom.tone}, 'ok', 'fp-text-normal', 'warn', 'fp-text-warn', 'alarm', 'fp-text-alarm', 'value-bad')
```


**`root/Level/PV/Eu`**

- `props.text`: expression

```js
{view.custom.eu}
```


**`root/Level/State/Pill`**

- `props.text`: expression

```js
{view.custom.state}
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + case({view.custom.tone}, 'ok', 'ok', 'warn', 'warn', 'alarm', 'alarm', 'muted')
```


**`root/Level/Gauge/Fill`**

- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.lvl}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin}))))
```


- `position.height`: expression

```js
if(isNull({view.custom.lvl}), 0, 284 * max(0, min(1, (coalesce({view.custom.lvl}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin}))))
```


- `meta.visible`: expression

```js
!isNull({view.custom.lvl})
```


- `props.style.classes`: expression

```js
'fp-gauge-' + {view.custom.tone}
```


**`root/Level/Gauge/Max`**

- `props.text`: expression

```js
if(isNull({view.custom.lmax}), '—', numberFormat({view.custom.lmax}, '#,##0.00'))
```


**`root/Level/Gauge/Min`**

- `props.text`: expression

```js
if(isNull({view.custom.lmin}), '—', numberFormat({view.custom.lmin}, '#,##0.00'))
```


**`root/Level/Gauge/TickHH`**

- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.hh}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 1
```


- `meta.visible`: expression

```js
!isNull({view.custom.hh})
```


**`root/Level/Gauge/LimHH`**

- `props.text`: expression

```js
'HH  ' + if(isNull({view.custom.hh}), '—', numberFormat({view.custom.hh}, '#,##0.00'))
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.sHH}, false), 'fp-mark fp-text-alarm', 'fp-mark')
```


- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.hh}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 9
```


- `meta.visible`: expression

```js
!isNull({view.custom.hh})
```


**`root/Level/Gauge/TickH`**

- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.h}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 1
```


- `meta.visible`: expression

```js
!isNull({view.custom.h})
```


**`root/Level/Gauge/LimH`**

- `props.text`: expression

```js
'H  ' + if(isNull({view.custom.h}), '—', numberFormat({view.custom.h}, '#,##0.00'))
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.sH}, false), 'fp-mark fp-text-warn', 'fp-mark')
```


- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.h}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 9
```


- `meta.visible`: expression

```js
!isNull({view.custom.h})
```


**`root/Level/Gauge/TickL`**

- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.l}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 1
```


- `meta.visible`: expression

```js
!isNull({view.custom.l})
```


**`root/Level/Gauge/LimL`**

- `props.text`: expression

```js
'L  ' + if(isNull({view.custom.l}), '—', numberFormat({view.custom.l}, '#,##0.00'))
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.sL}, false), 'fp-mark fp-text-warn', 'fp-mark')
```


- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.l}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 9
```


- `meta.visible`: expression

```js
!isNull({view.custom.l})
```


**`root/Level/Gauge/TickLL`**

- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.ll}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 1
```


- `meta.visible`: expression

```js
!isNull({view.custom.ll})
```


**`root/Level/Gauge/LimLL`**

- `props.text`: expression

```js
'LL  ' + if(isNull({view.custom.ll}), '—', numberFormat({view.custom.ll}, '#,##0.00'))
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.sLL}, false), 'fp-mark fp-text-alarm', 'fp-mark')
```


- `position.y`: expression

```js
8 + 284 * (1 - max(0, min(1, (coalesce({view.custom.ll}, {view.custom.lmin}) - {view.custom.lmin}) / if({view.custom.lmax} - {view.custom.lmin} = 0, 1, {view.custom.lmax} - {view.custom.lmin})))) - 9
```


- `meta.visible`: expression

```js
!isNull({view.custom.ll})
```


**`root/Level/Mode/Val`**

- `props.text`: expression

```js
if(!coalesce({view.custom.ok}, false), '—', if(coalesce({view.custom.oper}, false), if(coalesce({view.custom.lock}, false), 'Operator  ·  Locked', 'Operator  ·  Unlocked'), 'Program'))
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.ok}, false), 'fp-row-value', 'fp-row-value value-bad')
```


**`root/Level/Commands/Lock`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roMode}, false) && {view.params.tagPath} != '' && coalesce({view.custom.pax}, '') = '' && (coalesce({view.custom.lock}, false) || coalesce({view.custom.oper}, false))
```


- `props.text`: expression

```js
if(coalesce({view.custom.lock}, false), 'Unlock Operator', 'Lock Operator')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/Level/Commands/Reset`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roCommand}, false) && {view.params.tagPath} != '' && coalesce({view.custom.pax}, '') = '' && (coalesce({view.custom.sFail}, false) || coalesce({view.custom.sHH}, false) || coalesce({view.custom.sH}, false) || coalesce({view.custom.sL}, false) || coalesce({view.custom.sLL}, false))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/Right/Switches`**

- `position.display`: expression

```js
coalesce({view.custom.swHlcoDIn}, false) || coalesce({view.custom.swHiHiDIn}, false) || coalesce({view.custom.swOplDIn}, false) || coalesce({view.custom.swLoLoDIn}, false)
```


**`root/Right/Switches/Tiles/SwHlcoDIn`**

- `props.params.label`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Cfg_Label')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/HlcoDIn/Cfg_Label')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'HLCO' = 'LOLO LEVEL', 'LO LEVEL', 'HLCO')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'HLCO' = 'LOLO LEVEL', 'LO LEVEL', 'HLCO'))
```


- `props.params.tagPath`: expression

```js
{view.params.tagPath} + '/HlcoDIn/Sts'
```


- `props.params.diPath`: expression

```js
{view.params.tagPath} + '/DI_HLCO'
```


- `position.display`: expression

```js
coalesce({view.custom.swHlcoDIn}, false)
```


**`root/Right/Switches/Tiles/SwHiHiDIn`**

- `props.params.label`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Cfg_Label')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/HiHiDIn/Cfg_Label')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'HI LEVEL' = 'LOLO LEVEL', 'LO LEVEL', 'HI LEVEL')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'HI LEVEL' = 'LOLO LEVEL', 'LO LEVEL', 'HI LEVEL'))
```


- `props.params.tagPath`: expression

```js
{view.params.tagPath} + '/HiHiDIn/Sts'
```


- `props.params.diPath`: expression

```js
{view.params.tagPath} + '/DI_HiLevel'
```


- `position.display`: expression

```js
coalesce({view.custom.swHiHiDIn}, false)
```


**`root/Right/Switches/Tiles/SwOplDIn`**

- `props.params.label`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Cfg_Label')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/OplDIn/Cfg_Label')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'OPL' = 'LOLO LEVEL', 'LO LEVEL', 'OPL')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'OPL' = 'LOLO LEVEL', 'LO LEVEL', 'OPL'))
```


- `props.params.tagPath`: expression

```js
{view.params.tagPath} + '/OplDIn/Sts'
```


- `props.params.diPath`: expression

```js
{view.params.tagPath} + '/DI_OPL'
```


- `position.display`: expression

```js
coalesce({view.custom.swOplDIn}, false)
```


**`root/Right/Switches/Tiles/SwLoLoDIn`**

- `props.params.label`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Cfg_Label')), false), false), coalesce(toStr(tag({view.params.tagPath} + '/LoLoDIn/Cfg_Label')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'LOLO LEVEL' = 'LOLO LEVEL', 'LO LEVEL', 'LOLO LEVEL')), substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) + '-' + if(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1) = 'HPR' && 'LOLO LEVEL' = 'LOLO LEVEL', 'LO LEVEL', 'LOLO LEVEL'))
```


- `props.params.tagPath`: expression

```js
{view.params.tagPath} + '/LoLoDIn/Sts'
```


- `props.params.diPath`: expression

```js
{view.params.tagPath} + '/DI_LoLo'
```


- `position.display`: expression

```js
coalesce({view.custom.swLoLoDIn}, false)
```


**`root/Right/Pressures`**

- `position.display`: expression

```js
coalesce({view.custom.hasPumps}, false) || coalesce({view.custom.hasSuct}, false)
```


**`root/Right/Pressures/Kpis/PumpsPressure`**

- `position.display`: expression

```js
coalesce({view.custom.hasPumps}, false)
```


**`root/Right/Pressures/Kpis/PumpsPressure/Head/Tag`**

- `props.text`: expression

```js
{view.custom.pumpLabel}
```


**`root/Right/Pressures/Kpis/PumpsPressure/Value/Val`**

- `props.text`: expression

```js
if(isNull({view.custom.pumpP}), '—', numberFormat({view.custom.pumpP}, '#,##0.00'))
```


- `props.style.classes`: expression

```js
if(if(isNull({view.custom.pumpP}), '—', numberFormat({view.custom.pumpP}, '#,##0.00')) = '—', 'fp-kpi value-bad', 'fp-kpi')
```


**`root/Right/Pressures/Kpis/PumpsPressure/Value/Eu`**

- `props.text`: expression

```js
{view.custom.pumpEU}
```


**`root/Right/Pressures/Kpis/SuctionPressure`**

- `position.display`: expression

```js
coalesce({view.custom.hasSuct}, false)
```


**`root/Right/Pressures/Kpis/SuctionPressure/Head/Tag`**

- `props.text`: expression

```js
{view.custom.suctLabel}
```


**`root/Right/Pressures/Kpis/SuctionPressure/Value/Val`**

- `props.text`: expression

```js
if(isNull({view.custom.suct}), '—', numberFormat({view.custom.suct}, '#,##0.00'))
```


- `props.style.classes`: expression

```js
if(if(isNull({view.custom.suct}), '—', numberFormat({view.custom.suct}, '#,##0.00')) = '—', 'fp-kpi value-bad', 'fp-kpi')
```


**`root/Right/Pressures/Kpis/SuctionPressure/Value/Eu`**

- `props.text`: expression

```js
{view.custom.suctEU}
```


**`root/Right/Pumps`**

- `position.display`: expression

```js
coalesce({view.custom.hasPumps}, false)
```


**`root/Right/Pumps/LeadPump/Lead/Lead1`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roCommand}, false) && {view.params.tagPath} != '' && coalesce({view.custom.pax}, '') = '' && coalesce({view.custom.lead}, 0) != 1
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.lead}, 0) = 1, 'form-btn-primary', 'form-btn')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/Right/Pumps/LeadPump/Lead/Lead2`**

- `props.enabled`: expression

```js
!coalesce({view.custom.roCommand}, false) && {view.params.tagPath} != '' && coalesce({view.custom.pax}, '') = '' && coalesce({view.custom.lead}, 0) != 2
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.lead}, 0) = 2, 'form-btn-primary', 'form-btn')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/Right/Pumps/StartPressure`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/StartPress')
```


- `props.params.readOnly`: expression

```js
coalesce({view.custom.pax}, '') != ''
```


**`root/Right/Pumps/Cards/Pump1/Head/Name/Val`**

- `props.text`: expression

```js
substring({view.custom.pump1}, lastIndexOf({view.custom.pump1}, '/') + 1)
```


**`root/Right/Pumps/Cards/Pump1/Head/Lead`**

- `props.text`: expression

```js
'Lead'
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + 'accent'
```


- `position.display`: expression

```js
coalesce({view.custom.lead}, 0) = 1
```


**`root/Right/Pumps/Cards/Pump1/Status/Run`**

- `props.text`: expression

```js
if(isNull({view.custom.pump1Run}), '—', if({view.custom.pump1Run}, 'Running', 'Stopped'))
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + if(isNull({view.custom.pump1Run}), 'muted', if({view.custom.pump1Run}, 'ok', 'off'))
```


**`root/Right/Pumps/Cards/Pump1/Status/Alarm`**

- `props.text`: expression

```js
if(isNull({view.custom.pump1Alm}), '—', if({view.custom.pump1Alm}, 'Alarm', 'No Alarm'))
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + if(isNull({view.custom.pump1Alm}), 'muted', if({view.custom.pump1Alm}, 'alarm', 'muted'))
```


**`root/Right/Pumps/Cards/Pump1/Buttons/Interlocks`**

- `props.enabled`: expression

```js
{view.params.tagPath} != ''
```


- `props.style.classes`: expression

```js
if(isNull({view.custom.pump1Ilk}), 'form-btn', 'form-btn fp-pill-btn fp-tone-' + if({view.custom.pump1Ilk}, 'ok', 'alarm'))
```


- `props.text`: expression

```js
if(isNull({view.custom.pump1Ilk}), 'Interlocks', if({view.custom.pump1Ilk}, 'Interlocks OK', 'Interlocked'))
```


**`root/Right/Pumps/Cards/Pump1/Buttons/Open`**

- `props.enabled`: expression

```js
{view.params.tagPath} != ''
```


**`root/Right/Pumps/Cards/Pump2/Head/Name/Val`**

- `props.text`: expression

```js
substring({view.custom.pump2}, lastIndexOf({view.custom.pump2}, '/') + 1)
```


**`root/Right/Pumps/Cards/Pump2/Head/Lead`**

- `props.text`: expression

```js
'Lead'
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + 'accent'
```


- `position.display`: expression

```js
coalesce({view.custom.lead}, 0) = 2
```


**`root/Right/Pumps/Cards/Pump2/Status/Run`**

- `props.text`: expression

```js
if(isNull({view.custom.pump2Run}), '—', if({view.custom.pump2Run}, 'Running', 'Stopped'))
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + if(isNull({view.custom.pump2Run}), 'muted', if({view.custom.pump2Run}, 'ok', 'off'))
```


**`root/Right/Pumps/Cards/Pump2/Status/Alarm`**

- `props.text`: expression

```js
if(isNull({view.custom.pump2Alm}), '—', if({view.custom.pump2Alm}, 'Alarm', 'No Alarm'))
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + if(isNull({view.custom.pump2Alm}), 'muted', if({view.custom.pump2Alm}, 'alarm', 'muted'))
```


**`root/Right/Pumps/Cards/Pump2/Buttons/Interlocks`**

- `props.enabled`: expression

```js
{view.params.tagPath} != ''
```


- `props.style.classes`: expression

```js
if(isNull({view.custom.pump2Ilk}), 'form-btn', 'form-btn fp-pill-btn fp-tone-' + if({view.custom.pump2Ilk}, 'ok', 'alarm'))
```


- `props.text`: expression

```js
if(isNull({view.custom.pump2Ilk}), 'Interlocks', if({view.custom.pump2Ilk}, 'Interlocks OK', 'Interlocked'))
```


**`root/Right/Pumps/Cards/Pump2/Buttons/Open`**

- `props.enabled`: expression

```js
{view.params.tagPath} != ''
```

</details>

## Event Scripts And Handlers

- **`root/Level/PV/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/LvlAIn/Val')
```

- **`root/Level/Mode/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/LvlAIn/Val')
```

- **`root/Level/Commands/Lock`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
locked = bool(self.view.custom.lock)
cmd = 'Mode/OCmd_UnlockRel' if locked else 'Mode/OCmd_AcqLock'
shared.Alerts.confirmApplyWrite(
    label='Unlock Operator' if locked else 'Lock Operator',
    tagPath=base + '/LvlAIn/' + cmd,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root/Level/Commands/Reset`** `component.onActionPerformed`, script action, scope `G`

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

- **`root/Right/Pressures/Kpis/PumpsPressure/Value/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.slPath}/Val')
```

- **`root/Right/Pumps/LeadPump/Lead/Lead1`** `component.onActionPerformed`, script action, scope `G`

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

- **`root/Right/Pumps/LeadPump/Lead/Lead2`** `component.onActionPerformed`, script action, scope `G`

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

- **`root/Right/Pumps/Cards/Pump1/Buttons/Interlocks`** `component.onActionPerformed`, script action, scope `G`

```python
p = str(self.view.custom.pump1 or '')
if not p:
    return
shared.Alerts.showFaceplate(tagPath=p, deviceType='Pump', title=p.split('/')[-1], initialTab='Interlocks')
```

- **`root/Right/Pumps/Cards/Pump1/Buttons/Open`** `component.onActionPerformed`, script action, scope `G`

```python
p = str(self.view.custom.pump1 or '')
if not p:
    return
shared.Alerts.showFaceplate(tagPath=p, deviceType='Pump', title=p.split('/')[-1])
```

- **`root/Right/Pumps/Cards/Pump2/Buttons/Interlocks`** `component.onActionPerformed`, script action, scope `G`

```python
p = str(self.view.custom.pump2 or '')
if not p:
    return
shared.Alerts.showFaceplate(tagPath=p, deviceType='Pump', title=p.split('/')[-1], initialTab='Interlocks')
```

- **`root/Right/Pumps/Cards/Pump2/Buttons/Open`** `component.onActionPerformed`, script action, scope `G`

```python
p = str(self.view.custom.pump2 or '')
if not p:
    return
shared.Alerts.showFaceplate(tagPath=p, deviceType='Pump', title=p.split('/')[-1])
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (2): [00\_Pages/Groveport/Utility/OverviewStatusTile](../../../../00-pages/groveport/utility/overviewstatustile.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](../configuration/configfield.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/TankOverview](../../tankoverview.md)

## Style Classes

<details>
<summary>27 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `config-field-label` | 1 | stylesheet |
| `form-btn` | 8 | style class |
| `fp-card` | 4 | style class |
| `fp-card-title` | 6 | style class |
| `fp-gauge-ok` | 1 | style class |
| `fp-gauge-track` | 1 | style class |
| `fp-hero` | 1 | style class |
| `fp-kpi` | 2 | style class |
| `fp-mark` | 4 | style class |
| `fp-name` | 2 | style class |
| `fp-pill` | 7 | style class |
| `fp-row-label` | 1 | style class |
| `fp-row-value` | 1 | style class |
| `fp-scale` | 2 | style class |
| `fp-sub` | 5 | style class |
| `fp-tick-alarm` | 2 | style class |
| `fp-tick-warn` | 2 | style class |
| `fp-tile` | 4 | style class |
| `fp-unit` | 3 | style class |
| `fs-16` | 1 | style class |
| `fw-600` | 2 | style class |
| `fp-pill-btn` | bound | style class |
| `fp-text-alarm` | bound | style class |
| `fp-text-normal` | bound | style class |
| `fp-text-warn` | bound | style class |
| `value-bad` | bound | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>54 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_EU`, `/Cfg_Label`, `/DI_HLCO`, `/DI_HiLevel`, `/DI_LoLo`, `/DI_OPL`, `/DIn.Enabled`, `/HiHiDIn.Enabled`, `/HiHiDIn/Cfg_Label`, `/HiHiDIn/Sts`, `/HlcoDIn.Enabled`, `/HlcoDIn/Cfg_Label`, `/HlcoDIn/Sts`, `/Intlk/Sts_IntlkOK`, `/LeadPump`, `/LoLoDIn.Enabled`, `/LoLoDIn/Cfg_Label`, `/LoLoDIn/Sts`, `/LvlAIn/`, `/LvlAIn/Cfg_EU`, `/LvlAIn/Cfg_Label`, `/LvlAIn/Cfg_PVEUMax`, `/LvlAIn/Cfg_PVEUMin`, `/LvlAIn/Mode/Sts_ProgOperLock`, `/LvlAIn/OCmd_Reset`, `/LvlAIn/Sts_Fail`, `/LvlAIn/Sts_Hi`, `/LvlAIn/Sts_HiHi`, `/LvlAIn/Sts_Lo`, `/LvlAIn/Sts_LoLo`, `/LvlAIn/Sts_Oper`, `/LvlAIn/Val`, `/LvlAIn/Val.EngUnit`, `/LvlAIn/Val_HiHiLim`, `/LvlAIn/Val_HiLim`, `/LvlAIn/Val_LoLim`, `/LvlAIn/Val_LoLoLim`, `/Motor/Sts_Running`, `/OplDIn.Enabled`, `/OplDIn/Cfg_Label`, `/OplDIn/Sts`, `/PressAIn.Enabled`, `/PressAIn/Cfg_EU`, `/PressAIn/Cfg_Label`, `/PressAIn/Val`, `/Pump1Alm/Sts`, `/Pump2Alm/Sts`, `/Pumps/`, `/Sensors/`, `/StartPress`, `/Val`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
