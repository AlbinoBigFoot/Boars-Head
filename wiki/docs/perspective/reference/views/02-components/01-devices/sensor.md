---
title: "Sensor"
sidebar_label: "Sensor"
description: "Perspective view 02_Components/01_Devices/Sensor (Reusable component): 11 components, 39 bindings, 5 event scripts."
generated: true
keywords: ["02_Components/01_Devices/Sensor", "Sensor"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/Sensor`.

| | |
|---|---|
| View path | `02_Components/01_Devices/Sensor` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Sensor/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; Sensor |
| Root | `ia.container.flex`, height 100, width 160 |
| Size | 11 components, 39 bindings, 1 event handlers, 4 change scripts, 3 message handlers |
| Last saved | 2026-07-30T05:20:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `faceplate` | `null` | input |
| `tagPath` | `""` | input |
| `orientation` | `{"horizontal": false, "horizontalReverse": false, "vertical": true,...` | inout |
| `feedback` | `true` | input |
| `label` | `"SNS"` | input |
| `valuePosition` | `"auto"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | bound (expr) |
| `metadata` | `""` | bound (expr) |
| `orientation` | `"vertical"` | bound (expr) |
| `values` | `{}` | |
| `alarm` | `{"active": false, "priority": 10, "unack": false}` | |
| `oos` | `false` | bound (expr) |
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.container.flex x4, ia.display.view x4, ia.display.label x1, ia.display.icon x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [5 bindings; 1 event]
  NotificationHeader  ia.container.flex
    IconHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/IconHeader]
  StemAssembly  ia.container.flex  [2 bindings]
    BadgeBox  ia.container.flex  [1 binding]
      Badge  ia.display.label  [3 bindings]
      FaceplateIcon  ia.display.icon  [3 bindings]
      AlarmHeader  ia.display.view  [1 binding; view: 03_Elements/01_Status/AlarmHeader]
      BadgeValue  ia.display.view  [4 bindings; view: 03_Elements/01_Status/AnalogValue]
    Stem  ia.shapes.svg  [4 bindings]
  AnalogValue  ia.display.view  [3 bindings; view: 03_Elements/01_Status/AnalogValue]
```

## Bindings

39 bindings: expr 31, property 4, tag 3, expr-struct 1.

<details>
<summary>All 39 bindings, grouped by component</summary>

**`(view)`**

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


- `custom.values.status`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/AIn/Val_Fault')
```


- `custom.values.analog`: expression

```js
if({view.params.tagPath} = '',
	'',
	{view.params.tagPath} + '/AIn/Val')
```


- `custom.values.commLoss`: expression

```js
if(coalesce({view.params.tagPath}, '') = '' || coalesce({view.custom.oos}, false),
	false,
	!isGood(tag({view.params.tagPath} + '/AIn/Val')))
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


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../common-patterns.md#pattern-6).

**`root`**

- `props.alignContent`: expression

```js
if({view.params.orientation.verticalReverse},
   'flex-start',
   'flex-end')
```


- `props.justify`: expression

```js
if({view.params.orientation.vertical} || {view.params.orientation.verticalReverse},
   'center',
   if({view.params.orientation.horizontalReverse},
      'flex-start',
      'flex-end'))
```


- `props.style.classes`: expression

```js
((if({view.params.orientation.horizontal},
   'sensor-horizontal sensor-component',
   if({view.params.orientation.horizontalReverse},
      'sensor-horizontal-reverse sensor-component',
      if({view.params.orientation.vertical},
         'sensor-vertical sensor-component',
         'sensor-vertical-reverse sensor-component'))))) + if(coalesce({view.custom.values.commLoss}, false) || indexOf(case(coalesce({view.custom.orientation}, 'vertical'), 'horizontal', '', 'horizontal-reverse', '', 'vertical-reverse', ',left,right,top,', ',left,right,bottom,'), ',' + lower(coalesce({view.params.valuePosition}, 'auto')) + ',') >= 0, ' sensor-value-away', if(lower(coalesce({view.params.valuePosition}, 'auto')) = 'bottom' && indexOf(coalesce({view.custom.orientation}, 'vertical'), 'horizontal') = 0, ' sensor-value-under', ''))
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

**`root/NotificationHeader/IconHeader`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

- `props.params.statusPath`: property `view.custom.values.analog`

**`root/StemAssembly`**

- `props.direction`: expression

```js
if({view.params.orientation.verticalReverse},
   'column-reverse',
   if({view.params.orientation.horizontalReverse},
      'row-reverse',
      if({view.params.orientation.horizontal},
         'row',
         'column')))
```


- `props.style.classes`: expression

```js
'stem' + if(coalesce({session.custom.CanOpenFaceplates}, false) && (len(trim(coalesce({view.params.faceplate}, ''))) > 0), ' faceplate-hover', '')
```


**`root/StemAssembly/BadgeBox`**

- `props.style.classes`: expression

```js
(if(lower(coalesce({view.params.valuePosition}, 'auto')) = 'left', 'sensor-badge-box sensor-badge-box-value-left', 'sensor-badge-box')) + if(coalesce({view.custom.oos}, false), ' device-oos', '')
```


**`root/StemAssembly/BadgeBox/Badge`**

- `props.text`: property `view.custom.label`

- `props.style.cursor`: expression

```js
if(isNull({view.params.faceplate}) || {view.params.faceplate} = '',
   '',
   'pointer')
```


- `props.style.classes`: expression

```js
if(coalesce({view.custom.values.commLoss}, false), 'tag-label sensor-badge Fonts/Value fs-11 fw-700 device-comm-loss', if(coalesce({view.custom.alarm.active}, false), 'tag-label sensor-badge Fonts/Value fs-11 fw-700 alarm-border alarm-priority-' + case(coalesce({view.custom.alarm.priority}, -1), 4, 'critical', 3, 'high', 2, 'medium', 1, 'low', 'low'), 'tag-label sensor-badge Fonts/Value fs-11 fw-700'))
```


**`root/StemAssembly/BadgeBox/FaceplateIcon`**

- `meta.visible`: expression

```js
coalesce({session.custom.CanOpenFaceplates}, false) && (len(trim(coalesce({view.params.faceplate}, ''))) > 0)
```


- `props.style.opacity`: expression

```js
if(len(trim(coalesce({view.params.faceplate}, ''))) > 0, 1, 0)
```


- `props.style.classes`: expression

```js
'sensor-faceplate-icon ' + if((coalesce({view.params.orientation.horizontal}, false) || lower(coalesce({view.params.valuePosition}, 'auto')) = 'right' || (coalesce({view.params.orientation.horizontalReverse}, false) && lower(coalesce({view.params.valuePosition}, 'auto')) = 'auto')), if(lower(coalesce({view.params.valuePosition}, 'auto')) = 'bottom', 'sensor-faceplate-icon-raised', 'sensor-faceplate-icon-lowered'), 'sensor-faceplate-icon-side')
```


**`root/StemAssembly/BadgeBox/AlarmHeader`**

- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

**`root/StemAssembly/BadgeBox/BadgeValue`**

- `props.params.tagPath`: expression

```js
{view.custom.values.analog}
```


- `meta.visible`: expression

```js
coalesce({view.params.feedback}, true) && (lower(coalesce({view.params.valuePosition}, 'auto')) = 'top' || lower(coalesce({view.params.valuePosition}, 'auto')) = 'bottom' || lower(coalesce({view.params.valuePosition}, 'auto')) = 'left' || lower(coalesce({view.params.valuePosition}, 'auto')) = 'right')
```


- `props.style.classes`: expression

```js
'sensor-badge-value sensor-badge-value-' + lower(coalesce({view.params.valuePosition}, 'auto'))
```


- `props.style.visibility`: expression

```js
if(coalesce({view.custom.oos}, false), 'hidden', 'visible')
```


**`root/StemAssembly/Stem`**

- `props.elements[0].d`: expression

```js
if({view.params.orientation.vertical} || {view.params.orientation.verticalReverse},
   'M1 0V24',
   'M0 1H24')
```


- `props.style.height`: expression

```js
if({view.params.orientation.vertical} || {view.params.orientation.verticalReverse},
   '24px',
   '2px')
```


- `props.style.width`: expression

```js
if({view.params.orientation.vertical} || {view.params.orientation.verticalReverse},
   '2px',
   '24px')
```


- `props.viewBox`: expression

```js
if({view.params.orientation.vertical} || {view.params.orientation.verticalReverse},
   '0 0 2 24',
   '0 0 24 2')
```


**`root/AnalogValue`**

- `props.params.tagPath`: expression

```js
{view.custom.values.analog}
```


- `meta.visible`: expression

```js
coalesce({view.params.feedback}, true)
```


- `props.style.visibility`: expression

```js
if(coalesce({view.custom.oos}, false), 'hidden', if((lower(coalesce({view.params.valuePosition}, 'auto')) = 'top' || lower(coalesce({view.params.valuePosition}, 'auto')) = 'bottom' || lower(coalesce({view.params.valuePosition}, 'auto')) = 'left' || lower(coalesce({view.params.valuePosition}, 'auto')) = 'right'), 'hidden', 'visible'))
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
if title in (None, '', 'nn', 'SNS'):
    title = tagPath.split('/')[-1] if tagPath else self.view.name
# Unified tabbed Faceplate. show* are hints; tagFlags hide empty tabs.
params = {
    'tagPath': tagPath,
    'deviceType': 'Sensor',
    'webGuiUrl': '',
    'showControls': True,
    'showConfiguration': True,
    'showInterlocks': False,   # P_AIn has no interlocks
    'showTrend': True,
    'showAlarmConfiguration': True,
    'showAlarms': True
}
Navigation.Faceplate.openFaceplate(
    'sensor-fp-%s' % (tagPath or title),
    tagPath,
    '01_Popups/00_Faceplates/Faceplate',
    False,
    title,
# ... 4 more line(s): see the view.json
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

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.OutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openDialog](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.openHistory](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.OutOfService.setOutOfService](../../../../../scripting/reference/modules/shared-outofservice.md), [shared.Security.allowed](../../../../../scripting/reference/modules/shared-security.md).

## Related Views

**Embeds** (3): [03\_Elements/01\_Status/AlarmHeader](../../03-elements/01-status/alarmheader.md), [03\_Elements/01\_Status/AnalogValue](../../03-elements/01-status/analogvalue.md), [03\_Elements/01\_Status/IconHeader](../../03-elements/01-status/iconheader.md)

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/Faceplate](../../01-popups/00-faceplates/faceplate.md)

**Embedded in** (5): [00\_Pages/Boars Head/Machine Room/Overview](../../00-pages/boars-head/machine-room/overview.md), [00\_Pages/Boars Head/Sensors/Design](../../00-pages/boars-head/sensors/design.md), [00\_Pages/Groveport/Condensers/Utility/Overview](../../00-pages/groveport/condensers/utility/overview.md), [00\_Pages/Groveport/Condensers/Utility/Sensors/Design](../../00-pages/groveport/condensers/utility/sensors/design.md), [00\_Pages/Groveport/Machine Room/Utility/Overview](../../00-pages/groveport/machine-room/utility/overview.md)

## Style Classes

<details>
<summary>26 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `fs-11` | 1 | style class |
| `fw-700` | 1 | style class |
| `icon-header` | 1 | style class |
| `notification-wrapper` | 1 | stylesheet |
| `sensor-alarm-badge` | 1 | stylesheet |
| `sensor-badge` | 1 | stylesheet |
| `sensor-badge-box` | 1 | stylesheet |
| `sensor-badge-value` | 1 | stylesheet |
| `sensor-faceplate-icon` | 1 | stylesheet |
| `sensor-faceplate-icon-side` | 1 | stylesheet |
| `stem` | 1 | stylesheet |
| `stem-line` | 1 | stylesheet |
| `tag-label` | 1 | stylesheet |
| `value` | 1 | stylesheet |
| `alarm-border` | bound | stylesheet |
| `device-comm-loss` | bound | stylesheet |
| `device-oos` | bound | stylesheet |
| `sensor-badge-box-value-left` | bound | stylesheet |
| `sensor-component` | bound | stylesheet |
| `sensor-faceplate-icon-lowered` | bound | stylesheet |
| `sensor-faceplate-icon-raised` | bound | stylesheet |
| `sensor-horizontal` | bound | stylesheet |
| `sensor-horizontal-reverse` | bound | stylesheet |
| `sensor-vertical` | bound | stylesheet |
| `sensor-vertical-reverse` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{tagPath}/_Alarms/_Active`
- `{tagPath}/_Alarms/_ActiveHighPriority`
- `{tagPath}/_Alarms/_Unack`

Member paths appended to a base path in expressions (relative):

`.Enabled`, `.Metadata`, `.TypeId`, `/AIn.Enabled`, `/AIn/Val`, `/AIn/Val_Fault`, `/AInRef.Enabled`, `/DIn.Enabled`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
