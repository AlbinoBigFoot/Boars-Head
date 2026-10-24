---
title: "PreviewChart"
sidebar_label: "PreviewChart"
description: "Perspective view 01_Popups/Reports/_Assets/PreviewChart (Asset (embedded piece)): 3 components, 2 bindings, 0 event scripts."
generated: true
keywords: ["01_Popups/Reports/_Assets/PreviewChart", "PreviewChart"]
---

:::note

:::


**Asset (embedded piece)**: `01_Popups/Reports/_Assets/PreviewChart`.

| | |
|---|---|
| View path | `01_Popups/Reports/_Assets/PreviewChart` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/Reports/_Assets/PreviewChart/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; Reports &gt; \_Assets &gt; PreviewChart |
| Root | `ia.container.flex`, height 236, width 800 |
| Size | 3 components, 2 bindings, 0 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T19:45:31Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `chart` | `{"series": [], "title": ""}` | input |

## Component Tree

Component types: ia.container.flex x1, ia.display.label x1, kyvislabs.display.apexchart x1.

```text
root  ia.container.flex
  Title  ia.display.label  [1 binding]
  Chart  kyvislabs.display.apexchart  [1 binding]
```

## Bindings

2 bindings: expr 1, property 1.

**`root/Title`**

- `props.text`: expression

```js
coalesce({view.params.chart.title}, '')
```


**`root/Chart`**

- `props.series`: property `view.params.chart.series`, then script transform

Transform 1, script:

```python
return list(value or [])
```


## Related Views

**Embedded in** (1): [01\_Popups/Reports/\_Assets/PreviewSection](./previewsection.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `report-row-name` | 1 | style class |
| `utility-kpi-chart` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
