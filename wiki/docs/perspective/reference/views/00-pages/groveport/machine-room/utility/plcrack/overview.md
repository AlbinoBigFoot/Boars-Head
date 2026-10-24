---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview (Page): 23 components, 30 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview", "Overview", "/operations/plcs/:plc", "/plc-rack"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Machine Room &gt; Utility &gt; PlcRack &gt; Overview |
| Routes | `/operations/plcs/:plc` (PLC Rack)<br/>`/plc-rack` (PLC Rack) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 23 components, 30 bindings, 1 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `plc` | `"RCP1"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `plcs` | `{}` | bound (tag) |
| `sitePath` | `"[default]Boars_Head/GrovePort/Machine Room/PLC/RCP1"` | bound (expr) |
| `selected` | `"Controller"` | |
| `hover` | `""` | |
| `rack` | `{}` | bound (tag) |
| `alarms` | `null` | bound (expr) |

## Component Tree

Component types: ia.display.label x10, ia.container.flex x9, ia.display.view x2, ia.input.button x1, ia.display.flex-repeater x1.

<details>
<summary>Component tree (23 components)</summary>

```text
root  ia.container.flex
  Summary  ia.container.flex
    ChipController  ia.container.flex
      Label  ia.display.label
      Value  ia.display.label  [3 bindings]
    ChipDriver  ia.container.flex
      Label  ia.display.label
      Value  ia.display.label  [3 bindings]
    ChipFaulted  ia.container.flex
      Label  ia.display.label
      Value  ia.display.label  [3 bindings]
    ChipAlarms  ia.container.flex
      Label  ia.display.label
      Value  ia.display.label  [3 bindings]
    ChipFaultCode  ia.container.flex
      Label  ia.display.label
      Value  ia.display.label  [3 bindings]
    Spacer  ia.container.flex
    View3d  ia.input.button  [1 event]
  RackHost  ia.container.flex
    Rack  ia.display.flex-repeater  [2 bindings; view: 02_Components/03_PLC/RackSlot]
    Hover  ia.display.view  [6 bindings; view: 02_Components/03_PLC/ModuleHover]
  Detail  ia.display.view  [3 bindings; view: 02_Components/03_PLC/ModuleDetail]
```

</details>

## Bindings

30 bindings: expr 26, tag 2, property 2.

<details>
<summary>All 30 bindings, grouped by component</summary>

**`(view)`**

- `custom.plcs`: tag

Mode `direct`, tag path `[default]_Config/PLCs/List`, fallback delay 2.5 s


- `custom.sitePath`: expression

```js
coalesce(try(toStr(where(coalesce({view.custom.plcs.plcs}, asList()), it()['name'] = if(coalesce({view.params.plc}, '') = '', 'RCP1', {view.params.plc}))[0]['path']), null), '[default]Boars_Head/GrovePort/Machine Room/PLC/' + if(coalesce({view.params.plc}, '') = '', 'RCP1', {view.params.plc}))
```


- `custom.alarms`: expression, then script transform

```js
now(10000)
```

Transform 1, script:

```python
# active alarms of this PLC (sources under its site instance) - an expression cannot query alarms by path.
# {count, top}: top = the highest-priority active alarm's name
path = str(self.view.custom.sitePath or '')
if not path:
    return None
try:
    rel = path.split(']', 1)[-1]
    res = list(system.alarm.queryStatus(source=['*' + rel + '/*'], state=['ActiveUnacked', 'ActiveAcked']))
    top = ''
    if res:
        best = sorted(res, key=lambda a: -a.getPriority().ordinal())[0]
        top = str(best.getName())
    return {'count': len(res), 'top': top}
except:
    return None
```


- `custom.rack`: tag

Mode `indirect`, tag path `{site}/Rack`, references `site` = `{view.custom.sitePath}`, fallback delay 2.5 s


**`root/Summary/ChipController/Value`**

- `props.text`: expression

```js
if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), '—', if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.custom.sitePath} + '/Mode')), false), false), if((coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'No Data', 'Comm Loss'), toStr(tag({view.custom.sitePath} + '/Mode'))))
```


- `props.style.color`: expression

```js
if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'var(--neutral-60)', if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.custom.sitePath} + '/Mode')), false), false), if((coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'var(--neutral-60)', 'var(--sts-fault)'), if(coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Run')), false), false), 'var(--sts-run)', 'var(--text)')))
```


- `props.style.classes`: expression

```js
if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'fs-14 fw-700 value-bad', if((coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.custom.sitePath} + '/Mode')), false), false) || !(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'fs-14 fw-700', 'fs-14 fw-700 value-bad'))
```


**`root/Summary/ChipDriver/Value`**

- `props.text`: expression

```js
if(!coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false), 'No Data', if((coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'Connected', 'Disconnected'))
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'var(--sts-run)', if(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false), 'var(--sts-fault)', 'var(--neutral-60)'))
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false), 'fs-14 fw-700', 'fs-14 fw-700 value-bad')
```


**`root/Summary/ChipFaulted/Value`**

- `props.text`: expression

```js
if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), '—', if(!coalesce(try(isGood(tag({view.custom.sitePath} + '/ModulesFaulted')), false), false), 'No Data', toStr(coalesce(try(toInt(tag({view.custom.sitePath} + '/ModulesFaulted')), 0), 0)) + ' / ' + toStr(coalesce(try(toInt(tag({view.custom.sitePath} + '/ModuleCount')), len(coalesce({view.custom.rack.slots}, asList()))), len(coalesce({view.custom.rack.slots}, asList()))))))
```


- `props.style.color`: expression

```js
if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'var(--neutral-60)', if(!coalesce(try(isGood(tag({view.custom.sitePath} + '/ModulesFaulted')), false), false), 'var(--neutral-60)', if(coalesce(try(toInt(tag({view.custom.sitePath} + '/ModulesFaulted')), 0), 0) > 0, 'var(--sts-fault)', 'var(--sts-run)')))
```


- `props.style.classes`: expression

```js
if(!(coalesce(try(isGood(tag({view.custom.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.custom.sitePath} + '/Connected')), false), false)), 'fs-14 fw-700 value-bad', if(coalesce(try(isGood(tag({view.custom.sitePath} + '/ModulesFaulted')), false), false), 'fs-14 fw-700', 'fs-14 fw-700 value-bad'))
```


**`root/Summary/ChipAlarms/Value`**

- `props.text`: expression

```js
if(isNull(try({view.custom.alarms.count}, null)), '--', toStr({view.custom.alarms.count}) + if(coalesce(try({view.custom.alarms.top}, null), '') = '', '', ' · ' + {view.custom.alarms.top}))
```


- `props.style.color`: expression

```js
if(coalesce(try({view.custom.alarms.count}, null), 0) > 0, 'var(--sts-fault)', 'var(--sts-run)')
```


- `props.style.classes`: expression

```js
if(isNull(try({view.custom.alarms.count}, null)), 'fs-14 fw-700 value-bad', 'fs-14 fw-700')
```


**`root/Summary/ChipFaultCode/Value`**

- `props.text`: expression

```js
coalesce(try(if(isGood(tag({view.custom.sitePath} + '/MajorFaultRecordCode')), toStr(tag({view.custom.sitePath} + '/MajorFaultRecordCode')), null), null), '--')
```


- `props.style.color`: expression

```js
'var(--text)'
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.custom.sitePath} + '/MajorFaultRecordCode')), false), false), 'fs-14 fw-700', 'fs-14 fw-700 value-bad')
```


**`root/RackHost/Rack`**

- `props.style.aspectRatio`: expression

```js
toStr(coalesce(try(toFloat({view.custom.rack.units}), 1260.0), 1260.0)) + ' / 280'
```


- `props.instances`: expression

```js
forEach(coalesce({view.custom.rack.items}, asList()), asMap('tagPath', if(it()['kind'] = 'card', {view.custom.sitePath} + '/' + it()['member'], if(it()['kind'] = 'controller', {view.custom.sitePath}, '')), 'kind', it()['kind'], 'catalog', coalesce(it()['catalog'], ''), 'slot', coalesce(it()['slot'], 0), 'member', coalesce(it()['member'], ''), 'name', coalesce(it()['name'], ''), 'selected', coalesce(it()['member'], '-') = coalesce({view.custom.selected}, ''), 'instanceStyle', asMap('classes', 'plcrack-u' + toStr(it()['units'])), 'instancePosition', asMap('basis', toStr(floor(toFloat(it()['units']) * 1000000 / coalesce(try(toFloat({view.custom.rack.units}), 1260.0), 1260.0)) / 10000.0) + '%', 'shrink', 0, 'grow', 0)))
```


**`root/RackHost/Hover`**

- `position.display`: expression

```js
coalesce({view.custom.hover}, '') != ''
```


- `props.style.height`: expression

```js
case(if(coalesce({view.custom.hover}, '') = 'Controller', 'CTRL', coalesce(try(toStr(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['type']), ''), '')), 'AI', '178px', 'CTRL', '154px', '156px')
```


- `props.params.tagPath`: expression

```js
if(coalesce({view.custom.hover}, '') = 'Controller', {view.custom.sitePath}, {view.custom.sitePath} + '/' + coalesce({view.custom.hover}, ''))
```


- `props.params.kind`: expression

```js
if(coalesce({view.custom.hover}, '') = 'Controller', 'CTRL', coalesce(try(toStr(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['type']), ''), ''))
```


- `props.params.title`: expression

```js
if(coalesce({view.custom.hover}, '') = 'Controller', 'Controller · ' + coalesce(try(toStr({view.custom.rack.controller.name}), null), '') + ' · 1769-L36ERM', 'Slot ' + if(coalesce(try(toInt(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['slot']), 0), 0) < 10, '0', '') + toStr(coalesce(try(toInt(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['slot']), 0), 0)) + ' · ' + coalesce(try(toStr(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['name']), ''), '') + ' · ' + coalesce(try(toStr(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['catalog']), ''), ''))
```


- `props.style.left`: expression

```js
if((coalesce(try(toFloat(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['x']), 0.0), 0.0) + coalesce(try(toFloat(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['units']), 0.0), 0.0) / 2) / coalesce(try(toFloat({view.custom.rack.units}), 1260.0), 1260.0) < 0.5, 'clamp(0px, calc(' + toStr((coalesce(try(toFloat(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['x']), 0.0), 0.0) + coalesce(try(toFloat(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['units']), 0.0), 0.0)) * 100 / coalesce(try(toFloat({view.custom.rack.units}), 1260.0), 1260.0)) + '% + 16px), calc(100% - 340px))', 'clamp(0px, calc(' + toStr(coalesce(try(toFloat(coalesce(try(where(coalesce({view.custom.rack.items}, asList()), coalesce(it()['member'], '') = coalesce({view.custom.hover}, '-'))[0], null), asMap())['x']), 0.0), 0.0) * 100 / coalesce(try(toFloat({view.custom.rack.units}), 1260.0), 1260.0)) + '% - 346px), calc(100% - 340px))')
```


**`root/Detail`**

- `props.params.sitePath`: property `view.custom.sitePath`

- `props.params.member`: property `view.custom.selected`

- `props.style.height`: expression

```js
case(if(coalesce({view.custom.selected}, '') = 'Controller', 'CTRL', coalesce(try(toStr(where(coalesce({view.custom.rack.slots}, asList()), it()['member'] = coalesce({view.custom.selected}, ''))[0]['type']), 'CTRL'), 'CTRL')), 'AI', '188px', 'CTRL', '286px', '284px')
```

</details>

## Event Scripts And Handlers

- **`root/Summary/View3d`** `component.onActionPerformed`, script action, scope `G`

```python
# UI navigation only: the read-only 3D rack page for this PLC
plc = self.view.params.plc or 'RCP1'
system.perspective.navigate('/operations/plcs/%s/3d' % plc)
```

- **`root`** message handler `plcRackSelect` (scope: page)

```python
# module / controller click in the rack -> detail panel (UI state only)
self.view.custom.selected = str(payload.get('member') or 'Controller')
```

- **`root`** message handler `plcRackHover` (scope: page)

```python
# hover popover (UI state only): enter shows it, leave clears it unless another card took over
m = str(payload.get('member') or '')
if payload.get('leave'):
    if self.view.custom.hover == m:
        self.view.custom.hover = ''
else:
    self.view.custom.hover = m
```

## Related Views

**Embeds** (3): [02\_Components/03\_PLC/ModuleDetail](../../../../../02-components/03-plc/moduledetail.md), [02\_Components/03\_PLC/ModuleHover](../../../../../02-components/03-plc/modulehover.md), [02\_Components/03\_PLC/RackSlot](../../../../../02-components/03-plc/rackslot.md) (flex repeater)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `bg-page` | 1 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `fs-11` | 5 | style class |
| `fs-14` | 5 | style class |
| `fw-400` | 5 | style class |
| `fw-700` | 5 | style class |
| `plcrack-host` | 1 | stylesheet |
| `plcrack-rack` | 1 | stylesheet |
| `text-muted` | 5 | style class |
| `value-bad` | bound | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).

## Tags And Data

- `[default]Boars_Head/GrovePort/Machine Room/PLC/`
- `[default]_Config/PLCs/List`
- `{site}/Rack`

Member paths appended to a base path in expressions (relative):

`/Connected`, `/MajorFaultRecordCode`, `/Mode`, `/ModuleCount`, `/ModulesFaulted`, `/Run`

Tag folders and UDTs are documented under [Tags](../../../../../../../../tags/index.md).
