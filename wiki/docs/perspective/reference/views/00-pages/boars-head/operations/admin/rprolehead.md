---
title: "RPRoleHead"
sidebar_label: "RPRoleHead"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/RPRoleHead (Page piece (not routed)): 6 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/RPRoleHead", "RPRoleHead"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/RPRoleHead`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/RPRoleHead` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/RPRoleHead/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; RPRoleHead |
| Root | `ia.container.flex`, height 48, width 100 |
| Size | 6 components, 6 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:47:30Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `base` | `""` | input |
| `full` | `false` | input |
| `name` | `""` | input |
| `users` | `0` | input |

## Component Tree

Component types: ia.container.flex x2, ia.display.icon x2, ia.display.label x2.

```text
root  ia.container.flex  [2 bindings]
  NameRow  ia.container.flex
    Lock  ia.display.icon  [1 binding]
    Link  ia.display.icon  [1 binding]
    Name  ia.display.label  [1 binding]
  Sub  ia.display.label  [1 binding]
```

## Bindings

6 bindings: expr 5, property 1.

**`root`**

- `meta.tooltip.enabled`: expression

```js
len(coalesce(if({view.params.full}, {view.params.name} + ' is a full permission role (_Config/Security/FullPermissionRoles): it always has every permission, so its column cannot be changed here.', if(len({view.params.base}) > 0, {view.params.name} + ' also gets every permission of ' + {view.params.base} + ' (_Config/Security/RoleInherits).', '')), '')) > 0
```


- `meta.tooltip.text`: expression

```js
if({view.params.full}, {view.params.name} + ' is a full permission role (_Config/Security/FullPermissionRoles): it always has every permission, so its column cannot be changed here.', if(len({view.params.base}) > 0, {view.params.name} + ' also gets every permission of ' + {view.params.base} + ' (_Config/Security/RoleInherits).', ''))
```


**`root/NameRow/Lock`**

- `position.display`: expression

```js
{view.params.full}
```


**`root/NameRow/Link`**

- `position.display`: expression

```js
len({view.params.base}) > 0
```


**`root/NameRow/Name`**

- `props.text`: property `view.params.name`

**`root/Sub`**

- `props.text`: expression

```js
if({view.params.full}, 'Always All', toStr({view.params.users}) + if({view.params.users} = 1, ' User', ' Users'))
```


## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/RolesPermissions](../rolespermissions.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-head-sub` | 1 | style class |
| `admin-ico-muted` | 2 | style class |
| `admin-role-name` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
