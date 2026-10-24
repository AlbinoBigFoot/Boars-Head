---
title: "Toast"
sidebar_label: "Toast"
description: "Perspective view 01_Popups/TrendContext/Toast (Popup / faceplate): 4 components, 3 bindings, 2 event scripts."
generated: true
keywords: ["01_Popups/TrendContext/Toast", "Toast"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/TrendContext/Toast`.

| | |
|---|---|
| View path | `01_Popups/TrendContext/Toast` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/TrendContext/Toast/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; TrendContext &gt; Toast |
| Root | `ia.container.flex`, width 420, height 44 |
| Size | 4 components, 3 bindings, 1 event handlers, 1 change scripts, 0 message handlers |
| Last saved | 2026-10-23T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `text` | `""` | input |
| `kind` | `"ok"` | input |
| `openedAt` | `null` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `age` | `0` | bound (expr), change script |

## Component Tree

Component types: ia.container.flex x2, ia.display.label x2.

```text
root  ia.container.flex
  Dot  ia.container.flex  [1 binding]
  Text  ia.display.label  [1 binding]
  Open  ia.display.label  [1 event]
```

## Bindings

3 bindings: expr 2, property 1.

**`(view)`**

- `custom.age`: expression

```js
if(isNull({view.params.openedAt}), 0, dateDiff({view.params.openedAt}, now(500), 'second'))
```


**`root/Dot`**

- `props.style.classes`: expression

```js
'trend-ctx-toast-dot trend-ctx-toast-' + coalesce({view.params.kind}, 'ok')
```


**`root/Text`**

- `props.text`: property `view.params.text`

## Event Scripts And Handlers

- **`root/Open`** `dom.onClick`, script action, scope `G`

```python
system.perspective.closePopup('TrendToast')
shared.TrendContext.open_trend()
```

- **`(view)`** change script on `custom.age`

```python
if currentValue is not None and currentValue.value is not None and currentValue.value >= 3:
    system.perspective.closePopup('TrendToast')
```

## Related Views

**Named in project scripts**: [shared.TrendContext](../../../../../scripting/reference/modules/shared-trendcontext.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 1 | style class |
| `trend-ctx-link` | 1 | stylesheet |
| `trend-ctx-toast` | 1 | stylesheet |
| `trend-ctx-toast-dot` | 1 | stylesheet |
| `trend-ctx-toast-text` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
