---
title: "SiteCard"
sidebar_label: "SiteCard"
description: "Perspective view 02_Components/02_Widgets/SiteCard (Reusable component): 25 components, 9 bindings, 1 event scripts."
generated: true
keywords: ["02_Components/02_Widgets/SiteCard", "SiteCard"]
---

:::note

:::


**Reusable component**: `02_Components/02_Widgets/SiteCard`.

| | |
|---|---|
| View path | `02_Components/02_Widgets/SiteCard` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/02_Widgets/SiteCard/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 02\_Widgets &gt; SiteCard |
| Root | `ia.container.flex`, height 196, width 300 |
| Size | 25 components, 9 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-20T19:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `siteName` | `"Plant"` | input |
| `region` | `""` | input |
| `page` | `""` | input |
| `tagRoot` | `""` | input |

## Component Tree

Component types: ia.display.label x14, ia.container.flex x11.

<details>
<summary>Component tree (25 components)</summary>

```text
root  ia.container.flex  [3 bindings; 1 event]
  TitleRow  ia.container.flex
    SiteName  ia.display.label  [1 binding]
    Region  ia.display.label  [1 binding]
  Pens  ia.container.flex
    PenKwh  ia.container.flex
      Lbl  ia.display.label
      ValueUnit  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
    PenTherm  ia.container.flex
      Lbl  ia.display.label
      ValueUnit  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
    PenProd  ia.container.flex
      Lbl  ia.display.label
      ValueUnit  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
    PenTemp  ia.container.flex
      Lbl  ia.display.label
      ValueUnit  ia.container.flex
        Val  ia.display.label  [1 binding]
        Unit  ia.display.label
```

</details>

## Bindings

9 bindings: expr 7, property 2.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

- `meta.domId`: expression

```js
if(coalesce({view.params.page}, '') = '', '', 'bhcard' + replace({view.params.page}, '/', '-'))
```


**`root/TitleRow/SiteName`**

- `props.text`: property `view.params.siteName`

**`root/TitleRow/Region`**

- `props.text`: property `view.params.region`

**`root/Pens/PenKwh/ValueUnit/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '') + '/EPMS/kWh')), null, tag(coalesce({view.params.tagRoot}, '') + '/EPMS/kWh')), null), 0), '#,##0')
```


**`root/Pens/PenTherm/ValueUnit/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '') + '/Utility/Therm')), null, tag(coalesce({view.params.tagRoot}, '') + '/Utility/Therm')), null), 0), '#,##0')
```


**`root/Pens/PenProd/ValueUnit/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '') + '/Production/ProdVol')), null, tag(coalesce({view.params.tagRoot}, '') + '/Production/ProdVol')), null), 0), '#,##0')
```


**`root/Pens/PenTemp/ValueUnit/Val`**

- `props.text`: expression

```js
numberFormat(coalesce(try(if(!isGood(tag(coalesce({view.params.tagRoot}, '') + '/Utility/AmbientAvgF')), null, tag(coalesce({view.params.tagRoot}, '') + '/Utility/AmbientAvgF')), null), 0), '#,##0.#')
```


## Event Scripts And Handlers

- **`root`** `dom.onClick`, script action, scope `G`

```python
page = str(self.view.params.page or '').strip()
if not page:
    return
Navigation.Nav.navigate({'action': 'page', 'page': page})
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (1): [00\_Pages/Boars Head/LandingPage/Globe](../../00-pages/boars-head/landingpage/globe.md)

## Style Classes

<details>
<summary>15 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 9 | style class |
| `Fonts/LiveDataEntry` | 4 | style class |
| `Fonts/Title` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-14` | 5 | style class |
| `fs-15` | 4 | style class |
| `fs-18` | 5 | style class |
| `fw-600` | 4 | style class |
| `fw-700` | 1 | style class |
| `site-card` | 1 | stylesheet |
| `site-card-pen` | 4 | stylesheet |
| `site-card-pen-label` | 4 | stylesheet |
| `site-card-pen-unit` | 4 | stylesheet |
| `site-card-pen-value` | 4 | stylesheet |

</details>

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/EPMS/kWh`, `/Production/ProdVol`, `/Utility/AmbientAvgF`, `/Utility/Therm`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
