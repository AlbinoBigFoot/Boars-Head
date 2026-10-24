---
title: "ModuleDetail"
sidebar_label: "ModuleDetail"
description: "Perspective view 02_Components/03_PLC/ModuleDetail (Reusable component): 76 components, 88 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/03_PLC/ModuleDetail", "ModuleDetail"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/ModuleDetail`.

| | |
|---|---|
| View path | `02_Components/03_PLC/ModuleDetail` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/ModuleDetail/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; ModuleDetail |
| Root | `ia.container.flex`, width 1100, height 284 |
| Size | 76 components, 88 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `sitePath` | `"[default]Boars_Head/GrovePort/Machine Room/PLC/RCP1"` | input |
| `member` | `"Controller"` | input |
| `inPopup` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `fault` | `null` | bound (expr) |
| `faultGood` | `false` | bound (expr) |
| `rack` | `{}` | bound (tag) |
| `info` | `{}` | bound (expr) |
| `title` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x45, ia.container.flex x28, ia.display.flex-repeater x2, ia.input.button x1.

<details>
<summary>Component tree (76 components)</summary>

```text
root  ia.container.flex
  Header  ia.container.flex
    Titles  ia.container.flex
      Title  ia.display.label  [1 binding]
      Sub  ia.container.flex
        Status  ia.display.label  [4 bindings]
        Desc  ia.display.label  [1 binding]
    PopOut  ia.input.button  [1 binding; 1 event]
  ModulePane  ia.container.flex  [1 binding]
    Left  ia.container.flex
      Head  ia.container.flex
        Point  ia.display.label
        Led  ia.display.label
        Description  ia.display.label
        State  ia.display.label  [1 binding]
        Extra  ia.display.label  [3 bindings]
      Points  ia.display.flex-repeater  [1 binding; view: 02_Components/03_PLC/PointRow]
    Right  ia.container.flex
      Head  ia.container.flex
        Point  ia.display.label
        Led  ia.display.label
        Description  ia.display.label
        State  ia.display.label  [1 binding]
        Extra  ia.display.label  [3 bindings]
      Points  ia.display.flex-repeater  [1 binding; view: 02_Components/03_PLC/PointRow]
  ControllerPane  ia.container.flex  [1 binding]
    Left  ia.container.flex
      Connected  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      Mode  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      KeySwitch  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      CommLoss  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      MajorFault  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      MinorFault  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      IOFault  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      FaultCode  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      Power  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
    Right  ia.container.flex
      ProductName  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      Catalog  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      Revision  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      ProductCode  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      Serial  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      StatusWord  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
      IP  ia.container.flex
        Key  ia.display.label
        Value  ia.display.label  [4 bindings]
```

</details>

## Bindings

88 bindings: expr 86, tag 1, property 1.

<details>
<summary>All 88 bindings, grouped by component</summary>

**`(view)`**

- `custom.rack`: tag

Mode `indirect`, tag path `{site}/Rack`, references `site` = `{view.params.sitePath}`, fallback delay 2.5 s


- `custom.info`: expression

```js
coalesce(try(where(coalesce({view.custom.rack.slots}, asList()), it()['member'] = coalesce({view.params.member}, ''))[0], null), asMap())
```


- `custom.fault`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/' + coalesce({view.params.member}, '') + '/Fault')), false), false), if(coalesce({view.params.member}, '') = 'Controller' || coalesce({view.params.member}, '') = '', null, try(toInt(tag({view.params.sitePath} + '/' + coalesce({view.params.member}, '') + '/Fault')), null)), null)
```


- `custom.faultGood`: expression

```js
!(coalesce({view.params.member}, '') = 'Controller' || coalesce({view.params.member}, '') = '') && coalesce(try(isGood(tag({view.params.sitePath} + '/' + coalesce({view.params.member}, '') + '/Fault')), false), false)
```


- `custom.title`: expression

```js
if(coalesce({view.params.member}, '') = 'Controller' || coalesce({view.params.member}, '') = '', 'Controller · ' + coalesce(try(toStr({view.custom.rack.controller.name}), null), '') + ' (' + coalesce(try(split({view.params.sitePath}, '/')[len(split({view.params.sitePath}, '/')) - 1, 0], ''), '') + ')', 'Slot ' + if(coalesce(try(toInt({view.custom.info}['slot']), 0), 0) < 10, '0', '') + toStr(coalesce(try(toInt({view.custom.info}['slot']), 0), 0)) + ' · ' + coalesce(try(toStr({view.custom.info}['name']), ''), '') + ' · ' + coalesce(try(toStr({view.custom.info}['catalog']), ''), '') + '/' + coalesce(try(toStr({view.custom.info}['series']), ''), ''))
```


**`root/Header/Titles/Title`**

- `props.text`: property `view.custom.title`

**`root/Header/Titles/Sub/Status`**

- `props.text`: expression

```js
if(!{view.custom.faultGood}, 'No Data', if({view.custom.fault} = -1, 'Connection Fault · Fault Word -1', if({view.custom.fault} != 0, 'Module Fault · Fault Word ' + toStr({view.custom.fault}), 'Module OK · Fault Word 0')))
```


- `props.style.color`: expression

```js
if(!{view.custom.faultGood}, 'var(--neutral-60)', if({view.custom.fault} != 0, 'var(--sts-fault)', 'var(--sts-run)'))
```


- `props.style.classes`: expression

```js
if({view.custom.faultGood}, 'fs-11 fw-700', 'fs-11 fw-700 value-bad')
```


- `position.display`: expression

```js
!(coalesce({view.params.member}, '') = 'Controller' || coalesce({view.params.member}, '') = '')
```


**`root/Header/Titles/Sub/Desc`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/IPAddress')), false), false), if(coalesce({view.params.member}, '') = 'Controller' || coalesce({view.params.member}, '') = '', 'CompactLogix 5370 L3 · ' + coalesce(try(toStr(tag({view.params.sitePath} + '/IPAddress')), null), ''), coalesce(try(toStr({view.custom.info}['description']), ''), '') + ' · [' + coalesce(try(split({view.params.sitePath}, '/')[len(split({view.params.sitePath}, '/')) - 1, 0], ''), '') + ']Local:' + toStr(coalesce(try(toInt({view.custom.info}['slot']), 0), 0)) + if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'DO', ':O.Data / I.ReadBack', if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'AI', ':I.Ch0Data - Ch7Data', ':I.Data'))), '—')
```


**`root/Header/PopOut`**

- `position.display`: expression

```js
!coalesce({view.params.inPopup}, false)
```


**`root/ModulePane`**

- `position.display`: expression

```js
!(coalesce({view.params.member}, '') = 'Controller' || coalesce({view.params.member}, '') = '')
```


**`root/ModulePane/Left/Head/State`**

- `props.text`: expression

```js
if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'AI', 'Value', 'State')
```


**`root/ModulePane/Left/Head/Extra`**

- `props.text`: expression

```js
if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'DO', 'Command', 'Range · Raw · Config')
```


- `position.basis`: expression

```js
if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'AI', '200px', '64px')
```


- `position.display`: expression

```js
coalesce(try(toStr({view.custom.info}['type']), ''), '') != 'DI'
```


**`root/ModulePane/Left/Points`**

- `props.instances`: expression

```js
forEach(where(asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), it() >= 0 && it() < (coalesce(try(toInt({view.custom.info}['points']), 0), 0) / 2)), asMap('tagPath', {view.params.sitePath} + '/' + coalesce({view.params.member}, ''), 'point', it(), 'kind', coalesce(try(toStr({view.custom.info}['type']), ''), ''), 'description', coalesce(try(toStr({view.custom.info}['pointNames'][toStr(it())]), null), 'Not Documented'), 'instanceStyle', asMap('classes', ''), 'instancePosition', asMap('basis', '24px', 'shrink', 0, 'grow', 0)))
```


**`root/ModulePane/Right/Head/State`**

- `props.text`: expression

```js
if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'AI', 'Value', 'State')
```


**`root/ModulePane/Right/Head/Extra`**

- `props.text`: expression

```js
if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'DO', 'Command', 'Range · Raw · Config')
```


- `position.basis`: expression

```js
if(coalesce(try(toStr({view.custom.info}['type']), ''), '') = 'AI', '200px', '64px')
```


- `position.display`: expression

```js
coalesce(try(toStr({view.custom.info}['type']), ''), '') != 'DI'
```


**`root/ModulePane/Right/Points`**

- `props.instances`: expression

```js
forEach(where(asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), it() >= (coalesce(try(toInt({view.custom.info}['points']), 0), 0) / 2) && it() < coalesce(try(toInt({view.custom.info}['points']), 0), 0)), asMap('tagPath', {view.params.sitePath} + '/' + coalesce({view.params.member}, ''), 'point', it(), 'kind', coalesce(try(toStr({view.custom.info}['type']), ''), ''), 'description', coalesce(try(toStr({view.custom.info}['pointNames'][toStr(it())]), null), 'Not Documented'), 'instanceStyle', asMap('classes', ''), 'instancePosition', asMap('basis', '24px', 'shrink', 0, 'grow', 0)))
```


**`root/ControllerPane`**

- `position.display`: expression

```js
coalesce({view.params.member}, '') = 'Controller' || coalesce({view.params.member}, '') = ''
```


**`root/ControllerPane/Left/Connected/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false), if(toBoolean(tag({view.params.sitePath} + '/Connected')), 'Connected', 'Disconnected'), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false), toStr(if(toBoolean(tag({view.params.sitePath} + '/Connected')), 'Connected', 'Disconnected')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/Mode/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/Mode')), false), false), toStr(tag({view.params.sitePath} + '/Mode')), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/Mode')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/Mode')), false), false), toStr(toStr(tag({view.params.sitePath} + '/Mode'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/KeySwitch/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/KeySwitch')), false), false), toStr(tag({view.params.sitePath} + '/KeySwitch')), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/KeySwitch')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/KeySwitch')), false), false), toStr(toStr(tag({view.params.sitePath} + '/KeySwitch'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/CommLoss/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/CommLoss')), false), false), if(toBoolean(tag({view.params.sitePath} + '/CommLoss')), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/CommLoss')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/CommLoss')), false), false), toStr(if(toBoolean(tag({view.params.sitePath} + '/CommLoss')), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/MajorFault/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFault')), false), false), if(toBoolean(tag({view.params.sitePath} + '/MajorFault')), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFault')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFault')), false), false), toStr(if(toBoolean(tag({view.params.sitePath} + '/MajorFault')), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/MinorFault/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/MinorFault')), false), false), if(toBoolean(tag({view.params.sitePath} + '/MinorFault')), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/MinorFault')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/MinorFault')), false), false), toStr(if(toBoolean(tag({view.params.sitePath} + '/MinorFault')), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/IOFault/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/IOFault')), false), false), if(toBoolean(tag({view.params.sitePath} + '/IOFault')), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/IOFault')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/IOFault')), false), false), toStr(if(toBoolean(tag({view.params.sitePath} + '/IOFault')), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/FaultCode/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFaultRecordType')), false), false) && coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFaultRecordCode')), false), false), 'Type ' + toStr(tag({view.params.sitePath} + '/MajorFaultRecordType')) + ' · Code ' + toStr(tag({view.params.sitePath} + '/MajorFaultRecordCode')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFaultRecordType')), false), false) && coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFaultRecordCode')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFaultRecordType')), false), false) && coalesce(try(isGood(tag({view.params.sitePath} + '/MajorFaultRecordCode')), false), false), toStr('Type ' + toStr(tag({view.params.sitePath} + '/MajorFaultRecordType')) + ' · Code ' + toStr(tag({view.params.sitePath} + '/MajorFaultRecordCode'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Left/Power/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/PowerSupply')), false), false), toStr(tag({view.params.sitePath} + '/PowerSupply')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/PowerSupply')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/PowerSupply')), false), false), toStr(toStr(tag({view.params.sitePath} + '/PowerSupply'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Right/ProductName/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/ProductName')), false), false), toStr(tag({view.params.sitePath} + '/ProductName')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/ProductName')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/ProductName')), false), false), toStr(toStr(tag({view.params.sitePath} + '/ProductName'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Right/Catalog/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/CatalogNumber')), false), false), toStr(tag({view.params.sitePath} + '/CatalogNumber')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/CatalogNumber')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/CatalogNumber')), false), false), toStr(toStr(tag({view.params.sitePath} + '/CatalogNumber'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Right/Revision/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/MajorRevision')), false), false) && coalesce(try(isGood(tag({view.params.sitePath} + '/MinorRevision')), false), false), toStr(tag({view.params.sitePath} + '/MajorRevision')) + '.' + toStr(tag({view.params.sitePath} + '/MinorRevision')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/MajorRevision')), false), false) && coalesce(try(isGood(tag({view.params.sitePath} + '/MinorRevision')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/MajorRevision')), false), false) && coalesce(try(isGood(tag({view.params.sitePath} + '/MinorRevision')), false), false), toStr(toStr(tag({view.params.sitePath} + '/MajorRevision')) + '.' + toStr(tag({view.params.sitePath} + '/MinorRevision'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Right/ProductCode/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/ProductCode')), false), false), toStr(tag({view.params.sitePath} + '/ProductCode')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/ProductCode')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/ProductCode')), false), false), toStr(toStr(tag({view.params.sitePath} + '/ProductCode'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Right/Serial/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/SerialNumber')), false), false), toStr(tag({view.params.sitePath} + '/SerialNumber')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/SerialNumber')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/SerialNumber')), false), false), toStr(toStr(tag({view.params.sitePath} + '/SerialNumber'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Right/StatusWord/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/Status')), false), false), toStr(tag({view.params.sitePath} + '/Status')), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/Status')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag({view.params.sitePath} + '/Connected')), false), false) && coalesce(try(toBoolean(tag({view.params.sitePath} + '/Connected')), false), false)) && coalesce(try(isGood(tag({view.params.sitePath} + '/Status')), false), false), toStr(toStr(tag({view.params.sitePath} + '/Status'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/ControllerPane/Right/IP/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/IPAddress')), false), false), toStr(tag({view.params.sitePath} + '/IPAddress')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/IPAddress')), false), false), 'fs-12 fw-700', 'fs-12 fw-700 value-bad')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.sitePath} + '/IPAddress')), false), false), toStr(toStr(tag({view.params.sitePath} + '/IPAddress'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```

</details>

## Event Scripts And Handlers

- **`root/Header/PopOut`** `component.onActionPerformed`, script action, scope `G`

```python
# pop this card's detail out as its own faceplate (one popup per card: several can sit side by side)
info = self.view.custom.info
try:
    slot = int(info['slot'] or 0)
except:
    slot = 0
try:
    kind = str(info['type'] or '')
except:
    kind = ''
vw, vh = 0, 0
try:
    vw = int(self.page.props.dimensions.viewport.width or 0)
    vh = int(self.page.props.dimensions.viewport.height or 0)
except:
    pass
member = str(self.view.params.member or 'Controller')
shared.PlcRack.openCard(self.view.params.sitePath, member, slot, 'CTRL' if member == 'Controller' else kind,
    self.view.custom.title, vw, vh)
```

## Related Views

**Embeds** (1): [02\_Components/03\_PLC/PointRow](./pointrow.md) (flex repeater)

**Embedded in** (2): [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](../../00-pages/groveport/machine-room/utility/plcrack/overview.md), [01\_Popups/00\_Faceplates/PlcRack/CardDetail](../../01-popups/00-faceplates/plcrack/carddetail.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `faceplate-cmd-btn` | 1 | style class |
| `fs-11` | 12 | style class |
| `fs-12` | 32 | style class |
| `fs-14` | 1 | style class |
| `fw-400` | 17 | style class |
| `fw-700` | 26 | style class |
| `text-muted` | 17 | style class |
| `value-bad` | bound | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{site}/Rack`

Member paths appended to a base path in expressions (relative):

<details>
<summary>19 relative member paths</summary>

`/CatalogNumber`, `/CommLoss`, `/Connected`, `/Fault`, `/IOFault`, `/IPAddress`, `/KeySwitch`, `/MajorFault`, `/MajorFaultRecordCode`, `/MajorFaultRecordType`, `/MajorRevision`, `/MinorFault`, `/MinorRevision`, `/Mode`, `/PowerSupply`, `/ProductCode`, `/ProductName`, `/SerialNumber`, `/Status`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
