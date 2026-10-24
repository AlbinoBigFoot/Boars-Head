---
title: "StatusDot"
sidebar_label: "StatusDot"
description: "Perspective view 03_Elements/01_Status/StatusDot (Element (small reusable part)): 3 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/01_Status/StatusDot", "StatusDot"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/01_Status/StatusDot`.

| | |
|---|---|
| View path | `03_Elements/01_Status/StatusDot` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/StatusDot/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 01\_Status &gt; StatusDot |
| Root | `ia.container.flex`, height 48, width 72 |
| Size | 3 components, 6 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T06:30:48Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | input |
| `okValue` | `true` | input |
| `tagPath` | `""` | input |
| `blink` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `quality` | `"Bad_NotFound"` | bound (expr) |
| `value` | `false` | bound (expr) |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x1.

```text
root  ia.container.flex  [2 bindings]
  Label  ia.display.label  [1 binding]
  Dot  ia.container.flex  [1 binding]
```

## Bindings

6 bindings: expr 5, property 1.

**`(view)`**

- `custom.quality`: expression

```js
if({view.params.tagPath} = '',
	'Bad_NotFound',
	qualityOf(tag({view.params.tagPath})))
```


- `custom.value`: expression

```js
if({view.params.tagPath} = '' || left({view.custom.quality}, 4) != 'Good',
	false,
	coalesce(tag({view.params.tagPath}), false))
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/Label`**

- `props.text`: property `view.params.label`

**`root/Dot`**

- `props.style.classes`: expression

```js
if({view.params.tagPath} = '' || left({view.custom.quality}, 4) != 'Good',
	'status-dot status-dot-unknown',
	if({view.custom.value} = {view.params.okValue},
		'status-dot status-dot-ok',
		if(coalesce({view.params.blink}, false),
			'status-dot status-dot-alarm status-dot-blink',
			'status-dot status-dot-alarm')))
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [02\_Components/02\_Widgets/Safetys](../../02-components/02-widgets/safetys.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `fs-11` | 1 | style class |
| `fw-700` | 1 | style class |
| `status-dot-root` | 1 | stylesheet |
| `status-dot` | bound | stylesheet |
| `status-dot-alarm` | bound | stylesheet |
| `status-dot-blink` | bound | style class |
| `status-dot-ok` | bound | stylesheet |
| `status-dot-unknown` | bound | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
