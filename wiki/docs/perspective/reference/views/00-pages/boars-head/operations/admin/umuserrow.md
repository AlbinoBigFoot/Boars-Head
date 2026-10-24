---
title: "UMUserRow"
sidebar_label: "UMUserRow"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/UMUserRow (Page piece (not routed)): 7 components, 9 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/UMUserRow", "UMUserRow"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/UMUserRow`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/UMUserRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/UMUserRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; UMUserRow |
| Root | `ia.container.flex`, height 56, width 360 |
| Size | 7 components, 9 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:47:30Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `display` | `""` | input |
| `initials` | `""` | input |
| `more` | `""` | input |
| `role1` | `""` | input |
| `selected` | `false` | input |
| `username` | `""` | input |

## Component Tree

Component types: ia.display.label x5, ia.container.flex x2.

```text
root  ia.container.flex  [1 binding; 1 event]
  Avatar  ia.display.label  [2 bindings]
  Text  ia.container.flex
    Name  ia.display.label  [1 binding]
    User  ia.display.label  [1 binding]
  Role  ia.display.label  [2 bindings]
  More  ia.display.label  [2 bindings]
```

## Bindings

9 bindings: property 5, expr 4.

**`root`**

- `props.style.classes`: expression

```js
if({view.params.selected}, 'admin-list-item admin-list-item-selected', 'admin-list-item')
```


**`root/Avatar`**

- `props.style.classes`: expression

```js
if({view.params.selected}, 'admin-avatar admin-avatar-selected', 'admin-avatar')
```


- `props.text`: property `view.params.initials`

**`root/Text/Name`**

- `props.text`: property `view.params.display`

**`root/Text/User`**

- `props.text`: property `view.params.username`

**`root/Role`**

- `position.display`: expression

```js
len({view.params.role1}) > 0
```


- `props.text`: property `view.params.role1`

**`root/More`**

- `position.display`: expression

```js
len({view.params.more}) > 0
```


- `props.text`: property `view.params.more`

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage('umSelect', payload={'name': self.view.params.username}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](../usermanagement/usermanagement.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-avatar` | 1 | style class |
| `admin-chip` | 2 | style class |
| `admin-desc` | 1 | style class |
| `admin-item-title` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
