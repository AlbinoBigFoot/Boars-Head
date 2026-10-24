---
title: "Kpis"
sidebar_label: "Kpis"
description: "Perspective view 00_Pages/Groveport/Production/Level2/Kpis (Page piece (not routed)): 14 components, 8 bindings, 1 event scripts."
generated: true
keywords: ["00_Pages/Groveport/Production/Level2/Kpis", "Kpis"]
---

:::note

:::


**Page piece (not routed)**: `00_Pages/Groveport/Production/Level2/Kpis`.

| | |
|---|---|
| View path | `00_Pages/Groveport/Production/Level2/Kpis` |
| File | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Production/Level2/Kpis/view.json` |
| Designer | Project Browser &gt; Perspective &gt; Views &gt; 00\_Pages &gt; Groveport &gt; Production &gt; Level2 &gt; Kpis |
| Root | `ia.container.flex`, height 1016, width 500 |
| Size | 14 components, 8 bindings, 1 event handlers, 0 change scripts, 1 message handlers |
| Last saved | 2026-10-13T19:59:06Z by the Designer |

## Params

| Name | Default | Notes |
|---|---|---|
| `zone` | `"Prep"` | input |

## Custom properties

| Name | Default | Notes |
|---|---|---|
| `metrics` | `{}` | bound (expr-struct) |

## Component Tree

Component types: ia.display.label x8, ia.container.flex x5, ia.display.table x1.

<details>
<summary>Component tree (14 components)</summary>

```text
root  ia.container.flex  [2 bindings]
  RailTitle  ia.display.label  [1 binding]
  KpiGrid  ia.container.flex
    ZoneRate  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
    ZoneOEE  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
    ZoneDT  ia.container.flex
      Title  ia.display.label
      Value  ia.display.label  [1 binding]
  UnitTitle  ia.display.label
  UnitTable  ia.display.table  [1 binding; 1 event]
```

</details>

## Bindings

8 bindings: expr 6, expr-struct 1, property 1.

**`(view)`**

- `custom.metrics`: structured expression (expr-struct), then script + expression transform

```js
tick: now(60000)
zone: {view.params.zone}
Z_Rate: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/' + {view.params.zone} + '/Rate/Value')), false), false), try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/' + {view.params.zone} + '/Rate/Value')), null), null)
Z_OEE: if(coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/' + {view.params.zone} + '/OEE/Value')), false), false), try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/' + {view.params.zone} + '/OEE/Value')), null), null)
U_VD_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/OEE/Value')), null)
U_VD_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value')), null)
U_HOP_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/OEE/Value')), null)
U_HOP_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value')), null)
U_HND_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/OEE/Value')), null)
U_HND_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value')), null)
U_LDR_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/OEE/Value')), null)
U_LDR_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value')), null)
U_RSM_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/OEE/Value')), null)
U_RSM_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value')), null)
U_ST_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/OEE/Value')), null)
U_ST_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value')), null)
U_LS_OEE: try(toFloat(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/OEE/Value')), null)
U_LS_Status: try(toInt(tag('[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value')), null)
```

waitOnAll: `True`

Transform 1, script:

```python

# the custom report engine shared.Reports uses the same functions)
return shared.ProductionMetrics.l2(value)
```

Transform 2, expression:

```js
if((coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/' + {view.params.zone} + '/Rate/Value')), false), false) || coalesce(try(isGood(tag('[default]Boars_Head/GrovePort/Production/FCM/Zones/' + {view.params.zone} + '/OEE/Value')), false), false)), {value}, null)
```


**`root`**

- `meta.contextMenu.items`: expression, then script transform. Common pattern, see [pattern-3](../../../../../common-patterns.md#pattern-3).

- `meta.contextMenu.enabled`: expression. Common pattern, see [pattern-2](../../../../../common-patterns.md#pattern-2).

**`root/RailTitle`**

- `props.text`: expression

```js
'Zone KPIs — ' + {view.params.zone}
```


**`root/KpiGrid/ZoneRate/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.zoneRate}, 0), '#,##0') + ' lb/hr'
```


**`root/KpiGrid/ZoneOEE/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.zoneOee}, 0), '#,##0') + ' %'
```


**`root/KpiGrid/ZoneDT/Value`**

- `props.text`: expression

```js
numberFormat(coalesce({view.custom.metrics.zoneDowntime}, 0), '#,##0') + ' min'
```


**`root/UnitTable`**

- `props.data`: property `view.custom.metrics.units`

## Event Scripts And Handlers

- **`root/UnitTable`** `component.onRowClick`, script action, scope `G`

```python
row = event.row
if not row:
    return
uid = str(row.get('UnitId') or '')
if not uid:
    return
routes = {'VD': '/plants/groveport/production/vat-dumper', 'HOP': '/plants/groveport/production/hopper', 'HND': '/plants/groveport/production/handtman', 'LDR': '/plants/groveport/production/loaders', 'RSM': '/plants/groveport/production/roll-stock', 'ST': '/plants/groveport/production/shrink-tunnel', 'LS': '/plants/groveport/production/lazy-susan'}
r = routes.get(uid)
if r:
    system.perspective.navigate(page=r)
```

- **`root`** message handler `ticketLog` (scope: page). Common pattern, see [pattern-9](../../../../../common-patterns.md#pattern-9).

Project script calls: [shared.Alerts.contextMenuTicketLog](../../../../../../../scripting/reference/modules/shared-alerts.md), [shared.ProductionMetrics.l2](../../../../../../../scripting/reference/modules/shared-productionmetrics.md), [shared.Reports](../../../../../../../scripting/reference/modules/shared-reports.md).

## Related Views

**Embedded in** (3): [00\_Pages/Groveport/Production/Level2/Forming](./forming.md), [00\_Pages/Groveport/Production/Level2/Packaging](./packaging.md), [00\_Pages/Groveport/Production/Level2/Prep](./prep.md)

## Style Classes

<details>
<summary>13 classes</summary>

| Class | Uses | Defined in |
|---|---|---|
| `Fonts/Label` | 5 | style class |
| `Fonts/Title` | 1 | style class |
| `Fonts/Value` | 3 | style class |
| `container-card` | 4 | stylesheet |
| `container-card-border` | 1 | stylesheet |
| `fs-11` | 4 | style class |
| `fs-14` | 1 | style class |
| `fs-20` | 3 | style class |
| `fw-600` | 4 | style class |
| `fw-700` | 4 | style class |
| `text-muted` | 3 | style class |
| `utility-kpi-rail` | 1 | stylesheet |
| `utility-kpi-table` | 1 | stylesheet |

</details>

See the [style class catalog](../../../../../style-classes.md) and the [stylesheet index](../../../../../stylesheet.md).

## Tags And Data

<details>
<summary>15 literal tag paths</summary>

- `[default]Boars_Head/GrovePort/Production/FCM/HND/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HND/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/HOP/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LDR/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LDR/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LS/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/LS/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/RSM/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/ST/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/OEE/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/VD/Status/Value`
- `[default]Boars_Head/GrovePort/Production/FCM/Zones/`

</details>

Member paths appended to a base path in expressions (relative):

`/OEE/Value`, `/Rate/Value`

Tag folders and UDTs are documented under [Tags](../../../../../../../tags/index.md).
