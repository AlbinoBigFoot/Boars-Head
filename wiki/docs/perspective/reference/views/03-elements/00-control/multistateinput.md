---
title: "MultiStateInput"
sidebar_label: "MultiStateInput"
description: "Perspective view 03_Elements/00_Control/MultiStateInput (Element (small reusable part)): 4 components, 17 bindings, 3 event scripts."
generated: true
keywords: ["03_Elements/00_Control/MultiStateInput", "MultiStateInput"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/00_Control/MultiStateInput`.

| | |
|---|---|
| View path | `03_Elements/00_Control/MultiStateInput` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/00_Control/MultiStateInput/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 00\_Control &gt; MultiStateInput |
| Root | `ia.container.flex`, height 28, width 372 |
| Size | 4 components, 17 bindings, 1 event handlers, 2 change scripts, 3 message handlers |
| Last saved | 2026-07-30T20:12:34Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `Basis` | `{"eu": "", "input": "", "label": ""}` | input |
| `faceplate` | `""` | input |
| `label` | `""` | input |
| `permission` | `true` | input |
| `tagPath` | `""` | input |
| `enumPath` | `""` | input |
| `confirmLabel` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `edit` | `false` | |
| `editTimeout` | `{"durationInSecs": 15}` | |
| `metadata` | `""` | bound (tag) |
| `enum` | `""` | bound (expr) |
| `qualityOk` | `false` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1, ia.input.dropdown x1, ia.display.icon x1.

```text
root  ia.container.flex  [2 bindings]
  Label  ia.display.label  [2 bindings]
  StateSelect  ia.input.dropdown  [3 bindings]
  EditIcon  ia.display.icon  [3 bindings; 1 event]
```

## Bindings

17 bindings: expr 9, expr-struct 6, property 1, tag 1.

<details>
<summary>All 17 bindings, grouped by component</summary>

**`(view)`**

- `custom.editTimeout.end`: structured expression (expr-struct), then expression transform

```js
edit: {view.custom.edit}
now: {view.custom.editTimeout.now}
stop: {view.custom.editTimeout.stop}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['stop'] != '' && {value}['edit'],
	{value}['now'] > {value}['stop'],
	False
	)
```


- `custom.editTimeout.now`: expression

```js
now()
```


- `custom.editTimeout.start`: property `view.custom.edit`, then expression transform

Transform 1, expression:

```js
if({value},now(0),'')
```


- `custom.editTimeout.stop`: structured expression (expr-struct), then expression transform

```js
duration: {view.custom.editTimeout.durationInSecs}
start: {view.custom.editTimeout.start}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['start'] != '' && {value}['duration'] != '' && {value}['duration'] > 0,
dateArithmetic({value}['start'] , {value}['duration'], "seconds"),
'')
```


- `custom.metadata`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}.Metadata`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	"",
	{value}
	)
```


- `custom.enum`: expression

```js
if(coalesce({view.params.enumPath}, '') = '', null, tag('[default]_Config/Enums/' + {view.params.enumPath}))
```


- `custom.qualityOk`: expression

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath})), false), false)
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


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/Label`**

- `position.display`: expression

```js
!({view.params.label} = 'Null' || {view.params.label} = null)
```


- `props.text`: structured expression (expr-struct), then expression transform

```js
metadata: {view.custom.metadata}
tagName: {view.params.tagPath}
```

waitOnAll: `True`

Transform 1, expression:

```js
if({value}['metadata'] != '',
	if({value}['metadata']['shortDescription'] != "",
	   {value}['metadata']['shortDescription'],
	   if({value}['tagName'] != "",
		  {value}['tagName'],
		  ""
		 )
	),
	{value}['tagName']
)
```


**`root/StateSelect`**

- `props.enabled`: expression

```js
{view.custom.edit} && {view.params.permission} && !{session.custom.ReadOnly}
```


- `props.options`: structured expression (expr-struct), then script transform

```js
enum: {view.custom.enum}
enumPath: {view.params.enumPath}
metadata: {view.custom.metadata}
tagPath: {view.params.tagPath}
value: {this.props.value}
```

waitOnAll: `True`

Transform 1, script:

```python
# Options: enum DataSet (params.enumPath under [default]_Config/Enums via shared.Enums; rows with selectable
# false stay listed but disabled) > metadata states (dict only - a list-typed metadata override is ignored)
# > Boolean Off/On > the current value alone (shown, not selectable). Never a made-up 0/1 list.
cur = value.get('value')
ep = value.get('enumPath')
if ep:
    ds = value.get('enum')
    opts = shared.Enums.options(ep, cur, ds if hasattr(ds, 'getRowCount') else None)
    if opts:
        return opts
md = value.get('metadata')
try:
    states = md['states'] if md else None
except:
    states = None
out = []
try:
    for s in states or []:
        out.append({'label': s.get('label', str(s.get('value'))), 'value': s.get('value')})
except:
    out = []
if out:
    return out
try:
    dt = str(system.tag.readBlocking([value['tagPath'] + '.DataType'])[0].value)
except:
    dt = ''
if dt == 'Boolean':
    return [{'label': 'Off', 'value': False}, {'label': 'On', 'value': True}]
if cur is None or cur == '':
    return []
return [{'label': str(cur), 'value': cur, 'isDisabled': True}]
```


- `props.value`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath})), false), false), tag({view.params.tagPath}), null)
```


**`root/EditIcon`**

- `props.style.classes`: expression

```js
if({view.params.permission} && !{session.custom.ReadOnly} && coalesce({view.custom.qualityOk}, false), 'Fonts/Value', 'Fonts/Label value-bad')
```


- `props.style.cursor`: expression

```js
if({view.params.permission} && !{session.custom.ReadOnly} && coalesce({view.custom.qualityOk}, false), 'pointer', 'not-allowed')
```


- `props.style.opacity`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce({view.custom.qualityOk}, false), 1, 0.35)
```

</details>

## Event Scripts And Handlers

- **`root/EditIcon`** `dom.onClick`, script action, scope `G`

```python
if not self.view.custom.qualityOk:
    return
if self.view.params.permission and not self.session.custom.ReadOnly:
    if self.view.custom.edit:
        self.view.custom.edit = False
    else:
        self.view.custom.edit = True
```

- **`(view)`** change script on `custom.editTimeout.end`

```python
self.custom.edit = False
```

- **`root/StateSelect`** change script on `props.value`

```python
# Writes only through the shared confirm (Apply / Cancel) -> shared.Audit.writeTag (Faceplates/Operate gate +
# OpsAudit). The dropdown snaps back to the tag value; Apply writes, then the writeValue handler refreshes it.
if str(origin) != 'Browser':
    return
tagPath = self.view.params.tagPath
newValue = currentValue.value if currentValue is not None else None
self.view.custom.edit = False
try:
    oldValue = system.tag.readBlocking([tagPath])[0].value if tagPath else None
except:
    oldValue = previousValue.value if previousValue is not None else None
# snap back: assign, then refresh (a refresh alone does not re-send an unchanged tag value to the client)
self.props.value = oldValue
self.refreshBinding('props.value')
if not tagPath or newValue is None or newValue == '':
    return
if self.session.custom.ReadOnly or not self.view.params.permission:
    return
if not isinstance(newValue, bool):
    try:
        if float(newValue) == int(float(newValue)):
            newValue = int(float(newValue))
    except:
        pass
label = self.view.params.confirmLabel or self.view.params.label
# ... 13 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

- **`root`** message handler `cancel` (scope: page)

```python
# Cancel: the Alert popup's Apply already wrote through shared.Audit.writeTag - only refresh here, never write
if not payload or not self.view.params.tagPath or payload.get('tagPath') != self.view.params.tagPath:
    return
self.view.custom.edit = False
sel = self.getChild('StateSelect')
try:
    sel.props.value = system.tag.readBlocking([self.view.params.tagPath])[0].value
except:
    pass
try:
    sel.refreshBinding('props.value')
except:
    pass
```

- **`root`** message handler `writeValue` (scope: page)

```python
# Apply: the Alert popup's Apply already wrote through shared.Audit.writeTag - only refresh here, never write
if not payload or not self.view.params.tagPath or payload.get('tagPath') != self.view.params.tagPath:
    return
self.view.custom.edit = False
sel = self.getChild('StateSelect')
try:
    sel.props.value = system.tag.readBlocking([self.view.params.tagPath])[0].value
except:
    pass
try:
    sel.refreshBinding('props.value')
except:
    pass
```

Project script calls: [shared.Alerts.confirmApplyWrite](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Audit.writeTag](../../../../../scripting/reference/modules/shared-audit.md), [shared.Enums](../../../../../scripting/reference/modules/shared-enums.md), [shared.Enums.options](../../../../../scripting/reference/modules/shared-enums.md).

## Related Views

**Embedded in** (2): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](../../01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigurationRow](../../01-popups/00-faceplates/assets/configuration/configurationrow.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `config-input-label` | 1 | stylesheet |
| `config-input-row` | 1 | stylesheet |
| `value-bad` | bound | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Enums via shared.Enums; rows with selectable`
- `[default]_Config/Enums/`
- `{tagPath}.Metadata`

Member paths appended to a base path in expressions (relative):

`.DataType`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
