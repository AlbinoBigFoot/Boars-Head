---
title: "ModuleHover"
sidebar_label: "ModuleHover"
description: "Perspective view 02_Components/03_PLC/ModuleHover (Reusable component): 17 components, 86 bindings, 0 event scripts."
generated: true
keywords: ["02_Components/03_PLC/ModuleHover", "ModuleHover"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/ModuleHover`.

| | |
|---|---|
| View path | `02_Components/03_PLC/ModuleHover` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/ModuleHover/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; ModuleHover |
| Root | `ia.container.flex`, width 340, height 156 |
| Size | 17 components, 86 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `kind` | `""` | input |
| `title` | `""` | input |

## Custom properties

<details>
<summary>29 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `preview` | `"ok"` | bound (expr) |
| `good` | `false` | bound (expr) |
| `fault` | `0` | bound (expr) |
| `state` | `"bad"` | bound (expr) |
| `ch0` | `null` | bound (expr) |
| `unit0` | `""` | bound (expr) |
| `rng0` | `false` | bound (expr) |
| `ch1` | `null` | bound (expr) |
| `unit1` | `""` | bound (expr) |
| `rng1` | `false` | bound (expr) |
| `ch2` | `null` | bound (expr) |
| `unit2` | `""` | bound (expr) |
| `rng2` | `false` | bound (expr) |
| `ch3` | `null` | bound (expr) |
| `unit3` | `""` | bound (expr) |
| `rng3` | `false` | bound (expr) |
| `ch4` | `null` | bound (expr) |
| `unit4` | `""` | bound (expr) |
| `rng4` | `false` | bound (expr) |
| `ch5` | `null` | bound (expr) |
| `unit5` | `""` | bound (expr) |
| `rng5` | `false` | bound (expr) |
| `ch6` | `null` | bound (expr) |
| `unit6` | `""` | bound (expr) |
| `rng6` | `false` | bound (expr) |
| `ch7` | `null` | bound (expr) |
| `unit7` | `""` | bound (expr) |
| `rng7` | `false` | bound (expr) |
| `word` | `0` | bound (expr) |

</details>

## Component Tree

Component types: ia.display.label x13, ia.container.flex x3, ia.shapes.svg x1.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex
  Title  ia.display.label  [1 binding]
  Status  ia.display.label  [2 bindings]
  Grid  ia.shapes.svg  [33 bindings]
  Channels  ia.container.flex  [1 binding]
    Ch0  ia.display.label  [2 bindings]
    Ch1  ia.display.label  [2 bindings]
    Ch2  ia.display.label  [2 bindings]
    Ch3  ia.display.label  [2 bindings]
    Ch4  ia.display.label  [2 bindings]
    Ch5  ia.display.label  [2 bindings]
    Ch6  ia.display.label  [2 bindings]
    Ch7  ia.display.label  [2 bindings]
  Controller  ia.container.flex  [1 binding]
    Mode  ia.display.label  [1 binding]
    Driver  ia.display.label  [1 binding]
    Fault  ia.display.label  [1 binding]
```

</details>

## Bindings

86 bindings: expr 85, property 1.

<details>
<summary>All 86 bindings, grouped by component</summary>

**`(view)`**

- `custom.preview`: expression

```js
lower(trim(coalesce({view.params.state}, 'ok')))
```


- `custom.good`: expression

```js
if(coalesce({view.params.kind}, '') = 'CTRL', coalesce(try(toBoolean(tag({view.params.tagPath} + '/Connected')), false), false), coalesce(try(isGood(tag({view.params.tagPath} + '/Fault')), false), false))
```


- `custom.fault`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Fault')), false), false), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'fault', 1, 0), coalesce(try(toInt(tag({view.params.tagPath} + '/Fault')), 0), 0)), null)
```


- `custom.state`: expression

```js
if(!{view.custom.good}, 'bad', if({view.custom.fault} = -1, 'conn', if({view.custom.fault} != 0, 'fault', 'ok')))
```


- `custom.ch0`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch0En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch0Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 4.0, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch0En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch0Signal')), null), null)), null)
```


- `custom.unit0`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch0Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(0 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch0Unit')), ''), '')), null)
```


- `custom.rng0`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch0OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch0UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch0OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch0UnderRange')), false), false)), null)
```


- `custom.ch1`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch1En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch1Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 8.21, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch1En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch1Signal')), null), null)), null)
```


- `custom.unit1`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch1Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(1 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch1Unit')), ''), '')), null)
```


- `custom.rng1`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch1OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch1UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch1OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch1UnderRange')), false), false)), null)
```


- `custom.ch2`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch2En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch2Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 12.04, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch2En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch2Signal')), null), null)), null)
```


- `custom.unit2`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch2Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(2 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch2Unit')), ''), '')), null)
```


- `custom.rng2`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch2OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch2UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch2OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch2UnderRange')), false), false)), null)
```


- `custom.ch3`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch3En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch3Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 16.38, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch3En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch3Signal')), null), null)), null)
```


- `custom.unit3`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch3Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(3 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch3Unit')), ''), '')), null)
```


- `custom.rng3`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch3OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch3UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch3OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch3UnderRange')), false), false)), null)
```


- `custom.ch4`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch4En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch4Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 2.55, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch4En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch4Signal')), null), null)), null)
```


- `custom.unit4`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch4Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(4 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch4Unit')), ''), '')), null)
```


- `custom.rng4`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch4OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch4UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch4OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch4UnderRange')), false), false)), null)
```


- `custom.ch5`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch5En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch5Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 3.83, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch5En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch5Signal')), null), null)), null)
```


- `custom.unit5`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch5Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(5 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch5Unit')), ''), '')), null)
```


- `custom.rng5`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch5OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch5UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch5OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch5UnderRange')), false), false)), null)
```


- `custom.ch6`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch6En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch6Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 20.6, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch6En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch6Signal')), null), null)), null)
```


- `custom.unit6`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch6Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(6 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch6Unit')), ''), '')), null)
```


- `custom.rng6`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch6OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch6UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', true, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch6OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch6UnderRange')), false), false)), null)
```


- `custom.ch7`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch7En')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch7Signal')), false), false)), if(coalesce({view.params.tagPath}, '') = '', if({view.custom.preview} = 'ok', 4.09, null), if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch7En')), true), true), try(toFloat(tag({view.params.tagPath} + '/Ch7Signal')), null), null)), null)
```


- `custom.unit7`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Ch7Unit')), false), false), if(coalesce({view.params.tagPath}, '') = '', if(7 < 4, 'mA', 'V'), coalesce(try(toStr(tag({view.params.tagPath} + '/Ch7Unit')), ''), '')), null)
```


- `custom.rng7`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/Ch7OverRange')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Ch7UnderRange')), false), false)), if(coalesce({view.params.tagPath}, '') = '', false, coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch7OverRange')), false), false) || coalesce(try(toBoolean(tag({view.params.tagPath} + '/Ch7UnderRange')), false), false)), null)
```


- `custom.word`: expression

```js
if((coalesce(try(isGood(tag({view.params.tagPath} + '/ReadBack')), false), false) || coalesce(try(isGood(tag({view.params.tagPath} + '/Data')), false), false)), if(coalesce({view.params.kind}, '') = 'DO', coalesce(try(toInt(tag({view.params.tagPath} + '/ReadBack')), 0), 0), coalesce(try(toInt(tag({view.params.tagPath} + '/Data')), 0), 0)), null)
```


**`root/Title`**

- `props.text`: property `view.params.title`

**`root/Status`**

- `props.text`: expression

```js
if(coalesce({view.params.kind}, '') = 'CTRL', if({view.custom.good}, 'Controller Connected', 'Comm Loss'), case({view.custom.state}, 'ok', 'Module OK · Fault Word 0', 'fault', 'Module Fault · Fault Word ' + toStr({view.custom.fault}), 'conn', 'Connection Fault', 'No Data'))
```


- `props.style.color`: expression

```js
if(coalesce({view.params.kind}, '') = 'CTRL', if({view.custom.good}, 'var(--sts-run)', 'var(--sts-fault)'), case({view.custom.state}, 'ok', 'var(--sts-run)', 'fault', 'var(--sts-fault)', 'conn', 'var(--sts-fault)', 'var(--neutral-60)'))
```


**`root/Grid`**

- `props.elements[0].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 0) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[1].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 0) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[2].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 1) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[3].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 1) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[4].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 2) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[5].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 2) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[6].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 3) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[7].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 3) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[8].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 4) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[9].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 4) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[10].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 5) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[11].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 5) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[12].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 6) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[13].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 6) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[14].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 7) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[15].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 7) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[16].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 8) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[17].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 8) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[18].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 9) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[19].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 9) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[20].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 10) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[21].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 10) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[22].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 11) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[23].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 11) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[24].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 12) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[25].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 12) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[26].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 13) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[27].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 13) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[28].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 14) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[29].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 14) = 1, 'var(--sts-run)', 'var(--text)')
```


- `props.elements[30].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 15) = 1, 'var(--sts-run)', 'var(--neutral-60)')
```


- `props.elements[31].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && getBit(coalesce({view.custom.word}, 0), 15) = 1, 'var(--sts-run)', 'var(--text)')
```


- `position.display`: expression

```js
coalesce({view.params.kind}, '') = 'DI' || coalesce({view.params.kind}, '') = 'DO'
```


**`root/Channels`**

- `position.display`: expression

```js
coalesce({view.params.kind}, '') = 'AI'
```


**`root/Channels/Ch0`**

- `props.text`: expression

```js
'Ch0  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch0}), numberFormat({view.custom.ch0}, '0.00') + ' ' + coalesce({view.custom.unit0}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch0}), if({view.custom.rng0}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Channels/Ch1`**

- `props.text`: expression

```js
'Ch1  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch1}), numberFormat({view.custom.ch1}, '0.00') + ' ' + coalesce({view.custom.unit1}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch1}), if({view.custom.rng1}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Channels/Ch2`**

- `props.text`: expression

```js
'Ch2  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch2}), numberFormat({view.custom.ch2}, '0.00') + ' ' + coalesce({view.custom.unit2}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch2}), if({view.custom.rng2}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Channels/Ch3`**

- `props.text`: expression

```js
'Ch3  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch3}), numberFormat({view.custom.ch3}, '0.00') + ' ' + coalesce({view.custom.unit3}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch3}), if({view.custom.rng3}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Channels/Ch4`**

- `props.text`: expression

```js
'Ch4  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch4}), numberFormat({view.custom.ch4}, '0.00') + ' ' + coalesce({view.custom.unit4}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch4}), if({view.custom.rng4}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Channels/Ch5`**

- `props.text`: expression

```js
'Ch5  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch5}), numberFormat({view.custom.ch5}, '0.00') + ' ' + coalesce({view.custom.unit5}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch5}), if({view.custom.rng5}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Channels/Ch6`**

- `props.text`: expression

```js
'Ch6  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch6}), numberFormat({view.custom.ch6}, '0.00') + ' ' + coalesce({view.custom.unit6}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch6}), if({view.custom.rng6}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Channels/Ch7`**

- `props.text`: expression

```js
'Ch7  ' + if({view.custom.state} = 'ok' && !isNull({view.custom.ch7}), numberFormat({view.custom.ch7}, '0.00') + ' ' + coalesce({view.custom.unit7}, ''), '--')
```


- `props.style.color`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch7}), if({view.custom.rng7}, 'var(--status-level-warning)', 'var(--text)'), 'var(--neutral-60)')
```


**`root/Controller`**

- `position.display`: expression

```js
coalesce({view.params.kind}, '') = 'CTRL'
```


**`root/Controller/Mode`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Mode')), false), false), 'Mode  ' + coalesce(try(toStr(tag({view.params.tagPath} + '/Mode')), null), '--'), '—')
```


**`root/Controller/Driver`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/Connected')), false), false), 'Driver  ' + if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/Connected')), false), false), 'Connected', 'Disconnected'), '—')
```


**`root/Controller/Fault`**

- `props.text`: expression

```js
if(coalesce(try(isGood(tag({view.params.tagPath} + '/MajorFault')), false), false), 'Major Fault  ' + if(coalesce(try(toBoolean(tag({view.params.tagPath} + '/MajorFault')), false), false), 'Yes', 'No'), '—')
```

</details>

## Related Views

**Embedded in** (1): [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](../../00-pages/groveport/machine-room/utility/plcrack/overview.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `fs-14` | 12 | style class |
| `fs-16` | 1 | style class |
| `fw-600` | 11 | style class |
| `fw-700` | 2 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>46 relative member paths</summary>

`/Ch0En`, `/Ch0OverRange`, `/Ch0Signal`, `/Ch0UnderRange`, `/Ch0Unit`, `/Ch1En`, `/Ch1OverRange`, `/Ch1Signal`, `/Ch1UnderRange`, `/Ch1Unit`, `/Ch2En`, `/Ch2OverRange`, `/Ch2Signal`, `/Ch2UnderRange`, `/Ch2Unit`, `/Ch3En`, `/Ch3OverRange`, `/Ch3Signal`, `/Ch3UnderRange`, `/Ch3Unit`, `/Ch4En`, `/Ch4OverRange`, `/Ch4Signal`, `/Ch4UnderRange`, `/Ch4Unit`, `/Ch5En`, `/Ch5OverRange`, `/Ch5Signal`, `/Ch5UnderRange`, `/Ch5Unit`, `/Ch6En`, `/Ch6OverRange`, `/Ch6Signal`, `/Ch6UnderRange`, `/Ch6Unit`, `/Ch7En`, `/Ch7OverRange`, `/Ch7Signal`, `/Ch7UnderRange`, `/Ch7Unit`, `/Connected`, `/Data`, `/Fault`, `/MajorFault`, `/Mode`, `/ReadBack`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
