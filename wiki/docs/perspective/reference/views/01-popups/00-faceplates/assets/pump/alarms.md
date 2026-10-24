---
title: "Alarms"
sidebar_label: "Alarms"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Pump/Alarms (Asset (embedded piece)): 19 components, 22 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Pump/Alarms", "Alarms"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Pump/Alarms`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Pump/Alarms` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Pump/Alarms/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Pump &gt; Alarms |
| Root | `ia.container.flex`, height 360, width 480 |
| Size | 19 components, 22 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:19:43Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `qg0` | `null` | bound (expr) |
| `qg1` | `null` | bound (expr) |
| `qg2` | `null` | bound (expr) |
| `qg3` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x9, ia.container.flex x8, ia.input.button x1, ia.display.view x1.

<details>
<summary>Component tree (19 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  AlarmBits  ia.container.flex
    Title  ia.display.label
    Body  ia.container.flex
      Chips  ia.container.flex
        FailToStart  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [2 bindings]
        FailToStop  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [2 bindings]
        IOFault  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [2 bindings]
        IntlkTrip  ia.container.flex
          Code  ia.display.label
          State  ia.display.label  [2 bindings]
      BtnAckAll  ia.input.button  [3 bindings; 1 event]
  SharedAlarms  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Alarms]
```

</details>

## Bindings

22 bindings: expr 21, property 1.

<details>
<summary>All 22 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_FailToStart')), tag({view.params.tagPath} + '/Motor/Alm_FailToStart'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_FailToStop')), tag({view.params.tagPath} + '/Motor/Alm_FailToStop'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_IOFault')), tag({view.params.tagPath} + '/Motor/Alm_IOFault'), null), null)
```


- `custom.qg3`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Motor/Alm_IntlkTrip')), tag({view.params.tagPath} + '/Motor/Alm_IntlkTrip'), null), null)
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


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/AlarmBits/Body/Chips/FailToStart/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg0}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg0}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/AlarmBits/Body/Chips/FailToStop/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/AlarmBits/Body/Chips/IOFault/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg2}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg2}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/AlarmBits/Body/Chips/IntlkTrip/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg3}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false),
		'ACTIVE', 'OK')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg3}), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false),
		'faceplate-fault-state faceplate-fault-active',
		'faceplate-fault-state faceplate-fault-ok')))
```


**`root/AlarmBits/Body/BtnAckAll`**

- `props.enabled`: expression

```js
(!{view.custom.roCommand}) && coalesce({view.custom.pax}, '') = ''
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
def _r(p):
    try:
        c = system.tag.getConfiguration(p, False)[0]
        s = c.get('sourceTagPath')
        return str(s) if s else p
    except:
        return p
paths = [base + '/' + n + '/Value' for n in ('Ack_FailToStart','Ack_FailToStop','Ack_IOFault','Ack_IntlkTrip','OCmd_ResetAckAll')]
vals = [True] * len(paths)
system.tag.writeBlocking([_r(p) for p in paths], vals)
user = ''
try:
    user = str(self.session.props.auth.user.userName or '')
except:
    pass
try:
    shared.Alarms.acknowledgeForTag(base, user, 'Faceplate Ack / Reset')
except:
# ... 6 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Alarms](../alarms.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 6 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `faceplate-fault-chip` | 4 | style class |
| `faceplate-fault-chips` | 1 | stylesheet |
| `faceplate-fault-code` | 4 | style class |
| `faceplate-fault-ok` | 4 | stylesheet |
| `faceplate-fault-state` | 4 | stylesheet |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |
| `faceplate-fault-active` | bound | stylesheet |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Motor/Alm_FailToStart`, `/Motor/Alm_FailToStop`, `/Motor/Alm_IOFault`, `/Motor/Alm_IntlkTrip`, `/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
