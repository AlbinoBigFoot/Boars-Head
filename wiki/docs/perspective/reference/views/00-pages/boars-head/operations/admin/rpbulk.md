---
title: "RPBulk"
sidebar_label: "RPBulk"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/RPBulk (Page piece (not routed)): 3 components, 7 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/RPBulk", "RPBulk"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/RPBulk`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/RPBulk` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/RPBulk/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; RPBulk |
| Root | `ia.container.flex`, height 44, width 100 |
| Size | 3 components, 7 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:47:30Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `canEdit` | `false` | input |
| `cat` | `""` | input |
| `role` | `""` | input |
| `state` | `"none"` | input |
| `text` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.icon x1, ia.display.label x1.

```text
root  ia.container.flex  [3 bindings; 1 event]
  Icon  ia.display.icon  [2 bindings]
  Count  ia.display.label  [2 bindings]
```

## Bindings

7 bindings: expr 6, property 1.

**`root`**

- `meta.tooltip.enabled`: expression

```js
len(coalesce(if({view.params.state} = 'locked' || !{view.params.canEdit}, '', if({view.params.state} = 'all', 'Revoke All In ' + {view.params.cat} + ' From ' + {view.params.role}, 'Grant All In ' + {view.params.cat} + ' To ' + {view.params.role})), '')) > 0
```


- `meta.tooltip.text`: expression

```js
if({view.params.state} = 'locked' || !{view.params.canEdit}, '', if({view.params.state} = 'all', 'Revoke All In ' + {view.params.cat} + ' From ' + {view.params.role}, 'Grant All In ' + {view.params.cat} + ' To ' + {view.params.role}))
```


- `props.style.classes`: expression

```js
if({view.params.state} != 'locked' && {view.params.canEdit}, 'admin-cell admin-cell-click', 'admin-cell')
```


**`root/Icon`**

- `props.path`: expression

```js
case({view.params.state}, 'all', 'material/check_box', 'some', 'material/indeterminate_check_box', 'locked', 'material/lock', 'material/check_box_outline_blank')
```


- `props.style.classes`: expression

```js
case({view.params.state}, 'all', 'admin-ico-on', 'some', 'admin-ico-on', 'none', 'admin-ico-off', 'admin-ico-muted')
```


**`root/Count`**

- `props.style.classes`: expression

```js
if({view.params.state} = 'none', 'admin-cell-text admin-cell-text-muted', 'admin-cell-text')
```


- `props.text`: property `view.params.text`

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
p = self.view.params
if p.state != 'locked' and p.canEdit:
    system.perspective.sendMessage('rpBulk', payload={'cat': p.cat, 'role': p.role, 'grant': p.state != 'all'}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./rpgroup.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-cell-text` | 1 | style class |
| `admin-ico-on` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
