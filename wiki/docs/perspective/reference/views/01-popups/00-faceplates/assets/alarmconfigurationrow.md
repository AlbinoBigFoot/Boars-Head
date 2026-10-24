---
title: "AlarmConfigurationRow"
sidebar_label: "AlarmConfigurationRow"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow (Asset (embedded piece)): 13 components, 28 bindings, 5 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow", "AlarmConfigurationRow"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; AlarmConfigurationRow |
| Root | `ia.container.flex`, height 120, width 480 |
| Size | 13 components, 28 bindings, 2 event handlers, 3 change scripts, 3 message handlers |
| Last saved | 2026-07-30T19:30:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `alarmName` | `""` | input |
| `hasSetpoint` | `false` | input |
| `highlightRow` | `false` | input |
| `isDigital` | `true` | input |
| `instancePath` | `""` | input |
| `label` | `""` | input |
| `notes` | `""` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `priorityPath` | `""` | bound (expr) |
| `setpointPath` | `""` | bound (expr) |
| `priorityValue` | `""` | bound (expr) |
| `triggerValue` | `1` | bound (expr) |
| `setpointValue` | `0` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roAlarm` | `true` | bound (expr) |
| `tipAlarm` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x5, ia.display.label x5, ia.input.dropdown x2, ia.input.numeric-entry-field x1.

<details>
<summary>Component tree (13 components)</summary>

```text
root  ia.container.flex  [3 bindings]
  AlarmName  ia.display.label  [1 binding]
  Notes  ia.display.label  [2 bindings]
  Fields  ia.container.flex
    PrioritySection  ia.container.flex
      PriorityLabel  ia.display.label
      PriorityDropdown  ia.input.dropdown  [4 bindings; 1 event]
    TriggerSection  ia.container.flex  [1 binding]
      TriggerLabel  ia.display.label
      TriggerDropdown  ia.input.dropdown  [4 bindings; 1 event]
    SetpointSection  ia.container.flex  [1 binding]
      SetpointLabel  ia.display.label
      SetpointEntry  ia.input.numeric-entry-field  [4 bindings]
```

</details>

## Bindings

28 bindings: expr 22, property 4, expr-struct 2.

<details>
<summary>All 28 bindings, grouped by component</summary>

**`(view)`**

- `custom.priorityPath`: expression

```js
if({view.params.tagPath} = '' || {view.params.alarmName} = '', '', {view.params.tagPath} + '/Alarms/' + {view.params.alarmName} + '.Priority')
```


- `custom.setpointPath`: expression

```js
if({view.params.tagPath} = '' || {view.params.alarmName} = '', '', {view.params.tagPath} + '/Alarms/' + {view.params.alarmName} + '.Mode')
```


- `custom.priorityValue`: expression

```js
if({view.custom.priorityPath} = '', 'Medium',
  try(
    if(indexOf(toStr(try(if(!isGood(tag({view.custom.priorityPath})), null, tag({view.custom.priorityPath})), null)), '.') >= 0,
      subString(toStr(try(if(!isGood(tag({view.custom.priorityPath})), null, tag({view.custom.priorityPath})), null)), lastIndexOf(toStr(try(if(!isGood(tag({view.custom.priorityPath})), null, tag({view.custom.priorityPath})), null)), '.') + 1),
      if(toStr(try(if(!isGood(tag({view.custom.priorityPath})), null, tag({view.custom.priorityPath})), null)) = '', 'Medium', toStr(try(if(!isGood(tag({view.custom.priorityPath})), null, tag({view.custom.priorityPath})), null)))),
    'Medium'))
```


- `custom.triggerValue`: expression

```js
if({view.custom.setpointPath} = '', 'WhenTrue',
  try(
    if(indexOf(toStr(try(if(!isGood(tag({view.custom.setpointPath})), null, tag({view.custom.setpointPath})), null)), 'False') >= 0 ||
       toStr(try(if(!isGood(tag({view.custom.setpointPath})), null, tag({view.custom.setpointPath})), null)) = '0' ||
       toStr(try(if(!isGood(tag({view.custom.setpointPath})), null, tag({view.custom.setpointPath})), null)) = '0.0' ||
       toStr(try(if(!isGood(tag({view.custom.setpointPath})), null, tag({view.custom.setpointPath})), null)) = 'false',
      'WhenFalse', 'WhenTrue'),
    'WhenTrue'))
```


- `custom.setpointValue`: expression

```js
if({view.custom.setpointPath} = '', 0.0,
  coalesce(try(toFloat(try(if(!isGood(tag({view.custom.setpointPath})), null, tag({view.custom.setpointPath})), null)), 0.0), 0.0))
```


- `custom.permDevice`: expression

```js
if(coalesce({view.params.instancePath}, '') = '', '', coalesce(try(lookup(tag('[default]_Config/Security/DeviceTypes'), toStr(coalesce(try(tag({view.params.instancePath} + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup(tag('[default]_Config/Security/DeviceTypes'), toStr(coalesce(try(tag(left({view.params.instancePath}, lastIndexOf({view.params.instancePath}, '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), try(lookup(tag('[default]_Config/Security/DeviceTypes'), toStr(coalesce(try(tag(left(left({view.params.instancePath}, lastIndexOf({view.params.instancePath}, '/')), lastIndexOf(left({view.params.instancePath}, lastIndexOf({view.params.instancePath}, '/')), '/')) + '.TypeId'), ''), '')), null, 'TypeId', 'Device'), null), ''))
```


- `custom.roAlarm`: expression

```js
coalesce({session.custom.AlarmConfigReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Alarm'], null), true)
```


- `custom.tipAlarm`: expression

```js
if(!coalesce({session.custom.AlarmConfigReadOnly}, true) && coalesce({view.custom.roAlarm}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Alarm' + ' (Roles & Permissions)', '')
```


**`root`**

- `props.style.classes`: expression

```js
if({view.params.highlightRow}, 'faceplate-alarm-row faceplate-alarm-row-alt', 'faceplate-alarm-row')
```


- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
tagPath: 
```

waitOnAll: `True`

Transform 1, script:

```python
tagPath = ''
try:
    tagPath = self.view.params.tagPath
except:
    pass
if tagPath is None or str(tagPath).strip() == '':
    tagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]
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
            "link": {
              "url": "",
              "target": "self"
            },
            "method": {
              "name": "",
              "params": {}
            },
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
# ... 1 more line(s): see the view.json
```


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/AlarmName`**

- `props.text`: expression

```js
if({view.params.label} != '', {view.params.label}, {view.params.alarmName})
```


**`root/Notes`**

- `props.text`: expression

```js
if({view.params.notes} = '', '', 'Tag: ' + {view.params.notes})
```


- `position.display`: expression

```js
{view.params.notes} != ''
```


**`root/Fields/PrioritySection/PriorityDropdown`**

- `props.enabled`: expression

```js
!{view.custom.roAlarm} && {view.custom.priorityPath} != ''
```


- `props.value`: property `view.custom.priorityValue`

- `meta.tooltip.enabled`: expression

```js
{view.custom.tipAlarm} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipAlarm}
```


**`root/Fields/TriggerSection`**

- `position.display`: expression

```js
{view.params.isDigital} && !{view.params.hasSetpoint}
```


**`root/Fields/TriggerSection/TriggerDropdown`**

- `props.enabled`: expression

```js
!{view.custom.roAlarm} && {view.custom.setpointPath} != ''
```


- `props.value`: property `view.custom.triggerValue`

- `meta.tooltip.enabled`: expression

```js
{view.custom.tipAlarm} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipAlarm}
```


**`root/Fields/SetpointSection`**

- `position.display`: property `view.params.hasSetpoint`

**`root/Fields/SetpointSection/SetpointEntry`**

- `props.enabled`: expression

```js
!{view.custom.roAlarm} && {view.custom.setpointPath} != ''
```


- `props.value`: property `view.custom.setpointValue`

- `meta.tooltip.enabled`: expression

```js
{view.custom.tipAlarm} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipAlarm}
```

</details>

## Event Scripts And Handlers

- **`root/Fields/PrioritySection/PriorityDropdown`** `component.onActionPerformed`, script action, scope `G`

```python
oldVal = self.view.custom.priorityValue
if oldVal is None or str(oldVal).strip() == '':
    return
newVal = self.props.value
if newVal is None or str(newVal).strip() == '':
    self.refreshBinding('props.value')
    return
if str(newVal) == str(oldVal):
    return
self.refreshBinding('props.value')
if self.view.custom.roAlarm:
    return
label = (self.view.params.label or self.view.params.alarmName or 'Alarm') + ' priority'
shared.Alerts.confirmApplyWrite(
    label=label,
    tagPath=self.view.params.tagPath,
    newValue=str(newVal),
    oldValue=str(oldVal),
    title='Apply alarm configuration',
    extraPayload={
        'field': 'priority',
        'alarmName': self.view.params.alarmName,
        'valueTagPath': self.view.params.tagPath,
        'skipWrite': True,
        'viewName': self.view.id.split('@')[0],
# ... 2 more line(s): see the view.json
```

- **`root/Fields/TriggerSection/TriggerDropdown`** `component.onActionPerformed`, script action, scope `G`

```python
def _mode(v):
    s = str(v or '')
    if s in ('WhenFalse', '0', '0.0', 'False', 'false'):
        return 'WhenFalse'
    if s in ('WhenTrue', '1', '1.0', 'True', 'true'):
        return 'WhenTrue'
    return ''

oldV = _mode(self.view.custom.triggerValue)
if not oldV:
    return
v = _mode(self.props.value)
if not v or v == oldV:
    return
self.refreshBinding('props.value')
if self.view.custom.roAlarm:
    return
label = (self.view.params.label or self.view.params.alarmName or 'Alarm') + ' trigger'
shared.Alerts.confirmApplyWrite(
    label=label,
    tagPath=self.view.params.tagPath,
    newValue=v,
    oldValue=oldV,
    title='Apply alarm configuration',
    extraPayload={
# ... 7 more line(s): see the view.json
```

- **`root/Fields/PrioritySection/PriorityDropdown`** change script on `props.value`

```python
if str(origin) != 'Browser':
    return
oldVal = self.view.custom.priorityValue
if oldVal is None or str(oldVal).strip() == '':
    return
newVal = currentValue.value
if newVal is None or str(newVal).strip() == '':
    self.refreshBinding('props.value')
    return
if str(newVal) == str(oldVal):
    return
self.refreshBinding('props.value')
if self.view.custom.roAlarm:
    return
label = (self.view.params.label or self.view.params.alarmName or 'Alarm') + ' priority'
shared.Alerts.confirmApplyWrite(
    label=label,
    tagPath=self.view.params.tagPath,
    newValue=str(newVal),
    oldValue=str(oldVal),
    title='Apply alarm configuration',
    extraPayload={
        'field': 'priority',
        'alarmName': self.view.params.alarmName,
        'valueTagPath': self.view.params.tagPath,
# ... 4 more line(s): see the view.json
```

- **`root/Fields/TriggerSection/TriggerDropdown`** change script on `props.value`

```python
if str(origin) != 'Browser':
    return
def _mode(v):
    s = str(v or '')
    if s in ('WhenFalse', '0', '0.0', 'False', 'false'):
        return 'WhenFalse'
    if s in ('WhenTrue', '1', '1.0', 'True', 'true'):
        return 'WhenTrue'
    return ''
oldV = _mode(self.view.custom.triggerValue)
if not oldV:
    return
v = _mode(currentValue.value)
if not v or v == oldV:
    return
self.refreshBinding('props.value')
if self.view.custom.roAlarm:
    return
label = (self.view.params.label or self.view.params.alarmName or 'Alarm') + ' trigger'
shared.Alerts.confirmApplyWrite(
    label=label,
    tagPath=self.view.params.tagPath,
    newValue=v,
    oldValue=oldV,
    title='Apply alarm configuration',
# ... 8 more line(s): see the view.json
```

- **`root/Fields/SetpointSection/SetpointEntry`** change script on `props.value`

```python
try:
    if origin != 'Browser':
        return
    if self.view.custom.roAlarm:
        self.refreshBinding('props.value')
        return
    path = self.view.custom.setpointPath
    if not path:
        self.refreshBinding('props.value')
        return
    newVal = currentValue.value
    if newVal is None:
        self.refreshBinding('props.value')
        return
    oldVal = previousValue.value if previousValue is not None else None
    try:
        if oldVal is not None and float(newVal) == float(oldVal):
            return
    except:
        pass
    self.refreshBinding('props.value')
    label = (self.view.params.label or self.view.params.alarmName or 'Alarm') + ' setpoint'
    shared.Alerts.confirmApplyWrite(
        label=label,
        tagPath=path,
# ... 14 more line(s): see the view.json
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

- **`root`** message handler `cancel` (scope: page)

```python
path = payload.get('tagPath')
if not path:
    return
field = payload.get('field')
if field == 'priority' and path == self.view.custom.priorityPath:
    try:
        self.getChild('Fields').getChild('PrioritySection').getChild('PriorityDropdown').refreshBinding('props.value')
    except:
        pass
elif field in ('trigger', 'setpoint') and path == self.view.custom.setpointPath:
    try:
        if field == 'trigger':
            self.getChild('Fields').getChild('TriggerSection').getChild('TriggerDropdown').refreshBinding('props.value')
        else:
            self.getChild('Fields').getChild('SetpointSection').getChild('SetpointEntry').refreshBinding('props.value')
    except:
        pass
```

- **`root`** message handler `writeValue` (scope: page)

```python
if not payload:
    return
field = payload.get('field')
alarmName = payload.get('alarmName')
valueTag = payload.get('valueTagPath')
myAlarm = self.view.params.alarmName
myTag = self.view.params.tagPath
if field in ('priority', 'trigger', 'mode'):
    if alarmName and str(alarmName) != str(myAlarm):
        return
    if valueTag and str(valueTag) != str(myTag):
        return
    if not alarmName:
        alarmName = myAlarm
    if not valueTag:
        valueTag = myTag
    if not valueTag or not alarmName:
        return
    try:
        viewName = payload.get('viewName') or self.view.id.split('@')[0]
        if field == 'priority':
            shared.AlarmConfig.applyOverride(valueTag, alarmName, priority=payload.get('value'), viewName=viewName)
        else:
            shared.AlarmConfig.applyOverride(valueTag, alarmName, mode=payload.get('value'), viewName=viewName)
    except:
# ... 19 more line(s): see the view.json
```

Project script calls: [shared.AlarmConfig.applyOverride](../../../../../../scripting/reference/modules/shared-alarmconfig.md), [shared.Alerts.confirmApplyWrite](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Audit.writeTag](../../../../../../scripting/reference/modules/shared-audit.md).

## Related Views

**Embedded in** (1): [01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./alarmconfiguration.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 4 | style class |
| `faceplate-alarm-field-label` | 3 | stylesheet |
| `faceplate-alarm-fields` | 1 | stylesheet |
| `faceplate-alarm-name` | 1 | style class |
| `faceplate-alarm-notes` | 1 | style class |
| `faceplate-alarm-row` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.Mode`, `.Priority`, `.TypeId`, `/Alarms/`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
