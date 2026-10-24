---
title: "Remote"
sidebar_label: "Remote"
description: "Perspective view 03_Elements/01_Status/Icons/Remote (Element (small reusable part)): 2 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/Icons/Remote", "Remote"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/Icons/Remote`.

| | |
|---|---|
| View path | `03_Elements/01_Status/Icons/Remote` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/Icons/Remote/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; Icons &gt; Remote |
| Root | `ia.container.flex`, height 22, width 22 |
| Size | 2 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-02T02:30:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [2 bindings]
  SVG  ia.shapes.svg
```

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
tagPath: "No TagPath: "
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


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [01\_Popups/00\_Faceplates/\_Assets/Modes](../../../01-popups/00-faceplates/assets/modes.md)
