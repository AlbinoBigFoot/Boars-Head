---
title: "Menu"
sidebar_label: "Menu"
description: "Perspective view 01_Popups/00_Faceplates/Alerts/Menu (Popup / faceplate): 2 components, 4 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Alerts/Menu", "Menu"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Alerts/Menu`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Alerts/Menu` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/Menu/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Alerts &gt; Menu |
| Root | `ia.container.flex`, no default size |
| Size | 2 components, 4 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-24T18:35:03Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `classes` | `"container-item Fonts/Header"` | input |
| `cursor` | `"pointer"` | input |
| `fontWeight` | `"normal"` | input |
| `name` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1.

```text
root  ia.container.flex
  Label  ia.display.label  [4 bindings]
```

## Bindings

4 bindings: property 4.

**`root/Label`**

- `props.style.classes`: property `view.params.classes`

- `props.style.cursor`: property `view.params.cursor`

- `props.style.fontWeight`: property `view.params.fontWeight`

- `props.text`: property `view.params.name`

## Related Views

**Embedded in** (1): [01\_Popups/00\_Faceplates/Alerts/ContextMenu](./contextmenu.md)
