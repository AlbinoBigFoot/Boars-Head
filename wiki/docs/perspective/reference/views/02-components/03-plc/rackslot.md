---
title: "RackSlot"
sidebar_label: "RackSlot"
description: "Perspective view 02_Components/03_PLC/RackSlot (Reusable component): 2 components, 6 bindings, 0 event scripts."
generated: true
keywords: ["02_Components/03_PLC/RackSlot", "RackSlot"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/RackSlot`.

| | |
|---|---|
| View path | `02_Components/03_PLC/RackSlot` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/RackSlot/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; RackSlot |
| Root | `ia.container.flex`, width 54, height 280 |
| Size | 2 components, 6 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `kind` | `""` | input |
| `catalog` | `""` | input |
| `slot` | `0` | input |
| `member` | `""` | input |
| `selected` | `false` | input |
| `name` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex
  Item  ia.display.view  [6 bindings; view: (bound)]
```

## Bindings

6 bindings: property 5, expr 1.

**`root/Item`**

- `props.path`: expression

```js
case(coalesce({view.params.kind}, ''), 'controller', '02_Components/03_PLC/Controller_CompactLogix_5370', 'endcap', '02_Components/03_PLC/EndCap_1769_ECR', 'power', '02_Components/03_PLC/PowerSupply_1769', 'card', if(coalesce({view.params.catalog}, '') = '', '', '02_Components/03_PLC/Module_' + replace({view.params.catalog}, '-', '_')), '')
```


- `props.params.tagPath`: property `view.params.tagPath`. Common pattern, see [pattern-5](../../../common-patterns.md#pattern-5).

- `props.params.slot`: property `view.params.slot`

- `props.params.member`: property `view.params.member`

- `props.params.selected`: property `view.params.selected`

- `props.params.name`: property `view.params.name`

## Related Views

**Bound embeds** (view path set by a binding): `root/Item`

**Opens or names** (popups, scripts, expressions): [02\_Components/03\_PLC/Controller\_CompactLogix\_5370](./controller-compactlogix-5370.md), [02\_Components/03\_PLC/EndCap\_1769\_ECR](./endcap-1769-ecr.md), [02\_Components/03\_PLC/PowerSupply\_1769](./powersupply-1769.md)

**Embedded in** (1): [00\_Pages/Groveport/Machine Room/Utility/PlcRack/Overview](../../00-pages/groveport/machine-room/utility/plcrack/overview.md)
