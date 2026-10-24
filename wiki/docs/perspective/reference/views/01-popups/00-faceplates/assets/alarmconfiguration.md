---
title: "AlarmConfiguration"
sidebar_label: "AlarmConfiguration"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/AlarmConfiguration (Asset (embedded piece)): 4 components, 7 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/AlarmConfiguration", "AlarmConfiguration"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/AlarmConfiguration`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/AlarmConfiguration` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/AlarmConfiguration/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; AlarmConfiguration |
| Root | `ia.container.flex`, height 320, width 500 |
| Size | 4 components, 7 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T18:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `hiddenTags` | `""` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `tags` | `[]` | bound (expr-struct) |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1, ia.display.flex-repeater x1.

```text
root  ia.container.flex  [2 bindings]
  AcTitle  ia.display.label  [1 binding]
  AcEmpty  ia.display.label  [1 binding]
  FlexRepeater  ia.display.flex-repeater  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow]
```

## Bindings

7 bindings: expr-struct 7.

**`(view)`**

- `custom.tags`: structured expression (expr-struct), then script transform

```js
hiddenTags: {view.params.hiddenTags}
tagPath: {view.params.tagPath}
```

waitOnAll: `True`

Transform 1, script:

```python
hiddenTagsInput = value.get('hiddenTags', '') if hasattr(value, 'get') else ''
tagPath = value.get('tagPath', '') if hasattr(value, 'get') else ''
try:
    return shared.AlarmConfig.listAlarms(tagPath, hiddenTagsInput)
except Exception:
    return []
```


**`root`**

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

**`root/AcTitle`**

- `props.text`: structured expression (expr-struct), then script transform

```js
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, script:

```python
tags = value.get('tags') or []
n = len(tags)
return 'Alarm configuration (%d)' % n
```


**`root/AcEmpty`**

- `position.display`: structured expression (expr-struct), then script transform

```js
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, script:

```python
tags = value.get('tags') or []
return len(tags) == 0
```


**`root/FlexRepeater`**

- `position.display`: structured expression (expr-struct), then script transform

```js
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, script:

```python
tags = value.get('tags') or []
return len(tags) > 0
```


- `props.instances`: structured expression (expr-struct), then script transform

```js
alarms: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, script:

```python
instances = []
alarms = value.get('alarms') or []
for i, item in enumerate(alarms):
    instances.append({
        'instanceStyle': {'classes': ''},
        'instancePosition': {'basis': '120px', 'grow': 0, 'shrink': 0},
        'highlightRow': i % 2 == 1,
        'tagPath': item.get('tagPath', ''),
        'instancePath': item.get('instancePath', ''),
        'alarmName': item.get('alarmName', ''),
        'label': item.get('label', ''),
        'notes': item.get('notes', ''),
        'isDigital': bool(item.get('isDigital')),
        'hasSetpoint': bool(item.get('hasSetpoint'))
    })
return instances
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.AlarmConfig.listAlarms](../../../../../../scripting/reference/modules/shared-alarmconfig.md), [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/AlarmConfigurationRow](./alarmconfigurationrow.md) (flex repeater)

**Embedded in** (1): [01\_Popups/00\_Faceplates/DiscreteInput](../discreteinput.md)

**Opened or named by** (2): [01\_Popups/00\_Faceplates/Faceplate](../faceplate.md), [01\_Popups/00\_Faceplates/TankOverview](../tankoverview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `faceplate-alarm-list` | 1 | stylesheet |
| `faceplate-section-title` | 1 | style class |
| `faceplate-stub` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
