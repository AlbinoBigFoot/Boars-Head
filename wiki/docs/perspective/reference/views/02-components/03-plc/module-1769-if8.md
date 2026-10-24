---
title: "Module_1769_IF8"
sidebar_label: "Module_1769_IF8"
description: "Perspective view 02_Components/03_PLC/Module_1769_IF8 (Reusable component): 2 components, 78 bindings, 3 event scripts."
generated: true
keywords: ["02_Components/03_PLC/Module_1769_IF8", "Module_1769_IF8"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/Module_1769_IF8`.

| | |
|---|---|
| View path | `02_Components/03_PLC/Module_1769_IF8` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/Module_1769_IF8/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; Module\_1769\_IF8 |
| Root | `ia.container.flex`, width 54, height 280 |
| Size | 2 components, 78 bindings, 3 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `slot` | `0` | input |
| `member` | `""` | input |
| `selected` | `false` | input |
| `state` | `"OK"` | input |
| `name` | `""` | input |

## Custom properties

<details>
<summary>28 custom properties</summary>

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

</details>

## Component Tree

Component types: ia.container.flex x1, ia.shapes.svg x1.

```text
root  ia.container.flex  [3 bindings; 3 events]
  Module  ia.shapes.svg  [47 bindings]
```

## Bindings

78 bindings: expr 78.

<details>
<summary>All 78 bindings, grouped by component</summary>

**`(view)`**

- `custom.preview`: expression

```js
lower(trim(coalesce({view.params.state}, 'ok')))
```


- `custom.good`: expression

```js
if(coalesce({view.params.tagPath}, '') = '', {view.custom.preview} != 'bad', coalesce(try(isGood(tag({view.params.tagPath} + '/Fault')) && isGood(tag({view.params.tagPath} + '/Ch0Data')), false), false))
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


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

- `props.style.classes`: expression

```js
if(coalesce({view.params.member}, '') != '', 'faceplate-hover', '')
```


**`root/Module`**

- `props.elements[1].text`: expression

```js
if(coalesce({view.params.slot}, 0) < 10, '0', '') + toStr(coalesce({view.params.slot}, 0))
```


- `props.elements[3].fill.paint`: expression

```js
case({view.custom.state}, 'ok', 'var(--sts-run)', 'fault', 'var(--sts-fault)', 'conn', 'var(--sts-fault)', 'var(--neutral-60)')
```


- `props.elements[6].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch0}), if({view.custom.rng0}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[8].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch0}), coalesce({view.custom.unit0}, ''), '')
```


- `props.elements[9].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch0}), numberFormat({view.custom.ch0}, if(abs({view.custom.ch0}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[9].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch0}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[9].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch0}), 'normal', 'italic')
```


- `props.elements[10].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch1}), if({view.custom.rng1}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[12].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch1}), coalesce({view.custom.unit1}, ''), '')
```


- `props.elements[13].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch1}), numberFormat({view.custom.ch1}, if(abs({view.custom.ch1}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[13].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch1}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[13].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch1}), 'normal', 'italic')
```


- `props.elements[14].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch2}), if({view.custom.rng2}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[16].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch2}), coalesce({view.custom.unit2}, ''), '')
```


- `props.elements[17].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch2}), numberFormat({view.custom.ch2}, if(abs({view.custom.ch2}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[17].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch2}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[17].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch2}), 'normal', 'italic')
```


- `props.elements[18].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch3}), if({view.custom.rng3}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[20].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch3}), coalesce({view.custom.unit3}, ''), '')
```


- `props.elements[21].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch3}), numberFormat({view.custom.ch3}, if(abs({view.custom.ch3}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[21].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch3}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[21].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch3}), 'normal', 'italic')
```


- `props.elements[22].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch4}), if({view.custom.rng4}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[24].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch4}), coalesce({view.custom.unit4}, ''), '')
```


- `props.elements[25].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch4}), numberFormat({view.custom.ch4}, if(abs({view.custom.ch4}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[25].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch4}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[25].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch4}), 'normal', 'italic')
```


- `props.elements[26].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch5}), if({view.custom.rng5}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[28].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch5}), coalesce({view.custom.unit5}, ''), '')
```


- `props.elements[29].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch5}), numberFormat({view.custom.ch5}, if(abs({view.custom.ch5}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[29].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch5}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[29].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch5}), 'normal', 'italic')
```


- `props.elements[30].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch6}), if({view.custom.rng6}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[32].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch6}), coalesce({view.custom.unit6}, ''), '')
```


- `props.elements[33].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch6}), numberFormat({view.custom.ch6}, if(abs({view.custom.ch6}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[33].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch6}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[33].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch6}), 'normal', 'italic')
```


- `props.elements[34].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch7}), if({view.custom.rng7}, 'var(--status-level-warning)', 'var(--sts-run)'), 'var(--neutral-60)')
```


- `props.elements[36].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch7}), coalesce({view.custom.unit7}, ''), '')
```


- `props.elements[37].text`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch7}), numberFormat({view.custom.ch7}, if(abs({view.custom.ch7}) >= 100, '0.0', '0.00')), '--')
```


- `props.elements[37].fill.paint`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch7}), 'var(--text)', 'var(--neutral-60)')
```


- `props.elements[37].style.fontStyle`: expression

```js
if({view.custom.state} = 'ok' && !isNull({view.custom.ch7}), 'normal', 'italic')
```


- `props.elements[41].text`: expression

```js
coalesce({view.params.name}, '')
```


- `props.elements[43].text`: expression

```js
case({view.custom.state}, 'ok', 'OK', 'fault', 'FAULT', 'conn', 'NO CONN', 'NO DATA')
```


- `props.elements[43].fill.paint`: expression

```js
case({view.custom.state}, 'ok', 'var(--sts-run)', 'fault', 'var(--sts-fault)', 'conn', 'var(--sts-fault)', 'var(--neutral-60)')
```


- `props.elements[43].style.fontStyle`: expression

```js
if({view.custom.state} = 'bad', 'italic', 'normal')
```


- `props.elements[44].stroke.paint`: expression

```js
if(coalesce({view.params.selected}, false), 'var(--sts-run)', 'none')
```

</details>

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
# read-only rack: a click only selects the module for the detail panel (page message)
member = str(self.view.params.member or '')
if member:
    system.perspective.sendMessage('plcRackSelect', payload={'member': member}, scope='page')
```

- **`root`** `dom.onMouseEnter`, script action, scope `G`

```python
# hover popover over the rack (UI state only; the page clears it on leave)
m = str(self.view.params.member or '')
if m:
    system.perspective.sendMessage('plcRackHover', payload={'member': m, 'leave': False}, scope='page')
```

- **`root`** `dom.onMouseLeave`, script action, scope `G`

```python
# hover popover over the rack (UI state only; the page clears it on leave)
m = str(self.view.params.member or '')
if m:
    system.perspective.sendMessage('plcRackHover', payload={'member': m, 'leave': True}, scope='page')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

<details>
<summary>42 relative member paths</summary>

`/Ch0Data`, `/Ch0En`, `/Ch0OverRange`, `/Ch0Signal`, `/Ch0UnderRange`, `/Ch0Unit`, `/Ch1En`, `/Ch1OverRange`, `/Ch1Signal`, `/Ch1UnderRange`, `/Ch1Unit`, `/Ch2En`, `/Ch2OverRange`, `/Ch2Signal`, `/Ch2UnderRange`, `/Ch2Unit`, `/Ch3En`, `/Ch3OverRange`, `/Ch3Signal`, `/Ch3UnderRange`, `/Ch3Unit`, `/Ch4En`, `/Ch4OverRange`, `/Ch4Signal`, `/Ch4UnderRange`, `/Ch4Unit`, `/Ch5En`, `/Ch5OverRange`, `/Ch5Signal`, `/Ch5UnderRange`, `/Ch5Unit`, `/Ch6En`, `/Ch6OverRange`, `/Ch6Signal`, `/Ch6UnderRange`, `/Ch6Unit`, `/Ch7En`, `/Ch7OverRange`, `/Ch7Signal`, `/Ch7UnderRange`, `/Ch7Unit`, `/Fault`

</details>

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
