---
title: "SummaryLine"
sidebar_label: "SummaryLine"
description: "Perspective view 01_Popups/Reports/_Assets/SummaryLine (Asset (embedded piece)): 3 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/SummaryLine", "SummaryLine"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/SummaryLine`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/SummaryLine` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/SummaryLine/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; SummaryLine |
| Root | `ia.container.flex`, height 54, width 320 |
| Size | 3 components, 2 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T19:51:42Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `line` | `{"key": "", "value": ""}` | input |

## Component Tree

Component types: ia.display.label x2, ia.container.flex x1.

```text
root  ia.container.flex
  Key  ia.display.label  [1 binding]
  Value  ia.display.label  [1 binding]
```

## Bindings

2 bindings: expr 2.

**`root/Key`**

- `props.text`: expression

```js
coalesce({view.params.line.key}, '')
```


**`root/Value`**

- `props.text`: expression

```js
coalesce({view.params.line.value}, '')
```


## Related Views

**Embedded in** (1): [01\_Popups/Reports/ReportBuilder](../reportbuilder.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `form-th` | 1 | style class |
| `report-sum-value` | 1 | style class |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
