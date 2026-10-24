---
title: "InterlockButton"
sidebar_label: "InterlockButton"
description: "Perspective view 02_Components/00_Controls/InterlockButton (Reusable component): 2 components, 7 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/00_Controls/InterlockButton", "InterlockButton"]
---

:::note

:::


**Reusable component**: `02_Components/00_Controls/InterlockButton`.

| | |
|---|---|
| View path | `02_Components/00_Controls/InterlockButton` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/00_Controls/InterlockButton/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 00\_Controls &gt; InterlockButton |
| Root | `ia.container.flex`, height 28, width 120 |
| Size | 2 components, 7 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-25T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `title` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `paxRoot` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.input.button x1.

```text
root  ia.container.flex  [2 bindings]
  Btn  ia.input.button  [3 bindings; 1 event]
```

## Bindings

7 bindings: expr 7.

**`(view)`**

- `custom.pax`: expression

```js
if(right(coalesce({view.params.tagPath}, ''), 10) = '/Interlock', case(toStr(coalesce(try(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag(left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/DIn.Enabled')), false), false), 'DIn', ''), ''), '')
```


- `custom.paxRoot`: expression

```js
if(right(coalesce({view.params.tagPath}, ''), 10) = '/Interlock', left({view.params.tagPath}, len({view.params.tagPath}) - 10) + '/Intlk', '')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/Btn`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && !coalesce(try(isGood(tag({view.custom.paxRoot} + '/Sts_IntlkOK')), false), false), 'COMM LOSS', if({view.params.tagPath} = '', 'Interlocks', if(coalesce(try(if(!isGood(tag({view.custom.paxRoot} + '/Sts_IntlkOK')), null, tag({view.custom.paxRoot} + '/Sts_IntlkOK')), null), false), 'Interlocks OK', 'Interlocked')))
```


- `props.style.backgroundColor`: expression

```js
if({view.params.tagPath} != '' && !coalesce(try(isGood(tag({view.custom.paxRoot} + '/Sts_IntlkOK')), false), false), 'var(--neutral-30)', if({view.params.tagPath} = '' || try(!isGood(tag({view.custom.paxRoot} + '/Sts_IntlkOK')), true), 'var(--status-off)', if(coalesce(try(if(!isGood(tag({view.custom.paxRoot} + '/Sts_IntlkOK')), null, tag({view.custom.paxRoot} + '/Sts_IntlkOK')), null), false), '#2E7D32', 'var(--status-level-critical)')))
```


- `props.enabled`: expression

```js
!({view.params.tagPath} = '')
```


## Event Scripts And Handlers

- **`root/Btn`** `component.onActionPerformed`, script action, scope `G`

```python
tp = str(self.view.params.tagPath or '')
if not tp:
    return
title = str(self.view.params.title or '').strip()
if not title:
    parts = tp.split('/')
    title = parts[-2] if len(parts) > 1 else parts[-1]
Navigation.Faceplate.openFaceplate('intlk-fp-%s' % tp, tp, '01_Popups/00_Faceplates/Interlock', False, title, 560, 680, {'title': title})
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/Interlock](../../01-popups/00-faceplates/interlock.md)

**Embedded in** (1): [00\_Pages/Groveport/\_Shared/CG/AhuEvapPanel](../../00-pages/groveport/shared/cg/ahuevappanel.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Intlk`, `/Sts_IntlkOK`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
