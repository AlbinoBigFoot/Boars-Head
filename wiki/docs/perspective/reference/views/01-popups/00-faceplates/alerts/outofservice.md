---
title: "OutOfService"
sidebar_label: "OutOfService"
description: "Perspective view 01_Popups/00_Faceplates/Alerts/OutOfService (Popup / faceplate): 16 components, 17 bindings, 2 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Alerts/OutOfService", "OutOfService"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Alerts/OutOfService`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Alerts/OutOfService` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/OutOfService/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Alerts &gt; OutOfService |
| Root | `ia.container.flex`, height 470, width 460 |
| Size | 16 components, 17 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-10T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `deviceName` | `""` | input |
| `takeOut` | `true` | input |
| `viewName` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `memo` | `""` | |
| `reason` | `null` | |
| `error` | `""` | |

## Component Tree

Component types: ia.display.label x6, ia.container.flex x5, ia.input.button x2, ia.display.icon x1, ia.input.dropdown x1, ia.input.text-area x1.

<details>
<summary>Component tree (16 components)</summary>

```text
dialog  ia.container.flex  [2 bindings]
  body  ia.container.flex  [1 binding]
    Icon  ia.display.icon  [1 binding]
    content  ia.container.flex
      Title  ia.display.label  [1 binding]
      TagPath  ia.display.label  [1 binding]
      ReasonRow  ia.container.flex  [1 binding]
        Lbl  ia.display.label
        Reason  ia.input.dropdown  [1 binding]
      MemoLbl  ia.display.label  [1 binding]
      Memo  ia.input.text-area  [1 binding]
      Count  ia.display.label  [2 bindings]
      Error  ia.display.label  [2 bindings]
  footer  ia.container.flex
    Cancel  ia.input.button  [1 event]
    Confirm  ia.input.button  [3 bindings; 1 event]
```

</details>

## Bindings

17 bindings: expr 13, property 4.

<details>
<summary>All 17 bindings, grouped by component</summary>

**`dialog`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`dialog/body`**

- `props.style.borderTopColor`: expression

```js
if(coalesce({view.params.takeOut}, true), 'var(--warning)', 'var(--success)')
```


**`dialog/body/Icon`**

- `props.color`: expression

```js
if(coalesce({view.params.takeOut}, true), 'var(--warning)', 'var(--success)')
```


**`dialog/body/content/Title`**

- `props.text`: expression

```js
if(coalesce({view.params.takeOut}, true), 'Take ' + {view.params.deviceName} + ' Out Of Service', 'Return ' + {view.params.deviceName} + ' To Service')
```


**`dialog/body/content/TagPath`**

- `props.text`: property `view.params.tagPath`

**`dialog/body/content/ReasonRow`**

- `position.display`: expression

```js
coalesce({view.params.takeOut}, true)
```


**`dialog/body/content/ReasonRow/Reason`**

- `props.value`: property `view.custom.reason` (bidirectional)

**`dialog/body/content/MemoLbl`**

- `props.text`: expression

```js
if(coalesce({view.params.takeOut}, true), 'Memo - Why Is It Being Taken Out Of Service?', 'Memo - What Was Done? Is It Ready To Run?')
```


**`dialog/body/content/Memo`**

- `props.text`: property `view.custom.memo` (bidirectional)

**`dialog/body/content/Count`**

- `props.text`: expression

```js
if(len(trim(coalesce({view.custom.memo}, ''))) >= 10, toStr(len(trim(coalesce({view.custom.memo}, '')))) + ' Characters', toStr(len(trim(coalesce({view.custom.memo}, '')))) + ' / 10 Characters Minimum')
```


- `props.style.classes`: expression

```js
if(len(trim(coalesce({view.custom.memo}, ''))) >= 10, 'Fonts/Label fs-11 text-ok', 'Fonts/Label fs-11 text-muted')
```


**`dialog/body/content/Error`**

- `props.text`: property `view.custom.error`

- `position.display`: expression

```js
coalesce({view.custom.error}, '') != ''
```


**`dialog/footer/Confirm`**

- `props.text`: expression

```js
if(coalesce({view.params.takeOut}, true), 'Take Out Of Service', 'Return To Service')
```


- `props.enabled`: expression

```js
len(trim(coalesce({view.custom.memo}, ''))) >= 10 && (!coalesce({view.params.takeOut}, true) || coalesce({view.custom.reason}, '') != '')
```


- `props.style.classes`: expression

```js
'alert-btn alert-btn-primary alert-btn-' + if(coalesce({view.params.takeOut}, true), 'warning', 'success')
```

</details>

## Event Scripts And Handlers

- **`dialog/footer/Cancel`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.closePopup('oosDialog')
```

- **`dialog/footer/Confirm`** `component.onActionPerformed`, script action, scope `G`

```python
# one-shot command: shared.OutOfService re-checks the permission, memo, reason and device state server side,
# writes the Out Of Service log + <device>.Enabled + the OpsAudit entry (username / time from the session)
self.view.custom.error = ''
res = shared.OutOfService.setOutOfService(self.session, self.view.params.tagPath, self.view.params.takeOut,
    self.view.custom.reason, self.view.custom.memo, self.view.params.viewName)
if res.get('ok'):
    system.perspective.closePopup('oosDialog')
else:
    self.view.custom.error = res.get('error') or 'Not Saved'
```

- **`dialog`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.OutOfService](../../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.setOutOfService](../../../../../../scripting/reference/modules/shared-outofservice.md).

## Related Views

**Named in project scripts**: [shared.OutOfService](../../../../../../scripting/reference/modules/shared-outofservice.md)

## Style Classes

<details>
<summary>13 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Header` | 1 | style class |
| `Fonts/Label` | 4 | style class |
| `Fonts/Value` | 3 | style class |
| `alert-btn` | 2 | no rule found |
| `alert-btn-primary` | 1 | no rule found |
| `alert-btn-secondary` | 1 | no rule found |
| `bg-component` | 3 | stylesheet |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 2 | style class |
| `fs-12` | 1 | style class |
| `fw-600` | 1 | style class |
| `text-muted` | 2 | style class |

</details>

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
