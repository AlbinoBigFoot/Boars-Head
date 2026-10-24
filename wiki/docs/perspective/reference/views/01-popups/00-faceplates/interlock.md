---
title: "Interlock"
sidebar_label: "Interlock"
description: "Perspective view 01_Popups/00_Faceplates/Interlock (Popup / faceplate): 5 components, 6 bindings, 1 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Interlock", "Interlock"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Interlock`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Interlock` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Interlock/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Interlock |
| Root | `ia.container.flex`, height 680, width 560 |
| Size | 5 components, 6 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-25T00:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `popupId` | `""` | input |
| `tagPath` | `""` | input |
| `title` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `pax` | `""` | bound (expr) |
| `paxRoot` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x1, ia.display.icon x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Header  ia.container.flex
    Title  ia.display.label  [1 binding]
    Close  ia.display.icon  [1 event]
  Panel  ia.display.view  [1 binding; view: 01_Popups/00_Faceplates/_Assets/InterlockPanel]
```

## Bindings

6 bindings: expr 5, property 1.

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

**`root/Header/Title`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.custom.paxRoot} + '/Cfg_Tag')), false), false) || coalesce(try(isGood(tag({view.custom.paxRoot} + '/Cfg_Desc')), false), false)), if(coalesce(try(toStr(tag({view.custom.paxRoot} + '/Cfg_Tag')), ''), '') != '', coalesce(try(toStr(tag({view.custom.paxRoot} + '/Cfg_Tag')), ''), ''), coalesce({view.params.title}, '')) + if(coalesce(try(toStr(tag({view.custom.paxRoot} + '/Cfg_Desc')), ''), '') != '', ' - ' + coalesce(try(toStr(tag({view.custom.paxRoot} + '/Cfg_Desc')), ''), ''), ''), '—')
```


**`root/Panel`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

## Event Scripts And Handlers

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
pid = str(self.view.params.popupId or '').strip()
if pid:
    system.perspective.closePopup(pid)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (1): [01\_Popups/00\_Faceplates/\_Assets/InterlockPanel](./assets/interlockpanel.md)

**Opened or named by** (1): [02\_Components/00\_Controls/InterlockButton](../../02-components/00-controls/interlockbutton.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Title` | 1 | style class |
| `bg-component` | 1 | stylesheet |
| `bg-header` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `container-icon` | 1 | stylesheet |
| `faceplate` | 1 | stylesheet |
| `faceplate-close` | 1 | stylesheet |
| `faceplate-header` | 1 | stylesheet |
| `faceplate-tabs-vertical` | 1 | stylesheet |
| `faceplate-title` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/Cfg_Desc`, `/Cfg_Tag`, `/DIn.Enabled`, `/Intlk`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
