---
title: "Alarms"
sidebar_label: "Alarms"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Alarms (Asset (embedded piece)): 2 components, 4 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Alarms", "Alarms"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Alarms`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Alarms` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Alarms/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Alarms |
| Root | `ia.container.flex`, height 300, width 400 |
| Size | 2 components, 4 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T18:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.alarmstatustable x1.

```text
root  ia.container.flex  [2 bindings]
  AlarmStatusTable  ia.display.alarmstatustable  [2 bindings]
```

## Bindings

4 bindings: expr-struct 2, expr 2.

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

**`root/AlarmStatusTable`**

- `props.filters.active.conditions.source`: expression

```js
if({view.params.tagPath} = '' || lastIndexOf({view.params.tagPath}, ']') < 0,
  'prov:none:/tag:__unbound__',
  try(
'prov:' + subString({view.params.tagPath}, 1, lastIndexOf({view.params.tagPath}, ']')) +
':/tag:' + subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, ']') + 1) + '*',
'prov:none:/tag:__unbound__'))
```


- `props.enableAcknowledge`: expression

```js
coalesce({session.custom.Permissions.AlarmSummary.Acknowledge}, false)
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (4): [01\_Popups/00\_Faceplates/DiscreteInput](../discreteinput.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./valve/alarms.md)

**Opened or named by** (2): [01\_Popups/00\_Faceplates/Faceplate](../faceplate.md), [01\_Popups/00\_Faceplates/TankOverview](../tankoverview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
