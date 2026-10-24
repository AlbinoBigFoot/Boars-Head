---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Compressor/Controls (Asset (embedded piece)): 58 components, 37 bindings, 6 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Compressor/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Compressor/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Compressor/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Compressor/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Compressor &gt; Controls |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 58 components, 37 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T20:12:34Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x36, ia.container.flex x22.

<details>
<summary>Component tree (58 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  StatusSection  ia.container.flex
    StatusSectionTitle  ia.display.label
    StatusBanner  ia.display.label  [2 bindings]
    StatusChips  ia.container.flex
      Running  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      AutoEn  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Alarm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Failed  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Cutout  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      Comm  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
  ModesSection  ia.container.flex
    ModesSectionTitle  ia.display.label
    CpMode  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings]
    SvMode  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings]
    Rung  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    RequestChips  ia.container.flex
      StartReq  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
      StopReq  ia.container.flex
        Code  ia.display.label
        State  ia.display.label  [2 bindings]
  OperatingSection  ia.container.flex
    OperatingSectionTitle  ia.display.label
    Amps  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    Fla  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    Svp  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    DisP  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
    Runtime  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.label  [2 bindings; 1 event]
```

</details>

## Bindings

37 bindings: expr 37.

<details>
<summary>All 37 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/StatusSection/StatusBanner`**

- `props.text`: expression

```js
if({view.params.tagPath} = '', '—', if((try(!isGood(tag({view.params.tagPath} + '/Comp/Color')), true) || coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), null, tag({view.params.tagPath} + '/Comp/Comm')), null), false)), 'COMM LOSS', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Comp/Color')), -1), -1), 0, 'OFF', 1, 'RUNNING', 2, 'ANTI-RECYCLE', 3, 'CUTOUT', 4, 'COMM ERROR', 'UNKNOWN')))
```


- `props.style.classes`: expression

```js
'Refridgeration_STS faceplate-status-banner sts-' + if({view.params.tagPath} = '', 'UNKNOWN', if((try(!isGood(tag({view.params.tagPath} + '/Comp/Color')), true) || coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), null, tag({view.params.tagPath} + '/Comp/Comm')), null), false)), 'COMMLOSS', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Comp/Color')), -1), -1), 0, 'OFF', 1, 'RUNNING', 2, 'IDLE', 3, 'FAULT', 4, 'COMMLOSS', 'UNKNOWN')))
```


**`root/StatusSection/StatusChips/Running/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Started')), null, tag({view.params.tagPath} + '/Comp/Started')), null), false), 'ON', 'OFF')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Started')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Started')), null, tag({view.params.tagPath} + '/Comp/Started')), null), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/AutoEn/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), null, tag({view.params.tagPath} + '/Comp/AutoEN')), null), false), 'ON', 'OFF')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/AutoEN')), null, tag({view.params.tagPath} + '/Comp/AutoEN')), null), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/Alarm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), null, tag({view.params.tagPath} + '/Comp/Alm')), null), false), 'ACTIVE', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Alm')), null, tag({view.params.tagPath} + '/Comp/Alm')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/Failed/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), null, tag({view.params.tagPath} + '/Comp/Failed')), null), false), 'ACTIVE', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Failed')), null, tag({view.params.tagPath} + '/Comp/Failed')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/Cutout/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), null, tag({view.params.tagPath} + '/Comp/Cutout')), null), false), 'ACTIVE', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Cutout')), null, tag({view.params.tagPath} + '/Comp/Cutout')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/StatusSection/StatusChips/Comm/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), null, tag({view.params.tagPath} + '/Comp/Comm')), null), false), 'ERROR', 'OK')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Comm')), null, tag({view.params.tagPath} + '/Comp/Comm')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/ModesSection/CpMode/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), '—', if({view.params.tagPath} = '', '—', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Comp/CP_Mode')), -1), -1), 1, 'Remote', 2, 'Auto', 3, 'Manual', '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/CP_Mode')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/ModesSection/SvMode/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), '—', if({view.params.tagPath} = '', '—', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Comp/SV_Mode')), -1), -1), 1, 'Remote', 2, 'Auto', 3, 'Manual', '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SV_Mode')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/ModesSection/Rung/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), '—', if({view.params.tagPath} = '', '—', case(coalesce(try(toInt(tag({view.params.tagPath} + '/Comp/Rung')), -1), -1), 0, 'Off', 1, 'Running', 2, 'Anti-Recycle', 3, 'Starting', '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Rung')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/ModesSection/RequestChips/StartReq/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), null, tag({view.params.tagPath} + '/Comp/Start_Req')), null), false), 'ACTIVE', 'OFF')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Start_Req')), null, tag({view.params.tagPath} + '/Comp/Start_Req')), null), false), 'faceplate-fault-state text-ok', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/ModesSection/RequestChips/StopReq/State`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), '—', if({view.params.tagPath} = '', '—', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), null, tag({view.params.tagPath} + '/Comp/Stop_Req')), null), false), 'ACTIVE', 'OFF')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), true), true), 'faceplate-fault-state value-bad', if({view.params.tagPath} = '', 'faceplate-fault-state', if(coalesce(try(if(!isGood(tag({view.params.tagPath} + '/Comp/Stop_Req')), null, tag({view.params.tagPath} + '/Comp/Stop_Req')), null), false), 'faceplate-fault-state faceplate-fault-active', 'faceplate-fault-state faceplate-fault-ok')))))))))))))))))
```


**`root/OperatingSection/Amps/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Comp/Amps'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Comp/Amps' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/Amps')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/OperatingSection/Fla/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Comp/FLA'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Comp/FLA' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/FLA')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/OperatingSection/Svp/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Comp/SVP'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Comp/SVP' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/SVP')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/OperatingSection/DisP/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Comp/DisP'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Comp/DisP' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/DisP')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```


**`root/OperatingSection/Runtime/Val`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), '—', if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/Comp/TotalRuntime'), '#,##0.0') + ' ' + coalesce(try(tag({view.params.tagPath} + '/Comp/TotalRuntime' + '.EngUnit'), ''), ''), null), '—')))))))))))))))))
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/Comp/TotalRuntime')), true), true), 'Fonts/Value value-bad', 'Fonts/Value')))))))))))))))
```

</details>

## Event Scripts And Handlers

- **`root/ModesSection/Rung/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Comp/Rung')
```

- **`root/OperatingSection/Amps/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Comp/Amps')
```

- **`root/OperatingSection/Fla/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Comp/FLA')
```

- **`root/OperatingSection/Svp/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Comp/SVP')
```

- **`root/OperatingSection/DisP/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Comp/DisP')
```

- **`root/OperatingSection/Runtime/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/Comp/TotalRuntime')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

<details>
<summary>13 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 19 | style class |
| `Fonts/Value` | 8 | style class |
| `Refridgeration_STS` | 1 | stylesheet |
| `faceplate-fault-chip` | 8 | style class |
| `faceplate-fault-chips` | 2 | stylesheet |
| `faceplate-fault-code` | 8 | style class |
| `faceplate-fault-state` | 8 | stylesheet |
| `faceplate-kpi-label` | 8 | style class |
| `faceplate-kpi-row` | 8 | stylesheet |
| `faceplate-section` | 3 | style class |
| `faceplate-section-card` | 3 | style class |
| `faceplate-section-title` | 3 | style class |
| `faceplate-status-banner` | 1 | stylesheet |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>22 relative member paths</summary>

`.EngUnit`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Comp/Alm`, `/Comp/Amps`, `/Comp/AutoEN`, `/Comp/CP_Mode`, `/Comp/Color`, `/Comp/Comm`, `/Comp/Cutout`, `/Comp/DisP`, `/Comp/FLA`, `/Comp/Failed`, `/Comp/Rung`, `/Comp/SVP`, `/Comp/SV_Mode`, `/Comp/Start_Req`, `/Comp/Started`, `/Comp/Stop_Req`, `/Comp/TotalRuntime`, `/DIn.Enabled`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
