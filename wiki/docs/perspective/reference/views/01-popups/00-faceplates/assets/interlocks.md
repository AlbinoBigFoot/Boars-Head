---
title: "Interlocks"
sidebar_label: "Interlocks"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Interlocks (Asset (embedded piece)): 9 components, 14 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Interlocks", "Interlocks"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Interlocks`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Interlocks` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Interlocks/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Interlocks |
| Root | `ia.container.flex`, height 480, width 520 |
| Size | 9 components, 14 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T20:12:34Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `qg0` | `null` | bound (expr) |
| `qg1` | `null` | bound (expr) |
| `qg2` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roInterlocks` | `true` | bound (expr) |
| `tipInterlocks` | `""` | bound (expr) |
| `qg3` | `null` | bound (expr) |

## Component Tree

Component types: ia.display.label x4, ia.container.flex x3, ia.input.button x1, ia.display.flex-repeater x1.

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    ResetBtn  ia.input.button  [3 bindings; 1 event]
  ColHdr  ia.container.flex
    HCond  ia.display.label
    HSts  ia.display.label
    HByp  ia.display.label
  EmptyChannels  ia.display.label  [1 binding]
  Channels  ia.display.flex-repeater  [1 binding; view: 01_Popups/00_Faceplates/_Assets/InterlockRow]
```

## Bindings

14 bindings: expr 10, expr-struct 4.

<details>
<summary>All 14 bindings, grouped by component</summary>

**`(view)`**

- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Interlock/Rdy_Reset/Value')), tag({view.params.tagPath} + '/Interlock/Rdy_Reset/Value'), null), null)
```


- `custom.qg1`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Interlock/Sts_Intlk/Value')), tag({view.params.tagPath} + '/Interlock/Sts_Intlk/Value'), null), null)
```


- `custom.qg2`: expression

```js
try(if(isGood(tag({view.params.tagPath} + '/Interlock/Cfg_CondTxt00/Value')), tag({view.params.tagPath} + '/Interlock/Cfg_CondTxt00/Value'), null), null)
```


- `custom.permDevice`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', coalesce(try(lookup({view.custom.qg3}, toStr(coalesce(try(tag({view.params.tagPath} + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg3}, toStr(coalesce(try(tag(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg3}, toStr(coalesce(try(tag(left(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')), lastIndexOf(left({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/')), '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), ''))
```


- `custom.roInterlocks`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Interlocks'], null), true)
```


- `custom.tipInterlocks`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roInterlocks}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Interlocks' + ' (Roles & Permissions)', '')
```


- `custom.qg3`: expression

```js
try(if(isGood(tag('[default]_Config/Security/DeviceTypes')), tag('[default]_Config/Security/DeviceTypes'), null), null)
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

**`root/Header/ResetBtn`**

- `props.enabled`: expression

```js
!{view.custom.roInterlocks} && {view.custom.qg0}
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```


**`root/EmptyChannels`**

- `position.display`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
sts: {view.custom.qg1}
c0: {view.custom.qg2}
```

waitOnAll: `True`

Transform 1, script:

```python
base = value.get('tagPath') or ''
if not base:
    return False
ilk = base + '/Interlock'
try:
    sts = int(value.get('sts') or 0)
    c0 = value.get('c0')
    if c0 is not None and str(c0).strip() != '':
        return False
    if sts:
        return False
    paths = [ilk + '/Cfg_CondTxt%02d/Value' % i for i in range(1, 16)]
    qv = system.tag.readBlocking(paths)
    for q in qv:
        txt = q.value
        if txt is not None and str(txt).strip() != '':
            return False
    return True
except:
    return True
```


**`root/Channels`**

- `props.instances`: structured expression (expr-struct), then script transform

```js
tagPath: {view.params.tagPath}
sts: {view.custom.qg1}
c0: {view.custom.qg2}
```

waitOnAll: `True`

Transform 1, script:

```python
base = value.get('tagPath') or ''
ilk = (base + '/Interlock') if base else ''
instances = []
if not ilk:
    return instances
try:
    sts = int(system.tag.readBlocking([ilk + '/Sts_Intlk/Value'])[0].value or 0)
except:
    sts = 0
try:
    paths = [ilk + '/Cfg_CondTxt%02d/Value' % i for i in range(16)]
    qv = system.tag.readBlocking(paths)
except:
    qv = [None] * 16
for i in range(16):
    txt = qv[i].value if qv[i] is not None else ''
    label_ok = bool(txt) and str(txt).strip() != ''
    bit = bool(sts & (1 << i))
    if not (bit or label_ok):
        continue
    instances.append({
        'instanceStyle': {'classes': 'faceplate-interlock-instance'},
        'instancePosition': {'basis': '40px', 'shrink': 0, 'grow': 0},
        'interlockPath': ilk,
        'channel': i
    })
return instances
```

</details>

## Event Scripts And Handlers

- **`root/Header/ResetBtn`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.roInterlocks:
    return
base = self.view.params.tagPath
if not base:
    return
p = base + '/Interlock/OCmd_Reset/Value'
system.tag.writeBlocking([p], [True])
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/InterlockRow](./interlockrow.md) (flex repeater)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 5 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `faceplate-config-empty` | 1 | style class |
| `faceplate-interlock-channels` | 1 | stylesheet |
| `faceplate-interlock-colhdr` | 1 | stylesheet |
| `faceplate-interlock-header` | 1 | stylesheet |
| `faceplate-interlocks` | 1 | stylesheet |
| `faceplate-section` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/Interlock`, `/Interlock/Cfg_CondTxt00/Value`, `/Interlock/OCmd_Reset/Value`, `/Interlock/Rdy_Reset/Value`, `/Interlock/Sts_Intlk/Value`, `/Sts_Intlk/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
