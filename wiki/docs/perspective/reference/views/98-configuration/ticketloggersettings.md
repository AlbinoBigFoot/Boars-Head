---
title: "TicketLoggerSettings"
sidebar_label: "TicketLoggerSettings"
description: "Perspective view 98_Configuration/TicketLoggerSettings (Configuration / tool view): 33 components, 13 bindings, 3 event scripts."
generated: true
keywords: ["98_Configuration/TicketLoggerSettings", "TicketLoggerSettings"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/TicketLoggerSettings`.

| | |
|---|---|
| View path | `98_Configuration/TicketLoggerSettings` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/TicketLoggerSettings/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; TicketLoggerSettings |
| Root | `ia.container.flex`, width 552, height 660 |
| Size | 33 components, 13 bindings, 3 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `tab` | `"Destinations"` | not persistent |
| `rev` | `0` | not persistent |
| `data` | `null` | bound (expr) |

## Component Tree

Component types: ia.container.flex x14, ia.display.label x13, ia.input.text-field x3, ia.display.view x2, ia.input.button x1.

<details>
<summary>Component tree (33 components)</summary>

```text
root  ia.container.flex
  Denied  ia.display.label  [1 binding]
  Content  ia.container.flex  [1 binding]
    Tabs  ia.container.flex
      TabDestinations  ia.display.label  [1 binding; 1 event]
      TabRouting  ia.display.label  [1 binding; 1 event]
    Destinations  ia.container.flex  [1 binding]
      Integrations  ia.display.view  [view: 98_Configuration/Integrations]
      Oracle  ia.container.flex
        Head  ia.container.flex
          Name  ia.display.label
          Sub  ia.display.label
          Spacer  ia.container.flex
          Badge  ia.display.label
        Note  ia.display.label  [1 binding]
        Row  ia.container.flex
          Endpoint  ia.container.flex
            Label  ia.display.label
            Input  ia.input.text-field
          Client  ia.container.flex
            Label  ia.display.label
            Input  ia.input.text-field
        Credential  ia.container.flex
          Label  ia.display.label
          Input  ia.input.text-field
      DryRun  ia.container.flex
        Head  ia.container.flex
          Name  ia.display.label
          State  ia.display.label  [2 bindings]
          Spacer  ia.container.flex
          Toggle  ia.input.button  [1 binding; 1 event]
        Note  ia.display.label  [1 binding]
    Routing  ia.display.view  [2 bindings; view: 98_Configuration/TicketRouting]
```

</details>

## Bindings

13 bindings: expr 12, property 1.

<details>
<summary>All 13 bindings, grouped by component</summary>

**`(view)`**

- `custom.data`: expression

```js
runScript('shared.TicketLogger.routingForView', 0, {view.custom.rev})
```


**`root/Denied`**

- `position.display`: expression

```js
!(coalesce({session.custom.TicketLogSettings}, false))
```


**`root/Content`**

- `position.display`: expression

```js
coalesce({session.custom.TicketLogSettings}, false)
```


**`root/Content/Tabs/TabDestinations`**

- `props.style.classes`: expression

```js
if({view.custom.tab} = 'Destinations', 'admin-tab admin-tab-active', 'admin-tab')
```


**`root/Content/Tabs/TabRouting`**

- `props.style.classes`: expression

```js
if({view.custom.tab} = 'Routing', 'admin-tab admin-tab-active', 'admin-tab')
```


**`root/Content/Destinations`**

- `position.display`: expression

```js
{view.custom.tab} = 'Destinations'
```


**`root/Content/Destinations/Oracle/Note`**

- `props.text`: expression

```js
'Tickets routed to Oracle are queued in the local outbox (' + toStr(coalesce(try({view.custom.data.oraclePending}, 0), 0)) + ' Pending) until the client integration is connected.'
```


**`root/Content/Destinations/DryRun/Head/State`**

- `props.text`: expression

```js
if(coalesce(try({view.custom.data.dryRun}, false), false), 'On - Nothing Is Sent', 'Off - Tickets Go To Their Destinations')
```


- `props.style.classes`: expression

```js
if(coalesce(try({view.custom.data.dryRun}, false), false), 'form-status-error', 'form-status')
```


**`root/Content/Destinations/DryRun/Head/Toggle`**

- `props.text`: expression

```js
if(coalesce(try({view.custom.data.dryRun}, false), false), 'Turn Dry Run Off', 'Turn Dry Run On')
```


**`root/Content/Destinations/DryRun/Note`**

- `props.text`: expression

```js
'On: no Monday item is created and nothing is queued for Oracle; every ticket is recorded in the outbox ' + 'as Dry Run with its routed destination (' + toStr(coalesce(try({view.custom.data.dryRunCount}, 0), 0)) + ' Recorded). Use it to test routing.'
```


**`root/Content/Routing`**

- `position.display`: expression

```js
{view.custom.tab} = 'Routing'
```


- `props.params.rev`: property `view.custom.rev`

</details>

## Event Scripts And Handlers

- **`root/Content/Tabs/TabDestinations`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.tab = 'Destinations'
```

- **`root/Content/Tabs/TabRouting`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.tab = 'Routing'
```

- **`root/Content/Destinations/DryRun/Head/Toggle`** `component.onActionPerformed`, script action, scope `G`

```python
try:
    shared.TicketLogger.setDryRun(not bool(self.view.custom.data['dryRun']), self.view.id)
except Exception as e:
    shared.Alerts.showAlert(state='error', title='Dry Run', message=str(e), showCloseBtn=True,
        btnTextPrimary='OK', btnTextSecondary='', btnActionPrimary='closeAlert', btnActionSecondary='',
        payload={})
self.view.custom.rev = (self.view.custom.rev or 0) + 1
```

Project script calls: [shared.TicketLogger.routingForView](../../../../scripting/reference/modules/shared-ticketlogger.md).

## Related Views

**Embeds** (2): [98\_Configuration/Integrations](./integrations.md), [98\_Configuration/TicketRouting](./ticketrouting.md)

**Embedded in** (1): [98\_Configuration/TicketLogger](./ticketlogger.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `admin-tab` | 2 | style class |
| `admin-tabs` | 1 | style class |
| `form-btn` | 1 | style class |
| `form-card` | 2 | style class |
| `form-hint` | 4 | style class |
| `form-input` | 3 | style class |
| `form-label` | 3 | style class |
| `form-note` | 1 | style class |
| `form-section-title` | 2 | style class |
| `form-status` | 1 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../style-classes.md) and the [stylesheet index](../../stylesheet.md).
