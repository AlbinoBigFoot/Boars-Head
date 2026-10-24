---
title: "ConfigField"
sidebar_label: "ConfigField"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigField (Asset (embedded piece)): 8 components, 38 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Configuration/ConfigField", "ConfigField"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Configuration/ConfigField/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Configuration &gt; ConfigField |
| Root | `ia.container.flex`, height 40, width 400 |
| Size | 8 components, 38 bindings, 0 event handlers, 1 change scripts, 3 message handlers |
| Last saved | 2026-08-18T23:50:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `inputKind` | `"checkbox"` | input |
| `label` | `""` | input |
| `tagPath` | `""` | input |
| `engineering` | `false` | input |
| `enumPath` | `""` | input |
| `readOnly` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `ok` | `""` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roConfiguration` | `true` | bound (expr) |
| `tipConfiguration` | `""` | bound (expr) |
| `roSetpoint` | `true` | bound (expr) |
| `tipSetpoint` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.view x4, ia.display.label x2, ia.container.flex x1, ia.input.checkbox x1.

```text
root  ia.container.flex  [2 bindings]
  Lbl  ia.display.label  [1 binding]
  Chk  ia.input.checkbox  [6 bindings]
  ChkPlaceholder  ia.display.label  [1 binding]
  Analog  ia.display.view  [5 bindings; view: 03_Elements/00_Control/AnalogInput]
  MultiState  ia.display.view  [7 bindings; view: 03_Elements/00_Control/MultiStateInput]
  Time  ia.display.view  [5 bindings; view: 03_Elements/00_Control/TimeInput]
  String  ia.display.view  [5 bindings; view: 03_Elements/00_Control/StringInput]
```

## Bindings

38 bindings: expr 36, property 2.

<details>
<summary>All 38 bindings, grouped by component</summary>

**`(view)`**

- `custom.ok`: expression

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath})), false), false) && !isNull(try(tag({view.params.tagPath}), null)) && coalesce(try(abs(toFloat(tag({view.params.tagPath}))) < 1e30, true), true)
```


- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roConfiguration`: expression

```js
coalesce({session.custom.EngineeringReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), true)
```


- `custom.tipConfiguration`: expression

```js
if(!coalesce({session.custom.EngineeringReadOnly}, true) && coalesce({view.custom.roConfiguration}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), 'Setpoint', 'Configuration') + ' (Roles & Permissions)', '')
```


- `custom.roSetpoint`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), true)
```


- `custom.tipSetpoint`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roSetpoint}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), 'Configuration', 'Setpoint') + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Lbl`**

- `props.text`: property `view.params.label`

**`root/Chk`**

- `position.display`: expression

```js
{view.params.tagPath} != '' && (lower({view.params.inputKind}) = 'checkbox' || lower({view.params.inputKind}) = 'bool' || lower({view.params.inputKind}) = 'boolean') && coalesce({view.custom.ok}, false)
```


- `props.selected`: expression

```js
if({view.params.tagPath} = '', false,
	coalesce(try(if(!isGood(tag({view.params.tagPath})), null, tag({view.params.tagPath})), null), false))
```


- `props.enabled`: expression

```js
(!coalesce(if(coalesce({view.params.engineering}, false), {view.custom.roConfiguration}, {view.custom.roSetpoint}), false)) && !coalesce({view.params.readOnly}, false)
```


- `props.style.classes`: expression

```js
''
```


- `meta.tooltip.enabled`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint}) != ''
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint})
```


**`root/ChkPlaceholder`**

- `position.display`: expression

```js
{view.params.tagPath} != '' && (lower({view.params.inputKind}) = 'checkbox' || lower({view.params.inputKind}) = 'bool' || lower({view.params.inputKind}) = 'boolean') && !coalesce({view.custom.ok}, false)
```


**`root/Analog`**

- `position.display`: expression

```js
lower({view.params.inputKind}) = 'numeric' || lower({view.params.inputKind}) = 'number' || lower({view.params.inputKind}) = 'analog'
```


- `props.params.tagPath`: expression

```js
if(lower({view.params.inputKind}) = 'numeric' || lower({view.params.inputKind}) = 'number' || lower({view.params.inputKind}) = 'analog', {view.params.tagPath}, '')
```


- `props.params.permission`: expression

```js
(!coalesce(if(coalesce({view.params.engineering}, false), {view.custom.roConfiguration}, {view.custom.roSetpoint}), false)) && !coalesce({view.params.readOnly}, false)
```


- `meta.tooltip.enabled`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint}) != ''
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint})
```


**`root/MultiState`**

- `position.display`: expression

```js
lower({view.params.inputKind}) = 'multistate'
```


- `props.params.tagPath`: expression

```js
if(lower({view.params.inputKind}) = 'multistate', {view.params.tagPath}, '')
```


- `props.params.permission`: expression

```js
(!coalesce(if(coalesce({view.params.engineering}, false), {view.custom.roConfiguration}, {view.custom.roSetpoint}), false)) && !coalesce({view.params.readOnly}, false)
```


- `props.params.enumPath`: expression

```js
if(lower({view.params.inputKind}) = 'multistate', coalesce({view.params.enumPath}, ''), '')
```


- `props.params.confirmLabel`: property `view.params.label`

- `meta.tooltip.enabled`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint}) != ''
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint})
```


**`root/Time`**

- `position.display`: expression

```js
lower({view.params.inputKind}) = 'time'
```


- `props.params.tagPath`: expression

```js
if(lower({view.params.inputKind}) = 'time', {view.params.tagPath}, '')
```


- `props.params.permission`: expression

```js
(!coalesce(if(coalesce({view.params.engineering}, false), {view.custom.roConfiguration}, {view.custom.roSetpoint}), false)) && !coalesce({view.params.readOnly}, false)
```


- `meta.tooltip.enabled`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint}) != ''
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint})
```


**`root/String`**

- `position.display`: expression

```js
lower({view.params.inputKind}) = 'string' || lower({view.params.inputKind}) = 'text'
```


- `props.params.tagPath`: expression

```js
if(lower({view.params.inputKind}) = 'string' || lower({view.params.inputKind}) = 'text', {view.params.tagPath}, '')
```


- `props.params.permission`: expression

```js
(!coalesce(if(coalesce({view.params.engineering}, false), {view.custom.roConfiguration}, {view.custom.roSetpoint}), false)) && !coalesce({view.params.readOnly}, false)
```


- `meta.tooltip.enabled`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint}) != ''
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.engineering}, false), {view.custom.tipConfiguration}, {view.custom.tipSetpoint})
```

</details>

## Event Scripts And Handlers

- **`root/Chk`** change script on `props.selected`

```python
try:
    if origin != 'Browser':
        return
    if (self.view.custom.roConfiguration if self.view.params.engineering else self.view.custom.roSetpoint):
        self.refreshBinding('props.selected')
        return
    tagPath = self.view.params.tagPath
    if not tagPath:
        self.refreshBinding('props.selected')
        return
    newValue = bool(currentValue.value)
    oldValue = bool(previousValue.value) if previousValue is not None else (not newValue)
    if newValue == oldValue:
        return
    label = self.view.params.label or tagPath
    shared.Alerts.promptConfigWrite(self, 'props.selected', tagPath, label, newValue, oldValue)
except:
    system.util.getLogger('ConfigField').info('Error prompting apply write')
    try:
        self.refreshBinding('props.selected')
    except:
        pass
```

- **`root`** message handler `cancel` (scope: page)

```python
path = payload.get('tagPath') if payload else None
if path and path != self.view.params.tagPath:
    return
try:
    self.getChild('Chk').refreshBinding('props.selected')
except:
    pass
```

- **`root`** message handler `writeValue` (scope: page)

```python
if self.view.params.readOnly:
    return  # pax-bindings: live PLC member, read only
kind = str(self.view.params.inputKind or 'checkbox').lower()
if kind not in ('checkbox', 'bool', 'boolean'):
    return
path = payload.get('tagPath') if payload else None
if not path or path != self.view.params.tagPath:
    return
if payload.get('alreadyWritten'):
    try:
        self.getChild('Chk').refreshBinding('props.selected')
    except:
        pass
    return
try:
    shared.Audit.writeTag(
        path,
        payload.get('value'),
        label=payload.get('label'),
        viewName=payload.get('viewName') or self.view.id.split('@')[0],
    )
except:
    system.tag.writeBlocking([path], [payload.get('value')])
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.promptConfigWrite](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Audit.writeTag](../../../../../../../scripting/reference/modules/shared-audit.md).

## Related Views

**Embeds** (4): [03\_Elements/00\_Control/AnalogInput](../../../../03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/MultiStateInput](../../../../03-elements/00-control/multistateinput.md), [03\_Elements/00\_Control/StringInput](../../../../03-elements/00-control/stringinput.md), [03\_Elements/00\_Control/TimeInput](../../../../03-elements/00-control/timeinput.md)

**Embedded in** (4): [01\_Popups/00\_Faceplates/DiscreteInput](../../discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](./configsection.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](../tankoverview/overview.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](../valve/interlocks.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `config-field-label` | 1 | stylesheet |
| `value-bad` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
