---
title: "LTU"
sidebar_label: "LTU"
description: "Perspective view 02_Components/01_Devices/LTU (Reusable component): 12 components, 17 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/01_Devices/LTU", "LTU"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/LTU`.

| | |
|---|---|
| View path | `02_Components/01_Devices/LTU` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/LTU/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; LTU |
| Root | `ia.container.flex`, height 126, width 227 |
| Size | 12 components, 17 bindings, 1 event handlers, 0 change scripts, 3 message handlers |
| Last saved | 2026-07-24T18:04:58Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `oos` | `false` | bound (expr) |
| `pax` | `""` | bound (expr) |
| `permDevice` | `""` | bound (expr) |
| `roCommand` | `true` | bound (expr) |
| `tipCommand` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x6, ia.display.label x4, ia.display.view x1, ia.input.button x1.

```text
root  ia.container.flex  [3 bindings]
  Header  ia.container.flex
    Title  ia.display.label
  CountRow  ia.container.flex
    CountLabel  ia.display.label
    CountSlot  ia.container.flex
      Count  ia.display.label  [3 bindings]
  SetpointRow  ia.container.flex
    SPLabel  ia.display.label
    AlarmSP  ia.display.view  [4 bindings; view: 03_Elements/00_Control/AnalogInput]
  ResetRow  ia.container.flex
    ResetCount  ia.input.button  [2 bindings; 1 event]
```

## Bindings

17 bindings: expr 16, expr-struct 1.

<details>
<summary>All 17 bindings, grouped by component</summary>

**`(view)`**

- `custom.oos`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
```


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../common-patterns.md#pattern-6).

- `custom.permDevice`: expression. Common pattern, see [pattern-8](../../../common-patterns.md#pattern-8).

- `custom.roCommand`: expression

```js
coalesce({session.custom.ReadOnly}, true) || !coalesce(try({session.custom.Permissions}[{view.custom.permDevice}]['Command'], null), true)
```


- `custom.tipCommand`: expression

```js
if(!coalesce({session.custom.ReadOnly}, true) && coalesce({view.custom.roCommand}, false), 'Not Permitted: ' + {view.custom.permDevice} + ' / ' + 'Command' + ' (Roles & Permissions)', '')
```


**`root`**

- `props.style.classes`: expression

```js
(if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/_Alarms/_Active')), false), false), 'safetys-widget alarm-border alarm-priority-' + case(coalesce(try(toInt(tag({view.params.tagPath} + '/_Alarms/_ActiveHighPriority')), 0), 0), 4, 'critical', 3, 'high', 2, 'medium', 1, 'low', 'low'), 'safetys-widget')) + if(coalesce({view.custom.oos}, false), ' device-oos', '')
```


- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
ticket: coalesce({session.custom.TicketLogAccess}, false)
admin: coalesce({session.custom.Permissions.OutOfService.Set}, false)
history: coalesce({session.custom.Permissions.OutOfService.View}, false)
oos: coalesce({view.custom.oos}, false)
```

waitOnAll: `False`

Transform 1, script:

```python
tagPath = ''
try:
    tagPath = str(self.view.params.tagPath or '')
except:
    pass
view_name = self.view.id.split('@')[0]
def item(text, icon, msg_type, payload, scope):
    return {
        "text": text,
        "icon": {"path": icon, "color": "--neutral-80", "style": {}},
        "style": {"classes": "bg-component Fonts/Value", "height": 24, "width": 170},
        "type": "message",
        "children": [],
        "link": {"url": "", "target": "self"},
        "method": {"name": "", "params": {}},
        "message": {"type": msg_type, "payload": payload, "scope": scope}
    }
items = []
if value['ticket']:
    logged = tagPath if tagPath.strip() else 'No TagPath: ' + view_name.split('/')[-1]
    items.append(item('Ticket Logger', 'material/info', 'ticketLog',
        {'tagPath': logged, 'viewName': view_name, 'sender': self.view.id}, 'page'))
if value['admin'] and tagPath.strip():
    if value['oos']:
        items.append(item('Return To Service', 'material/info', 'oosToggle', {'tagPath': tagPath, 'sender': self.view.id}, 'page'))
    else:
        items.append(item('Take Out Of Service', 'material/info', 'oosToggle',
            {'tagPath': tagPath, 'sender': self.view.id}, 'page'))
if value['history'] and tagPath.strip():
    items.append(item('Out Of Service History', 'material/info', 'oosHistory',
        {'tagPath': tagPath, 'sender': self.view.id}, 'page'))
return items
```


- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/CountRow/CountSlot/Count`**

- `props.text`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), '—', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), '—', numberFormat(coalesce(try(toFloat(tag({view.params.tagPath} + '/PlcCount')), 0), 0), '#,##0'))))))))
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/PlcCountAlarm')), false), false), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/PlcCountAlarm')), false), false), 'var(--status-level-critical)', 'var(--text)'), 'var(--neutral-60)')
```


- `props.style.classes`: expression

```js
if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), 'Fonts/Value value-bad', if({view.params.tagPath} != '' && coalesce(try(!isGood(tag({view.params.tagPath} + '/PlcCount')), true), true), 'Fonts/Value fs-16 fw-700 value-bad', 'Fonts/Value fs-16 fw-700')))))))
```


**`root/SetpointRow/AlarmSP`**

- `props.params.tagPath`: expression

```js
if({view.params.tagPath} = '', '', {view.params.tagPath} + '/PlcCountAlarmSP')
```


- `props.params.permission`: expression

```js
(!coalesce({view.custom.roCommand}, false)) && coalesce({view.custom.pax}, '') = ''
```


- `meta.tooltip.enabled`: expression

```js
{view.custom.tipCommand} != ''
```


- `meta.tooltip.text`: expression

```js
{view.custom.tipCommand}
```


**`root/ResetRow/ResetCount`**

- `props.enabled`: expression

```js
({view.params.tagPath} != '' && !coalesce({view.custom.roCommand}, false) && coalesce(try(isGood(tag({view.params.tagPath} + '/PlcCount')) && isGood(tag({view.params.tagPath} + '/PlcResetCount')), false), false)) && coalesce({view.custom.pax}, '') = ''
```


- `props.tooltip.text`: expression

```js
if({view.params.tagPath} = '', '', if(coalesce({view.custom.tipCommand}, '') != '', {view.custom.tipCommand}, if(coalesce({view.custom.roCommand}, false), 'Your Role Cannot Operate Equipment', if(!coalesce(try(isGood(tag({view.params.tagPath} + '/PlcCount')) && isGood(tag({view.params.tagPath} + '/PlcResetCount')), false), false), 'PLC Link Lost - Reset Unavailable', 'Reset The NH3 LTU Transfer Count'))))
```

</details>

## Event Scripts And Handlers

- **`root/ResetRow/ResetCount`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.pax:
    return  # pax-bindings: live PLC object, read only
tp = str(self.view.params.tagPath or '')
if not tp or self.view.custom.roCommand:
    return
path = tp + '/PlcResetCount'
# FT setToOne: one click, no confirm. Guards in order: PLC write lock, then permissions (Faceplates/Operate +
# LTU/Command, 'Not Permitted' dialog); shared.Audit.writeTag re-checks both and logs to OpsAudit.
if not shared.PlcWriteLock.writeAllowed(path):
    shared.Alerts.showAlert(state='warning', title='PLC Writes Locked',
        message='This value is in the RCP1 controller (production PLC) and PLC writes are locked.',
        showCloseBtn=True, overlayDismiss=True)
    return
if not shared.Security.requireWrite(path, 'LTU Transfer Count Reset'):
    return
shared.Audit.writeTag(path, True, label='LTU Transfer Count Reset', viewName=self.view.id.split('@')[0])
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

- **`root`** message handler `oosToggle` (scope: page)

```python
# HMI Out Of Service (OutOfService/Set permission) - memo dialog; shared.OutOfService logs + audits the change
# page-scoped: every view on the page hears it - only the view whose menu was clicked acts
sender = payload.get('sender')
if sender and sender != self.view.id:
    return
if not shared.Security.allowed(self.session, 'OutOfService', 'Set'):
    return
tp = str(self.view.params.tagPath or '')
# page-scoped: every component on the page hears it - only the one that was right-clicked acts
if not tp or str(payload.get('tagPath') or '') != tp:
    return
# required memo (+ reason when taking it out): the dialog's Confirm calls shared.OutOfService.setOutOfService
shared.OutOfService.openDialog(tp, self.view.id.split('@')[0])
```

- **`root`** message handler `oosHistory` (scope: page)

```python
# Out Of Service History (OutOfService/View permission) - OOS log page filtered to this device
# page-scoped: every view on the page hears it - only the view whose menu was clicked acts
sender = payload.get('sender')
if sender and sender != self.view.id:
    return
if not shared.Security.allowed(self.session, 'OutOfService', 'View'):
    return
tp = str(self.view.params.tagPath or '')
if not tp or str(payload.get('tagPath') or '') != tp:
    return
shared.OutOfService.openHistory(tp)
```

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Audit.writeTag](../../../../../scripting/reference/modules/shared-audit.md), [shared.OutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openDialog](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openHistory](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.setOutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.PlcWriteLock.writeAllowed](../../../../../scripting/reference/modules/shared-plcwritelock.md), [shared.Security.allowed](../../../../../scripting/reference/modules/shared-security.md), [shared.Security.requireWrite](../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Embeds** (1): [03\_Elements/00\_Control/AnalogInput](../../03-elements/00-control/analoginput.md)

**Embedded in** (1): [00\_Pages/Groveport/Machine Room/Utility/Overview](../../00-pages/groveport/machine-room/utility/overview.md)

## Style Classes

<details>
<summary>13 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 2 | style class |
| `Fonts/Value` | 2 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `fs-13` | 2 | style class |
| `fs-15` | 1 | style class |
| `fs-16` | 1 | style class |
| `fw-600` | 2 | style class |
| `fw-700` | 2 | style class |
| `ltu-sp` | 1 | stylesheet |
| `safetys-title` | 1 | stylesheet |
| `safetys-widget` | 1 | stylesheet |
| `alarm-border` | bound | stylesheet |
| `device-oos` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `[default]_Config/Security/DeviceTypes`

Member paths appended to a base path in expressions (relative):

`.Enabled`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/PlcCount`, `/PlcCountAlarm`, `/PlcCountAlarmSP`, `/PlcResetCount`, `/_Alarms/_Active`, `/_Alarms/_ActiveHighPriority`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
