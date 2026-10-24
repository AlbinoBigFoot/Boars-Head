---
title: "Controls"
sidebar_label: "Controls"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Sensor/Controls (Asset (embedded piece)): 33 components, 50 bindings, 6 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Sensor/Controls", "Controls"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Sensor/Controls`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Sensor/Controls` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Sensor/Controls/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Sensor &gt; Controls |
| Root | `ia.container.flex`, height 560, width 400 |
| Size | 33 components, 50 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T21:00:00Z by the Designer |

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
| `roMode` | `true` | bound (expr) |
| `tipMode` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x15, ia.container.flex x14, ia.input.button x4.

<details>
<summary>Component tree (33 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  AinHome  ia.container.flex
    AinHomeTitle  ia.display.label  [1 binding]
    ModeRow  ia.container.flex
      Mode  ia.display.label  [3 bindings]
      BtnOper  ia.input.button  [6 bindings; 1 event]
      BtnProg  ia.input.button  [6 bindings; 1 event]
    LockRow  ia.container.flex
      BtnLock  ia.input.button  [5 bindings; 1 event]
      BtnReset  ia.input.button  [4 bindings; 1 event]
    Gauge  ia.container.flex
      Scale  ia.container.flex
        Max  ia.display.label  [1 binding]
        Min  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [2 bindings]
      Limits  ia.container.flex
        HH  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
        H  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
        PV  ia.container.flex  [1 binding]
          Val  ia.display.label  [1 binding; 1 event]
          EU  ia.display.label  [1 binding]
        L  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
        LL  ia.container.flex  [1 binding]
          Code  ia.display.label
          Val  ia.display.label  [1 binding]
    Comm  ia.display.label  [2 bindings; 1 event]
```

</details>

## Bindings

50 bindings: expr 50.

<details>
<summary>All 50 bindings, grouped by component</summary>

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


- `custom.roMode`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Mode'], null), true)
```


- `custom.tipMode`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roMode}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Mode' + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/AinHome/AinHomeTitle`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Cfg_Desc')), false), false), if(coalesce(try(toStr(tag({view.params.tagPath} + '/AIn/Cfg_Label')), ''), '') != '', coalesce(try(toStr(tag({view.params.tagPath} + '/AIn/Cfg_Label')), ''), '') + if(coalesce(try(toStr(tag({view.params.tagPath} + '/AIn/Cfg_Desc')), ''), '') != '', '  ·  ' + coalesce(try(toStr(tag({view.params.tagPath} + '/AIn/Cfg_Desc')), ''), ''), ''), 'Analog Input'), '—')
```


**`root/AinHome/ModeRow/Mode`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || (coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false)), if({view.params.tagPath} = '', '—', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false), 'Maintenance', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), 'Operator  ·  Locked', 'Operator'), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false), 'Program', 'No Mode')))), '—')
```


- `props.style.backgroundColor`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), '#F9A825', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), '#3E2723', ''), 'var(--neutral-60)')
```


**`root/AinHome/ModeRow/BtnOper`**

- `props.enabled`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false), (!coalesce({view.custom.roMode}, false) && !({view.params.tagPath} = '') && !coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false)) && coalesce({view.custom.pax}, '') = '', false)
```


- `props.style.backgroundColor`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false)), if(!coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) && coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false), 'var(--neutral-100)', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false)), if(!coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) && coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false), 'var(--text-inverse)', ''), 'var(--neutral-60)')
```


- `props.image.icon.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false)), if(!coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) && coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false), 'var(--text-inverse)', ''), 'var(--neutral-60)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/AinHome/ModeRow/BtnProg`**

- `props.enabled`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || (coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false)), (!coalesce({view.custom.roMode}, false) && !({view.params.tagPath} = '') && !coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false) && !coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false)) && coalesce({view.custom.pax}, '') = '', false)
```


- `props.style.backgroundColor`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false)), if(!coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) && !coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false) && coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false), 'var(--neutral-100)', ''), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false)), if(!coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) && !coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false) && coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false), 'var(--text-inverse)', ''), 'var(--neutral-60)')
```


- `props.image.icon.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false)), if(!coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Maint')), false), false) && !coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false) && coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Prog')), false), false), 'var(--text-inverse)', ''), 'var(--neutral-60)')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/AinHome/LockRow/BtnLock`**

- `props.enabled`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || (coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false)), (!coalesce({view.custom.roMode}, false) && !({view.params.tagPath} = '') && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Oper')), false), false))) && coalesce({view.custom.pax}, '') = '', false)
```


- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), 'Unlock Operator Mode', 'Lock Operator Mode'), '—')
```


- `props.image.icon.path`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Mode/Sts_ProgOperLock')), false), false), 'material/lock_open', 'material/lock'), 'material/link_off')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipMode} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipMode}
```


**`root/AinHome/LockRow/BtnReset`**

- `props.enabled`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || (coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false)), (!coalesce({view.custom.roCommand}, false) && !({view.params.tagPath} = '') && (coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false))) && coalesce({view.custom.pax}, '') = '', false)
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false)), if((coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false)), 'faceplate-cmd-btn faceplate-cmd-btn-active Fonts/Label', 'faceplate-cmd-btn Fonts/Label'), '/AIn/Sts_Fail value-bad')
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/AinHome/Gauge/Scale/Max`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), false), false), if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax'), '#,##0.00'), null), '—')), '—')
```


**`root/AinHome/Gauge/Scale/Min`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), false), false), if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin'), '#,##0.00'), null), '—')), '—')
```


**`root/AinHome/Gauge/Bar/Fill`**

- `position.basis`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Val')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), false), false)), toStr(max(0, min(100, (coalesce(try(toFloat(tag({view.params.tagPath} + '/AIn/Val')), 0), 0) - coalesce(try(toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), 0), 0)) / if(coalesce(try(toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), 100), 100) - coalesce(try(toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), 0), 0) = 0, 1, coalesce(try(toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMax')), 100), 100) - coalesce(try(toFloat(tag({view.params.tagPath} + '/AIn/Cfg_PVEUMin')), 0), 0)) * 100))) + '%', '0%')
```


- `props.style.backgroundColor`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), 'var(--status-level-critical)', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), '#F9A825', 'var(--status-cooling)')), 'var(--neutral-30)')
```


**`root/AinHome/Gauge/Limits/HH`**

- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false), 'var(--status-level-critical)', ''), 'var(--neutral-60)')
```


**`root/AinHome/Gauge/Limits/HH/Val`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Val_HiHiLim')), false), false), if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat(tag({view.params.tagPath} + '/AIn/Val_HiHiLim'))) >= 1e30, false), false), null, tag({view.params.tagPath} + '/AIn/Val_HiHiLim')), '#,##0.00'), null), '—')), '—')
```


**`root/AinHome/Gauge/Limits/H`**

- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false), 'var(--status-level-critical)', ''), 'var(--neutral-60)')
```


**`root/AinHome/Gauge/Limits/H/Val`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Val_HiLim')), false), false), if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat(tag({view.params.tagPath} + '/AIn/Val_HiLim'))) >= 1e30, false), false), null, tag({view.params.tagPath} + '/AIn/Val_HiLim')), '#,##0.00'), null), '—')), '—')
```


**`root/AinHome/Gauge/Limits/PV`**

- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_HiHi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), 'var(--status-level-critical)', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Hi')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), '#F9A825', 'var(--status-cooling)')), 'var(--neutral-60)')
```


**`root/AinHome/Gauge/Limits/PV/Val`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Val')), false), false), if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(tag({view.params.tagPath} + '/AIn/Val'), '#,##0.00'), null), '—')), '—')
```


**`root/AinHome/Gauge/Limits/PV/EU`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Cfg_EU')), false), false), if(coalesce(try(toStr(tag({view.params.tagPath} + '/AIn/Cfg_EU')), ''), '') != '', coalesce(try(toStr(tag({view.params.tagPath} + '/AIn/Cfg_EU')), ''), ''), coalesce(try(tag({view.params.tagPath} + '/AIn/Val' + '.EngUnit'), ''), '')), '—')
```


**`root/AinHome/Gauge/Limits/L`**

- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Lo')), false), false), 'var(--status-level-critical)', ''), 'var(--neutral-60)')
```


**`root/AinHome/Gauge/Limits/L/Val`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Val_LoLim')), false), false), if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat(tag({view.params.tagPath} + '/AIn/Val_LoLim'))) >= 1e30, false), false), null, tag({view.params.tagPath} + '/AIn/Val_LoLim')), '#,##0.00'), null), '—')), '—')
```


**`root/AinHome/Gauge/Limits/LL`**

- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_LoLo')), false), false), 'var(--status-level-critical)', ''), 'var(--neutral-60)')
```


**`root/AinHome/Gauge/Limits/LL/Val`**

- `props.text`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce(try(isGood(tag({view.params.tagPath} + '/AIn/Val_LoLoLim')), false), false), if({view.params.tagPath} = '', '—', coalesce(try(numberFormat(if(coalesce(try(abs(toFloat(tag({view.params.tagPath} + '/AIn/Val_LoLoLim'))) >= 1e30, false), false), null, tag({view.params.tagPath} + '/AIn/Val_LoLoLim')), '#,##0.00'), null), '—')), '—')
```


**`root/AinHome/Comm`**

- `props.text`: expression

```js
if(try(!isGood(tag({view.params.tagPath} + '/AIn/Val')), true), 'Comm Loss', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), 'Input Failure', 'Comm OK'))
```


- `props.style.color`: expression

```js
if(try(!isGood(tag({view.params.tagPath} + '/AIn/Val')), true) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/AIn/Sts_Fail')), false), false), 'var(--status-level-critical)', 'var(--text-muted)')
```

</details>

## Event Scripts And Handlers

- **`root/AinHome/ModeRow/BtnOper`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
qv = system.tag.readBlocking([base + '/' + str(self.view.custom.pax) + '/Sts_Oper', base + '/' + str(self.view.custom.pax) + '/Sts_Prog'])
if bool(qv[0].value) == True and bool(qv[1].value) != True:
    return
shared.ValveCommands.writeTag(base + '/' + str(self.view.custom.pax) + '/Mode/OCmd_AcqLock', True)
```

- **`root/AinHome/ModeRow/BtnProg`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
qv = system.tag.readBlocking([base + '/' + str(self.view.custom.pax) + '/Sts_Oper', base + '/' + str(self.view.custom.pax) + '/Sts_Prog'])
if bool(qv[0].value) == False and bool(qv[1].value) != False:
    return
shared.ValveCommands.writeTag(base + '/' + str(self.view.custom.pax) + '/Mode/OCmd_UnlockRel', True)
```

- **`root/AinHome/LockRow/BtnLock`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roMode:
    return
base = self.view.params.tagPath
if not base:
    return
locked = bool(system.tag.readBlocking([base + '/' + str(self.view.custom.pax) + '/Mode/Sts_ProgOperLock'])[0].value)
cmd = 'OCmd_Unlock' if locked else 'OCmd_Lock'
shared.ValveCommands.writeTag(base + '/' + cmd + '/Value', True)
```

- **`root/AinHome/LockRow/BtnReset`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
if self.view.custom.roCommand:
    return
base = self.view.params.tagPath
if not base:
    return
shared.ValveCommands.writeTag(base + '/' + str(self.view.custom.pax) + '/OCmd_Reset', True)
user = ''
try:
    user = str(self.session.props.auth.user.userName or '')
except:
    pass
try:
    shared.Alarms.acknowledgeForTag(base, user, 'Faceplate Ack / Reset')
except:
    system.util.getLogger('SensorAlarms').warn('Ignition alarm ack failed for %s' % base)
```

- **`root/AinHome/Gauge/Limits/PV/Val`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/AIn/Val')
```

- **`root/AinHome/Comm`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}/AIn/Val')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 13 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 5 | style class |
| `faceplate-cmd-btn` | 4 | style class |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |
| `fw-700` | 6 | style class |
| `faceplate-cmd-btn-active` | bound | style class |
| `value-bad` | bound | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

<details>
<summary>31 relative member paths</summary>

`.EngUnit`, `.TypeId`, `/AIn.Enabled`, `/AIn/Cfg_Desc`, `/AIn/Cfg_EU`, `/AIn/Cfg_Label`, `/AIn/Cfg_PVEUMax`, `/AIn/Cfg_PVEUMin`, `/AIn/Mode/Sts_ProgOperLock`, `/AIn/Sts_Fail`, `/AIn/Sts_Hi`, `/AIn/Sts_HiHi`, `/AIn/Sts_Lo`, `/AIn/Sts_LoLo`, `/AIn/Sts_Maint`, `/AIn/Sts_Oper`, `/AIn/Sts_Prog`, `/AIn/Val`, `/AIn/Val_HiHiLim`, `/AIn/Val_HiLim`, `/AIn/Val_LoLim`, `/AIn/Val_LoLoLim`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Mode/OCmd_AcqLock`, `/Mode/OCmd_UnlockRel`, `/Mode/Sts_ProgOperLock`, `/OCmd_Reset`, `/Sts_Oper`, `/Sts_Prog`, `/Value`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
