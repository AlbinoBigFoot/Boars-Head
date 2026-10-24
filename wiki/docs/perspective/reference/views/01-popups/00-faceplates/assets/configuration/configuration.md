---
title: "Configuration"
sidebar_label: "Configuration"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Configuration/Configuration (Asset (embedded piece)): 3 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Configuration/Configuration", "Configuration"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Configuration/Configuration`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Configuration/Configuration` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Configuration/Configuration/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Configuration &gt; Configuration |
| Root | `ia.container.flex`, height 300, width 400 |
| Size | 3 components, 6 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T20:12:34Z by the Designer |

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

Component types: ia.container.flex x1, ia.display.label x1, ia.display.flex-repeater x1.

```text
root  ia.container.flex  [2 bindings]
  EmptyState  ia.display.label  [1 binding]
  FlexRepeater  ia.display.flex-repeater  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow]
```

## Bindings

6 bindings: expr-struct 4, expr 2.

**`(view)`**

- `custom.tags`: structured expression (expr-struct), then script transform

```js
hiddenTags: {view.params.hiddenTags}
tagPath: {view.params.tagPath}
```

waitOnAll: `True`

Transform 1, script:

```python
hiddenTagsInput = value.get('hiddenTags', '')
hidden_set = set()
try:
    text = str(hiddenTagsInput or '')
    if text:
        text = text.replace(';', ',')
        for item in text.split(','):
            item = item.strip()
            if item:
                hidden_set.add(item)
except Exception:
    pass
# Always hide alarm-metric helpers (not operator config).
hidden_set.add('_Alarms/')
hidden_set.add('Alarm Metrics/')

def isHidden(fullPath):
    if not hidden_set:
        return False
    stripped = fullPath.split(']', 1)[-1] if ']' in fullPath else fullPath
    norm = stripped.replace(chr(92), '/')
    if fullPath in hidden_set or stripped in hidden_set or norm in hidden_set:
        return True
    norm_slash = '/' + norm.strip('/') + '/'
    for h in hidden_set:
        hh = str(h).replace(chr(92), '/')
        if hh.endswith('/'):
            seg = hh.strip('/')
            if not seg:
                continue
            if ('/' + seg + '/') in norm_slash:
                return True
            if norm.strip('/') == seg or norm.strip('/').startswith(seg + '/'):
                return True
        else:
            if norm.endswith('/' + hh) or norm.split('/')[-1] == hh:
                return True
    return False

# Match Faceplate tagFlags: writable + no alarms in getConfiguration.
# ... 36 more line(s): see the view.json
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


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../common-patterns.md#pattern-1).

**`root/EmptyState`**

- `position.display`: expression

```js
if(coalesce(try(isGood({view.custom.tags}), false), false), len({view.custom.tags}) = 0, false)
```


**`root/FlexRepeater`**

- `props.instances`: structured expression (expr-struct), then script transform

```js
tags: {view.custom.tags}
```

waitOnAll: `True`

Transform 1, script:

```python
instances = []
for tag in value['tags']:
    tagPath = tag
    instance = {
                "instanceStyle": {
                    "classes":""
                },
                "instancePosition": {},
                "highlightRow": len(instances) % 2 == 1,  # True for odd indices (every other row)
                "tagPath": tag
                }
    instances.append(instance)
return instances
```


- `position.display`: expression

```js
if(coalesce(try(isGood({view.custom.tags}), false), false), len({view.custom.tags}) > 0, false)
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigurationRow](./configurationrow.md) (flex repeater)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `faceplate-config-empty` | 1 | style class |
| `faceplate-section` | 1 | style class |
| `text-muted` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
