---
title: "PlcWriteLock"
sidebar_label: "PlcWriteLock"
description: "Perspective view 00_Pages/00_Docked/_Assets/PlcWriteLock (Asset (embedded piece)): 4 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/PlcWriteLock", "PlcWriteLock"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/PlcWriteLock`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/PlcWriteLock` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/PlcWriteLock/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; PlcWriteLock |
| Root | `ia.container.flex`, height 36, width 200 |
| Size | 4 components, 2 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-22T17:47:03Z by the Designer |

## Component Tree

Component types: ia.container.flex x2, ia.display.icon x1, ia.display.label x1.

```text
wrap  ia.container.flex
  root  ia.container.flex  [2 bindings]
    Icon  ia.display.icon
    Text  ia.display.label
```

## Bindings

2 bindings: expr 2.

**`wrap/root`**

- `meta.tooltip.text`: expression

```js
'PLC writes are UNLOCKED: [default]_Config/PlcWriteLock/Locked = false. Set it back to true in the Designer (Tag Browser) to relock.'
```


- `meta.tooltip.enabled`: expression

```js
true
```


## Related Views

**Embedded in** (1): [00\_Pages/00\_Docked/Header](../header.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `fw-700` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).

## Tags And Data

- `[default]_Config/PlcWriteLock/Locked = false. Set it back to true in the Designer (Tag Browser) to relock`

Tag folders and UDTs are documented under [Tags](../../../../../../tags/index.md).
