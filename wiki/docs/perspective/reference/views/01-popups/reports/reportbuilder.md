---
title: "ReportBuilder"
sidebar_label: "ReportBuilder"
description: "Perspective view 01_Popups/Reports/ReportBuilder (Popup / faceplate): 185 components, 103 bindings, 28 event scripts."
generated: true
keywords: ["01_Popups/Reports/ReportBuilder", "ReportBuilder"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/Reports/ReportBuilder`.

| | |
|---|---|
| View path | `01_Popups/Reports/ReportBuilder` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/ReportBuilder/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; ReportBuilder |
| Root | `ia.container.flex`, height 720, width 1318 |
| Size | 185 components, 103 bindings, 24 event handlers, 4 change scripts, 4 message handlers |
| Last saved | 2026-10-24T14:46:23Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `context` | `{}` | input |
| `sourceId` | `""` | input |
| `templateId` | `0` | input |

## Custom properties

<details>
<summary>18 custom properties</summary>

| Name | Default | Notes |
|---|---|---|
| `advanced` | `false` | |
| `ctx` | `{"manage": false, "share": false, "use": false}` | |
| `def` | `{"breakdown": "day", "filters": {}, "format": "PDF", "measures": []...` | |
| `format` | `"PDF"` | |
| `loading` | `false` | bound (expr) |
| `model` | `{}` | bound (expr-struct) |
| `msg` | `""` | |
| `noSources` | `false` | |
| `preview` | `{"empty": false, "instances": [], "message": "", "meta": {}, "ok": ...` | bound (expr-struct) |
| `railTab` | `"templates"` | |
| `refresh` | `0` | |
| `runKey` | `0` | |
| `saved` | `[]` | bound (expr-struct) |
| `step` | `1` | |
| `templateCanEdit` | `false` | |
| `templateId` | `0` | |
| `templateName` | `""` | |
| `templateShared` | `false` | |

</details>

## Component Tree

Component types: ia.container.flex x80, ia.display.label x58, ia.input.button x15, ia.display.icon x13, ia.display.flex-repeater x13, ia.input.date-time-input x2, ia.input.text-field x2, ia.input.text-area x1, ia.input.checkbox x1.

<details>
<summary>Component tree (185 components)</summary>

```text
root  ia.container.flex  [2 bindings; 1 event]
  Header  ia.container.flex
    Logo  ia.display.icon
    Title  ia.display.label
    Origin  ia.display.label  [1 binding]
    Close  ia.display.icon  [1 event]
  Stepper  ia.container.flex  [1 binding]
    Steps  ia.container.flex
      Step1  ia.container.flex  [1 event]
        Dot1  ia.container.flex  [1 binding]
          Num  ia.display.label  [2 bindings]
          Done  ia.display.icon  [1 binding]
        Label1  ia.display.label  [1 binding]
      Line1  ia.container.flex  [1 binding]
      Step2  ia.container.flex  [1 event]
        Dot2  ia.container.flex  [1 binding]
          Num  ia.display.label  [2 bindings]
          Done  ia.display.icon  [1 binding]
        Label2  ia.display.label  [1 binding]
      Line2  ia.container.flex  [1 binding]
      Step3  ia.container.flex  [1 event]
        Dot3  ia.container.flex  [1 binding]
          Num  ia.display.label  [2 bindings]
          Done  ia.display.icon  [1 binding]
        Label3  ia.display.label  [1 binding]
      Line3  ia.container.flex  [1 binding]
      Step4  ia.container.flex  [1 event]
        Dot4  ia.container.flex  [1 binding]
          Num  ia.display.label  [2 bindings]
          Done  ia.display.icon  [1 binding]
        Label4  ia.display.label  [1 binding]
  Body  ia.container.flex
    Step1  ia.container.flex  [1 binding]
      Main  ia.container.flex
        Heading  ia.container.flex
          Title  ia.display.label
          Sub  ia.display.label
        Sources  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/SourceCard]
        QuickCap  ia.display.label
        Quick  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/ChoiceTile]
      Saved  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
        Body  ia.container.flex
          Tabs  ia.container.flex
            Tab_templates  ia.display.label  [1 binding; 1 event]
            Tab_recent  ia.display.label  [1 binding; 1 event]
          Saved  ia.display.flex-repeater  [2 bindings; view: 01_Popups/Reports/_Assets/SavedRow]
          Empty  ia.container.flex  [1 binding]
            Icon  ia.display.icon
            Title  ia.display.label  [1 binding]
            Text  ia.display.label  [1 binding]
    Step2  ia.container.flex  [1 binding]
      Main  ia.container.flex
        Heading  ia.container.flex
          Title  ia.display.label
          Sub  ia.display.label
        TimeCap  ia.display.label
        Time  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/ChoiceTile]
        Dates  ia.container.flex  [1 binding]
          From  ia.container.flex
            Cap  ia.display.label
            Start  ia.input.date-time-input  [1 binding]
          To  ia.container.flex
            Cap  ia.display.label
            End  ia.input.date-time-input  [1 binding]
        GroupCap  ia.display.label
        GroupBy  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/ChoiceTile]
        ShiftCap  ia.display.label  [1 binding]
        Shifts  ia.display.flex-repeater  [2 bindings; view: 01_Popups/Reports/_Assets/ChoiceTile]
      Summary  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
        Body  ia.container.flex
          Lines  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/SummaryLine]
    Step3  ia.container.flex  [1 binding]
      Main  ia.container.flex
        Heading  ia.container.flex
          Title  ia.display.label
          Sub  ia.display.label
        Basic  ia.container.flex  [1 binding]
          Scope  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label  [1 binding]
            Body  ia.container.flex
              Items  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/CheckItem]
              Hint  ia.display.label
          Measures  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
            Body  ia.container.flex
              Items  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/CheckItem]
        AdvancedPanels  ia.container.flex  [1 binding]
          SectionsPanel  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
            Body  ia.container.flex
              Sections  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/SectionItem]
          Wording  ia.container.flex
            Head  ia.container.flex
              Title  ia.display.label
            Body  ia.container.flex
              FilterCap  ia.display.label  [2 bindings]
              Filters  ia.display.flex-repeater  [2 bindings; view: 01_Popups/Reports/_Assets/ChoiceTile]
              TitleField  ia.container.flex
                Cap  ia.display.label
                Title  ia.input.text-field  [1 binding]
              NotesField  ia.container.flex
                Cap  ia.display.label
                Notes  ia.input.text-area  [1 binding]
        Advanced  ia.container.flex  [1 binding; 1 event]
          Icon  ia.display.icon
          Title  ia.display.label
          Hint  ia.display.label  [1 binding]
          Chevron  ia.display.icon  [1 binding]
      Summary  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
        Body  ia.container.flex
          Lines  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/SummaryLine]
    Step4  ia.container.flex  [1 binding]
      Preview  ia.container.flex
        Head  ia.container.flex
          Title  ia.display.label
          Note  ia.display.label
        Body  ia.container.flex
          Titles  ia.container.flex  [1 binding]
            Title  ia.display.label  [1 binding]
            Meta  ia.display.label  [1 binding]
          Error  ia.display.label  [2 bindings]
          Sections  ia.display.flex-repeater  [2 bindings; view: 01_Popups/Reports/_Assets/PreviewSection]
          Loading  ia.container.flex  [1 binding]
            Icon  ia.display.icon
            Title  ia.display.label
            Text  ia.display.label
            Buttons  ia.container.flex
          NoData  ia.container.flex  [1 binding]
            Icon  ia.display.icon
            Title  ia.display.label
            Text  ia.display.label
            Buttons  ia.container.flex
              ChangeTime  ia.input.button  [1 event]
          Failed  ia.container.flex  [1 binding]
            Icon  ia.display.icon
            Title  ia.display.label
            Text  ia.display.label
            Buttons  ia.container.flex
              Retry  ia.input.button  [1 event]
              ChangeTime  ia.input.button  [1 event]
      Rail  ia.container.flex
        Download  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label
          Body  ia.container.flex
            FmtCap  ia.display.label
            Formats  ia.container.flex
              F_PDF  ia.input.button  [1 binding; 1 event]
              F_Excel  ia.input.button  [1 binding; 1 event]
              F_CSV  ia.input.button  [1 binding; 1 event]
            Hint  ia.display.label
            Download  ia.input.button  [4 bindings; 1 event]
        Save  ia.container.flex
          Head  ia.container.flex
            Title  ia.display.label  [1 binding]
          Body  ia.container.flex
            NameField  ia.container.flex
              Cap  ia.display.label
              Name  ia.input.text-field  [1 binding]
            ShareRow  ia.container.flex
              Shared  ia.input.checkbox  [2 bindings]
              Save  ia.input.button  [1 binding; 1 event]
            TplRow  ia.container.flex  [1 binding]
              SaveAs  ia.input.button  [1 event]
              Delete  ia.input.button  [1 binding; 1 event]
    Denied  ia.container.flex  [1 binding]
      Icon  ia.display.icon
      Title  ia.display.label  [1 binding]
      Text  ia.display.label  [1 binding]
  Footer  ia.container.flex
    Status  ia.display.label  [1 binding]
    Cancel  ia.input.button  [1 binding; 1 event]
    Back  ia.input.button  [1 binding; 1 event]
    Skip  ia.input.button  [1 binding; 1 event]
    StartOver  ia.input.button  [1 binding; 1 event]
    Next  ia.input.button  [2 bindings; 1 event]
```

</details>

## Bindings

103 bindings: expr 85, property 15, expr-struct 3.

<details>
<summary>All 103 bindings, grouped by component</summary>

**`(view)`**

- `custom.loading`: expression

```js
coalesce({view.custom.step}, 1) = 4 && !coalesce({view.custom.preview.ran}, false)
```


- `custom.model`: structured expression (expr-struct), then script transform

```js
def: {view.custom.def}
ok: len(coalesce({view.custom.def.source}, '')) > 0 && coalesce({view.custom.ctx.use}, false)
```

waitOnAll: `False`

Transform 1, script:

```python

if not value.ok:
    return {}
return shared.Reports.builderModel(self.session, value['def'])
```


- `custom.preview`: structured expression (expr-struct), then script transform

```js
def: {view.custom.def}
ok: len(coalesce({view.custom.def.source}, '')) > 0 && coalesce({view.custom.ctx.use}, false)
run: {view.custom.runKey}
step: {view.custom.step}
vw: {page.props.dimensions.viewport.width}
```

waitOnAll: `False`

Transform 1, script:

```python
# Step 4 preview: the same engine as the download, first rows only
if not value.ok or value.step != 4:
    return {'ok': True, 'message': '', 'meta': {}, 'instances': [], 'empty': False, 'ran': False}
return shared.Reports.previewInstances(self.session, value['def'], value.vw)
```


- `custom.saved`: structured expression (expr-struct), then script transform

```js
ok: coalesce({view.custom.ctx.use}, false)
refresh: {view.custom.refresh}
tab: {view.custom.railTab}
```

waitOnAll: `False`

Transform 1, script:

```python
# saved templates / recent downloads (named queries)
if not value.ok:
    return []
return shared.Reports.savedList(self.session, value.tab or 'templates')
```


**`root`**

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

**`root/Header/Origin`**

- `props.text`: expression

```js
if(len(coalesce({view.params.context.origin}, '')) > 0, 'From ' + {view.params.context.origin}, '')
```


**`root/Stepper`**

- `position.display`: expression

```js
coalesce({view.custom.ctx.use}, false) && !coalesce({view.custom.noSources}, false)
```


**`root/Stepper/Steps/Step1/Dot1`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 1 || coalesce({view.custom.step}, 1) > 1, 'report-step-dot report-step-dot-on', 'report-step-dot')
```


**`root/Stepper/Steps/Step1/Dot1/Num`**

- `position.display`: expression

```js
!(coalesce({view.custom.step}, 1) > 1)
```


- `props.style.color`: expression

```js
if(coalesce({view.custom.step}, 1) = 1, 'var(--neutral-10)', 'var(--text-muted)')
```


**`root/Stepper/Steps/Step1/Dot1/Done`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) > 1
```


**`root/Stepper/Steps/Step1/Label1`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 1, 'report-step-label report-step-label-current', if(coalesce({view.custom.step}, 1) > 1, 'report-step-label report-step-label-done', 'report-step-label'))
```


**`root/Stepper/Steps/Line1`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) > 1, 'report-step-line report-step-line-done', 'report-step-line')
```


**`root/Stepper/Steps/Step2/Dot2`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 2 || coalesce({view.custom.step}, 1) > 2, 'report-step-dot report-step-dot-on', 'report-step-dot')
```


**`root/Stepper/Steps/Step2/Dot2/Num`**

- `position.display`: expression

```js
!(coalesce({view.custom.step}, 1) > 2)
```


- `props.style.color`: expression

```js
if(coalesce({view.custom.step}, 1) = 2, 'var(--neutral-10)', 'var(--text-muted)')
```


**`root/Stepper/Steps/Step2/Dot2/Done`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) > 2
```


**`root/Stepper/Steps/Step2/Label2`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 2, 'report-step-label report-step-label-current', if(coalesce({view.custom.step}, 1) > 2, 'report-step-label report-step-label-done', 'report-step-label'))
```


**`root/Stepper/Steps/Line2`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) > 2, 'report-step-line report-step-line-done', 'report-step-line')
```


**`root/Stepper/Steps/Step3/Dot3`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 3 || coalesce({view.custom.step}, 1) > 3, 'report-step-dot report-step-dot-on', 'report-step-dot')
```


**`root/Stepper/Steps/Step3/Dot3/Num`**

- `position.display`: expression

```js
!(coalesce({view.custom.step}, 1) > 3)
```


- `props.style.color`: expression

```js
if(coalesce({view.custom.step}, 1) = 3, 'var(--neutral-10)', 'var(--text-muted)')
```


**`root/Stepper/Steps/Step3/Dot3/Done`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) > 3
```


**`root/Stepper/Steps/Step3/Label3`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 3, 'report-step-label report-step-label-current', if(coalesce({view.custom.step}, 1) > 3, 'report-step-label report-step-label-done', 'report-step-label'))
```


**`root/Stepper/Steps/Line3`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) > 3, 'report-step-line report-step-line-done', 'report-step-line')
```


**`root/Stepper/Steps/Step4/Dot4`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 4 || coalesce({view.custom.step}, 1) > 4, 'report-step-dot report-step-dot-on', 'report-step-dot')
```


**`root/Stepper/Steps/Step4/Dot4/Num`**

- `position.display`: expression

```js
!(coalesce({view.custom.step}, 1) > 4)
```


- `props.style.color`: expression

```js
if(coalesce({view.custom.step}, 1) = 4, 'var(--neutral-10)', 'var(--text-muted)')
```


**`root/Stepper/Steps/Step4/Dot4/Done`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) > 4
```


**`root/Stepper/Steps/Step4/Label4`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.step}, 1) = 4, 'report-step-label report-step-label-current', if(coalesce({view.custom.step}, 1) > 4, 'report-step-label report-step-label-done', 'report-step-label'))
```


**`root/Body/Step1`**

- `position.display`: expression

```js
coalesce({view.custom.ctx.use}, false) && !coalesce({view.custom.noSources}, false) && coalesce({view.custom.step}, 1) = 1
```


**`root/Body/Step1/Main/Sources`**

- `props.instances`: property `view.custom.model.sources`

**`root/Body/Step1/Main/Quick`**

- `props.instances`: property `view.custom.model.quick`

**`root/Body/Step1/Saved/Body/Tabs/Tab_templates`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.railTab}, 'templates') = 'templates', 'report-tab report-tab-active', 'report-tab')
```


**`root/Body/Step1/Saved/Body/Tabs/Tab_recent`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.railTab}, 'templates') = 'recent', 'report-tab report-tab-active', 'report-tab')
```


**`root/Body/Step1/Saved/Body/Saved`**

- `position.display`: expression

```js
len(coalesce({view.custom.saved}, [])) > 0
```


- `props.instances`: property `view.custom.saved`

**`root/Body/Step1/Saved/Body/Empty`**

- `position.display`: expression

```js
len(coalesce({view.custom.saved}, [])) < 1
```


**`root/Body/Step1/Saved/Body/Empty/Title`**

- `props.text`: expression

```js
if(coalesce({view.custom.railTab}, 'templates') = 'recent', 'No Recent Reports Yet', 'No Saved Reports Yet')
```


**`root/Body/Step1/Saved/Body/Empty/Text`**

- `props.text`: expression

```js
if(coalesce({view.custom.railTab}, 'templates') = 'recent', 'Your Last 10 Downloads Appear Here.', 'Build A Report, Then Use Save As Template On The Last Step.')
```


**`root/Body/Step2`**

- `position.display`: expression

```js
coalesce({view.custom.ctx.use}, false) && !coalesce({view.custom.noSources}, false) && coalesce({view.custom.step}, 1) = 2
```


**`root/Body/Step2/Main/Time`**

- `props.instances`: property `view.custom.model.time`

**`root/Body/Step2/Main/Dates`**

- `position.display`: expression

```js
coalesce({view.custom.model.custom}, false)
```


**`root/Body/Step2/Main/Dates/From/Start`**

- `props.value`: expression

```js
coalesce({view.custom.model.customStart}, now(0))
```


**`root/Body/Step2/Main/Dates/To/End`**

- `props.value`: expression

```js
coalesce({view.custom.model.customEnd}, now(0))
```


**`root/Body/Step2/Main/GroupBy`**

- `props.instances`: property `view.custom.model.groupBy`

**`root/Body/Step2/Main/ShiftCap`**

- `position.display`: expression

```js
coalesce({view.custom.model.hasShifts}, false)
```


**`root/Body/Step2/Main/Shifts`**

- `position.display`: expression

```js
coalesce({view.custom.model.hasShifts}, false)
```


- `props.instances`: property `view.custom.model.shifts`

**`root/Body/Step2/Summary/Body/Lines`**

- `props.instances`: property `view.custom.model.summary`, then script transform

Transform 1, script:

```python
return [{'line': l} for l in (value or [])]
```


**`root/Body/Step3`**

- `position.display`: expression

```js
coalesce({view.custom.ctx.use}, false) && !coalesce({view.custom.noSources}, false) && coalesce({view.custom.step}, 1) = 3
```


**`root/Body/Step3/Main/Basic`**

- `position.display`: expression

```js
!coalesce({view.custom.advanced}, false)
```


**`root/Body/Step3/Main/Basic/Scope/Head/Title`**

- `props.text`: expression

```js
coalesce({view.custom.model.scopeTitle}, 'Scope')
```


**`root/Body/Step3/Main/Basic/Scope/Body/Items`**

- `props.instances`: property `view.custom.model.scope`

**`root/Body/Step3/Main/Basic/Measures/Body/Items`**

- `props.instances`: property `view.custom.model.measures`

**`root/Body/Step3/Main/AdvancedPanels`**

- `position.display`: expression

```js
coalesce({view.custom.advanced}, false)
```


**`root/Body/Step3/Main/AdvancedPanels/SectionsPanel/Body/Sections`**

- `props.instances`: property `view.custom.model.sections`

**`root/Body/Step3/Main/AdvancedPanels/Wording/Body/FilterCap`**

- `position.display`: expression

```js
coalesce({view.custom.model.hasFilters}, false)
```


- `props.text`: expression

```js
coalesce({view.custom.model.filterLabel}, '')
```


**`root/Body/Step3/Main/AdvancedPanels/Wording/Body/Filters`**

- `position.display`: expression

```js
coalesce({view.custom.model.hasFilters}, false)
```


- `props.instances`: property `view.custom.model.filters`

**`root/Body/Step3/Main/AdvancedPanels/Wording/Body/TitleField/Title`**

- `props.text`: expression

```js
coalesce({view.custom.def.title}, '')
```


**`root/Body/Step3/Main/AdvancedPanels/Wording/Body/NotesField/Notes`**

- `props.text`: expression

```js
coalesce({view.custom.def.notes}, '')
```


**`root/Body/Step3/Main/Advanced`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.advanced}, false), 'report-advanced report-advanced-open', 'report-advanced')
```


**`root/Body/Step3/Main/Advanced/Hint`**

- `props.text`: expression

```js
if(coalesce({view.custom.advanced}, false), 'Back To ' + coalesce({view.custom.model.scopeTitle}, 'Scope') + ' & Measures', 'Sections & Order, Top N, Filters, Title, Notes')
```


**`root/Body/Step3/Main/Advanced/Chevron`**

- `props.path`: expression

```js
if(coalesce({view.custom.advanced}, false), 'material/expand_less', 'material/expand_more')
```


**`root/Body/Step3/Summary/Body/Lines`**

- `props.instances`: property `view.custom.model.summary`, then script transform

Transform 1, script:

```python
return [{'line': l} for l in (value or [])]
```


**`root/Body/Step4`**

- `position.display`: expression

```js
coalesce({view.custom.ctx.use}, false) && !coalesce({view.custom.noSources}, false) && coalesce({view.custom.step}, 1) = 4
```


**`root/Body/Step4/Preview/Body/Titles`**

- `position.display`: expression

```js
!coalesce({view.custom.loading}, false)
```


**`root/Body/Step4/Preview/Body/Titles/Title`**

- `props.text`: expression

```js
coalesce({view.custom.preview.meta.title}, {view.custom.def.title}, '')
```


**`root/Body/Step4/Preview/Body/Titles/Meta`**

- `props.text`: expression

```js
coalesce({view.custom.preview.meta.subtitle}, '')
```


**`root/Body/Step4/Preview/Body/Error`**

- `position.display`: expression

```js
!coalesce({view.custom.loading}, false) && !coalesce({view.custom.preview.ok}, true)
```


- `props.text`: expression

```js
'Report Failed - ' + coalesce({view.custom.preview.message}, '')
```


**`root/Body/Step4/Preview/Body/Sections`**

- `position.display`: expression

```js
!coalesce({view.custom.loading}, false) && coalesce({view.custom.preview.ok}, true) && !coalesce({view.custom.preview.empty}, false)
```


- `props.instances`: property `view.custom.preview.instances`

**`root/Body/Step4/Preview/Body/Loading`**

- `position.display`: expression

```js
coalesce({view.custom.loading}, false)
```


**`root/Body/Step4/Preview/Body/NoData`**

- `position.display`: expression

```js
!coalesce({view.custom.loading}, false) && coalesce({view.custom.preview.ok}, true) && coalesce({view.custom.preview.empty}, false)
```


**`root/Body/Step4/Preview/Body/Failed`**

- `position.display`: expression

```js
!coalesce({view.custom.loading}, false) && !coalesce({view.custom.preview.ok}, true)
```


**`root/Body/Step4/Rail/Download/Body/Formats/F_PDF`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.format}, 'PDF') = 'PDF', 'report-choice report-choice-selected report-choice-btn', 'report-choice report-choice-btn')
```


**`root/Body/Step4/Rail/Download/Body/Formats/F_Excel`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.format}, 'PDF') = 'Excel', 'report-choice report-choice-selected report-choice-btn', 'report-choice report-choice-btn')
```


**`root/Body/Step4/Rail/Download/Body/Formats/F_CSV`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.format}, 'PDF') = 'CSV', 'report-choice report-choice-selected report-choice-btn', 'report-choice report-choice-btn')
```


**`root/Body/Step4/Rail/Download/Body/Download`**

- `meta.tooltip.enabled`: expression

```js
!(coalesce({view.custom.preview.ok}, true) && !coalesce({view.custom.loading}, false))
```


- `meta.tooltip.text`: expression

```js
if(coalesce({view.custom.loading}, false), 'Building The Preview', if(coalesce({view.custom.preview.ok}, true), 'No Data For This Range', 'The Report Could Not Be Built'))
```


- `props.enabled`: expression

```js
coalesce({view.custom.preview.ok}, true) && !coalesce({view.custom.loading}, false)
```


- `props.text`: expression

```js
'Download ' + coalesce({view.custom.format}, 'PDF')
```


**`root/Body/Step4/Rail/Save/Head/Title`**

- `props.text`: expression

```js
if(coalesce({view.custom.templateId}, 0) > 0, 'Template: ' + coalesce({view.custom.templateName}, ''), 'Save As Template')
```


**`root/Body/Step4/Rail/Save/Body/NameField/Name`**

- `props.text`: property `view.custom.templateName` (bidirectional)

**`root/Body/Step4/Rail/Save/Body/ShareRow/Shared`**

- `props.enabled`: expression

```js
coalesce({view.custom.ctx.share}, false)
```


- `props.selected`: property `view.custom.templateShared` (bidirectional)

**`root/Body/Step4/Rail/Save/Body/ShareRow/Save`**

- `props.enabled`: expression

```js
len(trim(coalesce({view.custom.templateName}, ''))) >= 3 && (!coalesce({view.custom.templateId}, 0) > 0 || coalesce({view.custom.templateCanEdit}, false))
```


**`root/Body/Step4/Rail/Save/Body/TplRow`**

- `position.display`: expression

```js
coalesce({view.custom.templateId}, 0) > 0
```


**`root/Body/Step4/Rail/Save/Body/TplRow/Delete`**

- `props.enabled`: expression

```js
coalesce({view.custom.templateCanEdit}, false)
```


**`root/Body/Denied`**

- `position.display`: expression

```js
!coalesce({view.custom.ctx.use}, false) || coalesce({view.custom.noSources}, false)
```


**`root/Body/Denied/Title`**

- `props.text`: expression

```js
if(coalesce({view.custom.ctx.use}, false), 'No Report Sources Available', "You Don't Have Access To Reports")
```


**`root/Body/Denied/Text`**

- `props.text`: expression

```js
if(coalesce({view.custom.ctx.use}, false), 'Your Role Has No Reports Source Permission. Ask An Administrator To Tick One On Admin > Roles & Permissions.', 'The Report Builder Needs The Reports / Use Permission (Maintenance And Above). Ask An Administrator To Tick It On Admin > Roles & Permissions.')
```


**`root/Footer/Status`**

- `props.text`: expression

```js
if(len(coalesce({view.custom.msg}, '')) > 0, {view.custom.msg}, if(coalesce({view.custom.step}, 1) = 4 && !isNull({view.custom.preview.meta.elapsedMs}), 'Ran In ' + numberFormat({view.custom.preview.meta.elapsedMs} / 1000.0, '0.0') + ' s', 'Step ' + toStr(coalesce({view.custom.step}, 1)) + ' Of 4'))
```


**`root/Footer/Cancel`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) = 1 || !coalesce({view.custom.ctx.use}, false)
```


**`root/Footer/Back`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) > 1 && coalesce({view.custom.ctx.use}, false)
```


**`root/Footer/Skip`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) = 2 && coalesce({view.custom.ctx.use}, false)
```


**`root/Footer/StartOver`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) = 4 && coalesce({view.custom.ctx.use}, false)
```


**`root/Footer/Next`**

- `position.display`: expression

```js
coalesce({view.custom.step}, 1) < 4 && coalesce({view.custom.ctx.use}, false) && !coalesce({view.custom.noSources}, false)
```


- `props.text`: expression

```js
case(coalesce({view.custom.step}, 1), 1, 'Next: Time Range', 2, 'Next: Details', 'Preview Report')
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 32 event actions, change scripts and handlers</summary>

- **`root`** `system.onStartup`, script action, scope `G`

```python
# Report builder start: access, the start definition (template / opening page context), Step 1
v = self.view.custom
st = shared.Reports.startState(self.session, self.view.params.sourceId, self.view.params.context,
    self.view.params.templateId)
v.ctx = st['ctx']
v.templateId = st['templateId']
v.templateName = st['templateName']
v.templateShared = st['templateShared']
v.templateCanEdit = st['templateCanEdit']
v.msg = st['msg']
v.noSources = bool(st.get('noSources'))
if st['def'] is not None:
    v['def'] = st['def']
    v.format = st['def'].get('format') or 'PDF'
v.step = st.get('step') or 1
```

- **`root/Header/Close`** `dom.onClick`, script action, scope `G`

```python
shared.Reports.close()
```

- **`root/Stepper/Steps/Step1`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = 1
```

- **`root/Stepper/Steps/Step2`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = 2
```

- **`root/Stepper/Steps/Step3`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = 3
```

- **`root/Stepper/Steps/Step4`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = 4
```

- **`root/Body/Step1/Saved/Body/Tabs/Tab_templates`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.railTab = 'templates'
```

- **`root/Body/Step1/Saved/Body/Tabs/Tab_recent`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.railTab = 'recent'
```

- **`root/Body/Step3/Main/Advanced`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.advanced = not self.view.custom.advanced
```

- **`root/Body/Step4/Preview/Body/NoData/Buttons/ChangeTime`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = 2
```

- **`root/Body/Step4/Preview/Body/Failed/Buttons/Retry`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.runKey += 1
```

- **`root/Body/Step4/Preview/Body/Failed/Buttons/ChangeTime`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = 2
```

- **`root/Body/Step4/Rail/Download/Body/Formats/F_PDF`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.format = 'PDF'
```

- **`root/Body/Step4/Rail/Download/Body/Formats/F_Excel`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.format = 'Excel'
```

- **`root/Body/Step4/Rail/Download/Body/Formats/F_CSV`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.format = 'CSV'
```

- **`root/Body/Step4/Rail/Download/Body/Download`** `component.onActionPerformed`, script action, scope `G`

```python
# Run the full report and download it (shared.Reports checks access again and logs it under Recent)
v = self.view.custom
d = shared.Reports.normalize(v['def'])
d['format'] = v.format or 'PDF'
v.msg = shared.Reports.download(self.session, d)
v.refresh += 1
```

- **`root/Body/Step4/Rail/Save/Body/ShareRow/Save`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
d = shared.Reports.normalize(v['def'])
d['format'] = v.format or 'PDF'
res = shared.Reports.saveTemplate(self.session, v.templateId, v.templateName, d,
    bool(v.templateShared), saveAs=False)
v.msg = res['message']
if res['ok']:
    v.templateId = res['id']
    v.templateCanEdit = True
    v.refresh += 1
```

- **`root/Body/Step4/Rail/Save/Body/TplRow/SaveAs`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
d = shared.Reports.normalize(v['def'])
d['format'] = v.format or 'PDF'
res = shared.Reports.saveTemplate(self.session, v.templateId, v.templateName, d,
    bool(v.templateShared), saveAs=True)
v.msg = res['message']
if res['ok']:
    v.templateId = res['id']
    v.templateCanEdit = True
    v.refresh += 1
```

- **`root/Body/Step4/Rail/Save/Body/TplRow/Delete`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
shared.Alerts.showAlert(state='warning', title='Delete Template', message='Delete The Template "%s"? This Cannot Be Undone.' % v.templateName, showCloseBtn=False, btnTextPrimary='Delete', btnTextSecondary='Cancel', btnActionPrimary='rptDeleteTemplate', btnActionSecondary='', payload={'id': v.templateId}, overlayDismiss=False)
```

- **`root/Footer/Cancel`** `component.onActionPerformed`, script action, scope `G`

```python
shared.Reports.close()
```

- **`root/Footer/Back`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = max(1, (self.view.custom.step or 1) - 1)
```

- **`root/Footer/Skip`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = 4
```

- **`root/Footer/StartOver`** `component.onActionPerformed`, script action, scope `G`

```python
v = self.view.custom
v['def'] = shared.Reports.defaultDefinition(self.session, v['def'].get('source'), {})
v.templateId = 0
v.templateName = ''
v.templateCanEdit = False
v.advanced = False
v.msg = ''
v.step = 1
```

- **`root/Footer/Next`** `component.onActionPerformed`, script action, scope `G`

```python
self.view.custom.msg = ''
self.view.custom.step = min(4, (self.view.custom.step or 1) + 1)
```

- **`root/Body/Step2/Main/Dates/From/Start`** change script on `props.value`

```python
if str(origin) != 'Browser' or currentValue is None or currentValue.value is None:
    return
system.perspective.sendMessage('rptEdit', {'kind': 'time', 'preset': 'custom', 'start': currentValue.value}, scope='page')
```

- **`root/Body/Step2/Main/Dates/To/End`** change script on `props.value`

```python
if str(origin) != 'Browser' or currentValue is None or currentValue.value is None:
    return
system.perspective.sendMessage('rptEdit', {'kind': 'time', 'preset': 'custom', 'end': currentValue.value}, scope='page')
```

- **`root/Body/Step3/Main/AdvancedPanels/Wording/Body/TitleField/Title`** change script on `props.text`

```python
if str(origin) != 'Browser':
    return
system.perspective.sendMessage('rptEdit', {'kind': 'set', 'key': 'title', 'value': currentValue.value}, scope='page')
```

- **`root/Body/Step3/Main/AdvancedPanels/Wording/Body/NotesField/Notes`** change script on `props.text`

```python
if str(origin) != 'Browser':
    return
system.perspective.sendMessage('rptEdit', {'kind': 'set', 'key': 'notes', 'value': currentValue.value}, scope='page')
```

- **`root`** message handler `rptEdit` (scope: page)

```python

v = self.view.custom
if not v.ctx.get('use'):
    return
k = payload.get('kind')
v['def'] = shared.Reports.applyEdit(self.session, v['def'], payload)
if k in ('source', 'preset'):
    v.templateId = 0
    v.templateName = ''
    v.templateCanEdit = False
    v.msg = ''
if k == 'preset':
    v.format = v['def'].get('format') or 'PDF'
    v.step = 4
```

- **`root`** message handler `rptLoadSaved` (scope: page)

```python
# Step 1 rail: load a saved template / recent report, then show its preview
v = self.view.custom
r = shared.Reports.loadSaved(self.session, payload.get('kind'), payload.get('id'))
if r is None:
    v.msg = 'That Report Is No Longer Available'
    return
v['def'] = r['definition']
v.format = r['definition'].get('format') or 'PDF'
v.templateId = r['templateId']
v.templateName = r['name']
v.templateShared = r['shared']
v.templateCanEdit = r['canEdit']
v.msg = r['message']
v.step = 4
```

- **`root`** message handler `rptDeleteTemplate` (scope: page)

```python
res = shared.Reports.deleteTemplate(self.session, payload.get('id'))
v = self.view.custom
v.msg = res['message']
if res['ok']:
    v.templateId = 0
    v.templateName = ''
    v.templateCanEdit = False
    v.refresh += 1
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md), [shared.Reports](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.applyEdit](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.builderModel](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.defaultDefinition](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.deleteTemplate](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.download](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.loadSaved](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.normalize](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.previewInstances](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.saveTemplate](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.savedList](../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.startState](../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Embeds** (7): [01\_Popups/Reports/\_Assets/CheckItem](./assets/checkitem.md) (flex repeater), [01\_Popups/Reports/\_Assets/ChoiceTile](./assets/choicetile.md) (flex repeater), [01\_Popups/Reports/\_Assets/PreviewSection](./assets/previewsection.md) (flex repeater), [01\_Popups/Reports/\_Assets/SavedRow](./assets/savedrow.md) (flex repeater), [01\_Popups/Reports/\_Assets/SectionItem](./assets/sectionitem.md) (flex repeater), [01\_Popups/Reports/\_Assets/SourceCard](./assets/sourcecard.md) (flex repeater), [01\_Popups/Reports/\_Assets/SummaryLine](./assets/summaryline.md) (flex repeater)

**Named in project scripts**: [shared.Reports](../../../../../scripting/reference/modules/shared-reports.md)

## Style Classes

<details>
<summary>34 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `form-banner` | 1 | style class |
| `form-banner-error` | 1 | style class |
| `form-btn` | 9 | style class |
| `form-btn-primary` | 3 | style class |
| `form-card` | 10 | style class |
| `form-check` | 1 | style class |
| `form-input` | 5 | style class |
| `form-label` | 5 | style class |
| `form-section-head` | 10 | style class |
| `form-section-title` | 10 | style class |
| `form-status` | 1 | style class |
| `form-th` | 6 | style class |
| `report-advanced` | 1 | style class |
| `report-bar-bottom` | 1 | style class |
| `report-bar-mid` | 1 | style class |
| `report-bar-top` | 1 | style class |
| `report-choice` | 3 | style class |
| `report-choice-btn` | 3 | style class |
| `report-choice-detail` | 1 | style class |
| `report-choice-label` | 1 | style class |
| `report-heading` | 9 | style class |
| `report-hint` | 12 | style class |
| `report-step-dot` | 4 | style class |
| `report-step-label` | 4 | style class |
| `report-step-line` | 3 | style class |
| `report-step-num` | 4 | style class |
| `report-subtitle` | 1 | style class |
| `report-surface` | 1 | style class |
| `report-tab` | 2 | style class |
| `report-title` | 1 | style class |
| `report-choice-selected` | bound | style class |
| `report-step-dot-on` | bound | style class |
| `report-step-label-current` | bound | style class |
| `report-step-label-done` | bound | style class |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
