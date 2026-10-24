---
title: "Pump"
sidebar_label: "Pump"
description: "Perspective view 02_Components/01_Devices/Pump (Reusable component): 12 components, 32 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/01_Devices/Pump", "Pump"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/Pump`.

| | |
|---|---|
| View path | `02_Components/01_Devices/Pump` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Pump/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; Pump |
| Root | `ia.container.flex`, height 136, width 96 |
| Size | 12 components, 32 bindings, 1 event handlers, 0 change scripts, 3 message handlers |
| Last saved | 2026-09-30T03:15:07Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `analog` | `true` | input |
| `faceplate` | `null` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `alarm` | `{"active": false, "priority": 10, "unack": false}` | |
| `label` | `""` | bound (expr) |
| `metadata` | `""` | bound (expr) |
| `oos` | `false` | bound (expr) |
| `values` | `{}` | |
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.view x4, ia.container.flex x2, ia.container.coord x2, ia.shapes.svg x2, ia.display.label x1, ia.display.icon x1.

```text
root  ia.container.flex  [3 bindings; 1 event]
  IconHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/IconHeader]
  LabelHeader  ia.container.flex
    DeviceLabel  ia.display.label  [1 binding]
    FaceplateIcon  ia.display.icon  [2 bindings]
  Graphic  ia.container.coord  [1 binding]
    Housing  ia.shapes.svg
    Impeller  ia.shapes.svg  [1 binding]
    AlarmFrame  ia.container.coord  [2 bindings]
    AlarmHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/AlarmHeader]
  AnalogValue  ia.display.view  [4 bindings; view: 03_Elements/01_Status/AnalogValue]
  Status  ia.display.view  [3 bindings; view: 03_Elements/01_Status/StatusIndicator]
```

## Bindings

32 bindings: expr 23, property 5, tag 3, expr-struct 1.

<details>
<summary>All 32 bindings, grouped by component</summary>

**`(view)`**

- `custom.alarm.active`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}/_Alarms/_Active`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	False,
	if(typeof({value}) = 'java.lang.Boolean',
		{value},
		{value} = True || {value} = 1 || {value} = 'true' || {value} = 'True'))
```


- `custom.alarm.priority`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}/_Alarms/_ActiveHighPriority`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	10,
	{value})
```


- `custom.alarm.unack`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}/_Alarms/_Unack`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	False,
	if(typeof({value}) = 'java.lang.Boolean',
		{value},
		{value} = True || {value} = 1 || {value} = 'true' || {value} = 'True'))
```


- `custom.label`: expression

```js
try(
    if(
        isNull({view.custom.metadata.shortDescription}) ||
        {view.custom.metadata.shortDescription} = '',
        if({view.params.tagPath} = '',
           '',
           subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)),
        {view.custom.metadata.shortDescription}
    ),
'')
```


- `custom.metadata`: expression

```js
if(
	{view.params.tagPath}!='' && isGood(tag({view.params.tagPath} + '.Metadata')),
	tag({view.params.tagPath} + '.Metadata'),
	'')
```


- `custom.oos`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
```


- `custom.values.analog`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/RunTime/Val_TotRunHrs')
```


- `custom.values.commLoss`: expression

```js
if(coalesce({view.custom.oos}, false),
	false,
	(if({view.params.tagPath} = '',
	false,
	!isGood(tag({view.params.tagPath} + '/Motor/Val_Sts')))))
```


- `custom.values.running`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/Motor/Val_Sts')),
	false,
	tag({view.params.tagPath} + '/Motor/Val_Sts') = 2 || tag({view.params.tagPath} + '/Motor/Val_Sts') = 8)
```


- `custom.values.status`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/Motor/Val_Sts')
```


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

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


- `props.style.classes`: expression

```js
('device-vertical')
```


**`root/IconHeader`**

- `props.params.statusPath`: property `view.custom.values.status`

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/LabelHeader/DeviceLabel`**

- `props.text`: property `view.custom.label`

**`root/LabelHeader/FaceplateIcon`**

- `props.style.opacity`: expression

```js
if(isNull({view.params.faceplate}),
   0,
   1)
```


- `meta.visible`: expression

```js
coalesce({session.custom.CanOpenFaceplates}, false)
```


**`root/Graphic`**

- `props.style.classes`: expression

```js
((if(coalesce({view.custom.values.commLoss}, false),
	'device-graphic device-comm-loss component',
	'device-graphic component')) + if(coalesce({view.custom.oos}, false), ' device-oos', '')) + if(coalesce({session.custom.CanOpenFaceplates}, false) && (len(trim(coalesce({view.params.faceplate}, ''))) > 0), ' faceplate-hover', '')
```


**`root/Graphic/Impeller`**

- `props.style.classes`: expression, then script transform

```js
{view.custom.values.running}
```

Transform 1, script:

```python
return 'fan-spin' if value in (True, 1, '1', 'true', 'True') else ''
```


**`root/Graphic/AlarmFrame`**

- `meta.visible`: expression

```js
coalesce({view.custom.alarm.active}, false)
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.values.commLoss}, false),
	'',
	if(coalesce({view.custom.alarm.active}, false),
		'alarm-frame alarm-border alarm-priority-' +
			case(coalesce({view.custom.alarm.priority}, 10),
				4, 'critical',
				3, 'high',
				2, 'medium',
				1, 'low',
				'low'),
		'alarm-frame'))
```


**`root/Graphic/AlarmHeader`**

- `meta.visible`: expression

```js
{view.custom.alarm.active}
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/AnalogValue`**

- `meta.visible`: expression

```js
coalesce({view.params.analog}, true)
```


- `props.params.tagPath`: expression

```js
{view.custom.values.analog}
```


- `props.style.classes`: expression

```js
if(coalesce({view.params.analog}, true),
	'value',
	'')
```


- `props.style.visibility`: expression

```js
if(coalesce({view.custom.oos}, false), 'hidden', 'visible')
```


**`root/Status`**

- `props.params.outOfService`: property `view.custom.oos`

- `props.params.tagPath`: expression

```js
{view.custom.values.status}
```


- `props.style.classes`: expression

```js
if(coalesce({view.params.analog}, true),
	'status',
	'value')
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
faceplate = self.view.params.faceplate
if faceplate is None or str(faceplate).strip() == '':
    return
tagPath = str(self.view.params.tagPath or '')
title = str(self.view.custom.label or '')
if title in (None, '', 'nn'):
    title = tagPath.split('/')[-1] if tagPath else self.view.name
# Shell + typed Controls. Prefer shared.Alerts.showFaceplate (comp-fp id).
shared.Alerts.showFaceplate(
    tagPath=tagPath,
    deviceType='Pump',
    title=title,
    webGuiUrl='',
    showControls=True,
    showConfiguration=True,
    showInterlocks=True,
    showTrend=True,
    showAlarmConfiguration=True,
    showAlarms=True,
    width=560,
    height=640
)
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

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.showFaceplate](../../../../../scripting/reference/modules/shared-alerts.md), [shared.OutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openDialog](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openHistory](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.setOutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.Security.allowed](../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Embeds** (4): [03\_Elements/01\_Status/AlarmHeader](../../03-elements/01-status/alarmheader.md), [03\_Elements/01\_Status/AnalogValue](../../03-elements/01-status/analogvalue.md), [03\_Elements/01\_Status/IconHeader](../../03-elements/01-status/iconheader.md), [03\_Elements/01\_Status/StatusIndicator](../../03-elements/01-status/statusindicator.md)

**Embedded in** (6): [00\_Pages/Boars Head/Devices/DesignOverview](../../00-pages/boars-head/devices/designoverview.md), [00\_Pages/Boars Head/Machine Room/Overview](../../00-pages/boars-head/machine-room/overview.md), [00\_Pages/Boars Head/Pumps/Design](../../00-pages/boars-head/pumps/design.md), [00\_Pages/Groveport/Condensers/Utility/Overview](../../00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Pumps/Design](../../00-pages/groveport/condensers/utility/pumps/design.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../../00-pages/groveport/machine-room/utility/overview.md)

## Style Classes

<details>
<summary>15 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `alarm-header` | 1 | stylesheet |
| `fs-11` | 1 | style class |
| `fw-700` | 1 | style class |
| `icon-header` | 1 | style class |
| `label` | 1 | stylesheet |
| `alarm-border` | bound | stylesheet |
| `alarm-frame` | bound | stylesheet |
| `component` | bound | stylesheet |
| `device-comm-loss` | bound | stylesheet |
| `device-graphic` | bound | stylesheet |
| `device-oos` | bound | stylesheet |
| `fan-spin` | bound | stylesheet |
| `status` | bound | stylesheet |
| `value` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}/_Alarms/_Active`
- `{tagPath}/_Alarms/_ActiveHighPriority`
- `{tagPath}/_Alarms/_Unack`

Member paths appended to a base path in expressions (relative):

`.Enabled`, `.Metadata`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Motor/Val_Sts`, `/RunTime/Val_TotRunHrs`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
