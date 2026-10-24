---
title: "Configuration"
sidebar_label: "Configuration"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/Valve/Configuration (Asset (embedded piece)): 17 components, 29 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/Valve/Configuration", "Configuration"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/Valve/Configuration`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/Valve/Configuration` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Valve/Configuration/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; Valve &gt; Configuration |
| Root | `ia.container.flex`, height 480, width 420 |
| Size | 17 components, 29 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T05:04:23Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `hiddenTags` | `""` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roConfiguration` | `true` | bound (expr) |
| `tipConfiguration` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.view x8, ia.container.flex x5, ia.display.label x4.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Ident  ia.container.flex  [1 binding]
    IdentTitle  ia.display.label
    Desc  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
    Label  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
    Tag  ia.container.flex
      Lbl  ia.display.label
      Val  ia.display.view  [4 bindings; view: 03_Elements/00_Control/StringInput]
  LimitSwitches  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
  Behavior  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
  ObjectNav  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
  Deenergize  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
  Timing  ia.display.view  [2 bindings; view: 01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection]
```

</details>

## Bindings

29 bindings: expr 24, property 5.

<details>
<summary>All 29 bindings, grouped by component</summary>

**`(view)`**

- `custom.pax`: expression. Common pattern, see [pattern-6](../../../../../common-patterns.md#pattern-6).

- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../../../common-patterns.md#pattern-8).

- `custom.roConfiguration`: expression

```js
coalesce({session.custom.EngineeringReadOnly}, true) || !coalesce(coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null), try({session.custom.Permissions}[{view.custom.permDevice}]['Setpoint'], null)), true)
```


- `custom.tipConfiguration`: expression

```js
if(!coalesce({session.custom.EngineeringReadOnly}, true) && coalesce({view.custom.roConfiguration}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + if(isNull(try({session.custom.Permissions}[{view.custom.permDevice}]['Configuration'], null)), 'Setpoint', 'Configuration') + ' (Roles & Permissions)', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Ident`**

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Ident/Desc/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/Valve/Cfg_Desc')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Ident/Label/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/Valve/Cfg_Label')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/Ident/Tag/Val`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/Valve/Cfg_Tag')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roConfiguration}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipConfiguration} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipConfiguration}
```


**`root/LimitSwitches`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Behavior`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/ObjectNav`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Deenergize`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```


**`root/Timing`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

- `position.display`: expression

```js
coalesce({session.custom.EngineeringView}, false)
```

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (2): [01\_Popups/00\_Faceplates/\_Assets/Configuration/ConfigSection](../configuration/configsection.md), [03\_Elements/00\_Control/StringInput](../../../../03-elements/00-control/stringinput.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/Faceplate](../../faceplate.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 4 | style class |
| `faceplate-section` | 1 | style class |
| `faceplate-section-card` | 1 | style class |
| `faceplate-section-title` | 1 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Valve/Cfg_Desc`, `/Valve/Cfg_Label`, `/Valve/Cfg_Tag`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
