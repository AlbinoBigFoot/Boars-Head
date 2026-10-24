---
title: "OutOfServiceLog"
sidebar_label: "OutOfServiceLog"
description: "Perspective view 00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog (Page): 87 components, 70 bindings, 9 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog", "OutOfServiceLog", "/operations/out-of-service", "/operations/out-of-service/:device"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; OutOfService &gt; OutOfServiceLog |
| Routes | `/operations/out-of-service` (Out Of Service Log)<br/>`/operations/out-of-service/:device` (Out Of Service History) |
| Root | `ia.container.flex`, height 900, width 1400 |
| Size | 87 components, 70 bindings, 9 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `device` | `""` | input |

## Custom properties

<details>
<summary>19 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `filter` | `"open"` | bound (expr) |
| `search` | `""` | |
| `devicePath` | `""` | bound (expr) |
| `startDate` | `null` | bound (expr) |
| `endDate` | `null` | bound (expr) |
| `refresh` | `0` | |
| `selectedId` | `-1` | |
| `activeId` | `-1` | bound (expr) |
| `records` | `null` | bound (query) |
| `record` | `null` | bound (query) |
| `comments` | `[]` | bound (query) |
| `hasRecord` | `false` | bound (expr) |
| `recordOpen` | `false` | bound (expr) |
| `commentText` | `""` | |
| `commentStatus` | `""` | |
| `commentError` | `""` | |
| `narrow` | `false` | bound (expr) |
| `compact` | `false` | bound (expr) |
| `showDetail` | `false` | |

</details>

## Component Tree

Component types: ia.display.label x37, ia.container.flex x34, ia.input.button x8, ia.input.dropdown x2, ia.input.date-time-input x2, ia.input.text-field x1, ia.display.table x1, ia.display.flex-repeater x1, ia.input.text-area x1.

<details>
<summary>Component tree (87 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    TitleBlock  ia.container.flex
      Title  ia.display.label  [1 binding]
      Subtitle  ia.display.label  [3 bindings]
    AllDevices  ia.input.button  [1 binding; 1 event]
  Filters  ia.container.flex
    Show  ia.container.flex
      Lbl  ia.display.label
      V  ia.input.dropdown  [1 binding]
    From  ia.container.flex
      Lbl  ia.display.label
      V  ia.input.date-time-input  [1 binding]
    To  ia.container.flex
      Lbl  ia.display.label
      V  ia.input.date-time-input  [1 binding]
    Search  ia.container.flex
      Lbl  ia.display.label
      V  ia.input.text-field  [1 binding]
    Refresh  ia.input.button  [1 event]
    GenerateReport  ia.input.button  [1 binding; 1 event]
    Rows  ia.display.label  [1 binding]
  Denied  ia.container.flex  [1 binding]
    DeniedMsg  ia.display.label
  Content  ia.container.flex  [1 binding]
    List  ia.container.flex  [1 binding]
      Table  ia.display.table  [4 bindings; 1 event]
    Detail  ia.container.flex  [3 bindings]
      Back  ia.input.button  [1 binding; 1 event]
      NoSelection  ia.display.label  [1 binding]
      Record  ia.container.flex  [1 binding]
        Head  ia.container.flex  [2 bindings]
          Title  ia.display.label  [1 binding]
        Body  ia.container.flex
          Status  ia.display.label  [2 bindings]
          Area  ia.container.flex
            K  ia.display.label
            V  ia.display.label  [1 binding]
          Reason  ia.container.flex
            K  ia.display.label
            V  ia.display.label  [1 binding]
          TakenBy  ia.container.flex
            K  ia.display.label
            V  ia.display.label  [1 binding]
          TakenAt  ia.container.flex
            K  ia.display.label
            V  ia.display.label  [1 binding]
          Duration  ia.container.flex
            K  ia.display.label
            V  ia.display.label  [1 binding]
          MemoTitle  ia.display.label
          Memo  ia.display.label  [1 binding]
          Actions  ia.container.flex
            OpenFaceplate  ia.input.button  [1 binding; 1 event]
            History  ia.input.button  [1 binding; 1 event]
            Return  ia.input.button  [1 binding; 1 event]
      Returned  ia.container.flex  [1 binding]
        Head  ia.container.flex
          Title  ia.display.label
        Body  ia.container.flex
          By  ia.container.flex
            K  ia.display.label
            V  ia.display.label  [1 binding]
          At  ia.container.flex
            K  ia.display.label
            V  ia.display.label  [1 binding]
          MemoTitle  ia.display.label
          Memo  ia.display.label  [1 binding]
      Thread  ia.container.flex  [1 binding]
        Head  ia.container.flex
          Title  ia.display.label  [1 binding]
        Body  ia.container.flex
          Entries  ia.display.flex-repeater  [1 binding; view: 00_Pages/Boars Head/Operations/OutOfService/_Assets/CommentEntry]
          Empty  ia.display.label  [1 binding]
      AddComment  ia.container.flex  [1 binding]
        Head  ia.container.flex
          Title  ia.display.label
        Body  ia.container.flex
          StatusRow  ia.container.flex  [1 binding]
            Lbl  ia.display.label
            V  ia.input.dropdown  [1 binding]
          Text  ia.input.text-area  [1 binding]
          Foot  ia.container.flex
            Count  ia.display.label  [2 bindings]
            Add  ia.input.button  [1 binding; 1 event]
          Error  ia.display.label  [2 bindings]
      ReadOnlyNote  ia.display.label  [1 binding]
```

</details>

## Bindings

70 bindings: expr 58, property 9, query 3.

<details>
<summary>All 70 bindings, grouped by component</summary>

**`(view)`**

- `custom.devicePath`: expression

```js
if(indexOf(coalesce({page.props.path}, ''), '/operations/out-of-service/') >= 0 && trim(coalesce({view.params.device}, '')) != '', '[default]' + replace(trim({view.params.device}), '~', '/'), '')
```


- `custom.narrow`: expression

```js
coalesce({page.props.dimensions.primaryView.width}, 1920) < 1500
```


- `custom.compact`: expression

```js
coalesce({page.props.dimensions.primaryView.width}, 1920) < 900
```


- `custom.filter`: expression

```js
if(coalesce({view.custom.devicePath}, '') != '', 'all', 'open')
```


- `custom.startDate`: expression

```js
dateArithmetic(now(0), -365, 'day')
```


- `custom.endDate`: expression

```js
dateArithmetic(now(0), 1, 'day')
```


- `custom.records`: named query

Named query `OutOfService/Records`, return format `dataset`

```js
allowed: if(coalesce({session.custom.Permissions.OutOfService.View}, false), 1, 0)
filter: coalesce({view.custom.filter}, 'open')
search: if(trim(coalesce({view.custom.search}, '')) = '', '', '%' + trim(coalesce({view.custom.search}, '')) + '%')
device: coalesce({view.custom.devicePath}, '')
startDate: {view.custom.startDate}
endDate: {view.custom.endDate}
now: now(60000)
refresh: coalesce({view.custom.refresh}, 0)
```


- `custom.activeId`: expression

```js
if(coalesce({view.custom.selectedId}, -1) >= 0 && coalesce(try(lookup({view.custom.records}, {view.custom.selectedId}, -1, 'id', 'id'), -1), -1) >= 0, {view.custom.selectedId}, coalesce(try(toInt({view.custom.records}[0, 'id']), -1), -1))
```


- `custom.record`: named query

Named query `OutOfService/Record`, return format `dataset`

```js
allowed: if(coalesce({session.custom.Permissions.OutOfService.View}, false), 1, 0)
id: coalesce({view.custom.activeId}, -1)
now: now(60000)
refresh: coalesce({view.custom.refresh}, 0)
```


- `custom.comments`: named query

Named query `OutOfService/Comments`, return format `json`

```js
allowed: if(coalesce({session.custom.Permissions.OutOfService.View}, false), 1, 0)
id: coalesce({view.custom.activeId}, -1)
refresh: coalesce({view.custom.refresh}, 0)
```


- `custom.hasRecord`: expression

```js
coalesce(try(len({view.custom.record}) > 0, false), false)
```


- `custom.recordOpen`: expression

```js
coalesce({view.custom.hasRecord}, false) && coalesce(try(isNull({view.custom.record}[0, 'returned_at']), false), false)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Header/TitleBlock/Title`**

- `props.text`: expression

```js
if(coalesce({view.custom.devicePath}, '') != '', 'Device History · ' + coalesce(try(split(replace(coalesce({view.custom.devicePath}, ''), '[default]', ''), '/')[len(split(replace(coalesce({view.custom.devicePath}, ''), '[default]', ''), '/')) - 1, 0], ''), ''), 'Out Of Service Log')
```


**`root/Header/TitleBlock/Subtitle`**

- `props.text`: expression

```js
if(coalesce({view.custom.devicePath}, '') != '', coalesce(try(split(replace(coalesce({view.custom.devicePath}, ''), '[default]', ''), '/')[2, 0], ''), '') + if(coalesce(try(split(replace(coalesce({view.custom.devicePath}, ''), '[default]', ''), '/')[1, 0], ''), '') != '', ' · ' + coalesce(try(split(replace(coalesce({view.custom.devicePath}, ''), '[default]', ''), '/')[1, 0], ''), ''), ''), 'Equipment Taken Out Of Service: Why And By Whom, Notes And Comments, And When It Was Returned To Service. Select A Row To See The Full Record.')
```


- `meta.tooltip.enabled`: expression

```js
coalesce({view.custom.devicePath}, '') != ''
```


- `meta.tooltip.text`: expression

```js
coalesce({view.custom.devicePath}, '')
```


**`root/Header/AllDevices`**

- `position.display`: expression

```js
coalesce({view.custom.devicePath}, '') != ''
```


**`root/Filters/Show/V`**

- `props.value`: property `view.custom.filter` (bidirectional)

**`root/Filters/From/V`**

- `props.value`: property `view.custom.startDate` (bidirectional)

**`root/Filters/To/V`**

- `props.value`: property `view.custom.endDate` (bidirectional)

**`root/Filters/Search/V`**

- `props.text`: property `view.custom.search` (bidirectional)

**`root/Filters/GenerateReport`**

- `props.enabled`: expression

```js
coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/Filters/Rows`**

- `props.text`: expression

```js
toStr(coalesce(try(len({view.custom.records}), 0), 0)) + ' Records'
```


**`root/Denied`**

- `position.display`: expression

```js
!coalesce({session.custom.Permissions.OutOfService.View}, false)
```


**`root/Content`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.OutOfService.View}, false)
```


**`root/Content/List`**

- `position.display`: expression

```js
!(coalesce({view.custom.narrow}, false) && coalesce({view.custom.showDetail}, false))
```


**`root/Content/List/Table`**

- `props.data`: property `view.custom.records`

- `props.columns[6].visible`: expression

```js
!coalesce({view.custom.compact}, false)
```


- `props.columns[5].visible`: expression

```js
!coalesce({view.custom.compact}, false)
```


- `props.columns[1].strictWidth`: expression

```js
!coalesce({view.custom.compact}, false)
```


**`root/Content/Detail`**

- `position.display`: expression

```js
!coalesce({view.custom.narrow}, false) || coalesce({view.custom.showDetail}, false)
```


- `position.basis`: expression

```js
if(coalesce({view.custom.narrow}, false), '0', '420px')
```


- `position.grow`: expression

```js
if(coalesce({view.custom.narrow}, false), 1, 0)
```


**`root/Content/Detail/Back`**

- `position.display`: expression

```js
coalesce({view.custom.narrow}, false)
```


**`root/Content/Detail/NoSelection`**

- `position.display`: expression

```js
!coalesce({view.custom.hasRecord}, false)
```


**`root/Content/Detail/Record`**

- `position.display`: expression

```js
coalesce({view.custom.hasRecord}, false)
```


**`root/Content/Detail/Record/Head`**

- `meta.tooltip.enabled`: expression

```js
coalesce({view.custom.hasRecord}, false)
```


- `meta.tooltip.text`: expression

```js
coalesce(try({view.custom.record}[0, 'tag_path'], ''), '')
```


**`root/Content/Detail/Record/Head/Title`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'device_name'], ''), '')
```


**`root/Content/Detail/Record/Body/Status`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'status'], ''), '')
```


- `props.style.classes`: expression

```js
'oos-chip fs-11 fw-700 ' + case(coalesce(try({view.custom.record}[0, 'status'], ''), ''), 'Returned', 'oos-chip-returned', 'In Progress', 'oos-chip-progress', 'Ready To Return', 'oos-chip-ready', 'Awaiting Parts', 'oos-chip-waiting', 'On Hold', 'oos-chip-waiting', '')
```


**`root/Content/Detail/Record/Body/Area/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'area'], ''), '') + if(coalesce(try({view.custom.record}[0, 'site'], ''), '') != '', ' (' + coalesce(try({view.custom.record}[0, 'site'], ''), '') + ')', '') + if(coalesce(try({view.custom.record}[0, 'device_type'], ''), '') != '', ' · ' + coalesce(try({view.custom.record}[0, 'device_type'], ''), ''), '')
```


**`root/Content/Detail/Record/Body/Reason/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'reason'], ''), '')
```


**`root/Content/Detail/Record/Body/TakenBy/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'taken_name'], ''), '') + if(coalesce(try({view.custom.record}[0, 'taken_by'], ''), '') != '', ' (' + coalesce(try({view.custom.record}[0, 'taken_by'], ''), '') + ')', '')
```


**`root/Content/Detail/Record/Body/TakenAt/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'taken_at_text'], ''), '')
```


**`root/Content/Detail/Record/Body/Duration/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'duration'], ''), '')
```


**`root/Content/Detail/Record/Body/Memo`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'memo'], ''), '')
```


**`root/Content/Detail/Record/Body/Actions/OpenFaceplate`**

- `position.display`: expression

```js
coalesce({session.custom.CanOpenFaceplates}, false)
```


**`root/Content/Detail/Record/Body/Actions/History`**

- `position.display`: expression

```js
coalesce({view.custom.devicePath}, '') != coalesce(try({view.custom.record}[0, 'tag_path'], ''), '')
```


**`root/Content/Detail/Record/Body/Actions/Return`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.OutOfService.Set}, false) && coalesce({view.custom.recordOpen}, false)
```


**`root/Content/Detail/Returned`**

- `position.display`: expression

```js
coalesce({view.custom.hasRecord}, false) && !coalesce({view.custom.recordOpen}, false)
```


**`root/Content/Detail/Returned/Body/By/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'returned_name'], ''), '') + if(coalesce(try({view.custom.record}[0, 'returned_by'], ''), '') != '', ' (' + coalesce(try({view.custom.record}[0, 'returned_by'], ''), '') + ')', '')
```


**`root/Content/Detail/Returned/Body/At/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'returned_at_text'], ''), '')
```


**`root/Content/Detail/Returned/Body/Memo`**

- `props.text`: expression

```js
coalesce(try({view.custom.record}[0, 'return_memo'], ''), '')
```


**`root/Content/Detail/Thread`**

- `position.display`: expression

```js
coalesce({view.custom.hasRecord}, false)
```


**`root/Content/Detail/Thread/Head/Title`**

- `props.text`: expression

```js
'Comments & Status Updates (' + toStr(coalesce(try(len({view.custom.comments}), 0), 0)) + ')'
```


**`root/Content/Detail/Thread/Body/Entries`**

- `props.instances`: property `view.custom.comments`

**`root/Content/Detail/Thread/Body/Empty`**

- `position.display`: expression

```js
coalesce(try(len({view.custom.comments}), 0), 0) = 0
```


**`root/Content/Detail/AddComment`**

- `position.display`: expression

```js
coalesce({view.custom.hasRecord}, false) && coalesce({session.custom.Permissions.OutOfService.Comment}, false)
```


**`root/Content/Detail/AddComment/Body/StatusRow`**

- `position.display`: expression

```js
coalesce({view.custom.recordOpen}, false)
```


**`root/Content/Detail/AddComment/Body/StatusRow/V`**

- `props.value`: property `view.custom.commentStatus` (bidirectional)

**`root/Content/Detail/AddComment/Body/Text`**

- `props.text`: property `view.custom.commentText` (bidirectional)

**`root/Content/Detail/AddComment/Body/Foot/Count`**

- `props.text`: expression

```js
if(len(trim(coalesce({view.custom.commentText}, ''))) >= 10, toStr(len(trim(coalesce({view.custom.commentText}, '')))) + ' Characters', toStr(len(trim(coalesce({view.custom.commentText}, '')))) + ' / 10 Characters Minimum')
```


- `props.style.classes`: expression

```js
if(len(trim(coalesce({view.custom.commentText}, ''))) >= 10, 'Fonts/Label fs-11 text-ok', 'Fonts/Label fs-11 text-muted')
```


**`root/Content/Detail/AddComment/Body/Foot/Add`**

- `props.enabled`: expression

```js
len(trim(coalesce({view.custom.commentText}, ''))) >= 10
```


**`root/Content/Detail/AddComment/Body/Error`**

- `props.text`: property `view.custom.commentError`

- `position.display`: expression

```js
coalesce({view.custom.commentError}, '') != ''
```


**`root/Content/Detail/ReadOnlyNote`**

- `position.display`: expression

```js
coalesce({view.custom.hasRecord}, false) && !coalesce({session.custom.Permissions.OutOfService.Comment}, false)
```

</details>

## Event Scripts And Handlers

- **`root/Header/AllDevices`** `component.onActionPerformed`, script action, scope `G`

```python
# clear the device param too (same view instance on both routes), then the all-devices route
try:
    self.view.params.device = ''
except:
    pass
self.view.custom.selectedId = -1
self.view.custom.showDetail = False
system.perspective.navigate(page='/operations/out-of-service')
```

- **`root/Filters/Refresh`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.refresh = (self.view.custom.refresh or 0) + 1
```

- **`root/Filters/GenerateReport`** `component.onActionPerformed`, script action, scope `G`

```python
# redesign 2026-10-24: Report Builder on the Out Of Service source with this page's From / To dates
shared.Reports.open('oos', {'start': self.view.custom.startDate, 'end': self.view.custom.endDate, 'origin': 'Out Of Service Log'})
```

- **`root/Content/List/Table`** `component.onRowClick`, script action, scope `G`

```python
# selection kept in view.custom (the table re-queries every minute for the durations); tablet: open detail
self.view.custom.selectedId = event.value['id']
self.view.custom.showDetail = True
```

- **`root/Content/Detail/Back`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.showDetail = False
```

- **`root/Content/Detail/Record/Body/Actions/OpenFaceplate`** `component.onActionPerformed`, script action, scope `G`

```python
tp = self.view.custom.record.getValueAt(0, 'tag_path') if self.view.custom.record.getRowCount() else ''
if tp:
    Navigation.Faceplate.openDevice(tp)
```

- **`root/Content/Detail/Record/Body/Actions/History`** `component.onActionPerformed`, script action, scope `G`

```python
# every Out Of Service record of this device (route /operations/out-of-service/:device)
ds = self.view.custom.record
if ds is not None and ds.getRowCount():
    shared.OutOfService.openHistory(ds.getValueAt(0, 'tag_path'))
```

- **`root/Content/Detail/Record/Body/Actions/Return`** `component.onActionPerformed`, script action, scope `G`

```python
# same memo dialog + server handler as the device right-click menu (OutOfService/Set re-checked there)
ds = self.view.custom.record
if ds is not None and ds.getRowCount():
    shared.OutOfService.openDialog(ds.getValueAt(0, 'tag_path'), self.view.id.split('@')[0], False)
```

- **`root/Content/Detail/AddComment/Body/Foot/Add`** `component.onActionPerformed`, script action, scope `G`

```python
# one-shot command: shared.OutOfService.addComment re-checks OutOfService/Comment, the length and the record
# (returned records take comments, no status change); username / time come from the session on the gateway
res = shared.OutOfService.addComment(self.session, self.view.custom.activeId, self.view.custom.commentStatus,
    self.view.custom.commentText)
if res.get('ok'):
    self.view.custom.commentText = ''
    self.view.custom.commentStatus = ''
    self.view.custom.commentError = ''
    self.view.custom.refresh = (self.view.custom.refresh or 0) + 1
else:
    self.view.custom.commentError = res.get('error') or 'Not Saved'
```

- **`root`** message handler `oosChanged` (scope: session)

```python
# Out Of Service change in this session (memo dialog, comment): requery the list, record and thread
self.view.custom.refresh = (self.view.custom.refresh or 0) + 1
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.OutOfService.addComment](../../../../../../../scripting/reference/modules/shared-outofservice.md).

## Related Views

**Embeds** (1): [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/CommentEntry](./assets/commententry.md) (flex repeater)

**Opens or names** (popups, scripts, expressions): [00\_Pages/Boars Head/Operations/OutOfService/\_Assets/TwoLineCell](./assets/twolinecell.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

**Named in project scripts**: [shared.OutOfService](../../../../../../../scripting/reference/modules/shared-outofservice.md)

## Style Classes

<details>
<summary>24 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `bg-page` | 1 | style class |
| `form-btn` | 6 | style class |
| `form-btn-primary` | 2 | style class |
| `form-card` | 8 | style class |
| `form-check` | 9 | style class |
| `form-hint` | 3 | style class |
| `form-input` | 6 | style class |
| `form-label` | 12 | style class |
| `form-section-head` | 4 | style class |
| `form-section-title` | 5 | style class |
| `form-status` | 1 | style class |
| `form-subtitle` | 1 | style class |
| `form-th` | 2 | style class |
| `form-title` | 1 | style class |
| `fs-11` | 2 | style class |
| `fs-12` | 1 | style class |
| `fw-600` | 1 | style class |
| `fw-700` | 1 | style class |
| `oos-chip` | 1 | stylesheet |
| `oos-memo` | 2 | stylesheet |
| `text-muted` | 1 | style class |
| `status` | bound | stylesheet |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Named queries: `OutOfService/Comments`, `OutOfService/Record`, `OutOfService/Records`.

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
