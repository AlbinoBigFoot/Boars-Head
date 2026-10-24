---
title: "Controller_CompactLogix_5370"
sidebar_label: "Controller_CompactLogix_5370"
description: "Perspective view 02_Components/03_PLC/Controller_CompactLogix_5370 (Reusable component): 2 components, 27 bindings, 3 event scripts."
generated: true
keywords: ["02_Components/03_PLC/Controller_CompactLogix_5370", "Controller_CompactLogix_5370"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/Controller_CompactLogix_5370`.

| | |
|---|---|
| View path | `02_Components/03_PLC/Controller_CompactLogix_5370` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/Controller_CompactLogix_5370/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; Controller\_CompactLogix\_5370 |
| Root | `ia.container.flex`, width 114, height 280 |
| Size | 2 components, 27 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `member` | `"Controller"` | input |
| `selected` | `false` | input |
| `state` | `"Normal"` | input |
| `label` | `"BoarsHead"` | input |
| `name` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `preview` | `"normal"` | bound (expr) |
| `conn` | `false` | bound (expr) |
| `statusGood` | `false` | bound (expr) |
| `run` | `false` | bound (expr) |
| `major` | `false` | bound (expr) |
| `mode` | `"NO COMM"` | bound (expr) |
| `catalog` | `"1769-L36ERM"` | bound (expr) |
| `state` | `"bad"` | bound (expr) |
| `ip` | `""` | bound (expr) |
| `name` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [3 bindings; 3 events]
  Controller  ia.shapes.svg  [14 bindings]
```

## Bindings

27 bindings: expr 27.

<details>
<summary>All 27 bindings, grouped by component</summary>

**`(view)`**

- `custom.ip`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/IPAddress')), false), false), if(coalesce({view.params.tagPath}, '') = '', 'x.x.x.x', coalesce(try(toStr(tag({view.params.tagPath} + '/IPAddress')), null), '')), null)
```


- `custom.name`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/ControllerName')), false), false), if(coalesce({view.params.name}, '') != '', {view.params.name}, if(coalesce({view.params.tagPath}, '') = '', coalesce({view.params.label}, 'BoarsHead'), coalesce(try(toStr(tag({view.params.tagPath} + '/ControllerName')), null), ''))), null)
```


- `custom.preview`: expression

```js
lower(trim(coalesce({view.params.state}, 'normal')))
```


- `custom.conn`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} != 'comm loss', coalesce(try(isGood(tag({view.params.tagPath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.tagPath} + '/Connected')), false), false))
```


- `custom.statusGood`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.conn}, {view.custom.conn} && coalesce(try(isGood(tag({view.params.tagPath} + '/Status')), false), false))
```


- `custom.run`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', {view.custom.statusGood} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/Run')), false), false))
```


- `custom.major`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'fault', {view.custom.statusGood} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/MajorFault')), false), false))
```


- `custom.mode`: expression

```js
if(!{view.custom.conn}, 'NO COMM', if(coalesce({view.params.tagPath}, '') = '', if({view.custom.major}, 'MAJOR FAULT', 'REMOTE RUN'), if(!{view.custom.statusGood}, 'NO DATA', upper(coalesce(try(toStr(tag({view.params.tagPath} + '/Mode')), null), 'Unknown')))))
```


- `custom.catalog`: expression

```js
coalesce(if(coalesce({view.params.tagPath}, '') = '', null, try(if(isGood(tag({view.params.tagPath} + '/ProductName')) && len(trim(toStr(tag({view.params.tagPath} + '/ProductName')))) > 0, split(trim(toStr(tag({view.params.tagPath} + '/ProductName'))), ' ')[0, 0], null), null)), if(coalesce({view.params.tagPath}, '') = '', null, try(toStr(tag({view.params.tagPath} + '/CatalogNumber')), null)), '1769-L36ERM')
```


- `custom.state`: expression

```js
if(!{view.custom.conn}, 'bad', if({view.custom.major}, 'fault', if({view.custom.statusGood}, 'ok', 'bad')))
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

- `props.style.classes`: expression

```js
if(coalesce({view.params.member}, '') != '', 'faceplate-hover', '')
```


**`root/Controller`**

- `props.elements[2].text`: expression

```js
{view.custom.catalog}
```


- `props.elements[4].fill.paint`: expression

```js
if({view.custom.run}, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[10].fill.paint`: expression

```js
if({view.custom.major}, 'var(--sts-fault)', if({view.custom.conn}, 'var(--sts-run)', 'var(--neutral-60)'))
```


- `props.elements[12].fill.paint`: expression

```js
if({view.custom.conn}, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[14].fill.paint`: expression

```js
if({view.custom.conn}, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[19].text`: expression

```js
{view.custom.mode}
```


- `props.elements[19].fill.paint`: expression

```js
if({view.custom.run}, 'var(--sts-run)', if({view.custom.major} || !{view.custom.conn}, 'var(--sts-fault)', if({view.custom.statusGood}, 'var(--text)', 'var(--neutral-60)')))
```


- `props.elements[19].style.fontStyle`: expression

```js
if({view.custom.conn} && !{view.custom.statusGood}, 'italic', 'normal')
```


- `props.elements[26].text`: expression

```js
{view.custom.ip}
```


- `props.elements[27].text`: expression

```js
{view.custom.name}
```


- `props.elements[28].text`: expression

```js
case({view.custom.state}, 'ok', if({view.custom.run}, 'RUN', 'NOT RUN'), 'fault', 'MAJOR FAULT', if({view.custom.conn}, 'NO DATA', 'COMM LOSS'))
```


- `props.elements[28].fill.paint`: expression

```js
case({view.custom.state}, 'ok', if({view.custom.run}, 'var(--sts-run)', 'var(--status-off)'), 'fault', 'var(--sts-fault)', if({view.custom.conn}, 'var(--neutral-60)', 'var(--sts-fault)'))
```


- `props.elements[28].style.fontStyle`: expression

```js
if({view.custom.conn} && {view.custom.state} = 'bad', 'italic', 'normal')
```


- `props.elements[29].stroke.paint`: expression

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

## Related Views

**Opened or named by** (1): [02\_Components/03\_PLC/RackSlot](./rackslot.md)

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/CatalogNumber`, `/Connected`, `/ControllerName`, `/IPAddress`, `/MajorFault`, `/Mode`, `/ProductName`, `/Run`, `/Status`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
