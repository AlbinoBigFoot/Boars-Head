---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls (Asset (embedded piece)): 22 components, 20 bindings, 2 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; ExhaustFan &gt; Controls |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 22 components, 20 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:19:43Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x12, ia.container.flex x9, ia.input.button x1.

<details>
<summary>Component tree (22 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  StatusSection  ia.container.flex
    StatusSectionTitle  ia.display.label
    StatusBanner  ia.display.label  [2 bindings]
    StatusChips  ia.container.flex
      Running  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Fault  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      FailToStart  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      FaultCode  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings; 1 event]
  CommandsSection  ia.container.flex
    CommandsSectionTitle  ia.display.label
    ResetRow  ia.container.flex
      BtnReset  ia.input.button  [4 bindings; 1 event]
    ResetHint  ia.display.label
```

</details>

## Bindings

20 bindings: expr 20.

<details>
<summary>All 20 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roCommand`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Command'], null), true)
```


- `custom.tipCommand`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roCommand}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Command' + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/StatusSection/StatusBanner`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', if(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), 'COMM LOSS', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/FailToStart')), null, tag({view.params.tagPath} + '/FailToStart')), null), false), 'FAIL TO START', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null, tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null), false), 'FAULT', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), null, tag({view.params.tagPath} + '/DIn/Sts_PV')), null), false), 'RUNNING', 'STOPPED')))))
```


- `props.style.classes`: expression

```js
'Refridgeration_STS faceplate-status-banner sts-' + if({view.params.tagPath} = '', 'UNKNOWN', if(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), 'COMMLOSS', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/FailToStart')), null, tag({view.params.tagPath} + '/FailToStart')), null), false), 'FAULT', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null, tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null), false), 'FAULT', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), null, tag({view.params.tagPath} + '/DIn/Sts_PV')), null), false), 'RUNNING', 'STOP')))))
```


**`root/StatusSection/StatusChips/Running/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), null, tag({view.params.tagPath} + '/DIn/Sts_PV')), null), false), 'ON', 'OFF')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_PV')), null, tag({view.params.tagPath} + '/DIn/Sts_PV')), null), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/Fault/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null, tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null), false), 'ACTIVE', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null, tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/FailToStart/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/FailToStart')), null, tag({view.params.tagPath} + '/FailToStart')), null), false), 'ACTIVE', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/FailToStart')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/FailToStart')), null, tag({view.params.tagPath} + '/FailToStart')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/FaultCode/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), '—', if({view.params.tagPath} = '', '—', toStr(coalesce(try(toInt(tag({view.params.tagPath} + '/DIn/Val_Fault')), 0), 0))))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/DIn/Val_Fault')), true), true), 'faceplate-fault-state value-bad', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null, tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null), false) || coalesce(try(if(!isGood(tag({view.params.tagPath} + '/FailToStart')), null, tag({view.params.tagPath} + '/FailToStart')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok'))))))))))))))))
```


**`root/CommandsSection/ResetRow/BtnReset`**

- `props.enabled`: expression

```js
(!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '') && (coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null, tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null), false) || coalesce(try(if(!isGood(tag({view.params.tagPath} + '/FailToStart')), null, tag({view.params.tagPath} + '/FailToStart')), null), false))) && coalesce({view.custom.pax}, '') = ''
```


- `props.style.classes`: expression

```js
if((coalesce(try(if(!isGood(tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null, tag({view.params.tagPath} + '/DIn/Sts_TgtDisagree')), null), false) || coalesce(try(if(!isGood(tag({view.params.tagPath} + '/FailToStart')), null, tag({view.params.tagPath} + '/FailToStart')), null), false)), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```

</details>

## Event Scripts And Handlers

- **`root/StatusSection/StatusChips/FaultCode/State`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/DIn/Val_Fault')
```

- **`root/CommandsSection/ResetRow/BtnReset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
path = base + '/DIn/OCmd_Reset'
cur = system.tag.readBlocking([path])[0].value
shared.Alerts.confirmApplyWrite(
    label='Exhaust Fan Reset',
    tagPath=path,
    newValue=True,
    oldValue=False,
    extraPayload={'viewName': self.view.id.split('@')[0]},
)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

<details>
<summary>15 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 8 | style class |
| `Refridgeration_STS` | 1 | stylesheet |
| `faceplate-cmd-btn` | 1 | style class |
| `faceplate-cmd-row` | 1 | stylesheet |
| `faceplate-cmd-row-fill` | 1 | stylesheet |
| `faceplate-fault-chip` | 4 | style class |
| `faceplate-fault-chips` | 1 | stylesheet |
| `faceplate-fault-code` | 4 | style class |
| `faceplate-fault-state` | 4 | stylesheet |
| `faceplate-section` | 2 | style class |
| `faceplate-section-card` | 2 | style class |
| `faceplate-section-title` | 2 | style class |
| `faceplate-status-banner` | 1 | stylesheet |
| `text-muted` | 1 | style class |
| `faceplate-cmd-btn-active` | bound | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/DIn/OCmd_Reset`, `/DIn/Sts_PV`, `/DIn/Sts_TgtDisagree`, `/DIn/Val_Fault`, `/FailToStart`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
