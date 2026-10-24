---
title: "PlcCardLed"
sidebar_label: "PlcCardLed"
description: "Perspective view 02_Components/03_PLC/PlcCardLed (Reusable component): 2 components, 3 bindings, 0 event scripts."
generated: true
keywords: ["02_Components/03_PLC/PlcCardLed", "PlcCardLed"]
---

:::note

:::


**Reusable component**: `02_Components/03_PLC/PlcCardLed`.

| | |
|---|---|
| View path | `02_Components/03_PLC/PlcCardLed` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/PlcCardLed/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 02\_Components &gt; 03\_PLC &gt; PlcCardLed |
| Root | `ia.container.flex`, width 12, height 10 |
| Size | 2 components, 3 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T06:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `label` | `""` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1.

```text
root  ia.container.flex
  Led  ia.display.label  [3 bindings]
```

## Bindings

3 bindings: expr 2, property 1.

**`root/Led`**

- `props.style.backgroundColor`: expression

```js
if(!(coalesce(try(isGood(tag(coalesce({view.params.tagPath}, '') + '/Faulted')), false), false) && coalesce(try(toBoolean(tag(coalesce({view.params.tagPath}, '') + '/CommOk')), false), false)), 'var(--neutral-60)', if(coalesce(try(toBoolean(tag(coalesce({view.params.tagPath}, '') + '/Faulted')), false), false), 'var(--sts-fault)', 'var(--sts-run)'))
```


- `meta.tooltip.text`: property `view.params.label`

- `meta.tooltip.enabled`: expression

```js
true
```


## Related Views

**Embedded in** (1): [02\_Components/03\_PLC/PlcCard](./plccard.md)

## Tags And Data

Member paths appended to a base path in expressions (relative):

`/CommOk`, `/Faulted`

Tag folders and UDTs are documented under [Tags](../../../../../tags/index.md).
