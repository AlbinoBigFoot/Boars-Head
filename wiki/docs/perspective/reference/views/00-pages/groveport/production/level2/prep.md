---
title: "Prep"
sidebar_label: "Prep"
description: "Perspective view 00_Pages/Groveport/Production/Level2/Prep (Page): 17 components, 11 bindings, 9 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Production/Level2/Prep", "Prep", "/plants/groveport/production/level-2/prep"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Production/Level2/Prep`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Production/Level2/Prep` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Production/Level2/Prep/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Production &gt; Level2 &gt; Prep |
| Routes | `/plants/groveport/production/level-2/prep` (Groveport Production Prep Zone) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 17 components, 11 bindings, 9 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-01T14:45:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |

## Component Tree

Component types: ia.display.label x11, ia.container.flex x4, ia.container.coord x1, ia.display.view x1.

<details>
<summary>Component tree (17 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Draw  ia.container.coord  [1 binding]
    Title  ia.display.label
    BackL1  ia.display.label  [1 event]
    Zone_Prep  ia.container.flex
      ZoneLabel  ia.display.label
    VD  ia.container.flex  [2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    HOP  ia.container.flex  [2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    KpiRail  ia.display.view  [view: 00_Pages/Groveport/Production/Level2/Kpis]
```

</details>

## Bindings

11 bindings: expr 10, expr-struct 1.

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


**`root/Draw/VD/Sub`**

- `position.display`: expression

```js
'' != ''
```


**`root/Draw/VD/RunStatus`**

- `props.text`: expression

```js
if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 3, 'Fault', 'Idle')), 'Running')
```


- `props.style.color`: expression

```js
if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Fault', '#C62828', if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/VD/Rate`**

- `props.text`: expression

```js
numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value'), 90), '#,##0') + ' lb/hr'
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

- **`root/Draw/BackL1`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production-overview')
```

- **`root/Draw/VD`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/vat-dumper')
```

- **`root/Draw/VD`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value')
```

- **`root/Draw/VD/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')
```

- **`root/Draw/VD/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value')
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

**Embeds** (1): [00\_Pages/Groveport/Production/Level2/Kpis](./kpis.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

## Style Classes

<details>
<summary>16 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 8 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 2 | style class |
| `bg-page` | 1 | style class |
| `container-card` | 2 | stylesheet |
| `container-card-border` | 2 | stylesheet |
| `fs-11` | 2 | style class |
| `fs-12` | 2 | style class |
| `fs-14` | 2 | style class |
| `fs-22` | 2 | style class |
| `fs-9` | 2 | style class |
| `fw-700` | 8 | style class |
| `plant-feature-title` | 1 | style class |
| `prod-device-tile` | 2 | style class |
| `text-cta` | 1 | style class |
| `text-muted` | 3 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
