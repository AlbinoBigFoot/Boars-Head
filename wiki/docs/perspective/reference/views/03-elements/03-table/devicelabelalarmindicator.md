---
title: "DeviceLabelAlarmIndicator"
sidebar_label: "DeviceLabelAlarmIndicator"
description: "Perspective view 03_Elements/03_Table/DeviceLabelAlarmIndicator (Element (small reusable part)): 3 components, 11 bindings, 0 event scripts."
generated: true
keywords: ["03_Elements/03_Table/DeviceLabelAlarmIndicator", "DeviceLabelAlarmIndicator"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/03_Table/DeviceLabelAlarmIndicator`.

| | |
|---|---|
| View path | `03_Elements/03_Table/DeviceLabelAlarmIndicator` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/03_Table/DeviceLabelAlarmIndicator/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 03\_Table &gt; DeviceLabelAlarmIndicator |
| Root | `ia.container.flex`, height 30, width 200 |
| Size | 3 components, 11 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-24T13:59:54Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `value` | `"[default]Evaporators/EV-001"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `flash` | `true` | bound (tag) |
| `icon` | `"03_Elements/01_Status/NotificationIcons/Alarms/Medium"` | bound (tag) |
| `metadata` | `""` | bound (expr) |
| `tagName` | `"EV-001"` | bound (tag) |
| `tagPath` | `"[default]Evaporators/EV-001"` | bound (property) |
| `textAlign` | `"left"` | |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1, ia.display.label x1.

```text
root  ia.container.flex  [2 bindings]
  Icon  ia.display.view  [2 bindings; view: (bound)]
  Label  ia.display.label  [2 bindings]
```

## Bindings

11 bindings: property 4, tag 3, expr-struct 3, expr 1.

**`(view)`**

- `custom.flash`: tag, then expression transform

Mode `indirect`, tag path `{value}/_Alarms/_Flash`, references `value` = `{view.params.value}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	False,
	{value}
)
```


- `custom.icon`: tag, then expression transform

Mode `indirect`, tag path `{value}/_Alarms/_Icon`, references `value` = `{view.params.value}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	'03_Elements/01_Status/NotificationIcons/Blank',
	{value}
)
```


- `custom.metadata`: expression, then expression + expression transform

```js
tag(tag({tagPath} + ".metadata")
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
if(coalesce(try(isGood(tag({tagPath} + ".metadata")), false), false), {value}, null)
```


- `custom.tagName`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}.Name`, references `tagPath` = `{view.custom.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	"",
	{value}
	)
```


- `custom.tagPath`: property `view.params.value`

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

**`root/Icon`**

- `meta.visible`: property `view.custom.flash`

- `props.path`: property `view.custom.icon`

**`root/Label`**

- `props.text`: structured expression (expr-struct), then expression transform

```js
metadata: {view.custom.metadata}
tagName: {view.custom.tagName}
tagPath: {view.params.value}
```

waitOnAll: `True`

Transform 1, expression:

```js
if(len(coalesce({value}['tagPath'], '')) = 0, '', if(indexOf({value}['tagPath'], 'AppliedDigital') >= 0 || indexOf({value}['tagPath'], 'HDB') >= 0 || indexOf({value}['tagPath'], '/Condensers/Condensers/') >= 0, concat(split({value}['tagPath'], '/')[len(split({value}['tagPath'], '/')) - 2, 0], '-', split({value}['tagPath'], '/')[len(split({value}['tagPath'], '/')) - 1, 0]), coalesce(if(len(coalesce(try({value}['metadata']['shortDescription'], ''), '')) > 0, {value}['metadata']['shortDescription'], null), if(len(coalesce({value}['tagName'], '')) > 0, {value}['tagName'], null), split({value}['tagPath'], '/')[len(split({value}['tagPath'], '/')) - 1, 0])))
```


- `props.textStyle.textAlign`: property `view.custom.textAlign`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Bound embeds** (view path set by a binding): `root/Icon`

**Opens or names** (popups, scripts, expressions): [03\_Elements/01\_Status/NotificationIcons/Alarms/Medium](../01-status/notificationicons/alarms/medium.md), [03\_Elements/01\_Status/NotificationIcons/Blank](../01-status/notificationicons/blank.md)

**Named in project scripts**: [shared.Overview](../../../../../scripting/reference/modules/shared-overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}.Name`
- `{value}/_Alarms/_Flash`
- `{value}/_Alarms/_Icon`

Member paths appended to a base path in expressions (relative):

`.metadata`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
