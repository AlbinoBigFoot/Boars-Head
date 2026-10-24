---
title: Utility Overview
sidebar_position: 2
description: The Groveport Utility Overview home page - plant floor plan with the 19 CG evaporators, AD/FD status tiles, underfloor temps and the KPI rail.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Utility/**/view.json"
last_verified: 2026-10-24
---

# Utility Overview

The home page of the local Groveport HMI: a floor plan of the plant with one evaporator symbol per control group
(CG), the ammonia detector (AD) and fire detector (FD) status tiles on the left, the two underfloor temperatures,
and a KPI rail on the right.

![Utility Overview](/img/perspective/utility-overview.png)

| | |
|---|---|
| Routes | `/plants/groveport/utility-overview` (title "Groveport Utility Overview"); `/` uses the same view, and in local mode the Header route guard redirects `/` here |
| View | [`00_Pages/Groveport/Utility/Overview`](../reference/views/00-pages/groveport/utility/overview.md) |
| Embeds | [`OverviewStatuses`](../reference/views/00-pages/groveport/utility/overviewstatuses.md) (left tile stack), [`OverviewKpis`](../reference/views/00-pages/groveport/utility/overviewkpis.md) (right rail), 19 x [`02_Components/01_Devices/Evaporator`](../reference/views/02-components/01-devices/evaporator.md) |
| Role gates | The page's controls are gated on `session.custom.Permissions.*`; keep the gates when you move or copy components |
| Nav | Groveport > Utility Overview |

## What It Shows

- **Floor plan** (`root/Draw`, a coordinate container). The CG positions follow the legacy FactoryTalk (FT)
  Utility Overview: West PH (F) and East PH (E) in the main grid, Dock G5 to G1 along the bottom, and the
  B / C / A / D column on the right. The **Machine Room** block is clickable and opens `/machine-room`.
- **Evaporator symbols**, one per CG. Each shows the zone air temperature, the status word (CLG, IDLE, STOP, DFT,
  FLT ...) and the alarm frame. Clicking one opens that CG's page (`navPage` param, for example `/cg-a1`). The
  same component opens the Evaporator faceplate instead when it has no `navPage` and a `faceplate` param, as on
  the CG pages.
- **AD / FD tiles** (left stack): `OverviewStatusTile` embeds that read DiscreteInput members and open the
  DiscreteInput faceplate. A tile goes dark with the alarm text (for example "FIRE ALM") when the input is in its
  alarm state, and shows a dash when the tag quality is bad.
- **Underfloor temps** (Freezer and SuperChill): click opens the Sensor faceplate for
  `[default]Boars_Head/GrovePort/Freezer/Sensors/Underfloor Temp` (and the SuperChill one).
- **KPI rail** (`OverviewKpis`): tabs Overview / Per Area / Per Control Group, a Control Group Average bar chart,
  Status Hours and Defrost Modes (average hours per status over 24 h), and a Status Mix donut. Clicking a bar or a
  donut slice highlights the matching CGs on the floor plan (the others dim to 22 % opacity).
- **Comm loss (2026-10-24):** a CG whose data is not Good shows a red COMM LOSS symbol and is left out of the averages and
  counts (no "0.0 F" and no STOP from a dead link); a chart with no data says No Data. See
  [Comm Loss And Value Quality](../../features/comm-loss-quality.md).

## Where The Data Comes From

| Item | Tag path |
|---|---|
| Evaporator symbol | `tagPath` = the CG instance, for example `[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1` (UDT `Devices/Evaporator`). It reads `/HmiStatus`, `/ZAT/Val` (zone air temp), `/CG/TooHot`, `/CG/TooCold`, `/Fans/Sts_Running`, the `_Alarms` summary members and `.Enabled` (out of service). |
| Highlight filter | `try(tag('[default]Boars_Head/GrovePort/<Area>/Utility/<CG>/HmiStatus'), null)` per CG |
| KPI rail | `custom.metrics`: a `now(60000)` expression with a script transform that reads each CG's `HmiStatus` and `ZAT` and is now one call, `shared.UtilityMetrics.get(24)`: live values plus one batched historian query for the last 24 h (zone temp = time-weighted average of the historized `ZAT/Val`; status dwell = hours per `CG/Sts_State`), cached on the gateway for 3 minutes. No history shows **No Data**; nothing is synthetic. See [Real Data](#real-data-no-synthetic-values). |
| AD / FD tiles | DiscreteInput instances (`Sts_PV`, `Cfg_0StText` / `Cfg_1StText`, `Cfg_Label`). See [Components](../components.md#overviewstatustile). |

Status codes (`HmiStatus`): 1 = CLG (cooling), 2 and 6 to 9 = defrost (base, pump-down, hot gas, bleed, fan
delay), 3 = FLT (fault), 5 = IDLE, anything else = STOP.

## Key Bindings

The CG dimming is a structured expression per symbol:

```js
// root/Draw/CG-A1  props.style.opacity  (expr-struct, then a script transform)
statusFilter: {view.custom.highlightStatus}
cgFilter:     {view.custom.highlightCg}
areaFilter:   {view.custom.highlightArea}
myCg:   'CG-A1'
myArea: 'Freezer'
myStatus: try(tag('[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/HmiStatus'), null)
```

The transform returns `1.0` for a match and `0.22` otherwise. The `highlight*` custom props are **not
persistent**, so a page reload clears the highlight. The KPI charts set them from their
`dataPointSelectionHandler` events.

The page scales to the screen through `shared.Scale.cssTransform` on the root style (see
[Page Guides](./index.md#patterns-shared-by-most-pages)).

## Changing It

- Move or add a CG: in the Designer open the view, drag the `Evaporator` embed (or copy one for a new CG and set its
  `tagPath`); keep its permission gates. Save and test.
- New status tile: add an `OverviewStatusTile` embed to `OverviewStatuses` with `label`, `diPath` and `tagPath`
  params.
- The KPI script lists the CGs per area in `sections_cfg`; a new CG has to be added there too.

## Real Data, No Synthetic Values

Since 2026-10-24 every number on the Utility Overview comes from the PLC and the historian. The old made-up numbers (a random
24-hour average and a made-up dwell mix) is gone, as is every other made-up series in the local Groveport views.

- **Live part:** one read of every CG's `ZAT/Val` and `HmiStatus` per refresh. A CG whose value is not Good is not
  counted (see [Comm Loss And Value Quality](../../features/comm-loss-quality.md)).
- **History part:** one batched query for the 19 `ZAT/Val` and 19 `CG/Sts_State` paths, shared by all clients through
  a 3-minute cache in the gateway (script library `shared.UtilityMetrics`).
  - **Zone temp** = time-weighted average over the time the CG has Good samples; an outage gap or bad quality is not
    counted.
  - **Status dwell** = hours the CG spent in each state, averaged over the CGs that have state history.
- **No Data rules:** no samples gives an empty tile that says **No Data** and an empty chart (the chart's "No Data"
  text); never a zero or a guess.
- **Dwell history starts 2026-10-24 about 13:35.** `PLC/CG_RL_Evap/Sts_State` was not historized before; history is now
  enabled on it (OnChange), so older hours read No Data.

**How To Change It:** Designer > Project Library > `shared` > `UtilityMetrics` holds the rules (window, cache time). To
change which tags are read, edit the CG UDT's history settings in the Tag Browser (right-click the member > Edit
tag > History) and the paths in the script. Check a value against the historian with Designer > Tag Browser > right-click
the tag > Quick Trend, or by querying the historian tables ([Historian](../../gateway/historian.md)).
