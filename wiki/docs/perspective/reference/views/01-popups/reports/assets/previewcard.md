---
title: "PreviewCard"
sidebar_label: "PreviewCard"
description: "Perspective view 01_Popups/Reports/_Assets/PreviewCard (Asset (embedded piece)): 4 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/PreviewCard", "PreviewCard"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/PreviewCard`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/PreviewCard` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/PreviewCard/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; PreviewCard |
| Root | `ia.container.flex`, height 92, width 200 |
| Size | 4 components, 3 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T19:45:31Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `card` | `{"demo": false, "label": "", "sub": "", "value": ""}` | input |

## Component Tree

Component types: ia.display.label x3, ia.container.flex x1.

```text
root  ia.container.flex
  Label  ia.display.label  [1 binding]
  Value  ia.display.label  [1 binding]
  Sub  ia.display.label  [1 binding]
```

## Bindings

3 bindings: expr 3.

**`root/Label`**

- `props.text`: expression

```js
coalesce({view.params.card.label}, '')
```


**`root/Value`**

- `props.text`: expression

```js
coalesce({view.params.card.value}, '')
```


**`root/Sub`**

- `props.text`: expression

```js
coalesce({view.params.card.sub}, '')
```


## Related Views

**Embedded in** (1): [01\_Popups/Reports/\_Assets/PreviewSection](./previewsection.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `report-kpi` | 1 | style class |
| `report-kpi-detail` | 1 | style class |
| `report-kpi-label` | 1 | style class |
| `report-kpi-value` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
