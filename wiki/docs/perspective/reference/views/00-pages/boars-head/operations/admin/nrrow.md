---
title: "NRRow"
sidebar_label: "NRRow"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/NRRow (Page piece (not routed)): 7 components, 7 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/NRRow", "NRRow"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/NRRow`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/NRRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/NRRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; NRRow |
| Root | `ia.container.flex`, height 48, width 700 |
| Size | 7 components, 7 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-24T17:40:25Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `desc` | `""` | input |
| `key` | `""` | input |
| `label` | `""` | input |
| `on` | `false` | input |
| `sub` | `""` | input |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x3, ia.display.icon x1.

```text
root  ia.container.flex  [2 bindings; 1 event]
  Check  ia.display.icon  [2 bindings]
  Text  ia.container.flex
    Line1  ia.container.flex
      Label  ia.display.label  [1 binding]
      Key  ia.display.label  [1 binding]
    Desc  ia.display.label  [1 binding]
```

## Bindings

7 bindings: expr 5, property 2.

**`root`**

- `meta.tooltip.enabled`: expression

```js
len(coalesce({view.params.desc}, '')) > 0
```


- `meta.tooltip.text`: expression

```js
{view.params.desc}
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


**`root/Text/Line1/Label`**

- `props.text`: property `view.params.label`

**`root/Text/Line1/Key`**

- `props.text`: property `view.params.key`

**`root/Text/Desc`**

- `props.text`: expression

```js
{view.params.sub} + if(len(trim(coalesce({view.params.desc}, ''))) > 0 && {view.params.desc} != {view.params.label}, ' · ' + {view.params.desc}, '')
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage('nrToggle', payload={'key': self.view.params.key}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/\_Admin/NRGroup](./nrgroup.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-desc` | 1 | style class |
| `admin-ico-on` | 1 | style class |
| `admin-key` | 1 | style class |
| `admin-row` | 1 | style class |
| `admin-row-label` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
