---
title: "Interlocks"
sidebar_label: "Interlocks"
description: "Perspective view 01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks (Asset (embedded piece)): 7 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks", "Interlocks"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; \_Assets &gt; TankOverview &gt; Interlocks |
| Root | `ia.container.flex`, height 680, width 940 |
| Size | 7 components, 6 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-24T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x3, ia.display.label x2, ia.display.view x2.

```text
root  ia.container.flex  [2 bindings]
  Pump1  ia.container.flex
    Title  ia.display.label  [1 binding]
    Panel  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/InterlockPanel]
  Pump2  ia.container.flex
    Title  ia.display.label  [1 binding]
    Panel  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/InterlockPanel]
```

## Bindings

6 bindings: expr 6.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Pump1/Title`**

- `props.text`: expression

```js
'Pump #1  ·  ' + substring(substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1', lastIndexOf(substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1', '/') + 1)
```


**`root/Pump1/Panel`**

- `props.params.tagPath`: expression

```js
substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 1' + '/Interlock'
```


**`root/Pump2/Title`**

- `props.text`: expression

```js
'Pump #2  ·  ' + substring(substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2', lastIndexOf(substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2', '/') + 1)
```


**`root/Pump2/Panel`**

- `props.params.tagPath`: expression

```js
substring({view.params.tagPath}, 0, lastIndexOf({view.params.tagPath}, '/Tanks/')) + '/Pumps/' + left(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1), len(substring({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)) - 1) + 'LR-Pump 2' + '/Interlock'
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](../interlockpanel.md)

**Opened or named by** (1): [01\_Popups/00\_Faceplates/TankOverview](../../tankoverview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `fp-card-title` | 2 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/Interlock`, `/Pumps/`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
