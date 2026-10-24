---
title: "User"
sidebar_label: "User"
description: "Perspective view 00_Pages/00_Docked/_Assets/User (Asset (embedded piece)): 3 components, 3 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/User", "User"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/User`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/User` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/User/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; User |
| Root | `ia.container.flex`, height 36, width 120 |
| Size | 3 components, 3 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T07:26:16Z by the Designer |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1, ia.display.label x1.

```text
root  ia.container.flex  [2 bindings; 1 event]
  Icon  ia.display.icon
  UserLabel  ia.display.label  [1 binding]
```

## Bindings

3 bindings: expr-struct 2, property 1.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/UserLabel`**

- `props.text`: property `session.props.auth`, then expression transform

Transform 1, expression:

```js
if({value}['authenticated'],
	if({value}['user']['firstName'] != None,
		{value}['user']['firstName'],
		{value}['user']['userName']
	),
	'Log In'
)
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, popup action, scope `C`: toggle popup `userRolesLogin`, view [00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./userrolesandlogin.md)

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [00\_Pages/00\_Docked/\_Assets/UserRoles&Login](./userrolesandlogin.md)

**Embedded in** (2): [00\_Pages/00\_Docked/Header](../header.md), [00\_Pages/00\_Docked/TempNav](../tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `account-chip` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `fs-13` | 1 | style class |
| `header-icon` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
