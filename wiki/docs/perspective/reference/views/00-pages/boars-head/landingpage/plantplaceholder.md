---
title: "PlantPlaceholder"
sidebar_label: "PlantPlaceholder"
description: "Perspective view 00_Pages/Boars Head/LandingPage/PlantPlaceholder (Page): 3 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/LandingPage/PlantPlaceholder", "PlantPlaceholder", "/plants/forrest-city", "/plants/holland", "/plants/new-castle", "/plants/petersburg"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/LandingPage/PlantPlaceholder`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/LandingPage/PlantPlaceholder` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/LandingPage/PlantPlaceholder/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; LandingPage &gt; PlantPlaceholder |
| Routes | `/plants/forrest-city` (Forrest City)<br/>`/plants/holland` (Holland)<br/>`/plants/new-castle` (New Castle)<br/>`/plants/petersburg` (Petersburg) |
| Root | `ia.container.flex`, height 400, width 800 |
| Size | 3 components, 3 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T19:10:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `plantName` | `""` | input |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1.

```text
root  ia.container.flex  [2 bindings]
  Title  ia.display.label  [1 binding]
  Body  ia.display.label
```

## Bindings

3 bindings: expr-struct 3.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
tagPath: "No TagPath: "
```

waitOnAll: `True`

Transform 1, script:

```python
tagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]
items = [{
    "text": "Ticket Logger",
    "icon": {"path": "material/info", "color": "--neutral-80", "style": {}},
    "style": {"classes": "bg-component Fonts/Value", "height": 24, "width": 120},
    "type": "message",
    "children": [],
    "link": {"url": "", "target": "self"},
    "method": {"name": "", "params": {}},
    "message": {
        "type": "ticketLog",
        "payload": {"tagPath": tagPath, "viewName": self.view.id.split('@')[0], 'sender': self.view.id},
        "scope": "page"
    }
}]
return items
```


- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Title`**

- `props.text`: structured expression (expr-struct), then script transform

```js
name: {view.params.plantName}
path: {page.props.path}
```

waitOnAll: `True`

Transform 1, script:

```python
name = value['name'] or ''
if name:
    return str(name)
path = str(value['path'] or '')
return path.split('/')[-1].replace('-', ' ').title() or 'Plant'
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `bg-page` | 1 | style class |
| `fs-14` | 1 | style class |
| `fs-22` | 1 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
