---
title: "VesselGeneric"
sidebar_label: "VesselGeneric"
description: "Perspective view 02_Components/01_Devices/VesselGeneric (Reusable component): 3 components, 12 bindings, 0 event scripts."
generated: true
keywords: ["02_Components/01_Devices/VesselGeneric", "VesselGeneric"]
---

:::note

:::


**Reusable component**: `02_Components/01_Devices/VesselGeneric`.

| | |
|---|---|
| View path | `02_Components/01_Devices/VesselGeneric` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/VesselGeneric/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 01\_Devices &gt; VesselGeneric |
| Root | `ia.container.coord`, width 160, height 80 |
| Size | 3 components, 12 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-01T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `label` | `""` | input |
| `orientation` | `"horizontal"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `label` | `""` | bound (expr) |
| `vertical` | `false` | bound (expr) |

## Component Tree

Component types: ia.shapes.svg x2, ia.container.coord x1.

```text
root  ia.container.coord  [2 bindings]
  VesselHorizontal  ia.shapes.svg  [4 bindings]
  VesselVertical  ia.shapes.svg  [4 bindings]
```

## Bindings

12 bindings: expr 10, property 2.

**`(view)`**

- `custom.label`: expression

```js
if(coalesce({view.params.label}, '') != '', {view.params.label}, if(coalesce({view.params.tagPath}, '') = '', '', subString({view.params.tagPath}, lastIndexOf({view.params.tagPath}, '/') + 1)))
```


- `custom.vertical`: expression

```js
lower(trim(coalesce({view.params.orientation}, ''))) = 'vertical'
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../common-patterns.md#pattern-2).

**`root/VesselHorizontal`**

- `meta.visible`: expression

```js
!{view.custom.vertical}
```


- `props.elements[3].text`: property `view.custom.label`

- `props.elements[3].fontSize`: expression

```js
round(min(8, 62 / (0.66 * max(len(coalesce({view.custom.label}, '')), 1))), 2)
```


- `props.elements[3].y`: expression

```js
round(18 + 0.35 * round(min(8, 62 / (0.66 * max(len(coalesce({view.custom.label}, '')), 1))), 2), 2)
```


**`root/VesselVertical`**

- `meta.visible`: expression

```js
{view.custom.vertical}
```


- `props.elements[3].text`: property `view.custom.label`

- `props.elements[3].fontSize`: expression

```js
round(min(8, 22 / (0.66 * max(len(coalesce({view.custom.label}, '')), 1))), 2)
```


- `props.elements[3].y`: expression

```js
round(40 + 0.35 * round(min(8, 22 / (0.66 * max(len(coalesce({view.custom.label}, '')), 1))), 2), 2)
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (2): [00\_Pages/Groveport/Condensers/Utility/Overview](../../00-pages/groveport/condensers/utility/overview.md), [98\_Configuration/ComponentPreview/VesselGeneric](../../98-configuration/componentpreview/vesselgeneric.md)
