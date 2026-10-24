---
title: "StateText"
sidebar_label: "StateText"
description: "Perspective view 03_Elements/03_Table/StateText (Element (small reusable part)): 2 components, 8 bindings, 1 event scripts."
generated: true
keywords: ["03_Elements/03_Table/StateText", "StateText"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/03_Table/StateText`.

| | |
|---|---|
| View path | `03_Elements/03_Table/StateText` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/03_Table/StateText/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 03\_Table &gt; StateText |
| Root | `ia.container.flex`, height 30, width 100 |
| Size | 2 components, 8 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `commLoss` | `false` | input |
| `format` | `""` | input |
| `states` | `{}` | input |
| `value` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `quality` | `""` | bound (expr) |
| `raw` | `null` | bound (tag) |
| `tagPath` | `""` | bound (property) |
| `text` | `""` | bound (expr) |
| `valuePath` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1.

```text
root  ia.container.flex  [1 binding; 1 event]
  Label  ia.display.label  [2 bindings]
```

## Bindings

8 bindings: expr 5, property 2, tag 1.

**`(view)`**

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


- `custom.raw`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}.value`, references `tagPath` = `{view.custom.valuePath}`, fallback delay 2.5 s

Transform 1, expression:

```js
forceQuality({value})
```


- `custom.tagPath`: property `view.params.value`

- `custom.text`: expression

```js
if(coalesce({view.custom.tagPath}, '') != '' && coalesce({view.custom.quality}, '') != 'Good', if(coalesce({view.params.commLoss}, false), 'COMM LOSS', '—'), if(coalesce({view.custom.tagPath}, '') = '' || isNull({view.custom.raw}),
	'',
	coalesce(
		try({view.params.states}[toStr(toInt({view.custom.raw}))], null),
		if(len(coalesce({view.params.format}, '')) > 0,
			try(numberFormat({view.custom.raw}, {view.params.format}), ''),
			try(toStr({view.custom.raw}), '')))))
```


- `custom.valuePath`: expression

```js
if(left(coalesce({view.params.value}, ''), 4) = 'pax:', substring({view.params.value}, 4), coalesce({view.params.value}, '') + '/Value')
```


**`root`**

- `meta.visible`: expression

```js
coalesce({view.params.value}, '') != ''
```


**`root/Label`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.quality}, '') != 'Good', if(coalesce({view.params.commLoss}, false), 'Fonts/LiveData tank-level-text-critical fw-700', 'Fonts/LiveData value-bad'),
	if({view.custom.text} = 'Alarm' || {view.custom.text} = 'Fault' || {view.custom.text} = 'Not OK', 'Fonts/LiveData tank-level-text-critical fw-700', 'Fonts/LiveData'))
```


- `props.text`: property `view.custom.text`

## Event Scripts And Handlers

- **`root`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.tagPath}')
```

## Related Views

**Named in project scripts**: [shared.DevicePages](../../../../../scripting/reference/modules/shared-devicepages.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/LiveData` | bound | style class |
| `fw-700` | bound | style class |
| `tank-level-text-critical` | bound | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}.value`

Member paths appended to a base path in expressions (relative):

`.Quality`, `/Value`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
