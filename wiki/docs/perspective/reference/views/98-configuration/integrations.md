---
title: "Integrations"
sidebar_label: "Integrations"
description: "Perspective view 98_Configuration/Integrations (Configuration / tool view): 7 components, 5 bindings, 1 event scripts."
generated: true
keywords: ["98_Configuration/Integrations", "Integrations"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/Integrations`.

| | |
|---|---|
| View path | `98_Configuration/Integrations` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/Integrations/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; Integrations |
| Root | `ia.container.flex`, height 660, width 580 |
| Size | 7 components, 5 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:40:04Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `expanded` | `""` | not persistent |
| `rev` | `0` | not persistent |
| `items` | `[]` | bound (expr) |

## Component Tree

Component types: ia.container.flex x2, ia.display.flex-repeater x1, ia.display.label x1, ia.input.text-field x1, ia.input.dropdown x1, ia.input.button x1.

```text
root  ia.container.flex
  Sections  ia.display.flex-repeater  [1 binding; view: 98_Configuration/IntegrationSection]
  AddRow  ia.container.flex
    Label  ia.display.label
    NewName  ia.input.text-field  [1 binding]
    NewProvider  ia.input.dropdown  [1 binding]
    Add  ia.input.button  [1 binding; 1 event]
```

## Bindings

5 bindings: expr 5.

**`(view)`**

- `custom.items`: expression

```js
runScript('shared.Integrations.listForView', 10000, {view.custom.rev})
```


**`root/Sections`**

- `props.instances`: expression

```js
forEach(coalesce({view.custom.items}, asList()),
	asMap('name', coalesce(it()['name'], ''),
		'expanded', coalesce({view.custom.expanded}, '') = coalesce(it()['name'], ''),
		'instanceStyle', asMap('classes', ''),
		'instancePosition', if(coalesce({view.custom.expanded}, '') = coalesce(it()['name'], ''),
			asMap('grow', 1, 'shrink', 1, 'basis', '0px'),
			asMap('grow', 0, 'shrink', 0, 'basis', '38px'))))
```


**`root/AddRow/NewName`**

- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


**`root/AddRow/NewProvider`**

- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


**`root/AddRow/Add`**

- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


## Event Scripts And Handlers

- **`root/AddRow/Add`** `component.onActionPerformed`, script action, scope `G`

```python
if not self.session.custom.IntegrationAccess:
    return
r = self.parent
name = str(r.getChild("NewName").props.text or "").strip()
provider = r.getChild("NewProvider").props.value or "HTTP"
try:
    shared.Integrations.add(name, provider, self.view.id.split("@")[0])
    r.getChild("NewName").props.text = ""
    self.view.custom.expanded = name
    self.view.custom.rev += 1
except Exception as e:
    shared.Alerts.showAlert(state='error', title='Add Integration', message=str(e), showCloseBtn=True, btnTextPrimary='OK', btnTextSecondary='', btnActionPrimary='closeAlert', btnActionSecondary='', payload={})
```

- **`root`** message handler `integrationsToggle` (scope: page)

```python
name = str(payload.get("name") or "")
self.view.custom.expanded = "" if self.view.custom.expanded == name else name
```

Project script calls: [shared.Integrations.listForView](../../../../scripting/reference/modules/shared-integrations.md).

## Related Views

**Embeds** (1): [98\_Configuration/IntegrationSection](./integrationsection.md) (flex repeater)

**Embedded in** (1): [98\_Configuration/TicketLoggerSettings](./ticketloggersettings.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 1 | style class |
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 2 | style class |
| `bg-component` | 2 | stylesheet |
| `container-button` | 1 | style class |
| `container-card` | 2 | stylesheet |

See the [style class catalog](../../style-classes.md) and the [stylesheet index](../../stylesheet.md).
