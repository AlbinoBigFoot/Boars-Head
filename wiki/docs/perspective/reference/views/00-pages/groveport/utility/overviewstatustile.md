---
title: "OverviewStatusTile"
sidebar_label: "OverviewStatusTile"
description: "Perspective view 00_Pages/Groveport/Utility/OverviewStatusTile (Page piece (not routed)): 3 components, 14 bindings, 2 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Utility/OverviewStatusTile", "OverviewStatusTile"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Utility/OverviewStatusTile`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Utility/OverviewStatusTile` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Utility/OverviewStatusTile/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Utility &gt; OverviewStatusTile |
| Root | `ia.container.flex`, height 44, width 156 |
| Size | 3 components, 14 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-21T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | input |
| `tagPath` | `""` | input |
| `diPath` | `""` | input |
| `alarmText` | `"ALARM"` | input |
| `okValue` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `quality` | `"Bad_NotFound"` | bound (expr) |
| `value` | `false` | bound (expr) |
| `okText` | `"OK"` | bound (expr) |
| `alarmText` | `"ALARM"` | bound (expr) |
| `pax` | `""` | bound (expr) |
| `paxRoot` | `""` | bound (expr) |
| `valuePath` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1.

```text
root  ia.container.flex  [3 bindings; 1 event]
  Label  ia.display.label  [1 binding]
  Status  ia.display.label  [3 bindings; 1 event]
```

## Bindings

14 bindings: expr 13, property 1.

<details>
<summary>All 14 bindings, grouped by component</summary>

**`(view)`**

- `custom.okText`: expression

```js
if(coalesce(try(isGood(tag({view.custom.paxRoot} + '/Cfg_0StText')), false), false), if({view.params.diPath} = '',
	'OK',
	coalesce(try(toStr(tag({view.custom.paxRoot} + '/Cfg_0StText')), ''), 'OK')), null)
```


- `custom.alarmText`: expression

```js
if(coalesce(try(isGood(tag({view.custom.paxRoot} + '/Cfg_1StText')), false), false), if({view.params.diPath} = '',
	{view.params.alarmText},
	coalesce(try(toStr(tag({view.custom.paxRoot} + '/Cfg_1StText')), ''), {view.params.alarmText})), null)
```


- `custom.quality`: expression

```js
if({view.params.tagPath} = '',
	'Bad_NotFound',
	qualityOf(tag({view.custom.valuePath})))
```


- `custom.value`: expression

```js
if({view.params.tagPath} = '' || left({view.custom.quality}, 4) != 'Good',
	false,
	coalesce(tag({view.custom.valuePath}), false))
```


- `custom.pax`: expression

```js
if(if(coalesce({view.params.diPath}, '') = '', '', case(toStr(coalesce(try(tag({view.params.diPath} + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.params.diPath} + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.params.diPath} + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.params.diPath} + '/DIn.Enabled')), false), false), 'DIn', ''), '')) = 'DIn', 'DIn', if(coalesce({view.params.diPath}, '') != '' && case(substring({view.params.diPath}, lastIndexOf({view.params.diPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', '') != '' && case(toStr(coalesce(try(tag(left({view.params.diPath}, lastIndexOf({view.params.diPath}, '/')) + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag(left({view.params.diPath}, lastIndexOf({view.params.diPath}, '/')) + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag(left({view.params.diPath}, lastIndexOf({view.params.diPath}, '/')) + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag(left({view.params.diPath}, lastIndexOf({view.params.diPath}, '/')) + '/DIn.Enabled')), false), false), 'DIn', ''), '') = 'Tank', 'DIn', ''))
```


- `custom.paxRoot`: expression

```js
if(if(coalesce({view.params.diPath}, '') = '', '', case(toStr(coalesce(try(tag({view.params.diPath} + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.params.diPath} + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.params.diPath} + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.params.diPath} + '/DIn.Enabled')), false), false), 'DIn', ''), '')) = 'DIn', {view.params.diPath} + '/DIn', if(coalesce({view.params.diPath}, '') = '' || case(substring({view.params.diPath}, lastIndexOf({view.params.diPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', '') = '', '', left({view.params.diPath}, lastIndexOf({view.params.diPath}, '/')) + '/' + case(substring({view.params.diPath}, lastIndexOf({view.params.diPath}, '/') + 1), 'DI_HLCO', 'HlcoDIn', 'DI_HiLevel', 'HiHiDIn', 'DI_OPL', 'OplDIn', 'DI_LoLo', 'LoLoDIn', '')))
```


- `custom.valuePath`: expression

```js
{view.custom.paxRoot} + '/Sts'
```


**`root`**

- `props.style.classes`: expression

```js
'container-card' + if(coalesce({session.custom.CanOpenFaceplates}, false) && (len(coalesce({view.params.diPath}, '')) > 0), ' faceplate-hover', '')
```


- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Label`**

- `props.text`: property `view.params.label`

**`root/Status`**

- `props.text`: expression

```js
if({view.params.tagPath} = '',
	{view.custom.okText},
if(left({view.custom.quality}, 4) != 'Good',
	'—',
if({view.custom.value} = {view.params.okValue},
	{view.custom.okText},
	{view.custom.alarmText})))
```


- `props.style.backgroundColor`: expression

```js
if({view.params.tagPath} = '' || left({view.custom.quality}, 4) != 'Good',
	'var(--neutral-40)',
if({view.custom.value} = {view.params.okValue},
	'var(--neutral-40)',
	'var(--neutral-90)'))
```


- `props.style.color`: expression

```js
if({view.params.tagPath} != '' && left({view.custom.quality}, 4) = 'Good' && {view.custom.value} != {view.params.okValue},
	'var(--neutral-10)',
	'var(--neutral-90)')
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
p = str(self.view.params.diPath or '')
if not p:
    return
title = str(system.tag.readBlocking([str(self.view.custom.paxRoot) + '/Cfg_Label'])[0].value or self.view.params.label or '')
Navigation.Faceplate.openFaceplate('din-fp-%s' % p, p, '01_Popups/00_Faceplates/DiscreteInput', False, title, 600, 600, {'title': title})
```

- **`root/Status`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.valuePath}')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/DiscreteInput](../../../01-popups/00-faceplates/discreteinput.md)

**Embedded in** (5): [00\_Pages/Groveport/Condensers/Utility/Overview](../condensers/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../machine-room/utility/overview.md), [00\_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview](../machine-room/utility/rupturedisks/overview.md), [00\_Pages/Groveport/Utility/OverviewStatuses](./overviewstatuses.md), [01\_Popups/00\_Faceplates/\_Assets/TankOverview/Overview](../../../01-popups/00-faceplates/assets/tankoverview/overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `fs-10` | 1 | style class |
| `fs-12` | 1 | style class |
| `fw-700` | 2 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_0StText`, `/Cfg_1StText`, `/Cfg_Label`, `/DIn`, `/DIn.Enabled`, `/Sts`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
