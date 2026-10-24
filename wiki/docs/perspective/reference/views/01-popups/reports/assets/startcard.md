---
title: "StartCard"
sidebar_label: "StartCard"
description: "Perspective view 01_Popups/Reports/_Assets/StartCard (Asset (embedded piece)): 8 components, 8 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/StartCard", "StartCard"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/StartCard`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/StartCard` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/StartCard/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; StartCard |
| Root | `ia.container.flex`, height 120, width 280 |
| Size | 8 components, 8 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-24T13:51:33Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `item` | `{"description": "", "icon": "", "id": "", "label": "", "meta": "", ...` | input |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x3, ia.display.icon x2.

```text
root  ia.container.flex  [1 binding; 1 event]
  Top  ia.container.flex
    IconBox  ia.container.flex  [1 binding]
      Icon  ia.display.icon  [2 bindings]
    Title  ia.display.label  [1 binding]
    Check  ia.display.icon  [1 binding]
  Desc  ia.display.label  [1 binding]
  Meta  ia.display.label  [1 binding]
```

## Bindings

8 bindings: expr 8.

**`root`**

- `props.style.classes`: expression

```js
if(coalesce({view.params.item.selected}, false), 'report-tile report-tile-selected', 'report-tile')
```


**`root/Top/IconBox`**

- `props.style.classes`: expression

```js
if(coalesce({view.params.item.selected}, false), 'report-icon-box report-icon-box-selected', 'report-icon-box')
```


**`root/Top/IconBox/Icon`**

- `props.color`: expression

```js
if(coalesce({view.params.item.selected}, false), 'var(--neutral-10)', 'var(--callToAction)')
```


- `props.path`: expression

```js
coalesce({view.params.item.icon}, 'material/assessment')
```


**`root/Top/Title`**

- `props.text`: expression

```js
coalesce({view.params.item.label}, '')
```


**`root/Top/Check`**

- `position.display`: expression

```js
coalesce({view.params.item.selected}, false)
```


**`root/Desc`**

- `props.text`: expression

```js
coalesce({view.params.item.description}, '')
```


**`root/Meta`**

- `props.text`: expression

```js
coalesce({view.params.item.meta}, '')
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
it = self.view.params.item
system.perspective.sendMessage('rptStart', {'kind': 'source', 'value': it.id}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Groveport/Operations/ReportsBuilder](../../../00-pages/groveport/operations/reportsbuilder.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `report-icon-box` | 1 | style class |
| `report-tile` | 1 | style class |
| `report-tile-desc` | 1 | style class |
| `report-tile-meta` | 1 | style class |
| `report-tile-title` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
