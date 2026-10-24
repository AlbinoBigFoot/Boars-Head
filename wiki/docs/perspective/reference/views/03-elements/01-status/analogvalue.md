---
title: "AnalogValue"
sidebar_label: "AnalogValue"
description: "Perspective view 03_Elements/01_Status/AnalogValue (Element (small reusable part)): 2 components, 10 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/AnalogValue", "AnalogValue"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/AnalogValue`.

| | |
|---|---|
| View path | `03_Elements/01_Status/AnalogValue` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/AnalogValue/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; AnalogValue |
| Root | `ia.container.flex`, height 20, width 80 |
| Size | 2 components, 10 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-24T05:55:37Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `compact` | `false` | input |
| `spacing` | `{"center": true, "data": 0, "engUnit": 30, "textAlign": "center"}` | input |
| `tagPath` | `""` | input |
| `spTagPath` | `""` | input |
| `forceColor` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `effectiveSpPath` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [1 binding]
  Numeric  ia.display.view  [8 bindings; view: 03_Elements/01_Status/_Assets/Numeric]
```

## Bindings

10 bindings: property 6, expr 4.

**`(view)`**

- `custom.effectiveSpPath`: expression

```js
if({view.params.spTagPath} != '',
	{view.params.spTagPath},
	if({view.params.tagPath} = '',
		'',
		if(right({view.params.tagPath}, 6) = '/Value',
			left({view.params.tagPath}, len({view.params.tagPath}) - 6) + '/SP/Value',
			'')))
```


**`root`**

- `props.justify`: expression

```js
if({view.params.spacing.center},
	'center',
	'flex-start')
```


**`root/Numeric`**

- `position.grow`: expression

```js
if({view.params.spacing.center},
	0,
	1)
```


- `props.params.compact`: property `view.params.compact`

- `props.params.spacing.center`: property `view.params.spacing.center`

- `props.params.spacing.data`: property `view.params.spacing.data`

- `props.params.spacing.engUnit`: property `view.params.spacing.engUnit`

- `props.params.tagPath`: expression

```js
{view.params.tagPath}
```


- `props.params.spTagPath`: property `view.custom.effectiveSpPath`

- `props.params.forceColor`: property `view.params.forceColor`

## Related Views

**Embeds** (1): [03\_Elements/01\_Status/\_Assets/Numeric](./assets/numeric.md)

**Embedded in** (8): [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](../../01-popups/00-faceplates/assets/coolingtower/controls.md), [02\_Components/01\_Devices/Condenser](../../02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](../../02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](../../02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/Pump](../../02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](../../02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](../../02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](../../02-components/01-devices/tank.md)

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/SP/Value`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
