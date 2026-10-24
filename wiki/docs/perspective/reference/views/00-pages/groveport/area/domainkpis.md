---
title: "DomainKpis"
sidebar_label: "DomainKpis"
description: "Perspective view 00_Pages/Groveport/Area/DomainKpis (Page): 2 components, 8 bindings, 0 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Area/DomainKpis", "DomainKpis", "/plants/groveport/club/epms", "/plants/groveport/club/production", "/plants/groveport/dock/epms", "/plants/groveport/dock/production", "/plants/groveport/east-ph/epms", "/plants/groveport/east-ph/production", "/plants/groveport/freezer/epms", "/plants/groveport/freezer/production", "/plants/groveport/machine-room/epms", "/plants/groveport/machine-room/production", "/plants/groveport/palletizing/epms", "/plants/groveport/palletizing/production", "/plants/groveport/superchill/epms", "/plants/groveport/superchill/production", "/plants/groveport/west-ph/epms", "/plants/groveport/west-ph/production"]
---

:::note

:::


**Page**: `00_Pages/Groveport/Area/DomainKpis`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Area/DomainKpis` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Area/DomainKpis/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Area &gt; DomainKpis |
| Routes | `/plants/groveport/club/epms` (Groveport Club EPMS)<br/>`/plants/groveport/club/production` (Groveport Club Production)<br/>`/plants/groveport/dock/epms` (Groveport Dock EPMS)<br/>`/plants/groveport/dock/production` (Groveport Dock Production)<br/>`/plants/groveport/east-ph/epms` (Groveport East PH EPMS)<br/>`/plants/groveport/east-ph/production` (Groveport East PH Production)<br/>`/plants/groveport/freezer/epms` (Groveport Freezer EPMS)<br/>`/plants/groveport/freezer/production` (Groveport Freezer Production)<br/>`/plants/groveport/machine-room/epms` (Groveport Machine Room EPMS)<br/>`/plants/groveport/machine-room/production` (Groveport Machine Room Production)<br/>`/plants/groveport/palletizing/epms` (Groveport Palletizing EPMS)<br/>`/plants/groveport/palletizing/production` (Groveport Palletizing Production)<br/>`/plants/groveport/superchill/epms` (Groveport SuperChill EPMS)<br/>`/plants/groveport/superchill/production` (Groveport SuperChill Production)<br/>`/plants/groveport/west-ph/epms` (Groveport West PH EPMS)<br/>`/plants/groveport/west-ph/production` (Groveport West PH Production) |
| Root | `ia.container.flex`, height 800, width 1400 |
| Size | 2 components, 8 bindings, 0 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-02T18:08:49Z by the Designer |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `rest` | `""` | bound (expr) |
| `slug` | `""` | bound (expr) |
| `domain` | `"epms"` | bound (expr) |
| `area` | `"Freezer"` | bound (expr) |

## Component Tree

Component types: ia.container.flex x1, ia.display.view x1.

```text
root  ia.container.flex  [2 bindings]
  DomainBody  ia.display.view  [2 bindings; view: (bound)]
```

## Bindings

8 bindings: expr 7, property 1.

**`(view)`**

- `custom.rest`: expression

```js
try(substring(coalesce({page.props.path}, ''), 18), '')
```


- `custom.slug`: expression

```js
try(substring({view.custom.rest}, 0, indexOf({view.custom.rest}, '/')), '')
```


- `custom.domain`: expression

```js
try(lower(substring({view.custom.rest}, indexOf({view.custom.rest}, '/') + 1)), 'epms')
```


- `custom.area`: expression

```js
case(coalesce({view.custom.slug}, ''), 'freezer', 'Freezer', 'superchill', 'SuperChill', 'club', 'Club', 'palletizing', 'Palletizing', 'east-ph', 'East PH', 'west-ph', 'West PH', 'dock', 'Dock', 'machine-room', 'Machine Room', 'Freezer')
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../common-patterns.md#pattern-2).

**`root/DomainBody`**

- `props.path`: expression

```js
if(coalesce({view.custom.domain}, '') = 'production', '00_Pages/Groveport/Domains/Production', '00_Pages/Groveport/Domains/EPMS')
```


- `props.params.area`: property `view.custom.area`

## Event Scripts And Handlers

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../scripting/reference/modules/shared-alerts.md).

## Related Views

**Bound embeds** (view path set by a binding): `root/DomainBody`

**Opens or names** (popups, scripts, expressions): [00\_Pages/Groveport/Domains/EPMS](../domains/epms.md), [00\_Pages/Groveport/Domains/Production](../domains/production.md)

**Opened or named by** (2): [00\_Pages/00\_Docked/Navigation](../../00-docked/navigation.md), [00\_Pages/00\_Docked/TempNav](../../00-docked/tempnav.md)

## Style Classes

| Class | Uses | Defined in |
|---|---|---|
| `bg-page` | 1 | style class |
| `kpi-dashboard-page` | 1 | stylesheet |

See the [style class catalog](../../../../style-classes.md) and the [stylesheet index](../../../../stylesheet.md).
