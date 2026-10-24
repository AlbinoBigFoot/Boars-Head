---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Machine Room/Utility/Overview (Page): 49 components, 22 bindings, 3 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Machine Room/Utility/Overview", "Overview", "/machine-room"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Machine Room/Utility/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Machine Room/Utility/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Machine Room &gt; Utility &gt; Overview |
| Routes | `/machine-room` (Machine Room) |
| Root | `ia.container.flex`, height 791, width 1920 |
| Size | 49 components, 22 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T21:46:59Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |
| `tagPath` | `"[default]Boars_Head/GrovePort/Machine Room"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `hsdPax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.view x35, ia.display.label x9, ia.input.button x3, ia.container.flex x1, ia.container.coord x1.

<details>
<summary>Component tree (49 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Canvas  ia.container.coord  [1 binding]
    HTR  ia.display.view  [1 binding; view: 02_Components/01_Devices/Tank]
    HPR  ia.display.view  [1 binding; view: 02_Components/01_Devices/Tank]
    LTR  ia.display.view  [1 binding; view: 02_Components/01_Devices/Tank]
    HTLR-Pump 2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Pump]
    LTRL-Pump 1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Pump]
    LTRL-Pump 2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Pump]
    HTLR-Pump 1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Pump]
    Lbl-Comp1  ia.display.label
    Lbl-HTRS  ia.display.label
    COMP1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Compressor]
    COMP7  ia.display.view  [1 binding; view: 02_Components/01_Devices/Compressor]
    COMP6  ia.display.view  [1 binding; view: 02_Components/01_Devices/Compressor]
    COMP4  ia.display.view  [1 binding; view: 02_Components/01_Devices/Compressor]
    COMP5  ia.display.view  [1 binding; view: 02_Components/01_Devices/Compressor]
    MAIN LIQ SV  ia.display.view  [1 binding; view: 02_Components/01_Devices/SolenoidValve]
    OPL1_0  ia.display.view  [view: 02_Components/01_Devices/SolenoidValve]
    Condensor Nav  ia.display.view  [view: 02_Components/00_Controls/NavButton]
    OPL1_1  ia.display.view  [view: 02_Components/01_Devices/SolenoidValve]
    HSS-PT2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Sensor]
    HSS-PT3  ia.display.view  [1 binding; view: 02_Components/01_Devices/Sensor]
    HSS-PT4  ia.display.view  [1 binding; view: 02_Components/01_Devices/Sensor]
    Lbl-LTRL  ia.display.label
    Lbl-HSS  ia.display.label
    Lbl-HTR  ia.display.label
    Lbl-LTRS  ia.display.label
    Lbl-LSS  ia.display.label
    HSS-PT5  ia.display.view  [1 binding; view: 02_Components/01_Devices/Sensor]
    SAFETYS  ia.display.view  [view: 02_Components/02_Widgets/Safetys]
    Condensor Nav_0  ia.display.view  [1 binding; view: 02_Components/00_Controls/NavButton]
    HSS-SuctionSP  ia.input.button  [1 event]
    LSS-SuctionSP  ia.input.button  [1 event]
    RuptureDisks  ia.input.button  [1 event]
    LTU  ia.display.view  [view: 02_Components/01_Devices/LTU]
    AD-MR-AD1  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    AD-VL-AD  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    AD-MASTER-AD1  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    Lbl-LTU  ia.display.label
    Lbl-HTL  ia.display.label
    DI-HTR-HLCO  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-HTR-HiLevel  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-HTR-OPL  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-HTR-LoLo  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-LTR-HLCO  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-LTR-HiLevel  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-LTR-OPL  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-LTR-LoLo  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-HPR-LoLo  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
```

</details>

## Bindings

22 bindings: expr 21, expr-struct 1.

<details>
<summary>All 22 bindings, grouped by component</summary>

**`(view)`**

- `custom.hsdPax`: expression

```js
case(toStr(coalesce(try(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure' + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure' + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure' + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure' + '/DIn.Enabled')), false), false), 'DIn', ''), '')
```


**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

**`root/Canvas`**

- `props.style.transform`: structured expression (expr-struct), then script transform

```js
contentHeight: 782
contentWidth: 1524
contentX: 24
contentY: 0
defaultViewHeight: {view.props.defaultSize.height}
defaultViewWidth: {view.props.defaultSize.width}
primaryViewHeight: {page.props.dimensions.primaryView.height}
primaryViewWidth: {page.props.dimensions.primaryView.width}
scale: {view.params.Scale}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.Scale.cssTransform(value)
```


**`root/Canvas/HTR`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Tanks/HTR"
```


**`root/Canvas/HPR`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Tanks/HPR"
```


**`root/Canvas/LTR`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Tanks/LTR"
```


**`root/Canvas/HTLR-Pump 2`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Pumps/HTLR-Pump 2"
```


**`root/Canvas/LTRL-Pump 1`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Pumps/LTLR-Pump 1"
```


**`root/Canvas/LTRL-Pump 2`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Pumps/LTLR-Pump 2"
```


**`root/Canvas/HTLR-Pump 1`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Pumps/HTLR-Pump 1"
```


**`root/Canvas/COMP1`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Compressors/COMP 1"
```


**`root/Canvas/COMP7`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Compressors/COMP 7"
```


**`root/Canvas/COMP6`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Compressors/COMP 6"
```


**`root/Canvas/COMP4`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Compressors/COMP 4"
```


**`root/Canvas/COMP5`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Compressors/COMP 5"
```


**`root/Canvas/MAIN LIQ SV`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Valves/Main Liq SV"
```


**`root/Canvas/HSS-PT2`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Sensors/HSS-Pumps Pressure"
```


**`root/Canvas/HSS-PT3`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Sensors/HSL-Pumps Pressure"
```


**`root/Canvas/HSS-PT4`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Sensors/LSL-Pumps Pressure"
```


**`root/Canvas/HSS-PT5`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Sensors/LSS-Pumps Pressure"
```


**`root/Canvas/Condensor Nav_0`**

- `props.params.label`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure/AIn/Val')), false), false), coalesce(try(numberFormat(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure/AIn/Val'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure/AIn/Val.EngUnit'), ''), ''), null), '—'), '—')
```

</details>

## Event Scripts And Handlers

- **`root/Canvas/HSS-SuctionSP`** `component.onActionPerformed`, script action, scope `G`

```python
tagPath = '[default]Boars_Head/GrovePort/Machine Room/Sequences/HSS'
title = 'High Stage Suction'
Navigation.Faceplate.openFaceplate('seq-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/SuctionSequence', False, title, 820, 700,
    {'title': title})
```

- **`root/Canvas/LSS-SuctionSP`** `component.onActionPerformed`, script action, scope `G`

```python
tagPath = '[default]Boars_Head/GrovePort/Machine Room/Sequences/LSS'
title = 'Low Stage Suction'
Navigation.Faceplate.openFaceplate('seq-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/SuctionSequence', False, title, 820, 700,
    {'title': title})
```

- **`root/Canvas/RuptureDisks`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.navigate(page='/rupture-disks')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Scale.cssTransform](../../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Embeds** (9): [00\_Pages/Groveport/Utility/OverviewStatusTile](../../utility/overviewstatustile.md), [02\_Components/00\_Controls/NavButton](../../../../02-components/00-controls/navbutton.md), [02\_Components/01\_Devices/Compressor](../../../../02-components/01-devices/compressor.md), [02\_Components/01\_Devices/LTU](../../../../02-components/01-devices/ltu.md), [02\_Components/01\_Devices/Pump](../../../../02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](../../../../02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](../../../../02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](../../../../02-components/01-devices/tank.md), [02\_Components/02\_Widgets/Safetys](../../../../02-components/02-widgets/safetys.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `faceplate-cmd-btn` | 3 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]Boars_Head/GrovePort/Machine Room/Sequences/HSS`
- `[default]Boars_Head/GrovePort/Machine Room/Sequences/LSS`

Member paths appended to a base path in expressions (relative):

<details>
<summary>24 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Compressors/COMP 1`, `/Compressors/COMP 4`, `/Compressors/COMP 5`, `/Compressors/COMP 6`, `/Compressors/COMP 7`, `/DIn.Enabled`, `/Pumps/HTLR-Pump 1`, `/Pumps/HTLR-Pump 2`, `/Pumps/LTLR-Pump 1`, `/Pumps/LTLR-Pump 2`, `/Sensors/HSD-Discharge Pressure`, `/Sensors/HSD-Discharge Pressure/AIn/Val`, `/Sensors/HSD-Discharge Pressure/AIn/Val.EngUnit`, `/Sensors/HSL-Pumps Pressure`, `/Sensors/HSS-Pumps Pressure`, `/Sensors/LSL-Pumps Pressure`, `/Sensors/LSS-Pumps Pressure`, `/Tanks/HPR`, `/Tanks/HTR`, `/Tanks/LTR`, `/Valves/Main Liq SV`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
