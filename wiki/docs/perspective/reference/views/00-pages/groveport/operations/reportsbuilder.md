---
title: "ReportsBuilder"
sidebar_label: "ReportsBuilder"
description: "Perspective view 00_Pages/Groveport/Operations/ReportsBuilder (Page): 16 components, 6 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Operations/ReportsBuilder", "ReportsBuilder", "/operations/reports"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Operations/ReportsBuilder`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Operations/ReportsBuilder` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Operations/ReportsBuilder/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Operations &gt; ReportsBuilder |
| Routes | `/operations/reports` (Report Builder) |
| Root | `ia.container.flex`, height 1000, width 1600 |
| Size | 16 components, 6 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-24T14:19:27Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `model` | `{"denied": true, "quick": [], "sources": []}` | bound (expr-struct) |

## Component Tree

Component types: ia.container.flex x6, ia.display.label x6, ia.display.flex-repeater x2, ia.input.button x1, ia.display.icon x1.

<details>
<summary>Component tree (16 components)</summary>

```text
root  ia.container.flex
  Head  ia.container.flex
    TitleBox  ia.container.flex
      Title  ia.display.label
      Subtitle  ia.display.label
    Saved  ia.input.button  [1 event]
  Card  ia.container.flex
    Main  ia.container.flex  [1 binding]
      SourceCap  ia.display.label
      Sources  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/StartCard]
      QuickCap  ia.display.label
      Quick  ia.display.flex-repeater  [1 binding; view: 01_Popups/Reports/_Assets/StartTile]
  Denied  ia.container.flex  [1 binding]
    Icon  ia.display.icon
    Msg  ia.display.label  [1 binding]
    Text  ia.display.label
```

</details>

## Bindings

6 bindings: expr 3, property 2, expr-struct 1.

**`(view)`**

- `custom.model`: structured expression (expr-struct), then script transform

```js
ok: coalesce({session.custom.Permissions.Reports.Use}, false)
```

waitOnAll: `False`

Transform 1, script:

```python
if not value.ok:
    return {'sources': [], 'quick': [], 'denied': True}
return shared.Reports.startModel(self.session)
```


**`root/Card/Main`**

- `position.display`: expression

```js
!coalesce({view.custom.model.denied}, true)
```


**`root/Card/Main/Sources`**

- `props.instances`: property `view.custom.model.sources`

**`root/Card/Main/Quick`**

- `props.instances`: property `view.custom.model.quick`

**`root/Denied`**

- `position.display`: expression

```js
coalesce({view.custom.model.denied}, true)
```


**`root/Denied/Msg`**

- `props.text`: expression

```js
if(coalesce({session.custom.Permissions.Reports.Use}, false), 'No Report Sources Available', "You Don't Have Access To Reports")
```


## Event Scripts And Handlers

- **`root/Head/Saved`** `component.onActionPerformed`, script action, scope `G`

```python
system.perspective.navigate('/operations/reports/saved')
```

- **`root`** message handler `rptStart` (scope: page)

```python

if payload.get('kind') == 'preset':
    shared.Reports.open(None, {'preset': payload.get('id'), 'origin': 'Report Builder'}, self.session)
else:
    shared.Reports.open(payload.get('value'), {'origin': 'Report Builder'}, self.session)
```

Project script calls: [shared.Reports.open](../../../../../../scripting/reference/modules/shared-reports.md), [shared.Reports.startModel](../../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Embeds** (2): [01\_Popups/Reports/\_Assets/StartCard](../../../01-popups/reports/assets/startcard.md) (flex repeater), [01\_Popups/Reports/\_Assets/StartTile](../../../01-popups/reports/assets/starttile.md) (flex repeater)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `bg-page` | 1 | style class |
| `form-btn` | 1 | style class |
| `form-card` | 2 | style class |
| `form-th` | 2 | style class |
| `fs-13` | 1 | style class |
| `fs-20` | 1 | style class |
| `fw-700` | 1 | style class |
| `report-heading` | 1 | style class |
| `report-hint` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
