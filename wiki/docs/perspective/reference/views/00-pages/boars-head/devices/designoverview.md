---
title: "DesignOverview"
sidebar_label: "DesignOverview"
description: "Perspective view 00_Pages/Boars Head/Devices/DesignOverview (Page piece (not routed)): 15 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Devices/DesignOverview", "DesignOverview"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Devices/DesignOverview`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Devices/DesignOverview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Devices/DesignOverview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Devices &gt; DesignOverview |
| Root | `ia.container.flex`, height 600, width 1200 |
| Size | 15 components, 2 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T15:50:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x8, ia.display.view x5, ia.display.label x1, ia.container.coord x1.

<details>
<summary>Component tree (15 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  DesignHint  ia.display.label
  DesignCanvas  ia.container.coord
    PipeCT_to_EV_H  ia.container.flex
    PipeCT_to_PMP_V  ia.container.flex
    PipePMP_to_EV_H  ia.container.flex
    PipePMP_to_EV_V  ia.container.flex
    PipeEV_to_COMP_H  ia.container.flex
    PipeCOMP_to_EFAN_H  ia.container.flex
    PipeCOMP_to_EFAN_V  ia.container.flex
    CT-01  ia.display.view  [view: 02_Components/01_Devices/CoolingTower]
    PMP-01  ia.display.view  [view: 02_Components/01_Devices/Pump]
    EV-01  ia.display.view  [view: 02_Components/01_Devices/Evaporator]
    COMP-01  ia.display.view  [view: 02_Components/01_Devices/Compressor]
    EFAN-01  ia.display.view  [view: 02_Components/01_Devices/ExhaustFan]
```

</details>

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

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (5): [02\_Components/01\_Devices/Compressor](../../../02-components/01-devices/compressor.md), [02\_Components/01\_Devices/CoolingTower](../../../02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](../../../02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](../../../02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Pump](../../../02-components/01-devices/pump.md)

**Opened or named by** (1): [00\_Pages/Boars Head/Devices/Overview](./overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `bg-component` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
