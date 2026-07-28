---
quick_id: 260727-vma
slug: rebuild-adhoc-trend-multi-plot-ux-n-empt
phase: quick-260727-vma
plan: "01"
type: execute
mode: quick
branch: feature/adhoc-trend-nplots
wave: 1
depends_on: []
autonomous: true
requirements: [ADHOC-NPLOT]
files_modified:
  - gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py
  - gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/resource.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/resource.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenPlot/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenPlot/resource.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/Trend/view.json
  - scripts/_verify_adhoc_helpers.py
  - scripts/_verify_adhoc_views.py

must_haves:
  truths:
    - "Clicking the + icon (immediately left of Save Config) appends an empty plot and the new plot appears without a page reload."
    - "With exactly one plot, the chart fills the whole chart area — no tiny chart with a large empty gray band below it."
    - "With 2+ plots, every plot gets an equal share of the chart area height."
    - "Gear/Config icon, Realtime indicator, chart-type label and time-range labels are fully visible (not vertically clipped) in both full-page and faceplate mode."
    - "A pen for [default]Evaporators/EV-01/Pressure/Value is labeled EV-01 in the legend, pen table and chart series."
    - "Adding a float tag routes it to an analog plot; adding a boolean or integer status tag routes it to a discrete plot (created if none exists)."
    - "A pen can be moved to any other plot from the pen table, including across analog/discrete kinds, and the chart re-renders."
    - "plots and penPlots survive a Save Config / Load Config round trip."
  artifacts:
    - gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenPlot/view.json
  key_links:
    - "Trend Plots flex-repeater props.instances <- session.custom.AdhocTrend.plots (plain-list reassignment on add/remove)"
    - "Plot view custom.pens <- shared.AdhocTrend.pens_for_plot(session pens, penPlots, view.params.plotId)"
    - "Pen table plotId column view -> shared.AdhocTrend.move_pen -> session.custom.AdhocTrend.penPlots"
    - "Every Perspective resource.json lastModificationSignature + .resources CAS digests repaired after edits"
---

<objective>
Rebuild the Adhoc Trend multi-plot experience on clean `main`: the operator can create as many empty plots as they want, drop pens onto any of them freely, and the layout behaves correctly at 1 plot and at N plots.

Purpose: the previous attempt (`origin/ticket/12639491179-adhoc-trend-second-plot`, commit `050f184`) shipped magnitude-based auto-splitting plus a broken layout — text "Add Plot" button, a no-op add action, a squashed single plot, and a clipped toolbar. This rebuild replaces automatic splitting with explicit user-driven plots and fixes every layout defect.

Output: a `shared.AdhocTrend` script package, two new Perspective asset views (`_Assets/Plot`, `_Assets/PenPlot`), reworked `Trend/view.json` layout, session state for `plots`/`penPlots`, and stylesheet rules for equal-flex plot stacking.
</objective>

<context>
@.planning/STATE.md
@.planning/quick/260727-vma-rebuild-adhoc-trend-multi-plot-ux-n-empt/260727-vma-CONTEXT.md
@.cursor/rules/perspective-reference.mdc
@.cursor/rules/perspective-css-only.mdc
@.cursor/rules/perspective-json-newlines.mdc
@.cursor/rules/perspective-ticket-logger.mdc
@.cursor/rules/ignition-resource-signatures.mdc
@.cursor/rules/hbt-to-shared.mdc
@docs/ignition-resource-signatures.md
</context>

<current_state>
Verified on `feature/adhoc-trend-nplots` (branched from `origin/main`) — this is the ground truth the executor is editing:

**`98_Configuration/AdhocTrend/Trend/view.json` component tree**

```
/root                                          ia.container.flex
  /TagTree                                     ia.container.flex   (basis 260px)
    /Label /Tree /AddToTrend
  /TrendContainer                              ia.container.flex   (grow 1, classes adhoc-trend-chart-host)
    /Trend                                     ia.container.coord  (basis 92%, grow 1)   <-- COORD, percentage children
      /apexchart                               kyvislabs.display.apexchart  (y 0.06, height 0.94, width 1)
      /Icons                                   ia.container.flex   (height 0.07, width 0.5, x 0.0)
        /tagBrowser /trendConfig /ChartType /TimeRange /StartDate /EndDate
      /Buttons                                 ia.container.flex   (height 0.07, width 0.48, x 0.51)
        /SaveTrendConfig /UpdateTrendConfig /ClearPens
      /TrendName                               ia.display.label    (height 0.0471, width 0.4, x 0.3)
    /Pens                                      ia.container.flex   (direction column, classes container-card)
      /Toggle
        /Toggle                                ia.input.checkbox
        /Pens                                  ia.display.flex-repeater  (path 98_Configuration/AdhocTrend/_Assets/Pen)
      /Table                                   ia.display.table
    /NoPens                                    ia.input.text-area
```

**Root cause of the toolbar clipping:** `Icons` and `Buttons` are children of a *coordinate* container at `height: 0.07`. At full page height that is ~60px, but in faceplate/popup mode the container is much shorter, so 7% collapses below the 32px button height and the row is cut off. Fixing this requires converting `/root/TrendContainer/Trend` from `ia.container.coord` to `ia.container.flex` (column) with a fixed-pixel toolbar row. That conversion is also what makes N plots stack with equal flex.

**`Trend` view.custom props:** `aggregate, colors, dataset, dbTrendConfig, endDate, historicalDataset, isConfigUpdated, key, pens, pointCount, realTime, realTimeDataset, startDate, tags, timeRange, treeVisible, trendId, trendName, username`.

**`custom.pens` binding** — expr-struct over `{view.custom.tags}` + `{view.custom.colors}`, script transform emits a Dataset with headers `["penEnabled","tagPath","penName","alias","engUnit","penColor","penAction"]`. Today `penName` comes from `.Name` / Metadata `longDescription`, which is how pens end up labeled `Value` or `Pressure` instead of `EV-01`.

**`custom.realTimeDataset` binding config** (copy this shape into the Plot asset view):

```json
{"aggregate": "Average", "avoidScanClassValidation": true,
 "dateRange": {"mostRecent": "{view.custom.timeRange}", "mostRecentUnits": "HOUR"},
 "enableValueCache": true, "ignoreBadQuality": false, "polling": {"enabled": true, "rate": "5"},
 "preventInterpolation": false, "returnFormat": "Wide",
 "returnSize": {"numRows": "{view.custom.pointCount}", "type": "FIXED"},
 "tags": "{view.custom.key}", "valueFormat": "DATASET"}
```

**Pen table view-rendered cell contract** (from `_Assets/PenEnable`): the embedded view receives params `row` (row index), `rowData` (whole row object), `value` (that column's value). `_Assets/PenDelete` receives only `row`. Reuse this contract for the new `_Assets/PenPlot`.

**Session state** (`session-props/props.json` → `custom.AdhocTrend`) currently has `aggregate, chartType, colors, endDate, isShared, pointCount, realtime, startDate, tags, timeRange, trendId, trendName, username`. There is no `plots` and no `penPlots`.

**Not present on this branch:** `shared/AdhocTrend`, `_Assets/Plot`, `_Assets/PenPlot`. Existing `shared` packages are `Alarms, Alerts, Overview, tagsTree, TicketLogger, Utilities`.

**Prior-art to mine (read-only, do not check out):**

```
git show origin/ticket/12639491179-adhoc-trend-second-plot:gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py
```

Reuse `resolve_column(dataset, alias)` and the `filterColumns` series-building loop verbatim. Discard everything magnitude/scale related — `RANGE_RATIO_THRESHOLD`, `_column_extent`, `_magnitude_bucket`, `_pen_scale_key`, `scale_groups`, `needs_dual_plot`. Automatic scale-based splitting is explicitly rejected as product behavior.

**Layout sketch to mine:** `scripts/_fix_adhoc_nplots_ui.py` contains the intended `apply_add_plot` + plain-list reassignment idea, the `+` icon button props, and the equal-flex CSS. Treat it as a sketch; write the real implementation cleanly rather than running it.
</current_state>

<house_rules>
Non-negotiable for every file this plan touches:

1. **Signatures.** After any edit under `gateways/*/data/projects/`, run `python scripts/repair-resource-signatures.py`, then `python scripts/repair-resource-signatures.py --check` (must exit 0). Never hand-write a `lastModificationSignature`.
2. **Newlines.** No `\r` inside any JSON `"code"`, `"script"`, or `"expression"` string. Write JSON files with `newline="\n"`.
3. **Tab indentation.** Every executable line inside a Perspective `"code"` / `"script"` value starts with a tab, Designer-style. This does *not* apply to `script-python/**/code.py`, which is a normal Python file (use tabs there anyway to match the existing repo style).
4. **propConfig keys are scoped.** `props.text`, `props.style.classes`, `params.plotId`, `position.basis`, `custom.pens` — never a bare key.
5. **CSS only.** All styling goes in `com.inductiveautomation.perspective/stylesheet/stylesheet.css` as `psc-`-prefixed classes referenced by simple names in `props.style.classes`. Do not create Designer Style Classes and do not use path-style names like `Fonts/Value`.
6. **`shared.*`, never `HBT.*`.**
7. **Ticket logger.** Both new views get root `meta.contextMenu`, the gated `meta.contextMenu.enabled` / `meta.contextMenu.items` propConfig pair, and the `ticketLog` page-scope message handler. Copy the exact shape from `_Assets/Pen/view.json`.
8. **Edit JSON programmatically.** `Trend/view.json` is ~375 KB. Use a Python script with `json.load` / `json.dump(indent=2)` rather than hand-editing, and re-scrub `\r` from code strings before writing.
</house_rules>

<tasks>

<task type="auto" tdd="true">
  <name>Task 1: shared.AdhocTrend helper package + plots/penPlots session state</name>
  <files>
gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py (new)
gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/resource.json (new)
gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json (modify)
scripts/_verify_adhoc_helpers.py (new)
  </files>
  <behavior>
`pen_label` (UDT-instance naming):
- `[default]Evaporators/EV-01/Pressure/Value` → `EV-01`
- `[default]Evaporators/EV-01/Pressure` → `EV-01`
- `[default]Compressors/AU5-C1/Suction/Value` → `AU5-C1`
- `[default]Misc/SomeTag/Value` → `SomeTag` (only one segment left after stripping the member → fall back to it)
- `[default]LoneTag` → `LoneTag`
- Two pens resolving to the same label are disambiguated by appending the member name: `EV-01 Pressure`, `EV-01 Temperature`.

`tag_kind`:
- datatype `Boolean` → `discrete`; `Int1/Int2/Int4/Int8` → `discrete`; `Float4/Float8`/`Double` → `analog`; unknown/unreadable → `analog`.

`add_plot` / `plain_plots`:
- `add_plot` on a config whose plots are `[{"id":"p0",...}]` appends `{"id":"p1","title":"Plot 2","kind":"analog"}` and returns a plain `list` of plain `dict`s (not a Perspective wrapper).
- `plain_plots(None)` returns `default_plots()` — a single `p0` analog plot.

`move_pen`:
- `move_pen(cfg, "Evaporators-EV_01-Pressure", "p1")` sets `penPlots["Evaporators-EV_01-Pressure"] = "p1"` and returns the plain dict.

`remove_plot`:
- Refuses (`ok=False`) when the plot still has pens assigned, or when it is the last remaining plot; otherwise removes it and returns `ok=True`.

`route_new_tag`:
- Float tag with only an analog plot present → routed to that analog plot.
- Boolean tag with only an analog plot present → a `discrete` plot is created and the tag routed to it.
- Boolean tag when a `discrete` plot already exists → routed to the existing discrete plot, no new plot.
  </behavior>
  <action>
Create the `shared.AdhocTrend` script package. Write `code.py` as plain Jython-2.7-compatible Python that references the Ignition `system` module **only inside function bodies** (never at import time) so the verification harness can import it with a stub.

Public API to implement (keep it small and readable; helpers prefixed with `_`):

- `DEFAULT_COLORS` — the ten-color list already in `session-props/props.json`.
- `default_plots()` → `[{"id": "p0", "title": "Plot 1", "kind": "analog"}]`.
- `_as_list(value)`, `_cfg_get(cfg, key, default)`, `_cfg_set(cfg, key, value)`, `_plot_field(p, key, default)` — tolerate both plain dicts and Perspective `PropertyTreeScriptWrapper` objects (attribute access and `.get()` both). Lift these from the sketch in `scripts/_fix_adhoc_nplots_ui.py`, which already worked around the wrapper problem.
- `plain_plots(cfg_or_plots)` → plain `list[dict]` with `id`/`title`/`kind` coerced to `str`. This is the value the UI reassigns onto `session.custom.AdhocTrend.plots`; reassigning a plain list is what forces Perspective bindings to re-evaluate, and its absence is why the previous Add Plot silently did nothing.
- `plain_pen_plots(cfg)` → plain `dict` of `alias -> plotId`.
- `normalize_config(cfg)` → ensure `plots` (non-empty) and `penPlots` (dict) exist; safe to call repeatedly.
- `alias_for(tag_path)` → existing repo rule: drop a trailing `/Value`, take the part after `]`, replace `/` with `-` and spaces with `_`.
- `pen_label(tag_path)` → UDT-instance name per D-"Pen naming". Algorithm: strip the `[provider]` prefix, strip a trailing `/Value`, split on `/`; if two or more segments remain return the second-to-last (the UDT instance holding the member), otherwise the last. Then, only if it is unambiguous, allow tag metadata to override: read `<candidate>.TypeId`; if that read succeeds and returns a non-empty string the candidate really is a UDT instance, so keep the path-derived name. Never fall back to the leaf `Value` and never use the member folder (`Pressure`).
- `pen_labels(tag_paths)` → list of labels with duplicates disambiguated by appending the member segment.
- `tag_kind(tag_path)` → `"analog"` or `"discrete"` from `system.tag.readBlocking([<value path>.DataType])`, wrapped in try/except with `"analog"` as the fallback.
- `build_pens(tags, colors)` → Ignition Dataset with headers `["penEnabled", "tagPath", "penName", "alias", "engUnit", "penColor", "plotId", "penAction"]`. Preserve today's behaviour for `tagPath` (append `/Value` when absent) and `engUnit` (`.EngUnit` read). Set `penName` from `pen_labels`. `plotId` comes from `penPlots` when present, else the first plot id. Note the two new/renamed columns: `plotId` is new and `penAction` stays last.
- `pens_for_plot(pens, pen_plots, plot_id, first_plot_id)` → filtered Dataset of enabled pens assigned to `plot_id`; pens with no assignment fall through to `first_plot_id`.
- `resolve_column(dataset, alias)` → copy verbatim from the prior-ticket `code.py`.
- `build_series(dataset, pens)` → the `filterColumns` loop from the prior ticket, reduced to a single plot (no `plot_index`, no scale grouping): for each enabled pen resolve its column, append it to `["t_stamp", col]`, emit `{"name": penName or alias, "color": penColor, "data": system.dataset.filterColumns(dataset, cols)}`, then remove the column again.
- `build_key(pens, aggregate)` → the `[{"aggregate", "alias", "path"}]` list the tag-history binding consumes.
- `add_plot(cfg, title=None, kind="analog")` → append `{"id": _new_plot_id(...), "title": title or "Plot N", "kind": kind}`, write back with `_cfg_set`, return the new plot id.
- `apply_add_plot(cfg, title=None, kind="analog")` → `add_plot` then return `plain_plots(cfg)` for direct session reassignment.
- `remove_plot(cfg, plot_id)` → `(ok, message)`; refuse with `"Keep at least one plot."` when only one plot remains and `"Move or remove pens from this plot before deleting it."` when pens are still assigned.
- `move_pen(cfg, alias, plot_id)` → set the assignment and return `plain_pen_plots(cfg)`.
- `route_new_tag(cfg, tag_path)` → `(plot_id, plots, pen_plots)`. Choose the first plot whose `kind` matches `tag_kind(tag_path)`; if the tag is discrete and no discrete plot exists, append one titled `"Status"` with `kind: "discrete"`; assign the tag's alias to that plot.
- `plot_options_overrides(kind)` → `{"stroke": {"curve": "stepline"}, "yaxis": {"decimalsInFloat": 0}}` for `discrete`, `{}` for `analog`. Small, optional polish so status pens do not render as diagonal ramps.

Do **not** port `RANGE_RATIO_THRESHOLD`, `_column_extent`, `_magnitude_bucket`, `_pen_scale_key`, `scale_groups`, `needs_dual_plot`, or `pens_for_plot(dataset, pens, plot_index)` from the prior ticket. Magnitude-based auto-splitting is rejected product behaviour, and shipping it dormant invites its reintroduction.

Create `resource.json` for the package with `{"scope": "A", "version": 1, "restricted": false, "overridable": true, "files": ["code.py"], "attributes": {...}}` matching the other `shared/*` packages; let `repair-resource-signatures.py` fill in the signature.

Extend `session-props/props.json` `custom.AdhocTrend` with `"plots": [{"id": "p0", "title": "Plot 1", "kind": "analog"}]` and `"penPlots": {}` so a fresh session starts with exactly one analog plot and no assignments. Leave every existing key untouched.

Write `scripts/_verify_adhoc_helpers.py`: install a stub `system` module into `sys.modules` (stub `system.tag.readBlocking`, `system.dataset.toDataSet`, `system.dataset.toPyDataSet`, `system.dataset.filterColumns` with the minimum needed), import `code.py` by file path, and assert every case listed in `&lt;behavior&gt;`. It must exit non-zero on any failure.
  </action>
  <verify>
    <automated>python scripts/_verify_adhoc_helpers.py</automated>
    <automated>python -c "import json,io; d=json.load(io.open(r'gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json',encoding='utf-8'))['custom']['AdhocTrend']; assert d['plots'][0]['id']=='p0' and d['plots'][0]['kind']=='analog', d['plots']; assert d['penPlots']=={}; assert 'tags' in d and 'colors' in d; print('session state OK')"</automated>
    <automated>python scripts/repair-resource-signatures.py &amp;&amp; python scripts/repair-resource-signatures.py --check</automated>
  </verify>
  <done>`shared.AdhocTrend` exists with the full API above and no magnitude-split code; `_verify_adhoc_helpers.py` passes including the `EV-01` naming cases; session state ships one default analog plot and an empty `penPlots`; signature check exits 0.</done>
</task>

<task type="auto">
  <name>Task 2: _Assets/Plot and _Assets/PenPlot views + equal-flex stylesheet rules</name>
  <files>
gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json (new)
gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/resource.json (new)
gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenPlot/view.json (new)
gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/PenPlot/resource.json (new)
gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css (modify)
scripts/_verify_adhoc_views.py (new)
  </files>
  <action>
Build the two reusable asset views. Each Plot instance owns its own tag-history query, keyed off `session.custom.AdhocTrend` and its own `plotId` param — this is what decouples the plots from the parent Trend view, which cannot pass Datasets down through a flex-repeater `instances` array.

**`_Assets/Plot/view.json`**

`props.defaultSize`: `{"height": 320, "width": 800}`.

`params`: `plotId` (`""`), `plotTitle` (`""`), `plotKind` (`"analog"`), `plotCount` (`1`) — all `paramDirection: "input"`, `persistent: true` via `propConfig["params.*"]`.

`view.custom` + bindings (mirror the Trend view's existing chain, but scoped to this plot):
- `custom.pens` — expr-struct over `{session.custom.AdhocTrend}` and `{view.params.plotId}`, script transform returning `shared.AdhocTrend.pens_for_plot(shared.AdhocTrend.build_pens(tags, colors), penPlots, plotId, firstPlotId)`.
- `custom.key` — script transform over `custom.pens` returning `shared.AdhocTrend.build_key(pens, aggregate)`.
- `custom.realTime`, `custom.timeRange`, `custom.pointCount`, `custom.startDate`, `custom.endDate`, `custom.aggregate` — plain property bindings onto the matching `session.custom.AdhocTrend` keys.
- `custom.realTimeDataset` / `custom.historicalDataset` — `tag-hist` bindings copying the config shape quoted in `<current_state>` (realtime keeps `polling.enabled: true` and `dateRange.mostRecent`; historical uses `startDate`/`endDate`).
- `custom.dataset` — expr-struct choosing realtime vs historical, same `if({value}['realTime'], ...)` expression the Trend view uses today.

`root`: `ia.container.flex`, `direction: "column"`, `props.style.classes: "adhoc-trend-plot-slot"`. Children:
1. `Header` — `ia.container.flex`, `position: {"basis": "24px", "shrink": 0, "grow": 0}`, class `adhoc-trend-plot-header`. Contains `Title` (`ia.display.label`, `props.text` bound to `view.params.plotTitle`, class `adhoc-trend-plot-title`, `position.grow: 1`) and `RemovePlot` (`ia.display.icon`, `props.path: "material/close"`, `position: {"basis": "20px", "shrink": 0}`, `meta.visible` bound to an expression that is true when `{view.params.plotCount} > 1`). `RemovePlot` `onClick` calls `shared.AdhocTrend.remove_plot(...)`; on refusal show `shared.Alerts.showAlert(state="warning", title="Cannot Remove Plot", ...)`, on success reassign `self.session.custom.AdhocTrend.plots = shared.AdhocTrend.plain_plots(cfg)`.
2. `apexchart` — `kyvislabs.display.apexchart`, `position: {"grow": 1, "shrink": 1, "basis": "0px"}`, `props.style.classes: "adhoc-trend-apex"`, `props.style.overflow: "visible"`, `props.style.minHeight: 0`. Copy `props.options` wholesale from the existing `/root/TrendContainer/Trend/apexchart` node in `Trend/view.json` (chart events, xaxis datetime formatter, grid padding, tooltip, legend, stroke), then apply `shared.AdhocTrend.plot_options_overrides(view.params.plotKind)` on top. `props.series` is a script transform over `custom.dataset` + `custom.pens` returning `shared.AdhocTrend.build_series(dataset, pens)`. Bind `props.type` to `session.custom.AdhocTrend.chartType` as the Trend view does today.

Set `props.options.chart.height` to `"100%"` (not the current hardcoded `350`) so the chart tracks its flex slot instead of pinning itself — a fixed pixel height here is the other half of the "tiny chart, huge gray band" defect.

**`_Assets/PenPlot/view.json`**

`props.defaultSize`: `{"height": 30, "width": 120}`. `params`: `row` (`""`), `rowData` (`""`), `value` (`""`) — the table view-cell contract confirmed from `_Assets/PenEnable`.

`root`: `ia.container.flex` containing a single `Dropdown` (`ia.input.dropdown`, class `adhoc-trend-pen-plot-select`). `props.options` is a script transform over `{session.custom.AdhocTrend}` returning `[{"value": p["id"], "label": p["title"]} for p in plots]`. `props.value` binds to `view.params.value`. `onActionPerformed` (dropdown value change) reads the alias from `self.view.params.rowData` and calls:

```
self.session.custom.AdhocTrend.penPlots = shared.AdhocTrend.move_pen(self.session.custom.AdhocTrend, alias, self.props.value)
```

Reassigning the whole `penPlots` dict (rather than mutating one key) is what makes the dependent plot bindings re-evaluate. Cross-kind moves are allowed — do not filter the option list by `plotKind`.

**Ticket logger** on both new views: root `meta.contextMenu: {}`, the `meta.contextMenu.enabled` / `meta.contextMenu.items` propConfig pair, and the `ticketLog` page-scope message handler calling `shared.Alerts.contextMenuTicketLog(payload['tagPath'], payload['viewName'])`. Copy the exact JSON shape from `_Assets/Pen/view.json` — it is already correct — but note that view's `Label` uses the legacy path-style class `Fonts/Value`; use `font-value` in the new views instead.

**`stylesheet.css`** — append a block near the existing `.psc-adhoc-trend-*` rules (they start around line 648). Required rules:
- `.psc-adhoc-trend-plots` — `display: flex; flex-direction: column; flex: 1 1 0; height: 100%; min-height: 0; gap: 6px;`
- Flex-repeater instance wrappers get an equal share: target `.psc-adhoc-trend-plots > *`, `.psc-adhoc-trend-plots .ia_embeddedView`, `.psc-adhoc-trend-plots .view-parent` with `flex: 1 1 0 !important; min-height: 0 !important; height: auto !important;`. The `min-height: 0` is mandatory — without it flex children refuse to shrink below content height and the last plot overflows.
- `.psc-adhoc-trend-plot-slot` — `display: flex; flex-direction: column; flex: 1 1 0; min-height: 0; height: 100%;` plus the existing thin top border.
- `.psc-adhoc-trend-plot-header` — `flex: 0 0 auto; min-height: 24px;`
- `.psc-adhoc-trend-plot-title` — `font-weight: 600;`
- `.psc-adhoc-trend-plot-toolbar` — `flex: 0 0 auto; min-height: 48px; height: 48px; overflow: visible; gap: 8px;`
- `.psc-adhoc-trend-add-plot-btn` — `min-width: 36px !important; width: 36px; padding-left: 4px !important; padding-right: 4px !important;`
- `.psc-adhoc-trend-pen-plot-select` — `min-width: 96px;`

Do not delete or rewrite the existing `.psc-adhoc-trend-faceplate*` / `.psc-adhoc-trend-apex` rules; the faceplate overrides at lines ~791-880 already force chart host sizing inside the popup and must keep working.

**`scripts/_verify_adhoc_views.py`** — a reusable structural gate, written now and extended in Task 3. It must: load every JSON file this plan touches under `98_Configuration/AdhocTrend/` and confirm it parses; walk every `"code"` / `"script"` / `"expression"` string and fail if it contains a carriage return; fail if any non-blank line of a `"code"` / `"script"` string does not begin with a tab; confirm each new view's root carries `meta.contextMenu`, both context-menu propConfig entries, and a `ticketLog` message handler; confirm `_Assets/Plot` declares all four params and that its `apexchart` has `position.grow == 1` and `position.basis == "0px"`; confirm the stylesheet defines every `psc-` class listed above. Exit non-zero on any failure.
  </action>
  <verify>
    <automated>python scripts/_verify_adhoc_views.py</automated>
    <automated>python scripts/repair-resource-signatures.py &amp;&amp; python scripts/repair-resource-signatures.py --check</automated>
  </verify>
  <done>`_Assets/Plot` renders its own per-plot history query and series and carries no fixed pixel chart height; `_Assets/PenPlot` offers every plot as a move target regardless of kind; both views carry the ticket logger; the stylesheet defines the equal-flex plot rules; `_verify_adhoc_views.py` and the signature check both exit 0.</done>
</task>

<task type="auto">
  <name>Task 3: Rebuild Trend layout — flex toolbar, + icon, N-plot repeater, pen routing</name>
  <files>
gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/Trend/view.json (modify)
scripts/_verify_adhoc_views.py (extend)
  </files>
  <action>
Rewire `Trend/view.json` with a Python editing script (`json.load` → mutate → `json.dump(indent=2)` with `newline="\n"`, re-scrubbing `\r` from all code strings before writing). Do not hand-edit the 375 KB file.

**1. Convert `/root/TrendContainer/Trend` from `ia.container.coord` to `ia.container.flex`** with `props.direction: "column"`, keeping `position: {"basis": "92%", "grow": 1}` and its `adhoc-trend-chart-host` class, and adding `props.style.minHeight: 0`. Its children become, in order:

- `TrendName` — `position: {"basis": "22px", "shrink": 0, "grow": 0}`, keep the existing `props.text` binding, add `props.style.textAlign: "center"`. Drop the old coord `x`/`width`/`height` keys.
- `PlotToolbar` — **new** `ia.container.flex` row, `position: {"basis": "48px", "shrink": 0, "grow": 0}`, `props.style.classes: "adhoc-trend-plot-toolbar"`, `props.style.overflow: "visible"`, `props.style.alignItems: "center"`. Move the existing `Icons` node into it with `position: {"grow": 1, "shrink": 1, "basis": "0px"}` and the existing `Buttons` node with `position: {"shrink": 0, "grow": 0, "basis": "auto"}`. On both, delete the coord-era `position.height` / `position.width` / `position.x` keys **and** the `propConfig["position.height"]` entries — leaving those behind reintroduces the percentage sizing that clips the toolbar. Clear `Icons` `props.style.paddingTop` (the 4px top pad plus a 48px row double-shifts the icons).
- `Plots` — **new** `ia.display.flex-repeater`, `position: {"grow": 1, "shrink": 1, "basis": "0px"}`, `props.path: "98_Configuration/AdhocTrend/_Assets/Plot"`, `props.direction: "column"`, `props.elementPosition: {"grow": 1, "shrink": 1, "basis": "0px"}`, `props.style.classes: "adhoc-trend-plots"`, `props.style.height: "100%"`, `props.style.minHeight: 0`, `props.style.overflow: "hidden"`. `props.instances` is a script transform over `{session.custom.AdhocTrend}` returning one entry per plot:

  `{"instancePosition": {"grow": 1, "shrink": 1, "basis": "0px"}, "instanceStyle": {"classes": ""}, "plotId": p["id"], "plotTitle": p["title"], "plotKind": p["kind"], "plotCount": len(plots)}`

  Setting `instancePosition` per instance as well as `elementPosition` on the repeater is deliberate: the repeater default wins in some Perspective versions and a single plot must still grow to fill the whole area.

**2. Delete the old chart plumbing from the Trend view** — remove the `/root/TrendContainer/Trend/apexchart` node, and remove `custom.key`, `custom.dataset`, `custom.realTimeDataset`, `custom.historicalDataset` from both `view.custom` and `view.propConfig`. Each Plot instance now runs its own history query; leaving these in place would duplicate every tag-history call on every poll. Keep `custom.pens`, `custom.tags`, `custom.colors`, `custom.aggregate`, `custom.realTime`, `custom.timeRange`, `custom.pointCount`, `custom.startDate`, `custom.endDate`, `custom.dbTrendConfig`, `custom.isConfigUpdated`, `custom.trendId`, `custom.trendName`, `custom.username`, `custom.treeVisible` — the toolbar labels, pen table and save/load flow all still read them.

**3. Add the `+` icon button as the FIRST child of `Buttons`**, i.e. immediately left of `SaveTrendConfig`. Name it `AddPlot`, type `ia.input.button`, `position: {"basis": "36px", "shrink": 0, "grow": 0}`, `props.text: ""`, `props.align: "center"`, `props.image.icon: {"path": "material/add", "color": "--neutral-10"}`, `props.style.classes: "container-button font-button adhoc-trend-action-btn adhoc-trend-add-plot-btn"`, symmetric 4px padding, `minHeight: 32`, `minWidth: 36`, `width: 36`. It must not be a text button and must not sit in a separate row — the earlier attempt failed both.

`onActionPerformed` script (tab-indented):

```
	self.session.custom.AdhocTrend.plots = shared.AdhocTrend.apply_add_plot(self.session.custom.AdhocTrend)
```

Assigning the returned plain list back onto the session property is the whole mechanism — mutating `plots` in place leaves the repeater's `instances` binding unevaluated and the click looks like a no-op.

**4. Route newly added tags by type.** In `/root/TagTree/AddToTrend` `onActionPerformed`, after the existing duplicate check and the 10-tag limit check append the tag, then route it and reassign both session collections:

```
	cfg = self.session.custom.AdhocTrend
	plotId, plots, penPlots = shared.AdhocTrend.route_new_tag(cfg, tagPath)
	cfg.plots = plots
	cfg.penPlots = penPlots
```

Floats land on an analog plot; booleans and integer status tags land on a discrete plot, created on demand. Preserve the existing `shared.Alerts.showAlert` duplicate/limit messages exactly as they are.

**5. Give the pen table a plot column.** In `/root/TrendContainer/Pens/Table` `props.columns`, insert a column between `penColor` and `penAction` with `field: "plotId"`, `render: "view"`, `viewPath: "98_Configuration/AdhocTrend/_Assets/PenPlot"`, `viewParams: {}`, `header.title: "Plot"`, `width: 120`. The `plotId` field is supplied by the `build_pens` headers from Task 1.

**6. Point the Trend view's `custom.pens` transform at the shared builder** so the legend and table pick up UDT-instance names: replace the transform body with a call to `shared.AdhocTrend.build_pens(value.tags, value.colors)`, keeping the existing expr-struct config over `{view.custom.tags}` + `{view.custom.colors}`. Also update the `/root/TrendContainer/Pens/Toggle/Pens` legend repeater transform to read `penName` from the new dataset (its column set gained `plotId`, so index-based access would shift — use name-based access).

**7. Persist the new state with saved configs.** Wherever the save/load path serializes the trend config (`custom.dbTrendConfig`, `commitTrendConfig`, and the `_Assets/SaveTrendConfig` flow), make sure `plots` and `penPlots` ride along with `tags`/`colors`. The `ClearPens` handler's `default_config` dict must also reset `"plots": shared.AdhocTrend.default_plots()` and `"penPlots": {}` so clearing returns to a single analog plot rather than leaving orphaned empty plots.

**8. Extend `scripts/_verify_adhoc_views.py`** with Trend-structure assertions: `/root/TrendContainer/Trend` is `ia.container.flex` with `direction == "column"`; no node named `apexchart` remains anywhere in the Trend tree; `PlotToolbar` exists with `position.basis == "48px"` and `shrink == 0`, and neither it nor `Icons`/`Buttons` retains a `propConfig["position.height"]`; `Buttons.children[0]` is named `AddPlot` with empty `props.text` and `props.image.icon.path == "material/add"`; `Plots` is `ia.display.flex-repeater` with the `_Assets/Plot` path and `elementPosition.grow == 1`; the pen table has a `plotId` column pointing at `_Assets/PenPlot`; `custom.key` / `custom.dataset` / `custom.realTimeDataset` / `custom.historicalDataset` are gone from `view.propConfig`. Keep the Task 2 checks (JSON parses, no carriage returns, tab-indented scripts, ticket logger present) running over the Trend view too.

**9. Repair signatures and rescan.** Run `python scripts/repair-resource-signatures.py`, then `--check`. The ignition-scan hook normally POSTs for you; if it did not fire, POST manually using `IGNITION_API_BASE` + `IGNITION_API_TOKEN` from `.env` (`X-Ignition-API-Token: Name:key`) to `/data/api/v1/scan/projects`, and confirm the gateway is healthy via `StatusPing`.
  </action>
  <verify>
    <automated>python scripts/_verify_adhoc_views.py</automated>
    <automated>python scripts/repair-resource-signatures.py &amp;&amp; python scripts/repair-resource-signatures.py --check</automated>
    <automated>powershell -NoProfile -Command "$r = Invoke-RestMethod -Uri 'http://localhost:19088/StatusPing' -TimeoutSec 20; if ($r.state -ne 'RUNNING') { throw \"gateway state $($r.state)\" }; 'gateway RUNNING'"</automated>
    <human-check>
Open http://localhost:19088/data/perspective/client/BH and navigate to the Adhoc Trend page, then confirm each of the four criteria the previous attempt failed:

1. **Toolbar** — the gear/Config icon, the tag-browser icon, the chart-type label, the time-range label and the start/end date labels are all fully visible, not vertically cut off. Re-check inside the faceplate popup (open Adhoc Trend from a device faceplate) where the container is shorter.
2. **Single plot fills the area** — with one plot, the chart occupies the full chart region. There is no small chart sitting above a large empty gray band.
3. **`+` button** — a `+` icon button sits immediately to the LEFT of Save Config in the same button row. Clicking it appends a new empty plot straight away, with no page reload. Click it twice: three plots share the height equally.
4. **Pen names** — add `[default]Evaporators/EV-01/Pressure/Value` from the tag tree. The legend, the pen table `penName` cell and the chart series all read `EV-01`, not `Value` and not `Pressure`.

Also confirm free pen movement: use the Plot dropdown in the pen table to move a pen from plot 1 to plot 2 and back, including moving an analog pen onto a discrete plot. Then add a boolean tag and confirm it lands on a discrete/status plot while floats stay on the analog plot.
    </human-check>
  </verify>
  <done>Trend is a flex column of TrendName / 48px PlotToolbar / grow-1 Plots repeater with no `apexchart` left behind; `AddPlot` is the first child of `Buttons` and appends a plot on click; new tags route by datatype; the pen table exposes a plot dropdown; `_verify_adhoc_views.py` and the signature check exit 0; the gateway reports RUNNING after the scan; all four human-check criteria pass.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| Perspective session → gateway scripting | Operator-driven session property writes (`plots`, `penPlots`) reach `shared.AdhocTrend` and drive tag-history queries |
| Tag path string → `system.tag.readBlocking` / tag-history binding | Operator-selected tag paths flow into tag reads and history queries |
| Saved trend config (MSSQL `adhoc_trend_configs`) → session | JSON decoded from the DB is applied to live session state |
| Repo file edits → Ignition gateway | On-disk project resources are loaded by the gateway via the scan API |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-vma-01 | Tampering | `session.custom.AdhocTrend.plots` / `penPlots` | medium | mitigate | `normalize_config` / `plain_plots` coerce every plot to `{id,title,kind}` strings and guarantee at least one plot; unknown `penPlots` targets fall back to the first plot id in `pens_for_plot` |
| T-vma-02 | Denial of Service | Per-plot tag-history bindings in `_Assets/Plot` | medium | mitigate | Each plot queries only the pens assigned to it, and Task 3 deletes the now-redundant Trend-level `realTimeDataset`/`historicalDataset` bindings so total query volume does not grow with plot count; the existing 10-tag cap in `AddToTrend` still bounds pen count |
| T-vma-03 | Information Disclosure | `_Assets/PenPlot` dropdown, `_Assets/Plot` header | low | accept | Both views only expose plot titles and tag names the operator already selected in the tag tree; no new data surface. Ticket-logger context menu stays gated by `session.custom.TicketLogAccess` |
| T-vma-04 | Tampering | Saved trend config JSON round trip | medium | mitigate | `plots`/`penPlots` are run through `plain_plots` / `plain_pen_plots` on load, so a malformed or stale saved config cannot inject non-string plot ids or delete the last plot |
| T-vma-05 | Tampering | Project resources on disk vs gateway CAS | high | mitigate | `python scripts/repair-resource-signatures.py` plus `--check` gate every task; a stale `lastModificationSignature` is exactly what produces the `ProtoSerializationException` / `NoSuchElementException` failure mode |
| T-vma-SC | Tampering | package installs | low | accept | No npm/pip/cargo installs — everything uses the existing Jython runtime, stdlib Python, and the Kyvis ApexCharts module already on the gateway |
</threat_model>

<verification>
1. `python scripts/_verify_adhoc_helpers.py` — helper contract including `EV-01` naming, type routing, add/remove/move plot.
2. `python scripts/_verify_adhoc_views.py` — structural gate over all AdhocTrend view JSON: parses, no carriage returns in code strings, tab-indented scripts, ticket logger on new views, Trend flex layout, `AddPlot` first in `Buttons`, `Plots` repeater wired to `_Assets/Plot`, `plotId` table column, dead dataset props removed.
3. `python scripts/repair-resource-signatures.py --check` exits 0.
4. Gateway `StatusPing` returns `RUNNING` after the projects scan.
5. Human check of the four UI criteria plus free cross-plot pen movement and type-based routing.
</verification>

<success_criteria>
- Operator can add an arbitrary number of plots via the `+` icon left of Save Config, and each click takes effect immediately.
- One plot fills the chart area; N plots split it equally with no dead gray space.
- Toolbar controls are fully visible in both full-page and faceplate mode.
- Pens are labeled by UDT instance (`EV-01`), not by member (`Pressure`) or leaf (`Value`).
- New float tags route to an analog plot; boolean/integer status tags route to a discrete plot, created on demand.
- Pens move freely between any two plots, including across kinds.
- `plots` and `penPlots` persist in session state and in saved trend configs.
- No magnitude/scale-based automatic splitting exists anywhere in the shipped code.
- Signature repair check passes and the gateway reloads cleanly.
</success_criteria>

<output>
Create `.planning/quick/260727-vma-rebuild-adhoc-trend-multi-plot-ux-n-empt/260727-vma-SUMMARY.md` when done.
</output>
