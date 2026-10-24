---
title: "IconHeader"
sidebar_label: "IconHeader"
description: "Perspective view 03_Elements/01_Status/IconHeader (Element (small reusable part)): 10 components, 13 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/IconHeader", "IconHeader"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/IconHeader`.

| | |
|---|---|
| View path | `03_Elements/01_Status/IconHeader` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/IconHeader/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; IconHeader |
| Root | `ia.container.flex`, height 20, width 20 |
| Size | 10 components, 13 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-28T21:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `statusPath` | `""` | input |
| `hide` | `""` | input |
| `justify` | `"center"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.view x9, ia.container.flex x1.

```text
root  ia.container.flex  [3 bindings]
  CommLoss  ia.display.view  [1 binding; view: 03_Elements/01_Status/NotificationIcons/CommLoss]
  OutOfService  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/OutOfService]
  Interlock  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/Interlock]
  Maintenance  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/Maintenance]
  Hand  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/Hand]
  Operator  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/Operator]
  Program  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/Program]
  Override  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/Override]
  NoMode  ia.display.view  [1 binding; view: 03_Elements/01_Status/Icons/NoMode]
```

## Bindings

13 bindings: expr 11, expr-struct 2.

<details>
<summary>All 13 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

- `props.justify`: expression

```js
coalesce({view.params.justify}, 'center')
```


**`root/CommLoss`**

- `position.display`: expression

```js
!(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',CommLoss,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce({view.params.statusPath}, '') != '' && !isGood(tag({view.params.statusPath}))))
```


**`root/OutOfService`**

- `position.display`: expression

```js
!(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',OutOfService,') >= 0) && (!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
```


**`root/Interlock`**

- `position.display`: expression

```js
!(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',Interlock,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce(try(isGood(tag({view.params.tagPath} + '/Intlk/Sts_IntlkOK')) && !toBoolean(tag({view.params.tagPath} + '/Intlk/Sts_IntlkOK')), false), false)))
```


**`root/Maintenance`**

- `position.display`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false), !(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',Maintenance,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false))), false)
```


**`root/Hand`**

- `position.display`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Motor/Sts_Hand')), false), false), !(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',Hand,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/Motor/Sts_Hand')), false), false))), false)
```


**`root/Operator`**

- `position.display`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false), !(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',Operator,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false))), false)
```


**`root/Program`**

- `position.display`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false), !(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',Program,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false))), false)
```


**`root/Override`**

- `position.display`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Motor/Sts_Ovrd')), false), false), !(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',Override,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/Motor/Sts_Ovrd')), false), false))), false)
```


**`root/NoMode`**

- `position.display`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_NoMode')), false), false), !(indexOf(',' + replace(coalesce({view.params.hide}, ''), ' ', '') + ',', ',NoMode,') >= 0) && (!(!coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true)) && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_NoMode')), false), false))), false)
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (9): [03\_Elements/01\_Status/Icons/Hand](./icons/hand.md), [03\_Elements/01\_Status/Icons/Interlock](./icons/interlock.md), [03\_Elements/01\_Status/Icons/Maintenance](./icons/maintenance.md), [03\_Elements/01\_Status/Icons/NoMode](./icons/nomode.md), [03\_Elements/01\_Status/Icons/Operator](./icons/operator.md), [03\_Elements/01\_Status/Icons/OutOfService](./icons/outofservice.md), [03\_Elements/01\_Status/Icons/Override](./icons/override.md), [03\_Elements/01\_Status/Icons/Program](./icons/program.md), [03\_Elements/01\_Status/NotificationIcons/CommLoss](./notificationicons/commloss.md)

**Embedded in** (9): [02\_Components/01\_Devices/Compressor](../../02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](../../02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](../../02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](../../02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](../../02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Pump](../../02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](../../02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](../../02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](../../02-components/01-devices/tank.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `icon-header` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.Enabled`, `.TypeId`, `/AIn.Enabled`, `/AIn/Sts_Maint`, `/AIn/Sts_NoMode`, `/AIn/Sts_Oper`, `/AIn/Sts_Prog`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Intlk/Sts_IntlkOK`, `/Motor/Sts_Hand`, `/Motor/Sts_Ovrd`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
