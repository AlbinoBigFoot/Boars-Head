---
title: "Cmd_MO"
sidebar_label: "Cmd_MO"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO (Asset (embedded piece)): 7 components, 19 bindings, 3 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO", "Cmd_MO"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Valve &gt; Cmd\_MO |
| Root | `ia.container.flex`, height 48, width 520 |
| Size | 7 components, 19 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-02T19:48:53Z by the Designer |

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

Component types: ia.input.button x3, ia.container.flex x2, ia.display.label x2.

```text
root  ia.container.flex  [2 bindings]
  CmdState  ia.container.flex
    Code  ia.display.label
    State  ia.display.label  [2 bindings]
  BtnOpen  ia.input.button  [4 bindings; 1 event]
  BtnClose  ia.input.button  [4 bindings; 1 event]
  BtnReset  ia.input.button  [3 bindings; 1 event]
```

## Bindings

19 bindings: expr 17, expr-struct 2.

<details>
<summary>All 19 bindings, grouped by component</summary>

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

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
```

waitOnAll: `False`

Transform 1, script:

```python
tagPath = ''
try:
    tagPath = self.view.params.tagPath
except:
    pass
if tagPath is None or str(tagPath).strip() == '':
    tagPath = 'No TagPath: ' + self.view.id.split('@')[0].split('/')[-1]
items = [
    {
        "text": "Ticket Logger",
        "icon": {
            "path": "material/info",
            "color": "--neutral-80",
            "style": {}
        },
        "style": {
            "classes": "bg-component Fonts/Value",
            "height": 24,
            "width": 120
        },
        "type": "message",
        "children": [],
        "link": {"url": "", "target": "self"},
        "method": {"name": "", "params": {}},
        "message": {
            "type": "ticketLog",
            "payload": {
                "tagPath": tagPath,
                "viewName": self.view.id.split('@')[0], 'sender': self.view.id
            },
            "scope": "page"
        }
    }
]
return items
```


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../common-patterns.md#pattern-1).

**`root/CmdState/State`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—',
	if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/Out')), null, tag({view.params.tagPath} + '/Valve/Out')), null),
		try(if(!isGood(tag({view.params.tagPath} + '/Valve/OCmd_Open')), null, tag({view.params.tagPath} + '/Valve/OCmd_Open')), null), false),
		'ON', 'OFF'))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-fault-state',
	if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/Out')), null, tag({view.params.tagPath} + '/Valve/Out')), null),
		try(if(!isGood(tag({view.params.tagPath} + '/Valve/OCmd_Open')), null, tag({view.params.tagPath} + '/Valve/OCmd_Open')), null), false),
		'faceplate-fault-state faceplate-ls-on',
		'faceplate-fault-state faceplate-ls-off'))
```


**`root/BtnOpen`**

- `props.enabled`: expression

```js
(!{view.custom.roCommand}) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-cmd-btn Fonts/Label',
	if(if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/Cfg_HasOpenLS')), null, tag({view.params.tagPath} + '/Valve/Cfg_HasOpenLS')), null), false),
		coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/Inp_OpenLS')), null, tag({view.params.tagPath} + '/Valve/Inp_OpenLS')), null), false),
		coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/OCmd_Open')), null, tag({view.params.tagPath} + '/Valve/OCmd_Open')), null), false)),
		'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label',
		'faceplate-cmd-btn Fonts/Label'))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/BtnClose`**

- `props.enabled`: expression

```js
(!{view.custom.roCommand}) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} = '', 'faceplate-cmd-btn Fonts/Label',
	if(if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/Cfg_HasClosedLS')), null, tag({view.params.tagPath} + '/Valve/Cfg_HasClosedLS')), null), false),
		coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/Inp_ClosedLS')), null, tag({view.params.tagPath} + '/Valve/Inp_ClosedLS')), null), false),
		coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Valve/OCmd_Close')), null, tag({view.params.tagPath} + '/Valve/OCmd_Close')), null), false)),
		'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label',
		'faceplate-cmd-btn Fonts/Label'))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/BtnReset`**

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

</details>

## Event Scripts And Handlers

- **`root/BtnOpen`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.openValve(base, 'MO')
```

- **`root/BtnClose`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.closeValve(base, 'MO')
```

- **`root/BtnReset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.resetValve(base)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./controls.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 4 | style class |
| `faceplate-cmd-btn` | 3 | style class |
| `faceplate-cmd-row` | 1 | stylesheet |
| `faceplate-fault-chip` | 1 | style class |
| `faceplate-fault-code` | 1 | style class |
| `faceplate-fault-state` | 1 | stylesheet |
| `faceplate-ls-off` | 1 | stylesheet |
| `faceplate-cmd-btn-active` | bound | style class |
| `faceplate-ls-on` | bound | stylesheet |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Valve/Cfg_HasClosedLS`, `/Valve/Cfg_HasOpenLS`, `/Valve/Inp_ClosedLS`, `/Valve/Inp_OpenLS`, `/Valve/OCmd_Close`, `/Valve/OCmd_Open`, `/Valve/Out`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
