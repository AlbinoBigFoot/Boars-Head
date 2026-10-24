---
title: "SavedListRow"
sidebar_label: "SavedListRow"
description: "Perspective view 01_Popups/Reports/_Assets/SavedListRow (Asset (embedded piece)): 15 components, 36 bindings, 8 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/SavedListRow", "SavedListRow"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/SavedListRow`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/SavedListRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/SavedListRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; SavedListRow |
| Root | `ia.container.flex`, height 44, width 1000 |
| Size | 15 components, 36 bindings, 8 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-24T17:59:20Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `row` | `{"id": 0}` | input |
| `tab` | `"mine"` | input |

## Component Tree

Component types: ia.input.button x7, ia.display.label x6, ia.container.flex x2.

<details>
<summary>Component tree (15 components)</summary>

```text
root  ia.container.flex  [1 event]
  Name  ia.display.label  [1 binding]
  Source  ia.display.label  [1 binding]
  Range  ia.display.label  [1 binding]
  C4  ia.display.label  [1 binding]
  C5  ia.display.label  [1 binding]
  C6  ia.display.label  [1 binding]
  Actions  ia.container.flex  [1 binding]
    Run  ia.input.button  [4 bindings; 1 event]
    RunAgain  ia.input.button  [4 bindings; 1 event]
    Edit  ia.input.button  [4 bindings; 1 event]
    Download  ia.input.button  [4 bindings; 1 event]
    Share  ia.input.button  [5 bindings; 1 event]
    Rename  ia.input.button  [4 bindings; 1 event]
    Delete  ia.input.button  [4 bindings; 1 event]
```

</details>

## Bindings

36 bindings: expr 36.

<details>
<summary>All 36 bindings, grouped by component</summary>

**`root/Name`**

- `props.text`: expression

```js
coalesce({view.params.row.name}, '')
```


**`root/Source`**

- `props.text`: expression

```js
coalesce({view.params.row.source}, '')
```


**`root/Range`**

- `props.text`: expression

```js
coalesce({view.params.row.range}, '')
```


**`root/C4`**

- `props.text`: expression

```js
if(coalesce({view.params.tab}, 'mine') = 'runs', coalesce({view.params.row.runBy}, ''), coalesce({view.params.row.owner}, ''))
```


**`root/C5`**

- `props.text`: expression

```js
if(coalesce({view.params.tab}, 'mine') = 'runs', coalesce({view.params.row.runAt}, ''), coalesce({view.params.row.lastRun}, ''))
```


**`root/C6`**

- `props.text`: expression

```js
if(coalesce({view.params.tab}, 'mine') = 'runs', coalesce({view.params.row.format}, ''), coalesce({view.params.row.shared}, ''))
```


**`root/Actions`**

- `position.basis`: expression

```js
if(coalesce({view.params.tab}, 'mine') = 'runs', '68px', '212px')
```


**`root/Actions/Run`**

- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.tooltip.text`: expression

```js

```


- `position.display`: expression

```js
!(coalesce({view.params.tab}, 'mine') = 'runs')
```


- `props.enabled`: expression

```js
true
```


**`root/Actions/RunAgain`**

- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.tooltip.text`: expression

```js

```


- `position.display`: expression

```js
coalesce({view.params.tab}, 'mine') = 'runs'
```


- `props.enabled`: expression

```js
true
```


**`root/Actions/Edit`**

- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.tooltip.text`: expression

```js

```


- `position.display`: expression

```js
!(coalesce({view.params.tab}, 'mine') = 'runs')
```


- `props.enabled`: expression

```js
true
```


**`root/Actions/Download`**

- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.tooltip.text`: expression

```js
if(!(coalesce({view.params.tab}, 'mine') = 'runs') || coalesce({view.params.row.mine}, false), 'Download This Report As PDF, Excel Or CSV', 'Only The Person Who Ran A Report Can Download It Again')
```


- `position.display`: expression

```js
true
```


- `props.enabled`: expression

```js
!(coalesce({view.params.tab}, 'mine') = 'runs') || coalesce({view.params.row.mine}, false)
```


**`root/Actions/Share`**

- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.row.canShare}, false), if(coalesce({view.params.row.isShared}, false), 'Stop Sharing This Report', 'Share This Report With Others'), 'Only The Owner (With Share Permission) Can Share A Report')
```


- `position.display`: expression

```js
!(coalesce({view.params.tab}, 'mine') = 'runs')
```


- `props.enabled`: expression

```js
coalesce({view.params.row.canShare}, false)
```


- `props.image.icon.path`: expression

```js
if(coalesce({view.params.row.isShared}, false), 'material/people', 'material/share')
```


**`root/Actions/Rename`**

- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.row.canEdit}, false), 'Rename This Report', 'Only The Owner Can Rename A Report')
```


- `position.display`: expression

```js
!(coalesce({view.params.tab}, 'mine') = 'runs')
```


- `props.enabled`: expression

```js
coalesce({view.params.row.canEdit}, false)
```


**`root/Actions/Delete`**

- `meta.tooltip.enabled`: expression

```js
true
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.params.row.canEdit}, false), 'Delete This Report (Asks First)', 'Only The Owner Can Delete A Report')
```


- `position.display`: expression

```js
!(coalesce({view.params.tab}, 'mine') = 'runs')
```


- `props.enabled`: expression

```js
coalesce({view.params.row.canEdit}, false)
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onDoubleClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
shared.Reports.open(None, {'origin': 'Saved Reports', 'step': 4}, self.session, row['id'])
```

- **`root/Actions/Run`** `dom.onClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
shared.Reports.open(None, {'origin': 'Saved Reports', 'step': 4}, self.session, row['id'])
```

- **`root/Actions/RunAgain`** `dom.onClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
shared.Reports.open(None, {'origin': 'Saved Reports', 'runId': row['id'], 'step': 4}, self.session)
```

- **`root/Actions/Edit`** `dom.onClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
shared.Reports.open(None, {'origin': 'Saved Reports', 'step': 3}, self.session, row['id'])
```

- **`root/Actions/Download`** `dom.onClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
pos = shared.Reports.menuBox(self.page, event, 156, 122)
system.perspective.openPopup(id='rptDownload', view='01_Popups/Reports/DownloadMenu',
    params={'kind': 'run' if self.view.params.tab == 'runs' else 'tpl', 'id': row['id']}, position=pos,
    showCloseIcon=False, draggable=False, resizable=False, modal=True, overlayDismiss=True, viewportBound=True)
```

- **`root/Actions/Share`** `dom.onClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
res = shared.Reports.setTemplateShared(self.session, row['id'], not row.get('isShared'))
system.perspective.sendMessage('rptSavedChanged', {'message': res['message']}, scope='page')
```

- **`root/Actions/Rename`** `dom.onClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
pos = shared.Reports.centerBox(self.page, 440, 210)
system.perspective.openPopup(id='rptRename', view='01_Popups/Reports/RenameReport',
    params={'id': row['id'], 'name': row.get('name') or ''}, position=pos, modal=True, draggable=False,
    resizable=False, showCloseIcon=False, overlayDismiss=False, viewportBound=True)
```

- **`root/Actions/Delete`** `dom.onClick`, script action, scope `G`

```python
row = self.view.params.row
if not row or not row.get('id'):
    return
shared.Alerts.showAlert(state='warning', title='Delete Report', message="Delete '" + (row.get('name') or '') + "'? This cannot be undone.", showCloseBtn=False, btnTextPrimary='Delete', btnTextSecondary='Cancel', btnActionPrimary='rptPageDelete', btnActionSecondary='', payload={'id': row['id']}, overlayDismiss=False)
```

Project script calls: [shared.Reports.centerBox](../../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.menuBox](../../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.setTemplateShared](../../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [01\_Popups/Reports/DownloadMenu](../downloadmenu.md), [01\_Popups/Reports/RenameReport](../renamereport.md)

**Embedded in** (1): [00\_Pages/Groveport/Operations/ReportsSaved](../../../00-pages/groveport/operations/reportssaved.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 5 | style class |
| `form-btn` | 7 | style class |
| `fs-12` | 5 | style class |
| `report-row` | 1 | style class |
| `report-row-name` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
