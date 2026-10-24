---
title: "Numeric"
sidebar_label: "Numeric"
description: "Perspective view 03_Elements/00_Control/_Assets/Numeric (Asset (embedded piece)): 4 components, 20 bindings, 6 event scripts."
generated: true
keywords: ["03_Elements/00_Control/_Assets/Numeric", "Numeric"]
---

:::note

:::


**Asset (embedded piece)**: `03_Elements/00_Control/_Assets/Numeric`.

| | |
|---|---|
| View path | `03_Elements/00_Control/_Assets/Numeric` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/00_Control/_Assets/Numeric/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 00\_Control &gt; \_Assets &gt; Numeric |
| Root | `ia.container.flex`, height 20, width 100 |
| Size | 4 components, 20 bindings, 4 event handlers, 2 change scripts, 3 message handlers |
| Last saved | 2026-07-28T23:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `permissions` | `true` | input |
| `setpoint` | `true` | input |
| `spacing` | `{"center": false, "data": 0, "engUnit": 30}` | inout |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `engUnit` | `""` | bound (expr) |
| `format` | `"#0.0"` | bound (expr) |
| `metadata` | `null` | bound (expr) |
| `quality` | `""` | bound (expr) |
| `tagName` | `""` | bound (expr) |
| `timeOut` | `{"actionComplete": true, "startTime": {"$": ["ts", 192, 0], "$ts": 0}}` | |
| `value` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1, ia.input.numeric-entry-field x1.

```text
root  ia.container.flex  [2 bindings; 1 event]
  NumericEntryField  ia.input.numeric-entry-field  [5 bindings]
  Value  ia.display.label  [4 bindings; 2 events]
  EngineeringUnit  ia.display.label  [1 binding; 1 event]
```

## Bindings

20 bindings: expr 14, property 4, expr-struct 2.

<details>
<summary>All 20 bindings, grouped by component</summary>

**`(view)`**

- `custom.engUnit`: expression

```js
if(qualityOf(tag({view.params.tagPath})) != 'Good',
	'',
	tag({view.params.tagPath} + '.EngUnit'))
```


- `custom.format`: expression

```js
if(qualityOf(tag({view.params.tagPath})) != 'Good',
	'#0.0',
	if(isNull(tag({view.params.tagPath} + '.FormatString')) || tag({view.params.tagPath} + '.FormatString') = '',
		'#0.0',
		tag({view.params.tagPath} + '.FormatString')))
```


- `custom.metadata`: expression

```js
if({view.params.tagPath} != '' && isGood(tag({view.params.tagPath} + '.Metadata')),
	tag({view.params.tagPath} + '.Metadata'),
	'')
```


- `custom.quality`: expression

```js
qualityOf(tag({view.params.tagPath}))
```


- `custom.tagName`: expression

```js
subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)
```


- `custom.timeOut.endTime`: expression

```js
dateArithmetic({view.custom.timeOut.startTime}, 60, 'sec')
```


- `custom.timeOut.status`: expression

```js
(now() > {view.custom.timeOut.endTime}) || {view.custom.timeOut.actionComplete}
```


- `custom.value`: expression

```js
if({view.custom.quality} != 'Good',
	'',
	numberFormat(tag({view.params.tagPath}), {view.custom.format}))
```


**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/NumericEntryField`**

- `position.display`: expression

```js
!{../Value.position.display}
```


- `props.enabled`: expression

```js
{view.params.permissions} && !{session.custom.ReadOnly}
```


- `props.format`: property `view.custom.format`

- `props.style.classes`: expression

```js
if({view.custom.quality} = 'Good',
	'Fonts/Value',
	'Fonts/Label')
```


- `props.value`: expression

```js
toFloat({view.custom.value})
```


**`root/Value`**

- `position.display`: property `view.custom.timeOut.status`

- `props.style.classes`: expression

```js
if({view.custom.quality} = 'Good',
	'Fonts/Value',
	'Fonts/Label')
```


- `props.style.cursor`: expression

```js
if({view.params.setpoint} && {view.params.permissions} && !{session.custom.ReadOnly},
	'pointer',
	if({view.params.setpoint},
		'not-allowed',
		''))
```


- `props.text`: property `view.custom.value`

**`root/EngineeringUnit`**

- `props.text`: property `view.custom.engUnit`

</details>

## Event Scripts And Handlers

- **`root`** `system.onStartup`, script action, scope `G`

```python
self.getChild('Value').position.display = True
```

- **`root/Value`** `dom.onClick`, script action, scope `G`

```python
if self.view.params.permissions and self.view.params.setpoint and not self.session.custom.ReadOnly:
    self.position.display = False
    self.view.custom.timeOut.startTime = system.date.now()
    self.view.custom.timeOut.actionComplete = False
```

- **`root/Value`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}')
```

- **`root/EngineeringUnit`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}')
```

- **`(view)`** change script on `custom.timeOut.status`

```python
system.perspective.closePopup(id = 'alertDialog')
```

- **`root/NumericEntryField`** change script on `props.value`

```python
try:
    if origin == 'Browser':
        self.refreshBinding('props.value')
        self.view.custom.timeOut.startTime = system.date.now()
        oldValue = previousValue.value
        newValue = currentValue.value
        label = self.view.custom.tagName
        try:
            md = self.view.custom.metadata
            if md and 'shortDescription' in md and md['shortDescription']:
                label = md['shortDescription']
        except:
            pass
        payload = {
            'tagPath': self.view.params.tagPath,
            'value': currentValue.value,
            'label': label,
            'viewName': self.view.id.split('@')[0],
        }
        shared.Alerts.showAlert(
            title='Update setpoint',
            message='Tag: %s<br><br>Old: %s<br>New: %s' % (label, oldValue, newValue),
            showCloseBtn=False,
            btnTextPrimary='Cancel',
            btnTextSecondary='Accept',
# ... 6 more line(s): see the view.json
```

- **`root`** message handler `cancel` (scope: page)

```python
if payload.get('tagPath') == self.view.params.tagPath:
    self.getChild('NumericEntryField').refreshBinding('props.value')
    self.view.custom.timeOut.actionComplete = True
```

- **`root`** message handler `writeValue` (scope: page)

```python
if not self.view.params.tagPath or payload.get('tagPath') != self.view.params.tagPath:
    return
if not payload.get('alreadyWritten'):
    shared.Audit.writeTag(
        payload['tagPath'],
        payload['value'],
        label=payload.get('label'),
        viewName=payload.get('viewName'),
    )
self.view.custom.timeOut.actionComplete = True
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.showAlert](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Audit.writeTag](../../../../../../scripting/reference/modules/shared-audit.md).

## Related Views

**Embedded in** (1): [03\_Elements/00\_Control/AnalogValue](../analogvalue.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.EngUnit`, `.FormatString`, `.Metadata`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
