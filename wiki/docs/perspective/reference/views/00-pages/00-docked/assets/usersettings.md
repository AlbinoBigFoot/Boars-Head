---
title: "UserSettings"
sidebar_label: "UserSettings"
description: "Perspective view 00_Pages/00_Docked/_Assets/UserSettings (Asset (embedded piece)): 2 components, 2 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/UserSettings", "UserSettings"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/UserSettings`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/UserSettings` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/UserSettings/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; UserSettings |
| Root | `ia.container.flex`, height 36, width 36 |
| Size | 2 components, 2 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T07:27:46Z by the Designer |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1.

```text
root  ia.container.flex  [2 bindings; 1 event]
  Icon  ia.display.icon
```

## Bindings

2 bindings: expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

## Event Scripts And Handlers

- **`root`** `dom.onClick`, popup action, scope `C`: toggle popup `changeTheme`, view [00\_Pages/00\_Docked/\_Assets/ChangeTheme](./changetheme.md)

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [00\_Pages/00\_Docked/\_Assets/ChangeTheme](./changetheme.md)

**Embedded in** (1): [00\_Pages/00\_Docked/Header](../header.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `account-settings` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `header-icon` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
