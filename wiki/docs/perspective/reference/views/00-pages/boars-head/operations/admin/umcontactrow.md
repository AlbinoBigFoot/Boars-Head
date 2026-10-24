---
title: "UMContactRow"
sidebar_label: "UMContactRow"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/UMContactRow (Page piece (not routed)): 4 components, 5 bindings, 3 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/UMContactRow", "UMContactRow"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/UMContactRow`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/UMContactRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/UMContactRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; UMContactRow |
| Root | `ia.container.flex`, height 40, width 600 |
| Size | 4 components, 5 bindings, 1 event handlers, 2 change scripts, 0 message handlers |
| Last saved | 2026-10-23T20:47:30Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `canEdit` | `false` | input |
| `i` | `0` | input |
| `type` | `"email"` | input |
| `value` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.input.dropdown x1, ia.input.text-field x1, ia.display.icon x1.

```text
root  ia.container.flex
  Type  ia.input.dropdown  [2 bindings]
  Value  ia.input.text-field  [2 bindings]
  Remove  ia.display.icon  [1 binding; 1 event]
```

## Bindings

5 bindings: property 5.

**`root/Type`**

- `props.enabled`: property `view.params.canEdit`

- `props.value`: property `view.params.type`

**`root/Value`**

- `props.enabled`: property `view.params.canEdit`

- `props.text`: property `view.params.value`

**`root/Remove`**

- `position.display`: property `view.params.canEdit`

## Event Scripts And Handlers

- **`root/Remove`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage('umContactRemove', payload={'i': self.view.params.i}, scope='page')
```

- **`root/Type`** change script on `props.value`

```python
if origin == 'Browser' or origin == 'browser':
    system.perspective.sendMessage('umContactSet', payload={'i': self.view.params.i, 'field': 'type', 'value': currentValue.value}, scope='page')
```

- **`root/Value`** change script on `props.text`

```python
if origin == 'Browser' or origin == 'browser':
    system.perspective.sendMessage('umContactSet', payload={'i': self.view.params.i, 'field': 'value', 'value': currentValue.value}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](../usermanagement/usermanagement.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-ico-muted` | 1 | style class |
| `form-input` | 2 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
