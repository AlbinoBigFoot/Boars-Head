---
title: "PointRow"
sidebar_label: "PointRow"
description: "Perspective view 02_Components/03_PLC/PointRow (Reusable component): 6 components, 24 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/03_PLC/PointRow", "PointRow"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/PointRow`.

| | |
|---|---|
| View path | `02_Components/03_PLC/PointRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/PointRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; PointRow |
| Root | `ia.container.flex`, width 520, height 24 |
| Size | 6 components, 24 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `point` | `0` | input |
| `kind` | `"DI"` | input |
| `description` | `"Not Documented"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `good` | `false` | bound (expr) |
| `value` | `null` | bound (expr) |
| `on` | `false` | bound (expr) |
| `ma` | `null` | bound (expr) |
| `unit` | `""` | bound (expr) |
| `cmd` | `false` | bound (expr) |
| `range` | `""` | bound (expr) |
| `cfg` | `""` | bound (expr) |
| `extra` | `""` | bound (expr) |
| `trendPath` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x5, ia.container.flex x1.

```text
root  ia.container.flex  [1 event]
  Point  ia.display.label  [1 binding]
  Led  ia.display.label  [1 binding]
  Description  ia.display.label  [4 bindings]
  State  ia.display.label  [3 bindings]
  Extra  ia.display.label  [5 bindings]
```

## Bindings

24 bindings: expr 22, property 2.

<details>
<summary>All 24 bindings, grouped by component</summary>

**`(view)`**

- `custom.good`: expression

```js
coalesce({view.params.tagPath}, '') != '' && coalesce(try(isGood(tag({view.params.tagPath} + '/' + if(coalesce({view.params.kind}, '') = 'AI', 'Ch' + toStr(coalesce({view.params.point}, 0)) + 'Data', if(coalesce({view.params.kind}, '') = 'DO', 'ReadBack', 'Data')))) && isGood(tag({view.params.tagPath} + '/Fault')) && coalesce(toInt(tag({view.params.tagPath} + '/Fault')), -1) = 0, false), false)
```


- `custom.value`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/' + if(coalesce({view.params.kind}, '') = 'AI', 'Ch' + toStr(coalesce({view.params.point}, 0)) + 'Data', if(coalesce({view.params.kind}, '') = 'DO', 'ReadBack', 'Data')))), false), false), if({view.custom.good}, try(toInt(tag({view.params.tagPath} + '/' + if(coalesce({view.params.kind}, '') = 'AI', 'Ch' + toStr(coalesce({view.params.point}, 0)) + 'Data', if(coalesce({view.params.kind}, '') = 'DO', 'ReadBack', 'Data')))), null), null), '—')
```


- `custom.on`: expression

```js
coalesce({view.params.kind}, '') != 'AI' && !isNull({view.custom.value}) && getBit(coalesce({view.custom.value}, 0), coalesce({view.params.point}, 0)) = 1
```


- `custom.ma`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'Signal')), false), false)), if({view.custom.good} && coalesce({view.params.kind}, '') = 'AI' && coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'Signal')), null), null), null)
```


- `custom.unit`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'Unit')), false), false), if(coalesce({view.params.kind}, '') = 'AI', coalesce(try(toStr(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'Unit')), ''), ''), ''), null)
```


- `custom.cmd`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Data')), false), false), if(coalesce({view.params.kind}, '') = 'DO' && {view.custom.good}, getBit(coalesce(try(toInt(tag({view.params.tagPath} + '/Data')), 0), 0), coalesce({view.params.point}, 0)) = 1, false), null)
```


- `custom.range`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'UnderRange')), false), false)), if(coalesce({view.params.kind}, '') != 'AI' || !{view.custom.good}, '', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'OverRange')), false), false), 'Over Range', if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'UnderRange')), false), false), 'Under Range', 'In Range'))), null)
```


- `custom.cfg`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'RangeText')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'En')), false), false)), if(coalesce({view.params.kind}, '') != 'AI' || !{view.custom.good}, '', coalesce(try(toStr(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'RangeText')), null), '?') + if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch' + toStr(coalesce({view.params.point}, 0)) + 'En')), true), true), '', ' Disabled')), null)
```


- `custom.extra`: expression

```js
if(!{view.custom.good}, '', if(coalesce({view.params.kind}, '') = 'DO', 'Cmd ' + if({view.custom.cmd}, 'On', 'Off'), if(coalesce({view.params.kind}, '') = 'AI', {view.custom.range} + ' · Raw ' + toStr({view.custom.value}) + ' · ' + {view.custom.cfg}, '')))
```


- `custom.trendPath`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', {view.params.tagPath} + '/' + if(coalesce({view.params.kind}, '') = 'AI', 'Ch' + toStr(coalesce({view.params.point}, 0)) + 'Data', 'Data'))
```


**`root/Point`**

- `props.text`: expression

```js
if(coalesce({view.params.point}, 0) < 10, '0', '') + toStr(coalesce({view.params.point}, 0))
```


**`root/Led`**

- `props.style.backgroundColor`: expression

```js
if(!{view.custom.good}, 'var(--neutral-60)', if(coalesce({view.params.kind}, '') = 'AI', if({view.custom.range} = 'In Range', 'var(--sts-run)', 'var(--status-level-warning)'), if({view.custom.on}, 'var(--sts-run)', 'var(--neutral-60)')))
```


**`root/Description`**

- `props.text`: expression

```js
coalesce({view.params.description}, 'Not Documented')
```


- `props.style.classes`: expression

```js
if(coalesce({view.params.description}, 'Not Documented') = 'Not Documented', 'fs-12 fw-400 value-bad', 'fs-12 fw-400')
```


- `meta.tooltip.text`: expression

```js
coalesce({view.params.description}, 'Not Documented')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/State`**

- `props.text`: expression

```js
if(!{view.custom.good}, '--', if(coalesce({view.params.kind}, '') = 'AI', if(isNull({view.custom.ma}), '--', numberFormat({view.custom.ma}, '0.00') + ' ' + {view.custom.unit}), if({view.custom.on}, 'On', 'Off')))
```


- `props.style.classes`: expression

```js
if({view.custom.good}, 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `props.style.color`: expression

```js
if(!{view.custom.good}, 'var(--neutral-60)', if(coalesce({view.params.kind}, '') = 'AI', 'var(--text)', if({view.custom.on}, 'var(--sts-run)', 'var(--status-off)')))
```


**`root/Extra`**

- `props.text`: property `view.custom.extra`

- `position.basis`: expression

```js
if(coalesce({view.params.kind}, '') = 'AI', '200px', '64px')
```


- `position.display`: expression

```js
coalesce({view.params.kind}, '') != 'DI'
```


- `meta.tooltip.text`: property `view.custom.extra`

- `meta.tooltip.enabled`: expression

```js
true
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.trendPath}')
```

## Related Views

**Embedded in** (1): [02\_Components/03\_PLC/ModuleDetail](./moduledetail.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `fs-11` | 1 | style class |
| `fs-12` | 3 | style class |
| `fw-400` | 2 | style class |
| `fw-600` | 1 | style class |
| `fw-700` | 1 | style class |
| `text-muted` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/Ch`, `/Data`, `/Fault`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
