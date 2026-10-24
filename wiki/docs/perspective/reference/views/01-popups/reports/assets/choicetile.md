---
title: "ChoiceTile"
sidebar_label: "ChoiceTile"
description: "Perspective view 01_Popups/Reports/_Assets/ChoiceTile (Asset (embedded piece)): 3 components, 4 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/ChoiceTile", "ChoiceTile"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/ChoiceTile`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/ChoiceTile` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/ChoiceTile/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; ChoiceTile |
| Root | `ia.container.flex`, height 56, width 134 |
| Size | 3 components, 4 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T19:45:31Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `item` | `{"detail": "", "id": "", "kind": "", "label": "", "selected": false}` | input |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1.

```text
root  ia.container.flex  [1 binding; 1 event]
  Label  ia.display.label  [1 binding]
  Detail  ia.display.label  [2 bindings]
```

## Bindings

4 bindings: expr 4.

**`root`**

- `props.style.classes`: expression

```js
if(coalesce({view.params.item.selected}, false), 'report-choice report-choice-selected', 'report-choice')
```


**`root/Label`**

- `props.text`: expression

```js
coalesce({view.params.item.label}, '')
```


**`root/Detail`**

- `position.display`: expression

```js
len(coalesce({view.params.item.detail}, '')) > 0
```


- `props.text`: expression

```js
coalesce({view.params.item.detail}, '')
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
it = self.view.params.item
system.perspective.sendMessage('rptEdit', {'kind': it.kind, 'id': it.id, 'value': it.id, 'on': True}, scope='page')
```

## Related Views

**Embedded in** (1): [01\_Popups/Reports/ReportBuilder](../reportbuilder.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `report-choice` | 1 | style class |
| `report-choice-detail` | 1 | style class |
| `report-choice-label` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
