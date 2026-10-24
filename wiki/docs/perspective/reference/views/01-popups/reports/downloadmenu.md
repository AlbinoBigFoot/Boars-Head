---
title: "DownloadMenu"
sidebar_label: "DownloadMenu"
description: "Perspective view 01_Popups/Reports/DownloadMenu (Popup / faceplate): 4 components, 0 bindings, 3 event scripts."
generated: true
keywords: ["01_Popups/Reports/DownloadMenu", "DownloadMenu"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/Reports/DownloadMenu`.

| | |
|---|---|
| View path | `01_Popups/Reports/DownloadMenu` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/DownloadMenu/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; DownloadMenu |
| Root | `ia.container.flex`, height 122, width 156 |
| Size | 4 components, 0 bindings, 3 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-24T17:59:20Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `id` | `0` | input |
| `kind` | `"tpl"` | input |

## Component Tree

Component types: ia.input.button x3, ia.container.flex x1.

```text
root  ia.container.flex
  Pdf  ia.input.button  [1 event]
  Xls  ia.input.button  [1 event]
  Csv  ia.input.button  [1 event]
```

## Event Scripts And Handlers

- **`root/Pdf`** `component.onActionPerformed`, script action, scope `G`

```python
p = self.view.params
if p.kind == 'run':
    msg = shared.Reports.runFromRun(self.session, p.id, 'PDF')
else:
    msg = shared.Reports.runTemplate(self.session, p.id, 'PDF')
system.perspective.closePopup('rptDownload')
system.perspective.sendMessage('rptSavedChanged', {'message': msg}, scope='page')
```

- **`root/Xls`** `component.onActionPerformed`, script action, scope `G`

```python
p = self.view.params
if p.kind == 'run':
    msg = shared.Reports.runFromRun(self.session, p.id, 'Excel')
else:
    msg = shared.Reports.runTemplate(self.session, p.id, 'Excel')
system.perspective.closePopup('rptDownload')
system.perspective.sendMessage('rptSavedChanged', {'message': msg}, scope='page')
```

- **`root/Csv`** `component.onActionPerformed`, script action, scope `G`

```python
p = self.view.params
if p.kind == 'run':
    msg = shared.Reports.runFromRun(self.session, p.id, 'CSV')
else:
    msg = shared.Reports.runTemplate(self.session, p.id, 'CSV')
system.perspective.closePopup('rptDownload')
system.perspective.sendMessage('rptSavedChanged', {'message': msg}, scope='page')
```

Project script calls: [shared.Reports.runFromRun](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.runTemplate](../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Opened or named by** (1): [01\_Popups/Reports/\_Assets/SavedListRow](./assets/savedlistrow.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `form-btn` | 3 | style class |
| `form-card` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
