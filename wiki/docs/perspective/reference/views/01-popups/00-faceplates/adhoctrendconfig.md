---
title: "AdhocTrendConfig"
sidebar_label: "AdhocTrendConfig"
description: "Perspective view 01_Popups/00_Faceplates/AdhocTrendConfig (Popup / faceplate): 7 components, 2 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/AdhocTrendConfig", "AdhocTrendConfig"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/AdhocTrendConfig`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/AdhocTrendConfig` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/AdhocTrendConfig/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; AdhocTrendConfig |
| Root | `ia.container.flex`, height 360, width 340 |
| Size | 7 components, 2 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T06:05:00Z by the Designer |

## Component Tree

Component types: ia.container.flex x3, ia.display.icon x2, ia.display.label x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    TitleRow  ia.container.flex
      Icon  ia.display.icon
      Title  ia.display.label
    Close  ia.display.icon  [1 event]
  ToolBar  ia.display.view  [view: 98_Configuration/AdhocTrend/_Assets/ToolBar]
```

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
system.perspective.closePopup('AdhocTrendConfig')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [98\_Configuration/AdhocTrend/\_Assets/ToolBar](../../98-configuration/adhoctrend/assets/toolbar.md)

**Named in project scripts**: [shared.Alerts](../../../../../scripting/reference/modules/shared-alerts.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 1 | style class |
| `adhoc-trend-config-faceplate` | 1 | stylesheet |
| `adhoc-trend-config-faceplate-close` | 1 | stylesheet |
| `adhoc-trend-config-faceplate-header` | 1 | stylesheet |
| `bg-container` | 1 | stylesheet |
| `color-icon` | 2 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `container-header` | 1 | stylesheet |
| `container-icon` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
