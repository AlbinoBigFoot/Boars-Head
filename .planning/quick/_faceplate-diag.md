# Faceplate diagnosis — Controls / Config / Alarms / Trend / tabs

**Date:** 2026-07-30  
**Scope:** Diagnosis only (no fixes). Shared shell: `01_Popups/00_Faceplates/Faceplate`.

---

## Verdict

| Symptom | Root cause | Path strings wrong? |
|--------|------------|---------------------|
| Controls / Configuration → **View Not Found** | Views exist and EmbeddedView paths are **correct**, but **CAS digests missing** from `projects/.resources/` (signature check fails). Gateway cannot load those two resources. | **No** — paths match disk |
| Alarms → `ia.display.alarm-status-table not found` | **Wrong component type** (hyphenated invent). Working BH + Scout use `ia.display.alarmstatustable`. | N/A (view path OK) |
| Trend “broken” / stub | Intentional stub: label list + button → `Alerts.showAdhocTrend()`. Not Scout `_Assets/Main` in-popup chart. | Path to stub is correct |
| Tab white-on-light | Tab buttons set `textStyle.classes: font-button` → `--text-inverse` (near-white) on light `--surface-container` / `--surface-card` tabs. | N/A |

---

## 1. EmbeddedView path strings (Faceplate)

**File:** `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json`  
**Binding:** `root/Body/EmbeddedView` → `propConfig.props.path` (expression)

| Tab (`custom.selected`) | Expression path (current) | Disk view exists? | Correct Perspective path? |
|-------------------------|---------------------------|-------------------|---------------------------|
| Controls | `01_Popups/00_Faceplates/Compressor/Controls` (via `deviceType` case; default same) | Yes | **Yes** |
| Configuration | `01_Popups/00_Faceplates/Compressor/Configuration` | Yes | **Yes** |
| Trend | `01_Popups/00_Faceplates/_Assets/Trend` | Yes | **Yes** (but content is AdhocTrend stub) |
| Alarm Configuration | `01_Popups/00_Faceplates/_Assets/AlarmConfiguration` | Yes | **Yes** (stub content) |
| Alarms | `01_Popups/00_Faceplates/_Assets/Alarms` | Yes | **Yes** (broken component inside) |
| default | `01_Popups/00_Faceplates/Compressor/Controls` | Yes | Yes |

**Wrong vs correct:** There are **no wrong path strings** in the current Faceplate expression for Controls/Configuration. Planner CONTEXT assumed “paths wrong despite views on disk” — that was a **misdiagnosis**. Runtime “View Not Found” is explained by unloadable resources (below).

### Open / navigation (not the bug)

- `shared.Alerts.showFaceplate` → `Navigation.Faceplate.openFaceplate(..., "01_Popups/00_Faceplates/Faceplate", params)` — shell path correct.
- Device Compressor click: same shell + `deviceType: 'Compressor'` — correct.
- Do **not** confuse with Scout layout (different tree; see §5).

---

## 2. Controls / Configuration — why View Not Found

`python scripts/repair-resource-signatures.py --check` (2026-07-30):

```
ISSUE .../Compressor/Configuration/resource.json: cas:view.json=7d969c1579afe498…
ISSUE .../Compressor/Controls/resource.json: cas:view.json=8e9986f21ddad663…
check: 2 issue(s) of 138 resource(s)
```

| View | `view.json` sha256 prefix | Present in `projects/.resources/`? |
|------|---------------------------|-------------------------------------|
| Compressor/Controls | `8e9986f21ddad663…` | **False** |
| Compressor/Configuration | `7d969c1579afe498…` | **False** |
| _Assets/Trend, Alarms, AlarmConfiguration, Faceplate | (various) | True |

**Mechanism:** Ignition 8.3 loads project file bytes via content-addressed `.resources/<sha256>`. Agent-created Controls/Configuration `view.json` files + `resource.json` signatures were written, but digests were never written into CAS (or signatures not repaired/scanned). Result: optional empty → resource fails to open → EmbeddedView shows **View Not Found** even though the path string is valid.

**Fix direction (for planner, not done here):**
1. `python scripts/repair-resource-signatures.py` (writes CAS + signatures)
2. `--check` exit 0
3. POST scan/projects

`resource.json` files themselves look structurally fine (`files: ["view.json"]`, non-zero signatures) — problem is CAS parity, not missing folders.

---

## 3. Alarms — component fix needed

**File:** `_Assets/Alarms/view.json`

| | Type string |
|--|-------------|
| **BH Faceplate Alarms (broken)** | `ia.display.alarm-status-table` |
| **Correct (BH Alarms page + Scout Faceplate Alarms)** | `ia.display.alarmstatustable` |

Scout reference:  
`ScoutMotors/.../01_Popups/00_Faceplates/Alarm/Alarms/view.json` → `ia.display.alarmstatustable`  
BH working:  
`00_Pages/Alarms/_Assets/AlarmStatusTable/view.json` → same.

**Fix:** Rename type to `ia.display.alarmstatustable`. Keep source filter expression if desired (prov:/tag: pattern from `tagPath`); validate against Scout AlarmStatusTable props schema after rename.

---

## 4. Tab contrast CSS

**Faceplate tabs** apply:
- `props.style.classes` → `faceplate-button` / `faceplate-button-selected` (backgrounds: `--surface-container` / `--surface-card` — light neutrals)
- `props.textStyle.classes` → **`font-button`**

**stylesheet.css:**

```css
.psc-font-button {
  color: var(--text-inverse);  /* ≈ --neutral-10 = near white */
  ...
}
.psc-faceplate-button {
  background: var(--surface-container);
  color: var(--text);          /* correct dark text — but textStyle wins on label */
  ...
}
```

`--text-inverse` is for dark/accent chrome (`container-button` on headers). On light tab chrome it yields **white-on-light**.

**Fix direction:** Drop `font-button` from tab `textStyle`, or add faceplate-specific text class using `--text` / `--text-secondary`; optionally set explicit `color` on `.psc-faceplate-button` / `-selected` with higher specificity on the text node. Scout faceplate tabs do **not** use an inverse font class on tab labels.

---

## 5. Scout Faceplate / Trend auto-pen pattern

**Scout shell paths** (`ScoutMotors/.../Faceplate/view.json`):

| Tab | Scout path |
|-----|------------|
| Trend | `01_Popups/00_Faceplates/_Assets/Main` |
| Configuration | `01_Popups/00_Faceplates/Configuration/Configuration` |
| Alarm Configuration | `01_Popups/00_Faceplates/Alarm Configuration/AlarmConfiguration` |
| Alarms | `01_Popups/00_Faceplates/Alarm/Alarms` |

Scout has **no Controls tab** and **no `deviceType` path map**. Tab visibility comes from tagFlags script + `hiddenFrom*` params. EmbeddedView also binds `params.hiddenTags` from the matching `hiddenFrom*` when that tab is selected.

### Trend auto-pens (Scout) — files + how pens chosen

**Primary view:**  
`.../01_Popups/00_Faceplates/_Assets/Main/view.json`

**UI:** `ia.input.dropdown` + `kyvislabs.display.apexchart` (`AnalogChart`).

**Mechanism (not a UDT param pen list, not a deviceType map):**

1. **Input:** `params.tagPath`, `params.hiddenTags` (comma/semicolon list to exclude).
2. **Script transform on `custom.sensors`:**
   - `system.tag.browse(tagPath, recursive=True)`
   - Skip Folder / UdtType / UdtInstance / Property; skip `*.` meta leaves
   - Apply `hiddenTags` filter
   - `readBlocking` `.Enabled`, `.HistoryEnabled`, `.DataType` per candidate
   - Keep tags that are enabled + history-enabled + **not** string/date/bool
   - Alias: parent folder name if leaf is `Value`, else leaf name
   - Output `result['analog']` = `[{path, alias, aggregate: 'Average'}, ...]`
3. **`custom.chartDataAnalog`:** `system.tag.queryTagHistory` on those paths (default last 2 hours, Average, Wide).
4. ApexChart binds to that history dataset.

**Pen source summary:** **runtime tag browse under device `tagPath`**, filtered by history/enabled/datatype + optional hide list — **not** a static deviceType→pens map and **not** a UDT “pens” parameter (though Faceplate openers can pass `hiddenFromTrend` to prune).

### BH Trend today (contrast)

`_Assets/Trend/view.json`: hardcoded FLA/SVP/DisP/Amps summary + button that mutates `session.custom.AdhocTrend.tags` and calls `Alerts.showAdhocTrend()`. Locked CONTEXT: replace with Scout-style in-popup auto-pens (Compressor default list or browse/map — TBD with Dylan).

---

## 6. Alarm Configuration / Trend content notes (secondary)

- `_Assets/AlarmConfiguration`: stub list of `AlarmEvalEnabled` tags under device — path OK; content incomplete vs Scout `Alarm Configuration/AlarmConfiguration`.
- `_Assets/Trend`: path OK; wrong product behavior vs locked decision (no AdhocTrend).

---

## Planner checklist (suggested order)

1. Repair CAS/signatures for Controls + Configuration → re-scan → confirm Controls/Config tabs resolve.
2. Fix Alarms type → `ia.display.alarmstatustable`.
3. Fix tab text contrast (`font-button` / `--text-inverse`).
4. Replace Trend stub with Scout-like `_Assets` chart + auto-pen (browse and/or deviceType default map).
5. Optionally deepen Alarm Configuration later.

---

## Key absolute paths

- Shell: `C:\Users\dylan.jones\Documents\Bors\gateways\standard\data\projects\BH\com.inductiveautomation.perspective\views\01_Popups\00_Faceplates\Faceplate\view.json`
- Controls: `...\Compressor\Controls\`
- Configuration: `...\Compressor\Configuration\`
- Trend / Alarms / AlarmConfiguration: `...\ _Assets\{Trend,Alarms,AlarmConfiguration}\`
- CSS: `...\BH\com.inductiveautomation.perspective\stylesheet\stylesheet.css` (`.psc-font-button`, `.psc-faceplate-button*`)
- Scout Main: `C:\Program Files\Inductive Automation\Perspective-8-3-Scout\data\projects\ScoutMotors\com.inductiveautomation.perspective\views\01_Popups\00_Faceplates\_Assets\Main\view.json`
- Open API: `...\BH\ignition\script-python\Navigation\Faceplate\code.py`, `...\shared\Alerts\code.py` (`showFaceplate`)
