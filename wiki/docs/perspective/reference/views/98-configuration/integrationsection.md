---
title: "IntegrationSection"
sidebar_label: "IntegrationSection"
description: "Perspective view 98_Configuration/IntegrationSection (Configuration / tool view): 31 components, 23 bindings, 5 event scripts."
generated: true
keywords: ["98_Configuration/IntegrationSection", "IntegrationSection"]
---

:::note

:::


**Configuration / tool view**: `98_Configuration/IntegrationSection`.

| | |
|---|---|
| View path | `98_Configuration/IntegrationSection` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/IntegrationSection/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 98\_Configuration &gt; IntegrationSection |
| Root | `ia.container.flex`, height 560, width 560 |
| Size | 31 components, 23 bindings, 5 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-24T18:40:04Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `name` | `""` | input |
| `expanded` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `rev` | `0` | not persistent |
| `detail` | `{}` | bound (expr) |

## Component Tree

Component types: ia.display.label x12, ia.container.flex x9, ia.input.text-field x3, ia.input.button x3, ia.display.icon x1, ia.input.toggle-switch x1, ia.input.password-field x1, ia.display.table x1.

<details>
<summary>Component tree (31 components)</summary>

```text
root  ia.container.flex
  Header  ia.container.flex  [1 event]
    Chevron  ia.display.icon  [1 binding]
    Name  ia.display.label  [1 binding]
    Provider  ia.display.label  [1 binding]
    Dot  ia.display.label  [1 binding]
    Status  ia.display.label  [1 binding]
  Body  ia.container.flex  [1 binding]
    StatusRow  ia.container.flex
      Checked  ia.display.label  [1 binding]
      Error  ia.display.label  [1 binding]
    EnabledRow  ia.container.flex
      Label  ia.display.label
      Input  ia.input.toggle-switch  [2 bindings]
    DescriptionRow  ia.container.flex
      Label  ia.display.label
      Input  ia.input.text-field  [2 bindings]
    UrlRow  ia.container.flex
      Label  ia.display.label
      Input  ia.input.text-field  [2 bindings]
      VersionLabel  ia.display.label
      Version  ia.input.text-field  [2 bindings]
    TokenRow  ia.container.flex
      Label  ia.display.label
      Input  ia.input.password-field  [2 bindings]
      Replace  ia.input.button  [1 binding; 1 event]
    SettingsLabel  ia.display.label
    Settings  ia.display.table  [1 binding; 1 event]
    Buttons  ia.container.flex
      Test  ia.input.button  [1 binding; 1 event]
      Save  ia.input.button  [1 binding; 1 event]
```

</details>

## Bindings

23 bindings: expr 23.

<details>
<summary>All 23 bindings, grouped by component</summary>

**`(view)`**

- `custom.detail`: expression

```js
runScript('shared.Integrations.detail', 10000, coalesce({view.params.name}, ''), {view.custom.rev})
```


**`root/Header/Chevron`**

- `props.path`: expression

```js
if(coalesce({view.params.expanded}, false), 'material/expand_more', 'material/chevron_right')
```


**`root/Header/Name`**

- `props.text`: expression

```js
coalesce({view.params.name}, '')
```


**`root/Header/Provider`**

- `props.text`: expression

```js
coalesce({view.custom.detail.provider}, '')
```


**`root/Header/Dot`**

- `props.style.backgroundColor`: expression

```js
if(!coalesce({view.custom.detail.enabled}, false), 'var(--status-off)', if(coalesce({view.custom.detail.connected}, false), 'var(--status-idle)', 'var(--alarm-critical)'))
```


**`root/Header/Status`**

- `props.text`: expression

```js
if(!coalesce({view.custom.detail.enabled}, false), 'Disabled', if(coalesce({view.custom.detail.connected}, false), 'Connected', 'Not Connected'))
```


**`root/Body`**

- `position.display`: expression

```js
coalesce({view.params.expanded}, false)
```


**`root/Body/StatusRow/Checked`**

- `props.text`: expression

```js
if(isNull({view.custom.detail.lastCheck}), 'Never Checked', 'Last Check ' + dateFormat({view.custom.detail.lastCheck}, 'yyyy-MM-dd HH:mm:ss'))
```


**`root/Body/StatusRow/Error`**

- `props.text`: expression

```js
coalesce({view.custom.detail.lastError}, '')
```


**`root/Body/EnabledRow/Input`**

- `props.selected`: expression

```js
coalesce({view.custom.detail.enabled}, false)
```


- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


**`root/Body/DescriptionRow/Input`**

- `props.text`: expression

```js
coalesce({view.custom.detail.description}, '')
```


- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


**`root/Body/UrlRow/Input`**

- `props.text`: expression

```js
coalesce({view.custom.detail.url}, '')
```


- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


**`root/Body/UrlRow/Version`**

- `props.text`: expression

```js
coalesce({view.custom.detail.apiVersion}, '')
```


- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


**`root/Body/TokenRow/Input`**

- `props.placeholder`: expression

```js
if(coalesce({view.custom.detail.hasToken}, false), 'Set (hidden) - type to replace', 'Not set')
```


- `props.enabled`: expression

```js
coalesce({session.custom.IntegrationAccess}, false)
```


**`root/Body/TokenRow/Replace`**

- `props.enabled`: expression

```js
coalesce({view.params.name}, '') != '' && coalesce({session.custom.IntegrationAccess}, false)
```


**`root/Body/Settings`**

- `props.data`: expression

```js
runScript('shared.Integrations.settingsRows', 0, coalesce({view.params.name}, ''), {view.custom.rev})
```


**`root/Body/Buttons/Test`**

- `props.enabled`: expression

```js
coalesce({view.params.name}, '') != '' && true
```


**`root/Body/Buttons/Save`**

- `props.enabled`: expression

```js
coalesce({view.params.name}, '') != '' && coalesce({session.custom.IntegrationAccess}, false)
```

</details>

## Event Scripts And Handlers

- **`root/Header`** `dom.onClick`, script action, scope `G`

```python
system.perspective.sendMessage("integrationsToggle", payload={"name": self.view.params.name}, scope="page")
```

- **`root/Body/TokenRow/Replace`** `component.onActionPerformed`, script action, scope `G`

```python
name = self.view.params.name
if not name or not self.session.custom.IntegrationAccess:
    return
box = self.parent.getChild("Input")
try:
    shared.Integrations.setToken(name, box.props.text, self.view.id.split("@")[0])
    box.props.text = ""
    self.view.custom.rev += 1
    shared.Alerts.showAlert(state='success', title='API Token', message='%s token replaced.' % name, showCloseBtn=True, btnTextPrimary='OK', btnTextSecondary='', btnActionPrimary='closeAlert', btnActionSecondary='', payload={})
except Exception as e:
    shared.Alerts.showAlert(state='error', title='API Token', message=str(e), showCloseBtn=True, btnTextPrimary='OK', btnTextSecondary='', btnActionPrimary='closeAlert', btnActionSecondary='', payload={})
```

- **`root/Body/Settings`** `component.onEditCellCommit`, script action, scope `G`

```python
self.props.data[event.row][event.column] = event.value
```

- **`root/Body/Buttons/Test`** `component.onActionPerformed`, script action, scope `G`

```python
name = self.view.params.name
if not name:
    return
ok, msg = shared.Integrations.test(name)
self.view.custom.rev += 1
shared.Alerts.showAlert(state='success' if ok else 'error', title='Test Connection', message='%s: %s' % (name, msg), showCloseBtn=True, btnTextPrimary='OK', btnTextSecondary='', btnActionPrimary='closeAlert', btnActionSecondary='', payload={})
```

- **`root/Body/Buttons/Save`** `component.onActionPerformed`, script action, scope `G`

```python
name = self.view.params.name
if not name or not self.session.custom.IntegrationAccess:
    return
b = self.view.rootContainer.getChild("Body")
url = b.getChild("UrlRow")
values = {
    "enabled": bool(b.getChild("EnabledRow").getChild("Input").props.selected),
    "description": b.getChild("DescriptionRow").getChild("Input").props.text or "",
    "url": url.getChild("Input").props.text or "",
    "apiVersion": url.getChild("Version").props.text or "",
    "settings": shared.Integrations.unflatten(b.getChild("Settings").props.data),
}
try:
    shared.Integrations.save(name, values, self.view.id.split("@")[0])
    self.view.custom.rev += 1
    shared.Alerts.showAlert(state='success', title='Saved', message='%s saved.' % name, showCloseBtn=True, btnTextPrimary='OK', btnTextSecondary='', btnActionPrimary='closeAlert', btnActionSecondary='', payload={})
except Exception as e:
    shared.Alerts.showAlert(state='error', title='Save Failed', message=str(e), showCloseBtn=True, btnTextPrimary='OK', btnTextSecondary='', btnActionPrimary='closeAlert', btnActionSecondary='', payload={})
```

Project script calls: [shared.Integrations.detail](../../../../scripting/reference/modules/shared-integrations.md), [shared.Integrations.settingsRows](../../../../scripting/reference/modules/shared-integrations.md), [shared.Integrations.test](../../../../scripting/reference/modules/shared-integrations.md), [shared.Integrations.unflatten](../../../../scripting/reference/modules/shared-integrations.md).

## Related Views

**Embedded in** (1): [98\_Configuration/Integrations](./integrations.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 3 | style class |
| `Fonts/Label` | 8 | style class |
| `Fonts/Value` | 7 | style class |
| `bg-component` | 4 | stylesheet |
| `color-icon` | 1 | style class |
| `container-button` | 3 | style class |
| `container-card` | 5 | stylesheet |
| `fs-11` | 1 | style class |
| `fw-700` | 2 | style class |
| `integration-section-header` | 1 | stylesheet |

See the [style class catalog](../../style-classes.md) and the [stylesheet index](../../stylesheet.md).
