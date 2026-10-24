---
title: "CopyPath"
sidebar_label: "CopyPath"
description: "Perspective view 01_Popups/TrendContext/CopyPath (Popup / faceplate): 9 components, 2 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/TrendContext/CopyPath", "CopyPath"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/TrendContext/CopyPath`.

| | |
|---|---|
| View path | `01_Popups/TrendContext/CopyPath` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/TrendContext/CopyPath/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; TrendContext &gt; CopyPath |
| Root | `ia.container.flex`, width 520, height 150 |
| Size | 9 components, 2 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x3, ia.display.icon x1, ia.display.markdown x1.

```text
root  ia.container.flex
  Header  ia.container.flex
    Title  ia.display.label
    Close  ia.container.flex  [1 event]
      Icon  ia.display.icon
  Path  ia.display.label  [1 binding]
  Actions  ia.container.flex
    Copy  ia.display.markdown  [1 binding]
    Hint  ia.display.label
```

## Bindings

2 bindings: property 2.

**`root/Path`**

- `props.text`: property `view.params.tagPath`

**`root/Actions/Copy`**

- `props.source`: property `view.params.tagPath`, then script transform

Transform 1, script:

```python
return shared.TrendContext.copy_markdown(value)
```


## Event Scripts And Handlers

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
system.perspective.closePopup('TrendCopyPath')
```

Project script calls: [shared.TrendContext.copy\_markdown](../../../../../scripting/reference/modules/shared-trendcontext.md).

## Related Views

**Named in project scripts**: [shared.TrendContext](../../../../../scripting/reference/modules/shared-trendcontext.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `trend-ctx-close-btn` | 1 | stylesheet |
| `trend-ctx-copy` | 1 | stylesheet |
| `trend-ctx-copy-card` | 1 | stylesheet |
| `trend-ctx-copy-path` | 1 | stylesheet |
| `trend-ctx-icon` | 1 | stylesheet |
| `trend-ctx-menu` | 1 | stylesheet |
| `trend-ctx-path` | 1 | stylesheet |
| `trend-ctx-title` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
