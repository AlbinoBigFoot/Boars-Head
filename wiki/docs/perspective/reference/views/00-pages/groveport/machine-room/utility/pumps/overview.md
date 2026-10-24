---
title: "Overview"
sidebar_label: "Overview"
description: "Perspective view 00_Pages/Groveport/Machine Room/Utility/Pumps/Overview (Page): 9 components, 9 bindings, 2 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Machine Room/Utility/Pumps/Overview", "Overview", "/pumps"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Machine Room/Utility/Pumps/Overview`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Machine Room/Utility/Pumps/Overview` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/Pumps/Overview/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Machine Room &gt; Utility &gt; Pumps &gt; Overview |
| Routes | `/pumps` (Pumps) |
| Root | `ia.container.flex`, height 900, width 1280 |
| Size | 9 components, 9 bindings, 2 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-08-01T20:45:00Z by admin |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `"[default]Boars_Head/GrovePort/Machine Room/Pumps"` | input |
| `typeId` | `"Devices/Pump"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `overviewMode` | `"details"` | |

## Component Tree

Component types: ia.container.flex x4, ia.display.label x4, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  Title  ia.display.label
  Subtitle  ia.display.label
  ModeToggle  ia.container.flex
    DetailsBtn  ia.container.flex  [2 bindings; 1 event]
      DetailsLabel  ia.display.label
    DesignBtn  ia.container.flex  [2 bindings; 1 event]
      DesignLabel  ia.display.label
  Content  ia.display.view  [3 bindings; view: (bound)]
```

## Bindings

9 bindings: expr 5, expr-struct 2, property 2.

**`root`**

- `meta.contextMenu.items`: structured expression (expr-struct), then script transform. Common pattern, see [pattern-4](../../../../../../common-patterns.md#pattern-4).

- `meta.contextMenu.enabled`: structured expression (expr-struct), then expression transform. Common pattern, see [pattern-1](../../../../../../common-patterns.md#pattern-1).

**`root/ModeToggle/DetailsBtn`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.overviewMode},'details')='details','theme-toggle-option theme-toggle-option-selected','theme-toggle-option bg-component')
```


- `props.style.cursor`: expression

```js
if(coalesce({view.custom.overviewMode},'details')='details','auto','pointer')
```


**`root/ModeToggle/DesignBtn`**

- `props.style.classes`: expression

```js
if(coalesce({view.custom.overviewMode},'details')='design','theme-toggle-option theme-toggle-option-selected','theme-toggle-option bg-component')
```


- `props.style.cursor`: expression

```js
if(coalesce({view.custom.overviewMode},'details')='design','auto','pointer')
```


**`root/Content`**

- `props.path`: expression

```js
if(coalesce({view.custom.overviewMode},'details')='details','00_Pages/Boars Head/Pumps/Details',if(coalesce({view.custom.overviewMode},'details')='design','00_Pages/Boars Head/Pumps/Design','00_Pages/Boars Head/NoViewPath'))
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../../../../common-patterns.md#pattern-5).

- `props.params.typeId`: property `view.params.typeId`. Common pattern, see [pattern-7](../../../../../../common-patterns.md#pattern-7).

## Event Scripts And Handlers

- **`root/ModeToggle/DetailsBtn`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.overviewMode = 'details'
```

- **`root/ModeToggle/DesignBtn`** `dom.onClick`, script action, scope `G`

```python
self.view.custom.overviewMode = 'design'
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Bound embeds** (view path set by a binding): `root/Content`

**Opens or names** (popups, scripts, expressions): [00\_Pages/Boars Head/NoViewPath](../../../../boars-head/noviewpath.md), [00\_Pages/Boars Head/Pumps/Design](../../../../boars-head/pumps/design.md), [00\_Pages/Boars Head/Pumps/Details](../../../../boars-head/pumps/details.md)

**Opened or named by** (1): [00\_Pages/00\_Docked/Navigation](../../../../00-docked/navigation.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Title` | 1 | style class |
| `bg-component` | 2 | stylesheet |
| `bg-page` | 1 | style class |
| `fs-20` | 1 | style class |
| `fw-700` | 1 | style class |
| `theme-toggle` | 1 | style class |
| `theme-toggle-option` | 2 | style class |
| `themed-scroll` | 1 | stylesheet |
| `theme-toggle-option-selected` | bound | style class |

See the [style class catalog](../../../../../../style-classes.md) and the [stylesheet index](../../../../../../stylesheet.md).
