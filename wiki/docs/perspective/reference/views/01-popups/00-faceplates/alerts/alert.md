---
title: "Alert"
sidebar_label: "Alert"
description: "Perspective view 01_Popups/00_Faceplates/Alerts/Alert (Popup / faceplate): 10 components, 22 bindings, 4 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Alerts/Alert", "Alert"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Alerts/Alert`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Alerts/Alert` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/Alert/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Alerts &gt; Alert |
| Root | `ia.container.flex`, height 200, width 360 |
| Size | 10 components, 22 bindings, 4 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T18:51:20Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `btnActionPrimary` | `""` | input |
| `btnActionSecondary` | `""` | input |
| `btnIconAlignment` | `"right"` | inout |
| `btnIconPrimary` | `"material/chevron_right"` | inout |
| `btnIconSecondary` | `""` | inout |
| `btnTextPrimary` | `"Primary"` | inout |
| `btnTextSecondary` | `"Secondary"` | inout |
| `message` | `"Test Message"` | input |
| `payload` | `""` | input |
| `showCloseBtn` | `true` | input |
| `state` | `"info"` | input |
| `title` | `"Title"` | input |

## Component Tree

Component types: ia.container.flex x4, ia.display.icon x2, ia.input.button x2, ia.display.label x1, ia.display.markdown x1.

```text
dialog  ia.container.flex  [2 bindings; 1 event]
  body  ia.container.flex  [1 binding]
    iconMain  ia.display.icon  [2 bindings]
    content  ia.container.flex
      title  ia.display.label  [3 bindings]
      Markdown  ia.display.markdown  [1 binding]
    iconClose  ia.display.icon  [1 binding; 1 event]
  footer  ia.container.flex
    actionSecondary  ia.input.button  [5 bindings; 1 event]
    actionPrimary  ia.input.button  [5 bindings; 1 event]
```

## Bindings

22 bindings: expr 11, property 9, expr-struct 2.

<details>
<summary>All 22 bindings, grouped by component</summary>

**`(view)`**

- `props.defaultSize.height`: expression

```js
min(300, max(168, 72 + (len({view.params.message}) / 42 + 1) * 18 + 70))
```


- `props.defaultSize.width`: expression

```js
if(len({view.params.message}) > 48, 400, 320)
```


**`dialog`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../common-patterns.md#pattern-1).

**`dialog/body`**

- `props.style.borderTopColor`: expression, then map transform

```js
{view.params.state}
```

Transform 1, map (scalar to scalar):

```
"warning" -> "var(--warning)"
"success" -> "var(--success)"
"error" -> "var(--error)"
"info" -> "var(--info)"
fallback -> "var(--info)"
```


**`dialog/body/iconMain`**

- `props.color`: expression, then map transform

```js
{view.params.state}
```

Transform 1, map (scalar to scalar):

```
"warning" -> "var(--warning)"
"success" -> "var(--success)"
"error" -> "var(--error)"
"info" -> "var(--info)"
fallback -> "var(--info)"
```


- `props.path`: expression, then map transform

```js
{view.params.state}
```

Transform 1, map (scalar to scalar):

```
"warning" -> "material/warning"
"info" -> "material/info"
"error" -> "material/error"
"success" -> "material/check_circle"
fallback -> "material/info"
```


**`dialog/body/content/title`**

- `position.display`: expression, then map transform

```js
{this.props.text}
```

Transform 1, map (scalar to scalar):

```
"" -> false
fallback -> true
```


- `props.style.color`: property `view.params.state`, then map transform

Transform 1, map (scalar to scalar):

```
"info" -> "var(--info)"
"success" -> "var(--success)"
"error" -> "var(--error)"
"warning" -> "var(--warning)"
fallback -> "var(--info)"
```


- `props.text`: property `view.params.title`

**`dialog/body/content/Markdown`**

- `props.source`: property `view.params.message`

**`dialog/body/iconClose`**

- `position.display`: property `view.params.showCloseBtn`

**`dialog/footer/actionSecondary`**

- `position.display`: property `this.props.text`, then map transform

Transform 1, map (scalar to scalar):

```
"" -> false
fallback -> true
```


- `props.image.icon.path`: expression

```js
{view.params.btnIconSecondary}
```


- `props.image.position`: property `view.params.btnIconAlignment`

- `props.style.classes`: expression

```js
concat('alert-btn alert-btn-secondary alert-btn-', {view.params.state})
```


- `props.text`: expression

```js
{view.params.btnTextSecondary}
```


**`dialog/footer/actionPrimary`**

- `position.display`: property `this.props.text`, then map transform

Transform 1, map (scalar to scalar):

```
"" -> false
fallback -> true
```


- `props.image.icon.path`: expression

```js
{view.params.btnIconPrimary}
```


- `props.image.position`: property `view.params.btnIconAlignment`

- `props.style.classes`: expression

```js
concat('alert-btn alert-btn-primary alert-btn-', {view.params.state})
```


- `props.text`: property `view.params.btnTextPrimary`

</details>

## Event Scripts And Handlers

- **`dialog`** `dom.onFocus`, script action, scope `G`

```python
messageType = 'alertFocus'
system.perspective.sendMessage(messageType)
```

- **`dialog/body/iconClose`** `dom.onClick`, popup action, scope `C`: close popup `alertDialog`, view [01\_Popups/00\_Faceplates/Alerts/Alert](./alert.md)

- **`dialog/footer/actionSecondary`** `component.onActionPerformed`, script action, scope `G`

```python
action = self.view.params.btnActionSecondary
    
if len(action):
    system.perspective.sendMessage(messageType=action, payload=self.view.params.payload, scope='page')
    
system.perspective.closePopup(id = "alertDialog")
```

- **`dialog/footer/actionPrimary`** `component.onActionPerformed`, script action, scope `G`

```python
action = self.view.params.btnActionPrimary or ''
payload = {}
src = self.view.params.payload
try:
    if src:
        for k in src:
            payload[k] = src[k]
except:
    payload = dict(src) if src else {}
if action == 'writeValue' and payload.get('tagPath') and not payload.get('skipWrite'):
    try:
        shared.Audit.writeTag(
            payload.get('tagPath'),
            payload.get('value'),
            label=payload.get('label'),
            viewName=payload.get('viewName'),
        )
        payload['alreadyWritten'] = True
    except:
        pass
if action:
    system.perspective.sendMessage(messageType=action, payload=payload, scope='page')
system.perspective.closePopup(id='alertDialog')
```

- **`dialog`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Named in project scripts**: [shared.Alerts](../../../../../../scripting/reference/modules/shared-alerts.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Header` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `alert-btn` | 2 | no rule found |
| `alert-btn-primary` | 1 | no rule found |
| `alert-btn-secondary` | 1 | no rule found |
| `alert-close` | 1 | no rule found |
| `bg-component` | 1 | stylesheet |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
