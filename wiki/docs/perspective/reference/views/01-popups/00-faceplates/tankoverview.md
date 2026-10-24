---
title: "TankOverview"
sidebar_label: "TankOverview"
description: "Perspective view 01_Popups/00_Faceplates/TankOverview (Popup / faceplate): 17 components, 35 bindings, 7 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/TankOverview", "TankOverview"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/TankOverview`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/TankOverview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/TankOverview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; TankOverview |
| Root | `ia.container.flex`, height 760, width 1100 |
| Size | 17 components, 35 bindings, 7 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-24T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `popupId` | `""` | input |
| `tagPath` | `""` | input |
| `title` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `selected` | `"Overview"` | |
| `ok` | `null` | bound (expr) |
| `lvl` | `null` | bound (expr) |
| `sHH` | `null` | bound (expr) |
| `sH` | `null` | bound (expr) |
| `sL` | `null` | bound (expr) |
| `sLL` | `null` | bound (expr) |
| `sFail` | `null` | bound (expr) |
| `tone` | `null` | bound (expr) |
| `state` | `null` | bound (expr) |
| `hasPumps` | `null` | bound (expr) |

## Component Tree

Component types: ia.input.button x6, ia.container.flex x5, ia.display.label x4, ia.display.icon x1, ia.display.view x1.

<details>
<summary>Component tree (17 components)</summary>

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
      Overview  ia.input.button  [2 bindings; 1 event]
      Configuration  ia.input.button  [2 bindings; 1 event]
      Interlocks  ia.input.button  [3 bindings; 1 event]
      Trend  ia.input.button  [2 bindings; 1 event]
      Alarm Configuration  ia.input.button  [2 bindings; 1 event]
      Alarms  ia.input.button  [2 bindings; 1 event]
    Body  ia.container.flex
      EmbeddedView  ia.display.view  [2 bindings; view: (bound)]
```

</details>

## Bindings

35 bindings: expr 28, property 7.

<details>
<summary>All 35 bindings, grouped by component</summary>

**`(view)`**

- `custom.ok`: expression

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val')), false), false)
```


- `custom.lvl`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/LvlAIn/Val')), false), false), toFloat(tag({view.params.tagPath} + '/LvlAIn/Val')), null)
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


- `custom.hasPumps`: expression

```js
lastIndexOf({view.params.tagPath}, '/Tanks/') >= 0 && coalesce(try(isGood(tag(substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1.TypeId')), false), false)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/Header/Title`**

- `props.text`: expression

```js
if(coalesce({view.params.title}, '') != '', {view.params.title}, substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) + ' Tank'
```


**`root/Header/Sub`**

- `props.text`: expression

```js
''
```


**`root/Header/State`**

- `props.text`: expression

```js
'Level ' + {view.custom.state}
```


- `props.style.classes`: expression

```js
'fp-pill fp-tone-' + case({view.custom.tone}, 'ok', 'ok', 'warn', 'warn', 'alarm', 'alarm', 'muted')
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
{view.params.tagPath} != '' && !coalesce({view.custom.ok}, false)
```


**`root/Content/Tabs/Overview`**

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

**`root/Content/Tabs/Interlocks`**

- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.text`: property `this.meta.name`

- `props.style.display`: expression

```js
if(coalesce({view.custom.hasPumps}, false), 'flex', 'none')
```


**`root/Content/Tabs/Trend`**

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

**`root/Content/Body/EmbeddedView`**

- `props.path`: expression

```js
case({view.custom.selected}, 'Overview', '01_Popups/00_Faceplates/_Assets/TankOverview/Overview', 'Configuration', '01_Popups/00_Faceplates/_Assets/Tank/Configuration', 'Interlocks', '01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks', 'Trend', '01_Popups/00_Faceplates/_Assets/Trend', 'Alarm Configuration', '01_Popups/00_Faceplates/_Assets/AlarmConfiguration', 'Alarms', '01_Popups/00_Faceplates/_Assets/Alarms', '01_Popups/00_Faceplates/_Assets/TankOverview/Overview')
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

</details>

## Event Scripts And Handlers

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
pid = str(self.view.params.popupId or '').strip()
if pid:
    system.perspective.closePopup(pid)
```

- **`root/Content/Tabs/Overview`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Configuration`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Interlocks`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Trend`** `component.onActionPerformed`, script action, scope `G`

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

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Bound embeds** (view path set by a binding): `root/Content/Body/EmbeddedView`

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./assets/alarmconfiguration.md), [01\_Popups/00\_Faceplates/\_Assets/Alarms](./assets/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Interlocks](./assets/tankoverview/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](./assets/tankoverview/overview.md), [01\_Popups/00\_Faceplates/\_Assets/Trend](./assets/trend.md)

**Opened or named by** (1): [02\_Components/01\_Devices/Tank](../../02-components/01-devices/tank.md)

**Named in project scripts**: [Navigation.Faceplate](../../../../../scripting/reference/modules/navigation-faceplate.md)

## Style Classes

<details>
<summary>19 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 1 | style class |
| `bg-component` | 1 | stylesheet |
| `bg-header` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `container-icon` | 1 | stylesheet |
| `faceplate` | 1 | stylesheet |
| `faceplate-body` | 1 | stylesheet |
| `faceplate-buttons-6` | 1 | stylesheet |
| `faceplate-close` | 1 | stylesheet |
| `faceplate-content` | 1 | stylesheet |
| `faceplate-header` | 1 | stylesheet |
| `faceplate-tabs-vertical` | 3 | stylesheet |
| `faceplate-title` | 1 | style class |
| `fp-pill` | 2 | style class |
| `fp-title-sub` | 1 | style class |
| `faceplate-button` | bound | stylesheet |
| `faceplate-button-selected` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/LvlAIn/Sts_Fail`, `/LvlAIn/Sts_Hi`, `/LvlAIn/Sts_HiHi`, `/LvlAIn/Sts_Lo`, `/LvlAIn/Sts_LoLo`, `/LvlAIn/Val`, `/Pumps/`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
