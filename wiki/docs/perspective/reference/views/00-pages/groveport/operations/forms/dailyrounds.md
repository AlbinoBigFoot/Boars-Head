---
title: "DailyRounds"
sidebar_label: "DailyRounds"
description: "Perspective view 00_Pages/Groveport/Operations/Forms/DailyRounds (Page): 450 components, 402 bindings, 8 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/Forms/DailyRounds", "DailyRounds", "/operations/forms/daily-rounds"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Operations/Forms/DailyRounds`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/Forms/DailyRounds` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/Forms/DailyRounds/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; Forms &gt; DailyRounds |
| Routes | `/operations/forms/daily-rounds` (Daily Rounds Log) |
| Root | `ia.container.flex`, height 1000, width 1600 |
| Size | 450 components, 402 bindings, 8 event handlers, 0 change scripts, 3 message handlers |
| Last saved | 2026-10-23T18:53:37Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `readOnly` | `false` | input |
| `submissionId` | `0` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `attempted` | `false` | |
| `avg_probe` | `""` | bound (expr) |
| `avg_therm` | `""` | bound (expr) |
| `f` | `{"comp1_discharge": "", "comp1_fla": "", "comp1_hours": "", "comp1_...` | |
| `locked` | `false` | bound (expr) |
| `meta` | `""` | |
| `missing` | `""` | bound (expr) |
| `missingCount` | `0` | bound (expr) |
| `missingRaw` | `""` | bound (expr) |
| `msg` | `""` | |
| `operators` | `[]` | |
| `result` | `{"id": 0, "message": "", "ok": false}` | |

## Component Tree

Component types: ia.container.flex x149, ia.input.text-field x133, ia.display.label x112, ia.input.dropdown x46, ia.input.button x7, ia.input.checkbox x2, ia.input.date-time-input x1.

<details>
<summary>Component tree (450 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  Scroll  ia.container.flex
    Form  ia.container.flex
      Header  ia.container.flex
        TitleBlock  ia.container.flex
          Title  ia.display.label
          SubRow  ia.container.flex
            Subtitle  ia.display.label  [1 binding]
            Dot  ia.display.label  [1 binding]
            Legend  ia.display.label  [1 binding]
            LegendText  ia.display.label  [1 binding]
        NameDate  ia.container.flex
          Name  ia.container.flex
            Caption  ia.container.flex
              Label  ia.display.label
              Req  ia.display.label
            V  ia.input.dropdown  [4 bindings]
          Date  ia.container.flex
            Caption  ia.container.flex
              Label  ia.display.label
              Req  ia.display.label
            V  ia.input.date-time-input  [3 bindings]
      Denied  ia.container.flex  [1 binding]
        DeniedMsg  ia.display.label
      Summary  ia.container.flex  [1 binding]
        Title  ia.display.label
        List  ia.display.label  [1 binding]
      Result  ia.display.label  [2 bindings]
      Message  ia.display.label  [2 bindings]
      Sections  ia.container.flex  [1 binding]
        Compressors  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            Table  ia.container.flex
              Head  ia.container.flex
                RowHead  ia.display.label
                H_suction  ia.container.flex
                  Text  ia.display.label
                H_discharge  ia.container.flex
                  Text  ia.display.label
                H_fla  ia.container.flex
                  Text  ia.display.label
                H_hours  ia.container.flex
                  Text  ia.display.label
                H_slide  ia.container.flex
                  Text  ia.display.label
                H_ratio  ia.container.flex
                  Text  ia.display.label
                H_oil  ia.container.flex
                  Text  ia.display.label
              comp1  ia.container.flex
                RowLabel  ia.display.label
                suction  ia.input.text-field  [2 bindings]
                discharge  ia.input.text-field  [2 bindings]
                fla  ia.input.text-field  [2 bindings]
                hours  ia.input.text-field  [2 bindings]
                slide  ia.input.text-field  [2 bindings]
                ratio  ia.input.text-field  [2 bindings]
                oil  ia.input.text-field  [2 bindings]
              comp4  ia.container.flex
                RowLabel  ia.display.label
                suction  ia.input.text-field  [2 bindings]
                discharge  ia.input.text-field  [2 bindings]
                fla  ia.input.text-field  [2 bindings]
                hours  ia.input.text-field  [2 bindings]
                slide  ia.input.text-field  [2 bindings]
                ratio  ia.input.text-field  [2 bindings]
                oil  ia.input.text-field  [2 bindings]
              comp5  ia.container.flex
                RowLabel  ia.display.label
                suction  ia.input.text-field  [2 bindings]
                discharge  ia.input.text-field  [2 bindings]
                fla  ia.input.text-field  [2 bindings]
                hours  ia.input.text-field  [2 bindings]
                slide  ia.input.text-field  [2 bindings]
                ratio  ia.input.text-field  [2 bindings]
                oil  ia.input.text-field  [2 bindings]
              comp6  ia.container.flex
                RowLabel  ia.display.label
                suction  ia.input.text-field  [2 bindings]
                discharge  ia.input.text-field  [2 bindings]
                fla  ia.input.text-field  [2 bindings]
                hours  ia.input.text-field  [2 bindings]
                slide  ia.input.text-field  [2 bindings]
                ratio  ia.input.text-field  [2 bindings]
                oil  ia.input.text-field  [2 bindings]
              comp7  ia.container.flex
                RowLabel  ia.display.label
                suction  ia.input.text-field  [2 bindings]
                discharge  ia.input.text-field  [2 bindings]
                fla  ia.input.text-field  [2 bindings]
                hours  ia.input.text-field  [2 bindings]
                slide  ia.input.text-field  [2 bindings]
                ratio  ia.input.text-field  [2 bindings]
                oil  ia.input.text-field  [2 bindings]
        Purger  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            Row  ia.container.flex
              Psig  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                V  ia.input.text-field  [2 bindings]
              Purges  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                V  ia.input.text-field  [2 bindings]
              Visuals  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                V  ia.input.checkbox  [2 bindings]
              Fan  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                V  ia.input.checkbox  [2 bindings]
        Vessels  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            Table  ia.container.flex
              Head  ia.container.flex
                RowHead  ia.display.label
                H_level  ia.container.flex
                  Text  ia.display.label
                H_psi  ia.container.flex
                  Text  ia.display.label
                H_pump  ia.container.flex
                  Text  ia.display.label
                H_pumphrs  ia.container.flex
                  Text  ia.display.label
              htr  ia.container.flex
                RowLabel  ia.display.label
                Level  ia.input.text-field  [2 bindings]
                Psi  ia.input.text-field  [2 bindings]
                Pump  ia.input.dropdown  [2 bindings]
                PumpHrs  ia.input.text-field  [2 bindings]
              ltr  ia.container.flex
                RowLabel  ia.display.label
                Level  ia.input.text-field  [2 bindings]
                Psi  ia.input.text-field  [2 bindings]
                Pump  ia.input.dropdown  [2 bindings]
                PumpHrs  ia.input.text-field  [2 bindings]
              hpr  ia.container.flex
                RowLabel  ia.display.label
                Level  ia.input.text-field  [2 bindings]
                Psi  ia.input.text-field  [2 bindings]
                Pump  ia.input.dropdown  [2 bindings]
                E_pumphrs  ia.container.flex
              csv  ia.container.flex
                RowLabel  ia.display.label
                Level  ia.input.text-field  [2 bindings]
                Psi  ia.input.text-field  [2 bindings]
                Pump  ia.input.dropdown  [2 bindings]
                E_pumphrs  ia.container.flex
            FilterPonds  ia.container.flex
              Filter  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                V  ia.input.text-field  [2 bindings]
              PondsLbl  ia.display.label
              Ponds  ia.container.flex
                West  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.dropdown  [2 bindings]
                East  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.dropdown  [2 bindings]
        PumpsCondensers  ia.container.flex
          CsvPumps  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
            Body  ia.container.flex
              Table  ia.container.flex
                Head  ia.container.flex
                  RowHead  ia.display.label
                  H_status  ia.container.flex
                    Text  ia.display.label
                  H_hrs  ia.container.flex
                    Text  ia.display.label
                csvpump1  ia.container.flex
                  RowLabel  ia.display.label
                  Status  ia.input.dropdown  [2 bindings]
                  Hrs  ia.input.text-field  [2 bindings]
                csvpump2  ia.container.flex
                  RowLabel  ia.display.label
                  Status  ia.input.dropdown  [2 bindings]
                  Hrs  ia.input.text-field  [2 bindings]
                csvpump3  ia.container.flex
                  RowLabel  ia.display.label
                  Status  ia.input.dropdown  [2 bindings]
                  Hrs  ia.input.text-field  [2 bindings]
          Condensers  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
            Body  ia.container.flex
              Table  ia.container.flex
                Head  ia.container.flex
                  RowHead  ia.display.label
                  H_fana  ia.container.flex
                    Text  ia.display.label
                  H_fan1hrs  ia.container.flex
                    Text  ia.display.label
                  H_fanb  ia.container.flex
                    Text  ia.display.label
                  H_fan2hrs  ia.container.flex
                    Text  ia.display.label
                cond1  ia.container.flex
                  RowLabel  ia.display.label
                  fana  ia.input.dropdown  [2 bindings]
                  fan1hrs  ia.input.text-field  [2 bindings]
                  fanb  ia.input.dropdown  [2 bindings]
                  fan2hrs  ia.input.text-field  [2 bindings]
                cond2  ia.container.flex
                  RowLabel  ia.display.label
                  fana  ia.input.dropdown  [2 bindings]
                  fan1hrs  ia.input.text-field  [2 bindings]
                  fanb  ia.input.dropdown  [2 bindings]
                  fan2hrs  ia.input.text-field  [2 bindings]
              CondTitle  ia.display.label
              Conductivity  ia.container.flex
                WebMaster  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.text-field  [2 bindings]
                HandHeld  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.text-field  [2 bindings]
        EvapTherm  ia.container.flex
          Evaporators  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
            Body  ia.container.flex
              Table  ia.container.flex
                Head  ia.container.flex
                  RowHead  ia.display.label
                  H_temp  ia.container.flex
                    Text  ia.display.label
                  H_suction  ia.container.flex
                    Text  ia.display.label
                  H_status  ia.container.flex
                    Text  ia.display.label
                  H_hrs  ia.container.flex
                    Text  ia.display.label
                  H_coil  ia.container.flex
                    Text  ia.display.label
... 200 more components (see the Designer)
```

</details>

## Bindings

402 bindings: expr 217, property 185.

<details>
<summary>All 402 bindings, grouped by component</summary>

**`(view)`**

- `custom.avg_probe`: expression

```js
if((if((len(trim(toStr(coalesce({view.custom.f.evap_a1_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_a1_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_a2_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_a2_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_b1_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_b1_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_b2_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_b2_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_c1_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_c1_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_d1_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_d1_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_e1_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_e1_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_e2_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_e2_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_e3_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_e3_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_e4_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_e4_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_f1_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_f1_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_f2_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_f2_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_f3_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_f3_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_f4_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_f4_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_g1_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_g1_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_g2_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_g2_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_g3_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_g3_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_g4_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_g4_temp}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.evap_g5_temp}, '')))) > 0 && toFloat(coalesce({view.custom.f.evap_g5_temp}, ''), -1.0E12) > -1.0E11), 1, 0)) > 0, numberFormat((if((len(trim(toStr(coalesce({view.custom.f.evap_a1_temp}, '')))) > 0 &&
// ... truncated (9764 characters in total): see the view.json
```


- `custom.avg_therm`: expression

```js
if((if((len(trim(toStr(coalesce({view.custom.f.t1}, '')))) > 0 && toFloat(coalesce({view.custom.f.t1}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t2}, '')))) > 0 && toFloat(coalesce({view.custom.f.t2}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t3}, '')))) > 0 && toFloat(coalesce({view.custom.f.t3}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t4}, '')))) > 0 && toFloat(coalesce({view.custom.f.t4}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t5}, '')))) > 0 && toFloat(coalesce({view.custom.f.t5}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t6}, '')))) > 0 && toFloat(coalesce({view.custom.f.t6}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t7}, '')))) > 0 && toFloat(coalesce({view.custom.f.t7}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t8}, '')))) > 0 && toFloat(coalesce({view.custom.f.t8}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t9}, '')))) > 0 && toFloat(coalesce({view.custom.f.t9}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t10}, '')))) > 0 && toFloat(coalesce({view.custom.f.t10}, ''), -1.0E12) > -1.0E11), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.t11}, '')))) > 0 && toFloat(coalesce({view.custom.f.t11}, ''), -1.0E12) > -1.0E11), 1, 0)) > 0, numberFormat((if((len(trim(toStr(coalesce({view.custom.f.t1}, '')))) > 0 && toFloat(coalesce({view.custom.f.t1}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t1}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t2}, '')))) > 0 && toFloat(coalesce({view.custom.f.t2}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t2}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t3}, '')))) > 0 && toFloat(coalesce({view.custom.f.t3}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t3}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t4}, '')))) > 0 && toFloat(coalesce({view.custom.f.t4}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t4}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t5}, '')))) > 0 && toFloat(coalesce({view.custom.f.t5}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t5}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t6}, '')))) > 0 && toFloat(coalesce({view.custom.f.t6}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t6}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t7}, '')))) > 0 && toFloat(coalesce({view.custom.f.t7}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t7}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t8}, '')))) > 0 && toFloat(coalesce({view.custom.f.t8}, ''), -1.0E12) > -1.0E11), toFloat(coalesce({view.custom.f.t8}, ''), 0), 0) + if((len(trim(toStr(coalesce({view.custom.f.t9}, '')))) > 0 && toFloat(coalesce({view.custom.f.t9}, ''),
// ... truncated (4912 characters in total): see the view.json
```


- `custom.locked`: expression

```js
coalesce({view.params.readOnly}, false) || coalesce({view.custom.result.ok}, false)
```


- `custom.missing`: expression

```js
if(len({view.custom.missingRaw}) > 2, substring({view.custom.missingRaw}, 2), '')
```


- `custom.missingCount`: expression

```js
if(len(trim(toStr(coalesce({view.custom.f.name}, '')))) = 0, 1, 0) + if(isNull({view.custom.f.date}), 1, 0)
```


- `custom.missingRaw`: expression

```js
if(len(trim(toStr(coalesce({view.custom.f.name}, '')))) = 0, ', Name', '') + if(isNull({view.custom.f.date}), ', Date', '')
```


**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

**`root/Scroll/Form/Header/TitleBlock/SubRow/Subtitle`**

- `props.text`: expression

```js
if(coalesce({view.params.readOnly}, false), coalesce({view.custom.meta}, ''), 'NH3 Refrigeration Daily Log · Groveport')
```


**`root/Scroll/Form/Header/TitleBlock/SubRow/Dot`**

- `position.display`: expression

```js
!{view.custom.locked}
```


**`root/Scroll/Form/Header/TitleBlock/SubRow/Legend`**

- `position.display`: expression

```js
!{view.custom.locked}
```


**`root/Scroll/Form/Header/TitleBlock/SubRow/LegendText`**

- `position.display`: expression

```js
!{view.custom.locked}
```


**`root/Scroll/Form/Header/NameDate/Name/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.options`: property `view.custom.operators`

- `props.style.classes`: expression

```js
if(!{view.custom.locked} && (len(trim(toStr(coalesce({view.custom.f.name}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.name` (bidirectional)

**`root/Scroll/Form/Header/NameDate/Date/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && (isNull({view.custom.f.date})), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.date` (bidirectional)

**`root/Scroll/Form/Denied`**

- `position.display`: expression

```js
!coalesce({session.custom.Permissions.Forms.Use}, false)
```


**`root/Scroll/Form/Summary`**

- `position.display`: expression

```js
!{view.custom.locked} && coalesce({view.custom.attempted}, false) && len(coalesce({view.custom.missing}, '')) > 0
```


**`root/Scroll/Form/Summary/List`**

- `props.text`: property `view.custom.missing`

**`root/Scroll/Form/Result`**

- `position.display`: expression

```js
coalesce({view.custom.result.ok}, false) && !coalesce({view.params.readOnly}, false)
```


- `props.text`: expression

```js
coalesce({view.custom.result.message}, '') + ' - Print Or Download The PDF, Start A New Form, Or Open The History.'
```


**`root/Scroll/Form/Message`**

- `position.display`: expression

```js
len(coalesce({view.custom.msg}, '')) > 0
```


- `props.text`: property `view.custom.msg`

**`root/Scroll/Form/Sections`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false)
```


**`root/Scroll/Form/Sections/Compressors/Body/Table/comp1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp1_suction` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp1/discharge`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp1_discharge` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp1/fla`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp1_fla` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp1/hours`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp1_hours` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp1/slide`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp1_slide` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp1/ratio`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp1_ratio` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp1/oil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp1_oil` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp4/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp4_suction` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp4/discharge`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp4_discharge` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp4/fla`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp4_fla` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp4/hours`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp4_hours` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp4/slide`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp4_slide` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp4/ratio`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp4_ratio` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp4/oil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp4_oil` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp5/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp5_suction` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp5/discharge`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp5_discharge` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp5/fla`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp5_fla` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp5/hours`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp5_hours` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp5/slide`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp5_slide` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp5/ratio`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp5_ratio` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp5/oil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp5_oil` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp6/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp6_suction` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp6/discharge`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp6_discharge` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp6/fla`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp6_fla` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp6/hours`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp6_hours` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp6/slide`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp6_slide` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp6/ratio`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp6_ratio` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp6/oil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp6_oil` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp7/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp7_suction` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp7/discharge`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp7_discharge` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp7/fla`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp7_fla` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp7/hours`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp7_hours` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp7/slide`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp7_slide` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp7/ratio`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp7_ratio` (bidirectional)

**`root/Scroll/Form/Sections/Compressors/Body/Table/comp7/oil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.comp7_oil` (bidirectional)

**`root/Scroll/Form/Sections/Purger/Body/Row/Psig/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.purger_psig` (bidirectional)

**`root/Scroll/Form/Sections/Purger/Body/Row/Purges/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.purger_purges` (bidirectional)

**`root/Scroll/Form/Sections/Purger/Body/Row/Visuals/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.selected`: property `view.custom.f.prv_rd_visuals` (bidirectional)

**`root/Scroll/Form/Sections/Purger/Body/Row/Fan/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.selected`: property `view.custom.f.continuous_fan` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/htr/Level`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.htr_level` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/htr/Psi`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.htr_psi` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/htr/Pump`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.htr_pump` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/htr/PumpHrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.htr_pumphrs` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/ltr/Level`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.ltr_level` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/ltr/Psi`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.ltr_psi` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/ltr/Pump`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.ltr_pump` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/ltr/PumpHrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.ltr_pumphrs` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/hpr/Level`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.hpr_level` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/hpr/Psi`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.hpr_psi` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/hpr/Pump`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.hpr_pump` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/csv/Level`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.csv_level` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/csv/Psi`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.csv_psi` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/Table/csv/Pump`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.csv_pump` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/FilterPonds/Filter/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.filter_dp` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/FilterPonds/Ponds/West/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.pond_west` (bidirectional)

**`root/Scroll/Form/Sections/Vessels/Body/FilterPonds/Ponds/East/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.pond_east` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/CsvPumps/Body/Table/csvpump1/Status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.csvpump1_status` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/CsvPumps/Body/Table/csvpump1/Hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.csvpump1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/CsvPumps/Body/Table/csvpump2/Status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.csvpump2_status` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/CsvPumps/Body/Table/csvpump2/Hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.csvpump2_hrs` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/CsvPumps/Body/Table/csvpump3/Status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.csvpump3_status` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/CsvPumps/Body/Table/csvpump3/Hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.csvpump3_hrs` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond1/fana`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.cond1_fana` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond1/fan1hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.cond1_fan1hrs` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond1/fanb`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.cond1_fanb` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond1/fan2hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.cond1_fan2hrs` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond2/fana`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.cond2_fana` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond2/fan1hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.cond2_fan1hrs` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond2/fanb`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.cond2_fanb` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Table/cond2/fan2hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.cond2_fan2hrs` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Conductivity/WebMaster/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.cond_webmaster` (bidirectional)

**`root/Scroll/Form/Sections/PumpsCondensers/Condensers/Body/Conductivity/HandHeld/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.cond_handheld` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A1/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a1_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a1_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A1/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a1_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A1/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A1/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a1_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A2/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a2_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A2/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a2_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A2/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a2_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A2/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a2_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/A2/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_a2_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B1/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_b1_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_b1_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B1/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_b1_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B1/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_b1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B1/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_b1_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B2/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_b2_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B2/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_b2_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B2/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_b2_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B2/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_b2_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/B2/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_b2_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/C1/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_c1_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/C1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_c1_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/C1/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_c1_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/C1/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_c1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/C1/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_c1_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/D1/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_d1_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/D1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_d1_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/D1/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_d1_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/D1/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_d1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/D1/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_d1_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E1/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e1_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e1_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E1/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e1_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E1/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E1/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e1_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E2/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e2_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E2/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e2_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E2/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e2_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E2/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e2_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E2/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e2_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E3/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e3_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E3/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e3_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E3/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e3_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E3/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e3_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E3/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e3_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E4/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e4_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E4/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e4_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E4/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e4_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E4/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_e4_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/E4/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_e4_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F1/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f1_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f1_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F1/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f1_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F1/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F1/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f1_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F2/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f2_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F2/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f2_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F2/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f2_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F2/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f2_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F2/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f2_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F3/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f3_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F3/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f3_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F3/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f3_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F3/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f3_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F3/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f3_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F4/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f4_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F4/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f4_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F4/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f4_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F4/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_f4_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/F4/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_f4_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G1/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g1_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G1/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g1_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G1/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g1_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G1/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g1_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G1/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g1_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G2/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g2_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G2/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g2_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G2/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g2_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G2/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g2_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G2/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g2_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G3/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g3_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G3/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g3_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G3/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g3_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G3/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g3_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G3/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g3_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G4/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g4_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G4/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g4_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G4/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g4_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G4/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g4_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G4/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g4_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G5/temp`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g5_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G5/suction`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g5_suction` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G5/status`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g5_status` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G5/hrs`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.evap_g5_hrs` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Evaporators/Body/Table/G5/coil`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.evap_g5_coil` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t1/t1`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t1` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t2/t2`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t2` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t3/t3`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t3` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t4/t4`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t4` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t5/t5`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t5` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t6/t6`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t6` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t7/t7`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t7` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t8/t8`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t8` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t9/t9`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t9` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t10/t10`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t10` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Table/t11/t11`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.t11` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Totals/AvgTherm/AvgTherm`**

- `props.text`: expression

```js
if(len(coalesce({view.custom.avg_therm}, '')) > 0, {view.custom.avg_therm}, '--')
```


**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Totals/AvgProbe/AvgProbe`**

- `props.text`: expression

```js
if(len(coalesce({view.custom.avg_probe}, '')) > 0, {view.custom.avg_probe}, '--')
```


**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Totals/ControlRoom/ControlRoom`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.control_room_temp` (bidirectional)

**`root/Scroll/Form/Sections/EvapTherm/Therm/Body/Totals/Ambient/Ambient`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.outside_ambient_temp` (bidirectional)

**`root/Footer`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false)
```


**`root/Footer/Bar/ActionBar/Status`**

- `props.style.classes`: expression

```js
if(!{view.custom.locked} && coalesce({view.custom.missingCount}, 0) > 0, 'form-status form-status-error', 'form-status')
```


- `props.text`: expression

```js
if(coalesce({view.params.readOnly}, false), 'Read Only - Submitted Record', if(coalesce({view.custom.result.ok}, false), 'Submitted - Saved To Form History', if(coalesce({view.custom.missingCount}, 0) > 0, toStr(coalesce({view.custom.missingCount}, 0)) + if(coalesce({view.custom.missingCount}, 0) = 1, ' Required Field Missing: ', ' Required Fields Missing: ') + coalesce({view.custom.missing}, ''), 'All Required Fields Complete')))
```


**`root/Footer/Bar/ActionBar/Fill`**

- `position.display`: expression

```js
!coalesce({view.params.readOnly}, false) && !coalesce({view.custom.result.ok}, false) && coalesce({session.custom.Permissions.Forms.Use}, false)
```


- `props.enabled`: expression

```js
!{view.custom.locked}
```


**`root/Footer/Bar/ActionBar/Clear`**

- `position.display`: expression

```js
!coalesce({view.params.readOnly}, false) && !coalesce({view.custom.result.ok}, false) && coalesce({session.custom.Permissions.Forms.Use}, false)
```


- `props.enabled`: expression

```js
!{view.custom.locked}
```


**`root/Footer/Bar/ActionBar/Submit`**

- `position.display`: expression

```js
!coalesce({view.params.readOnly}, false) && !coalesce({view.custom.result.ok}, false) && coalesce({session.custom.Permissions.Forms.Use}, false)
```


- `props.enabled`: expression

```js
!{view.custom.locked}
```


**`root/Footer/Bar/ActionBar/Print`**

- `position.display`: expression

```js
coalesce({view.params.readOnly}, false) && coalesce({view.params.submissionId}, 0) > 0
```


**`root/Footer/Bar/ActionBar/New`**

- `position.display`: expression

```js
coalesce({view.custom.result.ok}, false) && !coalesce({view.params.readOnly}, false)
```


**`root/Footer/Bar/ActionBar/History`**

- `position.display`: expression

```js
coalesce({view.custom.result.ok}, false) && !coalesce({view.params.readOnly}, false)
```


**`root/Footer/Bar/ActionBar/Pdf`**

- `position.display`: expression

```js
coalesce({view.custom.result.ok}, false) && !coalesce({view.params.readOnly}, false)
```

</details>

## Event Scripts And Handlers

- **`root`** `system.onStartup`, script action, scope `G`

```python
# Operations Forms: defaults for a new form, or the stored submission (read only, History > View).
v = self.view
v.custom.operators = shared.Forms.operatorOptions(self.session)
if v.params.readOnly or v.params.submissionId:
    rec = shared.Forms.loadForView(self.session, v.params.submissionId)
    if rec is None or rec['formType'] != 'DailyRounds':
        v.custom.msg = 'Submission Not Available'
        return
    v.custom.f = rec['data']
    v.custom.meta = rec['meta']
elif shared.Forms.allowed(self.session):
    v.custom.f = shared.Forms.newData(self.session, 'DailyRounds')
```

- **`root/Footer/Bar/ActionBar/Fill`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.locked:
    return
vals = shared.Forms.liveValues(self.session)
self.view.custom.f = shared.Forms.merged('DailyRounds', self.view.custom.f, vals)
self.view.custom.msg = 'Filled %d Fields From Live Values - Verify Each Reading In The Field.' % len(vals)
```

- **`root/Footer/Bar/ActionBar/Clear`** `component.onActionPerformed`, script action, scope `G`

```python
shared.Alerts.showAlert(state='warning', title='Clear Form', message='Clear every field and start a new Daily Rounds Log?', showCloseBtn=False, btnTextPrimary='Clear', btnTextSecondary='Cancel', btnActionPrimary='opsFormsClearDailyRounds', btnActionSecondary='', payload={'sender': self.view.id}, overlayDismiss=False)
```

- **`root/Footer/Bar/ActionBar/Submit`** `component.onActionPerformed`, script action, scope `G`

```python
if self.view.custom.locked:
    return
if self.view.custom.missing:
    # blocked: the summary banner and the red outlines show what is missing
    self.view.custom.attempted = True
    self.view.custom.msg = ''
    return
shared.Alerts.showAlert(state='info', title='Submit Daily Rounds Log', message='Submit this Daily Rounds Log? It is saved to Form History and cannot be edited afterwards.', showCloseBtn=False, btnTextPrimary='Submit', btnTextSecondary='Cancel', btnActionPrimary='opsFormsSubmitDailyRounds', btnActionSecondary='', payload={'sender': self.view.id}, overlayDismiss=False)
```

- **`root/Footer/Bar/ActionBar/Print`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = shared.Forms.downloadPdf(self.session, 'DailyRounds', self.view.params.submissionId)
```

- **`root/Footer/Bar/ActionBar/New`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.f = shared.Forms.newData(self.session, 'DailyRounds')
self.view.custom.result = {'ok': False, 'id': 0, 'message': ''}
self.view.custom.msg = ''
self.view.custom.attempted = False
```

- **`root/Footer/Bar/ActionBar/History`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.navigate('/operations/forms/history')
```

- **`root/Footer/Bar/ActionBar/Pdf`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = shared.Forms.downloadPdf(self.session, 'DailyRounds', self.view.custom.result.id)
```

- **`root`** message handler `opsFormsSubmitDailyRounds` (scope: page)

```python
if self.view.params.readOnly or self.view.custom.result.ok:
    return
if payload.get('sender') and payload.get('sender') != self.view.id:
    return
res = shared.Forms.submit(self.session, 'DailyRounds', self.view.custom.f)
self.view.custom.result = res
self.view.custom.msg = '' if res.get('ok') else res.get('message')
```

- **`root`** message handler `opsFormsClearDailyRounds` (scope: page)

```python
if self.view.params.readOnly:
    return
if payload.get('sender') and payload.get('sender') != self.view.id:
    return
self.view.custom.f = shared.Forms.newData(self.session, 'DailyRounds')
self.view.custom.result = {'ok': False, 'id': 0, 'message': ''}
self.view.custom.msg = ''
self.view.custom.attempted = False
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Forms.allowed](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.downloadPdf](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.liveValues](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.loadForView](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.merged](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.newData](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.operatorOptions](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.submit](../../../../../../../scripting/reference/modules/shared-forms.md).

## Related Views

**Opened or named by** (4): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md), [00\_Pages/Groveport/Operations/Forms/History](./history.md), [00\_Pages/Groveport/Operations/Forms/\_Assets/HistoryActions](./assets/historyactions.md)

## Style Classes

<details>
<summary>27 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `bg-component` | 1 | stylesheet |
| `bg-page` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `form-banner` | 3 | style class |
| `form-banner-error` | 1 | style class |
| `form-banner-ok` | 1 | style class |
| `form-btn` | 4 | style class |
| `form-btn-primary` | 3 | style class |
| `form-calc` | 2 | style class |
| `form-card` | 9 | style class |
| `form-check` | 3 | style class |
| `form-input` | 180 | style class |
| `form-label` | 11 | style class |
| `form-page` | 1 | stylesheet |
| `form-required-marker` | 3 | style class |
| `form-row-label` | 48 | style class |
| `form-section-head` | 7 | style class |
| `form-section-title` | 8 | style class |
| `form-status` | 1 | style class |
| `form-subtitle` | 3 | style class |
| `form-th` | 31 | style class |
| `form-thead` | 6 | stylesheet |
| `form-title` | 1 | style class |
| `form-tr` | 54 | stylesheet |
| `fs-16` | 1 | style class |
| `fw-600` | 1 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
