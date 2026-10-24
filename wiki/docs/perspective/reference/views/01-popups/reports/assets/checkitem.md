---
title: "CheckItem"
sidebar_label: "CheckItem"
description: "Perspective view 01_Popups/Reports/_Assets/CheckItem (Asset (embedded piece)): 3 components, 6 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/CheckItem", "CheckItem"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/CheckItem`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/CheckItem` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/CheckItem/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; CheckItem |
| Root | `ia.container.flex`, height 28, width 320 |
| Size | 3 components, 6 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T19:45:31Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `item` | `{"head": false, "id": "", "indent": 0, "kind": "", "label": "", "on...` | input |

## Component Tree

Component types: ia.container.flex x1, ia.input.checkbox x1, ia.display.label x1.

```text
root  ia.container.flex  [1 binding]
  Check  ia.input.checkbox  [3 bindings; 1 event]
  Caption  ia.display.label  [2 bindings]
```

## Bindings

6 bindings: expr 6.

**`root`**

- `props.style.paddingLeft`: expression

```js
toStr(coalesce({view.params.item.indent}, 0) * 20) + 'px'
```


**`root/Check`**

- `position.display`: expression

```js
!coalesce({view.params.item.head}, false)
```


- `props.selected`: expression

```js
coalesce({view.params.item.on}, false)
```


- `props.text`: expression

```js
coalesce({view.params.item.label}, '')
```


**`root/Caption`**

- `position.display`: expression

```js
coalesce({view.params.item.head}, false)
```


- `props.text`: expression

```js
coalesce({view.params.item.label}, '')
```


## Event Scripts And Handlers

- **`root/Check`** `component.onActionPerformed`, script action, scope `G`

```python
it = self.view.params.item
system.perspective.sendMessage('rptEdit', {'kind': it.kind, 'id': it.id, 'on': bool(self.props.selected)}, scope='page')
```

## Related Views

**Embedded in** (1): [01\_Popups/Reports/ReportBuilder](../reportbuilder.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `form-check` | 1 | style class |
| `form-th` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
