---
title: "SolenoidValve"
sidebar_label: "SolenoidValve"
description: "Perspective view 02_Components/01_Devices/SolenoidValve (Reusable component): 11 components, 30 bindings, 5 event scripts."
generated: true
keywords: ["02_Components/01_Devices/SolenoidValve", "SolenoidValve"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/SolenoidValve`.

| | |
|---|---|
| View path | `02_Components/01_Devices/SolenoidValve` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/SolenoidValve/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; SolenoidValve |
| Root | `ia.container.flex`, height 133, width 71 |
| Size | 11 components, 30 bindings, 1 event handlers, 4 change scripts, 3 message handlers |
| Last saved | 2026-08-04T15:00:42Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `faceplate` | `null` | input |
| `feedback` | `true` | input |
| `label` | `""` | input |
| `tagPath` | `""` | input |
| `orientation` | `{"horizontal": false, "horizontalReverse": false, "vertical": true,...` | inout |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `alarm` | `{"active": false, "priority": 10, "unack": false}` | |
| `label` | `""` | bound (expr) |
| `metadata` | `""` | bound (expr) |
| `values` | `{}` | |
| `oos` | `false` | bound (expr) |
| `orientation` | `"vertical"` | bound (expr) |
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.view x4, ia.container.flex x2, ia.container.coord x2, ia.display.label x1, ia.display.icon x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [3 bindings; 1 event]
  LabelHeader  ia.container.flex
    IconHeader  ia.display.view  [1 binding; view: 03_Elements/01_Status/IconHeader]
    DeviceLabel  ia.display.label  [1 binding]
    FaceplateIcon  ia.display.icon  [2 bindings]
  Graphic  ia.container.coord  [1 binding]
    Body  ia.shapes.svg  [1 binding]
    AlarmFrame  ia.container.coord  [2 bindings]
    AlarmHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/AlarmHeader]
  AnalogValue  ia.display.view  [3 bindings; view: 03_Elements/01_Status/AnalogValue]
  Status  ia.display.view  [3 bindings; view: 03_Elements/01_Status/StatusIndicator]
```

## Bindings

30 bindings: expr 22, property 4, tag 3, expr-struct 1.

<details>
<summary>All 30 bindings, grouped by component</summary>

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
if({view.params.label} != '',
	{view.params.label},
	if({view.params.tagPath} = '',
		'',
		subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1))
)
```


- `custom.metadata`: expression

```js
if(
	{view.params.tagPath}!='' && isGood(tag({view.params.tagPath} + '.Metadata')),
	tag({view.params.tagPath} + '.Metadata'),
	'')
```


- `custom.values.analog`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/Valve/Cfg_TransitStallT')
```


- `custom.values.commLoss`: expression

```js
if(coalesce({view.custom.oos}, false),
	false,
	(if({view.params.tagPath} = '',
	false,
	if(isGood(tag({view.params.tagPath} + '/Valve/Sts_IOFault')),
		tag({view.params.tagPath} + '/Valve/Sts_IOFault') = true,
		if(isGood(tag({view.params.tagPath} + '/Valve/Val_Sts')),
			false,
			false)))))
```


- `custom.values.status`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/Valve/Val_Sts')
```


- `custom.oos`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
```


- `custom.orientation`: expression

```js
if({view.params.orientation.horizontal},
   'horizontal',
   if({view.params.orientation.horizontalReverse},
      'horizontal-reverse',
      if({view.params.orientation.verticalReverse},
         'vertical-reverse',
         'vertical')))
```


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../common-patterns.md#pattern-6).

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

- `props.style.classes`: expression

```js
'valve-component valve-' + coalesce({view.custom.orientation}, 'vertical')
```


**`root/LabelHeader/IconHeader`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/LabelHeader/DeviceLabel`**

- `props.text`: property `view.custom.label`

**`root/LabelHeader/FaceplateIcon`**

- `meta.visible`: expression

```js
coalesce({session.custom.CanOpenFaceplates}, false) && (!(isNull({view.params.faceplate}) || {view.params.faceplate} = ''))
```


- `props.style.opacity`: expression

```js
if(isNull({view.params.faceplate}) || {view.params.faceplate} = '',
   0,
   1)
```


**`root/Graphic`**

- `props.style.classes`: expression

```js
((if(coalesce({view.custom.values.commLoss}, false),
	'device-graphic device-comm-loss',
	'device-graphic')) + if(coalesce({view.custom.oos}, false), ' device-oos', '')) + if(coalesce({session.custom.CanOpenFaceplates}, false) && (len(trim(coalesce({view.params.faceplate}, ''))) > 0), ' faceplate-hover', '')
```


**`root/Graphic/Body`**

- `props.style.transform`: expression

```js
case(coalesce({view.custom.orientation}, 'vertical'),
	'vertical-reverse', 'scaleY(-1)',
	'horizontal', 'rotate(-90deg)',
	'horizontal-reverse', 'rotate(90deg)',
	'none')
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
{view.params.tagPath} != '' && coalesce({view.params.feedback}, true)
```


- `props.params.tagPath`: expression

```js
{view.custom.values.analog}
```


- `props.style.visibility`: expression

```js
if(coalesce({view.custom.oos}, false), 'hidden', 'visible')
```


**`root/Status`**

- `meta.visible`: expression

```js
{view.params.tagPath} != '' && coalesce({view.params.feedback}, true)
```


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
# Unified Faceplate via shared.Alerts (Valve Config/Trend curation defaults).
shared.Alerts.showFaceplate(
    tagPath=tagPath,
    deviceType='Valve',
    title=title,
    width=560,
    height=656
)
```

- **`(view)`** change script on `params.orientation.horizontal`

```python
if currentValue.value:
    self.params.orientation.horizontalReverse = False
    self.params.orientation.vertical = False
    self.params.orientation.verticalReverse = False
elif not self.params.orientation.vertical and not self.params.orientation.horizontalReverse and not self.params.orientation.verticalReverse:
    self.params.orientation.vertical = True
```

- **`(view)`** change script on `params.orientation.horizontalReverse`

```python
if currentValue.value:
    self.params.orientation.horizontal = False
    self.params.orientation.vertical = False
    self.params.orientation.verticalReverse = False
elif not self.params.orientation.vertical and not self.params.orientation.horizontal and not self.params.orientation.verticalReverse:
    self.params.orientation.vertical = True
```

- **`(view)`** change script on `params.orientation.vertical`

```python
if currentValue.value:
    self.params.orientation.horizontal = False
    self.params.orientation.horizontalReverse = False
    self.params.orientation.verticalReverse = False
elif not self.params.orientation.horizontalReverse and not self.params.orientation.horizontal and not self.params.orientation.verticalReverse:
    self.params.orientation.horizontal = True
```

- **`(view)`** change script on `params.orientation.verticalReverse`

```python
if currentValue.value:
    self.params.orientation.horizontalReverse = False
    self.params.orientation.horizontal = False
    self.params.orientation.vertical = False
elif not self.params.orientation.vertical and not self.params.orientation.horizontalReverse and not self.params.orientation.horizontal:
    self.params.orientation.vertical = True
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

Project script calls: [shared.Alerts](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.OutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openDialog](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openHistory](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.setOutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.Security.allowed](../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Embeds** (4): [03\_Elements/01\_Status/AlarmHeader](../../03-elements/01-status/alarmheader.md), [03\_Elements/01\_Status/AnalogValue](../../03-elements/01-status/analogvalue.md), [03\_Elements/01\_Status/IconHeader](../../03-elements/01-status/iconheader.md), [03\_Elements/01\_Status/StatusIndicator](../../03-elements/01-status/statusindicator.md)

**Embedded in** (6): [00\_Pages/Boars Head/Machine Room/Overview](../../00-pages/boars-head/machine-room/overview.md), [00\_Pages/Boars Head/Valves/Design](../../00-pages/boars-head/valves/design.md), [00\_Pages/Groveport/Condensers/Utility/Overview](../../00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Valves/Design](../../00-pages/groveport/condensers/utility/valves/design.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../../00-pages/groveport/machine-room/utility/overview.md), [00\_Pages/Groveport/\_Shared/CG/AhuEvapDisplay](../../00-pages/groveport/shared/cg/ahuevapdisplay.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `alarm-header` | 1 | stylesheet |
| `icon-header` | 1 | style class |
| `valve-label` | 1 | stylesheet |
| `valve-status` | 1 | stylesheet |
| `valve-value` | 1 | stylesheet |
| `alarm-border` | bound | stylesheet |
| `alarm-frame` | bound | stylesheet |
| `device-comm-loss` | bound | stylesheet |
| `device-graphic` | bound | stylesheet |
| `device-oos` | bound | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}/_Alarms/_Active`
- `{tagPath}/_Alarms/_ActiveHighPriority`
- `{tagPath}/_Alarms/_Unack`

Member paths appended to a base path in expressions (relative):

`.Enabled`, `.Metadata`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Valve/Cfg_TransitStallT`, `/Valve/Sts_IOFault`, `/Valve/Val_Sts`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
