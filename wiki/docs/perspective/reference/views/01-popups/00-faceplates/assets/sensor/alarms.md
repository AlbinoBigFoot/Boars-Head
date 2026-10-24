---
title: "Alarms"
sidebar_label: "Alarms"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Sensor/Alarms (Asset (embedded piece)): 27 components, 35 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Sensor/Alarms", "Alarms"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Sensor/Alarms`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Sensor/Alarms` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Sensor/Alarms/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Sensor &gt; Alarms |
| Root | `ia.container.flex`, height 360, width 400 |
| Size | 27 components, 35 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-24T00:00:00Z by the Designer |

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

## Component Tree

Component types: ia.display.label x16, ia.container.flex x9, ia.input.button x1, ia.display.view x1.

<details>
<summary>Component tree (27 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  AlarmBits  ia.container.flex
    Title  ia.display.label
    Body  ia.container.flex
      Chips  ia.container.flex
        Fail  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [5 bindings]
          Priority  ia.display.label
        HiHi  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [5 bindings]
          Priority  ia.display.label
        Hi  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [5 bindings]
          Priority  ia.display.label
        Lo  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [5 bindings]
          Priority  ia.display.label
        LoLo  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [5 bindings]
          Priority  ia.display.label
      BtnAckAll  ia.input.button  [3 bindings; 1 event]
  SharedAlarms  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Alarms]
```

</details>

## Bindings

35 bindings: expr 34, property 1.

<details>
<summary>All 35 bindings, grouped by component</summary>

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


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/AlarmBits/Body/Chips/Fail/State`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), if({view.params.tagPath} = '', '—', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), 'Active', 'Normal')), '—')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'), '/AIn/Sts_Fail value-bad')
```


- `props.style.padding`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), '0px 6px', '0px'), '0px')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), 'var(--alarm-high)', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), 'var(--alarm-row-fg-dark)', ''), 'var(--neutral-60)')
```


**`root/AlarmBits/Body/Chips/HiHi/State`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), if({view.params.tagPath} = '', '—', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), 'Active', 'Normal')), '—')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'), '/AIn/Sts_HiHi value-bad')
```


- `props.style.padding`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), '0px 6px', '0px'), '0px')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), 'var(--alarm-high)', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), 'var(--alarm-row-fg-dark)', ''), 'var(--neutral-60)')
```


**`root/AlarmBits/Body/Chips/Hi/State`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), if({view.params.tagPath} = '', '—', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), 'Active', 'Normal')), '—')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'), '/AIn/Sts_Hi value-bad')
```


- `props.style.padding`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), '0px 6px', '0px'), '0px')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), 'var(--alarm-medium)', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), 'var(--alarm-row-fg-dark)', ''), 'var(--neutral-60)')
```


**`root/AlarmBits/Body/Chips/Lo/State`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), if({view.params.tagPath} = '', '—', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), 'Active', 'Normal')), '—')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'), '/AIn/Sts_Lo value-bad')
```


- `props.style.padding`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), '0px 6px', '0px'), '0px')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), 'var(--alarm-medium)', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), 'var(--alarm-row-fg-dark)', ''), 'var(--neutral-60)')
```


**`root/AlarmBits/Body/Chips/LoLo/State`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), if({view.params.tagPath} = '', '—', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), 'Active', 'Normal')), '—')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'), '/AIn/Sts_LoLo value-bad')
```


- `props.style.padding`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), '0px 6px', '0px'), '0px')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), 'var(--alarm-high)', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), 'var(--alarm-row-fg-dark)', ''), 'var(--neutral-60)')
```


**`root/AlarmBits/Body/BtnAckAll`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '')) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/SharedAlarms`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

</details>

## Event Scripts And Handlers

- **`root/AlarmBits/Body/BtnAckAll`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.writeTag(base + '/' + str(self.view.custom.pax) + '/OCmd_Reset', True)
user = ''
try:
    user = str(self.session.props.auth.user.userName or '')
except:
    pass
try:
    shared.Alarms.acknowledgeForTag(base, user, 'Faceplate Ack / Reset')
except:
    system.util.getLogger('SensorAlarms').warn('Ignition alarm ack failed for %s' % base)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Alarms](../alarms.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 12 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `faceplate-fault-chip` | 5 | style class |
| `faceplate-fault-chips` | 1 | stylesheet |
| `faceplate-fault-code` | 10 | style class |
| `faceplate-fault-state` | 5 | stylesheet |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |
| `faceplate-fault-active` | bound | stylesheet |
| `faceplate-fault-ok` | bound | stylesheet |
| `value-bad` | bound | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AIn/Sts_Fail`, `/AIn/Sts_Hi`, `/AIn/Sts_HiHi`, `/AIn/Sts_Lo`, `/AIn/Sts_LoLo`, `/AInRef.Enabled`, `/DIn.Enabled`, `/OCmd_Reset`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
