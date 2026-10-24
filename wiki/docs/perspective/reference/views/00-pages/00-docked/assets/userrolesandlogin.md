---
title: "UserRoles&Login"
sidebar_label: "UserRoles&Login"
description: "Perspective view 00_Pages/00_Docked/_Assets/UserRoles&Login (Asset (embedded piece)): 14 components, 11 bindings, 2 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/UserRoles&Login", "UserRoles&Login"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/UserRoles&Login`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/UserRoles&Login` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/UserRoles&Login/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; UserRoles&Login |
| Root | `ia.container.flex`, height 240, width 220 |
| Size | 14 components, 11 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-25T04:25:00Z by the Designer |

## Component Tree

Component types: ia.display.label x7, ia.container.flex x4, ia.input.button x2, ia.display.icon x1.

<details>
<summary>Component tree (14 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  User  ia.container.flex
    Label  ia.display.label
    Value  ia.display.label  [1 binding]
  Roles  ia.container.flex
    Label  ia.display.label
    RolesValue  ia.display.label  [1 binding]
  Access  ia.container.flex
    Label  ia.display.label
    AccessIcon  ia.display.icon  [2 bindings]
    AccessValue  ia.display.label  [2 bindings]
    AccessGuest  ia.display.label  [1 binding]
  LoginLogOut  ia.input.button  [1 binding; 1 event]
  SwitchUser  ia.input.button  [1 binding; 1 event]
```

</details>

## Bindings

11 bindings: property 9, expr-struct 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/User/Value`**

- `props.text`: property `session.props.auth`, then expression transform

Transform 1, expression:

```js
if({value}['authenticated'],
	if({value}['user']['firstName'] != None,
		if({value}['user']['lastName'] != None,
			{value}['user']['firstName'] + ' ' + {value}['user']['lastName'],
			{value}['user']['firstName']
		),
		{value}['user']['userName']
	),
	'Not logged in'
)
```


**`root/Roles/RolesValue`**

- `props.text`: property `session.props.auth.user.roles`, then script transform

Transform 1, script:

```python
if value is None or len(value) == 0:
    return '(none)'
return ', '.join([str(r) for r in value])
```


**`root/Access/AccessIcon`**

- `meta.visible`: property `session.props.auth.authenticated`

- `props.path`: property `session.custom.ReadOnly`, then expression transform

Transform 1, expression:

```js
if({value}, 'material/lock', 'material/lock_open')
```


**`root/Access/AccessValue`**

- `meta.visible`: property `session.props.auth.authenticated`

- `props.text`: property `session.custom.ReadOnly`, then expression transform

Transform 1, expression:

```js
if({value}, 'Read', 'Write')
```


**`root/Access/AccessGuest`**

- `meta.visible`: property `session.props.auth.authenticated`, then expression transform

Transform 1, expression:

```js
!{value}
```


**`root/LoginLogOut`**

- `props.text`: property `session.props.auth.authenticated`, then expression transform

Transform 1, expression:

```js
if({value}, 'Log Out', 'Log In')
```


**`root/SwitchUser`**

- `meta.visible`: property `session.props.auth.authenticated`

## Event Scripts And Handlers

- **`root/LoginLogOut`** `component.onActionPerformed`, script action, scope `G`

```python
if self.session.props.auth.authenticated:
    system.perspective.logout()
else:
    system.perspective.login()
```

- **`root/SwitchUser`** `component.onActionPerformed`, script action, scope `G`

```python
# Force IdP login UI so operators can switch accounts without a full logout first
system.perspective.login(forceAuth=True)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [00\_Pages/00\_Docked/\_Assets/User](./user.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 2 | style class |
| `Fonts/Label` | 3 | style class |
| `Fonts/Value` | 4 | style class |
| `account-popup` | 1 | stylesheet |
| `bg-component` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `container-button` | 2 | style class |
| `container-card` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
