---
title: "AhuEvapDisplay"
sidebar_label: "AhuEvapDisplay"
description: "Perspective view 00_Pages/Groveport/_Shared/CG/AhuEvapDisplay (Page piece (not routed)): 17 components, 15 bindings, 3 event scripts."
generated: true
keywords: ["00_Pages/Groveport/_Shared/CG/AhuEvapDisplay", "AhuEvapDisplay"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/_Shared/CG/AhuEvapDisplay`.

| | |
|---|---|
| View path | `00_Pages/Groveport/_Shared/CG/AhuEvapDisplay` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/_Shared/CG/AhuEvapDisplay/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; \_Shared &gt; CG &gt; AhuEvapDisplay |
| Root | `ia.container.flex`, height 1110, width 1920 |
| Size | 17 components, 15 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-01T06:59:11Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |
| `label` | `""` | input |
| `tagPath` | `""` | input |
| `bleed` | `true` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `cgOrder` | `["CG-A1", "CG-A2", "CG-B1", "CG-B2", "CG-C1", "CG-D1", "CG-E1", "CG...` | |
| `hasBleed` | `true` | bound (expr) |

## Component Tree

Component types: ia.display.view x8, ia.display.label x3, ia.input.button x3, ia.container.coord x2, ia.container.flex x1.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Canvas  ia.container.coord  [1 binding]
    Pid  ia.container.coord  [1 binding]
      Evap  ia.display.view  [2 bindings; view: 02_Components/01_Devices/Evaporator]
      EvapCoil  ia.display.view  [view: 02_Components/01_Devices/EvapCoilSerpentine]
      Bleed SV  ia.display.view  [3 bindings; view: 02_Components/01_Devices/SolenoidValve]
      Suction SV  ia.display.view  [1 binding; view: 02_Components/01_Devices/SolenoidValve]
      Hot Gas SV  ia.display.view  [1 binding; view: 02_Components/01_Devices/SolenoidValve]
      Liquid SV  ia.display.view  [1 binding; view: 02_Components/01_Devices/SolenoidValve]
      Lbl-MTRS  ia.display.label
      Lbl-HGD  ia.display.label
      Lbl-MTRL  ia.display.label
    HistoryCard  ia.display.view  [1 binding; view: 00_Pages/Groveport/_Shared/CG/AhuEvapHistory]
    ControlPanel  ia.display.view  [1 binding; view: 00_Pages/Groveport/_Shared/CG/AhuEvapPanel]
    BackToOverview  ia.input.button  [1 event]
    PrevCg  ia.input.button  [1 event]
    NextCg  ia.input.button  [1 event]
```

</details>

## Bindings

15 bindings: expr 10, property 4, expr-struct 1.

<details>
<summary>All 15 bindings, grouped by component</summary>

**`(view)`**

- `custom.hasBleed`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_HasBleedValve')), false), false), coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/Cfg_HasBleedValve')), null), toBoolean(coalesce({view.params.bleed}, true))), toBoolean(coalesce({view.params.bleed}, true)))
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Canvas`**

- `props.style.transform`: structured expression (expr-struct), then script transform

```js
defaultViewHeight: {view.props.defaultSize.height}
defaultViewWidth: {view.props.defaultSize.width}
primaryViewHeight: {page.props.dimensions.primaryView.height}
primaryViewWidth: {page.props.dimensions.primaryView.width}
scale: {view.params.Scale}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.Scale.cssTransform(value)
```


**`root/Canvas/Pid`**

- `props.pipes[1].visible`: expression

```js
toBoolean(coalesce({view.custom.hasBleed}, true))
```


**`root/Canvas/Pid/Evap`**

- `props.params.label`: property `view.params.label`

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Canvas/Pid/Bleed SV`**

- `props.params.tagPath`: expression

```js
if(!toBoolean(coalesce({view.custom.hasBleed}, true)) || {view.params.tagPath} = "", "", {view.params.tagPath} + "/Valves/Bleed SV")
```


- `meta.visible`: expression

```js
toBoolean(coalesce({view.custom.hasBleed}, true))
```


- `props.style.display`: expression

```js
if(toBoolean(coalesce({view.custom.hasBleed}, true)), '', 'none')
```


**`root/Canvas/Pid/Suction SV`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + "/Valves/Suction SV")
```


**`root/Canvas/Pid/Hot Gas SV`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + "/Valves/Hot Gas SV")
```


**`root/Canvas/Pid/Liquid SV`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = "", "", {view.params.tagPath} + "/Valves/Liquid SV")
```


**`root/Canvas/HistoryCard`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

**`root/Canvas/ControlPanel`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../common-patterns.md#pattern-5).

</details>

## Event Scripts And Handlers

- **`root/Canvas/BackToOverview`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.navigate('/')
```

- **`root/Canvas/PrevCg`** `component.onActionPerformed`, script action, scope `G`

```python
# Cycle the CG pages in Utility Overview order (wraps around)
order = [str(c).upper() for c in (self.view.custom.cgOrder or [])]
cur = str(self.view.params.label or '').upper()
if cur not in order:
    return
nxt = order[(order.index(cur) + -1) % len(order)]
system.perspective.navigate('/' + nxt.lower())
```

- **`root/Canvas/NextCg`** `component.onActionPerformed`, script action, scope `G`

```python
# Cycle the CG pages in Utility Overview order (wraps around)
order = [str(c).upper() for c in (self.view.custom.cgOrder or [])]
cur = str(self.view.params.label or '').upper()
if cur not in order:
    return
nxt = order[(order.index(cur) + 1) % len(order)]
system.perspective.navigate('/' + nxt.lower())
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Scale.cssTransform](../../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Embeds** (5): [00\_Pages/Groveport/\_Shared/CG/AhuEvapHistory](./ahuevaphistory.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](./ahuevappanel.md), [02\_Components/01\_Devices/EvapCoilSerpentine](../../../../02-components/01-devices/evapcoilserpentine.md), [02\_Components/01\_Devices/Evaporator](../../../../02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/SolenoidValve](../../../../02-components/01-devices/solenoidvalve.md)

**Embedded in** (19): [00\_Pages/Groveport/Club/Utility/CG-C1](../../club/utility/cg-c1.md), [00\_Pages/Groveport/Dock/Utility/CG-G1](../../dock/utility/cg-g1.md), [00\_Pages/Groveport/Dock/Utility/CG-G2](../../dock/utility/cg-g2.md), [00\_Pages/Groveport/Dock/Utility/CG-G3](../../dock/utility/cg-g3.md), [00\_Pages/Groveport/Dock/Utility/CG-G4](../../dock/utility/cg-g4.md), [00\_Pages/Groveport/Dock/Utility/CG-G5](../../dock/utility/cg-g5.md), [00\_Pages/Groveport/East PH/Utility/CG-E1](../../east-ph/utility/cg-e1.md), [00\_Pages/Groveport/East PH/Utility/CG-E2](../../east-ph/utility/cg-e2.md), [00\_Pages/Groveport/East PH/Utility/CG-E3](../../east-ph/utility/cg-e3.md), [00\_Pages/Groveport/East PH/Utility/CG-E4](../../east-ph/utility/cg-e4.md), [00\_Pages/Groveport/Freezer/Utility/CG-A1](../../freezer/utility/cg-a1.md), [00\_Pages/Groveport/Freezer/Utility/CG-A2](../../freezer/utility/cg-a2.md), [00\_Pages/Groveport/Palletizing/Utility/CG-D1](../../palletizing/utility/cg-d1.md), [00\_Pages/Groveport/SuperChill/Utility/CG-B1](../../superchill/utility/cg-b1.md), [00\_Pages/Groveport/SuperChill/Utility/CG-B2](../../superchill/utility/cg-b2.md), [00\_Pages/Groveport/West PH/Utility/CG-F1](../../west-ph/utility/cg-f1.md), [00\_Pages/Groveport/West PH/Utility/CG-F2](../../west-ph/utility/cg-f2.md), [00\_Pages/Groveport/West PH/Utility/CG-F3](../../west-ph/utility/cg-f3.md), [00\_Pages/Groveport/West PH/Utility/CG-F4](../../west-ph/utility/cg-f4.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 6 | style class |
| `bg-page` | 1 | style class |
| `cg-nav-arrow` | 2 | stylesheet |
| `cg-nav-btn` | 3 | stylesheet |
| `faceplate-cmd-btn` | 3 | style class |
| `fs-13` | 3 | style class |
| `fs-18` | 3 | style class |
| `fw-700` | 6 | style class |

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/CG/Cfg_HasBleedValve`, `/Valves/Bleed SV`, `/Valves/Hot Gas SV`, `/Valves/Liquid SV`, `/Valves/Suction SV`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
