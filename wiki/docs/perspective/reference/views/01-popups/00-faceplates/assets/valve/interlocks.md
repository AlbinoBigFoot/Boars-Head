---
title: "Interlocks"
sidebar_label: "Interlocks"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Valve/Interlocks (Asset (embedded piece)): 11 components, 26 bindings, 3 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Valve/Interlocks", "Interlocks"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Valve/Interlocks`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Interlocks/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Valve &gt; Interlocks |
| Root | `ia.container.flex`, height 220, width 420 |
| Size | 11 components, 26 bindings, 3 event handlers, 0 change scripts, 3 message handlers |
| Last saved | 2026-07-30T21:00:00Z by the Designer |

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
| `permDevice` | `""` | bound (expr) |
| `roInterlocks` | `true` | bound (expr) |
| `tipInterlocks` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x3, ia.input.button x3, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  DeviceBypass  ia.container.flex
    Title  ia.display.label
    Body  ia.container.flex
      StatusLbl  ia.display.label  [2 bindings]
      BypLbl  ia.display.label  [2 bindings]
      Cmds  ia.container.flex
        BtnEnable  ia.input.button  [4 bindings; 1 event]
        BtnDisable  ia.input.button  [4 bindings; 1 event]
        BtnBypass  ia.input.button  [5 bindings; 1 event]
      OvrdPermIntlk  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField]
```

## Bindings

26 bindings: expr 26.

<details>
<summary>All 26 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Sts_Disabled')), tag({view.params.tagPath} + '/Valve/Sts_Disabled'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Valve/Sts_BypActive')), tag({view.params.tagPath} + '/Valve/Sts_BypActive'), null), null)
```


- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roInterlocks`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Interlocks'], null), true)
```


- `custom.tipInterlocks`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roInterlocks}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Interlocks' + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/DeviceBypass/Body/StatusLbl`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg0}), true), true), '—', if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), false),
		'DISABLED', 'ENABLED')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg0}), true), true), 'Fonts/Value value-bad', 'Fonts/Value')
```


**`root/DeviceBypass/Body/BypLbl`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), '—', if({view.params.tagPath} = '', '',
	if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
		'BYPASS ACTIVE — interlocks skipped',
		'Interlocks in service')))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), 'Fonts/Label value-bad', if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
	'Fonts/Label faceplate-bypass-banner',
	'Fonts/Label'))
```


**`root/DeviceBypass/Body/Cmds/BtnEnable`**

- `props.enabled`: expression

```js
(!{view.custom.roInterlocks}) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), false),
	'faceplate-cmd-btn Fonts/Label',
	'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/DeviceBypass/Body/Cmds/BtnDisable`**

- `props.enabled`: expression

```js
(!{view.custom.roInterlocks}) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), false),
	'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label',
	'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/DeviceBypass/Body/Cmds/BtnBypass`**

- `props.enabled`: expression

```js
(!{view.custom.roInterlocks}) && coalesce({view.custom.pax}, '') = ''
```


- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), '—', if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
	'Bypass On',
	'Bypass'))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(isNull({view.custom.qg1}), true), true), 'faceplate-cmd-btn value-bad', if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
	'faceplate-cmd-btn faceplate-cmd-btn-bypass Fonts/Label',
	'faceplate-cmd-btn Fonts/Label'))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/DeviceBypass/Body/OvrdPermIntlk`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/Valve/Cfg_OvrdPermIntlk')
```

</details>

## Event Scripts And Handlers

- **`root/DeviceBypass/Body/Cmds/BtnEnable`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roInterlocks:
    return
base = self.view.params.tagPath
if not base:
    return
shared.Alerts.confirmApplyWrite(
    label='Enable device',
    tagPath=base + '/Valve/MCmd_Enable',
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0], 'skipWrite': True},
)
```

- **`root/DeviceBypass/Body/Cmds/BtnDisable`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roInterlocks:
    return
base = self.view.params.tagPath
if not base:
    return
shared.Alerts.confirmApplyWrite(
    label='Disable device',
    tagPath=base + '/Valve/MCmd_Disable',
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0], 'skipWrite': True},
)
```

- **`root/DeviceBypass/Body/Cmds/BtnBypass`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roInterlocks:
    return
base = self.view.params.tagPath
if not base:
    return
on = False
try:
    on = bool(shared.ValveCommands.bypassActive(base))
except:
    pass
shared.Alerts.confirmApplyWrite(
    label='Clear interlock bypass' if on else 'Bypass interlocks',
    tagPath=base + '/Valve/Sts_BypActive',
    newValue=not on,
    oldValue=on,
    extraPayload={'viewName': self.view.id.split('@')[0], 'skipWrite': True},
)
```

- **`root`** message handler `cancel` (scope: page)

```python
pass
```

- **`root`** message handler `writeValue` (scope: page)

```python
path = payload.get('tagPath') if payload else None
base = self.view.params.tagPath or ''
if not path or not base:
    return
leaf = str(path).rstrip('/').split('/')
cmd = leaf[-2] if len(leaf) >= 2 and leaf[-1] == 'Value' else leaf[-1]
if cmd == 'Cmd_Enable':
    shared.ValveCommands.enableDevice(base)
elif cmd == 'Cmd_Disable':
    shared.ValveCommands.disableDevice(base)
elif cmd in ('Cmd_Bypass', 'Sts_BypActive'):
    val = payload.get('value') if payload else None
    shared.ValveCommands.bypassDevice(base, val)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.ValveCommands.bypassActive](../../../../../../../scripting/reference/modules/shared-valvecommands.md), [shared.ValveCommands.bypassDevice](../../../../../../../scripting/reference/modules/shared-valvecommands.md), [shared.ValveCommands.disableDevice](../../../../../../../scripting/reference/modules/shared-valvecommands.md), [shared.ValveCommands.enableDevice](../../../../../../../scripting/reference/modules/shared-valvecommands.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](../configuration/configfield.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 5 | style class |
| `Fonts/Value` | 1 | style class |
| `faceplate-cmd-btn` | 3 | style class |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |
| `faceplate-bypass-banner` | bound | style class |
| `faceplate-cmd-btn-active` | bound | style class |
| `faceplate-cmd-btn-bypass` | bound | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Valve/Cfg_OvrdPermIntlk`, `/Valve/MCmd_Disable`, `/Valve/MCmd_Enable`, `/Valve/Sts_BypActive`, `/Valve/Sts_Disabled`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
