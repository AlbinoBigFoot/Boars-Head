---
title: "AlarmHeader"
sidebar_label: "AlarmHeader"
description: "Perspective view 03_Elements/01_Status/AlarmHeader (Element (small reusable part)): 2 components, 8 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/AlarmHeader", "AlarmHeader"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/AlarmHeader`.

| | |
|---|---|
| View path | `03_Elements/01_Status/AlarmHeader` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/AlarmHeader/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; AlarmHeader |
| Root | `ia.container.flex`, height 20, width 20 |
| Size | 2 components, 8 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-28T21:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `active` | `false` | bound (tag) |
| `priority` | `-1` | bound (tag) |
| `ackPriority` | `-1` | bound (tag) |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Badge  ia.display.view  [3 bindings; view: (bound)]
```

## Bindings

8 bindings: tag 3, expr 3, expr-struct 2.

**`(view)`**

- `custom.active`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}/_Alarms/_Active`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}), false, {value})
```


- `custom.priority`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}/_Alarms/_ActiveHighPriority`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}), -1, {value})
```


- `custom.ackPriority`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}/_Alarms/_AckHighPriority`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}), -1, {value})
```


**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/Badge`**

- `meta.visible`: expression

```js
coalesce({view.custom.active}, false)
```


- `props.path`: expression

```js
case({view.custom.priority}, 4, '03_Elements/01_Status/NotificationIcons/Alarms/Critical', 3, '03_Elements/01_Status/NotificationIcons/Alarms/High', 2, '03_Elements/01_Status/NotificationIcons/Alarms/Medium', 1, '03_Elements/01_Status/NotificationIcons/Alarms/Low', '03_Elements/01_Status/NotificationIcons/Blank')
```


- `props.params.unack`: expression

```js
coalesce({view.custom.active}, false) && coalesce({view.custom.ackPriority}, -1) != coalesce({view.custom.priority}, -1)
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Bound embeds** (view path set by a binding): `root/Badge`

**Opens or names** (popups, scripts, expressions): [03\_Elements/01\_Status/NotificationIcons/Alarms/Critical](./notificationicons/alarms/critical.md), [03\_Elements/01\_Status/NotificationIcons/Alarms/High](./notificationicons/alarms/high.md), [03\_Elements/01\_Status/NotificationIcons/Alarms/Low](./notificationicons/alarms/low.md), [03\_Elements/01\_Status/NotificationIcons/Alarms/Medium](./notificationicons/alarms/medium.md), [03\_Elements/01\_Status/NotificationIcons/Blank](./notificationicons/blank.md)

**Embedded in** (9): [02\_Components/01\_Devices/Compressor](../../02-components/01-devices/compressor.md), [02\_Components/01\_Devices/Condenser](../../02-components/01-devices/condenser.md), [02\_Components/01\_Devices/CoolingTower](../../02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](../../02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](../../02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Pump](../../02-components/01-devices/pump.md), [02\_Components/01\_Devices/Sensor](../../02-components/01-devices/sensor.md), [02\_Components/01\_Devices/SolenoidValve](../../02-components/01-devices/solenoidvalve.md), [02\_Components/01\_Devices/Tank](../../02-components/01-devices/tank.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `alarm-header` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}/_Alarms/_AckHighPriority`
- `{tagPath}/_Alarms/_Active`
- `{tagPath}/_Alarms/_ActiveHighPriority`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
