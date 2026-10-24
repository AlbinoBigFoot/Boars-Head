---
title: "DiscreteInputs"
sidebar_label: "DiscreteInputs"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/DiscreteInputs (Asset (embedded piece)): 17 components, 23 bindings, 4 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/DiscreteInputs", "DiscreteInputs"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/DiscreteInputs`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/DiscreteInputs` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/DiscreteInputs/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; DiscreteInputs |
| Root | `ia.container.flex`, height 560, width 520 |
| Size | 17 components, 23 bindings, 4 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-25T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x10, ia.container.flex x7.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Inputs  ia.container.flex
    InputsTitle  ia.display.label
    Grid  ia.container.flex
      DI_HLCO  ia.container.flex  [1 binding; 1 event]
        Label  ia.display.label  [1 binding]
        State  ia.display.label  [3 bindings]
      DI_HiLevel  ia.container.flex  [1 binding; 1 event]
        Label  ia.display.label  [1 binding]
        State  ia.display.label  [3 bindings]
      DI_OPL  ia.container.flex  [1 binding; 1 event]
        Label  ia.display.label  [1 binding]
        State  ia.display.label  [3 bindings]
      DI_LoLo  ia.container.flex  [1 binding; 1 event]
        Label  ia.display.label  [1 binding]
        State  ia.display.label  [3 bindings]
  Hint  ia.display.label
```

</details>

## Bindings

23 bindings: expr 23.

<details>
<summary>All 23 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Inputs/Grid/DI_HLCO`**

- `position.display`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/HlcoDIn/Cfg_Label')), ''), '') != ''
```


**`root/Inputs/Grid/DI_HLCO/Label`**

- `props.text`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/HlcoDIn/Cfg_Label')), ''), '')
```


**`root/Inputs/Grid/DI_HLCO/State`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Cfg_1StText')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Cfg_0StText')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/HlcoDIn/Sts')), false), false), coalesce(try(toStr(tag({view.params.tagPath} + '/HlcoDIn/Cfg_1StText')), ''), ''), coalesce(try(toStr(tag({view.params.tagPath} + '/HlcoDIn/Cfg_0StText')), ''), '')), '—')
```


- `props.style.backgroundColor`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/HlcoDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/HlcoDIn/Inp_Target')), false), false), 'var(--surface-sunken)', 'var(--status-level-critical)'), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HlcoDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/HlcoDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/HlcoDIn/Inp_Target')), false), false), 'var(--text)', '#ffffff'), 'var(--neutral-60)')
```


**`root/Inputs/Grid/DI_HiLevel`**

- `position.display`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/HiHiDIn/Cfg_Label')), ''), '') != ''
```


**`root/Inputs/Grid/DI_HiLevel/Label`**

- `props.text`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/HiHiDIn/Cfg_Label')), ''), '')
```


**`root/Inputs/Grid/DI_HiLevel/State`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Cfg_1StText')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Cfg_0StText')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/HiHiDIn/Sts')), false), false), coalesce(try(toStr(tag({view.params.tagPath} + '/HiHiDIn/Cfg_1StText')), ''), ''), coalesce(try(toStr(tag({view.params.tagPath} + '/HiHiDIn/Cfg_0StText')), ''), '')), '—')
```


- `props.style.backgroundColor`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/HiHiDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/HiHiDIn/Inp_Target')), false), false), 'var(--surface-sunken)', 'var(--status-level-critical)'), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/HiHiDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/HiHiDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/HiHiDIn/Inp_Target')), false), false), 'var(--text)', '#ffffff'), 'var(--neutral-60)')
```


**`root/Inputs/Grid/DI_OPL`**

- `position.display`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/OplDIn/Cfg_Label')), ''), '') != ''
```


**`root/Inputs/Grid/DI_OPL/Label`**

- `props.text`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/OplDIn/Cfg_Label')), ''), '')
```


**`root/Inputs/Grid/DI_OPL/State`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Cfg_1StText')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Cfg_0StText')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/OplDIn/Sts')), false), false), coalesce(try(toStr(tag({view.params.tagPath} + '/OplDIn/Cfg_1StText')), ''), ''), coalesce(try(toStr(tag({view.params.tagPath} + '/OplDIn/Cfg_0StText')), ''), '')), '—')
```


- `props.style.backgroundColor`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/OplDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/OplDIn/Inp_Target')), false), false), 'var(--surface-sunken)', 'var(--status-level-critical)'), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/OplDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/OplDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/OplDIn/Inp_Target')), false), false), 'var(--text)', '#ffffff'), 'var(--neutral-60)')
```


**`root/Inputs/Grid/DI_LoLo`**

- `position.display`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/LoLoDIn/Cfg_Label')), ''), '') != ''
```


**`root/Inputs/Grid/DI_LoLo/Label`**

- `props.text`: expression

```js
coalesce(try(toStr(tag({view.params.tagPath} + '/LoLoDIn/Cfg_Label')), ''), '')
```


**`root/Inputs/Grid/DI_LoLo/State`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Cfg_1StText')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Cfg_0StText')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/LoLoDIn/Sts')), false), false), coalesce(try(toStr(tag({view.params.tagPath} + '/LoLoDIn/Cfg_1StText')), ''), ''), coalesce(try(toStr(tag({view.params.tagPath} + '/LoLoDIn/Cfg_0StText')), ''), '')), '—')
```


- `props.style.backgroundColor`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/LoLoDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/LoLoDIn/Inp_Target')), false), false), 'var(--surface-sunken)', 'var(--status-level-critical)'), 'var(--neutral-30)')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Sts')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/LoLoDIn/Inp_Target')), false), false)), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/LoLoDIn/Sts')), false), false) = coalesce(try(toBoolean(tag({view.params.tagPath} + '/LoLoDIn/Inp_Target')), false), false), 'var(--text)', '#ffffff'), 'var(--neutral-60)')
```

</details>

## Event Scripts And Handlers

- **`root/Inputs/Grid/DI_HLCO`** `dom.onClick`, script action, scope `G`

```python
p = str(self.view.params.tagPath or '')
if not p:
    return
p = p + '/DI_HLCO'
title = str(system.tag.readBlocking([shared.Pax.livePath(p + '/Cfg_Label/Value')])[0].value or 'DI_HLCO')
Navigation.Faceplate.openFaceplate('din-fp-%s' % p, p, '01_Popups/00_Faceplates/DiscreteInput', False, title, 600, 600, {'title': title})
```

- **`root/Inputs/Grid/DI_HiLevel`** `dom.onClick`, script action, scope `G`

```python
p = str(self.view.params.tagPath or '')
if not p:
    return
p = p + '/DI_HiLevel'
title = str(system.tag.readBlocking([shared.Pax.livePath(p + '/Cfg_Label/Value')])[0].value or 'DI_HiLevel')
Navigation.Faceplate.openFaceplate('din-fp-%s' % p, p, '01_Popups/00_Faceplates/DiscreteInput', False, title, 600, 600, {'title': title})
```

- **`root/Inputs/Grid/DI_OPL`** `dom.onClick`, script action, scope `G`

```python
p = str(self.view.params.tagPath or '')
if not p:
    return
p = p + '/DI_OPL'
title = str(system.tag.readBlocking([shared.Pax.livePath(p + '/Cfg_Label/Value')])[0].value or 'DI_OPL')
Navigation.Faceplate.openFaceplate('din-fp-%s' % p, p, '01_Popups/00_Faceplates/DiscreteInput', False, title, 600, 600, {'title': title})
```

- **`root/Inputs/Grid/DI_LoLo`** `dom.onClick`, script action, scope `G`

```python
p = str(self.view.params.tagPath or '')
if not p:
    return
p = p + '/DI_LoLo'
title = str(system.tag.readBlocking([shared.Pax.livePath(p + '/Cfg_Label/Value')])[0].value or 'DI_LoLo')
Navigation.Faceplate.openFaceplate('din-fp-%s' % p, p, '01_Popups/00_Faceplates/DiscreteInput', False, title, 600, 600, {'title': title})
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Pax.livePath](../../../../../../scripting/reference/modules/shared-pax.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/DiscreteInput](../discreteinput.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 6 | style class |
| `Fonts/Value` | 4 | style class |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |
| `fw-700` | 8 | style class |
| `text-muted` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>29 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_Label/Value`, `/DI_HLCO`, `/DI_HiLevel`, `/DI_LoLo`, `/DI_OPL`, `/DIn.Enabled`, `/HiHiDIn/Cfg_0StText`, `/HiHiDIn/Cfg_1StText`, `/HiHiDIn/Cfg_Label`, `/HiHiDIn/Inp_Target`, `/HiHiDIn/Sts`, `/HlcoDIn/Cfg_0StText`, `/HlcoDIn/Cfg_1StText`, `/HlcoDIn/Cfg_Label`, `/HlcoDIn/Inp_Target`, `/HlcoDIn/Sts`, `/LoLoDIn/Cfg_0StText`, `/LoLoDIn/Cfg_1StText`, `/LoLoDIn/Cfg_Label`, `/LoLoDIn/Inp_Target`, `/LoLoDIn/Sts`, `/OplDIn/Cfg_0StText`, `/OplDIn/Cfg_1StText`, `/OplDIn/Cfg_Label`, `/OplDIn/Inp_Target`, `/OplDIn/Sts`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
