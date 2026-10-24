---
title: "ConfigurationRow"
sidebar_label: "ConfigurationRow"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow (Asset (embedded piece)): 3 components, 20 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow", "ConfigurationRow"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Configuration &gt; ConfigurationRow |
| Root | `ia.container.flex`, height 36, width 704 |
| Size | 3 components, 20 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T20:12:34Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `highlightRow` | `false` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `dataType` | `""` | bound (expr) |
| `isBoolean` | `false` | bound (expr) |
| `isMultistate` | `false` | bound (property) |
| `metadata` | `""` | bound (tag) |
| `permDevice` | `""` | bound (expr) |
| `roSetpoint` | `true` | bound (expr) |
| `tipSetpoint` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.view x2, ia.container.flex x1.

```text
root  ia.container.flex  [3 bindings]
  AnalogView  ia.display.view  [5 bindings; view: 03_Elements/00_Control/AnalogInput]
  MultiStateView  ia.display.view  [5 bindings; view: 03_Elements/00_Control/MultiStateInput]
```

## Bindings

20 bindings: expr 16, property 3, tag 1.

<details>
<summary>All 20 bindings, grouped by component</summary>

**`(view)`**

- `custom.dataType`: expression

```js
if(try(isGood(tag({view.params.tagPath} + '.DataType')), false),
   toStr(try(if(!isGood(tag({view.params.tagPath} + '.DataType')), null, tag({view.params.tagPath} + '.DataType')), null)),
   '')
```


- `custom.isBoolean`: expression

```js
{view.custom.dataType} = 'Boolean'
```


- `custom.metadata`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}.Metadata`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	"",
	{value}
	)
```


- `custom.isMultistate`: property `view.custom.metadata`, then script transform

Transform 1, script:

```python
# Multistate only when metadata defines states — not every Int4
# (e.g. TravelTime is Int4 seconds and must use AnalogInput).
if value is None or value == '':
    return False
states = None
try:
    states = value.get('states') if hasattr(value, 'get') else value['states']
except:
    try:
        states = value['states']
    except:
        states = None
return bool(states)
```


- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roSetpoint`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), true)
```


- `custom.tipSetpoint`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roSetpoint}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), 'Configuration', 'Setpoint') + ' (Roles & Permissions)', '')
```


**`root`**

- `props.style.background`: expression

```js
if ({view.params.highlightRow},
	'var(--neutral-50)',
	'var(--neutral-40)')  
```


- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/AnalogView`**

- `position.display`: expression

```js
!{view.custom.isBoolean} && !{view.custom.isMultistate}
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `props.params.permission`: expression

```js
!{view.custom.roSetpoint}
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```


**`root/MultiStateView`**

- `position.display`: expression

```js
{view.custom.isMultistate} || {view.custom.isBoolean}
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `props.params.permission`: expression

```js
!{view.custom.roSetpoint}
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipSetpoint} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipSetpoint}
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (2): [03\_Elements/00\_Control/AnalogInput](../../../../03-elements/00-control/analoginput.md), [03\_Elements/00\_Control/MultiStateInput](../../../../03-elements/00-control/multistateinput.md)

**Embedded in** (1): [01\_Popups/00\_Faceplates/\_Assets/Configuration/Configuration](./configuration.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `faceplate-config-row` | 1 | stylesheet |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`
- `{tagPath}.Metadata`

Member paths appended to a base path in expressions (relative):

`.DataType`, `.TypeId`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
