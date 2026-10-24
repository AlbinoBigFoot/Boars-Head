---
title: "Menu"
sidebar_label: "Menu"
description: "Perspective view 01_Popups/TrendContext/Menu (Popup / faceplate): 27 components, 11 bindings, 8 event scripts."
generated: true
keywords: ["01_Popups/TrendContext/Menu", "Menu"]
---

:::note

:::


**Popup / faceplate**: `01_Popups/TrendContext/Menu`.

| | |
|---|---|
| View path | `01_Popups/TrendContext/Menu` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/TrendContext/Menu/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 01\_Popups &gt; TrendContext &gt; Menu |
| Root | `ia.container.flex`, width 236, height 260 |
| Size | 27 components, 11 bindings, 8 event handlers, 0 change scripts, 0 message handlers |
| Last saved | 2026-10-23T12:00:00Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `tagPath` | `""` | input |
| `label` | `""` | input |
| `historized` | `false` | input |
| `inTrend` | `false` | input |
| `ticketLog` | `false` | input |
| `viewName` | `""` | input |

## Component Tree

Component types: ia.container.flex x11, ia.display.label x9, ia.display.icon x7.

<details>
<summary>Component tree (27 components)</summary>

```text
root  ia.container.flex  [2 events]
  Header  ia.container.flex
    Title  ia.display.label  [1 binding]
    Path  ia.display.label  [1 binding]
  Sep0  ia.container.flex  [1 binding]
  AddToTrend  ia.container.flex  [1 binding; 1 event]
    Icon  ia.display.icon
    Text  ia.display.label
  RemoveFromTrend  ia.container.flex  [1 binding; 1 event]
    Icon  ia.display.icon
    Text  ia.display.label
  NotHistorized  ia.container.flex  [1 binding]
    Icon  ia.display.icon
    Text  ia.display.label
  OpenTrend  ia.container.flex  [1 binding; 1 event]
    Icon  ia.display.icon
    Text  ia.display.label
  QuickHistory  ia.container.flex  [1 binding; 1 event]
    Icon  ia.display.icon
    Text  ia.display.label
  Sep1  ia.container.flex  [1 binding]
  CopyTagPath  ia.container.flex  [1 binding; 1 event]
    Icon  ia.display.icon
    Text  ia.display.label
  TicketLogger  ia.container.flex  [1 binding; 1 event]
    Icon  ia.display.icon
    Text  ia.display.label
```

</details>

## Bindings

11 bindings: expr 9, property 2.

**`root/Header/Title`**

- `props.text`: property `view.params.label`

**`root/Header/Path`**

- `props.text`: property `view.params.tagPath`

**`root/Sep0`**

- `position.display`: expression

```js
true
```


**`root/AddToTrend`**

- `position.display`: expression

```js
coalesce({view.params.historized}, false) && !coalesce({view.params.inTrend}, false)
```


**`root/RemoveFromTrend`**

- `position.display`: expression

```js
coalesce({view.params.historized}, false) && coalesce({view.params.inTrend}, false)
```


**`root/NotHistorized`**

- `position.display`: expression

```js
!coalesce({view.params.historized}, false)
```


**`root/OpenTrend`**

- `position.display`: expression

```js
coalesce({view.params.historized}, false)
```


**`root/QuickHistory`**

- `position.display`: expression

```js
coalesce({view.params.historized}, false)
```


**`root/Sep1`**

- `position.display`: expression

```js
true
```


**`root/CopyTagPath`**

- `position.display`: expression

```js
true
```


**`root/TicketLogger`**

- `position.display`: expression

```js
coalesce({view.params.ticketLog}, false)
```


## Event Scripts And Handlers

- **`root`** `dom.onKeyDown`, script action, scope `G`

```python
if str(getattr(event, 'key', '')) == 'Escape':
    shared.TrendContext.close_menu()
```

- **`root`** `system.onStartup`, script action, scope `G`

```python
try:
    self.getChild('CopyTagPath').focus()
except:
    pass
```

- **`root/AddToTrend`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.menu_action(self, 'add')
```

- **`root/RemoveFromTrend`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.menu_action(self, 'remove')
```

- **`root/OpenTrend`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.menu_action(self, 'open')
```

- **`root/QuickHistory`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.menu_action(self, 'quick')
```

- **`root/CopyTagPath`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.menu_action(self, 'copy')
```

- **`root/TicketLogger`** `dom.onClick`, script action, scope `G`

```python
shared.TrendContext.menu_action(self, 'ticket')
```

## Related Views

**Named in project scripts**: [shared.TrendContext](../../../../../scripting/reference/modules/shared-trendcontext.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 1 | style class |
| `Fonts/Value` | 7 | style class |
| `trend-ctx-head` | 1 | stylesheet |
| `trend-ctx-icon` | 7 | stylesheet |
| `trend-ctx-menu` | 1 | stylesheet |
| `trend-ctx-muted` | 2 | stylesheet |
| `trend-ctx-path` | 1 | stylesheet |
| `trend-ctx-row` | 7 | stylesheet |
| `trend-ctx-row-muted` | 1 | stylesheet |
| `trend-ctx-sep` | 2 | stylesheet |
| `trend-ctx-text` | 7 | stylesheet |
| `trend-ctx-title` | 1 | stylesheet |

See the [style class catalog](../../../style-classes.md) and the [stylesheet index](../../../stylesheet.md).
