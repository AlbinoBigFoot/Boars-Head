---
title: "CardDetail"
sidebar_label: "CardDetail"
description: "Perspective view 01_Popups/00_Faceplates/PlcRack/CardDetail (Popup / faceplate): 2 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/00_Faceplates/PlcRack/CardDetail", "CardDetail"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/00_Faceplates/PlcRack/CardDetail`.

| | |
|---|---|
| View path | `01_Popups/00_Faceplates/PlcRack/CardDetail` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/PlcRack/CardDetail/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; 00\_Faceplates &gt; PlcRack &gt; CardDetail |
| Root | `ia.container.flex`, width 900, height 284 |
| Size | 2 components, 2 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `sitePath` | `"[default]Boars_Head/GrovePort/Machine Room/PLC/RCP1"` | input |
| `member` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex
  Detail  ia.display.view  [2 bindings; view: 02_Components/03_PLC/ModuleDetail]
```

## Bindings

2 bindings: property 2.

**`root/Detail`**

- `props.params.sitePath`: property `view.params.sitePath`

- `props.params.member`: property `view.params.member`

## Related Views

**Embeds** (1): [02\_Components/03\_PLC/ModuleDetail](../../../02-components/03-plc/moduledetail.md)

**Named in project scripts**: [shared.PlcRack](../../../../../../scripting/reference/modules/shared-plcrack.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
