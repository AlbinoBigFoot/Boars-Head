---
title: Trending And Add To Trend
sidebar_position: 6
description: The Trending page, Saved Trends, the faceplate Trend tab and the right-click Add To Trend menu (session trend basket). Updated 2026-10-23.
sources:
  - docs/trending.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py
  - gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py
  - gateways/standard/data/projects/BH/ignition/script-python/shared/FaceplateTrend/code.py
  - gateways/standard/data/projects/BH/ignition/named-query/AdhocTrend/**/*
  - sql/adhoc_trend_configs.sql
last_verified: 2026-10-24
---

# Trending And Add To Trend

## What it does

Lets anyone plot the history of any historized value without building a screen:

- **Trending page** (Operations > Trending, `/trending`, view `98_Configuration/AdhocTrend/Trend`): up to **10
  pens** on one or more plots (analog and discrete plots, pens movable between plots), time range, X-trace
  (crosshair with a shared tooltip), zoom and pan.
- **Saved Trends** (`/trending/saved`, view `98_Configuration/AdhocTrend/UserSavedTrendConfig`): save the current
  trend under a name, personal or shared; the FT trend displays are seeded as **locked** system trends.
- **Faceplate Trend tab**: each device faceplate opens a trend with that device's default pens
  (`shared.FaceplateTrend.defaultPens`, for example compressor suction / discharge pressures and temperatures,
  evaporator zone air temp and defrost time left).
- **Add To Trend from anywhere**: right-click a historized value, pick **Add To Trend**; the pen goes into your
  session's **trend basket** and the Trending page / Adhoc Trend popup shows it.

![Trending page: 4 pens on 3 plots, each plot with its own tool row](/img/features/trending/trending-basket.png)

## How to use it (operators)

1. Right-click a value (a tank level, a compressor pressure, a zone temperature ...).
2. The trend menu (header = pen name and full tag path) offers **Add To Trend** / **Remove From Trend**, **Open
   Trend** (goes to `/trending`), **Quick History** (an 8-hour chart popup with the same tools), **Copy Tag Path**
   (a popup with the path selected) and **Ticket Logger** (only for sessions with Ticket Logger access). A value that
   is not historized shows a gray, disabled **Not Historized** row plus Copy Tag Path, so a right-click never does
   nothing; labels and titles with no tag get no menu. Left-click is unchanged (faceplates still open). Escape or a
   click outside closes the menu.
3. A short toast confirms ("Added CG-E4 Zone Temp"); the header trend icon shows the pen count.
4. On the Trending page arrange pens, change the range, use the per-plot tools, and **Save** (needs
   `Trends/Save`; overwriting a locked or someone else's trend needs `Trends/ManageLocked`).

The basket holds at most 10 pens; adding an 11th shows a warning.

### Trending page tools

Redesigned 2026-10-24: **one set of chart tools above all plots**, the same on the Trending page, the faceplate Trend
tab and Quick History (the faceplate and Quick History versions are compact).

- **Top bar**: 1H / 8H / 24H / 7D presets, Live / Paused (any zoom or pan pauses), add plot (+), remove plot (-),
  save, and the gear for a custom date range.
- **Drag mode** (one segmented control, exactly one selected, default Zoom Time):
  - **Zoom Time**: drag across a chart to zoom into that time range.
  - **Zoom Area**: drag a box to zoom into time **and** value. The time part applies to every plot; the value part
    stays on the plot you drew on. **Zoom Area pauses live updates**, because a data refresh would undo the value
    zoom; on the faceplate the 15 s refresh stops while it is selected.
  - **Pan**: drag left or right to move through time. Switching from Zoom Area to another mode drops the value zoom.
- **Zoom In / Zoom Out** (Trending page): halve or double the visible time range around its centre.
- **Auto-Scale Y** (On / Off switch): On fits each plot's value axis to the visible data; Off covers the whole
  query range. It defaults to On on the faceplate and Off in Quick History.
- **Reset Zoom**: grayed out until zoomed; returns every plot to the full range and drops a Zoom Area value zoom.
- **Zoomed chip**: "Zoomed: 14:02 - 15:10 | Reset" shows only while zoomed; click it to reset.
- **Mouse wheel** zooms in time; **double-click** a chart resets (same as Reset Zoom).
- A **hint line** under the tools changes with the mode.
- **Download menu** (the three-line icon at the top right of each chart): PNG, SVG or CSV of that chart. It appears
  only while the chart has good data; with none the chart says **No Data**. The other native chart icons are hidden
  because they duplicated these tools.
- **Each plot** has a header with its title and pen count and **Remove Plot** (not on the Default plot).
- **Zoom and pan are shared by all plots**: a zoom on any plot moves every plot to the same window; Reset Zoom, a
  preset or Live restores them all.
- **X-trace**: hovering a plot shows a crosshair and one tooltip with every pen of that plot (not across plots).
- **Legend**: click an item to hide or show a pen. In the pen table the **Plot** column moves a pen to another
  plot, the checkbox turns it on or off, Remove drops it.
- **Gaps, not zeros**: time with no good history (before the first sample, or after a communication loss) is drawn
  as a gap. The historian returns 0.0 for such windows, so `shared.TrendContext.points()` turns bad-quality Tall
  rows into null.
- The **faceplate Trend tab** has a pen picker, a range dropdown (up to 24 h refreshes every 15 s, not while Zoom
  Area is selected) and the compact chart tools; it is one chart.

![The right-click trend menu on a tank level (header = pen name and full tag path)](/img/features/trending/add-to-trend-menu.png)

## Where to find it

- **HMI**: nav Groveport > Operations > Trending and Saved Trends; the header trend icon; right-click any value.
- **Designer**: Project Browser > Perspective > Views > `98_Configuration` > `AdhocTrend` (the page and its parts),
  `01_Popups` > `TrendContext` (menu, toast, copy path, quick history); scripts under Project Browser > Scripting >
  Project Library > `shared` > `TrendContext`, `AdhocTrend`, `TrendHistorized`.
- **Gateway web UI**: the history comes from the SQL historian (Services > Historians > Historians > `historian`); saved trends are rows in the
  database connection `ignition`. A value is only trendable if its tag has History enabled (Designer > Tag Browser >
  right-click the tag > Edit tag > History).

## Where the pieces live (developers)

| Piece | Where |
|---|---|
| Trend basket | session prop `session.custom.AdhocTrend` (`tags`, `plots`, `penPlots`); read-only summary `session.custom.trend {pens, count, key}` |
| Context menu | every component showing a historized value gets `events.dom.onContextMenu` -> `shared.TrendContext.menu(self, event, '<path template>')` ; popups `01_Popups/TrendContext/{Menu, Toast, CopyPath, QuickHistory}` |
| Historized check | `shared.TrendHistorized` (an index of the historized types, instances and standalone tags; skips `_RCP1_`, `System` and String members; holds `TYPES`, `INSTANCES`, `TAGS`, `OVERRIDES`, label words, units and `LEGACY` pre-PAX names). `shared.TrendContext.is_historized(path)` checks standalone set, override, then the owning UDT instance; only a path outside every known instance falls back to one cached `.HistoryEnabled` read (30 types, 128 instances, 42 standalone tags on 2026-10-23) |
| Plot helpers | `shared.AdhocTrend` (plots, pens, colours, routing a new tag to an analog or discrete plot by data type) |
| Popups | `shared.Alerts.showAdhocTrend()` (Adhoc Trend faceplate, bottom right), `showAdhocTrendConfig()` |
| Saved trends | SQL `dbo.adhoc_trend_configs` via `AdhocTrend/{Select, SelectTrendConfigById, Insert, Update, Delete}` |
| Faceplate defaults | `shared.FaceplateTrend.defaultPens(tagPath)` |
| History source | the SQL historian (see [Ignition Tables](../database/ignition-tables.md)) |

## How it works

- `menu(component, event, template)` resolves the path template against the clicked component at click time
  (`{view.params.tagPath}`, `{view.custom.x}`, `{session.custom.x}`, `{../Sibling.props.x}` references), turns it
  into the full atomic history path, checks it is historized, and opens the menu popup at the mouse position.
- Menu rows call `shared.TrendContext.menu_action(component, action)`: `add`, `remove`, `toggle` change only the
  session basket; `open` navigates to `/trending`; `quick` opens Quick History; `copy` the path popup; `ticket`
  the Ticket Logger. **The menu never writes a tag.**
- Pens are stored as full atomic history paths; labels come from `shared.TrendContext.label` ("CG-E4 Zone Temp").

## How To Change It

All steps are Designer edits; save, then test in a session.

- **Make a value trendable from the right-click menu:**
  1. Historize the tag or UDT member: Tag Browser > the tag > Edit Tag > **History** (enable, sample mode, tag
     group). For a UDT member do it on the UDT definition so every instance follows.
  2. On the component that shows the value, add an `onContextMenu` DOM event (Component Events > dom >
     `onContextMenu`, script) that calls `shared.TrendContext.menu(self, event, '<path template>')`. The template
     resolves against the clicked component, for example `{view.params.tagPath}`.
  3. The menu works for any historized path: a path not yet known to the `shared.TrendHistorized` index falls back to
     one cached `.HistoryEnabled` read. Add the new type or instance to that module's index only to avoid that read.
- **A component with its own `onContextMenu`, left-click handlers or write controls** should not get the menu. Skip
  the Report Builder, the trend views themselves, the docked header and nav, the Alerts popups, Ticket Logger and
  Integration views. PLC rack channel rows use `custom.trendPath` (`<module>/Ch<n>Data`, `<module>/Data`); those
  members are not historized, so they show "Not Historized".
- **Menu rows and popups:** Views > `01_Popups/TrendContext` (`Menu`, `Toast`, `CopyPath`, `QuickHistory`); the row
  actions are in `shared.TrendContext.menu_action` (Project Library).
- **Chart tools:** the tool row is part of the trend views (Trending page `98_Configuration/AdhocTrend/Trend`, the
  faceplate `01_Popups/00_Faceplates/_Assets/Trend`, Quick History under `01_Popups/TrendContext`). Drag mode and
  Auto-Scale Y live in the session custom properties (Perspective > Session Properties > Custom > `AdhocTrend`). The
  chart's drag behaviour is its `props.options.chart.zoom` setting and Auto-Scale Y is `chart.zoom.autoScaleYaxis`.
  Pan needs a second copy of each chart created in pan mode (the chart library only reads that setting when the
  chart is created), so edit both copies when you change chart options, and keep their `props.series` bound to the
  zoom chart.
- **Plots, pens and colours:** `shared.AdhocTrend` (Project Library); the trend views are under
  `00_Pages/Boars Head/Operations`. The plots sync zoom through `shared.AdhocTrend.zoom_event` / `zoom_reset`
  (`session.custom.AdhocTrend.zoomMin/zoomMax`, epoch ms) because the chart drops the group id.
- **Saved trends:** Named Queries > `AdhocTrend` (`Select`, `SelectTrendConfigById`, `Insert`, `Update`, `Delete`);
  table `dbo.adhoc_trend_configs`.
- **Faceplate default pens:** `shared.FaceplateTrend.defaultPens(tagPath)`.
- **Permissions:** `Trends/Save` and `Trends/ManageLocked` in the matrix
  ([Roles And Permissions](roles-permissions.md#how-to-change-it)).

## Known limitations and parked items

- No cross-plot x-trace (the tooltip covers the hovered plot's pens only).
- A zoom does not requery: resolution is the Point Count over the full range.
- Real PLC history only starts 2026-10-23 around 09:30; live mode against fresh PLC data is pending the SecureLink.
- Faceplate trend pens can share a colour (pre-existing palette). 10-pen limit per session basket.
- The DI and Tank faceplates still carry older context-menu handlers; replace them with the single
  `shared.TrendContext.menu(...)` call described above when those views are next edited.

Source of truth: `docs/trending.md`.
