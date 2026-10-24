---
title: "Numeric"
sidebar_label: "Numeric"
description: "Perspective view 03_Elements/03_Table/Numeric (Element (small reusable part)): 3 components, 10 bindings, 1 event scripts."
generated: true
keywords: ["03_Elements/03_Table/Numeric", "Numeric"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/03_Table/Numeric`.

| | |
|---|---|
| View path | `03_Elements/03_Table/Numeric` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/03_Table/Numeric/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 03\_Table &gt; Numeric |
| Root | `ia.container.flex`, height 30, width 100 |
| Size | 3 components, 10 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-24T18:51:20Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `value` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `engUnit` | `""` | bound (tag) |
| `format` | `"00000.00"` | bound (expr) |
| `quality` | `"Bad_NotFound(\"Path '[default]value.quality' not found.\")"` | bound (expr) |
| `tagPath` | `""` | bound (property) |
| `value` | `"00000.00"` | bound (tag) |
| `valuePath` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.display.markdown x1, ia.display.label x1.

```text
root  ia.container.flex  [1 binding; 1 event]
  Markdown  ia.display.markdown  [2 bindings]
  Label  ia.display.label  [1 binding]
```

## Bindings

10 bindings: expr 5, property 3, tag 2.

**`(view)`**

- `custom.engUnit`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}.EngUnit`, references `tagPath` = `{view.custom.valuePath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),"",{value})
```


- `custom.format`: expression, then expression + expression transform

```js
tag({view.custom.valuePath} + '.formatString')
```

Transform 1, expression:

```js
if(isNull({value}),'00000.00',if(indexOf({value},'#')!=-1,'00000.00',{value}))
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag({view.custom.valuePath} + '.formatString')), false), false), {value}, null)
```


- `custom.quality`: expression, then expression + expression transform

```js
tag({view.custom.valuePath} + '.Quality')
```

Transform 1, expression:

```js
if(isNull({value}),
	"",
	{value}
	)
```

Transform 2, expression:

```js
if(coalesce(try(isGood(tag({view.custom.valuePath} + '.Quality')), false), false), {value}, null)
```


- `custom.tagPath`: property `view.params.value`

- `custom.value`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}.value`, references `tagPath` = `{view.custom.valuePath}`, fallback delay 2.5 s

Transform 1, expression:

```js
forceQuality(if(isNull({value}) || coalesce({view.custom.quality}, '') != 'Good' || coalesce(try(abs(toFloat({value})) >= 1e30, false), false), '—', numberFormat({value}, {view.custom.format})))
```


- `custom.valuePath`: expression

```js
if(left(coalesce({view.params.value}, ''), 4) = 'pax:', substring({view.params.value}, 4), coalesce({view.params.value}, '') + '/Value')
```


**`root`**

- `meta.visible`: property `view.params.value`, then expression transform

Transform 1, expression:

```js
{value} != ''
```


**`root/Markdown`**

- `props.source`: property `view.custom.value`, then expression transform

Transform 1, expression:

```js
if({value} = '—' || {value} = '', {value}, if(indexOf({value}, ".") = -1,
    concat(
    		toInt({value}), 
			repeat("&nbsp;", 3)
	),
    concat(
			toInt(left({value}, indexOf({value}, "."))),
			right({value}, len({value}) - indexOf({value}, ".")),
			repeat("&nbsp;", 3 - (len({value}) - indexOf({value}, ".")))
	)
))
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.quality}, '') = 'Good' && coalesce({view.custom.value}, '') != '—', 'Fonts/LiveData', 'Fonts/LiveData value-bad')
```


**`root/Label`**

- `props.text`: expression

```js
if(coalesce({view.custom.value}, '') = '—', '', coalesce({view.custom.engUnit}, ''))
```


## Event Scripts And Handlers

- **`root`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.tagPath}')
```

## Related Views

**Opened or named by** (1): [00\_Pages/Groveport/Utility/OverviewKpis](../../00-pages/groveport/utility/overviewkpis.md)

**Named in project scripts**: [shared.Overview](../../../../../scripting/reference/modules/shared-overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `fs-11` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}.EngUnit`
- `{tagPath}.value`

Member paths appended to a base path in expressions (relative):

`.Quality`, `.formatString`, `/Value`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
