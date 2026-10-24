---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Boars Head/Machine Room/Overview (Page piece (not routed)): 32 components, 21 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Machine Room/Overview", "Overview"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Machine Room/Overview`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Machine Room/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Machine Room/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Machine Room &gt; Overview |
| Root | `ia.container.flex`, height 791, width 1920 |
| Size | 32 components, 21 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-24T21:00:16Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |
| `tagPath` | `"[default]Boars_Head/GrovePort/Machine Room"` | input |

## Component Tree

Component types: ia.display.view x23, ia.display.label x7, ia.container.flex x1, ia.container.coord x1.

<details>
<summary>Component tree (32 components)</summary>

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
    Condensor Nav_0  ia.display.view  [view: 02_Components/00_Controls/NavButton]
    HSS-PT6  ia.display.view  [1 binding; view: 02_Components/01_Devices/Sensor]
```

</details>

## Bindings

21 bindings: expr 20, expr-struct 1.

<details>
<summary>All 21 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Canvas`**

- `props.style.transform`: structured expression (expr-struct), then script transform

```js
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


**`root/Canvas/HSS-PT6`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Sensors/HSS-Pumps Pressure"
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Scale.cssTransform](../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Embeds** (7): [02\_Components/00\_Controls/NavButton](../../../02-components/00-controls/navbutton.md), [02\_Components/01\_Devices/Compressor](../../../02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Pump](../../../02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](../../../02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](../../../02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](../../../02-components/01-devices/tank.md), [02\_Components/02\_Widgets/Safetys](../../../02-components/02-widgets/safetys.md)

**Named in project scripts**: [Navigation.Nav](../../../../../../scripting/reference/modules/navigation-nav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>17 relative member paths</summary>

`/Compressors/COMP 1`, `/Compressors/COMP 4`, `/Compressors/COMP 5`, `/Compressors/COMP 6`, `/Compressors/COMP 7`, `/Pumps/HTLR-Pump 1`, `/Pumps/HTLR-Pump 2`, `/Pumps/LTLR-Pump 1`, `/Pumps/LTLR-Pump 2`, `/Sensors/HSL-Pumps Pressure`, `/Sensors/HSS-Pumps Pressure`, `/Sensors/LSL-Pumps Pressure`, `/Sensors/LSS-Pumps Pressure`, `/Tanks/HPR`, `/Tanks/HTR`, `/Tanks/LTR`, `/Valves/Main Liq SV`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
