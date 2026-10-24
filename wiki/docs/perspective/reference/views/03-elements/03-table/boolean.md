---
title: "Boolean"
sidebar_label: "Boolean"
description: "Perspective view 03_Elements/03_Table/Boolean (Element (small reusable part)): 2 components, 10 bindings, 1 event scripts."
generated: true
keywords: ["03_Elements/03_Table/Boolean", "Boolean"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/03_Table/Boolean`.

| | |
|---|---|
| View path | `03_Elements/03_Table/Boolean` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/03_Table/Boolean/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 03\_Table &gt; Boolean |
| Root | `ia.container.flex`, height 20, width 100 |
| Size | 2 components, 10 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-07-24T18:51:20Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `value` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `marginRight` | `"0%"` | |
| `multistates` | `""` | bound (expr) |
| `quality` | `"Bad_NotFound(\"Path '[default]value.quality' not found.\")"` | bound (expr) |
| `tagPath` | `""` | bound (property) |
| `textAlign` | `"center"` | |
| `value` | `""` | bound (tag) |
| `valuePath` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.display.markdown x1.

```text
root  ia.container.flex  [1 binding; 1 event]
  Markdown  ia.display.markdown  [4 bindings]
```

## Bindings

10 bindings: property 5, expr 3, tag 1, expr-struct 1.

**`(view)`**

- `custom.multistates`: expression

```js
if({view.custom.tagPath} = '',
	'',
	if(isGood(tag({view.custom.valuePath} + '.Metadata')),
		if(isNull(tag({view.custom.valuePath} + '.Metadata')['states']),
			'',
			tag({view.custom.valuePath} + '.Metadata')['states']),
		if(isGood(tag({view.custom.tagPath} + '/Metadata')),
			if(isNull(jsonGet(tag({view.custom.tagPath} + '/Metadata'), 'states')),
				'',
				jsonGet(tag({view.custom.tagPath} + '/Metadata'), 'states')),
			'')))
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
forceQuality(if(isNull({value}) || coalesce({view.custom.quality}, '') != 'Good', '—', {value}))
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

- `props.source`: structured expression (expr-struct), then script transform

```js
multistates: {view.custom.multistates}
value: {view.custom.value}
```

waitOnAll: `True`

Transform 1, script:

```python
from shared import Utilities
result = Utilities.getLabelValue(value.value, value.multistates)
if result in (None, '') and value.value not in (None, ''):
    try:
        v = int(value.value)
        fallback = {0: 'Off', 1: 'Cooling', 2: 'Defrost', 3: 'Fault', 5: 'Idle'}
        result = fallback.get(v, unicode(value.value))
    except:
        result = unicode(value.value)
return (result if result is not None else '') + "&nbsp;"
```


- `props.style.classes`: property `view.custom.quality`, then expression transform

Transform 1, expression:

```js
if({value} = "Good",
	'Fonts/LiveData',
	'Fonts/LiveData value-bad'
	)
```


- `props.style.marginRight`: property `view.custom.marginRight`

- `props.style.textAlign`: property `view.custom.textAlign`

## Event Scripts And Handlers

- **`root`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.tagPath}')
```

## Related Views

**Named in project scripts**: [shared.Overview](../../../../../scripting/reference/modules/shared-overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/LiveData` | bound | style class |
| `value-bad` | bound | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}.value`

Member paths appended to a base path in expressions (relative):

`.Metadata`, `.Quality`, `/Metadata`, `/Value`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
