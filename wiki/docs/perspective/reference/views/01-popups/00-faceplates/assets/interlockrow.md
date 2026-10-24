---
title: "InterlockRow"
sidebar_label: "InterlockRow"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/InterlockRow (Asset (embedded piece)): 4 components, 14 bindings, 2 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/InterlockRow", "InterlockRow"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/InterlockRow`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/InterlockRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/InterlockRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; InterlockRow |
| Root | `ia.container.flex`, height 40, width 500 |
| Size | 4 components, 14 bindings, 2 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-30T20:12:34Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `interlockPath` | `""` | input |
| `channel` | `0` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `channel` | `0` | |
| `nn` | `"00"` | bound (expr) |
| `qg0` | `null` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roInterlocks` | `true` | bound (expr) |
| `tipInterlocks` | `""` | bound (expr) |
| `qg1` | `null` | bound (expr) |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1, ia.input.checkbox x1.

```text
root  ia.container.flex  [1 binding; 2 events]
  CondLbl  ia.display.label  [1 binding]
  StatusCode  ia.display.label  [1 binding]
  Bypass  ia.input.checkbox  [5 bindings]
```

## Bindings

14 bindings: expr 10, expr-struct 3, tag 1.

<details>
<summary>All 14 bindings, grouped by component</summary>

**`(view)`**

- `custom.nn`: expression

```js
if({view.params.channel} < 10, '0' + toStr({view.params.channel}), toStr({view.params.channel}))
```


- `custom.qg0`: expression

```js
try(if(isGood(tag({view.params.interlockPath} + '/Cfg_CondTxt' + {view.custom.nn} + '/Value')), tag({view.params.interlockPath} + '/Cfg_CondTxt' + {view.custom.nn} + '/Value'), null), null)
```


- `custom.permDevice`: expression

```js
if(coalesce({view.params.interlockPath}, '') = '', '', coalesce(try(lookup({view.custom.qg1}, toStr(coalesce(try(tag({view.params.interlockPath} + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg1}, toStr(coalesce(try(tag(left({view.params.interlockPath}, lastIndexOf({view.params.interlockPath}, '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup({view.custom.qg1}, toStr(coalesce(try(tag(left(left({view.params.interlockPath}, lastIndexOf({view.params.interlockPath}, '/')), lastIndexOf(left({view.params.interlockPath}, lastIndexOf({view.params.interlockPath}, '/')), '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), ''))
```


- `custom.roInterlocks`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Interlocks'], null), true)
```


- `custom.tipInterlocks`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roInterlocks}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Interlocks' + ' (Roles & Permissions)', '')
```


- `custom.qg1`: expression

```js
try(if(isGood(tag('[default]_Config/Security/DeviceTypes')), tag('[default]_Config/Security/DeviceTypes'), null), null)
```


**`root`**

- `props.style.classes`: structured expression (expr-struct), then script transform

```js
path: {view.params.interlockPath}
ch: {view.params.channel}
```

waitOnAll: `True`

Transform 1, script:

```python
path = value.get('path') or ''
ch = int(value.get('ch') or 0)
base = 'faceplate-interlock-row'
try:
    sts = int(system.tag.readBlocking([path + '/Sts_Intlk/Value'])[0].value or 0)
    if sts & (1 << ch):
        return base + ' faceplate-interlock-fault'
    return base + ' faceplate-interlock-ok'
except:
    return base
```


**`root/CondLbl`**

- `props.text`: expression

```js
coalesce({view.custom.qg0}, 'Interlock ' + {view.custom.nn})
```


**`root/StatusCode`**

- `props.text`: structured expression (expr-struct), then script transform

```js
path: {view.params.interlockPath}
ch: {view.params.channel}
```

waitOnAll: `True`

Transform 1, script:

```python
path = value.get('path') or ''
ch = int(value.get('ch') or 0)
try:
    sts = int(system.tag.readBlocking([path + '/Sts_Intlk/Value'])[0].value or 0)
    if sts & (1 << ch):
        return 'FLT'
    return 'OK'
except:
    return '—'
```


**`root/Bypass`**

- `props.selected`: tag

Mode `indirect`, tag path `{base}/MSet_Bypass{nn}/Value`, references `base` = `{view.params.interlockPath}`, `nn` = `{view.custom.nn}`, fallback delay 2.5 s


- `props.enabled`: structured expression (expr-struct), then script transform

```js
path: {view.params.interlockPath}
ch: {view.params.channel}
ro: {view.custom.roInterlocks}
```

waitOnAll: `True`

Transform 1, script:

```python
if value.get('ro'):
    return False
path = value.get('path') or ''
ch = int(value.get('ch') or 0)
try:
    cfg = int(system.tag.readBlocking([path + '/Cfg_Bypassable/Value'])[0].value or 0)
    return bool(cfg & (1 << ch))
except:
    return False
```


- `props.text`: expression

```js
''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipInterlocks} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipInterlocks}
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.contextmenu`, script action, scope `G`

```python
shared.ticketLog.promptFromEvent(self, event)
```

- **`root`** `component.ticketLog`, script action, scope `G`

```python
shared.ticketLog.handleMessage(self, payload)
```

## Related Views

**Embedded in** (1): [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./interlocks.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `faceplate-interlock-bypass` | 1 | stylesheet |
| `faceplate-interlock-cond` | 1 | stylesheet |
| `faceplate-interlock-row` | 1 | stylesheet |
| `faceplate-interlock-sts` | 1 | style class |
| `faceplate-interlock-fault` | bound | stylesheet |
| `faceplate-interlock-ok` | bound | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`
- `{base}/MSet_Bypass{nn}/Value`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/Cfg_Bypassable/Value`, `/Cfg_CondTxt`, `/Sts_Intlk/Value`, `/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
