---
title: "ShiftLog"
sidebar_label: "ShiftLog"
description: "Perspective view 00_Pages/Groveport/Operations/Forms/ShiftLog (Page): 544 components, 267 bindings, 7 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/Forms/ShiftLog", "ShiftLog", "/operations/forms/shift-log"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Operations/Forms/ShiftLog`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/Forms/ShiftLog` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/Forms/ShiftLog/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; Forms &gt; ShiftLog |
| Routes | `/operations/forms/shift-log` (NH3 Shift Log) |
| Root | `ia.container.flex`, height 1000, width 1600 |
| Size | 544 components, 267 bindings, 7 event handlers, 0 change scripts, 3 message handlers |
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
| `f` | `{"alarm1_action": "", "alarm1_desc": "", "alarm1_equip": "", "alarm...` | |
| `locked` | `false` | bound (expr) |
| `meta` | `""` | |
| `missing` | `""` | bound (expr) |
| `missingCount` | `0` | bound (expr) |
| `missingRaw` | `""` | bound (expr) |
| `msg` | `""` | |
| `operators` | `[]` | |
| `result` | `{"id": 0, "message": "", "ok": false}` | |

## Component Tree

Component types: ia.container.flex x259, ia.display.label x184, ia.input.text-field x60, ia.input.dropdown x28, ia.input.button x6, ia.input.text-area x5, ia.input.date-time-input x2.

<details>
<summary>Component tree (544 components)</summary>

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
      Denied  ia.container.flex  [1 binding]
        DeniedMsg  ia.display.label
      Summary  ia.container.flex  [1 binding]
        Title  ia.display.label
        List  ia.display.label  [1 binding]
      Result  ia.display.label  [2 bindings]
      Message  ia.display.label  [2 bindings]
      Sections  ia.container.flex  [1 binding]
        ShiftInfo  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            Row  ia.container.flex
              Date  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                  Req  ia.display.label
                V  ia.input.date-time-input  [3 bindings]
              Op1Group  ia.container.flex
                Op1  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                    Req  ia.display.label
                  V  ia.input.dropdown  [4 bindings]
                Op1Time  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.text-field  [2 bindings]
              Op2Group  ia.container.flex
                Op2  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.dropdown  [3 bindings]
                Op2Time  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.text-field  [2 bindings]
              Status  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                  Req  ia.display.label
                V  ia.input.dropdown  [3 bindings]
        Handover  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            Row  ia.container.flex
              OutGroup  ia.container.flex
                Out  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.dropdown  [3 bindings]
                OutTime  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.text-field  [2 bindings]
              InGroup  ia.container.flex
                In  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.dropdown  [3 bindings]
                InTime  ia.container.flex
                  Caption  ia.container.flex
                    Label  ia.display.label
                  V  ia.input.text-field  [2 bindings]
              Reviewed  ia.container.flex
                Caption  ia.container.flex
                  Label  ia.display.label
                  Req  ia.display.label  [1 binding]
                V  ia.input.dropdown  [3 bindings]
        KeyItems  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            Text  ia.input.text-area  [2 bindings]
        Alarms  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            Table  ia.container.flex
              Head  ia.container.flex
                H_time  ia.container.flex
                  Text  ia.display.label
                  Req  ia.display.label
                H_equip  ia.container.flex
                  Text  ia.display.label
                H_desc  ia.container.flex
                  Text  ia.display.label
                  Req  ia.display.label
                H_action  ia.container.flex
                  Text  ia.display.label
                H_resolved  ia.container.flex
                  Text  ia.display.label
                H_initials  ia.container.flex
                  Text  ia.display.label
              R1  ia.container.flex
                RowLabel  ia.display.label
                C_time  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  time  ia.input.text-field  [3 bindings]
                C_equip  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  equip  ia.input.text-field  [2 bindings]
                C_desc  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  desc  ia.input.text-field  [3 bindings]
                C_action  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  action  ia.input.text-field  [2 bindings]
                C_resolved  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  resolved  ia.input.dropdown  [2 bindings]
                C_initials  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  initials  ia.input.text-field  [2 bindings]
              R2  ia.container.flex
                RowLabel  ia.display.label
                C_time  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  time  ia.input.text-field  [3 bindings]
                C_equip  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  equip  ia.input.text-field  [2 bindings]
                C_desc  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  desc  ia.input.text-field  [3 bindings]
                C_action  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  action  ia.input.text-field  [2 bindings]
                C_resolved  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  resolved  ia.input.dropdown  [2 bindings]
                C_initials  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  initials  ia.input.text-field  [2 bindings]
              R3  ia.container.flex
                RowLabel  ia.display.label
                C_time  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  time  ia.input.text-field  [3 bindings]
                C_equip  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  equip  ia.input.text-field  [2 bindings]
                C_desc  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  desc  ia.input.text-field  [3 bindings]
                C_action  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  action  ia.input.text-field  [2 bindings]
                C_resolved  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  resolved  ia.input.dropdown  [2 bindings]
                C_initials  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  initials  ia.input.text-field  [2 bindings]
              R4  ia.container.flex
                RowLabel  ia.display.label
                C_time  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  time  ia.input.text-field  [3 bindings]
                C_equip  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  equip  ia.input.text-field  [2 bindings]
                C_desc  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  desc  ia.input.text-field  [3 bindings]
                C_action  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  action  ia.input.text-field  [2 bindings]
                C_resolved  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  resolved  ia.input.dropdown  [2 bindings]
                C_initials  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  initials  ia.input.text-field  [2 bindings]
              R5  ia.container.flex
                RowLabel  ia.display.label
                C_time  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  time  ia.input.text-field  [3 bindings]
                C_equip  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  equip  ia.input.text-field  [2 bindings]
                C_desc  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                    Req  ia.display.label
                  desc  ia.input.text-field  [3 bindings]
                C_action  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  action  ia.input.text-field  [2 bindings]
                C_resolved  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  resolved  ia.input.dropdown  [2 bindings]
                C_initials  ia.container.flex
                  Cap  ia.container.flex
                    Text  ia.display.label
                  initials  ia.input.text-field  [2 bindings]
              R6  ia.container.flex
                RowLabel  ia.display.label
                C_time  ia.container.flex
                  Cap  ia.container.flex
... 294 more components (see the Designer)
```

</details>

## Bindings

267 bindings: expr 165, property 102.

<details>
<summary>All 267 bindings, grouped by component</summary>

**`(view)`**

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
if(isNull({view.custom.f.date}), 1, 0) + if(len(trim(toStr(coalesce({view.custom.f.op1}, '')))) = 0, 1, 0) + if(len(trim(toStr(coalesce({view.custom.f.shift_status}, '')))) = 0, 1, 0) + if(len(trim(toStr(coalesce({view.custom.f.name}, '')))) = 0, 1, 0) + if(isNull({view.custom.f.sign_date}), 1, 0) + if((coalesce({view.custom.f.shift_status}, '') = 'Abnormal - See Notes') && (len(trim(toStr(coalesce({view.custom.f.summary}, '')))) = 0), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.in_op}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.in_reviewed}, '')))) = 0), 1, 0) + if((coalesce({view.custom.f.open_items}, '') = 'Yes - See Comments') && (len(trim(toStr(coalesce({view.custom.f.comments}, '')))) = 0), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.alarm1_time}, '')) + toStr(coalesce({view.custom.f.alarm1_equip}, '')) + toStr(coalesce({view.custom.f.alarm1_desc}, '')) + toStr(coalesce({view.custom.f.alarm1_action}, '')) + toStr(coalesce({view.custom.f.alarm1_resolved}, '')) + toStr(coalesce({view.custom.f.alarm1_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm1_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm1_desc}, '')))) = 0), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.alarm2_time}, '')) + toStr(coalesce({view.custom.f.alarm2_equip}, '')) + toStr(coalesce({view.custom.f.alarm2_desc}, '')) + toStr(coalesce({view.custom.f.alarm2_action}, '')) + toStr(coalesce({view.custom.f.alarm2_resolved}, '')) + toStr(coalesce({view.custom.f.alarm2_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm2_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm2_desc}, '')))) = 0), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.alarm3_time}, '')) + toStr(coalesce({view.custom.f.alarm3_equip}, '')) + toStr(coalesce({view.custom.f.alarm3_desc}, '')) + toStr(coalesce({view.custom.f.alarm3_action}, '')) + toStr(coalesce({view.custom.f.alarm3_resolved}, '')) + toStr(coalesce({view.custom.f.alarm3_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm3_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm3_desc}, '')))) = 0), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.alarm4_time}, '')) + toStr(coalesce({view.custom.f.alarm4_equip}, '')) + toStr(coalesce({view.custom.f.alarm4_desc}, '')) + toStr(coalesce({view.custom.f.alarm4_action}, '')) + toStr(coalesce({view.custom.f.alarm4_resolved}, '')) + toStr(coalesce({view.custom.f.alarm4_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm4_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm4_desc}, '')))) = 0), 1, 0) + if((len(trim(toStr(coalesce({view.custom.f.alarm5_time}, '')) + toStr(coalesce({view.custom.f.alarm5_equip}, '')) + toStr(coalesce({view.custom.f.alarm5_desc}, '')) + toStr(coalesce({view.custom.f.alarm5_action}, '')) + toStr(coalesce({view.custom.f.alarm5_resolved}, '')) + toStr(coalesce({view.custom.f.alarm5_initials}, '')))) > 0) && (len(trim
// ... truncated (7230 characters in total): see the view.json
```


- `custom.missingRaw`: expression

```js
if(isNull({view.custom.f.date}), ', Date', '') + if(len(trim(toStr(coalesce({view.custom.f.op1}, '')))) = 0, ', Operator 1', '') + if(len(trim(toStr(coalesce({view.custom.f.shift_status}, '')))) = 0, ', Shift Status', '') + if(len(trim(toStr(coalesce({view.custom.f.name}, '')))) = 0, ', Name', '') + if(isNull({view.custom.f.sign_date}), ', Sign-Off Date', '') + if((coalesce({view.custom.f.shift_status}, '') = 'Abnormal - See Notes') && (len(trim(toStr(coalesce({view.custom.f.summary}, '')))) = 0), ', General Shift Summary / Notes (Abnormal Shift)', '') + if((len(trim(toStr(coalesce({view.custom.f.in_op}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.in_reviewed}, '')))) = 0), ', Incoming Op. Reviewed?', '') + if((coalesce({view.custom.f.open_items}, '') = 'Yes - See Comments') && (len(trim(toStr(coalesce({view.custom.f.comments}, '')))) = 0), ', Comments (Open Items)', '') + if((len(trim(toStr(coalesce({view.custom.f.alarm1_time}, '')) + toStr(coalesce({view.custom.f.alarm1_equip}, '')) + toStr(coalesce({view.custom.f.alarm1_desc}, '')) + toStr(coalesce({view.custom.f.alarm1_action}, '')) + toStr(coalesce({view.custom.f.alarm1_resolved}, '')) + toStr(coalesce({view.custom.f.alarm1_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm1_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm1_desc}, '')))) = 0), ', Alarm Row 1 Time And Description', '') + if((len(trim(toStr(coalesce({view.custom.f.alarm2_time}, '')) + toStr(coalesce({view.custom.f.alarm2_equip}, '')) + toStr(coalesce({view.custom.f.alarm2_desc}, '')) + toStr(coalesce({view.custom.f.alarm2_action}, '')) + toStr(coalesce({view.custom.f.alarm2_resolved}, '')) + toStr(coalesce({view.custom.f.alarm2_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm2_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm2_desc}, '')))) = 0), ', Alarm Row 2 Time And Description', '') + if((len(trim(toStr(coalesce({view.custom.f.alarm3_time}, '')) + toStr(coalesce({view.custom.f.alarm3_equip}, '')) + toStr(coalesce({view.custom.f.alarm3_desc}, '')) + toStr(coalesce({view.custom.f.alarm3_action}, '')) + toStr(coalesce({view.custom.f.alarm3_resolved}, '')) + toStr(coalesce({view.custom.f.alarm3_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm3_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm3_desc}, '')))) = 0), ', Alarm Row 3 Time And Description', '') + if((len(trim(toStr(coalesce({view.custom.f.alarm4_time}, '')) + toStr(coalesce({view.custom.f.alarm4_equip}, '')) + toStr(coalesce({view.custom.f.alarm4_desc}, '')) + toStr(coalesce({view.custom.f.alarm4_action}, '')) + toStr(coalesce({view.custom.f.alarm4_resolved}, '')) + toStr(coalesce({view.custom.f.alarm4_initials}, '')))) > 0) && (len(trim(toStr(coalesce({view.custom.f.alarm4_time}, '')))) = 0 || len(trim(toStr(coalesce({view.custom.f.alarm4_desc}, '')))) = 0), ', Alarm Row 4 Time And Description', '') + if((len(trim(toStr(coalesce({view.custo
// ... truncated (7922 characters in total): see the view.json
```


**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

**`root/Scroll/Form/Header/TitleBlock/SubRow/Subtitle`**

- `props.text`: expression

```js
if(coalesce({view.params.readOnly}, false), coalesce({view.custom.meta}, ''), 'NH3 Refrigeration Shift Log · Groveport')
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


**`root/Scroll/Form/Sections/ShiftInfo/Body/Row/Date/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && (isNull({view.custom.f.date})), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.date` (bidirectional)

**`root/Scroll/Form/Sections/ShiftInfo/Body/Row/Op1Group/Op1/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.options`: property `view.custom.operators`

- `props.style.classes`: expression

```js
if(!{view.custom.locked} && (len(trim(toStr(coalesce({view.custom.f.op1}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.op1` (bidirectional)

**`root/Scroll/Form/Sections/ShiftInfo/Body/Row/Op1Group/Op1Time/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.op1_time` (bidirectional)

**`root/Scroll/Form/Sections/ShiftInfo/Body/Row/Op2Group/Op2/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.options`: property `view.custom.operators`

- `props.value`: property `view.custom.f.op2` (bidirectional)

**`root/Scroll/Form/Sections/ShiftInfo/Body/Row/Op2Group/Op2Time/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.op2_time` (bidirectional)

**`root/Scroll/Form/Sections/ShiftInfo/Body/Row/Status/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && (len(trim(toStr(coalesce({view.custom.f.shift_status}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.shift_status` (bidirectional)

**`root/Scroll/Form/Sections/Handover/Body/Row/OutGroup/Out/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.options`: property `view.custom.operators`

- `props.value`: property `view.custom.f.out_op` (bidirectional)

**`root/Scroll/Form/Sections/Handover/Body/Row/OutGroup/OutTime/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.out_time` (bidirectional)

**`root/Scroll/Form/Sections/Handover/Body/Row/InGroup/In/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.options`: property `view.custom.operators`

- `props.value`: property `view.custom.f.in_op` (bidirectional)

**`root/Scroll/Form/Sections/Handover/Body/Row/InGroup/InTime/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.in_time` (bidirectional)

**`root/Scroll/Form/Sections/Handover/Body/Row/Reviewed/Caption/Req`**

- `position.display`: expression

```js
len(trim(toStr(coalesce({view.custom.f.in_op}, '')))) > 0
```


**`root/Scroll/Form/Sections/Handover/Body/Row/Reviewed/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.in_op}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.in_reviewed}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.in_reviewed` (bidirectional)

**`root/Scroll/Form/Sections/KeyItems/Body/Text`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.key_items` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R1/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm1_time}, '')) + toStr(coalesce({view.custom.f.alarm1_equip}, '')) + toStr(coalesce({view.custom.f.alarm1_desc}, '')) + toStr(coalesce({view.custom.f.alarm1_action}, '')) + toStr(coalesce({view.custom.f.alarm1_resolved}, '')) + toStr(coalesce({view.custom.f.alarm1_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm1_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm1_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R1/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm1_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R1/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm1_time}, '')) + toStr(coalesce({view.custom.f.alarm1_equip}, '')) + toStr(coalesce({view.custom.f.alarm1_desc}, '')) + toStr(coalesce({view.custom.f.alarm1_action}, '')) + toStr(coalesce({view.custom.f.alarm1_resolved}, '')) + toStr(coalesce({view.custom.f.alarm1_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm1_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm1_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R1/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm1_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R1/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm1_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R1/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm1_initials` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R2/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm2_time}, '')) + toStr(coalesce({view.custom.f.alarm2_equip}, '')) + toStr(coalesce({view.custom.f.alarm2_desc}, '')) + toStr(coalesce({view.custom.f.alarm2_action}, '')) + toStr(coalesce({view.custom.f.alarm2_resolved}, '')) + toStr(coalesce({view.custom.f.alarm2_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm2_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm2_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R2/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm2_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R2/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm2_time}, '')) + toStr(coalesce({view.custom.f.alarm2_equip}, '')) + toStr(coalesce({view.custom.f.alarm2_desc}, '')) + toStr(coalesce({view.custom.f.alarm2_action}, '')) + toStr(coalesce({view.custom.f.alarm2_resolved}, '')) + toStr(coalesce({view.custom.f.alarm2_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm2_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm2_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R2/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm2_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R2/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm2_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R2/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm2_initials` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R3/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm3_time}, '')) + toStr(coalesce({view.custom.f.alarm3_equip}, '')) + toStr(coalesce({view.custom.f.alarm3_desc}, '')) + toStr(coalesce({view.custom.f.alarm3_action}, '')) + toStr(coalesce({view.custom.f.alarm3_resolved}, '')) + toStr(coalesce({view.custom.f.alarm3_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm3_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm3_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R3/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm3_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R3/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm3_time}, '')) + toStr(coalesce({view.custom.f.alarm3_equip}, '')) + toStr(coalesce({view.custom.f.alarm3_desc}, '')) + toStr(coalesce({view.custom.f.alarm3_action}, '')) + toStr(coalesce({view.custom.f.alarm3_resolved}, '')) + toStr(coalesce({view.custom.f.alarm3_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm3_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm3_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R3/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm3_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R3/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm3_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R3/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm3_initials` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R4/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm4_time}, '')) + toStr(coalesce({view.custom.f.alarm4_equip}, '')) + toStr(coalesce({view.custom.f.alarm4_desc}, '')) + toStr(coalesce({view.custom.f.alarm4_action}, '')) + toStr(coalesce({view.custom.f.alarm4_resolved}, '')) + toStr(coalesce({view.custom.f.alarm4_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm4_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm4_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R4/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm4_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R4/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm4_time}, '')) + toStr(coalesce({view.custom.f.alarm4_equip}, '')) + toStr(coalesce({view.custom.f.alarm4_desc}, '')) + toStr(coalesce({view.custom.f.alarm4_action}, '')) + toStr(coalesce({view.custom.f.alarm4_resolved}, '')) + toStr(coalesce({view.custom.f.alarm4_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm4_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm4_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R4/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm4_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R4/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm4_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R4/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm4_initials` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R5/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm5_time}, '')) + toStr(coalesce({view.custom.f.alarm5_equip}, '')) + toStr(coalesce({view.custom.f.alarm5_desc}, '')) + toStr(coalesce({view.custom.f.alarm5_action}, '')) + toStr(coalesce({view.custom.f.alarm5_resolved}, '')) + toStr(coalesce({view.custom.f.alarm5_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm5_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm5_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R5/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm5_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R5/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm5_time}, '')) + toStr(coalesce({view.custom.f.alarm5_equip}, '')) + toStr(coalesce({view.custom.f.alarm5_desc}, '')) + toStr(coalesce({view.custom.f.alarm5_action}, '')) + toStr(coalesce({view.custom.f.alarm5_resolved}, '')) + toStr(coalesce({view.custom.f.alarm5_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm5_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm5_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R5/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm5_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R5/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm5_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R5/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm5_initials` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R6/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm6_time}, '')) + toStr(coalesce({view.custom.f.alarm6_equip}, '')) + toStr(coalesce({view.custom.f.alarm6_desc}, '')) + toStr(coalesce({view.custom.f.alarm6_action}, '')) + toStr(coalesce({view.custom.f.alarm6_resolved}, '')) + toStr(coalesce({view.custom.f.alarm6_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm6_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm6_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R6/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm6_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R6/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm6_time}, '')) + toStr(coalesce({view.custom.f.alarm6_equip}, '')) + toStr(coalesce({view.custom.f.alarm6_desc}, '')) + toStr(coalesce({view.custom.f.alarm6_action}, '')) + toStr(coalesce({view.custom.f.alarm6_resolved}, '')) + toStr(coalesce({view.custom.f.alarm6_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm6_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm6_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R6/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm6_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R6/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm6_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R6/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm6_initials` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R7/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm7_time}, '')) + toStr(coalesce({view.custom.f.alarm7_equip}, '')) + toStr(coalesce({view.custom.f.alarm7_desc}, '')) + toStr(coalesce({view.custom.f.alarm7_action}, '')) + toStr(coalesce({view.custom.f.alarm7_resolved}, '')) + toStr(coalesce({view.custom.f.alarm7_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm7_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm7_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R7/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm7_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R7/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm7_time}, '')) + toStr(coalesce({view.custom.f.alarm7_equip}, '')) + toStr(coalesce({view.custom.f.alarm7_desc}, '')) + toStr(coalesce({view.custom.f.alarm7_action}, '')) + toStr(coalesce({view.custom.f.alarm7_resolved}, '')) + toStr(coalesce({view.custom.f.alarm7_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm7_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm7_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R7/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm7_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R7/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm7_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R7/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm7_initials` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R8/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm8_time}, '')) + toStr(coalesce({view.custom.f.alarm8_equip}, '')) + toStr(coalesce({view.custom.f.alarm8_desc}, '')) + toStr(coalesce({view.custom.f.alarm8_action}, '')) + toStr(coalesce({view.custom.f.alarm8_resolved}, '')) + toStr(coalesce({view.custom.f.alarm8_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm8_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm8_time` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R8/C_equip/equip`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm8_equip` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R8/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.alarm8_time}, '')) + toStr(coalesce({view.custom.f.alarm8_equip}, '')) + toStr(coalesce({view.custom.f.alarm8_desc}, '')) + toStr(coalesce({view.custom.f.alarm8_action}, '')) + toStr(coalesce({view.custom.f.alarm8_resolved}, '')) + toStr(coalesce({view.custom.f.alarm8_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.alarm8_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.alarm8_desc` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R8/C_action/action`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm8_action` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R8/C_resolved/resolved`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.alarm8_resolved` (bidirectional)

**`root/Scroll/Form/Sections/Alarms/Body/Table/R8/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.alarm8_initials` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R1/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel1_time}, '')) + toStr(coalesce({view.custom.f.rel1_location}, '')) + toStr(coalesce({view.custom.f.rel1_desc}, '')) + toStr(coalesce({view.custom.f.rel1_detection}, '')) + toStr(coalesce({view.custom.f.rel1_reportable}, '')) + toStr(coalesce({view.custom.f.rel1_notified}, '')) + toStr(coalesce({view.custom.f.rel1_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel1_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel1_time` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R1/C_location/location`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel1_time}, '')) + toStr(coalesce({view.custom.f.rel1_location}, '')) + toStr(coalesce({view.custom.f.rel1_desc}, '')) + toStr(coalesce({view.custom.f.rel1_detection}, '')) + toStr(coalesce({view.custom.f.rel1_reportable}, '')) + toStr(coalesce({view.custom.f.rel1_notified}, '')) + toStr(coalesce({view.custom.f.rel1_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel1_location}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel1_location` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R1/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel1_time}, '')) + toStr(coalesce({view.custom.f.rel1_location}, '')) + toStr(coalesce({view.custom.f.rel1_desc}, '')) + toStr(coalesce({view.custom.f.rel1_detection}, '')) + toStr(coalesce({view.custom.f.rel1_reportable}, '')) + toStr(coalesce({view.custom.f.rel1_notified}, '')) + toStr(coalesce({view.custom.f.rel1_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel1_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel1_desc` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R1/C_detection/detection`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel1_detection` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R1/C_reportable/reportable`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel1_time}, '')) + toStr(coalesce({view.custom.f.rel1_location}, '')) + toStr(coalesce({view.custom.f.rel1_desc}, '')) + toStr(coalesce({view.custom.f.rel1_detection}, '')) + toStr(coalesce({view.custom.f.rel1_reportable}, '')) + toStr(coalesce({view.custom.f.rel1_notified}, '')) + toStr(coalesce({view.custom.f.rel1_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel1_reportable}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.rel1_reportable` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R1/C_notified/notified`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel1_notified` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R1/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.rel1_initials` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R2/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel2_time}, '')) + toStr(coalesce({view.custom.f.rel2_location}, '')) + toStr(coalesce({view.custom.f.rel2_desc}, '')) + toStr(coalesce({view.custom.f.rel2_detection}, '')) + toStr(coalesce({view.custom.f.rel2_reportable}, '')) + toStr(coalesce({view.custom.f.rel2_notified}, '')) + toStr(coalesce({view.custom.f.rel2_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel2_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel2_time` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R2/C_location/location`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel2_time}, '')) + toStr(coalesce({view.custom.f.rel2_location}, '')) + toStr(coalesce({view.custom.f.rel2_desc}, '')) + toStr(coalesce({view.custom.f.rel2_detection}, '')) + toStr(coalesce({view.custom.f.rel2_reportable}, '')) + toStr(coalesce({view.custom.f.rel2_notified}, '')) + toStr(coalesce({view.custom.f.rel2_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel2_location}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel2_location` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R2/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel2_time}, '')) + toStr(coalesce({view.custom.f.rel2_location}, '')) + toStr(coalesce({view.custom.f.rel2_desc}, '')) + toStr(coalesce({view.custom.f.rel2_detection}, '')) + toStr(coalesce({view.custom.f.rel2_reportable}, '')) + toStr(coalesce({view.custom.f.rel2_notified}, '')) + toStr(coalesce({view.custom.f.rel2_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel2_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel2_desc` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R2/C_detection/detection`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel2_detection` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R2/C_reportable/reportable`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel2_time}, '')) + toStr(coalesce({view.custom.f.rel2_location}, '')) + toStr(coalesce({view.custom.f.rel2_desc}, '')) + toStr(coalesce({view.custom.f.rel2_detection}, '')) + toStr(coalesce({view.custom.f.rel2_reportable}, '')) + toStr(coalesce({view.custom.f.rel2_notified}, '')) + toStr(coalesce({view.custom.f.rel2_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel2_reportable}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.rel2_reportable` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R2/C_notified/notified`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel2_notified` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R2/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.rel2_initials` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R3/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel3_time}, '')) + toStr(coalesce({view.custom.f.rel3_location}, '')) + toStr(coalesce({view.custom.f.rel3_desc}, '')) + toStr(coalesce({view.custom.f.rel3_detection}, '')) + toStr(coalesce({view.custom.f.rel3_reportable}, '')) + toStr(coalesce({view.custom.f.rel3_notified}, '')) + toStr(coalesce({view.custom.f.rel3_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel3_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel3_time` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R3/C_location/location`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel3_time}, '')) + toStr(coalesce({view.custom.f.rel3_location}, '')) + toStr(coalesce({view.custom.f.rel3_desc}, '')) + toStr(coalesce({view.custom.f.rel3_detection}, '')) + toStr(coalesce({view.custom.f.rel3_reportable}, '')) + toStr(coalesce({view.custom.f.rel3_notified}, '')) + toStr(coalesce({view.custom.f.rel3_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel3_location}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel3_location` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R3/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel3_time}, '')) + toStr(coalesce({view.custom.f.rel3_location}, '')) + toStr(coalesce({view.custom.f.rel3_desc}, '')) + toStr(coalesce({view.custom.f.rel3_detection}, '')) + toStr(coalesce({view.custom.f.rel3_reportable}, '')) + toStr(coalesce({view.custom.f.rel3_notified}, '')) + toStr(coalesce({view.custom.f.rel3_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel3_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel3_desc` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R3/C_detection/detection`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel3_detection` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R3/C_reportable/reportable`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel3_time}, '')) + toStr(coalesce({view.custom.f.rel3_location}, '')) + toStr(coalesce({view.custom.f.rel3_desc}, '')) + toStr(coalesce({view.custom.f.rel3_detection}, '')) + toStr(coalesce({view.custom.f.rel3_reportable}, '')) + toStr(coalesce({view.custom.f.rel3_notified}, '')) + toStr(coalesce({view.custom.f.rel3_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel3_reportable}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.rel3_reportable` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R3/C_notified/notified`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel3_notified` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R3/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.rel3_initials` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R4/C_time/time`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel4_time}, '')) + toStr(coalesce({view.custom.f.rel4_location}, '')) + toStr(coalesce({view.custom.f.rel4_desc}, '')) + toStr(coalesce({view.custom.f.rel4_detection}, '')) + toStr(coalesce({view.custom.f.rel4_reportable}, '')) + toStr(coalesce({view.custom.f.rel4_notified}, '')) + toStr(coalesce({view.custom.f.rel4_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel4_time}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel4_time` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R4/C_location/location`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel4_time}, '')) + toStr(coalesce({view.custom.f.rel4_location}, '')) + toStr(coalesce({view.custom.f.rel4_desc}, '')) + toStr(coalesce({view.custom.f.rel4_detection}, '')) + toStr(coalesce({view.custom.f.rel4_reportable}, '')) + toStr(coalesce({view.custom.f.rel4_notified}, '')) + toStr(coalesce({view.custom.f.rel4_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel4_location}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel4_location` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R4/C_desc/desc`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel4_time}, '')) + toStr(coalesce({view.custom.f.rel4_location}, '')) + toStr(coalesce({view.custom.f.rel4_desc}, '')) + toStr(coalesce({view.custom.f.rel4_detection}, '')) + toStr(coalesce({view.custom.f.rel4_reportable}, '')) + toStr(coalesce({view.custom.f.rel4_notified}, '')) + toStr(coalesce({view.custom.f.rel4_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel4_desc}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.rel4_desc` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R4/C_detection/detection`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel4_detection` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R4/C_reportable/reportable`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((len(trim(toStr(coalesce({view.custom.f.rel4_time}, '')) + toStr(coalesce({view.custom.f.rel4_location}, '')) + toStr(coalesce({view.custom.f.rel4_desc}, '')) + toStr(coalesce({view.custom.f.rel4_detection}, '')) + toStr(coalesce({view.custom.f.rel4_reportable}, '')) + toStr(coalesce({view.custom.f.rel4_notified}, '')) + toStr(coalesce({view.custom.f.rel4_initials}, '')))) > 0) && len(trim(toStr(coalesce({view.custom.f.rel4_reportable}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.rel4_reportable` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R4/C_notified/notified`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.rel4_notified` (bidirectional)

**`root/Scroll/Form/Sections/Releases/Body/Table/R4/C_initials/initials`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.rel4_initials` (bidirectional)

**`root/Scroll/Form/Sections/Maintenance/Body/Row/Wo/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.wo_completed` (bidirectional)

**`root/Scroll/Form/Sections/Maintenance/Body/Row/Permits/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.text`: property `view.custom.f.permits_active` (bidirectional)

**`root/Scroll/Form/Sections/Maintenance/Body/Row/Open/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.value`: property `view.custom.f.open_items` (bidirectional)

**`root/Scroll/Form/Sections/Maintenance/Body/Comments/Caption/Req`**

- `position.display`: expression

```js
coalesce({view.custom.f.open_items}, '') = 'Yes - See Comments'
```


**`root/Scroll/Form/Sections/Maintenance/Body/Comments/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((coalesce({view.custom.f.open_items}, '') = 'Yes - See Comments') && len(trim(toStr(coalesce({view.custom.f.comments}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.comments` (bidirectional)

**`root/Scroll/Form/Sections/Summary/Head/Req`**

- `position.display`: expression

```js
coalesce({view.custom.f.shift_status}, '') = 'Abnormal - See Notes'
```


**`root/Scroll/Form/Sections/Summary/Body/Text`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && ((coalesce({view.custom.f.shift_status}, '') = 'Abnormal - See Notes') && len(trim(toStr(coalesce({view.custom.f.summary}, '')))) = 0), 'form-input form-input-required', 'form-input')
```


- `props.text`: property `view.custom.f.summary` (bidirectional)

**`root/Scroll/Form/Sections/SignOff/Body/Row/Name/V`**

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

**`root/Scroll/Form/Sections/SignOff/Body/Row/Date/V`**

- `props.enabled`: expression

```js
!{view.custom.locked}
```


- `props.style.classes`: expression

```js
if(!{view.custom.locked} && (isNull({view.custom.f.sign_date})), 'form-input form-input-required', 'form-input')
```


- `props.value`: property `view.custom.f.sign_date` (bidirectional)

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
    if rec is None or rec['formType'] != 'ShiftLog':
        v.custom.msg = 'Submission Not Available'
        return
    v.custom.f = rec['data']
    v.custom.meta = rec['meta']
elif shared.Forms.allowed(self.session):
    v.custom.f = shared.Forms.newData(self.session, 'ShiftLog')
```

- **`root/Footer/Bar/ActionBar/Clear`** `component.onActionPerformed`, script action, scope `G`

```python
shared.Alerts.showAlert(state='warning', title='Clear Form', message='Clear every field and start a new NH3 Shift Log?', showCloseBtn=False, btnTextPrimary='Clear', btnTextSecondary='Cancel', btnActionPrimary='opsFormsClearShiftLog', btnActionSecondary='', payload={'sender': self.view.id}, overlayDismiss=False)
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
shared.Alerts.showAlert(state='info', title='Submit NH3 Shift Log', message='Submit this NH3 Shift Log? It is saved to Form History and cannot be edited afterwards.', showCloseBtn=False, btnTextPrimary='Submit', btnTextSecondary='Cancel', btnActionPrimary='opsFormsSubmitShiftLog', btnActionSecondary='', payload={'sender': self.view.id}, overlayDismiss=False)
```

- **`root/Footer/Bar/ActionBar/Print`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = shared.Forms.downloadPdf(self.session, 'ShiftLog', self.view.params.submissionId)
```

- **`root/Footer/Bar/ActionBar/New`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.f = shared.Forms.newData(self.session, 'ShiftLog')
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
self.view.custom.msg = shared.Forms.downloadPdf(self.session, 'ShiftLog', self.view.custom.result.id)
```

- **`root`** message handler `opsFormsSubmitShiftLog` (scope: page)

```python
if self.view.params.readOnly or self.view.custom.result.ok:
    return
if payload.get('sender') and payload.get('sender') != self.view.id:
    return
res = shared.Forms.submit(self.session, 'ShiftLog', self.view.custom.f)
self.view.custom.result = res
self.view.custom.msg = '' if res.get('ok') else res.get('message')
```

- **`root`** message handler `opsFormsClearShiftLog` (scope: page)

```python
if self.view.params.readOnly:
    return
if payload.get('sender') and payload.get('sender') != self.view.id:
    return
self.view.custom.f = shared.Forms.newData(self.session, 'ShiftLog')
self.view.custom.result = {'ok': False, 'id': 0, 'message': ''}
self.view.custom.msg = ''
self.view.custom.attempted = False
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Forms.allowed](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.downloadPdf](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.loadForView](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.newData](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.operatorOptions](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.submit](../../../../../../../scripting/reference/modules/shared-forms.md).

## Related Views

**Opened or named by** (4): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md), [00\_Pages/Groveport/Operations/Forms/History](./history.md), [00\_Pages/Groveport/Operations/Forms/\_Assets/HistoryActions](./assets/historyactions.md)

## Style Classes

<details>
<summary>30 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `bg-component` | 1 | stylesheet |
| `bg-page` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `form-banner` | 3 | style class |
| `form-banner-error` | 1 | style class |
| `form-banner-ok` | 1 | style class |
| `form-btn` | 3 | style class |
| `form-btn-primary` | 3 | style class |
| `form-card` | 10 | style class |
| `form-check` | 1 | style class |
| `form-input` | 95 | style class |
| `form-label` | 93 | style class |
| `form-note` | 1 | style class |
| `form-page` | 1 | stylesheet |
| `form-required-marker` | 47 | style class |
| `form-row-label` | 12 | style class |
| `form-section-head` | 8 | style class |
| `form-section-title` | 9 | style class |
| `form-stack` | 2 | stylesheet |
| `form-status` | 1 | style class |
| `form-subtitle` | 3 | style class |
| `form-td` | 76 | stylesheet |
| `form-td-cap` | 88 | stylesheet |
| `form-th` | 13 | style class |
| `form-thead` | 2 | stylesheet |
| `form-title` | 1 | style class |
| `form-tr` | 14 | stylesheet |
| `fs-16` | 1 | style class |
| `fw-600` | 1 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
