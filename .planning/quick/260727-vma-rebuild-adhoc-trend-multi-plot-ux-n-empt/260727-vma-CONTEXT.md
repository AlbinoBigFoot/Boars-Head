# Quick Task 260727-vma: Rebuild Adhoc Trend multi-plot UX - Context

**Gathered:** 2026-07-27
**Status:** Ready for planning
**Branch:** `feature/adhoc-trend-nplots` (from origin/main)

<domain>
## Task Boundary

Rebuild Adhoc Trend multi-plot UX from scratch on clean main. User can add N empty plots; free pen moves; type-based default routing (not magnitude); UDT-instance pen names; `+` icon left of Save Config; single plot full-height; multi plots equal flex; toolbar not clipped.

Ignore unrelated WIP (wiki, comm-loss, navigation).

</domain>

<decisions>
## Implementation Decisions

### Plots / routing
- User can add **as many plots as they want**.
- **Add Plot** creates an **empty** plot; user moves pens themselves.
- Free pen moves between any plots (including cross-type).
- Default routing when adding tags: **floats → analog plot**; **booleans + integer multistate/status → discrete/status plot** (create status plot if needed). **NO** magnitude/range-based auto-split (reject prior ticket `050f184` scale-split UX as product behavior).
- Persist `plots` + per-pen plot assignment in session + saved trend config.

### Pen naming
- Pen label = **UDT/instance holding the tag**, not leaf `value`.
- Example: `[default]Evaporators/EV-01/Pressure/Value` → **`EV-01`** (not `Value`, not `Pressure`).
- Path pattern: `.../<UDTInstance>/<Member>/Value` → use `<UDTInstance>`.
- Prefer metadata only if it clearly is the UDT instance name; otherwise derive from path.

### UI (CRITICAL — prior attempt failed these)
1. **Add Plot:** NOT a text button in main toolbar. Use **`+` icon button** (`material/add` or equivalent) to the **LEFT of Save Config** with other action buttons.
2. **Plot height:** One plot fills chart area like original single chart. Only with **2+ plots** share space proportionally (equal flex grow). No tiny plot + huge empty gray region.
3. **Add Plot must work** — click `+` appends plot and updates Flex Repeater / session state (reassign plain list so bindings refresh).
4. **Toolbar cutoff:** Gear/Config, Realtime, and time range labels must be fully visible (restore prior toolbar spacing/heights; faceplateMode vs full page).

### Architecture preferences
- BH: CSS-only Advanced Stylesheet; `shared.*` not HBT; faceplates under `01_Popups/00_Faceplates/`; tab-indented Perspective scripts; ticket logger on new views.
- Prefer FlexRepeater of `_Assets/Plot` (Kyvis ApexCharts) over hardcoded dual apexchart.
- Extract helpers to `shared/AdhocTrend` (reuse `resolve_column` / series patterns from prior ticket; rewrite UX).
- After project edits: `python scripts/repair-resource-signatures.py` then `--check`, then POST Ignition projects scan from `.env`.
- Prefer readable shared Python + careful view.json edits; existing `scripts/_fix_adhoc_*.py` may be used carefully but rewrite cleanly if brittle.
- GSD executor SHOULD commit atomically per skill; leave tree testable.

### Claude's Discretion
- Plot id scheme (`p0`, `p1`, …), plot title defaults, status vs analog `kind` naming.
- Exact CSS class names for multi-plot flex host.
- Whether pen move UI is dropdown on pen row vs plot chrome — must support free cross-plot moves.
- How to detect boolean vs float vs integer multistate for routing (tag datatype / Value.DataType).

</decisions>

<specifics>
## Specific Ideas

- Current main: single Kyvis ApexCharts in `98_Configuration/AdhocTrend/Trend/view.json` (~375KB); no `plots`/`penPlots` in session.
- Prior ticket commit: auto dual-plot by scale — **do not ship as product UX**.
- Failed WIP mistakes: text "Add Plot", FlexRepeater without equal flex/`min-height:0`, Add Plot no-op (no plain-list reassignment), toolbar clipping, parent-of-leaf naming (`Pressure`) instead of UDT instance (`EV-01`).
- Fix script sketch: `scripts/_fix_adhoc_nplots_ui.py` shows intended `apply_add_plot` + plain_plots reassignment + + icon reorder.

</specifics>

<canonical_refs>
## Canonical References

- `.cursor/rules/perspective-*.mdc`, `ignition-resource-signatures.mdc`, `hbt-to-shared.mdc`
- Scout/BH Perspective patterns under `gateways/standard/data/projects/BH/`
- `docs/ignition-resource-signatures.md` / scan via `.env` `IGNITION_API_*`

</canonical_refs>
