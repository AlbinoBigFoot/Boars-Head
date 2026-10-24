---
title: "RPCell"
sidebar_label: "RPCell"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/RPCell (Page piece (not routed)): 5 components, 9 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/RPCell", "RPCell"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/RPCell`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/RPCell` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/RPCell/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; RPCell |
| Root | `ia.container.flex`, height 47, width 100 |
| Size | 5 components, 9 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:47:30Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `canEdit` | `false` | input |
| `key` | `""` | input |
| `role` | `""` | input |
| `state` | `"off"` | input |
| `tip` | `""` | input |

## Component Tree

Component types: ia.container.flex x2, ia.display.icon x2, ia.display.label x1.

```text
root  ia.container.flex  [3 bindings; 1 event]
  Icon  ia.display.icon  [3 bindings]
  All  ia.display.label  [1 binding]
  Link  ia.display.icon  [1 binding]
  Dot  ia.container.flex  [1 binding]
```

## Bindings

9 bindings: expr 9.

**`root`**

- `meta.tooltip.enabled`: expression

```js
len(coalesce({view.params.tip}, '')) > 0
```


- `meta.tooltip.text`: expression

```js
{view.params.tip}
```


- `props.style.classes`: expression

```js
'admin-cell' + if({view.params.state} = 'changedOn' || {view.params.state} = 'changedOff', ' admin-cell-changed', '') + if({view.params.canEdit} && ({view.params.state} = 'on' || {view.params.state} = 'off' || {view.params.state} = 'changedOn' || {view.params.state} = 'changedOff'), ' admin-cell-click', '')
```


**`root/Icon`**

- `position.basis`: expression

```js
if({view.params.state} = 'locked', '15px', '20px')
```


- `props.path`: expression

```js
case({view.params.state}, 'locked', 'material/lock', 'on', 'material/check_box', 'changedOn', 'material/check_box', 'inherited', 'material/check_box', 'roOn', 'material/check_box', 'material/check_box_outline_blank')
```


- `props.style.classes`: expression

```js
case({view.params.state}, 'on', 'admin-ico-on', 'changedOn', 'admin-ico-on', 'changedOff', 'admin-ico-on', 'off', 'admin-ico-off', 'roOff', 'admin-ico-off', 'admin-ico-muted')
```


**`root/All`**

- `position.display`: expression

```js
{view.params.state} = 'locked'
```


**`root/Link`**

- `position.display`: expression

```js
{view.params.state} = 'inherited'
```


**`root/Dot`**

- `position.display`: expression

```js
{view.params.state} = 'changedOn' || {view.params.state} = 'changedOff'
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
if self.view.params.state in ('on', 'off', 'changedOn', 'changedOff') and self.view.params.canEdit:
    system.perspective.sendMessage('rpToggle', payload={'key': self.view.params.key, 'role': self.view.params.role}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/\_Admin/RPRow](./rprow.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-cell-text` | 1 | style class |
| `admin-cell-text-muted` | 1 | style class |
| `admin-dot` | 1 | style class |
| `admin-ico-muted` | 1 | style class |
| `admin-ico-off` | 1 | style class |
| `admin-cell` | bound | style class |
| `admin-cell-changed` | bound | style class |
| `admin-ico-on` | bound | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
