---
title: "Faceplate"
sidebar_label: "Faceplate"
description: "Perspective view 01_Popups/00_Faceplates/Faceplate (Popup / faceplate): 16 components, 62 bindings, 12 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/Faceplate", "Faceplate"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/Faceplate`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/Faceplate` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; Faceplate |
| Root | `ia.container.flex`, height 656, width 560 |
| Size | 16 components, 62 bindings, 10 event handlers, 2 change scripts, 2 message handlers |
| Last saved | 2026-07-31T05:37:13Z by djones |

## Params

<details>
<summary>15 params</summary>

| Name | Default | Notes |
|---|---|---|
| `deviceType` | `"Compressor"` | input |
| `hiddenFromAlarmConfiguration` | `""` | input |
| `hiddenFromAlarms` | `""` | input |
| `hiddenFromConfiguration` | `""` | input |
| `hiddenFromTrend` | `""` | input |
| `popupId` | `""` | |
| `showAlarmConfiguration` | `true` | input |
| `showAlarms` | `true` | input |
| `showConfiguration` | `true` | input |
| `showControls` | `true` | input |
| `showInterlocks` | `true` | input |
| `showTrend` | `true` | input |
| `tagPath` | `""` | input |
| `webGuiUrl` | `""` | input |
| `initialTab` | `""` | input |

</details>

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | bound (expr) |
| `metadata` | `""` | bound (expr) |
| `selected` | `"Controls"` | change script |
| `tagFlags` | `{"defaultTab": "Controls", "showAlarmConfiguration": false, "showAl...` | bound (expr-struct), change script |
| `visibleTabCount` | `1` | bound (expr) |
| `verticalTabs` | `true` | |
| `showDiscreteInputs` | `false` | bound (expr) |
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.input.button x8, ia.container.flex x5, ia.display.label x1, ia.display.icon x1, ia.display.view x1.

<details>
<summary>Component tree (16 components)</summary>

```text
root  ia.container.flex  [3 bindings; 1 event]
  Header  ia.container.flex
    Title  ia.display.label  [1 binding]
    WebGui  ia.input.button  [1 binding; 1 event]
    Close  ia.display.icon  [1 event]
  Content  ia.container.flex  [2 bindings]
    Tabs  ia.container.flex  [4 bindings]
      Controls  ia.input.button  [6 bindings; 1 event]
      Configuration  ia.input.button  [6 bindings; 1 event]
      Interlocks  ia.input.button  [6 bindings; 1 event]
      Discrete Inputs  ia.input.button  [6 bindings; 1 event]
      Trend  ia.input.button  [6 bindings; 1 event]
      Alarm Configuration  ia.input.button  [6 bindings; 1 event]
      Alarms  ia.input.button  [6 bindings; 1 event]
    Body  ia.container.flex
      EmbeddedView  ia.display.view  [3 bindings; view: (bound)]
```

</details>

## Bindings

62 bindings: expr 50, property 9, expr-struct 3.

<details>
<summary>All 62 bindings, grouped by component</summary>

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
	{view.params.tagPath}!='' && try(isGood(tag({view.params.tagPath} + '.Metadata')), false),
	try(if(!isGood(tag({view.params.tagPath} + '.Metadata')), null, tag({view.params.tagPath} + '.Metadata')), null),
	'')
```


- `custom.tagFlags`: structured expression (expr-struct)

```js
showControls: coalesce({view.params.showControls}, false)
showConfiguration: coalesce({view.params.showConfiguration}, false)
showInterlocks: coalesce({view.params.showInterlocks}, false) && coalesce(try(if(isGood(tag({view.params.tagPath} + '/ShowInterlocks')), toBoolean(tag({view.params.tagPath} + '/ShowInterlocks')), null), null), coalesce({view.params.deviceType}, '') = 'CoolingTower')
showTrend: coalesce({view.params.showTrend}, false)
showAlarmConfiguration: coalesce({view.params.showAlarmConfiguration}, false)
showAlarms: coalesce({view.params.showAlarms}, false)
defaultTab: 'Controls'
```

waitOnAll: `False`


- `custom.visibleTabCount`: expression

```js
(if({view.params.showControls} && {view.custom.tagFlags.showControls}, 1, 0) + if({view.params.showConfiguration} && {view.custom.tagFlags.showConfiguration}, 1, 0) + if({view.params.showInterlocks} && {view.custom.tagFlags.showInterlocks}, 1, 0) + if({view.params.showTrend} && {view.custom.tagFlags.showTrend}, 1, 0) + if({view.params.showAlarmConfiguration} && {view.custom.tagFlags.showAlarmConfiguration}, 1, 0) + if({view.params.showAlarms} && {view.custom.tagFlags.showAlarms}, 1, 0) + if({view.custom.showDiscreteInputs}, 1, 0))
```


- `custom.showDiscreteInputs`: expression

```js
({view.params.deviceType} = 'Tank')
```


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../common-patterns.md#pattern-1).

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform

```js
tagPath: 
```

waitOnAll: `True`

Transform 1, script:

```python
tagPath = ''
try:
    tagPath = self.view.params.tagPath
except:
    pass
if tagPath is None or str(tagPath).strip() == '':
    tagPath = value.tagPath + self.view.id.split('@')[0].split('/')[-1]
items = [
          {
            "text": "Ticket Logger",
            "icon": {
              "path": "material/info",
              "color": "--neutral-80",
              "style": {}
            },
            "style": {
              "classes": "bg-component Fonts/Value",
              "height": 24,
              "width": 120
            },
            "type": "message",
            "children": [],
            "link": {
              "url": "",
              "target": "self"
            },
            "method": {
              "name": "",
              "params": {}
            },
            "message": {
              "type": "ticketLog",
              "payload": {
                "tagPath": tagPath,
                "viewName": self.view.id.split('@')[0], 'sender': self.view.id
              },
              "scope": "page"
            }
          }
        ]
# ... 1 more line(s): see the view.json
```


- `props.style.classes`: expression

```js
if({view.custom.verticalTabs},
   if(({view.custom.selected} = 'Trend' || {view.params.deviceType} = 'Tank' || ({view.params.deviceType} = 'Sensor' && {view.custom.selected} = 'Configuration')),
      'bg-component container-card container-card-border faceplate faceplate-tabs-vertical faceplate-trend-wide',
      'bg-component container-card container-card-border faceplate faceplate-tabs-vertical'),
   if(({view.custom.selected} = 'Trend' || {view.params.deviceType} = 'Tank' || ({view.params.deviceType} = 'Sensor' && {view.custom.selected} = 'Configuration')),
      'bg-component container-card container-card-border faceplate faceplate-trend-wide',
      'bg-component container-card container-card-border faceplate'))
```


**`root/Header/Title`**

- `props.text`: property `view.custom.label`

**`root/Header/WebGui`**

- `meta.visible`: expression

```js
{view.params.deviceType} = 'Compressor' && len(coalesce({view.params.webGuiUrl}, '')) > 0
```


**`root/Content`**

- `props.direction`: expression

```js
if({view.custom.verticalTabs}, 'row', 'column')
```


- `props.style.classes`: expression

```js
if({view.custom.verticalTabs},
   'faceplate-content faceplate-tabs-vertical',
   'faceplate-content')
```


**`root/Content/Tabs`**

- `props.style.classes`: expression

```js
if({view.custom.verticalTabs},
   'faceplate-buttons-' + {view.custom.visibleTabCount} + ' faceplate-tabs-vertical',
   'faceplate-buttons-' + {view.custom.visibleTabCount})
```


- `position.basis`: expression

```js
if({view.custom.verticalTabs}, '144px', '56px')
```


- `props.direction`: expression

```js
if({view.custom.verticalTabs}, 'column', 'row')
```


- `props.alignItems`: expression

```js
if({view.custom.verticalTabs}, 'stretch', 'flex-end')
```


**`root/Content/Tabs/Controls`**

- `position.basis`: expression

```js
if({view.params.showControls} && {view.custom.tagFlags.showControls},
   if({view.custom.verticalTabs}, '68px', '72px'),
   '0px')
```


- `position.grow`: expression

```js
if({view.params.showControls} && {view.custom.tagFlags.showControls},
   if({view.custom.verticalTabs}, 0, 1),
   0)
```


- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.style.display`: expression

```js
if({view.params.showControls} && {view.custom.tagFlags.showControls}, 'flex', 'none')
```


- `props.text`: property `this.meta.name`

- `position.shrink`: expression

```js
if({view.custom.verticalTabs}, 0, 1)
```


**`root/Content/Tabs/Configuration`**

- `position.basis`: expression

```js
if({view.params.showConfiguration} && {view.custom.tagFlags.showConfiguration},
   if({view.custom.verticalTabs}, '68px', '96px'),
   '0px')
```


- `position.grow`: expression

```js
if({view.params.showConfiguration} && {view.custom.tagFlags.showConfiguration},
   if({view.custom.verticalTabs}, 0, 1),
   0)
```


- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.style.display`: expression

```js
if({view.params.showConfiguration} && {view.custom.tagFlags.showConfiguration}, 'flex', 'none')
```


- `props.text`: property `this.meta.name`

- `position.shrink`: expression

```js
if({view.custom.verticalTabs}, 0, 1)
```


**`root/Content/Tabs/Interlocks`**

- `position.basis`: expression

```js
if({view.params.showInterlocks} && {view.custom.tagFlags.showInterlocks},
   if({view.custom.verticalTabs}, '68px', '80px'),
   '0px')
```


- `position.grow`: expression

```js
if({view.params.showInterlocks} && {view.custom.tagFlags.showInterlocks},
   if({view.custom.verticalTabs}, 0, 1),
   0)
```


- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.style.display`: expression

```js
if({view.params.showInterlocks} && {view.custom.tagFlags.showInterlocks}, 'flex', 'none')
```


- `props.text`: property `this.meta.name`

- `position.shrink`: expression

```js
if({view.custom.verticalTabs}, 0, 1)
```


**`root/Content/Tabs/Discrete Inputs`**

- `position.basis`: expression

```js
if({view.custom.showDiscreteInputs},
   if({view.custom.verticalTabs}, '68px', '104px'),
   '0px')
```


- `position.grow`: expression

```js
if({view.custom.showDiscreteInputs},
   if({view.custom.verticalTabs}, 0, 1),
   0)
```


- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.style.display`: expression

```js
if({view.custom.showDiscreteInputs}, 'flex', 'none')
```


- `props.text`: property `this.meta.name`

- `position.shrink`: expression

```js
if({view.custom.verticalTabs}, 0, 1)
```


**`root/Content/Tabs/Trend`**

- `position.basis`: expression

```js
if({view.params.showTrend} && {view.custom.tagFlags.showTrend},
   if({view.custom.verticalTabs}, '68px', '64px'),
   '0px')
```


- `position.grow`: expression

```js
if({view.params.showTrend} && {view.custom.tagFlags.showTrend},
   if({view.custom.verticalTabs}, 0, 1),
   0)
```


- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.style.display`: expression

```js
if({view.params.showTrend} && {view.custom.tagFlags.showTrend}, 'flex', 'none')
```


- `props.text`: property `this.meta.name`

- `position.shrink`: expression

```js
if({view.custom.verticalTabs}, 0, 1)
```


**`root/Content/Tabs/Alarm Configuration`**

- `position.basis`: expression

```js
if({view.params.showAlarmConfiguration} && {view.custom.tagFlags.showAlarmConfiguration},
   if({view.custom.verticalTabs}, '68px', '120px'),
   '0px')
```


- `position.grow`: expression

```js
if({view.params.showAlarmConfiguration} && {view.custom.tagFlags.showAlarmConfiguration},
   if({view.custom.verticalTabs}, 0, 1),
   0)
```


- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.style.display`: expression

```js
if({view.params.showAlarmConfiguration} && {view.custom.tagFlags.showAlarmConfiguration}, 'flex', 'none')
```


- `props.text`: property `this.meta.name`

- `position.shrink`: expression

```js
if({view.custom.verticalTabs}, 0, 1)
```


**`root/Content/Tabs/Alarms`**

- `position.basis`: expression

```js
if({view.params.showAlarms} && {view.custom.tagFlags.showAlarms},
   if({view.custom.verticalTabs}, '68px', '64px'),
   '0px')
```


- `position.grow`: expression

```js
if({view.params.showAlarms} && {view.custom.tagFlags.showAlarms},
   if({view.custom.verticalTabs}, 0, 1),
   0)
```


- `props.style.classes`: expression

```js
if({view.custom.selected} = {this.meta.name},
   'faceplate-button-selected',
   'faceplate-button')
```


- `props.style.display`: expression

```js
if({view.params.showAlarms} && {view.custom.tagFlags.showAlarms}, 'flex', 'none')
```


- `props.text`: property `this.meta.name`

- `position.shrink`: expression

```js
if({view.custom.verticalTabs}, 0, 1)
```


**`root/Content/Body/EmbeddedView`**

- `props.params.hiddenTags`: expression

```js
case(
  {view.custom.selected},
  "Trend", {view.params.hiddenFromTrend},
  "Configuration", {view.params.hiddenFromConfiguration},
  "Alarm Configuration", {view.params.hiddenFromAlarmConfiguration},
  "Alarms", {view.params.hiddenFromAlarms},
  ''
)
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

- `props.path`: expression

```js
case(
  {view.custom.selected},
  "Controls",
    case({view.params.deviceType},
      "Compressor", "01_Popups/00_Faceplates/_Assets/Compressor/Controls",
      "SuctionSequence", "01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls",
      "Pump", "01_Popups/00_Faceplates/_Assets/Pump/Controls",
      "ExhaustFan", "01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls",
      "Valve", "01_Popups/00_Faceplates/_Assets/Valve/Controls",
      "Tank", "01_Popups/00_Faceplates/_Assets/Tank/Controls",
      "Sensor", "01_Popups/00_Faceplates/_Assets/Sensor/Controls",
      "Evaporator", "01_Popups/00_Faceplates/_Assets/Evaporator/Controls",
      "CoolingTower", "01_Popups/00_Faceplates/_Assets/CoolingTower/Controls",
      ""),
  "Configuration", case({view.params.deviceType}, "Valve", "01_Popups/00_Faceplates/_Assets/Valve/Configuration", "Pump", "01_Popups/00_Faceplates/_Assets/Pump/Configuration", "Evaporator", "01_Popups/00_Faceplates/_Assets/Evaporator/Configuration", "Compressor", "01_Popups/00_Faceplates/_Assets/Compressor/Configuration", "Tank", "01_Popups/00_Faceplates/_Assets/Tank/Configuration", "Sensor", "01_Popups/00_Faceplates/_Assets/Sensor/Configuration", "Compressor", "01_Popups/00_Faceplates/_Assets/Compressor/Configuration", "01_Popups/00_Faceplates/_Assets/Configuration/Configuration"),
  "Interlocks", case({view.params.deviceType}, "Valve", "01_Popups/00_Faceplates/_Assets/Valve/Interlocks", "Pump", "01_Popups/00_Faceplates/_Assets/Pump/Interlocks", "Evaporator", "01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks", "Compressor", "01_Popups/00_Faceplates/_Assets/Compressor/Interlocks", "01_Popups/00_Faceplates/_Assets/Interlocks"),
  "Discrete Inputs", "01_Popups/00_Faceplates/_Assets/DiscreteInputs",
  "Trend", "01_Popups/00_Faceplates/_Assets/Trend",
  "Alarm Configuration", "01_Popups/00_Faceplates/_Assets/AlarmConfiguration",
  "Alarms", case({view.params.deviceType}, "Valve", "01_Popups/00_Faceplates/_Assets/Valve/Alarms", "Pump", "01_Popups/00_Faceplates/_Assets/Pump/Alarms", "Sensor", "01_Popups/00_Faceplates/_Assets/Sensor/Alarms", "01_Popups/00_Faceplates/_Assets/Alarms"),
  ""
)
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 14 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
tab = str(self.view.params.initialTab or '').strip()
if tab:
    self.view.custom.selected = tab
```

- **`root/Header/WebGui`** `component.onActionPerformed`, script action, scope `G`

```python
url = str(self.view.params.webGuiUrl or '').strip()
if not url:
    return
system.perspective.navigate(url=url, newTab=True)
```

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
ids = []
popupId = str(self.view.params.popupId or '').strip()
if popupId:
    ids.append(popupId)
tagPath = str(self.view.params.tagPath or '')
label = str(self.view.custom.label or '')
key = tagPath or label
ids.extend([
    'comp-fp-%s' % key,
    'nav-fp-%s' % key,
    'fp-%s' % key,
    'pump-fp-%s' % key,
    'valve-fp-%s' % key,
    'sensor-fp-%s' % key,
    'tank-fp-%s' % key,
    'efan-fp-%s' % key,
    'ev-fp-%s' % key,
    'ct-fp-%s' % key,
    key,
])
leaf = key.split('/')[-1] if key else ''
if leaf and leaf != key:
    ids.extend([
        'comp-fp-%s' % leaf,
        'nav-fp-%s' % leaf,
# ... 12 more line(s): see the view.json
```

- **`root/Content/Tabs/Controls`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Configuration`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Interlocks`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Discrete Inputs`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Trend`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Alarm Configuration`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`root/Content/Tabs/Alarms`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.selected = self.meta.name
```

- **`(view)`** change script on `custom.selected`

```python
# Width is applied in stylesheet via .psc-faceplate-trend-wide on the view root.
# alterPopup is not available in this Ignition version.
pass
```

- **`(view)`** change script on `custom.tagFlags`

```python
flags = currentValue.value
if not flags:
    return
sel = self.custom.selected
visible = {
    'Controls': flags.get('showControls'),
    'Configuration': flags.get('showConfiguration'),
    'Interlocks': flags.get('showInterlocks'),
    'Trend': flags.get('showTrend'),
    'Alarm Configuration': flags.get('showAlarmConfiguration'),
    'Alarms': flags.get('showAlarms'),
}
if not visible.get(sel, False):
    self.custom.selected = flags.get('defaultTab') or 'Controls'
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

- **`root`** message handler `faceplateSelectTab` (scope: page)

```python
# Chip shortcuts inside a tab (e.g. valve INTLK -> Interlocks)
if payload.get('tab') and payload.get('tagPath') == self.view.params.tagPath:
    self.view.custom.selected = payload['tab']
```

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Bound embeds** (view path set by a binding): `root/Content/Body/EmbeddedView`

**Opens or names** (popups, scripts, expressions): [01\_Popups/00\_Faceplates/\_Assets/AlarmConfiguration](./assets/alarmconfiguration.md), [01\_Popups/00\_Faceplates/\_Assets/Alarms](./assets/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Configuration](./assets/compressor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Controls](./assets/compressor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Compressor/Interlocks](./assets/compressor/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Configuration/Configuration](./assets/configuration/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/CoolingTower/Controls](./assets/coolingtower/controls.md), [01\_Popups/00\_Faceplates/\_Assets/DiscreteInputs](./assets/discreteinputs.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Configuration](./assets/evaporator/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Controls](./assets/evaporator/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Evaporator/Interlocks](./assets/evaporator/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/ExhaustFan/Controls](./assets/exhaustfan/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Interlocks](./assets/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Alarms](./assets/pump/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Configuration](./assets/pump/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Controls](./assets/pump/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Pump/Interlocks](./assets/pump/interlocks.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Alarms](./assets/sensor/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Configuration](./assets/sensor/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Sensor/Controls](./assets/sensor/controls.md), [01\_Popups/00\_Faceplates/\_Assets/SuctionSequence/Controls](./assets/suctionsequence/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Configuration](./assets/tank/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Tank/Controls](./assets/tank/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Trend](./assets/trend.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Alarms](./assets/valve/alarms.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Configuration](./assets/valve/configuration.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Controls](./assets/valve/controls.md), [01\_Popups/00\_Faceplates/\_Assets/Valve/Interlocks](./assets/valve/interlocks.md)

**Embedded in** (9): [01\_Popups/00\_Faceplates/Compressor](./compressor.md), [01\_Popups/00\_Faceplates/CoolingTower](./coolingtower.md), [01\_Popups/00\_Faceplates/Evaporator](./evaporator.md), [01\_Popups/00\_Faceplates/ExhaustFan](./exhaustfan.md), [01\_Popups/00\_Faceplates/Pump](./pump.md), [01\_Popups/00\_Faceplates/Sensor](./sensor.md), [01\_Popups/00\_Faceplates/SolenoidValve](./solenoidvalve.md), [01\_Popups/00\_Faceplates/SolenoidValve3Way](./solenoidvalve3way.md), [01\_Popups/00\_Faceplates/Tank](./tank.md)

**Opened or named by** (7): [00\_Pages/Groveport/Utility/Overview](../../00-pages/groveport/utility/overview.md), [02\_Components/01\_Devices/Compressor](../../02-components/01-devices/compressor.md), [02\_Components/01\_Devices/CoolingTower](../../02-components/01-devices/coolingtower.md), [02\_Components/01\_Devices/Evaporator](../../02-components/01-devices/evaporator.md), [02\_Components/01\_Devices/ExhaustFan](../../02-components/01-devices/exhaustfan.md), [02\_Components/01\_Devices/Sensor](../../02-components/01-devices/sensor.md), [02\_Components/01\_Devices/Tank](../../02-components/01-devices/tank.md)

**Named in project scripts**: [shared.Alerts](../../../../../scripting/reference/modules/shared-alerts.md)

## Style Classes

<details>
<summary>20 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `bg-header` | 1 | stylesheet |
| `color-icon` | 1 | style class |
| `container-button` | 1 | style class |
| `container-icon` | 1 | stylesheet |
| `faceplate-body` | 1 | stylesheet |
| `faceplate-close` | 1 | stylesheet |
| `faceplate-content` | 1 | stylesheet |
| `faceplate-header` | 1 | stylesheet |
| `faceplate-title` | 1 | style class |
| `faceplate-webgui` | 1 | stylesheet |
| `bg-component` | bound | stylesheet |
| `container-card` | bound | stylesheet |
| `container-card-border` | bound | stylesheet |
| `faceplate` | bound | stylesheet |
| `faceplate-button` | bound | stylesheet |
| `faceplate-button-selected` | bound | stylesheet |
| `faceplate-tabs-vertical` | bound | stylesheet |
| `faceplate-trend-wide` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.Metadata`, `.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/ShowInterlocks`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
