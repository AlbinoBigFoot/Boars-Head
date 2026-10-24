---
title: "UMRoleOption"
sidebar_label: "UMRoleOption"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/UMRoleOption (Page piece (not routed)): 5 components, 5 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/UMRoleOption", "UMRoleOption"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/UMRoleOption`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/UMRoleOption` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/UMRoleOption/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; UMRoleOption |
| Root | `ia.container.flex`, height 54, width 178 |
| Size | 5 components, 5 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:47:30Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `canEdit` | `false` | input |
| `name` | `""` | input |
| `on` | `false` | input |
| `sub` | `""` | input |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x2, ia.display.icon x1.

```text
root  ia.container.flex  [1 binding; 1 event]
  Check  ia.display.icon  [2 bindings]
  Text  ia.container.flex
    Name  ia.display.label  [1 binding]
    Sub  ia.display.label  [1 binding]
```

## Bindings

5 bindings: expr 3, property 2.

**`root`**

- `props.style.classes`: expression

```js
if({view.params.on}, 'admin-option admin-option-on', 'admin-option')
```


**`root/Check`**

- `props.path`: expression

```js
if({view.params.on}, 'material/check_box', 'material/check_box_outline_blank')
```


- `props.style.classes`: expression

```js
if({view.params.on}, 'admin-ico-on', 'admin-ico-off')
```


**`root/Text/Name`**

- `props.text`: property `view.params.name`

**`root/Text/Sub`**

- `props.text`: property `view.params.sub`

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
if self.view.params.canEdit:
    system.perspective.sendMessage('umRoleToggle', payload={'name': self.view.params.name}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](../usermanagement/usermanagement.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-desc` | 1 | style class |
| `admin-ico-off` | 1 | style class |
| `admin-row-label` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
