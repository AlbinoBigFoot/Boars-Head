---
title: "CgHit"
sidebar_label: "CgHit"
description: "Perspective view 03_Elements/03_Table/CgHit (Element (small reusable part)): 2 components, 1 bindings, 2 event scripts."
generated: true
keywords: ["03_Elements/03_Table/CgHit", "CgHit"]
---

:::note

:::


**Element (small reusable part)**: `03_Elements/03_Table/CgHit`.

| | |
|---|---|
| View path | `03_Elements/03_Table/CgHit` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/03_Table/CgHit/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 03\_Elements &gt; 03\_Table &gt; CgHit |
| Root | `ia.container.flex`, height 28, width 70 |
| Size | 2 components, 1 bindings, 2 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-08-21T13:50:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `row` | `""` | input |
| `rowData` | `{}` | input |
| `value` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1.

```text
root  ia.container.flex  [2 events]
  Cg  ia.display.label  [1 binding]
```

## Bindings

1 bindings: property 1.

**`root/Cg`**

- `props.text`: property `view.params.value`

## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
cg = ''
try:
    cg = str(self.view.params.value or '')
except:
    cg = ''
if not cg:
    try:
        cg = str((self.view.params.rowData or {}).get('cg') or '')
    except:
        pass
if cg:
    system.perspective.sendMessage(
        'UtilityOverviewHighlight',
        {'cg': cg, 'status': '', 'action': 'select'},
        scope='page'
    )
```

- **`root`** `dom.onDoubleClick`, script action, scope `G`

```python
row = {}
try:
    row = self.view.params.rowData or {}
except:
    row = {}
page = ''
try:
    page = str(row.get('navPage') or '').strip()
except:
    page = ''
if not page:
    cg = str(self.view.params.value or row.get('cg') or '')
    slug = cg.lower().replace('cg-', '')
    if slug:
        page = '/cg-' + slug
if page:
    Navigation.Nav.navigate({'action': 'page', 'page': page})
```

## Related Views

**Opened or named by** (1): [00\_Pages/Groveport/Utility/OverviewKpis](../../00-pages/groveport/utility/overviewkpis.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Value` | 1 | style class |
| `fs-12` | 1 | style class |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
