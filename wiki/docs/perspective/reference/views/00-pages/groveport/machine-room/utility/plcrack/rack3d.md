---
title: "Rack3d"
sidebar_label: "Rack3d"
description: "Perspective view 00_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d (Page): 6 components, 2 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d", "Rack3d", "/operations/plcs/:plc/3d"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Machine Room &gt; Utility &gt; PlcRack &gt; Rack3d |
| Routes | `/operations/plcs/:plc/3d` (PLC Rack 3D) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 6 components, 2 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `plc` | `"RCP1"` | input |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x2, ia.input.button x1, ia.display.iframe x1.

```text
root  ia.container.flex
  Header  ia.container.flex
    Title  ia.display.label  [1 binding]
    Note  ia.display.label
    View2d  ia.input.button  [1 event]
  Rack3d  ia.display.iframe  [1 binding]
```

## Bindings

2 bindings: expr 2.

**`root/Header/Title`**

- `props.text`: expression

```js
coalesce({view.params.plc}, 'RCP1') + ' PLC Rack · 3D'
```


**`root/Rack3d`**

- `props.src`: expression

```js
'/system/webdev/BH/rack3d/view?plc=' + coalesce({view.params.plc}, 'RCP1') + '&theme=' + if(indexOf(lower(coalesce({session.props.theme}, '')), 'dark') = 0, 'dark', 'light')
```


## Event Scripts And Handlers

- **`root/Header/View2d`** `component.onActionPerformed`, script action, scope `G`

```python
# UI navigation only: back to the 2D rack of this PLC
system.perspective.navigate('/operations/plcs/%s' % (self.view.params.plc or 'RCP1'))
```

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `bg-page` | 1 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `fs-12` | 1 | style class |
| `fs-18` | 1 | style class |
| `fw-400` | 1 | style class |
| `fw-700` | 1 | style class |
| `text-muted` | 1 | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
