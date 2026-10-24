---
title: "PlcOverview"
sidebar_label: "PlcOverview"
description: "Perspective view 00_Pages/Groveport/Operations/PlcOverview (Page): 5 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/PlcOverview", "PlcOverview", "/operations/plcs"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Operations/PlcOverview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/PlcOverview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/PlcOverview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; PlcOverview |
| Routes | `/operations/plcs` (PLCs) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 5 components, 3 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `list` | `{}` | bound (tag) |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x2, ia.display.flex-repeater x1.

```text
root  ia.container.flex
  Header  ia.container.flex
    Title  ia.display.label
    Subtitle  ia.display.label  [1 binding]
  Cards  ia.display.flex-repeater  [1 binding; view: 02_Components/03_PLC/PlcCard]
```

## Bindings

3 bindings: expr 2, tag 1.

**`(view)`**

- `custom.list`: tag

Mode `direct`, tag path `[default]_Config/PLCs/List`, fallback delay 2.5 s


**`root/Header/Subtitle`**

- `props.text`: expression

```js
toStr(len(coalesce({view.custom.list.plcs}, asList()))) + if(len(coalesce({view.custom.list.plcs}, asList())) = 1, ' PLC', ' PLCs') + ' · Click A Card For Its Rack'
```


**`root/Cards`**

- `props.instances`: expression

```js
forEach(coalesce({view.custom.list.plcs}, asList()), asMap('plcPath', it()['path'], 'name', coalesce(it()['name'], ''), 'description', coalesce(it()['description'], '') + if(coalesce(it()['location'], '') = '', '', ' · ' + it()['location']), 'page', coalesce(it()['page'], ''), 'showDescription', try(it()['show']['Description'], null), 'showCatalog', try(it()['show']['Catalog'], null), 'showFirmware', try(it()['show']['Firmware'], null), 'showIp', try(it()['show']['Ip'], null), 'showDriver', try(it()['show']['Driver'], null), 'showCommLoss', try(it()['show']['CommLoss'], null), 'showMode', try(it()['show']['Mode'], null), 'showMajorFault', try(it()['show']['MajorFault'], null), 'showMinorFault', try(it()['show']['MinorFault'], null), 'showIoFault', try(it()['show']['IoFault'], null), 'showLastFault', try(it()['show']['LastFault'], null), 'showModuleTypes', try(it()['show']['ModuleTypes'], null), 'showAlarms', try(it()['show']['Alarms'], null), 'showRackStrip', try(it()['show']['RackStrip'], null), 'instanceStyle', asMap('classes', '', 'height', '440px'), 'instancePosition', asMap('basis', '400px', 'shrink', 0, 'grow', 0)))
```


## Related Views

**Embeds** (1): [02\_Components/03\_PLC/PlcCard](../../../02-components/03-plc/plccard.md) (flex repeater)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `form-subtitle` | 1 | style class |
| `form-title` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/PLCs/List`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
