---
title: "History"
sidebar_label: "History"
description: "Perspective view 00_Pages/Groveport/Operations/Forms/History (Page): 30 components, 14 bindings, 4 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/Forms/History", "History", "/operations/forms/history"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Operations/Forms/History`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/Forms/History` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/Forms/History/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; Forms &gt; History |
| Routes | `/operations/forms/history` (Form History) |
| Root | `ia.container.flex`, height 1000, width 1600 |
| Size | 30 components, 14 bindings, 4 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-24T01:16:15Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `end` | `null` | |
| `formType` | `""` | |
| `refresh` | `0` | |
| `start` | `null` | |
| `user` | `""` | |

## Component Tree

Component types: ia.container.flex x12, ia.display.label x9, ia.input.dropdown x2, ia.input.date-time-input x2, ia.input.button x2, ia.display.table x2, ia.container.tab x1.

<details>
<summary>Component tree (30 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  Head  ia.container.flex
    Title  ia.display.label
    Subtitle  ia.display.label
  Denied  ia.container.flex  [1 binding]
    DeniedMsg  ia.display.label
  Tabs  ia.container.tab  [1 binding]
    Forms  ia.container.flex
      Filters  ia.container.flex
        Form  ia.container.flex
          Cap  ia.display.label
          V  ia.input.dropdown  [1 binding]
        From  ia.container.flex
          Cap  ia.display.label
          V  ia.input.date-time-input  [1 binding]
        To  ia.container.flex
          Cap  ia.display.label
          V  ia.input.date-time-input  [1 binding]
        User  ia.container.flex  [1 binding]
          Cap  ia.display.label
          V  ia.input.dropdown  [2 bindings]
        Btn  ia.container.flex
          Refresh  ia.input.button  [1 event]
        ReportBtn  ia.container.flex
          GenerateReport  ia.input.button  [1 binding; 1 event]
        Scope  ia.display.label  [1 binding]
      Table  ia.display.table  [1 binding; 1 event]
    Cycles  ia.container.flex
      Hint  ia.display.label
      Table  ia.display.table  [1 binding]
```

</details>

## Bindings

14 bindings: expr 7, property 4, expr-struct 3.

<details>
<summary>All 14 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

**`root/Denied`**

- `position.display`: expression

```js
!coalesce({session.custom.Permissions.Forms.Use}, false)
```


**`root/Tabs`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false)
```


**`root/Tabs/Forms/Filters/Form/V`**

- `props.value`: property `view.custom.formType` (bidirectional)

**`root/Tabs/Forms/Filters/From/V`**

- `props.value`: property `view.custom.start` (bidirectional)

**`root/Tabs/Forms/Filters/To/V`**

- `props.value`: property `view.custom.end` (bidirectional)

**`root/Tabs/Forms/Filters/User`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.ViewAll}, false)
```


**`root/Tabs/Forms/Filters/User/V`**

- `props.options`: structured expression (expr-struct), then script transform

```js
viewAll: coalesce({session.custom.Permissions.Forms.ViewAll}, false)
```

waitOnAll: `False`

Transform 1, script:

```python
return shared.Forms.historyUsers(self.session)
```


- `props.value`: property `view.custom.user` (bidirectional)

**`root/Tabs/Forms/Filters/ReportBtn/GenerateReport`**

- `props.enabled`: expression

```js
coalesce({session.custom.Permissions.Reports.Use}, false)
```


**`root/Tabs/Forms/Filters/Scope`**

- `props.text`: expression

```js
if(coalesce({session.custom.Permissions.Forms.ViewAll}, false), "Showing Every User's Submissions", 'Showing Your Submissions Only')
```


**`root/Tabs/Forms/Table`**

- `props.data`: structured expression (expr-struct), then script transform

```js
allowed: coalesce({session.custom.Permissions.Forms.Use}, false)
end: {view.custom.end}
formType: {view.custom.formType}
refresh: {view.custom.refresh}
start: {view.custom.start}
user: {view.custom.user}
```

waitOnAll: `False`

Transform 1, script:

```python
return shared.Forms.history(self.session, value.formType, value.start, value.end, value.user)
```


**`root/Tabs/Cycles/Table`**

- `props.data`: structured expression (expr-struct), then script transform

```js
allowed: coalesce({session.custom.Permissions.Forms.Use}, false)
refresh: {view.custom.refresh}
```

waitOnAll: `False`

Transform 1, script:

```python
return shared.Forms.pidCycles(self.session)
```

</details>

## Event Scripts And Handlers

- **`root`** `system.onStartup`, script action, scope `G`

```python
self.view.custom.start = system.date.addDays(system.date.midnight(system.date.now()), -30)
self.view.custom.end = system.date.now()
```

- **`root/Tabs/Forms/Filters/Btn/Refresh`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.refresh += 1
```

- **`root/Tabs/Forms/Filters/ReportBtn/GenerateReport`** `component.onActionPerformed`, script action, scope `G`

```python
# redesign 2026-10-24: Report Builder on the Operations Forms source with this page's filters
ft = self.view.custom.formType
shared.Reports.open('forms', {'forms': [ft] if ft else [], 'start': self.view.custom.start, 'end': self.view.custom.end, 'origin': 'Form History'})
```

- **`root/Tabs/Forms/Table`** `component.onRowDoubleClick`, script action, scope `G`

```python
kind = self.props.data[event.row]['form_type']
rid = self.props.data[event.row]['id']
paths = {'DailyRounds': '00_Pages/Groveport/Operations/Forms/DailyRounds', 'ShiftLog': '00_Pages/Groveport/Operations/Forms/ShiftLog'}
system.perspective.openPopup(id='opsFormView', view=paths[kind], params={'readOnly': True, 'submissionId': rid}, title='', showCloseIcon=True, draggable=True, resizable=True, modal=True, overlayDismiss=True, position={'width': 1560, 'height': 880})
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Forms.history](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.historyUsers](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidCycles](../../../../../../../scripting/reference/modules/shared-forms.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [00\_Pages/Groveport/Operations/Forms/DailyRounds](./dailyrounds.md), [00\_Pages/Groveport/Operations/Forms/ShiftLog](./shiftlog.md), [00\_Pages/Groveport/Operations/Forms/\_Assets/HistoryActions](./assets/historyactions.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

## Style Classes

<details>
<summary>15 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 2 | style class |
| `Fonts/Label` | 7 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 5 | style class |
| `bg-component` | 7 | stylesheet |
| `bg-page` | 1 | style class |
| `container-button` | 2 | style class |
| `container-card` | 1 | stylesheet |
| `fs-11` | 4 | style class |
| `fs-12` | 2 | style class |
| `fs-13` | 1 | style class |
| `fs-16` | 1 | style class |
| `fs-20` | 1 | style class |
| `fw-600` | 5 | style class |
| `fw-700` | 1 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
