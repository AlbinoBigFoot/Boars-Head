---
title: "IntegratorLogo"
sidebar_label: "IntegratorLogo"
description: "Perspective view 00_Pages/00_Docked/_Assets/IntegratorLogo (Asset (embedded piece)): 3 components, 5 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/00_Docked/_Assets/IntegratorLogo", "IntegratorLogo"]
---

:::note

:::


**Asset (embedded piece)**: `00_Pages/00_Docked/_Assets/IntegratorLogo`.

| | |
|---|---|
| View path | `00_Pages/00_Docked/_Assets/IntegratorLogo` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/IntegratorLogo/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; 00\_Docked &gt; \_Assets &gt; IntegratorLogo |
| Root | `ia.container.flex`, width 117, height 28 |
| Size | 3 components, 5 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-22T16:26:11Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `collapsible` | `false` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `logo` | `{"dark": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOkAAAA4CAY...` | |

## Component Tree

Component types: ia.display.image x2, ia.container.flex x1.

```text
root  ia.container.flex  [2 bindings]
  Lockup  ia.display.image  [1 binding]
  Mark  ia.display.image  [2 bindings]
```

## Bindings

5 bindings: expr 5.

**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/Lockup`**

- `props.source`: expression

```js
if(left(lower(coalesce({session.props.theme}, '')), 4) = 'dark', {view.custom.logo.dark}, {view.custom.logo.light})
```


**`root/Mark`**

- `props.source`: expression

```js
if(left(lower(coalesce({session.props.theme}, '')), 4) = 'dark', {view.custom.logo.markDark}, {view.custom.logo.markLight})
```


- `position.display`: expression

```js
coalesce({view.params.collapsible}, false)
```


## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Embedded in** (2): [00\_Pages/00\_Docked/Header](../header.md), [00\_Pages/00\_Docked/\_Assets/IntegratorContact](./integratorcontact.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `integrator-logo-full` | 1 | stylesheet |
| `integrator-logo-mark` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
