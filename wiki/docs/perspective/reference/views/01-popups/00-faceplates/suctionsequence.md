---
title: "SuctionSequence"
sidebar_label: "SuctionSequence"
description: "Perspective view 01_Popups/00_Faceplates/SuctionSequence (Popup / faceplate): 5 components, 4 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/SuctionSequence", "SuctionSequence"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/SuctionSequence`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/SuctionSequence` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/SuctionSequence/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; SuctionSequence |
| Root | `ia.container.flex`, height 700, width 820 |
| Size | 5 components, 4 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-25T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `popupId` | `""` | input |
| `tagPath` | `""` | input |
| `title` | `""` | input |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x1, ia.display.icon x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    Title  ia.display.label  [1 binding]
    Close  ia.display.icon  [1 event]
  Body  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls]
```

## Bindings

4 bindings: expr 3, property 1.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/Header/Title`**

- `props.text`: expression

```js
coalesce({view.params.title}, '')
```


**`root/Body`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

## Event Scripts And Handlers

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
pid = str(self.view.params.popupId or '').strip()
if pid:
    system.perspective.closePopup(pid)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./assets/suctionsequence/controls.md)

**Named in project scripts**: [Navigation.Faceplate](../../../../../scripting/reference/modules/navigation-faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 1 | style class |
| `bg-component` | 1 | stylesheet |
| `bg-header` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `container-icon` | 1 | stylesheet |
| `faceplate` | 1 | stylesheet |
| `faceplate-close` | 1 | stylesheet |
| `faceplate-header` | 1 | stylesheet |
| `faceplate-title` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
