---
title: "TicketLogger"
sidebar_label: "TicketLogger"
description: "Perspective view 98_Configuration/TicketLogger (Configuration / tool view): 51 components, 43 bindings, 3 event scripts."
generated: true
keywords: ["98_Configuration/TicketLogger", "TicketLogger"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/TicketLogger`.

| | |
|---|---|
| View path | `98_Configuration/TicketLogger` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/TicketLogger/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; TicketLogger |
| Root | `ia.container.flex`, height 740, width 580 |
| Size | 51 components, 43 bindings, 3 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-07-24T18:40:04Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `viewName` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `mode` | `"ticket"` | not persistent |
| `type` | `"Issue"` | |
| `fieldKeys` | `""` | bound (expr) |
| `types` | `null` | bound (tag) |
| `fields` | `null` | bound (tag) |
| `route` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x19, ia.display.label x19, ia.input.text-area x6, ia.display.icon x2, ia.input.dropdown x2, ia.input.button x2, ia.display.view x1.

<details>
<summary>Component tree (51 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    Icon  ia.display.icon
    Title  ia.display.label  [1 binding]
    Settings  ia.display.icon  [3 bindings; 1 event]
  Integrations  ia.display.view  [1 binding; view: 98_Configuration/TicketLoggerSettings]
  TagPathContainer  ia.container.flex  [1 binding]
    Label  ia.display.label
    TagPath  ia.display.label  [1 binding]
  ViewName  ia.container.flex  [1 binding]
    Label  ia.display.label
    Name  ia.display.label  [1 binding]
  IssueData  ia.container.flex  [1 binding]
    IssueTimePriority  ia.container.flex
      IssuerName  ia.container.flex
        Label  ia.display.label
        Name  ia.display.label  [1 binding]
      IssueDate  ia.container.flex
        Label  ia.display.label
        Date  ia.display.label  [1 binding]
      IssuePriority  ia.container.flex
        Label  ia.display.label
        PriorityDropdown  ia.input.dropdown
      IssueType  ia.container.flex
        TypeRow  ia.container.flex
          Label  ia.display.label
          TypeDropdown  ia.input.dropdown  [2 bindings]
        TypeHelp  ia.display.label  [1 binding]
        RouteHint  ia.display.label  [1 binding]
  Results  ia.container.flex  [1 binding]
    Field_expected  ia.container.flex  [1 binding]
      Label  ia.display.label  [1 binding]
      TextBox  ia.input.text-area  [1 binding]
    Field_actual  ia.container.flex  [1 binding]
      Label  ia.display.label  [1 binding]
      TextBox  ia.input.text-area  [1 binding]
    Field_steps  ia.container.flex  [1 binding]
      Label  ia.display.label  [1 binding]
      TextBox  ia.input.text-area  [1 binding]
    Field_details  ia.container.flex  [1 binding]
      Label  ia.display.label  [1 binding]
      TextBox  ia.input.text-area  [1 binding]
    Field_reason  ia.container.flex  [1 binding]
      Label  ia.display.label  [1 binding]
      TextBox  ia.input.text-area  [1 binding]
    Field_question  ia.container.flex  [1 binding]
      Label  ia.display.label  [1 binding]
      TextBox  ia.input.text-area  [1 binding]
  Buttons  ia.container.flex  [1 binding]
    SendButton  ia.input.button  [1 binding; 1 event]
    CloseButton  ia.input.button  [1 event]
```

</details>

## Bindings

43 bindings: expr 32, property 6, tag 3, expr-struct 2.

<details>
<summary>All 43 bindings, grouped by component</summary>

**`(view)`**

- `custom.types`: tag

Mode `direct`, tag path `[default]_Config/TicketLogger/Types`, fallback delay 2.5 s


- `custom.fields`: tag

Mode `direct`, tag path `[default]_Config/TicketLogger/Fields`, fallback delay 2.5 s


- `custom.fieldKeys`: expression

```js
',' + replace(coalesce(try(lookup({view.custom.types}, {view.custom.type}, '', 'Type', 'Fields'), ''), ''), ' ', '') + ','
```


- `custom.route`: expression

```js
coalesce(try(runScript('shared.TicketLogger.routeLabel', 0, {view.custom.type}, {view.params.tagPath}), ''), '')
```


**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../common-patterns.md#pattern-4).

**`root/Header/Title`**

- `props.text`: expression

```js
if({view.custom.mode} = 'settings', 'Ticket Logger Settings', 'Ticket Logger')
```


**`root/Header/Settings`**

- `meta.visible`: property `session.custom.TicketLogSettings`

- `props.path`: expression

```js
if({view.custom.mode} = 'settings', 'material/close', 'material/settings')
```


- `meta.tooltip.text`: expression

```js
if({view.custom.mode} = 'settings', 'Back To Ticket', 'Ticket Logger Settings')
```


**`root/Integrations`**

- `position.display`: expression

```js
{view.custom.mode} = 'settings'
```


**`root/TagPathContainer`**

- `position.display`: expression

```js
!({view.custom.mode} = 'settings')
```


**`root/TagPathContainer/TagPath`**

- `props.text`: property `view.params.tagPath`, then expression transform

Transform 1, expression:

```js
if({value} != '',
	if(indexOf({value},']') != -1,
		split({value},']')[1,0],
		{value}),
	'')
```


**`root/ViewName`**

- `position.display`: expression

```js
!({view.custom.mode} = 'settings')
```


**`root/ViewName/Name`**

- `props.text`: property `view.params.viewName`

**`root/IssueData`**

- `position.display`: expression

```js
!({view.custom.mode} = 'settings')
```


**`root/IssueData/IssueTimePriority/IssuerName/Name`**

- `props.text`: expression

```js
{session.props.auth.user.firstName} + " " + {session.props.auth.user.lastName}
```


**`root/IssueData/IssueTimePriority/IssueDate/Date`**

- `props.text`: expression, then format transform

```js
now(0)
```

Transform 1, format `datetime` `{'date': 'medium', 'time': 'short'}`


**`root/IssueData/IssueTimePriority/IssueType/TypeRow/TypeDropdown`**

- `props.value`: property `view.custom.type` (bidirectional)

- `props.options`: tag, then script transform

Mode `direct`, tag path `[default]_Config/TicketLogger/Types`, fallback delay 2.5 s

Transform 1, script:

```python
if value is None:
    return []
return [{'value': r['Type'], 'label': r['Label']} for r in system.dataset.toPyDataSet(value)]
```


**`root/IssueData/IssueTimePriority/IssueType/TypeHelp`**

- `props.text`: expression

```js
coalesce(try(lookup({view.custom.types}, {view.custom.type}, '', 'Type', 'Help'), ''), 'Pick a type — hover the dropdown for a full description.')
```


**`root/IssueData/IssueTimePriority/IssueType/RouteHint`**

- `props.text`: property `view.custom.route`

**`root/Results`**

- `position.display`: expression

```js
!({view.custom.mode} = 'settings')
```


**`root/Results/Field_expected`**

- `position.display`: expression

```js
indexOf({view.custom.fieldKeys}, ',expected,') >= 0
```


**`root/Results/Field_expected/Label`**

- `props.text`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'expected', 'expected', 'Key', 'Label'), 'expected'), 'expected')
```


**`root/Results/Field_expected/TextBox`**

- `props.placeholder`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'expected', '', 'Key', 'Placeholder'), ''), '')
```


**`root/Results/Field_actual`**

- `position.display`: expression

```js
indexOf({view.custom.fieldKeys}, ',actual,') >= 0
```


**`root/Results/Field_actual/Label`**

- `props.text`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'actual', 'actual', 'Key', 'Label'), 'actual'), 'actual')
```


**`root/Results/Field_actual/TextBox`**

- `props.placeholder`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'actual', '', 'Key', 'Placeholder'), ''), '')
```


**`root/Results/Field_steps`**

- `position.display`: expression

```js
indexOf({view.custom.fieldKeys}, ',steps,') >= 0
```


**`root/Results/Field_steps/Label`**

- `props.text`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'steps', 'steps', 'Key', 'Label'), 'steps'), 'steps')
```


**`root/Results/Field_steps/TextBox`**

- `props.placeholder`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'steps', '', 'Key', 'Placeholder'), ''), '')
```


**`root/Results/Field_details`**

- `position.display`: expression

```js
indexOf({view.custom.fieldKeys}, ',details,') >= 0
```


**`root/Results/Field_details/Label`**

- `props.text`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'details', 'details', 'Key', 'Label'), 'details'), 'details')
```


**`root/Results/Field_details/TextBox`**

- `props.placeholder`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'details', '', 'Key', 'Placeholder'), ''), '')
```


**`root/Results/Field_reason`**

- `position.display`: expression

```js
indexOf({view.custom.fieldKeys}, ',reason,') >= 0
```


**`root/Results/Field_reason/Label`**

- `props.text`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'reason', 'reason', 'Key', 'Label'), 'reason'), 'reason')
```


**`root/Results/Field_reason/TextBox`**

- `props.placeholder`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'reason', '', 'Key', 'Placeholder'), ''), '')
```


**`root/Results/Field_question`**

- `position.display`: expression

```js
indexOf({view.custom.fieldKeys}, ',question,') >= 0
```


**`root/Results/Field_question/Label`**

- `props.text`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'question', 'question', 'Key', 'Label'), 'question'), 'question')
```


**`root/Results/Field_question/TextBox`**

- `props.placeholder`: expression

```js
coalesce(try(lookup({view.custom.fields}, 'question', '', 'Key', 'Placeholder'), ''), '')
```


**`root/Buttons`**

- `position.display`: expression

```js
!({view.custom.mode} = 'settings')
```


**`root/Buttons/SendButton`**

- `props.enabled`: property `session.custom.TicketLogAccess`

</details>

## Event Scripts And Handlers

- **`root/Header/Settings`** `dom.onClick`, script action, scope `G`

```python
if not self.session.custom.TicketLogSettings:
    return
self.view.custom.mode = 'ticket' if self.view.custom.mode == 'settings' else 'settings'
```

- **`root/Buttons/SendButton`** `dom.onClick`, script action, scope `G`

```python
from shared import TicketLogger
from shared import Alerts

# ticket-routing: every user with TicketLogger/Use submits; shared.TicketLogger.send routes the ticket by its
# selection (Type + the Area of its tag path) to Monday or the Oracle outbox (or records it in a dry run)
root = self.parent.parent
view = self.view
priority = root.getChild("IssueData").getChild("IssueTimePriority").getChild("IssuePriority").getChild("PriorityDropdown").props.value
requestType = view.custom.type or "Issue"
keys = [k for k in str(view.custom.fieldKeys or "").split(",") if k]
defs = {}
if view.custom.fields is not None:
    for r in system.dataset.toPyDataSet(view.custom.fields):
        defs[r["Key"]] = (r["Label"], int(r["MinLength"] or 0))

errors = []
if priority is None or priority == "" or priority == 0:
    errors.append("Select a Priority")
if not keys:
    errors.append("Select a Type")
sections = []
for k in keys:
    label, minLen = defs.get(k, (k, 0))
    text = str(root.getChild("Results").getChild("Field_" + k).getChild("TextBox").props.text or "").strip()
    if len(text) < minLen:
# ... 28 more line(s): see the view.json
```

- **`root/Buttons/CloseButton`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.closePopup(id="ticketLog"+self.view.params.tagPath)
```

- **`root`** message handler `commitTicketLog` (scope: page)

```python
# implement your handler here
system.perspective.closePopup(id="ticketLog"+self.view.params.tagPath)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../scripting/reference/modules/shared-alerts.md), [shared.TicketLogger.routeLabel](../../../../scripting/reference/modules/shared-ticketlogger.md), [shared.TicketLogger.send](../../../../scripting/reference/modules/shared-ticketlogger.md).

## Related Views

**Embeds** (1): [98\_Configuration/TicketLoggerSettings](./ticketloggersettings.md)

**Named in project scripts**: [shared.Alerts](../../../../scripting/reference/modules/shared-alerts.md)

## Style Classes

<details>
<summary>14 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 2 | style class |
| `Fonts/Label` | 14 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 12 | style class |
| `bg-component` | 8 | stylesheet |
| `bg-container` | 1 | stylesheet |
| `color-icon` | 2 | style class |
| `container-button` | 2 | style class |
| `container-card` | 3 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 2 | style class |
| `fw-600` | 1 | style class |
| `ticket-logger` | 1 | stylesheet |
| `ticket-logger-gear` | 1 | stylesheet |

</details>

See the [style class catalog](../../style-classes.md) and the [stylesheet index](../../stylesheet.md).

## Tags And Data

- `[default]_Config/TicketLogger/Fields`
- `[default]_Config/TicketLogger/Types`

Tag folders and UDTs are documented under [Tags](../../../../tags/index.md).
