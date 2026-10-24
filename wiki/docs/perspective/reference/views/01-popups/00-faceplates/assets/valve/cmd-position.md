---
title: "Cmd_Position"
sidebar_label: "Cmd_Position"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position (Asset (embedded piece)): 4 components, 16 bindings, 2 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position", "Cmd_Position"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Valve &gt; Cmd\_Position |
| Root | `ia.container.flex`, height 56, width 520 |
| Size | 4 components, 16 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
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

Component types: ia.input.button x2, ia.container.flex x1, ia.input.numeric-entry-field x1.

```text
root  ia.container.flex  [2 bindings]
  PositionEntry  ia.input.numeric-entry-field  [4 bindings]
  BtnApply  ia.input.button  [3 bindings; 1 event]
  BtnReset  ia.input.button  [3 bindings; 1 event]
```

## Bindings

16 bindings: expr 14, expr-struct 2.

<details>
<summary>All 16 bindings, grouped by component</summary>

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

**`root/PositionEntry`**

- `props.enabled`: expression

```js
!{view.custom.roCommand}
```


- `props.value`: expression

```js
if({view.params.tagPath} = '', 0, coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Cmd_Position/Value')), null, tag({view.params.tagPath} + '/Cmd_Position/Value')), null), 0))
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/BtnApply`**

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

- **`root/BtnApply`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return  # security-tiers
base = self.view.params.tagPath
if not base:
    return
val = self.getSibling('PositionEntry').props.value
paths = [base + '/Cmd_Position/Value']
vals = [float(val) if val is not None else 0.0]
system.tag.writeBlocking(paths, vals)
```

- **`root/BtnReset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return  # security-tiers
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Valve/OCmd_Reset']
vals = [True]
system.tag.writeBlocking(paths, vals)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./controls.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `Fonts/Value` | 1 | style class |
| `faceplate-cmd-btn` | 2 | style class |
| `faceplate-cmd-row` | 1 | stylesheet |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cmd_Position/Value`, `/DIn.Enabled`, `/Valve/OCmd_Reset`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
