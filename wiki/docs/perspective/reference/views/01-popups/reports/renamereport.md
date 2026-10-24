---
title: "RenameReport"
sidebar_label: "RenameReport"
description: "Perspective view 01_Popups/Reports/RenameReport (Popup / faceplate): 9 components, 2 bindings, 4 event scripts."
generated: true
keywords: ["01_Popups/Reports/RenameReport", "RenameReport"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/Reports/RenameReport`.

| | |
|---|---|
| View path | `01_Popups/Reports/RenameReport` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/RenameReport/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; RenameReport |
| Root | `ia.container.flex`, height 210, width 440 |
| Size | 9 components, 2 bindings, 4 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-24T14:05:50Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `id` | `0` | input |
| `name` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `err` | `""` | |
| `name` | `""` | |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x3, ia.input.button x2, ia.input.text-field x1.

```text
root  ia.container.flex  [1 event]
  Title  ia.display.label
  Caption  ia.display.label
  Name  ia.input.text-field  [1 binding; 1 event]
  Error  ia.display.label  [1 binding]
  Buttons  ia.container.flex
    Spacer  ia.container.flex
    Cancel  ia.input.button  [1 event]
    Save  ia.input.button  [1 event]
```

## Bindings

2 bindings: property 1, expr 1.

**`root/Name`**

- `props.text`: property `view.custom.name` (bidirectional)

**`root/Error`**

- `props.text`: expression

```js
coalesce({view.custom.err}, '')
```


## Event Scripts And Handlers

- **`root`** `system.onStartup`, script action, scope `G`

```python
self.view.custom.name = self.view.params.name
```

- **`root/Name`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.name = self.props.text
v = self.view.custom
res = shared.Reports.renameTemplate(self.session, self.view.params.id, v.name)
if res['ok']:
    system.perspective.sendMessage('rptSavedChanged', {'message': res['message']}, scope='page')
    system.perspective.closePopup('rptRename')
else:
    v.err = res['message']
```

- **`root/Buttons/Cancel`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.closePopup('rptRename')
```

- **`root/Buttons/Save`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
res = shared.Reports.renameTemplate(self.session, self.view.params.id, v.name)
if res['ok']:
    system.perspective.sendMessage('rptSavedChanged', {'message': res['message']}, scope='page')
    system.perspective.closePopup('rptRename')
else:
    v.err = res['message']
```

Project script calls: [shared.Reports.renameTemplate](../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Opened or named by** (1): [01\_Popups/Reports/\_Assets/SavedListRow](./assets/savedlistrow.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `form-btn` | 1 | style class |
| `form-btn-primary` | 1 | style class |
| `form-input` | 1 | style class |
| `form-th` | 1 | style class |
| `fs-12` | 1 | style class |
| `fw-600` | 1 | style class |
| `report-heading` | 1 | style class |
| `report-surface` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
