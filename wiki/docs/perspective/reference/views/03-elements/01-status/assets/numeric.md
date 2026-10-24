---
title: "Numeric"
sidebar_label: "Numeric"
description: "Perspective view 03_Elements/01_Status/_Assets/Numeric (Asset (embedded piece)): 3 components, 18 bindings, 2 event scripts."
generated: true
keywords: ["03_Elements/01_Status/_Assets/Numeric", "Numeric"]
---

:::note

:::


**Asset (embedded piece)**: `03_Elements/01_Status/_Assets/Numeric`.

| | |
|---|---|
| View path | `03_Elements/01_Status/_Assets/Numeric` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/_Assets/Numeric/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; \_Assets &gt; Numeric |
| Root | `ia.container.flex`, height 18, width 92 |
| Size | 3 components, 18 bindings, 2 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-24T03:44:26Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `compact` | `false` | input |
| `spacing` | `{"center": false, "data": 0, "engUnit": 30}` | inout |
| `tagPath` | `""` | input |
| `spTagPath` | `""` | input |
| `forceColor` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `engUnit` | `""` | bound (expr) |
| `format` | `""` | bound (expr) |
| `quality` | `"Uncertain_InitialValue"` | bound (tag) |
| `type` | `"Integer"` | bound (expr) |
| `value` | `""` | bound (expr) |
| `overSp` | `false` | bound (expr) |
| `ok` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1.

```text
root  ia.container.flex  [1 binding; 1 event]
  Value  ia.display.label  [7 bindings; 1 event]
  EngineeringUnit  ia.display.label  [3 bindings]
```

## Bindings

18 bindings: expr 15, property 2, tag 1.

<details>
<summary>All 18 bindings, grouped by component</summary>

**`(view)`**

- `custom.engUnit`: expression

```js
if({view.custom.quality} = 'Good',
   tag({view.params.tagPath} + '.EngUnit'),
   '')
```


- `custom.format`: expression

```js
if({view.custom.quality} = 'Good',
   if({view.custom.type} = 'Integer',
      '#',
      if(isNull(tag({view.params.tagPath} + '.FormatString')) || tag({view.params.tagPath} + '.FormatString') = '',
         '#0.0',
         tag({view.params.tagPath} + '.FormatString'))),
   '')
```


- `custom.quality`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
qualityOf({value})
```


- `custom.type`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath})), false), false), typeOf(tag({view.params.tagPath})), null)
```


- `custom.value`: expression

```js
if({view.params.tagPath} = '', '', if(coalesce({view.custom.ok}, false), coalesce(try(numberFormat(tag({view.params.tagPath}), {view.custom.format}), null), '—'), '—'))
```


- `custom.overSp`: expression

```js
if({view.params.tagPath} = '' || {view.params.spTagPath} = '' || {view.custom.quality} != 'Good' || !isGood(tag({view.params.spTagPath})),
	false,
	tag({view.params.tagPath}) > tag({view.params.spTagPath}))
```


- `custom.ok`: expression

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath})), false), false) && !isNull(try(tag({view.params.tagPath}), null)) && coalesce(try(abs(toFloat(tag({view.params.tagPath}))) < 1e30, true), true)
```


**`root`**

- `props.justify`: expression

```js
if({view.params.spacing.center},
	'center',
	'flex-start')
```


**`root/Value`**

- `position.grow`: expression

```js
if({view.params.spacing.center},
	0,
	1)
```


- `props.style.color`: expression

```js
if({view.custom.quality} != 'Good',
	'#90A4AE',
	if({view.params.forceColor} = 'alarm', 'var(--error)', if({view.params.forceColor} = 'critical',
		'var(--status-level-critical, var(--analog-over-sp))',
		if({view.params.forceColor} = 'warning',
			'var(--status-level-warning)',
			if({view.custom.overSp},
				'var(--analog-over-sp)',
				'var(--accent)')))))
```


- `props.style.fontSize`: expression

```js
if({view.params.compact},
	'11px',
	'14px')
```


- `props.style.paddingRight`: expression

```js
if({view.params.spacing.data} = '',
	'0em',
	0.85 * {view.params.spacing.data} + 'em')
```


- `props.style.textAlign`: expression

```js
if({view.params.spacing.center},
	'left',
	'right')
```


- `props.text`: property `view.custom.value`

- `props.style.classes`: expression

```js
if(coalesce({view.params.tagPath}, '') != '' && !coalesce({view.custom.ok}, false), 'value-bad', if({view.params.forceColor} = 'alarm', 'value-alarm', if({view.params.forceColor} = 'critical',
	'analog-over-sp',
	if({view.params.forceColor} = 'warning',
		'analog-level-warning',
		if({view.custom.overSp},
			'analog-over-sp',
			'')))))
```


**`root/EngineeringUnit`**

- `position.grow`: expression

```js
if({view.params.spacing.center},
	0,
	1)
```


- `position.basis`: expression

```js
if({view.params.spacing.center},
	'auto',
	if({view.params.spacing.engUnit} = '',
		'auto',
		{view.params.spacing.engUnit} + 'px'))
```


- `props.text`: property `view.custom.engUnit`

</details>

## Event Scripts And Handlers

- **`root`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}')
```

- **`root/Value`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.params.tagPath}')
```

## Related Views

**Embedded in** (1): [03\_Elements/01\_Status/AnalogValue](../analogvalue.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `analog-level-warning` | bound | stylesheet |
| `analog-over-sp` | bound | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `{tagPath}`

Member paths appended to a base path in expressions (relative):

`.EngUnit`, `.FormatString`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
