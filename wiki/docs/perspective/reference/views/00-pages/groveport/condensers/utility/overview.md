---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Condensers/Utility/Overview (Page): 26 components, 13 bindings, 3 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Condensers/Utility/Overview", "Overview", "/condensers"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Condensers/Utility/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Condensers/Utility/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Condensers/Utility/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Condensers &gt; Utility &gt; Overview |
| Routes | `/condensers` (Condensers) |
| Root | `ia.container.flex`, height 791, width 1920 |
| Size | 26 components, 13 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T22:04:15Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |
| `tagPath` | `"[default]Boars_Head/GrovePort/Condensers"` | input |

## Component Tree

Component types: ia.display.view x14, ia.display.label x8, ia.container.flex x2, ia.container.coord x1, ia.input.button x1.

<details>
<summary>Component tree (26 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Canvas  ia.container.coord  [1 binding]
    HSD-PT3  ia.display.view  [view: 02_Components/01_Devices/Sensor]
    OAT  ia.container.flex  [1 event]
      Label  ia.display.label
      Value  ia.display.label  [1 binding; 1 event]
    EC-1A  ia.display.view  [1 binding; view: 02_Components/01_Devices/Condenser]
    EC-1B  ia.display.view  [1 binding; view: 02_Components/01_Devices/Condenser]
    MAIN HG CV6  ia.display.view  [1 binding; view: 02_Components/01_Devices/SolenoidValve]
    BACKUP MW CV26  ia.display.view  [1 binding; view: 02_Components/01_Devices/SolenoidValve]
    MAIN MW CV25  ia.display.view  [1 binding; view: 02_Components/01_Devices/SolenoidValve]
    CSV  ia.display.view  [1 binding; view: 02_Components/01_Devices/Tank]
    DI-RS-LVL-OL2  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-RS-LVL-OL3  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    DI-RS-LLCO2  ia.display.view  [view: 00_Pages/Groveport/Utility/OverviewStatusTile]
    Sump Pump 1  ia.display.view  [1 binding; view: 02_Components/01_Devices/Pump]
    Sump Pump 2  ia.display.view  [1 binding; view: 02_Components/01_Devices/Pump]
    Sump Pump 3  ia.display.view  [1 binding; view: 02_Components/01_Devices/Pump]
    Discharge-SP  ia.input.button  [1 event]
    Lbl-TSR  ia.display.label
    Lbl-TSS  ia.display.label
    Lbl-HPL  ia.display.label
    Lbl-HSD  ia.display.label
    Lbl-CWR  ia.display.label
    Lbl-WATER  ia.display.label
    VesselGeneric  ia.display.view  [view: 02_Components/01_Devices/VesselGeneric]
```

</details>

## Bindings

13 bindings: expr 12, expr-struct 1.

<details>
<summary>All 13 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

**`root/Canvas`**

- `props.style.transform`: structured expression (expr-struct), then script transform

```js
contentHeight: 751
contentWidth: 1703
contentX: 55
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


**`root/Canvas/OAT/Value`**

- `props.text`: expression

```js
if(!isGood(tag('[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp/AIn/Val')),
	'— °F',
	numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp/AIn/Val'), 0), '0.0') + ' °F')
```


**`root/Canvas/EC-1A`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Condensers/EC-1A"
```


**`root/Canvas/EC-1B`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Condensers/EC-1B"
```


**`root/Canvas/MAIN HG CV6`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Valves/Main HG CV6"
```


**`root/Canvas/BACKUP MW CV26`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Valves/Backup MW CV26"
```


**`root/Canvas/MAIN MW CV25`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Valves/Main MW CV25"
```


**`root/Canvas/CSV`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Tanks/CSV"
```


**`root/Canvas/Sump Pump 1`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Pumps/Sump Pump 1"
```


**`root/Canvas/Sump Pump 2`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Pumps/Sump Pump 2"
```


**`root/Canvas/Sump Pump 3`**

- `props.params.tagPath`: expression

```js
{view.params.tagPath} + "/Pumps/Sump Pump 3"
```

</details>

## Event Scripts And Handlers

- **`root/Canvas/OAT`** `dom.onClick`, script action, scope `G`

```python
tagPath = '[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp'
title = 'OUTSIDE AIR TEMP'
params = {'tagPath': tagPath, 'deviceType': 'Sensor', 'webGuiUrl': '', 'showControls': True,
    'showConfiguration': True, 'showInterlocks': False, 'showTrend': True, 'showAlarmConfiguration': True,
    'showAlarms': True, 'title': title}
Navigation.Faceplate.openFaceplate('sensor-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/Faceplate',
    False, title, 560, 640, params)
```

- **`root/Canvas/OAT/Value`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp/AIn/Val')
```

- **`root/Canvas/Discharge-SP`** `component.onActionPerformed`, script action, scope `G`

```python
tagPath = '[default]Boars_Head/GrovePort/Condensers/Sequences/HSD'
title = 'High Stage Discharge'
Navigation.Faceplate.openFaceplate('seq-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/DischargeSequence', False, title, 1180, 740,
    {'title': title})
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Scale.cssTransform](../../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Embeds** (7): [00\_Pages/Groveport/Utility/OverviewStatusTile](../../utility/overviewstatustile.md), [02\_Components/01\_Devices/Condenser](../../../../02-components/01-devices/condenser.md), [02\_Components/01\_Devices/Pump](../../../../02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](../../../../02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](../../../../02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](../../../../02-components/01-devices/tank.md), [02\_Components/01\_Devices/VesselGeneric](../../../../02-components/01-devices/vesselgeneric.md)

**Opened or named by** (1): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `bg-page` | 1 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `faceplate-hover` | 1 | stylesheet |
| `fs-12` | 1 | style class |
| `fs-9` | 1 | style class |
| `fw-600` | 1 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp`
- `[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp/AIn/Val`
- `[default]Boars_Head/GrovePort/Condensers/Sequences/HSD`

Member paths appended to a base path in expressions (relative):

`/Condensers/EC-1A`, `/Condensers/EC-1B`, `/Pumps/Sump Pump 1`, `/Pumps/Sump Pump 2`, `/Pumps/Sump Pump 3`, `/Tanks/CSV`, `/Valves/Backup MW CV26`, `/Valves/Main HG CV6`, `/Valves/Main MW CV25`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
