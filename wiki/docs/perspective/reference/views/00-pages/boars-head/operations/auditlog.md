---
title: "AuditLog"
sidebar_label: "AuditLog"
description: "Perspective view 00_Pages/Boars Head/Operations/AuditLog (Page): 62 components, 36 bindings, 6 event scripts."
generated: true
keywords: ["00_Pages/Boars Head/Operations/AuditLog", "AuditLog", "/operations/audit"]
---

:::note

:::


**Page**: `00_Pages/Boars Head/Operations/AuditLog`.

| | |
|---|---|
| View path | `00_Pages/Boars Head/Operations/AuditLog` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Operations/AuditLog/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Boars Head &gt; Operations &gt; AuditLog |
| Routes | `/operations/audit` (OPS Audit Log) |
| Root | `ia.container.flex`, height 900, width 1400 |
| Size | 62 components, 36 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-28T23:00:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `startDate` | `null` | bound (expr) |
| `endDate` | `null` | bound (expr) |
| `search` | `""` | |
| `refresh` | `0` | |
| `selected` | `{}` | |
| `showDetail` | `false` | |
| `narrow` | `false` | bound (expr) |
| `compact` | `false` | bound (expr) |

## Component Tree

Component types: ia.display.label x28, ia.container.flex x25, ia.input.button x5, ia.input.date-time-input x2, ia.input.text-field x1, ia.display.table x1.

<details>
<summary>Component tree (62 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    Title  ia.display.label
    Subtitle  ia.display.label  [2 bindings]
  Denied  ia.container.flex  [1 binding]
    DeniedMsg  ia.display.label
  Content  ia.container.flex  [1 binding]
    Filters  ia.container.flex
      Range  ia.container.flex
        Lbl  ia.display.label
        Buttons  ia.container.flex
          Last24  ia.input.button  [1 binding; 1 event]
          Last7  ia.input.button  [1 binding; 1 event]
          Last30  ia.input.button  [1 binding; 1 event]
      Start  ia.container.flex
        Lbl  ia.display.label
        V  ia.input.date-time-input  [1 binding]
      End  ia.container.flex
        Lbl  ia.display.label
        V  ia.input.date-time-input  [1 binding]
      Search  ia.container.flex
        Lbl  ia.display.label
        V  ia.input.text-field  [1 binding]
      Refresh  ia.input.button  [1 event]
    Body  ia.container.flex
      List  ia.container.flex  [1 binding]
        Table  ia.display.table  [3 bindings; 1 event]
      Detail  ia.container.flex  [3 bindings]
        Record  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label  [1 binding]
            Close  ia.input.button  [1 binding; 1 event]
          Body  ia.container.flex
            Time  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            User  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            Host  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            Action  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            Target  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            Area  ia.container.flex  [1 binding]
              K  ia.display.label
              V  ia.display.label  [1 binding]
            TagPath  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            Source  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            Status  ia.container.flex
              K  ia.display.label
              V  ia.display.label  [1 binding]
            ChangeTitle  ia.display.label
            Change  ia.display.label  [1 binding]
```

</details>

## Bindings

36 bindings: expr 30, property 3, expr-struct 2, query 1.

<details>
<summary>All 36 bindings, grouped by component</summary>

**`(view)`**

- `custom.narrow`: expression

```js
coalesce({page.props.dimensions.primaryView.width}, 1920) < 1500
```


- `custom.compact`: expression

```js
coalesce({page.props.dimensions.primaryView.width}, 1920) < 1000
```


- `custom.startDate`: expression

```js
dateArithmetic(now(0), -7, 'day')
```


- `custom.endDate`: expression

```js
dateArithmetic(now(0), 1, 'day')
```


**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`root/Header/Subtitle`**

- `props.text`: expression

```js
if(coalesce(try(len({../../Content/Body/List/Table.props.data}), 0), 0) >= 5000, 'Latest 5,000 Events (Limit) · Narrow The Range', toStr(coalesce(try(len({../../Content/Body/List/Table.props.data}), 0), 0)) + if(coalesce(try(len({../../Content/Body/List/Table.props.data}), 0), 0) = 1, ' Event', ' Events'))
```


- `position.display`: expression

```js
coalesce({session.custom.Permissions.AuditLog.View}, false)
```


**`root/Denied`**

- `position.display`: expression

```js
!coalesce({session.custom.Permissions.AuditLog.View}, false)
```


**`root/Content`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.AuditLog.View}, false)
```


**`root/Content/Filters/Range/Buttons/Last24`**

- `props.style.classes`: expression

```js
if(abs(coalesce(try(dateDiff({view.custom.startDate}, {view.custom.endDate}, 'minute'), -1), -1) - 2880) <= 60, 'form-btn-primary', 'form-btn')
```


**`root/Content/Filters/Range/Buttons/Last7`**

- `props.style.classes`: expression

```js
if(abs(coalesce(try(dateDiff({view.custom.startDate}, {view.custom.endDate}, 'minute'), -1), -1) - 11520) <= 60, 'form-btn-primary', 'form-btn')
```


**`root/Content/Filters/Range/Buttons/Last30`**

- `props.style.classes`: expression

```js
if(abs(coalesce(try(dateDiff({view.custom.startDate}, {view.custom.endDate}, 'minute'), -1), -1) - 44640) <= 60, 'form-btn-primary', 'form-btn')
```


**`root/Content/Filters/Start/V`**

- `props.value`: property `view.custom.startDate` (bidirectional)

**`root/Content/Filters/End/V`**

- `props.value`: property `view.custom.endDate` (bidirectional)

**`root/Content/Filters/Search/V`**

- `props.text`: property `view.custom.search` (bidirectional)

**`root/Content/Body/List`**

- `position.display`: expression

```js
!(coalesce({view.custom.narrow}, false) && coalesce({view.custom.showDetail}, false))
```


**`root/Content/Body/List/Table`**

- `props.data`: named query

Named query `OpsAudit/AuditLog`, return format `dataset`

```js
startDate: {view.custom.startDate}
endDate: {view.custom.endDate}
search: if(trim(coalesce({view.custom.search}, '')) = '', '', '%' + trim(coalesce({view.custom.search}, '')) + '%')
allowed: if(coalesce({session.custom.Permissions.AuditLog.View}, false), 1, 0)
refresh: coalesce({view.custom.refresh}, 0)
```


- `props.columns[5].visible`: expression

```js
!coalesce({view.custom.compact}, false)
```


- `props.columns[3].width`: expression

```js
if(coalesce({view.custom.narrow}, false), 210, 250)
```


**`root/Content/Body/Detail`**

- `position.display`: expression

```js
coalesce({view.custom.showDetail}, false)
```


- `position.basis`: expression

```js
if(coalesce({view.custom.narrow}, false), '0', '400px')
```


- `position.grow`: expression

```js
if(coalesce({view.custom.narrow}, false), 1, 0)
```


**`root/Content/Body/Detail/Record/Head/Title`**

- `props.text`: expression

```js
'Event ' + toStr(coalesce(try({view.custom.selected.id}, ''), ''))
```


**`root/Content/Body/Detail/Record/Head/Close`**

- `props.text`: expression

```js
if(coalesce({view.custom.narrow}, false), 'Back To List', 'Close')
```


**`root/Content/Body/Detail/Record/Body/Time/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.selected.time_text}, ''), '')
```


**`root/Content/Body/Detail/Record/Body/User/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.selected.actor}, ''), '')
```


**`root/Content/Body/Detail/Record/Body/Host/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.selected.actor_host}, ''), '')
```


**`root/Content/Body/Detail/Record/Body/Action/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.selected.action_text}, ''), '')
```


**`root/Content/Body/Detail/Record/Body/Target/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.selected.target_text}, ''), '')
```


**`root/Content/Body/Detail/Record/Body/Area`**

- `position.display`: expression

```js
coalesce(try({view.custom.selected.area}, ''), '') != ''
```


**`root/Content/Body/Detail/Record/Body/Area/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.selected.area}, ''), '')
```


**`root/Content/Body/Detail/Record/Body/TagPath/V`**

- `props.text`: expression

```js
if(coalesce(try({view.custom.selected.tag_path}, ''), '') != '', coalesce(try({view.custom.selected.tag_path}, ''), ''), coalesce(try({view.custom.selected.action_target}, ''), ''))
```


**`root/Content/Body/Detail/Record/Body/Source/V`**

- `props.text`: expression

```js
coalesce(try({view.custom.selected.source_text}, ''), '') + if(coalesce(try({view.custom.selected.view_path}, ''), '') != '' && coalesce(try({view.custom.selected.view_path}, ''), '') != coalesce(try({view.custom.selected.source_text}, ''), ''), ' (' + coalesce(try({view.custom.selected.view_path}, ''), '') + ')', '')
```


**`root/Content/Body/Detail/Record/Body/Status/V`**

- `props.text`: expression

```js
toStr(coalesce(try({view.custom.selected.status_code}, ''), ''))
```


**`root/Content/Body/Detail/Record/Body/Change`**

- `props.text`: expression

```js
if(coalesce(try({view.custom.selected.change_full}, ''), '') != '', coalesce(try({view.custom.selected.change_full}, ''), ''), '(No Value)')
```

</details>

## Event Scripts And Handlers

- **`root/Content/Filters/Range/Buttons/Last24`** `component.onActionPerformed`, script action, scope `G`

```python
# quick range: the last 24 hours up to tomorrow (new events stay in range; Refresh re-runs the query)
now = system.date.now()
self.view.custom.startDate = system.date.addHours(now, -24)
self.view.custom.endDate = system.date.addDays(now, 1)
```

- **`root/Content/Filters/Range/Buttons/Last7`** `component.onActionPerformed`, script action, scope `G`

```python
# quick range: the last 168 hours up to tomorrow (new events stay in range; Refresh re-runs the query)
now = system.date.now()
self.view.custom.startDate = system.date.addHours(now, -168)
self.view.custom.endDate = system.date.addDays(now, 1)
```

- **`root/Content/Filters/Range/Buttons/Last30`** `component.onActionPerformed`, script action, scope `G`

```python
# quick range: the last 720 hours up to tomorrow (new events stay in range; Refresh re-runs the query)
now = system.date.now()
self.view.custom.startDate = system.date.addHours(now, -720)
self.view.custom.endDate = system.date.addDays(now, 1)
```

- **`root/Content/Filters/Refresh`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.refresh = (self.view.custom.refresh or 0) + 1
```

- **`root/Content/Body/List/Table`** `component.onRowClick`, script action, scope `G`

```python
# row detail = a copy of the clicked row (full values); narrow screens: the detail replaces the table
row = event.value
try:
    self.view.custom.selected = dict((k, row[k]) for k in row)
except:
    self.view.custom.selected = dict(row)
self.view.custom.showDetail = True
```

- **`root/Content/Body/Detail/Record/Head/Close`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.showDetail = False
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [00\_Pages/Boars Head/Operations/\_Assets/AuditLogCell](./assets/auditlogcell.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-docked/tempnav.md)

**Named in project scripts**: [Navigation.Nav](../../../../../../scripting/reference/modules/navigation-nav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `form-btn` | 5 | style class |
| `form-card` | 4 | style class |
| `form-check` | 10 | style class |
| `form-input` | 3 | style class |
| `form-label` | 13 | style class |
| `form-section-head` | 1 | style class |
| `form-section-title` | 2 | style class |
| `form-status` | 1 | style class |
| `form-th` | 1 | style class |
| `form-title` | 1 | style class |
| `form-btn-primary` | bound | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Named queries: `OpsAudit/AuditLog`.

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
