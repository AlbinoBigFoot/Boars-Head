---
title: "Safetys"
sidebar_label: "Safetys"
description: "Perspective view 02_Components/02_Widgets/Safetys (Reusable component): 15 components, 13 bindings, 3 event scripts."
generated: true
keywords: ["02_Components/02_Widgets/Safetys", "Safetys"]
---

:::note

:::


**Reusable component**: `02_Components/02_Widgets/Safetys`.

| | |
|---|---|
| View path | `02_Components/02_Widgets/Safetys` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/02_Widgets/Safetys/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 02\_Widgets &gt; Safetys |
| Root | `ia.container.flex`, height 393, width 233 |
| Size | 15 components, 13 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-07-30T06:43:30Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `brEfTagPath` | `""` | input |
| `fireTagPath` | `""` | input |
| `mrAdTagPath` | `""` | input |
| `mrEfTagPath` | `""` | input |
| `rdisksTagPath` | `""` | input |
| `title` | `"SAFETYS"` | input |
| `vlAdTagPath` | `""` | input |
| `resetTagPath` | `""` | input |
| `silenceTagPath` | `""` | input |
| `lightTagPath` | `""` | input |
| `circuitTagPath` | `""` | input |

## Component Tree

Component types: ia.container.flex x6, ia.display.view x6, ia.input.button x2, ia.display.label x1.

<details>
<summary>Component tree (15 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  TopRow  ia.container.flex
    Title  ia.display.label  [1 binding]
    AlarmButtons  ia.container.flex
      Reset  ia.input.button  [2 bindings; 1 event]
      Silence  ia.input.button  [2 bindings; 1 event]
  Body  ia.container.flex
    Indicators  ia.container.flex
      MrAd  ia.display.view  [1 binding; view: 03_Elements/01_Status/StatusDot]
      VlAd  ia.display.view  [1 binding; view: 03_Elements/01_Status/StatusDot]
      Rdisks  ia.display.view  [1 binding; 1 event; view: 03_Elements/01_Status/StatusDot]
      Fire  ia.display.view  [1 binding; view: 03_Elements/01_Status/StatusDot]
    Fans  ia.container.flex
      MrEf  ia.display.view  [1 binding; view: 02_Components/01_Devices/ExhaustFan]
      BrEf  ia.display.view  [1 binding; view: 02_Components/01_Devices/ExhaustFan]
```

</details>

## Bindings

13 bindings: property 7, expr 6.

<details>
<summary>All 13 bindings, grouped by component</summary>

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/TopRow/Title`**

- `props.text`: property `view.params.title`

**`root/TopRow/AlarmButtons/Reset`**

- `props.enabled`: expression

```js
{view.params.resetTagPath} != '' && !coalesce({session.custom.ReadOnly}, false) && coalesce({session.custom.Permissions.AlarmSummary.Acknowledge}, false)
```


- `props.style.visibility`: expression

```js
if(coalesce(try(isGood(tag({view.params.lightTagPath})), false), false), if({view.params.lightTagPath} != '' && coalesce(try(toBoolean(tag({view.params.lightTagPath})), false), false), 'visible', 'hidden'), 'hidden')
```


**`root/TopRow/AlarmButtons/Silence`**

- `props.enabled`: expression

```js
{view.params.silenceTagPath} != '' && !coalesce({session.custom.ReadOnly}, false) && coalesce({session.custom.Permissions.AlarmSummary.Acknowledge}, false)
```


- `props.style.visibility`: expression

```js
if(coalesce(try(isGood(tag({view.params.circuitTagPath})), false), false), if({view.params.circuitTagPath} != '' && coalesce(try(toBoolean(tag({view.params.circuitTagPath})), false), false), 'visible', 'hidden'), 'hidden')
```


**`root/Body/Indicators/MrAd`**

- `props.params.tagPath`: property `view.params.mrAdTagPath`

**`root/Body/Indicators/VlAd`**

- `props.params.tagPath`: property `view.params.vlAdTagPath`

**`root/Body/Indicators/Rdisks`**

- `props.params.tagPath`: property `view.params.rdisksTagPath`

**`root/Body/Indicators/Fire`**

- `props.params.tagPath`: property `view.params.fireTagPath`

**`root/Body/Fans/MrEf`**

- `props.params.tagPath`: property `view.params.mrEfTagPath`

**`root/Body/Fans/BrEf`**

- `props.params.tagPath`: property `view.params.brEfTagPath`

</details>

## Event Scripts And Handlers

- **`root/TopRow/AlarmButtons/Reset`** `component.onActionPerformed`, script action, scope `G`

```python
tp = str(self.view.params.resetTagPath or '')
if not tp or self.session.custom.ReadOnly:
    return
if not shared.PlcWriteLock.writeAllowed(tp, 'Machine Room Alarm Reset'):
    shared.Alerts.showAlert(state='warning', title='PLC Writes Locked', message='This command goes to the RCP1 controller (production PLC) and PLC writes are locked.', showCloseBtn=True, overlayDismiss=True)
    return
shared.Audit.writeTag(tp, True, 'Machine Room Alarm Reset', self.view.id.split('@')[0])
```

- **`root/TopRow/AlarmButtons/Silence`** `component.onActionPerformed`, script action, scope `G`

```python
tp = str(self.view.params.silenceTagPath or '')
if not tp or self.session.custom.ReadOnly:
    return
if not shared.PlcWriteLock.writeAllowed(tp, 'Machine Room Alarm Silence'):
    shared.Alerts.showAlert(state='warning', title='PLC Writes Locked', message='This command goes to the RCP1 controller (production PLC) and PLC writes are locked.', showCloseBtn=True, overlayDismiss=True)
    return
shared.Audit.writeTag(tp, True, 'Machine Room Alarm Silence', self.view.id.split('@')[0])
```

- **`root/Body/Indicators/Rdisks`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/rupture-disks')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.PlcWriteLock.writeAllowed](../../../../../scripting/reference/modules/shared-plcwritelock.md).

## Related Views

**Embeds** (2): [02\_Components/01\_Devices/ExhaustFan](../01-devices/exhaustfan.md), [03\_Elements/01\_Status/StatusDot](../../03-elements/01-status/statusdot.md)

**Embedded in** (2): [00\_Pages/Boars Head/Machine Room/Overview](../../00-pages/boars-head/machine-room/overview.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../../00-pages/groveport/machine-room/utility/overview.md)

## Style Classes

<details>
<summary>14 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `faceplate-cmd-btn` | 2 | style class |
| `faceplate-hover` | 1 | stylesheet |
| `fs-12` | 1 | style class |
| `fw-700` | 1 | style class |
| `safetys-alarm-btn` | 2 | stylesheet |
| `safetys-body` | 1 | stylesheet |
| `safetys-embed` | 6 | stylesheet |
| `safetys-fan` | 2 | stylesheet |
| `safetys-fans` | 1 | no rule found |
| `safetys-indicators` | 1 | stylesheet |
| `safetys-reset` | 1 | stylesheet |
| `safetys-title` | 1 | stylesheet |
| `safetys-widget` | 1 | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
