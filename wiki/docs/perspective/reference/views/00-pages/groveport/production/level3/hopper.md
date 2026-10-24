---
title: "Hopper"
sidebar_label: "Hopper"
description: "Perspective view 00_Pages/Groveport/Production/Level3/Hopper (Page): 17 components, 7 bindings, 8 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Production/Level3/Hopper", "Hopper", "/plants/groveport/production/hopper"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Production/Level3/Hopper`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Production/Level3/Hopper` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Production/Level3/Hopper/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Production &gt; Level3 &gt; Hopper |
| Routes | `/plants/groveport/production/hopper` (Groveport Production Hopper) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 17 components, 7 bindings, 8 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-01T14:45:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |

## Component Tree

Component types: ia.display.label x13, ia.container.flex x2, ia.container.coord x1, ia.display.view x1.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Draw  ia.container.coord  [1 binding]
    Title  ia.display.label
    CrumbL1  ia.display.label  [1 event]
    CrumbSep1  ia.display.label
    CrumbL2  ia.display.label  [1 event]
    CrumbSep2  ia.display.label
    CrumbL3  ia.display.label
    Upstream  ia.display.label  [1 event]
    Downstream  ia.display.label  [1 event]
    HOP  ia.container.flex  [2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    MimicCaption  ia.display.label
    KpiRail  ia.display.view  [view: 00_Pages/Groveport/Production/Level3/Kpis]
```

</details>

## Bindings

7 bindings: expr 6, expr-struct 1.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/Draw`**

- `props.style.transform`: structured expression (expr-struct), then script transform

```js
scale: {view.params.Scale}
defaultViewHeight: {view.props.defaultSize.height}
defaultViewWidth: {view.props.defaultSize.width}
primaryViewHeight: {page.props.dimensions.primaryView.height}
primaryViewWidth: {page.props.dimensions.primaryView.width}
```

waitOnAll: `True`

Transform 1, script:

```python
return shared.Scale.cssTransform(value)
```


**`root/Draw/HOP/Sub`**

- `position.display`: expression

```js
'' != ''
```


**`root/Draw/HOP/RunStatus`**

- `props.text`: expression

```js
if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 3, 'Fault', 'Idle')), 'Running')
```


- `props.style.color`: expression

```js
if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Fault', '#C62828', if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/HOP/Rate`**

- `props.text`: expression

```js
numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value'), 97), '#,##0') + ' lb/hr'
```


## Event Scripts And Handlers

- **`root/Draw/CrumbL1`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production-overview')
```

- **`root/Draw/CrumbL2`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/level-2/prep')
```

- **`root/Draw/Upstream`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/vat-dumper')
```

- **`root/Draw/Downstream`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/handtman')
```

- **`root/Draw/HOP`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/hopper')
```

- **`root/Draw/HOP`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value')
```

- **`root/Draw/HOP/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')
```

- **`root/Draw/HOP/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Scale.cssTransform](../../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Embeds** (1): [00\_Pages/Groveport/Production/Level3/Kpis](./kpis.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

## Style Classes

<details>
<summary>17 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 11 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `bg-page` | 1 | style class |
| `container-card` | 1 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 4 | style class |
| `fs-12` | 2 | style class |
| `fs-14` | 1 | style class |
| `fs-22` | 1 | style class |
| `fs-9` | 1 | style class |
| `fw-600` | 2 | style class |
| `fw-700` | 4 | style class |
| `plant-feature-title` | 1 | style class |
| `prod-device-tile` | 1 | style class |
| `text-cta` | 4 | style class |
| `text-muted` | 3 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
