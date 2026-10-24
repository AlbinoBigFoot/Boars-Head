---
title: "PreviewSection"
sidebar_label: "PreviewSection"
description: "Perspective view 01_Popups/Reports/_Assets/PreviewSection (Asset (embedded piece)): 8 components, 12 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/PreviewSection", "PreviewSection"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/PreviewSection`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/PreviewSection` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/PreviewSection/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; PreviewSection |
| Root | `ia.container.flex`, height 200, width 840 |
| Size | 8 components, 12 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T19:45:31Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `sec` | `{"cards": [], "charts": [], "columns": [], "data": [], "more": "", ...` | input |

## Component Tree

Component types: ia.display.label x3, ia.container.flex x2, ia.display.flex-repeater x2, ia.display.table x1.

```text
root  ia.container.flex
  Bar  ia.container.flex
    Title  ia.display.label  [1 binding]
    Note  ia.display.label  [1 binding]
  Cards  ia.display.flex-repeater  [2 bindings; view: 01_Popups/Reports/_Assets/PreviewCard]
  Charts  ia.display.flex-repeater  [2 bindings; view: 01_Popups/Reports/_Assets/PreviewChart]
  Table  ia.display.table  [4 bindings]
  More  ia.display.label  [2 bindings]
```

## Bindings

12 bindings: expr 8, property 4.

**`root/Bar/Title`**

- `props.text`: expression

```js
coalesce({view.params.sec.title}, '')
```


**`root/Bar/Note`**

- `props.text`: expression

```js
coalesce({view.params.sec.note}, '')
```


**`root/Cards`**

- `position.display`: expression

```js
coalesce({view.params.sec.type}, '') = 'cards'
```


- `props.instances`: property `view.params.sec.cards`, then script transform

Transform 1, script:

```python
return [{'card': c} for c in (value or [])]
```


**`root/Charts`**

- `position.display`: expression

```js
coalesce({view.params.sec.type}, '') = 'trend'
```


- `props.instances`: property `view.params.sec.charts`, then script transform

Transform 1, script:

```python
return [{'chart': c} for c in list(value or [])[:2]]
```


**`root/Table`**

- `position.display`: expression

```js
coalesce({view.params.sec.type}, '') != 'cards' && coalesce({view.params.sec.type}, '') != 'trend'
```


- `props.columns`: property `view.params.sec.columns`

- `props.data`: property `view.params.sec.data`

- `props.rows.height`: expression

```js
coalesce({view.params.sec.rowHeight}, 30)
```


**`root/More`**

- `position.display`: expression

```js
len(coalesce({view.params.sec.more}, '')) > 0
```


- `props.text`: expression

```js
coalesce({view.params.sec.more}, '')
```


## Related Views

**Embeds** (2): [01\_Popups/Reports/\_Assets/PreviewCard](./previewcard.md) (flex repeater), [01\_Popups/Reports/\_Assets/PreviewChart](./previewchart.md) (flex repeater)

**Embedded in** (1): [01\_Popups/Reports/ReportBuilder](../reportbuilder.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-component` | 1 | stylesheet |
| `form-th` | 1 | style class |
| `report-choice-detail` | 2 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
