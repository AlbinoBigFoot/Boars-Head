---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/CoolingTower/Controls (Asset (embedded piece)): 24 components, 25 bindings, 6 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/CoolingTower/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/CoolingTower/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/CoolingTower/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/CoolingTower/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; CoolingTower &gt; Controls |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 24 components, 25 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:19:43Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |
| `roMode` | `true` | bound (expr) |
| `tipMode` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x8, ia.display.label x8, ia.display.view x4, ia.input.button x4.

<details>
<summary>Component tree (24 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Modes  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/Modes]
  StatusSection  ia.container.flex
    StatusTitle  ia.display.label
    StatusInd  ia.display.view  [1 binding; view: 03_Elements/01_Status/StatusIndicator]
    CmdRow  ia.container.flex
      BtnStart  ia.input.button  [3 bindings; 1 event]
      BtnStop  ia.input.button  [3 bindings; 1 event]
      BtnAuto  ia.input.button  [3 bindings; 1 event]
      BtnManual  ia.input.button  [3 bindings; 1 event]
  KpiSection  ia.container.flex
    KpiTitle  ia.display.label
    Runtime  ia.container.flex
      RuntimeLbl  ia.display.label
      RuntimeVal  ia.display.label  [1 binding; 1 event]
    Starts  ia.container.flex
      StartsLbl  ia.display.label
      StartsVal  ia.display.label  [1 binding; 1 event]
    Temp  ia.container.flex
      TempLbl  ia.display.label
      TempVal  ia.display.view  [1 binding; view: 03_Elements/01_Status/AnalogValue]
    SpdFbk  ia.container.flex
      SpdFbkLbl  ia.display.label
      SpdFbkVal  ia.display.view  [1 binding; view: 03_Elements/01_Status/AnalogValue]
```

</details>

## Bindings

25 bindings: expr 22, expr-struct 2, property 1.

<details>
<summary>All 25 bindings, grouped by component</summary>

**`(view)`**

- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roCommand`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Command'], null), true)
```


- `custom.tipCommand`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roCommand}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Command' + ' (Roles & Permissions)', '')
```


- `custom.roMode`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Mode'], null), true)
```


- `custom.tipMode`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roMode}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Mode' + ' (Roles & Permissions)', '')
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

**`root/Modes`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/StatusSection/StatusInd`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/Status')
```


**`root/StatusSection/CmdRow/BtnStart`**

- `props.enabled`: expression

```js
!{view.custom.roCommand}
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/StatusSection/CmdRow/BtnStop`**

- `props.enabled`: expression

```js
!{view.custom.roCommand}
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/StatusSection/CmdRow/BtnAuto`**

- `props.enabled`: expression

```js
!{view.custom.roMode}
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/StatusSection/CmdRow/BtnManual`**

- `props.enabled`: expression

```js
!{view.custom.roMode}
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/KpiSection/Runtime/RuntimeVal`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/RuntimeHours/Value')), false), false), if({view.params.tagPath} = '', '', numberFormat(toFloat(tag({view.params.tagPath} + '/RuntimeHours/Value')), '#0.0')), '—')
```


**`root/KpiSection/Starts/StartsVal`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/MotorStarts/Value')), false), false), if({view.params.tagPath} = '', '', numberFormat(toFloat(tag({view.params.tagPath} + '/MotorStarts/Value')), '#0')), '—')
```


**`root/KpiSection/Temp/TempVal`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/Temp')
```


**`root/KpiSection/SpdFbk/SpdFbkVal`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/SPD_FBK')
```

</details>

## Event Scripts And Handlers

- **`root/StatusSection/CmdRow/BtnStart`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Cmd_Start/Value']
vals = [True]
system.tag.writeBlocking(paths, vals)
```

- **`root/StatusSection/CmdRow/BtnStop`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Cmd_Stop/Value']
vals = [True]
system.tag.writeBlocking(paths, vals)
```

- **`root/StatusSection/CmdRow/BtnAuto`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Cmd_Auto/Value']
vals = [True]
system.tag.writeBlocking(paths, vals)
```

- **`root/StatusSection/CmdRow/BtnManual`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Cmd_Manual/Value']
vals = [True]
system.tag.writeBlocking(paths, vals)
```

- **`root/KpiSection/Runtime/RuntimeVal`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/RuntimeHours/Value')
```

- **`root/KpiSection/Starts/StartsVal`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/MotorStarts/Value')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (3): [01\_Popups/00\_Faceplates/\_Assets/Modes](../modes.md), [03\_Elements/01\_Status/AnalogValue](../../../../03-elements/01-status/analogvalue.md), [03\_Elements/01\_Status/StatusIndicator](../../../../03-elements/01-status/statusindicator.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 10 | style class |
| `Fonts/Value` | 2 | style class |
| `faceplate-cmd-btn` | 4 | style class |
| `faceplate-cmd-row` | 1 | stylesheet |
| `faceplate-kpi-label` | 4 | style class |
| `faceplate-kpi-row` | 4 | stylesheet |
| `faceplate-section` | 2 | style class |
| `faceplate-section-card` | 2 | style class |
| `faceplate-section-title` | 2 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/Cmd_Auto/Value`, `/Cmd_Manual/Value`, `/Cmd_Start/Value`, `/Cmd_Stop/Value`, `/MotorStarts/Value`, `/RuntimeHours/Value`, `/SPD_FBK`, `/Status`, `/Temp`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
