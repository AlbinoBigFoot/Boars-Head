---
title: "DisplayTrend"
sidebar_label: "DisplayTrend"
description: "Perspective view 03_Elements/03_Table/DisplayTrend (Element (small reusable part)): 3 components, 4 bindings, 1 event scripts."
generated: true
keywords: ["03_Elements/03_Table/DisplayTrend", "DisplayTrend"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/03_Table/DisplayTrend`.

| | |
|---|---|
| View path | `03_Elements/03_Table/DisplayTrend` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/03_Table/DisplayTrend/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 03\_Table &gt; DisplayTrend |
| Root | `ia.container.flex`, height 28, width 88 |
| Size | 3 components, 4 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-08-21T13:40:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `row` | `""` | input |
| `rowData` | `{}` | input |
| `value` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | bound (property) |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1.

```text
root  ia.container.flex  [1 binding; 1 event]
  Value  ia.display.label  [2 bindings]
  Unit  ia.display.label
```

## Bindings

4 bindings: property 3, expr 1.

**`(view)`**

- `custom.tagPath`: property `view.params.rowData.tempTagPath`, then expression transform

Transform 1, expression:

```js
coalesce({value}, '')
```


**`root`**

- `meta.visible`: expression

```js
len(coalesce({view.custom.tagPath}, '')) > 0
```


**`root/Value`**

- `props.text`: property `view.params.value`, then expression transform

Transform 1, expression:

```js
if(isNull({value}), '—', numberFormat({value}, '0.0'))
```


- `props.style.classes`: property `view.custom.tagPath`, then expression transform

Transform 1, expression:

```js
if(len({value}) > 0, 'Fonts/LiveData', 'Fonts/BadData')
```


## Event Scripts And Handlers

- **`root`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.tagPath}')
```

## Related Views

**Opened or named by** (1): [00\_Pages/Groveport/Utility/OverviewKpis](../../00-pages/groveport/utility/overviewkpis.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `fs-11` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
