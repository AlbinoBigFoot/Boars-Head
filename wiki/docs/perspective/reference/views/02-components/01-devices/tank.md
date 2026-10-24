---
title: "Tank"
sidebar_label: "Tank"
description: "Perspective view 02_Components/01_Devices/Tank (Reusable component): 29 components, 58 bindings, 8 event scripts."
generated: true
keywords: ["02_Components/01_Devices/Tank", "Tank"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/Tank`.

| | |
|---|---|
| View path | `02_Components/01_Devices/Tank` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Tank/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; Tank |
| Root | `ia.container.flex`, height 191, width 168 |
| Size | 29 components, 58 bindings, 6 event handlers, 2 change scripts, 3 message handlers |
| Last saved | 2026-07-30T05:08:25Z by djones |

## Params

| Name | Default | Notes |
|---|---|---|
| `faceplate` | `null` | input |
| `orientation` | `{"reverse": false, "standard": true}` | inout |
| `tagPath` | `""` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `alarm` | `{"active": false, "priority": 10, "unack": false}` | |
| `label` | `""` | bound (expr) |
| `metadata` | `""` | bound (expr) |
| `selectedSp` | `""` | |
| `values` | `{}` | |
| `oos` | `false` | bound (expr) |
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.coord x14, ia.container.flex x5, ia.display.label x5, ia.display.view x4, ia.display.icon x1.

<details>
<summary>Component tree (29 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  TankStack  ia.container.flex
    LabelHeader  ia.container.flex  [1 binding]
      IconHeader  ia.display.view  [1 binding; view: 03_Elements/01_Status/IconHeader]
      DeviceLabel  ia.display.label  [1 binding]
      FaceplateIcon  ia.display.icon  [2 bindings]
    Graphic  ia.container.coord  [1 binding]
      GlassPipeTop  ia.container.coord  [1 binding]
      GlassPipeBot  ia.container.coord  [1 binding]
      Vessel  ia.container.flex  [1 binding]
        Liquid  ia.container.coord  [1 binding]
      SightGlass  ia.container.flex  [1 binding]
        GlassLiquid  ia.container.coord  [1 binding]
      MarkHH  ia.container.coord  [2 bindings; 1 event]
        tick  ia.container.coord  [1 binding]
        label  ia.display.label  [1 binding]
      MarkH  ia.container.coord  [2 bindings; 1 event]
        tick  ia.container.coord  [1 binding]
        label  ia.display.label  [1 binding]
      MarkL  ia.container.coord  [2 bindings; 1 event]
        tick  ia.container.coord  [1 binding]
        label  ia.display.label  [1 binding]
      MarkLL  ia.container.coord  [2 bindings; 1 event]
        tick  ia.container.coord  [1 binding]
        label  ia.display.label  [1 binding]
      AlarmFrame  ia.container.coord  [2 bindings]
      AlarmHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/AlarmHeader]
    AnalogValue  ia.display.view  [4 bindings; 1 event; view: 03_Elements/01_Status/AnalogValue]
    Status  ia.display.view  [4 bindings; view: 03_Elements/01_Status/StatusIndicator]
```

</details>

## Bindings

58 bindings: expr 50, property 4, tag 3, expr-struct 1.

<details>
<summary>All 58 bindings, grouped by component</summary>

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


- `custom.values.analog`: expression

```js
if({view.params.tagPath} = '',
	'',
	if({view.custom.selectedSp} = '',
		{view.params.tagPath} + '/LvlAIn/Val',
		{view.params.tagPath} + '/LvlAIn/' + case({view.custom.selectedSp}, 'HH', 'Val_HiHiLim', 'H', 'Val_HiLim', 'L', 'Val_LoLim', 'LL', 'Val_LoLoLim', 'Val')))
```


- `custom.values.analogForceColor`: expression

```js
if(coalesce({view.custom.values.hh}, false) || coalesce({view.custom.values.ll}, false),
	'critical',
	if(coalesce({view.custom.values.h}, false) || coalesce({view.custom.values.l}, false),
		'warning',
		''))
```


- `custom.values.commLoss`: expression

```js
if(coalesce({view.custom.oos}, false),
	false,
	(if({view.params.tagPath} = '',
	false,
	!isGood(tag({view.params.tagPath} + '/LvlAIn/Val_Fault')))))
```


- `custom.values.h`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Hi')),
	false,
	coalesce(tag({view.params.tagPath} + '/LvlAIn/Sts_Hi'), false))
```


- `custom.values.hh`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_HiHi')),
	false,
	coalesce(tag({view.params.tagPath} + '/LvlAIn/Sts_HiHi'), false))
```


- `custom.values.l`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_Lo')),
	false,
	coalesce(tag({view.params.tagPath} + '/LvlAIn/Sts_Lo'), false))
```


- `custom.values.level`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/LvlAIn/Val')),
	0,
	coalesce(tag({view.params.tagPath} + '/LvlAIn/Val'), 0))
```


- `custom.values.ll`: expression

```js
if({view.params.tagPath} = '' || !isGood(tag({view.params.tagPath} + '/LvlAIn/Sts_LoLo')),
	false,
	coalesce(tag({view.params.tagPath} + '/LvlAIn/Sts_LoLo'), false))
```


- `custom.values.status`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/LvlAIn/Val_Fault')
```


- `custom.oos`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
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


**`root/TankStack/LabelHeader`**

- `props.style.marginLeft`: expression

```js
if({view.params.orientation.reverse},
	'60px',
	'36px')
```


**`root/TankStack/LabelHeader/IconHeader`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/TankStack/LabelHeader/DeviceLabel`**

- `props.text`: property `view.custom.label`

**`root/TankStack/LabelHeader/FaceplateIcon`**

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


**`root/TankStack/Graphic`**

- `props.style.classes`: expression

```js
((if(coalesce({view.custom.values.commLoss}, false),
	'device-graphic device-comm-loss',
	'device-graphic')) + if(coalesce({view.custom.oos}, false), ' device-oos', '')) + if(coalesce({session.custom.CanOpenFaceplates}, false) && (len(trim(coalesce({view.params.faceplate}, ''))) > 0), ' faceplate-hover', '')
```


**`root/TankStack/Graphic/GlassPipeTop`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	48,
	108)
```


**`root/TankStack/Graphic/GlassPipeBot`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	48,
	108)
```


**`root/TankStack/Graphic/Vessel`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	60,
	36)
```


**`root/TankStack/Graphic/Vessel/Liquid`**

- `props.style.height`: expression

```js
toString(max(0, min(100, coalesce({view.custom.values.level}, 0)))) + '%'
```


**`root/TankStack/Graphic/SightGlass`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	32,
	120)
```


**`root/TankStack/Graphic/SightGlass/GlassLiquid`**

- `props.style.height`: expression

```js
toString(max(0, min(100, coalesce({view.custom.values.level}, 0)))) + '%'
```


**`root/TankStack/Graphic/MarkHH`**

- `meta.visible`: expression

```js
coalesce({view.custom.values.hh}, false)
```


- `position.x`: expression

```js
if({view.params.orientation.reverse},
	2,
	138)
```


**`root/TankStack/Graphic/MarkHH/tick`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	20,
	0)
```


**`root/TankStack/Graphic/MarkHH/label`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	0,
	10)
```


**`root/TankStack/Graphic/MarkH`**

- `meta.visible`: expression

```js
coalesce({view.custom.values.h}, false)
```


- `position.x`: expression

```js
if({view.params.orientation.reverse},
	2,
	138)
```


**`root/TankStack/Graphic/MarkH/tick`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	20,
	0)
```


**`root/TankStack/Graphic/MarkH/label`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	0,
	10)
```


**`root/TankStack/Graphic/MarkL`**

- `meta.visible`: expression

```js
coalesce({view.custom.values.l}, false)
```


- `position.x`: expression

```js
if({view.params.orientation.reverse},
	2,
	138)
```


**`root/TankStack/Graphic/MarkL/tick`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	20,
	0)
```


**`root/TankStack/Graphic/MarkL/label`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	0,
	10)
```


**`root/TankStack/Graphic/MarkLL`**

- `meta.visible`: expression

```js
coalesce({view.custom.values.ll}, false)
```


- `position.x`: expression

```js
if({view.params.orientation.reverse},
	2,
	138)
```


**`root/TankStack/Graphic/MarkLL/tick`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	20,
	0)
```


**`root/TankStack/Graphic/MarkLL/label`**

- `position.x`: expression

```js
if({view.params.orientation.reverse},
	0,
	10)
```


**`root/TankStack/Graphic/AlarmFrame`**

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


**`root/TankStack/Graphic/AlarmHeader`**

- `meta.visible`: expression

```js
{view.custom.alarm.active}
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/TankStack/AnalogValue`**

- `props.params.forceColor`: expression

```js
{view.custom.values.analogForceColor}
```


- `props.params.tagPath`: expression

```js
{view.custom.values.analog}
```


- `props.style.marginLeft`: expression

```js
if({view.params.orientation.reverse},
	'60px',
	'36px')
```


- `props.style.visibility`: expression

```js
if(coalesce({view.custom.oos}, false), 'hidden', 'visible')
```


**`root/TankStack/Status`**

- `props.params.tagPath`: expression

```js
{view.custom.values.status}
```


- `meta.visible`: expression

```js
if(coalesce({view.custom.values.commLoss}, false),
	true,
	if({view.custom.values.status} = '' || !isGood(tag({view.custom.values.status})),
		false,
		coalesce(tag({view.custom.values.status}), 0) != 0))
```


- `props.params.outOfService`: property `view.custom.oos`

- `props.style.marginLeft`: expression

```js
if({view.params.orientation.reverse},
	'60px',
	'36px')
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
if str(faceplate).strip() == 'TankOverview':
    Navigation.Faceplate.openFaceplate('tankov-fp-%s' % (tagPath or title), tagPath,
        '01_Popups/00_Faceplates/TankOverview', False, title, 1100, 760, {'title': title})
    return
# Unified tabbed Faceplate. show* are hints; tagFlags hide empty tabs.
params = {
    'tagPath': tagPath,
    'deviceType': 'Tank',
    'webGuiUrl': '',
    'showControls': True,
    'showConfiguration': True,
    'showInterlocks': True,
    'showTrend': True,
    'showAlarmConfiguration': True,
    'showAlarms': True
}
Navigation.Faceplate.openFaceplate(
    'tank-fp-%s' % (tagPath or title),
# ... 8 more line(s): see the view.json
```

- **`root/TankStack/Graphic/MarkHH`** `dom.onClick`, script action, scope `G`

```python
key = 'HH'
cur = ''
try:
    cur = str(self.view.custom.selectedSp or '')
except:
    cur = ''
self.view.custom.selectedSp = '' if cur == key else key
```

- **`root/TankStack/Graphic/MarkH`** `dom.onClick`, script action, scope `G`

```python
key = 'H'
cur = ''
try:
    cur = str(self.view.custom.selectedSp or '')
except:
    cur = ''
self.view.custom.selectedSp = '' if cur == key else key
```

- **`root/TankStack/Graphic/MarkL`** `dom.onClick`, script action, scope `G`

```python
key = 'L'
cur = ''
try:
    cur = str(self.view.custom.selectedSp or '')
except:
    cur = ''
self.view.custom.selectedSp = '' if cur == key else key
```

- **`root/TankStack/Graphic/MarkLL`** `dom.onClick`, script action, scope `G`

```python
key = 'LL'
cur = ''
try:
    cur = str(self.view.custom.selectedSp or '')
except:
    cur = ''
self.view.custom.selectedSp = '' if cur == key else key
```

- **`root/TankStack/AnalogValue`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.selectedSp = ''
```

- **`(view)`** change script on `params.orientation.reverse`

```python
if currentValue.value:
    self.params.orientation.standard = False
elif not self.params.orientation.standard:
    self.params.orientation.standard = True
```

- **`(view)`** change script on `params.orientation.standard`

```python
if currentValue.value:
    self.params.orientation.reverse = False
elif not self.params.orientation.reverse:
    self.params.orientation.reverse = True
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

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/Faceplate](../../01-popups/00-faceplates/faceplate.md), [01\_Popups/00\_Faceplates/TankOverview](../../01-popups/00-faceplates/tankoverview.md)

**Embedded in** (5): [00\_Pages/Boars Head/Machine Room/Overview](../../00-pages/boars-head/machine-room/overview.md), [00\_Pages/Boars Head/Tanks/Design](../../00-pages/boars-head/tanks/design.md), [00\_Pages/Groveport/Condensers/Utility/Overview](../../00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Tanks/Design](../../00-pages/groveport/condensers/utility/tanks/design.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../../00-pages/groveport/machine-room/utility/overview.md)

## Style Classes

<details>
<summary>23 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 4 | style class |
| `Fonts/Value` | 1 | style class |
| `alarm-header` | 1 | stylesheet |
| `fs-10` | 4 | style class |
| `fs-11` | 1 | style class |
| `fw-600` | 4 | style class |
| `fw-700` | 1 | style class |
| `icon-header` | 1 | style class |
| `tank-level-critical` | 2 | stylesheet |
| `tank-level-mark` | 4 | stylesheet |
| `tank-level-text-critical` | 2 | style class |
| `tank-level-text-warning` | 2 | style class |
| `tank-level-warning` | 2 | stylesheet |
| `tank-liquid` | 2 | stylesheet |
| `tank-over-vessel` | 3 | stylesheet |
| `tank-sight` | 1 | stylesheet |
| `tank-stem` | 2 | stylesheet |
| `tank-vessel` | 1 | stylesheet |
| `alarm-border` | bound | stylesheet |
| `alarm-frame` | bound | stylesheet |
| `device-comm-loss` | bound | stylesheet |
| `device-graphic` | bound | stylesheet |
| `device-oos` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}/_Alarms/_Active`
- `{tagPath}/_Alarms/_ActiveHighPriority`
- `{tagPath}/_Alarms/_Unack`

Member paths appended to a base path in expressions (relative):

<details>
<summary>13 relative member paths</summary>

`.Enabled`, `.Metadata`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/LvlAIn/`, `/LvlAIn/Sts_Hi`, `/LvlAIn/Sts_HiHi`, `/LvlAIn/Sts_Lo`, `/LvlAIn/Sts_LoLo`, `/LvlAIn/Val`, `/LvlAIn/Val_Fault`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
