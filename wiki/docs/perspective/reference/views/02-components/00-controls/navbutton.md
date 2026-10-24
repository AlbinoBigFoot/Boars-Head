---
title: "NavButton"
sidebar_label: "NavButton"
description: "Perspective view 02_Components/00_Controls/NavButton (Reusable component): 5 components, 1 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/00_Controls/NavButton", "NavButton"]
---

:::note

:::


**Reusable component**: `02_Components/00_Controls/NavButton`.

| | |
|---|---|
| View path | `02_Components/00_Controls/NavButton` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/00_Controls/NavButton/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 00\_Controls &gt; NavButton |
| Root | `ia.container.flex`, height 36, width 168 |
| Size | 5 components, 1 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-30T04:55:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `label` | `"CONDENSER"` | input |
| `page` | `""` | input |
| `viewPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x1.

```text
root  ia.container.flex  [1 event]
  Shape  ia.container.flex
    Stroke  ia.container.flex
    Fill  ia.container.flex
    Label  ia.display.label  [1 binding]
```

## Bindings

1 bindings: property 1.

**`root/Shape/Label`**

- `props.text`: property `view.params.label`

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
page = str(self.view.params.page or '').strip()
viewPath = str(self.view.params.viewPath or '').strip()
if not page and not viewPath:
    return
data = {}
if page:
    data['action'] = 'page'
    data['page'] = page
if viewPath:
    data['viewPath'] = viewPath
Navigation.Nav.navigate(data)
```

## Related Views

**Embedded in** (2): [00\_Pages/Boars Head/Machine Room/Overview](../../00-pages/boars-head/machine-room/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../../00-pages/groveport/machine-room/utility/overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `nav-button` | 1 | stylesheet |
| `nav-button-fill` | 1 | stylesheet |
| `nav-button-label` | 1 | stylesheet |
| `nav-button-shape` | 1 | stylesheet |
| `nav-button-stroke` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
