---
title: "SectionItem"
sidebar_label: "SectionItem"
description: "Perspective view 01_Popups/Reports/_Assets/SectionItem (Asset (embedded piece)): 12 components, 12 bindings, 6 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/SectionItem", "SectionItem"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/SectionItem`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/SectionItem` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/SectionItem/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; SectionItem |
| Root | `ia.container.flex`, height 44, width 420 |
| Size | 12 components, 12 bindings, 3 event handlers, 3 change scripts, 0 message handlers |
| Last saved | 2026-10-24T12:07:22Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `sec` | `{"first": false, "hint": "", "label": "", "last": false, "n": 10, "...` | input |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x3, ia.display.icon x2, ia.input.dropdown x2, ia.input.checkbox x1, ia.input.numeric-entry-field x1.

```text
root  ia.container.flex
  Line1  ia.container.flex
    On  ia.input.checkbox  [2 bindings; 1 event]
    Hint  ia.display.label  [2 bindings]
    Up  ia.display.icon  [1 binding; 1 event]
    Down  ia.display.icon  [1 binding; 1 event]
  TopNSettings  ia.container.flex  [1 binding]
    Show  ia.display.label
    N  ia.input.numeric-entry-field  [1 binding]
    TopN  ia.input.dropdown  [2 bindings]
    By  ia.display.label
    OrderBy  ia.input.dropdown  [2 bindings]
```

## Bindings

12 bindings: expr 10, property 2.

**`root/Line1/On`**

- `props.selected`: expression

```js
coalesce({view.params.sec.on}, false)
```


- `props.text`: expression

```js
coalesce({view.params.sec.label}, '')
```


**`root/Line1/Hint`**

- `position.display`: expression

```js
!(coalesce({view.params.sec.type}, '') = 'topn')
```


- `props.text`: expression

```js
coalesce({view.params.sec.hint}, '')
```


**`root/Line1/Up`**

- `props.style.opacity`: expression

```js
if(coalesce({view.params.sec.first}, false), 0.25, 1)
```


**`root/Line1/Down`**

- `props.style.opacity`: expression

```js
if(coalesce({view.params.sec.last}, false), 0.25, 1)
```


**`root/TopNSettings`**

- `position.display`: expression

```js
coalesce({view.params.sec.type}, '') = 'topn'
```


**`root/TopNSettings/N`**

- `props.value`: expression

```js
coalesce({view.params.sec.n}, 10)
```


**`root/TopNSettings/TopN`**

- `props.options`: property `view.params.sec.topNOptions`

- `props.value`: expression

```js
{view.params.sec.topN}
```


**`root/TopNSettings/OrderBy`**

- `props.options`: property `view.params.sec.orderOptions`

- `props.value`: expression

```js
{view.params.sec.orderBy}
```


## Event Scripts And Handlers

- **`root/Line1/On`** `component.onActionPerformed`, script action, scope `G`

```python
s = self.view.params.sec
system.perspective.sendMessage('rptEdit', {'kind': 'section', 'type': s.type, 'on': bool(self.props.selected)}, scope='page')
```

- **`root/Line1/Up`** `dom.onClick`, script action, scope `G`

```python
s = self.view.params.sec
system.perspective.sendMessage('rptEdit', {'kind': 'move', 'type': s.type, 'dir': -1}, scope='page')
```

- **`root/Line1/Down`** `dom.onClick`, script action, scope `G`

```python
s = self.view.params.sec
system.perspective.sendMessage('rptEdit', {'kind': 'move', 'type': s.type, 'dir': 1}, scope='page')
```

- **`root/TopNSettings/N`** change script on `props.value`

```python
if str(origin) != 'Browser':
    return
s = self.view.params.sec
system.perspective.sendMessage('rptEdit', {'kind': 'sectionSet', 'type': s.type, 'key': 'n', 'value': int(currentValue.value or 10)}, scope='page')
```

- **`root/TopNSettings/TopN`** change script on `props.value`

```python
if str(origin) != 'Browser':
    return
s = self.view.params.sec
system.perspective.sendMessage('rptEdit', {'kind': 'sectionSet', 'type': s.type, 'key': 'topN', 'value': currentValue.value}, scope='page')
```

- **`root/TopNSettings/OrderBy`** change script on `props.value`

```python
if str(origin) != 'Browser':
    return
s = self.view.params.sec
system.perspective.sendMessage('rptEdit', {'kind': 'sectionSet', 'type': s.type, 'key': 'orderBy', 'value': currentValue.value}, scope='page')
```

## Related Views

**Embedded in** (1): [01\_Popups/Reports/ReportBuilder](../reportbuilder.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `form-check` | 1 | style class |
| `form-input` | 3 | style class |
| `report-choice-detail` | 3 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
