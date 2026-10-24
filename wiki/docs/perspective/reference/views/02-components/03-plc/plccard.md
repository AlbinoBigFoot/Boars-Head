---
title: "PlcCard"
sidebar_label: "PlcCard"
description: "Perspective view 02_Components/03_PLC/PlcCard (Reusable component): 48 components, 100 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/03_PLC/PlcCard", "PlcCard"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/PlcCard`.

| | |
|---|---|
| View path | `02_Components/03_PLC/PlcCard` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/PlcCard/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; PlcCard |
| Root | `ia.container.flex`, width 400, height 440 |
| Size | 48 components, 100 bindings, 1 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

<details>
<summary>18 params</summary>

| Name | Default | Notes |
|---|---|---|
| `plcPath` | `""` | input |
| `name` | `""` | input |
| `description` | `""` | input |
| `page` | `""` | input |
| `showDescription` | `null` | input |
| `showCatalog` | `null` | input |
| `showFirmware` | `null` | input |
| `showIp` | `null` | input |
| `showDriver` | `null` | input |
| `showCommLoss` | `null` | input |
| `showMode` | `null` | input |
| `showMajorFault` | `null` | input |
| `showMinorFault` | `null` | input |
| `showIoFault` | `null` | input |
| `showLastFault` | `null` | input |
| `showModuleTypes` | `null` | input |
| `showAlarms` | `null` | input |
| `showRackStrip` | `null` | input |

</details>

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `rack` | `{}` | bound (tag) |
| `alarms` | `null` | bound (expr) |
| `show` | `{"Alarms": true, "Catalog": true, "CommLoss": true, "Description": ...` | |

## Component Tree

Component types: ia.display.label x29, ia.container.flex x18, ia.display.flex-repeater x1.

<details>
<summary>Component tree (48 components)</summary>

```text
root  ia.container.flex  [1 event]
  Head  ia.container.flex
    Titles  ia.container.flex
      Name  ia.display.label  [1 binding]
      Description  ia.display.label  [4 bindings]
    Pill  ia.display.label  [2 bindings]
  Body  ia.container.flex
    RowCatalog  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowFirmware  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowIp  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowDriver  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowCommLoss  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowMode  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowMajorFault  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowMinorFault  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowIoFault  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowLastFault  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowModuleTypes  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RowAlarms  ia.container.flex  [1 binding]
      Key  ia.display.label
      Value  ia.display.label  [5 bindings]
    RackStrip  ia.container.flex  [1 binding]
      Key  ia.display.label
      Health  ia.container.flex
        Leds  ia.display.flex-repeater  [1 binding; view: 02_Components/03_PLC/PlcCardLed]
        Summary  ia.display.label  [3 bindings]
```

</details>

## Bindings

100 bindings: expr 83, property 16, tag 1.

<details>
<summary>All 100 bindings, grouped by component</summary>

**`(view)`**

- `custom.rack`: tag

Mode `indirect`, tag path `{p}/Rack`, references `p` = `{view.params.plcPath}`, fallback delay 2.5 s


- `custom.alarms`: expression, then script transform

```js
now(10000)
```

Transform 1, script:

```python
# active alarms of this PLC (sources under its site instance) - an expression cannot query alarms by path.
# {count, top}: top = the highest-priority active alarm's name
path = str(self.view.params.plcPath or '')
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


- `custom.show.Catalog`: expression

```js
coalesce({view.params.showCatalog}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CatalogNumber.tagType')), false), false))
```


- `custom.show.Firmware`: expression

```js
coalesce({view.params.showFirmware}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorRevision.tagType')), false), false))
```


- `custom.show.Ip`: expression

```js
coalesce({view.params.showIp}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IPAddress.tagType')), false), false))
```


- `custom.show.Driver`: expression

```js
coalesce({view.params.showDriver}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected.tagType')), false), false))
```


- `custom.show.CommLoss`: expression

```js
coalesce({view.params.showCommLoss}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CommLoss.tagType')), false), false))
```


- `custom.show.Mode`: expression

```js
coalesce({view.params.showMode}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Mode.tagType')), false), false))
```


- `custom.show.MajorFault`: expression

```js
coalesce({view.params.showMajorFault}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFault.tagType')), false), false))
```


- `custom.show.MinorFault`: expression

```js
coalesce({view.params.showMinorFault}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorFault.tagType')), false), false))
```


- `custom.show.IoFault`: expression

```js
coalesce({view.params.showIoFault}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IOFault.tagType')), false), false))
```


- `custom.show.LastFault`: expression

```js
coalesce({view.params.showLastFault}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordCode.tagType')), false), false))
```


- `custom.show.ModuleTypes`: expression

```js
coalesce({view.params.showModuleTypes}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Rack.tagType')), false), false))
```


- `custom.show.Alarms`: expression

```js
coalesce({view.params.showAlarms}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected.tagType')), false), false))
```


- `custom.show.Description`: expression

```js
coalesce({view.params.showDescription}, coalesce({view.params.description}, '') != '')
```


- `custom.show.RackStrip`: expression

```js
coalesce({view.params.showRackStrip}, coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Rack.tagType')), false), false))
```


**`root/Head/Titles/Name`**

- `props.text`: property `view.params.name`

**`root/Head/Titles/Description`**

- `props.text`: expression

```js
coalesce({view.params.description}, '')
```


- `position.display`: property `view.custom.show.Description`

- `meta.tooltip.text`: property `view.params.description`

- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Head/Pill`**

- `props.text`: expression

```js
if(!(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)), if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false), 'COMM LOSS', 'NO DATA'), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), 'MAJOR FAULT', if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Mode')), false), false), upper(toStr(tag(coalesce({view.params.plcPath}, '') + '/Mode'))), 'NO DATA')))
```


- `props.style.backgroundColor`: expression

```js
if(!(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)), if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false), 'var(--sts-fault)', 'var(--neutral-60)'), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), 'var(--sts-fault)', if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Run')), false), false), 'var(--sts-run)', 'var(--neutral-60)')))
```


**`root/Body/RowCatalog`**

- `position.display`: property `view.custom.show.Catalog`

**`root/Body/RowCatalog/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ProductName')), false), false) || coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CatalogNumber')), false), false), coalesce(try(if(isGood(tag(coalesce({view.params.plcPath}, '') + '/ProductName')) && len(trim(toStr(tag(coalesce({view.params.plcPath}, '') + '/ProductName')))) > 0, split(trim(toStr(tag(coalesce({view.params.plcPath}, '') + '/ProductName'))), ' ')[0, 0], null), null), try(toStr(tag(coalesce({view.params.plcPath}, '') + '/CatalogNumber')), null), '--'), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ProductName')), false), false) || coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CatalogNumber')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ProductName')), false), false) || coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CatalogNumber')), false), false), 'var(--text)', 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ProductName')), false), false) || coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CatalogNumber')), false), false), toStr(coalesce(try(if(isGood(tag(coalesce({view.params.plcPath}, '') + '/ProductName')) && len(trim(toStr(tag(coalesce({view.params.plcPath}, '') + '/ProductName')))) > 0, split(trim(toStr(tag(coalesce({view.params.plcPath}, '') + '/ProductName'))), ' ')[0, 0], null), null), try(toStr(tag(coalesce({view.params.plcPath}, '') + '/CatalogNumber')), null), '--')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowFirmware`**

- `position.display`: property `view.custom.show.Firmware`

**`root/Body/RowFirmware/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorRevision')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorRevision')), false), false), toStr(tag(coalesce({view.params.plcPath}, '') + '/MajorRevision')) + '.' + toStr(tag(coalesce({view.params.plcPath}, '') + '/MinorRevision')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorRevision')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorRevision')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorRevision')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorRevision')), false), false), 'var(--text)', 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorRevision')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorRevision')), false), false), toStr(toStr(tag(coalesce({view.params.plcPath}, '') + '/MajorRevision')) + '.' + toStr(tag(coalesce({view.params.plcPath}, '') + '/MinorRevision'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowIp`**

- `position.display`: property `view.custom.show.Ip`

**`root/Body/RowIp/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IPAddress')), false), false), toStr(tag(coalesce({view.params.plcPath}, '') + '/IPAddress')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IPAddress')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IPAddress')), false), false), 'var(--text)', 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IPAddress')), false), false), toStr(toStr(tag(coalesce({view.params.plcPath}, '') + '/IPAddress'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowDriver`**

- `position.display`: property `view.custom.show.Driver`

**`root/Body/RowDriver/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false), if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)), 'Connected', 'Disconnected'), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false), if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)), 'var(--sts-run)', 'var(--sts-fault)'), 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false), toStr(if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)), 'Connected', 'Disconnected')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowCommLoss`**

- `position.display`: property `view.custom.show.CommLoss`

**`root/Body/RowCommLoss/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CommLoss')), false), false), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/CommLoss')), false), false), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CommLoss')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CommLoss')), false), false), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/CommLoss')), false), false), 'var(--sts-fault)', 'var(--text)'), 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/CommLoss')), false), false), toStr(if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/CommLoss')), false), false), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowMode`**

- `position.display`: property `view.custom.show.Mode`

**`root/Body/RowMode/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Mode')), false), false), toStr(tag(coalesce({view.params.plcPath}, '') + '/Mode')), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Mode')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Mode')), false), false), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Run')), false), false), 'var(--sts-run)', 'var(--text)'), 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Mode')), false), false), toStr(toStr(tag(coalesce({view.params.plcPath}, '') + '/Mode'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowMajorFault`**

- `position.display`: property `view.custom.show.MajorFault`

**`root/Body/RowMajorFault/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), if(!((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false)), 'var(--neutral-60)', if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), 'var(--sts-fault)', 'var(--text)')), 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), toStr(if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MajorFault')), false), false), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowMinorFault`**

- `position.display`: property `view.custom.show.MinorFault`

**`root/Body/RowMinorFault/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false), if(!((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false)), 'var(--neutral-60)', if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false), 'var(--sts-fault)', 'var(--text)')), 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false), toStr(if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/MinorFault')), false), false), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowIoFault`**

- `position.display`: property `view.custom.show.IoFault`

**`root/Body/RowIoFault/Value`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false), if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false), 'Yes', 'No'), '--')
```


- `props.style.classes`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false), if(!((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false)), 'var(--neutral-60)', if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false), 'var(--sts-fault)', 'var(--text)')), 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false), toStr(if(coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/IOFault')), false), false), 'Yes', 'No')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowLastFault`**

- `position.display`: property `view.custom.show.LastFault`

**`root/Body/RowLastFault/Value`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordType')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordCode')), false), false), 'Type ' + toStr(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordType')) + ' · Code ' + toStr(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordCode')), '--')
```


- `props.style.classes`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordType')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordCode')), false), false), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordType')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordCode')), false), false), 'var(--text)', 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordType')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordCode')), false), false), toStr('Type ' + toStr(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordType')) + ' · Code ' + toStr(tag(coalesce({view.params.plcPath}, '') + '/MajorFaultRecordCode'))), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowModuleTypes`**

- `position.display`: property `view.custom.show.ModuleTypes`

**`root/Body/RowModuleTypes/Value`**

- `props.text`: expression

```js
if(!isNull(try({view.custom.rack.typeSummary}, null)), coalesce(try(toStr({view.custom.rack.typeSummary}), null), '--'), '--')
```


- `props.style.classes`: expression

```js
if(!isNull(try({view.custom.rack.typeSummary}, null)), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(!isNull(try({view.custom.rack.typeSummary}, null)), 'var(--text)', 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(!isNull(try({view.custom.rack.typeSummary}, null)), toStr(coalesce(try(toStr({view.custom.rack.typeSummary}), null), '--')), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RowAlarms`**

- `position.display`: property `view.custom.show.Alarms`

**`root/Body/RowAlarms/Value`**

- `props.text`: expression

```js
if(!isNull(try({view.custom.alarms.count}, null)), toStr(coalesce(try({view.custom.alarms.count}, null), 0)) + if(coalesce(try({view.custom.alarms.top}, null), '') = '', '', ' · ' + {view.custom.alarms.top}), '--')
```


- `props.style.classes`: expression

```js
if(!isNull(try({view.custom.alarms.count}, null)), 'form-label', 'form-label value-bad')
```


- `props.style.color`: expression

```js
if(!isNull(try({view.custom.alarms.count}, null)), if(coalesce(try({view.custom.alarms.count}, null), 0) > 0, 'var(--sts-fault)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `meta.tooltip.text`: expression

```js
if(!isNull(try({view.custom.alarms.count}, null)), toStr(toStr(coalesce(try({view.custom.alarms.count}, null), 0)) + if(coalesce(try({view.custom.alarms.top}, null), '') = '', '', ' · ' + {view.custom.alarms.top})), '')
```


- `meta.tooltip.enabled`: expression

```js
true
```


**`root/Body/RackStrip`**

- `position.display`: property `view.custom.show.RackStrip`

**`root/Body/RackStrip/Health/Leds`**

- `props.instances`: expression

```js
forEach(where(coalesce({view.custom.rack.items}, asList()), it()['kind'] = 'card'), asMap('tagPath', {view.params.plcPath} + '/' + it()['member'], 'label', 'Slot ' + toStr(toInt(it()['slot'])) + ' · ' + coalesce(it()['name'], '') + ' · ' + coalesce(it()['catalog'], ''), 'instanceStyle', asMap('classes', ''), 'instancePosition', asMap('basis', '0px', 'shrink', 1, 'grow', 1)))
```


**`root/Body/RackStrip/Health/Summary`**

- `props.text`: expression

```js
if((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ModulesFaulted')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ModuleCount')), false), false), if(coalesce(try(toInt(tag(coalesce({view.params.plcPath}, '') + '/ModulesFaulted')), 0), 0) > 0, toStr(coalesce(try(toInt(tag(coalesce({view.params.plcPath}, '') + '/ModulesFaulted')), 0), 0)) + ' Faulted · ', '') + toStr(coalesce(try(toInt(tag(coalesce({view.params.plcPath}, '') + '/ModuleCount')), 0), 0) - coalesce(try(toInt(tag(coalesce({view.params.plcPath}, '') + '/ModulesFaulted')), 0), 0)) + ' / ' + toStr(coalesce(try(toInt(tag(coalesce({view.params.plcPath}, '') + '/ModuleCount')), 0), 0)) + ' OK', 'COMM LOSS')
```


- `props.style.classes`: expression

```js
'fs-11 fw-700'
```


- `props.style.color`: expression

```js
if(!((coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.plcPath}, '') + '/Connected')), false), false)) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ModulesFaulted')), false), false) && coalesce(try(isGood(tag(coalesce({view.params.plcPath}, '') + '/ModuleCount')), false), false)), 'var(--sts-fault)', if(coalesce(try(toInt(tag(coalesce({view.params.plcPath}, '') + '/ModulesFaulted')), 0), 0) > 0, 'var(--sts-fault)', 'var(--sts-run)'))
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
# open this PLC's rack page
page = str(self.view.params.page or '')
if not page:
    page = '/operations/plcs/' + str(self.view.params.name or '')
system.perspective.navigate(page=page)
```

## Related Views

**Embeds** (1): [02\_Components/03\_PLC/PlcCardLed](./plccardled.md) (flex repeater)

**Embedded in** (1): [00\_Pages/Groveport/Operations/PlcOverview](../../00-pages/groveport/operations/plcoverview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `faceplate-hover` | 1 | stylesheet |
| `form-card` | 1 | style class |
| `form-label` | 25 | style class |
| `form-section-head` | 1 | style class |
| `form-subtitle` | 1 | style class |
| `form-title` | 1 | style class |
| `fs-11` | 3 | style class |
| `fs-16` | 1 | style class |
| `fw-400` | 13 | style class |
| `fw-700` | 2 | style class |
| `text-muted` | 13 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

- `{p}/Rack`

Member paths appended to a base path in expressions (relative):

<details>
<summary>27 relative member paths</summary>

`/CatalogNumber`, `/CatalogNumber.tagType`, `/CommLoss`, `/CommLoss.tagType`, `/Connected`, `/Connected.tagType`, `/IOFault`, `/IOFault.tagType`, `/IPAddress`, `/IPAddress.tagType`, `/MajorFault`, `/MajorFault.tagType`, `/MajorFaultRecordCode`, `/MajorFaultRecordCode.tagType`, `/MajorFaultRecordType`, `/MajorRevision`, `/MajorRevision.tagType`, `/MinorFault`, `/MinorFault.tagType`, `/MinorRevision`, `/Mode`, `/Mode.tagType`, `/ModuleCount`, `/ModulesFaulted`, `/ProductName`, `/Rack.tagType`, `/Run`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
