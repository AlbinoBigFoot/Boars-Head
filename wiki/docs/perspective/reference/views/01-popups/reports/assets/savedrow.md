---
title: "SavedRow"
sidebar_label: "SavedRow"
description: "Perspective view 01_Popups/Reports/_Assets/SavedRow (Asset (embedded piece)): 6 components, 3 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/SavedRow", "SavedRow"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/SavedRow`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/SavedRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/SavedRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; SavedRow |
| Root | `ia.container.flex`, height 56, width 320 |
| Size | 6 components, 3 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T19:45:31Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `item` | `{"icon": "", "id": 0, "kind": "", "meta": "", "name": ""}` | input |

## Component Tree

Component types: ia.container.flex x2, ia.display.icon x2, ia.display.label x2.

```text
root  ia.container.flex  [1 event]
  Icon  ia.display.icon  [1 binding]
  Text  ia.container.flex
    Name  ia.display.label  [1 binding]
    Meta  ia.display.label  [1 binding]
  Go  ia.display.icon
```

## Bindings

3 bindings: expr 3.

**`root/Icon`**

- `props.path`: expression

```js
coalesce({view.params.item.icon}, 'material/description')
```


**`root/Text/Name`**

- `props.text`: expression

```js
coalesce({view.params.item.name}, '')
```


**`root/Text/Meta`**

- `props.text`: expression

```js
coalesce({view.params.item.meta}, '')
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
it = self.view.params.item
system.perspective.sendMessage('rptLoadSaved', {'kind': it.kind, 'id': it.id}, scope='page')
```

## Related Views

**Embedded in** (1): [01\_Popups/Reports/ReportBuilder](../reportbuilder.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `report-choice-detail` | 1 | style class |
| `report-row` | 1 | style class |
| `report-row-name` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
