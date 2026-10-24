---
title: Trending
sidebar_position: 9
description: The Adhoc Trend page (/trending), saved trends (/trending/saved), the trend faceplate, the session trend basket and the right-click Add To Trend menu.
sources:
  - docs/trending.md
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/**/view.json"
  - "gateways/standard/data/projects/BH/ignition/script-python/shared/TrendContext/code.py"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json"
last_verified: 2026-10-24
---

# Trending

![Trending page with 4 pens on 3 plots](/img/perspective/trending.png)

One synced **tool row** sits above the plots (Trend Tools v2, 2026-10-24): a Zoom Time | Zoom Area | Pan segmented control (exactly one selected), Zoom In / Zoom Out, an Auto-Scale Y On / Off switch, Reset Zoom, a "Zoomed" chip and a mode hint. Zoom and pan are shared by all plots. The faceplate Trend tab and Quick History get the compact version. See [Trending And Add To Trend](../../features/trending.md) for the full tool list.

| | |
|---|---|
| Routes | `/trending` (title "Adhoc Trend"), `/trending/saved` (title "User Saved Trends") |
| Views | [`98_Configuration/AdhocTrend/Trend`](../reference/views/98-configuration/adhoctrend/trend.md), [`98_Configuration/AdhocTrend/UserSavedTrendConfig`](../reference/views/98-configuration/adhoctrend/usersavedtrendconfig.md), parts under `98_Configuration/AdhocTrend/_Assets/` (Plot, Pen, PenColor, PenPlot, ToolBar, SaveTrendConfig, LoadDeleteTrend ...) |
| Popups | `01_Popups/00_Faceplates/AdhocTrend` (the trend as a floating faceplate, `faceplateMode`), `AdhocTrendConfig` (its configuration beside it), `01_Popups/TrendContext/*` (right-click menu, toast, copy path, quick history) |
| Scripts | `shared.AdhocTrend` (pens, plots, colours), `shared.tagsTree` (historized tag tree), `shared.TrendContext` (right-click menu and basket), `shared.FaceplateTrend` (faceplate Trend tab) |
| SQL | `dbo.adhoc_trend_configs` through the named queries `AdhocTrend/Select`, `SelectTrendConfigById`, `Insert`, `Update`, `Delete` |
| Nav | Groveport > Operations > Trending and Saved Trends; header trend icon (with a pen-count badge) |

## The Trend Basket

All trend views share one session object, **`session.custom.AdhocTrend`** (defined in session props):

| Key | Meaning |
|---|---|
| `tags` | The pens: full history paths of the trended tags |
| `plots`, `penPlots` | Plots (stacked charts) and which plot each pen is on |
| `disabledPens` | Pens hidden without removing them |
| `timeRange`, `startDate`, `endDate`, `realtime`, `pointCount`, `aggregate` | Query window and resolution |
| `colors` | The fixed pen palette (data colours; they don't change with the theme) |
| `trendId`, `trendName`, `username`, `isShared` | The saved configuration that is loaded, if any |

A read-only summary, `session.custom.trend` (pens, count, key), feeds the header badge. The tool state (drag mode, Auto-Scale Y, zoom window) is `session.custom.trendTools`, shared by the tool row and every plot. Because the basket is a
session property, a pen added on one page is still there on the next page and in the trend faceplate.

## Add To Trend (Right-Click)

Every component that shows a historized value calls the trend context menu from its right-click:

```python
# events.dom.onContextMenu
shared.TrendContext.menu(self, event, '{view.params.tagPath}/ZAT/Val')
```

The third argument is a path template resolved at click time against the component (`{view.params.x}`,
`{view.custom.x}`, `{session.custom.x}`, `{../Sibling.props.x}` ...). The menu offers Add To Trend / Remove From
Trend, opening the trend, quick history and copying the path. It never writes tags: it only changes the session
basket, navigates and opens popups. A non-historized value still gets a menu (gray "Not Historized" row plus Copy Tag Path). Whether a path is historized comes from `shared.TrendHistorized` (generated
from the UDT definitions and tag config).

## The `/trending` Page

- **Tag browser** (hidden until opened): a tree of historized tags built on startup by
  `shared.tagsTree.getHistoricalTags()` / `createTree()`.
- **Tool row** (in `Trend`): drives `session.custom.trendTools`. The native zoom / pan / home icons of each chart are hidden so there is one set of tools; each chart keeps only its download menu (hidden without good data). Zoom Area pauses live updates. Pan works through a second copy of each chart that is created in pan mode (ApexCharts only reads that option at creation). `shared.TrendContext` holds the zoom-event handling.
- **Plots** (`_Assets/Plot`, ApexCharts `kyvislabs.display.apexchart`): one or more stacked charts. With no pens
  the chart shows "No Trend Data Source available. Please add Tags for Trending." With no good data it says "No Data".
- **Pens table** (`_Assets/Pen`): colour, plot, enable and delete per pen.
- **Toolbar** (`_Assets/ToolBar`, opened by the gear): realtime on / off, time range, aggregate, point count.
- **Save** (`_Assets/SaveTrendConfig`): writes the basket to `dbo.adhoc_trend_configs` (Insert / Update).

`custom.dbTrendConfig` loads a saved configuration with the named query `AdhocTrend/SelectTrendConfigById` when
`trendId` is set.

## Saved Trends (`/trending/saved`)

![Saved trends](/img/perspective/trending-saved.png)

A table of the saved configurations (`AdhocTrend/Select`) with Load / Delete per row
(`_Assets/LoadDeleteTrend`). Load copies the configuration into `session.custom.AdhocTrend` and opens `/trending`.
Delete runs the named query `AdhocTrend/Delete` with `isAdmin = shared.Security.allowed(self.session, 'Trends',
'ManageLocked')`, so only a role with the `Trends/ManageLocked` permission can delete locked configurations.

## Faceplate Trend Tab

Every device faceplate has a Trend tab (`01_Popups/00_Faceplates/_Assets/Trend`) that trends the device's own
historized members, built by `shared.FaceplateTrend`. See [Faceplates](../faceplates.md).

## Gotchas

- ApexCharts throws a browser error on a `null` series. Every chart series expression is wrapped as
  `list(value or [])`; keep that guard when you edit or add a chart.
- The chart layout depends on `!important` height and flex rules in the stylesheet
  (`/* Adhoc Trend ApexCharts ... */` sections). Don't remove them as "redundant"; see
  [Style Classes And Stylesheet](../styling/style-classes-and-stylesheet.md).
