---
title: "TimeInput"
sidebar_label: "TimeInput"
description: "Perspective view 03_Elements/00_Control/TimeInput (Element (small reusable part)): 6 components, 28 bindings, 4 event scripts."
generated: true
keywords: ["03_Elements/00_Control/TimeInput", "TimeInput"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/00_Control/TimeInput`.

| | |
|---|---|
| View path | `03_Elements/00_Control/TimeInput` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/00_Control/TimeInput/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 00\_Control &gt; TimeInput |
| Root | `ia.container.flex`, height 28, width 372 |
| Size | 6 components, 28 bindings, 2 event handlers, 2 change scripts, 3 message handlers |
| Last saved | 2026-09-22T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `Basis` | `{"eu": "", "input": "", "label": ""}` | input |
| `faceplate` | `""` | input |
| `label` | `""` | input |
| `permission` | `true` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `edit` | `false` | |
| `primedValue` | `null` | not persistent |
| `editTimeout` | `{"durationInSecs": 15}` | |
| `format` | `""` | bound (expr) |
| `metadata` | `""` | bound (tag) |
| `quality` | `""` | bound (tag) |
| `value` | `""` | bound (expr) |
| `ok` | `""` | bound (expr) |
| `qualityOk` | `false` | bound (expr) |

## Component Tree

Component types: ia.display.label x3, ia.container.flex x1, ia.input.numeric-entry-field x1, ia.display.icon x1.

```text
root  ia.container.flex  [3 bindings]
  Label  ia.display.label  [2 bindings]
  EditValue  ia.input.numeric-entry-field  [5 bindings]
  Value  ia.display.label  [3 bindings; 1 event]
  EU  ia.display.label  [2 bindings]
  EditIcon  ia.display.icon  [3 bindings; 1 event]
```

## Bindings

28 bindings: expr 16, expr-struct 5, property 5, tag 2.

<details>
<summary>All 28 bindings, grouped by component</summary>

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


- `custom.format`: expression

```js
if({view.params.tagPath} = '', '#0',
   try(tag({view.params.tagPath} + '.FormatString'), '#0'))
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


- `custom.quality`: tag, then expression transform

Mode `expression`, tag path `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
qualityOf({value})
```


- `custom.value`: expression

```js
if(coalesce({view.params.tagPath}, '') != '' && !coalesce({view.custom.ok}, false), '—', if({view.params.tagPath} = '', '',
  if(try(isGood(tag({view.params.tagPath})), false),
     numberFormat(floor(toInt(try(tag({view.params.tagPath}), 0)) / 100), '00') + ':' +
     numberFormat(toInt(try(tag({view.params.tagPath}), 0)) % 100, '00'),
     '')))
```


- `custom.ok`: expression

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath})), false), false) && !isNull(try(tag({view.params.tagPath}), null)) && coalesce(try(abs(toFloat(tag({view.params.tagPath}))) < 1e30, true), true)
```


- `custom.qualityOk`: expression

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath})), false), false)
```


**`root`**

- `props.justify`: expression

```js
if({view.params.label} = 'Null' || {view.params.label} = null, 'flex-end', 'flex-start')
```


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


**`root/EditValue`**

- `custom.editedValue`: property `this.props.value`

- `meta.tooltip.enabled`: property `this.props.enabled`, then expression transform

Transform 1, expression:

```js
!{value}
```


- `position.display`: property `view.custom.edit`

- `props.enabled`: expression

```js
{view.params.permission} && !{session.custom.ReadOnly}
```


- `props.format`: expression

```js
'#0'
```


**`root/Value`**

- `position.display`: expression

```js
!{view.custom.edit}
```


- `props.style.classes`: expression

```js
if(coalesce({view.params.tagPath}, '') != '' && !coalesce({view.custom.ok}, false), 'Fonts/Value value-bad', 'Fonts/Value')
```


- `props.text`: property `view.custom.value`

**`root/EU`**

- `props.text`: expression

```js
if({view.custom.edit}, 'HHMM', '')
```


- `position.display`: expression

```js
coalesce({view.params.Basis.eu}, '') != 'none'
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

- **`root/Value`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}')
```

- **`root/EditIcon`** `dom.onClick`, script action, scope `G`

```python
if not self.view.custom.qualityOk:
    return
if not self.view.params.permission or self.session.custom.ReadOnly:
    return
editVal = None
try:
    editVal = self.parent.getChild('EditValue')
except:
    pass
tagPath = self.view.params.tagPath
tagVal = None
try:
    tagVal = system.tag.readBlocking([tagPath])[0].value
except:
    pass
self.view.custom.primedValue = tagVal
if self.view.custom.edit:
    self.view.custom.edit = False
    try:
        editVal.props.value = tagVal
    except:
        pass
else:
    try:
        editVal.props.value = tagVal
# ... 13 more line(s): see the view.json
```

- **`(view)`** change script on `custom.editTimeout.end`

```python
self.custom.edit = False
```

- **`root/EditValue`** change script on `custom.editedValue`

```python
if not self.view.custom.edit:
    return
if self.session.custom.ReadOnly:
    self.view.custom.edit = False
    return
tagPath = self.view.params.tagPath
if not tagPath:
    return
newV = currentValue.value
oldV = self.view.custom.primedValue
if oldV is None:
    try:
        oldV = system.tag.readBlocking([tagPath])[0].value
    except:
        oldV = previousValue.value
try:
    skip = shared.Audit.valuesEqual(newV, oldV)
except:
    skip = (newV == oldV)
self.view.custom.edit = False
try:
    self.props.value = oldV
except:
    pass
if skip:
# ... 11 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

- **`root`** message handler `cancel` (scope: page)

```python
if not self.view.params.tagPath or payload.get('tagPath') != self.view.params.tagPath:
    return
self.view.custom.edit = False
try:
    qv = system.tag.readBlocking([self.view.params.tagPath])[0].value
    self.getChild('EditValue').props.value = qv
except:
    pass
```

- **`root`** message handler `writeValue` (scope: page)

```python
if not self.view.params.tagPath or payload.get('tagPath') != self.view.params.tagPath:
    return
if not payload.get('alreadyWritten'):
    shared.Audit.writeTag(
        payload.get('tagPath'),
        payload.get('value'),
        label=payload.get('label'),
        viewName=payload.get('viewName') or self.view.id.split('@')[0],
    )
self.view.custom.edit = False
try:
    self.getChild('EditValue').props.value = payload.get('value')
except:
    pass
```

Project script calls: [shared.Alerts.confirmApplyWrite](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Audit.valuesEqual](../../../../../scripting/reference/modules/shared-audit.md), [shared.Audit.writeTag](../../../../../scripting/reference/modules/shared-audit.md).

## Related Views

**Embedded in** (2): [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](../../00-pages/groveport/shared/cg/ahuevappanel.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](../../01-popups/00-faceplates/assets/configuration/configfield.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `Fonts/Value` | 1 | style class |
| `analog-input-edit` | 1 | stylesheet |
| `config-input-label` | 1 | stylesheet |
| `config-input-row` | 1 | stylesheet |
| `value-bad` | bound | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}.Metadata`
- `{view.params.tagPath}`

Member paths appended to a base path in expressions (relative):

`.FormatString`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
