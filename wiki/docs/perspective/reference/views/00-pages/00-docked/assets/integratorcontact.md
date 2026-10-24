---
title: "IntegratorContact"
sidebar_label: "IntegratorContact"
description: "Perspective view 00_Pages/00_Docked/_Assets/IntegratorContact (Asset (embedded piece)): 17 components, 2 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/IntegratorContact", "IntegratorContact"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/IntegratorContact`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/IntegratorContact` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/IntegratorContact/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; IntegratorContact |
| Root | `ia.container.flex`, width 300, height 212 |
| Size | 17 components, 2 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-22T16:26:11Z by the Designer |

## Component Tree

Component types: ia.display.label x8, ia.container.flex x7, ia.display.view x1, ia.display.icon x1.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Top  ia.container.flex
    Logo  ia.display.view  [view: 00_Pages/00_Docked/_Assets/IntegratorLogo]
    Spacer  ia.container.flex
    Close  ia.display.icon  [1 event]
  Tagline  ia.display.label
  Rule  ia.container.flex
  Name  ia.display.label
  Phone  ia.container.flex
    Label  ia.display.label
    Value  ia.display.label
  Email  ia.container.flex
    Label  ia.display.label
    Value  ia.display.label
  Web  ia.container.flex
    Label  ia.display.label
    Value  ia.display.label
```

</details>

## Bindings

2 bindings: expr 2.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

## Event Scripts And Handlers

- **`root/Top/Close`** `dom.onClick`, popup action, scope `C`: close popup `integratorContact`, view [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./integratorcontact.md)

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [00\_Pages/00\_Docked/\_Assets/IntegratorLogo](./integratorlogo.md)

**Opened or named by** (1): [00\_Pages/00\_Docked/Header](../header.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 4 | style class |
| `Fonts/Value` | 4 | style class |
| `account-popup` | 1 | stylesheet |
| `bg-component` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `fw-600` | 1 | style class |
| `integrator-contact` | 1 | no rule found |
| `integrator-divider` | 1 | stylesheet |
| `text-muted` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
