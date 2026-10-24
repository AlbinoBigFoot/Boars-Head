---
title: "UMAdjustRow"
sidebar_label: "UMAdjustRow"
description: "Perspective view 00_Pages/Boars Head/Operations/_Admin/UMAdjustRow (Page piece (not routed)): 11 components, 9 bindings, 5 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/_Admin/UMAdjustRow", "UMAdjustRow"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Boars Head/Operations/_Admin/UMAdjustRow`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/_Admin/UMAdjustRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/_Admin/UMAdjustRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; \_Admin &gt; UMAdjustRow |
| Root | `ia.container.flex`, height 104, width 600 |
| Size | 11 components, 9 bindings, 1 event handlers, 4 change scripts, 0 message handlers |
| Last saved | 2026-10-24T01:28:07Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `available` | `false` | input |
| `canEdit` | `false` | input |
| `end` | `null` | input |
| `i` | `0` | input |
| `note` | `""` | input |
| `start` | `null` | input |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x2, ia.input.date-time-input x2, ia.input.checkbox x1, ia.display.icon x1, ia.input.text-field x1.

```text
root  ia.container.flex
  Dates  ia.container.flex
    Start  ia.container.flex
      Label  ia.display.label
      Input  ia.input.date-time-input  [2 bindings]
    End  ia.container.flex
      Label  ia.display.label
      Input  ia.input.date-time-input  [2 bindings]
    Available  ia.input.checkbox  [2 bindings]
    Remove  ia.display.icon  [1 binding; 1 event]
  Note  ia.input.text-field  [2 bindings]
```

## Bindings

9 bindings: property 9.

**`root/Dates/Start/Input`**

- `props.enabled`: property `view.params.canEdit`

- `props.value`: property `view.params.start`

**`root/Dates/End/Input`**

- `props.enabled`: property `view.params.canEdit`

- `props.value`: property `view.params.end`

**`root/Dates/Available`**

- `props.enabled`: property `view.params.canEdit`

- `props.selected`: property `view.params.available`

**`root/Dates/Remove`**

- `position.display`: property `view.params.canEdit`

**`root/Note`**

- `props.enabled`: property `view.params.canEdit`

- `props.text`: property `view.params.note`

## Event Scripts And Handlers

- **`root/Dates/Remove`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage('umAdjRemove', payload={'i': self.view.params.i}, scope='page')
```

- **`root/Dates/Start/Input`** change script on `props.value`

```python
if origin == 'Browser' or origin == 'browser':
    system.perspective.sendMessage('umAdjSet', payload={'i': self.view.params.i, 'field': 'start', 'value': currentValue.value}, scope='page')
```

- **`root/Dates/End/Input`** change script on `props.value`

```python
if origin == 'Browser' or origin == 'browser':
    system.perspective.sendMessage('umAdjSet', payload={'i': self.view.params.i, 'field': 'end', 'value': currentValue.value}, scope='page')
```

- **`root/Dates/Available`** change script on `props.selected`

```python
if origin == 'Browser' or origin == 'browser':
    system.perspective.sendMessage('umAdjSet', payload={'i': self.view.params.i, 'field': 'available', 'value': currentValue.value}, scope='page')
```

- **`root/Note`** change script on `props.text`

```python
if origin == 'Browser' or origin == 'browser':
    system.perspective.sendMessage('umAdjSet', payload={'i': self.view.params.i, 'field': 'note', 'value': currentValue.value}, scope='page')
```

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/Operations/UserManagement/UserManagement](../usermanagement/usermanagement.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-ico-muted` | 1 | style class |
| `form-check` | 1 | style class |
| `form-input` | 3 | style class |
| `form-label` | 2 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
