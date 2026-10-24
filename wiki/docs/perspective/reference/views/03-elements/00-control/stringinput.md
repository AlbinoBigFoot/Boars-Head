---
title: "StringInput"
sidebar_label: "StringInput"
description: "Perspective view 03_Elements/00_Control/StringInput (Element (small reusable part)): 4 components, 13 bindings, 2 event scripts."
generated: true
keywords: ["03_Elements/00_Control/StringInput", "StringInput"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/00_Control/StringInput`.

| | |
|---|---|
| View path | `03_Elements/00_Control/StringInput` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/00_Control/StringInput/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 00\_Control &gt; StringInput |
| Root | `ia.container.flex`, height 28, width 160 |
| Size | 4 components, 13 bindings, 2 event handlers, 0 change scripts, 3 message handlers |
| Last saved | 2026-08-18T23:55:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `label` | `"Null"` | input |
| `permission` | `true` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `edit` | `false` | |
| `value` | `""` | bound (expr) |
| `ok` | `""` | bound (expr) |
| `qualityOk` | `false` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.input.text-field x1, ia.display.label x1, ia.display.icon x1.

```text
root  ia.container.flex  [2 bindings]
  EditValue  ia.input.text-field  [2 bindings; 1 event]
  Value  ia.display.label  [3 bindings]
  EditIcon  ia.display.icon  [3 bindings; 1 event]
```

## Bindings

13 bindings: expr 12, property 1.

<details>
<summary>All 13 bindings, grouped by component</summary>

**`(view)`**

- `custom.value`: expression, then expression + expression transform

```js
tag({view.params.tagPath})
```

Transform 1, expression:

```js
if(isNull({value}), '', toStr({value}))
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag({view.params.tagPath})), false), false), {value}, '—')
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

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/EditValue`**

- `position.display`: property `view.custom.edit`

- `props.enabled`: expression

```js
{view.params.permission} && !coalesce({session.custom.ReadOnly}, false)
```


**`root/Value`**

- `position.display`: expression

```js
!{view.custom.edit}
```


- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') != '' && !coalesce({view.custom.ok}, false), '—', {view.custom.value})
```


- `props.style.classes`: expression

```js
if(coalesce({view.params.tagPath}, '') != '' && !coalesce({view.custom.ok}, false), 'Fonts/Value value-bad', 'Fonts/Value')
```


**`root/EditIcon`**

- `props.style.cursor`: expression

```js
if({view.params.permission} && !{session.custom.ReadOnly} && coalesce({view.custom.qualityOk}, false), 'pointer', 'not-allowed')
```


- `props.style.classes`: expression

```js
if({view.params.permission} && !{session.custom.ReadOnly} && coalesce({view.custom.qualityOk}, false), 'Fonts/Value', 'Fonts/Label value-bad')
```


- `props.style.opacity`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce({view.custom.qualityOk}, false), 1, 0.35)
```

</details>

## Event Scripts And Handlers

- **`root/EditValue`** `component.onActionPerformed`, script action, scope `G`

```python
if self.session.custom.ReadOnly:
    return
tagPath = self.view.params.tagPath
if not tagPath:
    return
newV = self.props.text
oldV = None
try:
    oldV = system.tag.readBlocking([tagPath])[0].value
except:
    oldV = self.view.custom.value
try:
    skip = shared.Audit.valuesEqual(newV, oldV)
except:
    skip = (newV == oldV)
self.view.custom.edit = False
try:
    self.props.text = oldV if oldV is not None else ''
except:
    pass
if skip:
    return
label = self.view.params.label
if label in (None, '', 'Null'):
    label = str(tagPath).split('/')[-1]
# ... 7 more line(s): see the view.json
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
if self.view.custom.edit:
    tagPath = self.view.params.tagPath
    try:
        newV = editVal.props.text
    except:
        newV = None
    oldV = None
    try:
        oldV = system.tag.readBlocking([tagPath])[0].value
    except:
        oldV = self.view.custom.value
    self.view.custom.edit = False
    try:
        editVal.props.text = '' if oldV is None else str(oldV)
    except:
        pass
# ... 23 more line(s): see the view.json
```

- **`root`** message handler `cancel` (scope: page)

```python
if not self.view.params.tagPath or payload.get('tagPath') != self.view.params.tagPath:
    return
self.view.custom.edit = False
try:
    qv = system.tag.readBlocking([self.view.params.tagPath])[0].value
    self.getChild('EditValue').props.text = '' if qv is None else str(qv)
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
    self.getChild('EditValue').props.text = '' if payload.get('value') is None else str(payload.get('value'))
except:
    pass
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Audit.valuesEqual](../../../../../scripting/reference/modules/shared-audit.md), [shared.Audit.writeTag](../../../../../scripting/reference/modules/shared-audit.md).

## Related Views

**Embedded in** (6): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigField](../../01-popups/00-faceplates/assets/configuration/configfield.md), [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](../../01-popups/00-faceplates/assets/interlockpanel.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](../../01-popups/00-faceplates/assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](../../01-popups/00-faceplates/assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](../../01-popups/00-faceplates/assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](../../01-popups/00-faceplates/assets/valve/configuration.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 3 | style class |
| `config-input-row` | 1 | stylesheet |
| `Fonts/Label` | bound | style class |
| `value-bad` | bound | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
