---
title: "TwoLineCell"
sidebar_label: "TwoLineCell"
description: "Perspective view 00_Pages/Boars Head/Operations/OutOfService/_Assets/TwoLineCell (Asset (embedded piece)): 3 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/OutOfService/_Assets/TwoLineCell", "TwoLineCell"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/Boars Head/Operations/OutOfService/_Assets/TwoLineCell`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/OutOfService/_Assets/TwoLineCell` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/OutOfService/_Assets/TwoLineCell/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; OutOfService &gt; \_Assets &gt; TwoLineCell |
| Root | `ia.container.flex`, height 44, width 180 |
| Size | 3 components, 2 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `value` | `""` | input |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1.

```text
root  ia.container.flex
  Line1  ia.display.label  [1 binding]
  Line2  ia.display.label  [1 binding]
```

## Bindings

2 bindings: expr 2.

**`root/Line1`**

- `props.text`: expression

```js
coalesce(try(split(coalesce({view.params.value}, ''), ';;')[0, 0], ''), '')
```


**`root/Line2`**

- `props.text`: expression

```js
coalesce(try(split(coalesce({view.params.value}, ''), ';;')[1, 0], ''), '')
```


## Related Views

**Opened or named by** (1): [00\_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog](../outofservicelog.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `form-hint` | 1 | style class |
| `form-row-label` | 1 | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
