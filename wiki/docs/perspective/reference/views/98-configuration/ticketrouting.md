---
title: "TicketRouting"
sidebar_label: "TicketRouting"
description: "Perspective view 98_Configuration/TicketRouting (Configuration / tool view): 46 components, 32 bindings, 6 event scripts."
generated: true
keywords: ["98_Configuration/TicketRouting", "TicketRouting"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/TicketRouting`.

| | |
|---|---|
| View path | `98_Configuration/TicketRouting` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/TicketRouting/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; TicketRouting |
| Root | `ia.container.flex`, width 552, height 640 |
| Size | 46 components, 32 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `rev` | `0` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `rev` | `0` | not persistent |
| `data` | `null` | bound (expr) |
| `draft` | `null` | bound (expr) |
| `sel` | `-1` | not persistent |
| `edit` | `{"area": "", "boardId": "", "destination": "Monday", "groupId": "",...` | not persistent |
| `error` | `""` | not persistent |
| `note` | `""` | not persistent |
| `dirty` | `false` | bound (expr) |

## Component Tree

Component types: ia.container.flex x17, ia.display.label x15, ia.input.button x5, ia.input.dropdown x4, ia.input.text-field x4, ia.display.table x1.

<details>
<summary>Component tree (46 components)</summary>

```text
root  ia.container.flex
  Denied  ia.display.label  [1 binding]
  Content  ia.container.flex  [1 binding]
    Intro  ia.display.label
    DryRun  ia.display.label  [1 binding]
    Rules  ia.display.table  [2 bindings; 1 event]
    Editor  ia.container.flex
      Title  ia.display.label  [1 binding]
      Row1  ia.container.flex
        Type  ia.container.flex
          Label  ia.display.label
          Input  ia.input.dropdown  [2 bindings]
        Area  ia.container.flex
          Label  ia.display.label
          Input  ia.input.dropdown  [2 bindings]
        Destination  ia.container.flex
          Label  ia.display.label
          Input  ia.input.dropdown  [2 bindings]
      Row2  ia.container.flex
        Board  ia.container.flex
          Label  ia.display.label
          Input  ia.input.text-field  [2 bindings]
        Group  ia.container.flex
          Label  ia.display.label
          Input  ia.input.text-field  [2 bindings]
      Buttons  ia.container.flex
        Error  ia.display.label  [1 binding]
        New  ia.input.button  [1 event]
        Remove  ia.input.button  [1 binding; 1 event]
        Apply  ia.input.button  [1 binding; 1 event]
    Default  ia.container.flex
      Title  ia.display.label
      Row  ia.container.flex
        Destination  ia.container.flex
          Label  ia.display.label
          Input  ia.input.dropdown  [2 bindings]
        Board  ia.container.flex
          Label  ia.display.label
          Input  ia.input.text-field  [2 bindings]
        Group  ia.container.flex
          Label  ia.display.label
          Input  ia.input.text-field  [2 bindings]
    ActionBar  ia.container.flex
      Status  ia.display.label  [2 bindings]
      Discard  ia.input.button  [1 binding; 1 event]
      Save  ia.input.button  [1 binding; 1 event]
```

</details>

## Bindings

32 bindings: expr 19, property 13.

<details>
<summary>All 32 bindings, grouped by component</summary>

**`(view)`**

- `custom.data`: expression

```js
runScript('shared.TicketLogger.routingForView', 0, {view.custom.rev}, {view.params.rev})
```


- `custom.draft`: expression

```js
try({view.custom.data.routing}, null)
```


- `custom.dirty`: expression

```js
coalesce(try(runScript('shared.TicketLogger.isDirty', 0, {view.custom.draft}, {view.custom.data.routing}), false), false)
```


**`root/Denied`**

- `position.display`: expression

```js
!(!isNull(try({view.custom.data.routing}, null)))
```


**`root/Content`**

- `position.display`: expression

```js
!isNull(try({view.custom.data.routing}, null))
```


**`root/Content/DryRun`**

- `position.display`: expression

```js
coalesce(try({view.custom.data.dryRun}, false), false)
```


**`root/Content/Rules`**

- `props.data`: expression

```js
try(runScript('shared.TicketLogger.ruleRows', 0, {view.custom.draft.rules}), null)
```


- `props.selection.selectedRow`: expression

```js
if({view.custom.sel} >= 0, {view.custom.sel}, null)
```


**`root/Content/Editor/Title`**

- `props.text`: expression

```js
if({view.custom.sel} >= 0, 'Edit Rule ' + toStr({view.custom.sel} + 1), 'New Rule')
```


**`root/Content/Editor/Row1/Type/Input`**

- `props.options`: property `view.custom.data.typeOptions`

- `props.value`: property `view.custom.edit.type` (bidirectional)

**`root/Content/Editor/Row1/Area/Input`**

- `props.options`: property `view.custom.data.areaOptions`

- `props.value`: property `view.custom.edit.area` (bidirectional)

**`root/Content/Editor/Row1/Destination/Input`**

- `props.options`: property `view.custom.data.destOptions`

- `props.value`: property `view.custom.edit.destination` (bidirectional)

**`root/Content/Editor/Row2/Board/Input`**

- `props.text`: property `view.custom.edit.boardId` (bidirectional)

- `props.enabled`: expression

```js
coalesce({view.custom.edit.destination}, '') = 'Monday'
```


**`root/Content/Editor/Row2/Group/Input`**

- `props.text`: property `view.custom.edit.groupId` (bidirectional)

- `props.enabled`: expression

```js
coalesce({view.custom.edit.destination}, '') = 'Monday'
```


**`root/Content/Editor/Buttons/Error`**

- `props.text`: property `view.custom.error`

**`root/Content/Editor/Buttons/Remove`**

- `props.enabled`: expression

```js
{view.custom.sel} >= 0
```


**`root/Content/Editor/Buttons/Apply`**

- `props.text`: expression

```js
if({view.custom.sel} >= 0, 'Apply To Rule', 'Add Rule')
```


**`root/Content/Default/Row/Destination/Input`**

- `props.options`: property `view.custom.data.destOptions`

- `props.value`: property `view.custom.draft.default.destination` (bidirectional)

**`root/Content/Default/Row/Board/Input`**

- `props.text`: property `view.custom.draft.default.boardId` (bidirectional)

- `props.enabled`: expression

```js
coalesce({view.custom.draft.default.destination}, '') = 'Monday'
```


**`root/Content/Default/Row/Group/Input`**

- `props.text`: property `view.custom.draft.default.groupId` (bidirectional)

- `props.enabled`: expression

```js
coalesce({view.custom.draft.default.destination}, '') = 'Monday'
```


**`root/Content/ActionBar/Status`**

- `props.text`: expression

```js
if(coalesce({view.custom.dirty}, false), 'Unsaved Changes', coalesce({view.custom.note}, ''))
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.dirty}, false), 'form-status-error', 'form-status')
```


**`root/Content/ActionBar/Discard`**

- `props.enabled`: expression

```js
coalesce({view.custom.dirty}, false)
```


**`root/Content/ActionBar/Save`**

- `props.enabled`: expression

```js
coalesce({view.custom.dirty}, false)
```

</details>

## Event Scripts And Handlers

- **`root/Content/Rules`** `component.onRowClick`, script action, scope `G`

```python
# routing editor: load the clicked rule into the editor (nothing is saved until Save Routing)
try:
    i = int(event.value['idx']) - 1
except Exception:
    i = int(event.rowIndex)
d = shared.TicketLogger.normalize(self.view.custom.draft)
if 0 <= i < len(d['rules']):
    self.view.custom.sel = i
    self.view.custom.edit = d['rules'][i]
    self.view.custom.error = ''
    self.view.custom.note = ''
```

- **`root/Content/Editor/Buttons/New`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.sel = -1
self.view.custom.edit = {'type': '', 'area': '', 'destination': 'Monday', 'boardId': '', 'groupId': ''}
self.view.custom.error = ''
self.view.custom.note = ''
```

- **`root/Content/Editor/Buttons/Remove`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.draft = shared.TicketLogger.removeRule(self.view.custom.draft, self.view.custom.sel)
self.view.custom.sel = -1
self.view.custom.edit = {'type': '', 'area': '', 'destination': 'Monday', 'boardId': '', 'groupId': ''}
self.view.custom.error = ''
self.view.custom.note = 'Rule Removed - Save Routing To Apply'
```

- **`root/Content/Editor/Buttons/Apply`** `component.onActionPerformed`, script action, scope `G`

```python
res = shared.TicketLogger.applyRule(self.view.custom.draft, self.view.custom.sel, self.view.custom.edit)
self.view.custom.error = res[2]
if not res[2]:
    self.view.custom.draft = res[0]
    self.view.custom.sel = res[1]
    self.view.custom.note = 'Rule %d Updated - Save Routing To Apply' % (res[1] + 1)
```

- **`root/Content/ActionBar/Discard`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.draft = shared.TicketLogger.plain(self.view.custom.data['routing'])
self.view.custom.sel = -1
self.view.custom.edit = {'type': '', 'area': '', 'destination': 'Monday', 'boardId': '', 'groupId': ''}
self.view.custom.error = ''
self.view.custom.note = ''
```

- **`root/Content/ActionBar/Save`** `component.onActionPerformed`, script action, scope `G`

```python
d = shared.TicketLogger.normalize(self.view.custom.draft)
shared.Alerts.showAlert(state='info', title='Save Ticket Routing',
    message='Save %d Routing Rules With Default Destination %s? Tickets Submitted After This Use The New '
    'Routing.' % (len(d['rules']), d['default']['destination']), showCloseBtn=False, btnTextPrimary='Save',
    btnTextSecondary='Cancel', btnActionPrimary='tlRoutingSave', btnActionSecondary='', payload={},
    overlayDismiss=False)
```

- **`root`** message handler `tlRoutingSave` (scope: page)

```python
# confirmed in the alert: shared.TicketLogger.saveRouting re-checks TicketLogger/Settings, validates, writes the
# Routing tag and the OpsAudit entry
try:
    res = shared.TicketLogger.saveRouting(self.view.custom.draft, self.view.id)
except Exception as e:
    res = [False, str(e)]
if res[0]:
    self.view.custom.error = ''
    self.view.custom.note = res[1]
    self.view.custom.rev = (self.view.custom.rev or 0) + 1
    self.view.custom.sel = -1
    self.view.custom.edit = {'type': '', 'area': '', 'destination': 'Monday', 'boardId': '', 'groupId': ''}
else:
    self.view.custom.error = res[1]
```

Project script calls: [shared.TicketLogger.applyRule](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.isDirty](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.normalize](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.plain](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.removeRule](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.routingForView](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.ruleRows](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.saveRouting](../../../../scripting/reference/modules/shared-ticketlogger.md).

## Related Views

**Embedded in** (1): [98\_Configuration/TicketLoggerSettings](./ticketloggersettings.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `form-banner` | 1 | style class |
| `form-btn` | 3 | style class |
| `form-btn-primary` | 2 | style class |
| `form-card` | 3 | style class |
| `form-hint` | 1 | style class |
| `form-input` | 8 | style class |
| `form-label` | 8 | style class |
| `form-note` | 1 | style class |
| `form-section-title` | 2 | style class |
| `form-status` | 1 | style class |
| `form-status-error` | 1 | style class |

See the [style class catalog](../../style-classes.md) and the [stylesheet index](../../stylesheet.md).
