---
title: "ReportsSaved"
sidebar_label: "ReportsSaved"
description: "Perspective view 00_Pages/Groveport/Operations/ReportsSaved (Page): 34 components, 30 bindings, 6 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/ReportsSaved", "ReportsSaved", "/operations/reports/saved"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Operations/ReportsSaved`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/ReportsSaved` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/ReportsSaved/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; ReportsSaved |
| Routes | `/operations/reports/saved` (Saved Reports) |
| Root | `ia.container.flex`, height 1000, width 1600 |
| Size | 34 components, 30 bindings, 6 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-10-24T17:54:56Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `model` | `{"counts": {"mine": 0, "runs": 0, "shared": 0}, "owners": [], "rows...` | bound (expr-struct) |
| `msg` | `""` | |
| `owner` | `null` | |
| `refresh` | `0` | |
| `search` | `""` | |
| `source` | `null` | |
| `tab` | `"mine"` | |

## Component Tree

Component types: ia.display.label x15, ia.container.flex x11, ia.input.button x3, ia.input.dropdown x2, ia.input.text-field x1, ia.display.flex-repeater x1, ia.display.icon x1.

<details>
<summary>Component tree (34 components)</summary>

```text
root  ia.container.flex
  Head  ia.container.flex
    TitleBox  ia.container.flex
      Title  ia.display.label
      Subtitle  ia.display.label
    New  ia.input.button  [1 binding; 1 event]
  Denied  ia.container.flex  [1 binding]
    DeniedMsg  ia.display.label
  Card  ia.container.flex  [1 binding]
    Tabs  ia.container.flex
      Tab_mine  ia.display.label  [2 bindings; 1 event]
      Tab_shared  ia.display.label  [2 bindings; 1 event]
      Tab_runs  ia.display.label  [2 bindings; 1 event]
    Toolbar  ia.container.flex
      Search  ia.input.text-field  [1 binding]
      Source  ia.input.dropdown  [2 bindings]
      Owner  ia.input.dropdown  [2 bindings]
      Refresh  ia.input.button  [1 event]
    Tables  ia.container.flex
      ListHeader  ia.container.flex  [1 binding]
        Name  ia.display.label  [1 binding]
        Source  ia.display.label  [1 binding]
        Range  ia.display.label  [1 binding]
        C4  ia.display.label  [1 binding]
        C5  ia.display.label  [1 binding]
        C6  ia.display.label  [1 binding]
        ActionsSpace  ia.container.flex  [1 binding]
      List  ia.display.flex-repeater  [2 bindings; view: 01_Popups/Reports/_Assets/SavedListRow]
      Empty  ia.container.flex  [1 binding]
        Icon  ia.display.icon
        Title  ia.display.label  [1 binding]
        Text  ia.display.label  [1 binding]
        Create  ia.input.button  [1 binding; 1 event]
    Status  ia.display.label  [1 binding]
```

</details>

## Bindings

30 bindings: expr 23, property 6, expr-struct 1.

<details>
<summary>All 30 bindings, grouped by component</summary>

**`(view)`**

- `custom.model`: structured expression (expr-struct), then script transform

```js
ok: coalesce({session.custom.Permissions.Reports.Use}, false)
owner: {view.custom.owner}
refresh: {view.custom.refresh}
search: {view.custom.search}
source: {view.custom.source}
tab: {view.custom.tab}
```

waitOnAll: `False`

Transform 1, script:

```python
if not value.ok:
    return {'rows': [], 'owners': [], 'sources': [], 'total': 0,
        'counts': {'mine': 0, 'shared': 0, 'runs': 0}}
return shared.Reports.savedModel(self.session, value.tab or 'mine', value.source or '',
    value.owner or '', value.search or '')
```


**`root/Head/New`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/Denied`**

- `position.display`: expression

```js
!coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/Card`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/Card/Tabs/Tab_mine`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'mine', 'report-tab report-tab-active', 'report-tab')
```


- `props.text`: expression

```js
'My Reports (' + toStr(coalesce({view.custom.model.counts.mine}, 0)) + ')'
```


**`root/Card/Tabs/Tab_shared`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'shared', 'report-tab report-tab-active', 'report-tab')
```


- `props.text`: expression

```js
'Shared (' + toStr(coalesce({view.custom.model.counts.shared}, 0)) + ')'
```


**`root/Card/Tabs/Tab_runs`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', 'report-tab report-tab-active', 'report-tab')
```


- `props.text`: expression

```js
'Recent Runs (' + toStr(coalesce({view.custom.model.counts.runs}, 0)) + ')'
```


**`root/Card/Toolbar/Search`**

- `props.text`: property `view.custom.search` (bidirectional)

**`root/Card/Toolbar/Source`**

- `props.options`: property `view.custom.model.sources`

- `props.value`: property `view.custom.source` (bidirectional)

**`root/Card/Toolbar/Owner`**

- `props.options`: property `view.custom.model.owners`

- `props.value`: property `view.custom.owner` (bidirectional)

**`root/Card/Tables/ListHeader`**

- `position.display`: expression

```js
coalesce({view.custom.model.total}, 0) > 0
```


**`root/Card/Tables/ListHeader/Name`**

- `props.text`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', 'Report', 'Name')
```


**`root/Card/Tables/ListHeader/Source`**

- `props.text`: expression

```js
'Source'
```


**`root/Card/Tables/ListHeader/Range`**

- `props.text`: expression

```js
'Time Range'
```


**`root/Card/Tables/ListHeader/C4`**

- `props.text`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', 'Run By', 'Owner')
```


**`root/Card/Tables/ListHeader/C5`**

- `props.text`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', 'Run At', 'Last Run')
```


**`root/Card/Tables/ListHeader/C6`**

- `props.text`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', 'Format', 'Shared')
```


**`root/Card/Tables/ListHeader/ActionsSpace`**

- `position.basis`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', '68px', '212px')
```


**`root/Card/Tables/List`**

- `position.display`: expression

```js
coalesce({view.custom.model.total}, 0) > 0
```


- `props.instances`: property `view.custom.model`, then script transform

Transform 1, script:

```python
m = value or {}
tab = m.get('tab') or 'mine'
return [{'row': dict((k, r[k]) for k in r.keys()), 'tab': tab} for r in (m.get('rows') or [])]
```


**`root/Card/Tables/Empty`**

- `position.display`: expression

```js
coalesce({view.custom.model.total}, 0) = 0
```


**`root/Card/Tables/Empty/Title`**

- `props.text`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', 'No Recent Runs Yet', if(coalesce({view.custom.tab}, 'mine') = 'shared', 'Nothing Is Shared Yet', 'No Saved Reports Yet'))
```


**`root/Card/Tables/Empty/Text`**

- `props.text`: expression

```js
if(coalesce({view.custom.tab}, 'mine') = 'runs', 'Reports You Download Appear Here.', if(coalesce({view.custom.tab}, 'mine') = 'shared', 'Reports Their Owners Share Show Up Here.', 'Build A Report, Then Use Save As Template On The Last Step.'))
```


**`root/Card/Tables/Empty/Create`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/Card/Status`**

- `props.text`: expression

```js
coalesce({view.custom.msg}, '')
```

</details>

## Event Scripts And Handlers

- **`root/Head/New`** `component.onActionPerformed`, script action, scope `G`

```python
shared.Reports.open(None, {'origin': 'Saved Reports'}, self.session)
```

- **`root/Card/Tabs/Tab_mine`** `dom.onClick`, script action, scope `G`

```python
v = self.view.custom
v.tab = 'mine'
v.source = None
v.owner = None
v.msg = ''
```

- **`root/Card/Tabs/Tab_shared`** `dom.onClick`, script action, scope `G`

```python
v = self.view.custom
v.tab = 'shared'
v.source = None
v.owner = None
v.msg = ''
```

- **`root/Card/Tabs/Tab_runs`** `dom.onClick`, script action, scope `G`

```python
v = self.view.custom
v.tab = 'runs'
v.source = None
v.owner = None
v.msg = ''
```

- **`root/Card/Toolbar/Refresh`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.refresh += 1
```

- **`root/Card/Tables/Empty/Create`** `component.onActionPerformed`, script action, scope `G`

```python
shared.Reports.open(None, {'origin': 'Saved Reports'}, self.session)
```

- **`root`** message handler `rptPageDelete` (scope: page)

```python
res = shared.Reports.deleteTemplate(self.session, payload.get('id'))
self.view.custom.msg = res['message']
if res['ok']:
    self.view.custom.refresh += 1
```

- **`root`** message handler `rptSavedChanged` (scope: page)

```python
self.view.custom.msg = payload.get('message') or ''
self.view.custom.refresh += 1
```

Project script calls: [shared.Reports.deleteTemplate](../../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.savedModel](../../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Embeds** (1): [01\_Popups/Reports/\_Assets/SavedListRow](../../../01-popups/reports/assets/savedlistrow.md) (flex repeater)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-docked/tempnav.md)

## Style Classes

<details>
<summary>20 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 2 | style class |
| `bg-component` | 1 | stylesheet |
| `bg-page` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `form-btn` | 1 | style class |
| `form-btn-primary` | 2 | style class |
| `form-card` | 1 | style class |
| `form-input` | 3 | style class |
| `form-th` | 6 | style class |
| `fs-12` | 1 | style class |
| `fs-13` | 1 | style class |
| `fs-16` | 1 | style class |
| `fs-20` | 1 | style class |
| `fw-600` | 2 | style class |
| `fw-700` | 1 | style class |
| `report-heading` | 1 | style class |
| `report-hint` | 1 | style class |
| `report-tab` | 3 | style class |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
