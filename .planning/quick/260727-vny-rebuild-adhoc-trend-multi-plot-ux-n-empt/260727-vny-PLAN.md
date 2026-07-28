---
phase: 260727-vny-rebuild-adhoc-trend-multi-plot-ux-n-empt
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py
  - gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/resource.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/resource.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/Trend/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Pen/view.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css
autonomous: true
requirements:
  - D-01
  - D-02
  - D-03
  - D-04
  - D-05
  - D-06
user_setup: []

must_haves:
  truths:
    - User can add unlimited empty plots via + immediately left of Save Config; plots refresh from session state
    - New pens default-route floats to analog and booleans/integer multistate-status to discrete/status (creating that plot if needed); free cross-type pen moves work; no magnitude engUnit auto-split
    - plots and per-pen plot assignment persist in session.custom.AdhocTrend and saved trend_config JSON
    - Pen labels show UDT instance name (e.g. EV-01) not leaf Value/Pressure
    - One plot fills full chart area; 2+ plots share equal flex height; Gear/Config, Realtime, and time range remain fully visible
  artifacts:
    - gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py
    - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json
    - session.custom.AdhocTrend.plots and penPlots keys in session-props/props.json
  key_links:
    - AddPlot onActionPerformed → shared.AdhocTrend.apply_add_plot → session.custom.AdhocTrend.plots reassignment → Plots FlexRepeater instances
    - custom.pens transform → shared.AdhocTrend.pen_label → UDT instance display
    - Save/Load path serializes full session.custom.AdhocTrend including plots and penPlots
---

<objective>
Rebuild Adhoc Trend multi-plot UX on clean main: N empty plots via toolbar +, free pen moves, UDT-instance pen labels, proportional flex layout, and persistence in session/saved config (D-01..D-06).

Purpose: Replace single-chart Adhoc Trend with operator-controlled N-plot layout without magnitude auto-split.
Output: `shared.AdhocTrend` package, Plot asset view, restructured Trend view + CSS, session defaults for plots/penPlots.
</objective>

<execution_context>
@$HOME/.cursor/gsd-core/workflows/execute-plan.md
@$HOME/.cursor/gsd-core/templates/summary.md
</execution_context>

<context>
@.planning/quick/260727-vny-rebuild-adhoc-trend-multi-plot-ux-n-empt/260727-vny-CONTEXT.md
@.cursor/rules/perspective-reference.mdc
@.cursor/rules/perspective-css-only.mdc
@.cursor/rules/perspective-ticket-logger.mdc
@.cursor/rules/hbt-to-shared.mdc
@.cursor/rules/ignition-resource-signatures.mdc
@.cursor/rules/ignition-8-3-scan-api.mdc

# Baseline (read before editing)
@gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/Trend/view.json
@gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json
@gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Pen/view.json
@gateways/standard/data/projects/BH/ignition/script-python/shared/Utilities/resource.json

# Reference only (patterns — do NOT copy magnitude split UX)
@scripts/_fix_adhoc_nplots_ui.py
</context>

<tasks>

<task type="auto">
  <name>Task 1: shared.AdhocTrend + session plots/penPlots</name>
  <files>gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py, gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/resource.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json</files>
  <action>
Create package `shared.AdhocTrend` (mirror `shared/Utilities/resource.json` shape with `code.py`; never use HBT — D-06).

Implement in `code.py` (Perspective-safe, plain Python; helpers that tolerate dict-like and session custom objects):

1. **Config shape (D-03):** `plots` = list of `{id, title, kind}` where kind is `analog` or `discrete`; `penPlots` = map tagPath→plotId (dict preferred; list of pairs acceptable if normalize converts both ways). `default_plots()` returns one analog plot (discretion: match original single-chart feel). `normalize_config(cfg)` ensures plots/penPlots exist and returns cfg.

2. **Add empty plot (D-01):** `apply_add_plot(cfg, title=None, kind="analog")` appends an empty plot with a new unique id, writes back via attribute-friendly setters, returns a **plain** `list[dict]` of plots suitable for `session.custom.AdhocTrend.plots = ...` reassignment so bindings refresh. Reference patterns in `scripts/_fix_adhoc_nplots_ui.py` (`_cfg_get`/`_cfg_set`, `plain_plots`, `apply_add_plot`) — adapt, do not blind-copy.

3. **Default routing + free moves (D-02):** `route_new_pen(cfg, tagPath, dataType)` — floats → analog plot (create if missing); booleans and integer multistate/status → discrete/status plot (create if needed). **Do not** implement magnitude/engUnit auto-split. `move_pen(cfg, tagPath, targetPlotId)` allows any pen to any existing plot (cross-type OK). `remove_plot` may refuse if pens still assigned or last plot — discretion, keep UX clear.

4. **Pen label (D-04):** `pen_label(tagPath)` returns UDT instance name holding the tag. Example: `[default]Evaporators/EV-01/Pressure/Value` → `EV-01`. Strip provider bracket; walk path segments and return the UDT instance segment (not leaf member names like Value/Pressure). Fallback: last meaningful non-leaf segment.

5. **Series helpers:** Expose `resolve_column` / `build_series` style helpers only as needed for per-plot Apex options — reuse prior ticket patterns for column matching if useful; never reuse magnitude-split as UX.

6. **Session defaults (D-03):** In `session-props/props.json` under `custom.AdhocTrend`, add `plots` (one default analog) and `penPlots` (`{}`). Do not change SQL schema — opaque `trend_config` already saves the session blob wholesale.

Scripts/strings: `\n` only inside JSON script fields; no `\r\n`.
  </action>
  <verify>
    <automated>python -c "from pathlib import Path; p=Path('gateways/standard/data/projects/BH/ignition/script-python/shared/AdhocTrend/code.py'); t=p.read_text(encoding='utf-8'); assert 'def apply_add_plot' in t and 'def pen_label' in t and 'def route_new_pen' in t and 'def move_pen' in t and 'def normalize_config' in t; assert 'HBT' not in t; s=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/session-props/props.json').read_text(encoding='utf-8'); assert '\"plots\"' in s and 'penPlots' in s; print('ok')"</automated>
  </verify>
  <done>shared.AdhocTrend exists with normalize/add/route/move/pen_label; session.custom.AdhocTrend has plots + penPlots; no HBT; no magnitude split.</done>
</task>

<task type="auto">
  <name>Task 2: Plot asset + Trend multi-plot UI + UDT pens</name>
  <files>gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/resource.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/Trend/view.json, gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Pen/view.json</files>
  <action>
Match Designer-exported shapes from Scout/BH patterns; propConfig keys must use scope prefixes (`props.*`, `params.*`, `custom.*`); tab-indent all Perspective script bodies; `\n` only in JSON strings (D-06).

1. **Create Plot asset (discretion path):** `98_Configuration/AdhocTrend/_Assets/Plot` with `view.json` + `resource.json`. Root is a flex column (`adhoc-trend-plot-slot`) holding optional title/header and one `kyvislabs.display.apexchart` that charts only pens assigned to `params.plotId`. Wire chart options/series via script transforms calling `shared.AdhocTrend` helpers. Include Ticket Logger on root: `meta.contextMenu`, items/enabled propConfig, and `ticketLog` message handler → `shared.Alerts.contextMenuTicketLog` (per perspective-ticket-logger — D-06).

2. **Restructure Trend chart area (D-01, D-05):** In `Trend/view.json`, replace the single page-level `apexchart` chart host with a Flex container named `Plots` (class `adhoc-trend-plots`) using a Flex Repeater (or equivalent) whose instances bind to `session.custom.AdhocTrend.plots`, each embedding `98_Configuration/AdhocTrend/_Assets/Plot` with `plotId` (and any needed history/pens params). Position: grow/shrink so one instance fills the chart area; repeater `elementPosition` grow=1 shrink=1 basis=0.

3. **Add Plot button (D-01):** Inside toolbar `Buttons` children, insert Icon Button `AddPlot` **immediately before** `SaveTrendConfig` (left of Save). Use material `add` icon (empty text), classes including `adhoc-trend-action-btn` / `adhoc-trend-add-plot-btn`. `onActionPerformed` script (Gateway scope): reassign `self.session.custom.AdhocTrend.plots = shared.AdhocTrend.apply_add_plot(self.session.custom.AdhocTrend)` so the Plots repeater refreshes. Do not place + elsewhere.

4. **Pen add routing + free moves (D-02):** Where tags are added to the trend, call `shared.AdhocTrend.route_new_pen` (or equivalent) instead of any magnitude/engUnit split. On Pen chip/asset (`_Assets/Pen`), add minimal move UI (dropdown or context menu listing current plots) calling `shared.AdhocTrend.move_pen` then reassign `penPlots`/`plots` so bindings refresh — cross-type allowed.

5. **UDT pen labels (D-04):** Change `propConfig.custom.pens` script transform in Trend (and Pen display if it uses `penName`) to set `penName` via `shared.AdhocTrend.pen_label(tagPath)` (or inline equivalent calling that helper). Stop preferring Metadata long/shortDescription / leaf Name as the primary label.

6. **Toolbar cutoff (D-05):** Ensure Icons/Buttons flex styles keep Gear/Config, Realtime, and time range fully visible (overflow visible; avoid clipping). Compare main toolbar before multi-plot; widen or reflow as needed without abandoning coordinate layout of the Trend chrome.
  </action>
  <verify>
    <automated>python -c "import json; from pathlib import Path; t=json.loads(Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/Trend/view.json').read_text(encoding='utf-8'));
def find(n,name):
  if isinstance(n,dict):
    if n.get('meta',{}).get('name')==name: return n
    for c in n.get('children') or []:
      r=find(c,name)
      if r: return r
  return None
btns=find(t['root'],'Buttons'); names=[c.get('meta',{}).get('name') for c in (btns or {}).get('children') or []]; assert 'AddPlot' in names and names.index('AddPlot') < names.index('SaveTrendConfig'), names; add=find(t['root'],'AddPlot'); assert 'apply_add_plot' in json.dumps(add); assert find(t['root'],'Plots') is not None; pens=json.dumps(t.get('propConfig',{}).get('custom.pens',{})); assert 'pen_label' in pens or 'AdhocTrend.pen_label' in pens; p=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/98_Configuration/AdhocTrend/_Assets/Plot/view.json'); assert p.exists(); pj=p.read_text(encoding='utf-8'); assert 'ticketLog' in pj and 'shared.Alerts.contextMenuTicketLog' in pj; assert 'HBT' not in pens and 'HBT' not in pj; print('ok')"</automated>
  </verify>
  <done>AddPlot sits left of Save and calls apply_add_plot; Plots repeater drives Plot assets; pens use UDT labels; routing/moves wired without magnitude split; Plot view has ticket logger.</done>
</task>

<task type="auto">
  <name>Task 3: Proportional CSS + signatures + scan</name>
  <files>gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css</files>
  <action>
CSS-only styling in Advanced Stylesheet only — no Designer Style Class folders (D-05, D-06).

1. Add/update rules (use `adhoc-trend-*` class names; Ignition adds `psc-` prefix):
   - `.psc-adhoc-trend-plots`: column flex, `flex: 1 1 0`, `height: 100%`, `min-height: 0`, small gap.
   - Equal-share children: `.psc-adhoc-trend-plots > *` (and embedded view wrappers if needed) `flex: 1 1 0 !important`, `min-height: 0`, so **1 plot = full area** and **2+ = equal proportional height** — no tiny plot + huge empty gray.
   - `.psc-adhoc-trend-plot-slot` / apex host: fill slot height (`flex` column, `min-height: 0`).
   - `.psc-adhoc-trend-add-plot-btn`: compact 36px width so + fits left of Save.
   - Toolbar rules: ensure toolbar row / Icons area `overflow: visible` and adequate height so Gear/Config, Realtime, time range are not cut off (D-05). Prefer existing `adhoc-trend-toolbar-*` classes; extend rather than invent path-style Fonts/Colors classes.

2. Reference WIP CSS block in `scripts/_fix_adhoc_nplots_ui.py` `patch_css` as a starting point; adapt to current stylesheet section (~adhoc-trend rules).

3. After all project file edits this plan: run `python scripts/repair-resource-signatures.py` then `python scripts/repair-resource-signatures.py --check` (exit 0). POST Ignition projects scan per repo `.env` / `.ignition-scan.json` / docs cloud-agent scan config (D-06). Do not invent signatures by hand.
  </action>
  <verify>
    <automated>python -c "from pathlib import Path; c=Path('gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css').read_text(encoding='utf-8'); assert '.psc-adhoc-trend-plots' in c and 'adhoc-trend-add-plot-btn' in c; assert 'flex: 1 1 0' in c or 'flex:1 1 0' in c; print('css-ok')"; python scripts/repair-resource-signatures.py; python scripts/repair-resource-signatures.py --check</automated>
  </verify>
  <done>Proportional plot CSS present; signatures repaired and --check clean; projects scanned.</done>
</task>

</tasks>

<threat_model>
## Trust Boundaries

| Boundary | Description |
|----------|-------------|
| Operator session → historian / tag paths | Tag paths and plot config come from authenticated Perspective session and tag browser |
| Session blob → MSSQL trend_config | Saved configs store opaque JSON including plots/penPlots |

## STRIDE Threat Register

| Threat ID | Category | Component | Severity | Disposition | Mitigation Plan |
|-----------|----------|-----------|----------|-------------|-----------------|
| T-260727-01 | Tampering | shared.AdhocTrend.move_pen / route_new_pen | medium | mitigate | Validate plotId exists in cfg.plots before assignment; ignore unknown ids |
| T-260727-02 | Information Disclosure | pen_label / tagPath in session | low | accept | Tag paths already visible to authorized HMI users; no new external exposure |
| T-260727-03 | Elevation of Privilege | SaveTrendConfig persistence | low | accept | Existing auth/roles unchanged; opaque JSON write path unchanged |
| T-260727-SC | Tampering | npm/pip installs | low | accept | No new package-manager dependencies in this plan |
</threat_model>

<verification>
- Automated asserts in each task pass.
- Manual smoke (executor notes): open Adhoc Trend → one full-height plot → click + → second equal-height empty plot → add float and bool pens → correct default plots → move pen cross-plot → save/reload config retains plots/penPlots → pen chips show UDT instance → toolbar controls fully visible.
</verification>

<success_criteria>
All locked decisions D-01..D-06 implemented: N empty plots via + left of Save, free moves + type-based default routing without magnitude split, session/config persistence, UDT instance pen labels, proportional flex layout, CSS-only + shared.* + ticket logger + signature repair/scan.
</success_criteria>

<output>
Create `.planning/quick/260727-vny-rebuild-adhoc-trend-multi-plot-ux-n-empt/260727-vny-SUMMARY.md` when execution completes.
</output>
