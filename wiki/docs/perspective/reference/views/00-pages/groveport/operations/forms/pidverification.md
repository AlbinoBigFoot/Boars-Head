---
title: "PidVerification"
sidebar_label: "PidVerification"
description: "Perspective view 00_Pages/Groveport/Operations/Forms/PidVerification (Page): 130 components, 84 bindings, 18 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/Forms/PidVerification", "PidVerification", "/operations/forms/pid-verification"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Operations/Forms/PidVerification`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/Forms/PidVerification` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/Forms/PidVerification/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; Forms &gt; PidVerification |
| Routes | `/operations/forms/pid-verification` (Annual P&ID Verification) |
| Root | `ia.container.flex`, height 1000, width 1600 |
| Size | 130 components, 84 bindings, 18 event handlers, 0 change scripts, 2 message handlers |
| Last saved | 2026-10-11T03:47:43Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `category` | `""` | |
| `completed` | `{"id": 0, "year": 0}` | |
| `cycle` | `{"allowed": true, "created": "", "cycle_year": "", "drawing_revisio...` | bound (expr-struct) |
| `msg` | `""` | |
| `newCycle` | `{"performed": "", "reviewed": "", "revision": "R-8 rev 04/14/20, R-...` | |
| `operators` | `[]` | |
| `refresh` | `0` | |
| `search` | `""` | |
| `sel` | `{"function_service": "", "notes": "", "pid": "", "position": "", "s...` | |
| `show` | `"All"` | |
| `summary` | `{"all": {"disc": 0, "incomplete": 0, "pct": 0.0, "pctText": "0%", "...` | bound (expr-struct) |
| `unit` | `""` | |

## Component Tree

Component types: ia.display.label x59, ia.container.flex x48, ia.input.button x8, ia.input.text-field x8, ia.input.dropdown x3, ia.display.table x1, ia.input.checkbox x1, ia.input.date-time-input x1, ia.input.text-area x1.

<details>
<summary>Component tree (130 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  Head  ia.container.flex
    Title  ia.display.label
    Subtitle  ia.display.label
  Denied  ia.container.flex  [1 binding]
    DeniedMsg  ia.display.label
  Completed  ia.container.flex  [1 binding]
    Msg  ia.display.label  [1 binding]
    Pdf  ia.input.button  [1 event]
    History  ia.input.button  [1 event]
  NoCycle  ia.container.flex  [1 binding]
    Title  ia.display.label
    Hint  ia.display.label
    Row  ia.container.flex
      Year  ia.container.flex
        Cap  ia.display.label
        V  ia.input.text-field  [1 binding]
      Rev  ia.container.flex
        Cap  ia.display.label
        V  ia.input.text-field  [1 binding]
      Perf  ia.container.flex
        Cap  ia.display.label
        V  ia.input.text-field  [1 binding]
      Rev2  ia.container.flex
        Cap  ia.display.label
        V  ia.input.text-field  [1 binding]
      Btn  ia.container.flex
        Start  ia.input.button  [1 event]
  Cycle  ia.container.flex  [1 binding]
    Title  ia.display.label
    Row  ia.container.flex
      Year  ia.display.label  [1 binding]
      Rev  ia.container.flex
        Cap  ia.display.label
        V  ia.input.text-field  [1 binding]
      Perf  ia.container.flex
        Cap  ia.display.label
        V  ia.input.text-field  [1 binding]
      Rev2  ia.container.flex
        Cap  ia.display.label
        V  ia.input.text-field  [1 binding]
      Started  ia.container.flex
        Cap  ia.display.label
        V  ia.display.label  [1 binding]
      Btns  ia.container.flex
        SaveHdr  ia.input.button  [1 event]
        Pdf  ia.input.button  [1 event]
        Complete  ia.input.button  [1 event]
  Dashboard  ia.container.flex  [1 binding]
    Card0  ia.container.flex  [1 binding; 1 event]
      Name  ia.display.label
      Count  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [1 binding]
      Detail  ia.display.label  [1 binding]
      Disc  ia.display.label  [2 bindings]
    Card1  ia.container.flex  [1 binding; 1 event]
      Name  ia.display.label
      Count  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [1 binding]
      Detail  ia.display.label  [1 binding]
      Disc  ia.display.label  [2 bindings]
    Card2  ia.container.flex  [1 binding; 1 event]
      Name  ia.display.label
      Count  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [1 binding]
      Detail  ia.display.label  [1 binding]
      Disc  ia.display.label  [2 bindings]
    Card3  ia.container.flex  [1 binding; 1 event]
      Name  ia.display.label
      Count  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [1 binding]
      Detail  ia.display.label  [1 binding]
      Disc  ia.display.label  [2 bindings]
    Card4  ia.container.flex  [1 binding; 1 event]
      Name  ia.display.label
      Count  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [1 binding]
      Detail  ia.display.label  [1 binding]
      Disc  ia.display.label  [2 bindings]
    Card5  ia.container.flex  [1 binding; 1 event]
      Name  ia.display.label
      Count  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [1 binding]
      Detail  ia.display.label  [1 binding]
      Disc  ia.display.label  [2 bindings]
    Card6  ia.container.flex  [1 binding; 1 event]
      Name  ia.display.label
      Count  ia.display.label  [1 binding]
      Bar  ia.container.flex
        Fill  ia.container.flex  [1 binding]
      Detail  ia.display.label  [1 binding]
      Disc  ia.display.label  [2 bindings]
  Filters  ia.container.flex  [1 binding]
    Cat  ia.display.label  [1 binding]
    Unit  ia.input.dropdown  [2 bindings]
    Show  ia.input.dropdown  [1 binding]
    Search  ia.input.text-field  [1 binding]
    Hint  ia.display.label
  Message  ia.display.label  [2 bindings]
  Main  ia.container.flex  [1 binding]
    Table  ia.display.table  [1 binding; 2 events]
    Editor  ia.container.flex
      Empty  ia.display.label  [1 binding]
      Valve  ia.container.flex  [1 binding]
        Title  ia.display.label
        Valve  ia.display.label  [1 binding]
        Unit  ia.display.label  [1 binding]
        Func  ia.display.label  [1 binding]
        Spec  ia.display.label  [1 binding]
        Verified  ia.input.checkbox  [1 binding]
        By  ia.container.flex
          Cap  ia.display.label
          V  ia.input.dropdown  [2 bindings]
        Date  ia.container.flex
          Cap  ia.display.label
          V  ia.input.date-time-input  [1 binding]
        Notes  ia.container.flex
          Cap  ia.display.label
          V  ia.input.text-area  [1 binding]
        Flag  ia.display.label  [1 binding]
        Btns  ia.container.flex
          Save  ia.input.button  [1 event]
          Quick  ia.input.button  [1 event]
        Updated  ia.display.label  [1 binding]
```

</details>

## Bindings

84 bindings: expr 61, property 20, expr-struct 3.

<details>
<summary>All 84 bindings, grouped by component</summary>

**`(view)`**

- `custom.cycle`: structured expression (expr-struct), then script transform

```js
refresh: {view.custom.refresh}
```

waitOnAll: `False`

Transform 1, script:

```python
return shared.Forms.pidOpenCycle(self.session)
```


- `custom.summary`: structured expression (expr-struct), then script transform

```js
category: {view.custom.category}
cycle: coalesce({view.custom.cycle.id}, 0)
refresh: {view.custom.refresh}
```

waitOnAll: `False`

Transform 1, script:

```python
return shared.Forms.pidSummary(self.session, value.cycle, value.category)
```


**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

**`root/Denied`**

- `position.display`: expression

```js
!coalesce({session.custom.Permissions.Forms.Use}, false)
```


**`root/Completed`**

- `position.display`: expression

```js
coalesce({view.custom.completed.id}, 0) > 0
```


**`root/Completed/Msg`**

- `props.text`: expression

```js
'Cycle ' + toStr({view.custom.completed.year}) + ' Completed - Print Or Download The Final Record.'
```


**`root/NoCycle`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false) && !(coalesce({view.custom.cycle.id}, 0) > 0)
```


**`root/NoCycle/Row/Year/V`**

- `props.text`: property `view.custom.newCycle.year` (bidirectional)

**`root/NoCycle/Row/Rev/V`**

- `props.text`: property `view.custom.newCycle.revision` (bidirectional)

**`root/NoCycle/Row/Perf/V`**

- `props.text`: property `view.custom.newCycle.performed` (bidirectional)

**`root/NoCycle/Row/Rev2/V`**

- `props.text`: property `view.custom.newCycle.reviewed` (bidirectional)

**`root/Cycle`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false) && coalesce({view.custom.cycle.id}, 0) > 0
```


**`root/Cycle/Row/Year`**

- `props.text`: expression

```js
'Cycle ' + toStr(coalesce({view.custom.cycle.cycle_year}, ''))
```


**`root/Cycle/Row/Rev/V`**

- `props.text`: property `view.custom.cycle.drawing_revision` (bidirectional)

**`root/Cycle/Row/Perf/V`**

- `props.text`: property `view.custom.cycle.performed_by` (bidirectional)

**`root/Cycle/Row/Rev2/V`**

- `props.text`: property `view.custom.cycle.reviewed_by` (bidirectional)

**`root/Cycle/Row/Started/V`**

- `props.text`: property `view.custom.cycle.created`

**`root/Dashboard`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false) && coalesce({view.custom.cycle.id}, 0) > 0
```


**`root/Dashboard/Card0`**

- `props.style.borderTop`: expression

```js
if(coalesce({view.custom.category}, '') = 'Compressors', '3px solid var(--accent)', '3px solid transparent')
```


**`root/Dashboard/Card0/Count`**

- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c0.verified}, 0)) + ' / ' + toStr(coalesce({view.custom.summary.c0.total}, 0))
```


**`root/Dashboard/Card0/Bar/Fill`**

- `props.style.width`: expression

```js
toStr(coalesce({view.custom.summary.c0.pct}, 0)) + '%'
```


**`root/Dashboard/Card0/Detail`**

- `props.text`: expression

```js
coalesce({view.custom.summary.c0.pctText}, '0%') + ' Complete | ' + toStr(coalesce({view.custom.summary.c0.remaining}, 0)) + ' Remaining'
```


**`root/Dashboard/Card0/Disc`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.summary.c0.incomplete}, 0) > 0, 'var(--alarm-critical)', '')
```


- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c0.disc}, 0)) + ' Discrepancies' + if(coalesce({view.custom.summary.c0.incomplete}, 0) > 0, ' | ' + toStr({view.custom.summary.c0.incomplete}) + ' No Operator', '')
```


**`root/Dashboard/Card1`**

- `props.style.borderTop`: expression

```js
if(coalesce({view.custom.category}, '') = 'Recirculators & Pumps', '3px solid var(--accent)', '3px solid transparent')
```


**`root/Dashboard/Card1/Count`**

- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c1.verified}, 0)) + ' / ' + toStr(coalesce({view.custom.summary.c1.total}, 0))
```


**`root/Dashboard/Card1/Bar/Fill`**

- `props.style.width`: expression

```js
toStr(coalesce({view.custom.summary.c1.pct}, 0)) + '%'
```


**`root/Dashboard/Card1/Detail`**

- `props.text`: expression

```js
coalesce({view.custom.summary.c1.pctText}, '0%') + ' Complete | ' + toStr(coalesce({view.custom.summary.c1.remaining}, 0)) + ' Remaining'
```


**`root/Dashboard/Card1/Disc`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.summary.c1.incomplete}, 0) > 0, 'var(--alarm-critical)', '')
```


- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c1.disc}, 0)) + ' Discrepancies' + if(coalesce({view.custom.summary.c1.incomplete}, 0) > 0, ' | ' + toStr({view.custom.summary.c1.incomplete}) + ' No Operator', '')
```


**`root/Dashboard/Card2`**

- `props.style.borderTop`: expression

```js
if(coalesce({view.custom.category}, '') = 'Receivers & Vessels', '3px solid var(--accent)', '3px solid transparent')
```


**`root/Dashboard/Card2/Count`**

- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c2.verified}, 0)) + ' / ' + toStr(coalesce({view.custom.summary.c2.total}, 0))
```


**`root/Dashboard/Card2/Bar/Fill`**

- `props.style.width`: expression

```js
toStr(coalesce({view.custom.summary.c2.pct}, 0)) + '%'
```


**`root/Dashboard/Card2/Detail`**

- `props.text`: expression

```js
coalesce({view.custom.summary.c2.pctText}, '0%') + ' Complete | ' + toStr(coalesce({view.custom.summary.c2.remaining}, 0)) + ' Remaining'
```


**`root/Dashboard/Card2/Disc`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.summary.c2.incomplete}, 0) > 0, 'var(--alarm-critical)', '')
```


- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c2.disc}, 0)) + ' Discrepancies' + if(coalesce({view.custom.summary.c2.incomplete}, 0) > 0, ' | ' + toStr({view.custom.summary.c2.incomplete}) + ' No Operator', '')
```


**`root/Dashboard/Card3`**

- `props.style.borderTop`: expression

```js
if(coalesce({view.custom.category}, '') = 'Evaporative Condensers', '3px solid var(--accent)', '3px solid transparent')
```


**`root/Dashboard/Card3/Count`**

- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c3.verified}, 0)) + ' / ' + toStr(coalesce({view.custom.summary.c3.total}, 0))
```


**`root/Dashboard/Card3/Bar/Fill`**

- `props.style.width`: expression

```js
toStr(coalesce({view.custom.summary.c3.pct}, 0)) + '%'
```


**`root/Dashboard/Card3/Detail`**

- `props.text`: expression

```js
coalesce({view.custom.summary.c3.pctText}, '0%') + ' Complete | ' + toStr(coalesce({view.custom.summary.c3.remaining}, 0)) + ' Remaining'
```


**`root/Dashboard/Card3/Disc`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.summary.c3.incomplete}, 0) > 0, 'var(--alarm-critical)', '')
```


- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c3.disc}, 0)) + ' Discrepancies' + if(coalesce({view.custom.summary.c3.incomplete}, 0) > 0, ' | ' + toStr({view.custom.summary.c3.incomplete}) + ' No Operator', '')
```


**`root/Dashboard/Card4`**

- `props.style.borderTop`: expression

```js
if(coalesce({view.custom.category}, '') = 'Truck Dock & Pallet Air Units', '3px solid var(--accent)', '3px solid transparent')
```


**`root/Dashboard/Card4/Count`**

- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c4.verified}, 0)) + ' / ' + toStr(coalesce({view.custom.summary.c4.total}, 0))
```


**`root/Dashboard/Card4/Bar/Fill`**

- `props.style.width`: expression

```js
toStr(coalesce({view.custom.summary.c4.pct}, 0)) + '%'
```


**`root/Dashboard/Card4/Detail`**

- `props.text`: expression

```js
coalesce({view.custom.summary.c4.pctText}, '0%') + ' Complete | ' + toStr(coalesce({view.custom.summary.c4.remaining}, 0)) + ' Remaining'
```


**`root/Dashboard/Card4/Disc`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.summary.c4.incomplete}, 0) > 0, 'var(--alarm-critical)', '')
```


- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c4.disc}, 0)) + ' Discrepancies' + if(coalesce({view.custom.summary.c4.incomplete}, 0) > 0, ' | ' + toStr({view.custom.summary.c4.incomplete}) + ' No Operator', '')
```


**`root/Dashboard/Card5`**

- `props.style.borderTop`: expression

```js
if(coalesce({view.custom.category}, '') = 'System & Misc', '3px solid var(--accent)', '3px solid transparent')
```


**`root/Dashboard/Card5/Count`**

- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c5.verified}, 0)) + ' / ' + toStr(coalesce({view.custom.summary.c5.total}, 0))
```


**`root/Dashboard/Card5/Bar/Fill`**

- `props.style.width`: expression

```js
toStr(coalesce({view.custom.summary.c5.pct}, 0)) + '%'
```


**`root/Dashboard/Card5/Detail`**

- `props.text`: expression

```js
coalesce({view.custom.summary.c5.pctText}, '0%') + ' Complete | ' + toStr(coalesce({view.custom.summary.c5.remaining}, 0)) + ' Remaining'
```


**`root/Dashboard/Card5/Disc`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.summary.c5.incomplete}, 0) > 0, 'var(--alarm-critical)', '')
```


- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.c5.disc}, 0)) + ' Discrepancies' + if(coalesce({view.custom.summary.c5.incomplete}, 0) > 0, ' | ' + toStr({view.custom.summary.c5.incomplete}) + ' No Operator', '')
```


**`root/Dashboard/Card6`**

- `props.style.borderTop`: expression

```js
if(coalesce({view.custom.category}, '') = '', '3px solid var(--accent)', '3px solid transparent')
```


**`root/Dashboard/Card6/Count`**

- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.all.verified}, 0)) + ' / ' + toStr(coalesce({view.custom.summary.all.total}, 0))
```


**`root/Dashboard/Card6/Bar/Fill`**

- `props.style.width`: expression

```js
toStr(coalesce({view.custom.summary.all.pct}, 0)) + '%'
```


**`root/Dashboard/Card6/Detail`**

- `props.text`: expression

```js
coalesce({view.custom.summary.all.pctText}, '0%') + ' Complete | ' + toStr(coalesce({view.custom.summary.all.remaining}, 0)) + ' Remaining'
```


**`root/Dashboard/Card6/Disc`**

- `props.style.color`: expression

```js
if(coalesce({view.custom.summary.all.incomplete}, 0) > 0, 'var(--alarm-critical)', '')
```


- `props.text`: expression

```js
toStr(coalesce({view.custom.summary.all.disc}, 0)) + ' Discrepancies' + if(coalesce({view.custom.summary.all.incomplete}, 0) > 0, ' | ' + toStr({view.custom.summary.all.incomplete}) + ' No Operator', '')
```


**`root/Filters`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false) && coalesce({view.custom.cycle.id}, 0) > 0
```


**`root/Filters/Cat`**

- `props.text`: expression

```js
if(len(coalesce({view.custom.category}, '')) > 0, {view.custom.category}, 'All Categories')
```


**`root/Filters/Unit`**

- `props.options`: property `view.custom.summary.units`

- `props.value`: property `view.custom.unit` (bidirectional)

**`root/Filters/Show`**

- `props.value`: property `view.custom.show` (bidirectional)

**`root/Filters/Search`**

- `props.text`: property `view.custom.search` (bidirectional)

**`root/Message`**

- `position.display`: expression

```js
len(coalesce({view.custom.msg}, '')) > 0
```


- `props.text`: property `view.custom.msg`

**`root/Main`**

- `position.display`: expression

```js
coalesce({session.custom.Permissions.Forms.Use}, false) && coalesce({view.custom.cycle.id}, 0) > 0
```


**`root/Main/Table`**

- `props.data`: structured expression (expr-struct), then script transform

```js
category: {view.custom.category}
cycle: coalesce({view.custom.cycle.id}, 0)
refresh: {view.custom.refresh}
search: {view.custom.search}
show: {view.custom.show}
unit: {view.custom.unit}
```

waitOnAll: `False`

Transform 1, script:

```python
if not value.cycle:
    return []
return shared.Forms.pidRows(self.session, value.cycle, value.category, value.unit, value.search, value.show)
```


**`root/Main/Editor/Empty`**

- `position.display`: expression

```js
coalesce({view.custom.sel.valve_pk}, 0) = 0
```


**`root/Main/Editor/Valve`**

- `position.display`: expression

```js
coalesce({view.custom.sel.valve_pk}, 0) > 0
```


**`root/Main/Editor/Valve/Valve`**

- `props.text`: expression

```js
coalesce({view.custom.sel.unit_id}, '') + '  ' + coalesce({view.custom.sel.valve_id}, '')
```


**`root/Main/Editor/Valve/Unit`**

- `props.text`: property `view.custom.sel.unit_desc`

**`root/Main/Editor/Valve/Func`**

- `props.text`: property `view.custom.sel.function_service`

**`root/Main/Editor/Valve/Spec`**

- `props.text`: expression

```js
'P&ID ' + coalesce({view.custom.sel.pid}, '-') + ' | Size ' + coalesce({view.custom.sel.size}, '-') + ' | ' + coalesce({view.custom.sel.valve_type}, '-') + ' | ' + coalesce({view.custom.sel.position}, '-')
```


**`root/Main/Editor/Valve/Verified`**

- `props.selected`: property `view.custom.sel.verified` (bidirectional)

**`root/Main/Editor/Valve/By/V`**

- `props.options`: property `view.custom.operators`

- `props.value`: property `view.custom.sel.verified_by` (bidirectional)

**`root/Main/Editor/Valve/Date/V`**

- `props.value`: property `view.custom.sel.verified_date` (bidirectional)

**`root/Main/Editor/Valve/Notes/V`**

- `props.text`: property `view.custom.sel.notes` (bidirectional)

**`root/Main/Editor/Valve/Flag`**

- `position.display`: expression

```js
coalesce({view.custom.sel.verified}, false) && len(trim(coalesce({view.custom.sel.verified_by}, ''))) = 0
```


**`root/Main/Editor/Valve/Updated`**

- `props.text`: expression

```js
if(len(coalesce({view.custom.sel.updated}, '')) > 0, 'Last Saved: ' + {view.custom.sel.updated}, 'Not Recorded Yet')
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 20 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
self.view.custom.operators = shared.Forms.operatorOptions(self.session)
self.view.custom.newCycle = {'year': system.date.getYear(system.date.now()), 'revision': shared.Forms.pidDefaultRevision(), 'performed': shared.Forms.displayName(self.session), 'reviewed': ''}
```

- **`root/Completed/Pdf`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = shared.Forms.downloadPdf(self.session, 'PidCycle', self.view.custom.completed.id)
```

- **`root/Completed/History`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.navigate('/operations/forms/history')
```

- **`root/NoCycle/Row/Btn/Start`** `component.onActionPerformed`, script action, scope `G`

```python
n = self.view.custom.newCycle
res = shared.Forms.pidStartCycle(self.session, n.year, n.revision, n.performed, n.reviewed)
self.view.custom.msg = res['message']
if res.get('ok'):
    self.view.custom.completed = {'id': 0, 'year': 0}
    self.view.custom.refresh += 1
```

- **`root/Cycle/Row/Btns/SaveHdr`** `component.onActionPerformed`, script action, scope `G`

```python
c = self.view.custom.cycle
res = shared.Forms.pidSaveHeader(self.session, c.id, c.drawing_revision, c.performed_by, c.reviewed_by)
self.view.custom.msg = res['message']
```

- **`root/Cycle/Row/Btns/Pdf`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = shared.Forms.downloadPdf(self.session, 'PidCycle', self.view.custom.cycle.id)
```

- **`root/Cycle/Row/Btns/Complete`** `component.onActionPerformed`, script action, scope `G`

```python
s = self.view.custom.summary.all
c = self.view.custom.cycle
msg = 'Complete the %s P&ID verification cycle?<br><br>' % c.cycle_year
msg += '%s of %s valves verified, %s remaining, %s discrepancies' % (s.verified, s.total, s.remaining, s.disc)
if s.incomplete:
    msg += ', %s verified without an operator' % s.incomplete
msg += '.<br>A completed cycle is read only and moves to Form History.'
shared.Alerts.showAlert(state='warning', title='Complete Cycle', message=msg, showCloseBtn=False, btnTextPrimary='Complete', btnTextSecondary='Cancel', btnActionPrimary='opsFormsPidComplete', btnActionSecondary='', payload={'sender': self.view.id}, overlayDismiss=False)
```

- **`root/Dashboard/Card0`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.category = 'Compressors'
self.view.custom.unit = ''
```

- **`root/Dashboard/Card1`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.category = 'Recirculators & Pumps'
self.view.custom.unit = ''
```

- **`root/Dashboard/Card2`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.category = 'Receivers & Vessels'
self.view.custom.unit = ''
```

- **`root/Dashboard/Card3`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.category = 'Evaporative Condensers'
self.view.custom.unit = ''
```

- **`root/Dashboard/Card4`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.category = 'Truck Dock & Pallet Air Units'
self.view.custom.unit = ''
```

- **`root/Dashboard/Card5`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.category = 'System & Misc'
self.view.custom.unit = ''
```

- **`root/Dashboard/Card6`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.category = ''
self.view.custom.unit = ''
```

- **`root/Main/Table`** `component.onEditCellCommit`, script action, scope `G`

```python
# Inline edits save immediately (Verified checkbox: Verified By / Date default to you / today)
row = self.props.data[event.row]
res = shared.Forms.pidSetField(self.session, self.view.custom.cycle.id, row['valve_pk'], event.column, event.value)
self.view.custom.msg = res['message']
if self.view.custom.sel.valve_pk == row['valve_pk']:
    self.view.custom.sel = shared.Forms.pidCheck(self.session, self.view.custom.cycle.id, row['valve_pk'])
self.view.custom.refresh += 1
```

- **`root/Main/Table`** `component.onSelectionChange`, script action, scope `G`

```python
rows = self.props.selection.data or []
if not rows:
    return
self.view.custom.sel = shared.Forms.pidCheck(self.session, self.view.custom.cycle.id, rows[0]['valve_pk'])
```

- **`root/Main/Editor/Valve/Btns/Save`** `component.onActionPerformed`, script action, scope `G`

```python
s = self.view.custom.sel
res = shared.Forms.pidSaveCheck(self.session, self.view.custom.cycle.id, s.valve_pk, s.verified, s.verified_by, s.verified_date, s.notes)
self.view.custom.msg = res['message']
self.view.custom.sel = shared.Forms.pidCheck(self.session, self.view.custom.cycle.id, s.valve_pk)
self.view.custom.refresh += 1
```

- **`root/Main/Editor/Valve/Btns/Quick`** `component.onActionPerformed`, script action, scope `G`

```python
s = self.view.custom.sel
res = shared.Forms.pidSaveCheck(self.session, self.view.custom.cycle.id, s.valve_pk, True, s.verified_by, s.verified_date, s.notes, quick=True)
self.view.custom.msg = res['message']
self.view.custom.sel = shared.Forms.pidCheck(self.session, self.view.custom.cycle.id, s.valve_pk)
self.view.custom.refresh += 1
```

- **`root`** message handler `opsFormsPidComplete` (scope: page)

```python
if payload.get('sender') and payload.get('sender') != self.view.id:
    return
c = self.view.custom.cycle
res = shared.Forms.pidComplete(self.session, c.id)
self.view.custom.msg = res['message']
if res.get('ok'):
    self.view.custom.completed = {'id': c.id, 'year': c.cycle_year}
    self.view.custom.sel = shared.Forms.pidBlankSel()
self.view.custom.refresh += 1
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Forms.displayName](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.downloadPdf](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.operatorOptions](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidBlankSel](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidCheck](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidComplete](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidDefaultRevision](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidOpenCycle](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidRows](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidSaveCheck](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidSaveHeader](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidSetField](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidStartCycle](../../../../../../../scripting/reference/modules/shared-forms.md), [shared.Forms.pidSummary](../../../../../../../scripting/reference/modules/shared-forms.md).

## Related Views

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

## Style Classes

<details>
<summary>22 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Button` | 4 | style class |
| `Fonts/Label` | 46 | style class |
| `Fonts/Title` | 3 | style class |
| `Fonts/Value` | 28 | style class |
| `bg-component` | 15 | stylesheet |
| `bg-page` | 1 | style class |
| `container-button` | 4 | style class |
| `container-card` | 1 | stylesheet |
| `faceplate-cmd-btn` | 4 | style class |
| `faceplate-section` | 4 | style class |
| `faceplate-section-card` | 11 | style class |
| `faceplate-section-title` | 3 | style class |
| `fs-11` | 26 | style class |
| `fs-12` | 14 | style class |
| `fs-13` | 1 | style class |
| `fs-14` | 2 | style class |
| `fs-16` | 1 | style class |
| `fs-18` | 9 | style class |
| `fs-20` | 1 | style class |
| `fw-600` | 14 | style class |
| `fw-700` | 20 | style class |
| `text-muted` | 3 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).
