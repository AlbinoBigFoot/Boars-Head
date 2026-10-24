---
title: "Module_1769_OW16"
sidebar_label: "Module_1769_OW16"
description: "Perspective view 02_Components/03_PLC/Module_1769_OW16 (Reusable component): 2 components, 47 bindings, 3 event scripts."
generated: true
keywords: ["02_Components/03_PLC/Module_1769_OW16", "Module_1769_OW16"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/Module_1769_OW16`.

| | |
|---|---|
| View path | `02_Components/03_PLC/Module_1769_OW16` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/Module_1769_OW16/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; Module\_1769\_OW16 |
| Root | `ia.container.flex`, width 54, height 280 |
| Size | 2 components, 47 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `slot` | `0` | input |
| `member` | `""` | input |
| `selected` | `false` | input |
| `state` | `"OK"` | input |
| `name` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `preview` | `"ok"` | bound (expr) |
| `good` | `false` | bound (expr) |
| `fault` | `0` | bound (expr) |
| `state` | `"bad"` | bound (expr) |
| `word` | `0` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [3 bindings; 3 events]
  Module  ia.shapes.svg  [39 bindings]
```

## Bindings

47 bindings: expr 47.

<details>
<summary>All 47 bindings, grouped by component</summary>

**`(view)`**

- `custom.preview`: expression

```js
lower(trim(coalesce({view.params.state}, 'ok')))
```


- `custom.good`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} != 'bad', coalesce(try(isGood(tag({view.params.tagPath} + '/Fault')) && isGood(tag({view.params.tagPath} + '/ReadBack')), false), false))
```


- `custom.fault`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Fault')), false), false), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'fault', 1, 0), coalesce(try(toInt(tag({view.params.tagPath} + '/Fault')), 0), 0)), null)
```


- `custom.state`: expression

```js
if(!{view.custom.good}, 'bad', if({view.custom.fault} = -1, 'conn', if({view.custom.fault} != 0, 'fault', 'ok')))
```


- `custom.word`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/ReadBack')), false), false), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 261, 0), coalesce(try(toInt(tag({view.params.tagPath} + '/ReadBack')), 0), 0)), null)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

- `props.style.classes`: expression

```js
if(coalesce({view.params.member}, '') != '', 'faceplate-hover', '')
```


**`root/Module`**

- `props.elements[1].text`: expression

```js
if(coalesce({view.params.slot}, 0) < 10, '0', '') + toStr(coalesce({view.params.slot}, 0))
```


- `props.elements[3].fill.paint`: expression

```js
case({view.custom.state}, 'ok', 'var(--sts-run)', 'fault', 'var(--sts-fault)', 'conn', 'var(--sts-fault)', 'var(--neutral-60)')
```


- `props.elements[6].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 0) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[7].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 0) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[8].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 1) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[9].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 1) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[10].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 2) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[11].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 2) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[12].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 3) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[13].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 3) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[14].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 4) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[15].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 4) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[16].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 5) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[17].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 5) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[18].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 6) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[19].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 6) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[20].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 7) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[21].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 7) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[22].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 8) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[23].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 8) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[24].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 9) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[25].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 9) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[26].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 10) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[27].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 10) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[28].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 11) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[29].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 11) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[30].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 12) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[31].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 12) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[32].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 13) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[33].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 13) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[34].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 14) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[35].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 14) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[36].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 15) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[37].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 15) = 1, 'var(--sts-run)', if({view.custom.state} = 'bad', 'var(--neutral-60)', 'var(--text)'))
```


- `props.elements[41].text`: expression

```js
coalesce({view.params.name}, '')
```


- `props.elements[43].text`: expression

```js
case({view.custom.state}, 'ok', 'OK', 'fault', 'FAULT', 'conn', 'NO CONN', 'NO DATA')
```


- `props.elements[43].fill.paint`: expression

```js
case({view.custom.state}, 'ok', 'var(--sts-run)', 'fault', 'var(--sts-fault)', 'conn', 'var(--sts-fault)', 'var(--neutral-60)')
```


- `props.elements[43].style.fontStyle`: expression

```js
if({view.custom.state} = 'bad', 'italic', 'normal')
```


- `props.elements[44].stroke.paint`: expression

```js
if(coalesce({view.params.selected}, false), 'var(--sts-run)', 'none')
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
# read-only rack: a click only selects the module for the detail panel (page message)
member = str(self.view.params.member or '')
if member:
    system.perspective.sendMessage('plcRackSelect', payload={'member': member}, scope='page')
```

- **`root`** `dom.onMouseEnter`, script action, scope `G`

```python
# hover popover over the rack (UI state only; the page clears it on leave)
m = str(self.view.params.member or '')
if m:
    system.perspective.sendMessage('plcRackHover', payload={'member': m, 'leave': False}, scope='page')
```

- **`root`** `dom.onMouseLeave`, script action, scope `G`

```python
# hover popover over the rack (UI state only; the page clears it on leave)
m = str(self.view.params.member or '')
if m:
    system.perspective.sendMessage('plcRackHover', payload={'member': m, 'leave': True}, scope='page')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/Fault`, `/ReadBack`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
