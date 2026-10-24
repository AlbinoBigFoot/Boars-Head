---
title: "RPRow"
sidebar_label: "RPRow"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/RPRow (Page piece (not routed)): 11 components, 11 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/RPRow", "RPRow"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/RPRow`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/RPRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/RPRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; RPRow |
| Root | `ia.container.flex`, height 48, width 900 |
| Size | 11 components, 11 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:47:30Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `cells` | `[]` | input |
| `desc` | `""` | input |
| `key` | `""` | input |
| `kind` | `"row"` | input |
| `label` | `""` | input |
| `n` | `0` | input |
| `rw` | `100` | input |
| `title` | `""` | input |

## Component Tree

Component types: ia.container.flex x5, ia.display.label x5, ia.display.flex-repeater x1.

```text
root  ia.container.flex
  Sub  ia.container.flex  [1 binding]
    Title  ia.display.label  [1 binding]
    Count  ia.display.label  [1 binding]
  Row  ia.container.flex  [1 binding]
    LabelCell  ia.container.flex  [2 bindings]
      Line1  ia.container.flex
        Label  ia.display.label  [1 binding]
        Key  ia.display.label  [1 binding]
      Desc  ia.display.label  [1 binding]
    Cells  ia.display.flex-repeater  [2 bindings; view: 00_Pages/Boars Head/Operations/_Admin/RPCell]
```

## Bindings

11 bindings: expr 6, property 5.

**`root/Sub`**

- `position.display`: expression

```js
{view.params.kind} = 'sub'
```


**`root/Sub/Title`**

- `props.text`: property `view.params.title`

**`root/Sub/Count`**

- `props.text`: expression

```js
'·  ' + toStr({view.params.n})
```


**`root/Row`**

- `position.display`: expression

```js
!({view.params.kind} = 'sub')
```


**`root/Row/LabelCell`**

- `meta.tooltip.enabled`: expression

```js
len(coalesce({view.params.desc}, '')) > 0
```


- `meta.tooltip.text`: expression

```js
{view.params.desc}
```


**`root/Row/LabelCell/Line1/Label`**

- `props.text`: property `view.params.label`

**`root/Row/LabelCell/Line1/Key`**

- `props.text`: property `view.params.key`

**`root/Row/LabelCell/Desc`**

- `props.text`: property `view.params.desc`

**`root/Row/Cells`**

- `position.basis`: expression

```js
toStr(len({view.params.cells}) * {view.params.rw}) + 'px'
```


- `props.instances`: property `view.params.cells`

## Related Views

**Embeds** (1): [00\_Pages/Boars Head/Operations/\_Admin/RPCell](./rpcell.md) (flex repeater)

**Embedded in** (1): [00\_Pages/Boars Head/Operations/\_Admin/RPGroup](./rpgroup.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-desc` | 1 | style class |
| `admin-head-sub` | 1 | style class |
| `admin-key` | 1 | style class |
| `admin-row` | 1 | style class |
| `admin-row-label` | 1 | style class |
| `admin-sub` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
