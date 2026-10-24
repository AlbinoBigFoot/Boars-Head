---
title: "Condenser"
sidebar_label: "Condenser"
description: "Perspective view 02_Components/01_Devices/Condenser (Reusable component): 30 components, 56 bindings, 6 event scripts."
generated: true
keywords: ["02_Components/01_Devices/Condenser", "Condenser"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/Condenser`.

| | |
|---|---|
| View path | `02_Components/01_Devices/Condenser` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/Condenser/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; Condenser |
| Root | `ia.container.flex`, width 320, height 190 |
| Size | 30 components, 56 bindings, 6 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `fans` | `3` | input |
| `label` | `""` | input |
| `state` | `"Unknown"` | input |
| `analog` | `true` | input |
| `analogPath` | `""` | input |
| `faceplate` | `null` | input |
| `fanMap` | `[]` | input |
| `fanLabels` | `[]` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | bound (expr) |
| `preview` | `0` | bound (expr) |
| `fanMapList` | `[]` | bound (expr) |
| `fanLabelList` | `[]` | bound (expr) |
| `fanAuto` | `[]` | bound (expr) |
| `fan1` | `{"member": "Fan 1", "path": "", "sts": 0}` | |
| `fan2` | `{"member": "Fan 2", "path": "", "sts": 0}` | |
| `fan3` | `{"member": "Fan 3", "path": "", "sts": 0}` | |
| `fan1Pax` | `""` | bound (expr) |
| `fan2Pax` | `""` | bound (expr) |
| `fan3Pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x7, ia.display.view x7, ia.shapes.svg x5, ia.container.flex x4, ia.container.coord x4, ia.display.icon x3.

<details>
<summary>Component tree (30 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  DeviceLabel  ia.display.label  [1 binding]
  Graphic  ia.container.coord  [1 binding]
    Housing3  ia.shapes.svg  [1 binding]
    Housing2  ia.shapes.svg  [1 binding]
    Fan1  ia.container.coord  [1 binding; 1 event]
      Fan  ia.shapes.svg  [2 bindings]
      Caption  ia.container.flex
        FanLabel  ia.display.label  [1 binding]
        FaceplateIcon  ia.display.icon  [1 binding]
      AlarmHeader  ia.display.view  [1 binding; view: 03_Elements/01_Status/AlarmHeader]
      IconHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/IconHeader]
      FanStatus  ia.display.label  [2 bindings; 1 event]
    Fan2  ia.container.coord  [1 binding; 1 event]
      Fan  ia.shapes.svg  [2 bindings]
      Caption  ia.container.flex
        FanLabel  ia.display.label  [1 binding]
        FaceplateIcon  ia.display.icon  [1 binding]
      AlarmHeader  ia.display.view  [1 binding; view: 03_Elements/01_Status/AlarmHeader]
      IconHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/IconHeader]
      FanStatus  ia.display.label  [2 bindings; 1 event]
    Fan3  ia.container.coord  [2 bindings; 1 event]
      Fan  ia.shapes.svg  [2 bindings]
      Caption  ia.container.flex
        FanLabel  ia.display.label  [1 binding]
        FaceplateIcon  ia.display.icon  [1 binding]
      AlarmHeader  ia.display.view  [1 binding; view: 03_Elements/01_Status/AlarmHeader]
      IconHeader  ia.display.view  [2 bindings; view: 03_Elements/01_Status/IconHeader]
      FanStatus  ia.display.label  [2 bindings; 1 event]
  AnalogValue  ia.display.view  [2 bindings; view: 03_Elements/01_Status/AnalogValue]
```

</details>

## Bindings

56 bindings: expr 48, property 8.

<details>
<summary>All 56 bindings, grouped by component</summary>

**`(view)`**

- `custom.label`: expression

```js
if(coalesce({view.params.label}, '') != '', {view.params.label}, if(coalesce({view.params.tagPath}, '') = '', '', subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)))
```


- `custom.preview`: expression

```js
case(lower(trim(coalesce({view.params.state}, ''))), 'stopped', 1, 'running', 2, 'stopping', 7, 'starting', 8, 'disabled', 33, 'comm loss', -1, 0)
```


- `custom.fanMapList`: expression

```js
if(isNull({view.params.fanMap}), asList(), if(indexOf(typeOf({view.params.fanMap}), '[]') >= 0 || indexOf(typeOf({view.params.fanMap}), 'List') >= 0, forEach({view.params.fanMap}, coalesce(trim(toStr(it())), '')), forEach(split(toStr({view.params.fanMap}), ','), trim(toStr(it()[0])))))
```


- `custom.fanLabelList`: expression

```js
if(isNull({view.params.fanLabels}), asList(), if(indexOf(typeOf({view.params.fanLabels}), '[]') >= 0 || indexOf(typeOf({view.params.fanLabels}), 'List') >= 0, forEach({view.params.fanLabels}, coalesce(trim(toStr(it())), '')), forEach(split(toStr({view.params.fanLabels}), ','), trim(toStr(it()[0])))))
```


- `custom.fanAuto`: expression, then script transform

```js
if(coalesce({view.params.tagPath}, '') = '' || len(where({view.custom.fanMapList}, it() != '')) >= coalesce(try(toInt({view.params.fans}), 3), 3), '', {view.params.tagPath})
```

Transform 1, script:

```python
path = str(value or '').strip()
if not path:
    return []
import re
try:
    results = system.tag.browse(path, {'tagType': 'UdtInstance'}).getResults()
except:
    return []
cands = []
for r in results:
    try:
        cands.append((str(r['name']), str(r['fullPath'])))
    except:
        pass
if not cands:
    return []
qvs = system.tag.readBlocking([p + '.typeId' for n, p in cands])
names = [n for (n, p), qv in zip(cands, qvs) if str(qv.value or '').split(']')[-1].lower() == 'devices/pump']
names.sort(key=lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)])
return names
```


- `custom.fan1.member`: expression

```js
coalesce(if(coalesce(try(toStr({view.custom.fanMapList}[0]), ''), '') != '', coalesce(try(toStr({view.custom.fanMapList}[0]), ''), ''), null), if(coalesce(try(toStr({view.custom.fanAuto}[0]), ''), '') != '', coalesce(try(toStr({view.custom.fanAuto}[0]), ''), ''), null), 'Fan 1')
```


- `custom.fan1.path`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', if(coalesce(try(isGood(tag({view.params.tagPath} + '/' + {view.custom.fan1.member} + '.tagType')), false), false), {view.params.tagPath} + '/' + {view.custom.fan1.member}, ''))
```


- `custom.fan1.sts`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview}, if({view.custom.fan1.path} = '', -2, if(coalesce(try(!isGood(tag({view.custom.fan1.path} + '/Motor/Val_Sts')), true), true), -1, coalesce(try(toInt(tag({view.custom.fan1.path} + '/Motor/Val_Sts')), 0), 0))))
```


- `custom.fan2.member`: expression

```js
coalesce(if(coalesce(try(toStr({view.custom.fanMapList}[1]), ''), '') != '', coalesce(try(toStr({view.custom.fanMapList}[1]), ''), ''), null), if(coalesce(try(toStr({view.custom.fanAuto}[1]), ''), '') != '', coalesce(try(toStr({view.custom.fanAuto}[1]), ''), ''), null), 'Fan 2')
```


- `custom.fan2.path`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', if(coalesce(try(isGood(tag({view.params.tagPath} + '/' + {view.custom.fan2.member} + '.tagType')), false), false), {view.params.tagPath} + '/' + {view.custom.fan2.member}, ''))
```


- `custom.fan2.sts`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview}, if({view.custom.fan2.path} = '', -2, if(coalesce(try(!isGood(tag({view.custom.fan2.path} + '/Motor/Val_Sts')), true), true), -1, coalesce(try(toInt(tag({view.custom.fan2.path} + '/Motor/Val_Sts')), 0), 0))))
```


- `custom.fan3.member`: expression

```js
coalesce(if(coalesce(try(toStr({view.custom.fanMapList}[2]), ''), '') != '', coalesce(try(toStr({view.custom.fanMapList}[2]), ''), ''), null), if(coalesce(try(toStr({view.custom.fanAuto}[2]), ''), '') != '', coalesce(try(toStr({view.custom.fanAuto}[2]), ''), ''), null), 'Fan 3')
```


- `custom.fan3.path`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', '', if(coalesce(try(isGood(tag({view.params.tagPath} + '/' + {view.custom.fan3.member} + '.tagType')), false), false), {view.params.tagPath} + '/' + {view.custom.fan3.member}, ''))
```


- `custom.fan3.sts`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview}, if({view.custom.fan3.path} = '', -2, if(coalesce(try(!isGood(tag({view.custom.fan3.path} + '/Motor/Val_Sts')), true), true), -1, coalesce(try(toInt(tag({view.custom.fan3.path} + '/Motor/Val_Sts')), 0), 0))))
```


- `custom.fan1Pax`: expression

```js
if(coalesce({view.custom.fan1.path}, '') = '', '', case(toStr(coalesce(try(tag({view.custom.fan1.path} + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.custom.fan1.path} + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.custom.fan1.path} + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.custom.fan1.path} + '/DIn.Enabled')), false), false), 'DIn', ''), ''))
```


- `custom.fan2Pax`: expression

```js
if(coalesce({view.custom.fan2.path}, '') = '', '', case(toStr(coalesce(try(tag({view.custom.fan2.path} + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.custom.fan2.path} + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.custom.fan2.path} + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.custom.fan2.path} + '/DIn.Enabled')), false), false), 'DIn', ''), ''))
```


- `custom.fan3Pax`: expression

```js
if(coalesce({view.custom.fan3.path}, '') = '', '', case(toStr(coalesce(try(tag({view.custom.fan3.path} + '.TypeId'), ''), '')), 'Devices/Pump', 'Motor', 'Devices/Valve', 'Valve', 'Devices/Tank', 'Tank', 'Devices/Compressor', 'Comp', 'Devices/Evaporator', 'CG', 'Devices/ExhaustFan', 'EF', 'Devices/LTU', 'LTU', 'Devices/SafetyRelay', 'Relay', 'Devices/SuctionSequence', 'Seq', 'Devices/DischargeSequence', 'Dsq', 'Devices/Sensor', if(coalesce(try(toBoolean(tag({view.custom.fan3.path} + '/AIn.Enabled')), false), false), 'AIn', if(coalesce(try(toBoolean(tag({view.custom.fan3.path} + '/AInRef.Enabled')), false), false), 'AInRef', '')), 'Devices/DiscreteInput', if(coalesce(try(toBoolean(tag({view.custom.fan3.path} + '/DIn.Enabled')), false), false), 'DIn', ''), ''))
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/DeviceLabel`**

- `props.text`: property `view.custom.label`

**`root/Graphic`**

- `props.style.width`: expression

```js
if(coalesce(try(toInt({view.params.fans}), 3), 3) >= 3, '304px', '208px')
```


**`root/Graphic/Housing3`**

- `meta.visible`: expression

```js
coalesce(try(toInt({view.params.fans}), 3), 3) >= 3
```


**`root/Graphic/Housing2`**

- `meta.visible`: expression

```js
coalesce(try(toInt({view.params.fans}), 3), 3) < 3
```


**`root/Graphic/Fan1`**

- `props.style.classes`: expression

```js
if(coalesce({session.custom.CanOpenFaceplates}, false) && coalesce({view.params.faceplate}, '') != '' && coalesce({view.custom.fan1.path}, '') != '', 'faceplate-hover', '')
```


**`root/Graphic/Fan1/Fan`**

- `props.style.classes`: expression

```js
if({view.custom.fan1.sts} = -1, 'device-comm-loss', if({view.custom.fan1.sts} = 2 || {view.custom.fan1.sts} = 8, 'fan-spin', ''))
```


- `props.style.opacity`: expression

```js
if({view.custom.fan1.sts} = -2, 0.4, 1)
```


**`root/Graphic/Fan1/Caption/FanLabel`**

- `props.text`: expression

```js
coalesce(if(coalesce(try(toStr({view.custom.fanLabelList}[0]), ''), '') != '', coalesce(try(toStr({view.custom.fanLabelList}[0]), ''), ''), null), {view.custom.fan1.member})
```


**`root/Graphic/Fan1/Caption/FaceplateIcon`**

- `props.style.opacity`: expression

```js
if(isNull({view.params.faceplate}) || {view.custom.fan1.path} = '', 0, 1)
```


**`root/Graphic/Fan1/AlarmHeader`**

- `props.params.tagPath`: property `view.custom.fan1.path`

**`root/Graphic/Fan1/IconHeader`**

- `props.params.tagPath`: property `view.custom.fan1.path`

- `props.params.statusPath`: expression

```js
if({view.custom.fan1.path} = '', '', {view.custom.fan1.path} + '/Motor/Val_Sts')
```


**`root/Graphic/Fan1/FanStatus`**

- `props.text`: expression

```js
case({view.custom.fan1.sts}, -2, 'NO TAG', -1, 'COMM LOSS', 1, 'STOP', 2, 'RUN', 7, 'STOPPING', 8, 'STARTING', 33, 'DISABLED', 'UNK')
```


- `props.style.color`: expression

```js
case({view.custom.fan1.sts}, -2, 'var(--text-muted)', -1, 'var(--sts-fault)', 1, 'var(--status-off)', 2, 'var(--sts-run)', 'var(--status-unknown)')
```


**`root/Graphic/Fan2`**

- `props.style.classes`: expression

```js
if(coalesce({session.custom.CanOpenFaceplates}, false) && coalesce({view.params.faceplate}, '') != '' && coalesce({view.custom.fan2.path}, '') != '', 'faceplate-hover', '')
```


**`root/Graphic/Fan2/Fan`**

- `props.style.classes`: expression

```js
if({view.custom.fan2.sts} = -1, 'device-comm-loss', if({view.custom.fan2.sts} = 2 || {view.custom.fan2.sts} = 8, 'fan-spin', ''))
```


- `props.style.opacity`: expression

```js
if({view.custom.fan2.sts} = -2, 0.4, 1)
```


**`root/Graphic/Fan2/Caption/FanLabel`**

- `props.text`: expression

```js
coalesce(if(coalesce(try(toStr({view.custom.fanLabelList}[1]), ''), '') != '', coalesce(try(toStr({view.custom.fanLabelList}[1]), ''), ''), null), {view.custom.fan2.member})
```


**`root/Graphic/Fan2/Caption/FaceplateIcon`**

- `props.style.opacity`: expression

```js
if(isNull({view.params.faceplate}) || {view.custom.fan2.path} = '', 0, 1)
```


**`root/Graphic/Fan2/AlarmHeader`**

- `props.params.tagPath`: property `view.custom.fan2.path`

**`root/Graphic/Fan2/IconHeader`**

- `props.params.tagPath`: property `view.custom.fan2.path`

- `props.params.statusPath`: expression

```js
if({view.custom.fan2.path} = '', '', {view.custom.fan2.path} + '/Motor/Val_Sts')
```


**`root/Graphic/Fan2/FanStatus`**

- `props.text`: expression

```js
case({view.custom.fan2.sts}, -2, 'NO TAG', -1, 'COMM LOSS', 1, 'STOP', 2, 'RUN', 7, 'STOPPING', 8, 'STARTING', 33, 'DISABLED', 'UNK')
```


- `props.style.color`: expression

```js
case({view.custom.fan2.sts}, -2, 'var(--text-muted)', -1, 'var(--sts-fault)', 1, 'var(--status-off)', 2, 'var(--sts-run)', 'var(--status-unknown)')
```


**`root/Graphic/Fan3`**

- `props.style.classes`: expression

```js
if(coalesce({session.custom.CanOpenFaceplates}, false) && coalesce({view.params.faceplate}, '') != '' && coalesce({view.custom.fan3.path}, '') != '', 'faceplate-hover', '')
```


- `meta.visible`: expression

```js
coalesce(try(toInt({view.params.fans}), 3), 3) >= 3
```


**`root/Graphic/Fan3/Fan`**

- `props.style.classes`: expression

```js
if({view.custom.fan3.sts} = -1, 'device-comm-loss', if({view.custom.fan3.sts} = 2 || {view.custom.fan3.sts} = 8, 'fan-spin', ''))
```


- `props.style.opacity`: expression

```js
if({view.custom.fan3.sts} = -2, 0.4, 1)
```


**`root/Graphic/Fan3/Caption/FanLabel`**

- `props.text`: expression

```js
coalesce(if(coalesce(try(toStr({view.custom.fanLabelList}[2]), ''), '') != '', coalesce(try(toStr({view.custom.fanLabelList}[2]), ''), ''), null), {view.custom.fan3.member})
```


**`root/Graphic/Fan3/Caption/FaceplateIcon`**

- `props.style.opacity`: expression

```js
if(isNull({view.params.faceplate}) || {view.custom.fan3.path} = '', 0, 1)
```


**`root/Graphic/Fan3/AlarmHeader`**

- `props.params.tagPath`: property `view.custom.fan3.path`

**`root/Graphic/Fan3/IconHeader`**

- `props.params.tagPath`: property `view.custom.fan3.path`

- `props.params.statusPath`: expression

```js
if({view.custom.fan3.path} = '', '', {view.custom.fan3.path} + '/Motor/Val_Sts')
```


**`root/Graphic/Fan3/FanStatus`**

- `props.text`: expression

```js
case({view.custom.fan3.sts}, -2, 'NO TAG', -1, 'COMM LOSS', 1, 'STOP', 2, 'RUN', 7, 'STOPPING', 8, 'STARTING', 33, 'DISABLED', 'UNK')
```


- `props.style.color`: expression

```js
case({view.custom.fan3.sts}, -2, 'var(--text-muted)', -1, 'var(--sts-fault)', 1, 'var(--status-off)', 2, 'var(--sts-run)', 'var(--status-unknown)')
```


**`root/AnalogValue`**

- `props.params.tagPath`: property `view.params.analogPath`

- `meta.visible`: expression

```js
coalesce({view.params.analog}, true)
```

</details>

## Event Scripts And Handlers

- **`root/Graphic/Fan1`** `dom.onClick`, script action, scope `G`

```python
if not self.view.params.faceplate:
    return
path = str(self.view.custom.fan1.path or '')
if not path:
    return
name = str(self.view.custom.label or '')
title = ('%s %s' % (name, self.view.custom.fan1.member)).strip()
# each condenser fan is a P_Motor: same typed Controls as the pumps
shared.Alerts.showFaceplate(
    tagPath=path,
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

- **`root/Graphic/Fan1/FanStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.fan1.path}/Motor/Val_Sts')
```

- **`root/Graphic/Fan2`** `dom.onClick`, script action, scope `G`

```python
if not self.view.params.faceplate:
    return
path = str(self.view.custom.fan2.path or '')
if not path:
    return
name = str(self.view.custom.label or '')
title = ('%s %s' % (name, self.view.custom.fan2.member)).strip()
# each condenser fan is a P_Motor: same typed Controls as the pumps
shared.Alerts.showFaceplate(
    tagPath=path,
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

- **`root/Graphic/Fan2/FanStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.fan2.path}/Motor/Val_Sts')
```

- **`root/Graphic/Fan3`** `dom.onClick`, script action, scope `G`

```python
if not self.view.params.faceplate:
    return
path = str(self.view.custom.fan3.path or '')
if not path:
    return
name = str(self.view.custom.label or '')
title = ('%s %s' % (name, self.view.custom.fan3.member)).strip()
# each condenser fan is a P_Motor: same typed Controls as the pumps
shared.Alerts.showFaceplate(
    tagPath=path,
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

- **`root/Graphic/Fan3/FanStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '{view.custom.fan3.path}/Motor/Val_Sts')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embeds** (3): [03\_Elements/01\_Status/AlarmHeader](../../03-elements/01-status/alarmheader.md), [03\_Elements/01\_Status/AnalogValue](../../03-elements/01-status/analogvalue.md), [03\_Elements/01\_Status/IconHeader](../../03-elements/01-status/iconheader.md)

**Embedded in** (3): [00\_Pages/Groveport/Condensers/Utility/CondenserFans/Design](../../00-pages/groveport/condensers/utility/condenserfans/design.md), [00\_Pages/Groveport/Condensers/Utility/Overview](../../00-pages/groveport/condensers/utility/overview.md), [98\_Configuration/ComponentPreview/Condenser-SafetyRelay](../../98-configuration/componentpreview/condenser-safetyrelay.md)

## Style Classes

<details>
<summary>13 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `alarm-header` | 3 | stylesheet |
| `component` | 1 | stylesheet |
| `device-graphic` | 1 | stylesheet |
| `device-vertical` | 1 | stylesheet |
| `fs-11` | 7 | style class |
| `fw-600` | 3 | style class |
| `fw-700` | 4 | style class |
| `icon-header` | 3 | style class |
| `label` | 1 | stylesheet |
| `value` | 1 | stylesheet |
| `device-comm-loss` | bound | stylesheet |
| `fan-spin` | bound | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`.TypeId`, `.tagType`, `.typeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/Motor/Val_Sts`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
