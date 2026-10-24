---
title: "Modes"
sidebar_label: "Modes"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Modes (Asset (embedded piece)): 23 components, 30 bindings, 6 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Modes", "Modes"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Modes`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Modes` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Modes/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Modes |
| Root | `ia.container.flex`, height 90, width 520 |
| Size | 23 components, 30 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-02T02:30:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `deviceType` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `qg0` | `null` | bound (expr) |
| `qg1` | `null` | bound (expr) |
| `qg2` | `null` | bound (expr) |
| `qg3` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roMode` | `true` | bound (expr) |
| `tipMode` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x9, ia.display.label x8, ia.display.view x6.

<details>
<summary>Component tree (23 components)</summary>

```text
root  ia.container.flex  [3 bindings]
  ModeHeader  ia.container.flex
    ModeTitle  ia.display.label
    ModeCurrent  ia.display.label  [1 binding]
  ModeRow  ia.container.flex
    ModeOper  ia.container.flex  [3 bindings; 1 event]
      Icon  ia.display.view  [view: 03_Elements/01_Status/Icons/Operator]
      Label  ia.display.label
    ModeProg  ia.container.flex  [3 bindings; 1 event]
      Icon  ia.display.view  [view: 03_Elements/01_Status/Icons/Program]
      Label  ia.display.label
    ModeMaint  ia.container.flex  [3 bindings; 1 event]
      Icon  ia.display.view  [view: 03_Elements/01_Status/Icons/Maintenance]
      Label  ia.display.label
    ModeRemote  ia.container.flex  [3 bindings; 1 event]
      Icon  ia.display.view  [view: 03_Elements/01_Status/Icons/Remote]
      Label  ia.display.label
    ModeAuto  ia.container.flex  [3 bindings; 1 event]
      Icon  ia.display.view  [view: 03_Elements/01_Status/Icons/Auto]
      Label  ia.display.label
    ModeManual  ia.container.flex  [3 bindings; 1 event]
      Icon  ia.display.view  [view: 03_Elements/01_Status/Icons/Hand]
      Label  ia.display.label
```

</details>

## Bindings

30 bindings: expr 28, expr-struct 2.

<details>
<summary>All 30 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../common-patterns.md#pattern-6).

- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), tag({view.params.tagPath} + '/Comp/CP_Mode'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/' + {view.custom.pax} + '/Sts_Oper')), tag({view.params.tagPath} + '/' + {view.custom.pax} + '/Sts_Oper'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/' + {view.custom.pax} + '/Sts_Prog')), tag({view.params.tagPath} + '/' + {view.custom.pax} + '/Sts_Prog'), null), null)
```


- `custom.qg3`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/' + {view.custom.pax} + '/Sts_Maint')), tag({view.params.tagPath} + '/' + {view.custom.pax} + '/Sts_Maint'), null), null)
```


- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../common-patterns.md#pattern-8).

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


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

- `position.display`: expression

```js
({view.params.deviceType} = 'Pump' || {view.params.deviceType} = 'Valve' || {view.params.deviceType} = 'ExhaustFan' || {view.params.deviceType} = 'CoolingTower') || ({view.params.deviceType} = 'Compressor')
```


**`root/ModeHeader/ModeCurrent`**

- `props.text`: expression

```js
if({view.params.deviceType} = 'Compressor',
	case(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null), 1, 'Remote', 2, 'Auto', 3, 'Manual', '—'),
	if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
		'Operator',
		if(coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false),
			'Program',
			if(coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false),
				'Maintenance',
				'—'))))
```


**`root/ModeRow/ModeOper`**

- `position.display`: expression

```js
({view.params.deviceType} = 'Pump' || {view.params.deviceType} = 'Valve' || {view.params.deviceType} = 'ExhaustFan' || {view.params.deviceType} = 'CoolingTower')
```


- `props.style.classes`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg1}), null, {view.custom.qg1}), null), false),
	'faceplate-mode-btn faceplate-mode-btn-active',
	'faceplate-mode-btn')
```


- `props.style.cursor`: expression

```js
if(!{view.custom.roMode}, 'pointer', 'not-allowed')
```


**`root/ModeRow/ModeProg`**

- `position.display`: expression

```js
({view.params.deviceType} = 'Pump' || {view.params.deviceType} = 'Valve' || {view.params.deviceType} = 'ExhaustFan' || {view.params.deviceType} = 'CoolingTower')
```


- `props.style.classes`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg2}), null, {view.custom.qg2}), null), false),
	'faceplate-mode-btn faceplate-mode-btn-active',
	'faceplate-mode-btn')
```


- `props.style.cursor`: expression

```js
if(!{view.custom.roMode}, 'pointer', 'not-allowed')
```


**`root/ModeRow/ModeMaint`**

- `position.display`: expression

```js
({view.params.deviceType} = 'Pump' || {view.params.deviceType} = 'Valve' || {view.params.deviceType} = 'ExhaustFan' || {view.params.deviceType} = 'CoolingTower')
```


- `props.style.classes`: expression

```js
if(coalesce(try(if(isNull({view.custom.qg3}), null, {view.custom.qg3}), null), false),
	'faceplate-mode-btn faceplate-mode-btn-active',
	'faceplate-mode-btn')
```


- `props.style.cursor`: expression

```js
if(!{view.custom.roMode}, 'pointer', 'not-allowed')
```


**`root/ModeRow/ModeRemote`**

- `position.display`: expression

```js
({view.params.deviceType} = 'Compressor')
```


- `props.style.classes`: expression

```js
if(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null) = 1, 'faceplate-mode-btn faceplate-mode-btn-active', 'faceplate-mode-btn')
```


- `props.style.cursor`: expression

```js
if(!{view.custom.roMode}, 'pointer', 'not-allowed')
```


**`root/ModeRow/ModeAuto`**

- `position.display`: expression

```js
({view.params.deviceType} = 'Compressor')
```


- `props.style.classes`: expression

```js
if(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null) = 2, 'faceplate-mode-btn faceplate-mode-btn-active', 'faceplate-mode-btn')
```


- `props.style.cursor`: expression

```js
if(!{view.custom.roMode}, 'pointer', 'not-allowed')
```


**`root/ModeRow/ModeManual`**

- `position.display`: expression

```js
({view.params.deviceType} = 'Compressor')
```


- `props.style.classes`: expression

```js
if(try(if(isNull({view.custom.qg0}), null, {view.custom.qg0}), null) = 3, 'faceplate-mode-btn faceplate-mode-btn-active', 'faceplate-mode-btn')
```


- `props.style.cursor`: expression

```js
if(!{view.custom.roMode}, 'pointer', 'not-allowed')
```

</details>

## Event Scripts And Handlers

- **`root/ModeRow/ModeOper`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
dt = str(self.view.params.deviceType or '')
if dt == 'Pump':
    shared.ValveCommands.setPumpMode(base, 'Sts_Oper')
else:
    shared.ValveCommands.setMode(base, 'OPER')
```

- **`root/ModeRow/ModeProg`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
dt = str(self.view.params.deviceType or '')
if dt == 'Pump':
    shared.ValveCommands.setPumpMode(base, 'Sts_Prog')
else:
    shared.ValveCommands.setMode(base, 'PROG')
```

- **`root/ModeRow/ModeMaint`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
dt = str(self.view.params.deviceType or '')
if dt == 'Pump':
    shared.ValveCommands.setPumpMode(base, 'Sts_Maint')
else:
    shared.ValveCommands.setMode(base, 'MAINT')
```

- **`root/ModeRow/ModeRemote`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return  # security-tiers
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Comp/CP_Mode']
vals = [1]
system.tag.writeBlocking(paths, vals)
```

- **`root/ModeRow/ModeAuto`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return  # security-tiers
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Comp/CP_Mode']
vals = [2]
system.tag.writeBlocking(paths, vals)
```

- **`root/ModeRow/ModeManual`** `dom.onClick`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return  # security-tiers
base = self.view.params.tagPath
if not base:
    return
paths = [base + '/Comp/CP_Mode']
vals = [3]
system.tag.writeBlocking(paths, vals)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (6): [03\_Elements/01\_Status/Icons/Auto](../../../03-elements/01-status/icons/auto.md), [03\_Elements/01\_Status/Icons/Hand](../../../03-elements/01-status/icons/hand.md), [03\_Elements/01\_Status/Icons/Maintenance](../../../03-elements/01-status/icons/maintenance.md), [03\_Elements/01\_Status/Icons/Operator](../../../03-elements/01-status/icons/operator.md), [03\_Elements/01\_Status/Icons/Program](../../../03-elements/01-status/icons/program.md), [03\_Elements/01\_Status/Icons/Remote](../../../03-elements/01-status/icons/remote.md)

**Embedded in** (3): [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./valve/controls.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 8 | style class |
| `faceplate-mode-btn` | 6 | stylesheet |
| `faceplate-mode-btn-label` | 6 | style class |
| `faceplate-mode-current` | 1 | no rule found |
| `faceplate-mode-header` | 1 | no rule found |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |
| `faceplate-mode-btn-active` | bound | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Comp/CP_Mode`, `/DIn.Enabled`, `/Sts_Maint`, `/Sts_Oper`, `/Sts_Prog`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
