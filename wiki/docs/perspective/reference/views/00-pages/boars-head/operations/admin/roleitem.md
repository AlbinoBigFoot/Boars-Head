---
title: "RoleItem"
sidebar_label: "RoleItem"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/RoleItem (Page piece (not routed)): 10 components, 10 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/RoleItem", "RoleItem"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/RoleItem`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/RoleItem` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/RoleItem/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; RoleItem |
| Root | `ia.container.flex`, height 62, width 330 |
| Size | 10 components, 10 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:52:44Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `badge1` | `""` | input |
| `badge2` | `""` | input |
| `full` | `false` | input |
| `msg` | `"rpRoleSelect"` | input |
| `name` | `""` | input |
| `selected` | `false` | input |
| `sub` | `""` | input |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x4, ia.display.icon x2.

```text
root  ia.container.flex  [1 binding; 1 event]
  IconBox  ia.container.flex  [1 binding]
    Icon  ia.display.icon  [2 bindings]
  Text  ia.container.flex
    L1  ia.container.flex
      Name  ia.display.label  [1 binding]
      Badge1  ia.display.label  [2 bindings]
      Badge2  ia.display.label  [2 bindings]
    Sub  ia.display.label  [1 binding]
  Chevron  ia.display.icon
```

## Bindings

10 bindings: expr 6, property 4.

**`root`**

- `props.style.classes`: expression

```js
if({view.params.selected}, 'admin-list-item admin-list-item-selected', 'admin-list-item')
```


**`root/IconBox`**

- `props.style.classes`: expression

```js
if({view.params.selected}, 'admin-avatar admin-avatar-selected', 'admin-avatar')
```


**`root/IconBox/Icon`**

- `props.path`: expression

```js
if({view.params.full}, 'material/verified_user', 'material/assignment_ind')
```


- `props.style.classes`: expression

```js
if({view.params.selected}, 'admin-avatar-selected', 'admin-ico-on')
```


**`root/Text/L1/Name`**

- `props.text`: property `view.params.name`

**`root/Text/L1/Badge1`**

- `position.display`: expression

```js
len({view.params.badge1}) > 0
```


- `props.text`: property `view.params.badge1`

**`root/Text/L1/Badge2`**

- `position.display`: expression

```js
len({view.params.badge2}) > 0
```


- `props.text`: property `view.params.badge2`

**`root/Text/Sub`**

- `props.text`: property `view.params.sub`

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage(self.view.params.msg, payload={'name': self.view.params.name}, scope='page')
```

## Related Views

**Embedded in** (2): [00\_Pages/Boars Head/Operations/RolesPermissions](../rolespermissions.md), [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](../usermanagement/usermanagement.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-chip` | 2 | style class |
| `admin-desc` | 1 | style class |
| `admin-ico-muted` | 1 | style class |
| `admin-ico-on` | 1 | style class |
| `admin-item-title` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
