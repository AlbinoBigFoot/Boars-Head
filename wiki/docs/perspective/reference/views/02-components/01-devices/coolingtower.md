---
title: "CoolingTower"
sidebar_label: "CoolingTower"
description: "Perspective view 02_Components/01_Devices/CoolingTower (Reusable component): 13 components, 27 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/01_Devices/CoolingTower", "CoolingTower"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/CoolingTower`.

| | |
|---|---|
| View path | `02_Components/01_Devices/CoolingTower` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/CoolingTower/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; CoolingTower |
| Root | `ia.container.flex`, height 206, width 100 |
| Size | 13 components, 27 bindings, 1 event handlers, 0 change scripts, 3 message handlers |
| Last saved | 2026-07-24T23:15:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `faceplate` | `null` | input |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | bound (expr) |
| `metadata` | `""` | bound (expr) |
| `values` | `{}` | |
| `alarm` | `{"active": false, "priority": 10, "unack": false}` | |
| `oos` | `false` | bound (expr) |

## Component Tree

Component types: ia.display.view x4, ia.shapes.svg x3, ia.container.flex x2, ia.container.coord x2, ia.display.label x1, ia.display.icon x1.

<details>
<summary>Component tree (13 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  LabelHeader  ia.container.flex
    IconHeader  ia.display.view  [1 binding; view: 03_Elements/01_Status/IconHeader]
    DeviceLabel  ia.display.label  [1 binding]
    FaceplateIcon  ia.display.icon  [2 bindings]
  Graphic  ia.container.coord  [1 binding]
    Housing  ia.shapes.svg
    FanRotor  ia.shapes.svg  [1 binding]
    Spray  ia.shapes.svg  [1 binding]
    AlarmFrame  ia.container.coord  [2 bindings]
    AlarmHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/AlarmHeader]
  AnalogValue  ia.display.view  [2 bindings; view: 03_Elements/01_Status/AnalogValue]
  Status  ia.display.view  [2 bindings; view: 03_Elements/01_Status/StatusIndicator]
```

</details>

## Bindings

27 bindings: expr 19, property 4, tag 3, expr-struct 1.

<details>
<summary>All 27 bindings, grouped by component</summary>

**`(view)`**

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


- `custom.values.status`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/Status/Value')
```


- `custom.values.analog`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/SPD_FBK/Value')
```


- `custom.values.running`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/Status/Value')),
	false,
	tag({view.params.tagPath} + '/Status/Value') = 1)
```


- `custom.values.commLoss`: expression

```js
if(coalesce({view.custom.oos}, false),
	false,
	(if({view.params.tagPath} = '',
	false,
	!isGood(tag({view.params.tagPath} + '/Status/Value')))))
```


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


- `custom.alarm.priority`: tag, then expression transform

Mode `indirect`, tag path `{tagPath}/_Alarms/_ActiveHighPriority`, references `tagPath` = `{view.params.tagPath}`, fallback delay 2.5 s

Transform 1, expression:

```js
if(isNull({value}),
	10,
	{value})
```


- `custom.oos`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
```


**`root`**

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

**`root/LabelHeader/IconHeader`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/LabelHeader/DeviceLabel`**

- `props.text`: property `view.custom.label`

**`root/LabelHeader/FaceplateIcon`**

- `props.style.opacity`: expression

```js
if(isNull({view.params.faceplate}) || {view.params.faceplate} = '',
   0,
   1)
```


- `meta.visible`: expression

```js
coalesce({session.custom.CanOpenFaceplates}, false) && (!(isNull({view.params.faceplate}) || {view.params.faceplate} = ''))
```


**`root/Graphic`**

- `props.style.classes`: expression

```js
((if(coalesce({view.custom.values.commLoss}, false),
	'device-graphic device-comm-loss',
	'device-graphic')) + if(coalesce({view.custom.oos}, false), ' device-oos', '')) + if(coalesce({session.custom.CanOpenFaceplates}, false) && (len(trim(coalesce({view.params.faceplate}, ''))) > 0), ' faceplate-hover', '')
```


**`root/Graphic/FanRotor`**

- `props.style.classes`: expression, then script transform

```js
{view.custom.values.running}
```

Transform 1, script:

```python
return 'ct-fan-side-spin' if value in (True, 1, '1', 'true', 'True') else ''
```


**`root/Graphic/Spray`**

- `props.style.classes`: expression, then script transform

```js
{view.custom.values.running}
```

Transform 1, script:

```python
return 'ct-spray-run' if value in (True, 1, '1', 'true', 'True') else ''
```


**`root/Graphic/AlarmFrame`**

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


- `meta.visible`: expression

```js
coalesce({view.custom.alarm.active}, false)
```


**`root/Graphic/AlarmHeader`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

- `meta.visible`: expression

```js
{view.custom.alarm.active}
```


**`root/AnalogValue`**

- `props.params.tagPath`: expression

```js
{view.custom.values.analog}
```


- `props.style.visibility`: expression

```js
if(coalesce({view.custom.oos}, false), 'hidden', 'visible')
```


**`root/Status`**

- `props.params.tagPath`: expression

```js
{view.custom.values.status}
```


- `props.params.outOfService`: property `view.custom.oos`

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
# Unified tabbed Faceplate. show* are hints; tagFlags hide empty tabs.
params = {
    'tagPath': tagPath,
    'deviceType': 'CoolingTower',
    'webGuiUrl': '',
    'showControls': True,
    'showConfiguration': True,
    'showInterlocks': True,
    'showTrend': True,
    'showAlarmConfiguration': True,
    'showAlarms': True
}
Navigation.Faceplate.openFaceplate(
    'ct-fp-%s' % (tagPath or title),
    tagPath,
    '01_Popups/00_Faceplates/Faceplate',
    False,
    title,
# ... 4 more line(s): see the view.json
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

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.OutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openDialog](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openHistory](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.setOutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.Security.allowed](../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Embeds** (4): [03\_Elements/01\_Status/AlarmHeader](../../03-elements/01-status/alarmheader.md), [03\_Elements/01\_Status/AnalogValue](../../03-elements/01-status/analogvalue.md), [03\_Elements/01\_Status/IconHeader](../../03-elements/01-status/iconheader.md), [03\_Elements/01\_Status/StatusIndicator](../../03-elements/01-status/statusindicator.md)

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/Faceplate](../../01-popups/00-faceplates/faceplate.md)

**Embedded in** (1): [00\_Pages/Boars Head/Devices/DesignOverview](../../00-pages/boars-head/devices/designoverview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `alarm-frame` | 1 | stylesheet |
| `alarm-header` | 1 | stylesheet |
| `fs-11` | 1 | style class |
| `fw-700` | 1 | style class |
| `icon-header` | 1 | style class |
| `alarm-border` | bound | stylesheet |
| `ct-fan-side-spin` | bound | stylesheet |
| `ct-spray-run` | bound | stylesheet |
| `device-comm-loss` | bound | stylesheet |
| `device-graphic` | bound | stylesheet |
| `device-oos` | bound | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}/_Alarms/_Active`
- `{tagPath}/_Alarms/_ActiveHighPriority`
- `{tagPath}/_Alarms/_Unack`

Member paths appended to a base path in expressions (relative):

`.Enabled`, `.Metadata`, `/SPD_FBK/Value`, `/Status/Value`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
