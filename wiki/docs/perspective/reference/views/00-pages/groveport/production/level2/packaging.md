---
title: "Packaging"
sidebar_label: "Packaging"
description: "Perspective view 00_Pages/Groveport/Production/Level2/Packaging (Page): 22 components, 15 bindings, 13 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Production/Level2/Packaging", "Packaging", "/plants/groveport/production/level-2/packaging"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Production/Level2/Packaging`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Production/Level2/Packaging` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Production/Level2/Packaging/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Production &gt; Level2 &gt; Packaging |
| Routes | `/plants/groveport/production/level-2/packaging` (Groveport Production Packaging Zone) |
| Root | `ia.container.flex`, height 1080, width 1920 |
| Size | 22 components, 15 bindings, 13 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-09-01T14:45:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `Scale` | `true` | input |

## Component Tree

Component types: ia.display.label x15, ia.container.flex x5, ia.container.coord x1, ia.display.view x1.

<details>
<summary>Component tree (22 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  Draw  ia.container.coord  [1 binding]
    Title  ia.display.label
    BackL1  ia.display.label  [1 event]
    Zone_Packaging  ia.container.flex
      ZoneLabel  ia.display.label
    RSM  ia.container.flex  [2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    ST  ia.container.flex  [2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    LS  ia.container.flex  [2 events]
      Title  ia.display.label
      Sub  ia.display.label  [1 binding]
      RunStatus  ia.display.label  [2 bindings; 1 event]
      Rate  ia.display.label  [1 binding; 1 event]
    KpiRail  ia.display.view  [view: 00_Pages/Groveport/Production/Level2/Kpis]
```

</details>

## Bindings

15 bindings: expr 14, expr-struct 1.

<details>
<summary>All 15 bindings, grouped by component</summary>

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


**`root/Draw/RSM/Sub`**

- `position.display`: expression

```js
'Vacuum Sealed' != ''
```


**`root/Draw/RSM/RunStatus`**

- `props.text`: expression

```js
if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 3, 'Fault', 'Idle')), 'Running')
```


- `props.style.color`: expression

```js
if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Fault', '#C62828', if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/RSM/Rate`**

- `props.text`: expression

```js
numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value'), 107), '#,##0') + ' lb/hr'
```


**`root/Draw/ST/Sub`**

- `position.display`: expression

```js
'' != ''
```


**`root/Draw/ST/RunStatus`**

- `props.text`: expression

```js
if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 3, 'Fault', 'Idle')), 'Running')
```


- `props.style.color`: expression

```js
if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Fault', '#C62828', if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/ST/Rate`**

- `props.text`: expression

```js
numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value'), 92), '#,##0') + ' lb/hr'
```


**`root/Draw/LS/Sub`**

- `position.display`: expression

```js
'Placed On Trees' != ''
```


**`root/Draw/LS/RunStatus`**

- `props.text`: expression

```js
if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 3, 'Fault', 'Idle')), 'Running')
```


- `props.style.color`: expression

```js
if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Fault', '#C62828', if((if(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')), if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 1, 'Running', if(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value') = 3, 'Fault', 'Idle')), 'Running')) = 'Idle', '#9E9E9E', '#2E7D32'))
```


**`root/Draw/LS/Rate`**

- `props.text`: expression

```js
numberFormat(coalesce(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value'), 99), '#,##0') + ' lb/hr'
```

</details>

## Event Scripts And Handlers

<details>
<summary>All 14 event actions, change scripts and handlers</summary>

- **`root/Draw/BackL1`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production-overview')
```

- **`root/Draw/RSM`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/roll-stock')
```

- **`root/Draw/RSM`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value')
```

- **`root/Draw/RSM/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')
```

- **`root/Draw/RSM/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value')
```

- **`root/Draw/ST`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/shrink-tunnel')
```

- **`root/Draw/ST`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value')
```

- **`root/Draw/ST/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')
```

- **`root/Draw/ST/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value')
```

- **`root/Draw/LS`** `dom.onClick`, script action, scope `G`

```python
system.perspective.navigate(page='/plants/groveport/production/lazy-susan')
```

- **`root/Draw/LS`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value')
```

- **`root/Draw/LS/RunStatus`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')
```

- **`root/Draw/LS/Rate`** `dom.onContextMenu`, script action, scope `G`

```python
shared.TrendContext.menu(self, event, '[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value')
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

</details>

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.Scale.cssTransform](../../../../../../../scripting/reference/modules/shared-scale.md).

## Related Views

**Embeds** (1): [00\_Pages/Groveport/Production/Level2/Kpis](./kpis.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../../00-docked/tempnav.md)

## Style Classes

<details>
<summary>16 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 11 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 3 | style class |
| `bg-page` | 1 | style class |
| `container-card` | 3 | stylesheet |
| `container-card-border` | 3 | stylesheet |
| `fs-11` | 2 | style class |
| `fs-12` | 3 | style class |
| `fs-14` | 3 | style class |
| `fs-22` | 3 | style class |
| `fs-9` | 3 | style class |
| `fw-700` | 11 | style class |
| `plant-feature-title` | 1 | style class |
| `prod-device-tile` | 3 | style class |
| `text-cta` | 1 | style class |
| `text-muted` | 4 | style class |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

- `[default]Boars_Head/GrovePort/Production/FCM/LS/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/Rate/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
