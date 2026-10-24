---
title: "SafetyRelay"
sidebar_label: "SafetyRelay"
description: "Perspective view 02_Components/01_Devices/SafetyRelay (Reusable component): 8 components, 66 bindings, 0 event scripts."
generated: true
keywords: ["02_Components/01_Devices/SafetyRelay", "SafetyRelay"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/SafetyRelay`.

| | |
|---|---|
| View path | `02_Components/01_Devices/SafetyRelay` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/SafetyRelay/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; SafetyRelay |
| Root | `ia.container.flex`, width 536, height 404 |
| Size | 8 components, 66 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `label` | `"HLCO Safety Relay"` | input |
| `state` | `"Normal"` | input |
| `input0Name` | `"In 0: LSS HLCO"` | input |
| `input1Name` | `"In 1: HSS HLCO"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | bound (expr) |
| `preview` | `"normal"` | bound (expr) |
| `commLoss` | `false` | bound (expr) |
| `fault` | `false` | bound (expr) |
| `run` | `true` | bound (expr) |
| `pts` | `{"in0": false, "in1": false, "in2": false, "in3": false, "in4": fal...` | |
| `pax` | `""` | bound (expr) |

## Component Tree

Component types: ia.display.label x4, ia.container.flex x2, ia.container.coord x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [2 bindings]
  DeviceLabel  ia.display.label  [1 binding]
  Graphic  ia.container.coord
    Enclosure  ia.shapes.svg  [29 bindings]
  Status  ia.display.label  [2 bindings]
  InputNames  ia.container.flex
    Input0  ia.display.label  [1 binding]
    Input1  ia.display.label  [1 binding]
```

## Bindings

66 bindings: expr 63, property 3.

<details>
<summary>All 66 bindings, grouped by component</summary>

**`(view)`**

- `custom.label`: expression

```js
if(coalesce({view.params.label}, '') != '', {view.params.label}, if(coalesce({view.params.tagPath}, '') = '', '', subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)))
```


- `custom.preview`: expression

```js
lower(trim(coalesce({view.params.state}, 'normal')))
```


- `custom.commLoss`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'comm loss', !isGood(tag({view.params.tagPath} + '/IO/ConnectionFaulted')) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/ConnectionFaulted')), true), true))
```


- `custom.fault`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'fault', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/PlcMajorFault')), false), false))
```


- `custom.run`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/RunMode')), false), false))
```


- `custom.pts.in0`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt00Data')), false), false))
```


- `custom.pts.in1`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal' || {view.custom.preview} = 'fault', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt01Data')), false), false))
```


- `custom.pts.in2`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt02Data')), false), false))
```


- `custom.pts.in3`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt03Data')), false), false))
```


- `custom.pts.in4`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt04Data')), false), false))
```


- `custom.pts.in5`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt05Data')), false), false))
```


- `custom.pts.in6`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt06Data')), false), false))
```


- `custom.pts.in7`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt07Data')), false), false))
```


- `custom.pts.in8`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt08Data')), false), false))
```


- `custom.pts.in9`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt09Data')), false), false))
```


- `custom.pts.out0`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt18Data')), false), false))
```


- `custom.pts.out1`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt19Data')), false), false))
```


- `custom.pts.out2`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt20Data')), false), false))
```


- `custom.pts.out3`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Pt21Data')), false), false))
```


- `custom.pts.out4`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/SOF05')), false), false))
```


- `custom.pts.out5`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/SOF06')), false), false))
```


- `custom.pts.pin0`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2InPt00Data')), false), false))
```


- `custom.pts.pin1`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal' || {view.custom.preview} = 'fault', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2InPt01Data')), false), false))
```


- `custom.pts.pin2`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2InPt02Data')), false), false))
```


- `custom.pts.pin3`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2InPt03Data')), false), false))
```


- `custom.pts.pout0`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2OutPt00Data')), false), false))
```


- `custom.pts.pout1`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} = 'normal', !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2OutPt01Data')), false), false))
```


- `custom.pts.pout2`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2OutPt02Data')), false), false))
```


- `custom.pts.pout3`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', false, !{view.custom.commLoss} && coalesce(try(toBoolean(tag({view.params.tagPath} + '/IO/Plugin2OutPt03Data')), false), false))
```


- `custom.pax`: expression. Common pattern, see [pattern-6](../../../common-patterns.md#pattern-6).

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/DeviceLabel`**

- `props.text`: property `view.custom.label`

**`root/Graphic/Enclosure`**

- `props.elements[2].fill.paint`: expression

```js
if({view.custom.pts.in0}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[3].fill.paint`: expression

```js
if({view.custom.pts.in1}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[4].fill.paint`: expression

```js
if({view.custom.pts.in2}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[5].fill.paint`: expression

```js
if({view.custom.pts.in3}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[6].fill.paint`: expression

```js
if({view.custom.pts.in4}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[7].fill.paint`: expression

```js
if({view.custom.pts.in5}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[8].fill.paint`: expression

```js
if({view.custom.pts.in6}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[9].fill.paint`: expression

```js
if({view.custom.pts.in7}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[10].fill.paint`: expression

```js
if({view.custom.pts.in8}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[11].fill.paint`: expression

```js
if({view.custom.pts.in9}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[13].fill.paint`: expression

```js
if({view.custom.run}, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[14].fill.paint`: expression

```js
if({view.custom.fault}, 'var(--sts-fault)', 'var(--neutral-60)')
```


- `props.elements[15].fill.paint`: expression

```js
if({view.custom.commLoss}, 'var(--sts-fault)', 'var(--sts-run)')
```


- `props.elements[19].fill.paint`: expression

```js
if({view.custom.pts.out0}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[20].fill.paint`: expression

```js
if({view.custom.pts.out1}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[21].fill.paint`: expression

```js
if({view.custom.pts.out2}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[22].fill.paint`: expression

```js
if({view.custom.pts.out3}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[23].fill.paint`: expression

```js
if({view.custom.pts.out4}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[24].fill.paint`: expression

```js
if({view.custom.pts.out5}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[29].fill.paint`: expression

```js
if({view.custom.commLoss}, 'var(--sts-fault)', 'var(--sts-run)')
```


- `props.elements[35].fill.paint`: expression

```js
if({view.custom.pts.pin0}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[36].fill.paint`: expression

```js
if({view.custom.pts.pin1}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[37].fill.paint`: expression

```js
if({view.custom.pts.pin2}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[38].fill.paint`: expression

```js
if({view.custom.pts.pin3}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[40].fill.paint`: expression

```js
if({view.custom.pts.pout0}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[41].fill.paint`: expression

```js
if({view.custom.pts.pout1}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[42].fill.paint`: expression

```js
if({view.custom.pts.pout2}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[43].fill.paint`: expression

```js
if({view.custom.pts.pout3}, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[29].style.classes`: expression

```js
if({view.custom.commLoss}, '', 'led-comm-flash')
```


**`root/Status`**

- `props.text`: expression

```js
if({view.custom.commLoss}, 'COMM LOSS', if({view.custom.fault}, 'FAULT', if({view.custom.run}, 'RUN', 'STOP')))
```


- `props.style.color`: expression

```js
if({view.custom.commLoss} || {view.custom.fault}, 'var(--sts-fault)', if({view.custom.run}, 'var(--sts-run)', 'var(--status-off)'))
```


**`root/InputNames/Input0`**

- `props.text`: property `view.params.input0Name`

**`root/InputNames/Input1`**

- `props.text`: property `view.params.input1Name`

</details>

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (2): [00\_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview](../../00-pages/groveport/machine-room/utility/safetyrelay/overview.md), [98\_Configuration/ComponentPreview/Condenser-SafetyRelay](../../98-configuration/componentpreview/condenser-safetyrelay.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `component` | 1 | stylesheet |
| `device-graphic` | 1 | stylesheet |
| `fs-11` | 3 | style class |
| `fs-12` | 1 | style class |
| `fw-400` | 2 | style class |
| `fw-700` | 2 | style class |
| `label` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>31 relative member paths</summary>

`.TypeId`, `/AIn.Enabled`, `/AInRef.Enabled`, `/DIn.Enabled`, `/IO/ConnectionFaulted`, `/IO/Plugin2InPt00Data`, `/IO/Plugin2InPt01Data`, `/IO/Plugin2InPt02Data`, `/IO/Plugin2InPt03Data`, `/IO/Plugin2OutPt00Data`, `/IO/Plugin2OutPt01Data`, `/IO/Plugin2OutPt02Data`, `/IO/Plugin2OutPt03Data`, `/IO/Pt00Data`, `/IO/Pt01Data`, `/IO/Pt02Data`, `/IO/Pt03Data`, `/IO/Pt04Data`, `/IO/Pt05Data`, `/IO/Pt06Data`, `/IO/Pt07Data`, `/IO/Pt08Data`, `/IO/Pt09Data`, `/IO/Pt18Data`, `/IO/Pt19Data`, `/IO/Pt20Data`, `/IO/Pt21Data`, `/IO/RunMode`, `/IO/SOF05`, `/IO/SOF06`, `/PlcMajorFault`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
