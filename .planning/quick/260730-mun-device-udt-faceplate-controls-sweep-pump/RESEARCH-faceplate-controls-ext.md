# RESEARCH — BH Faceplate Controls architecture (multi-device extension)

**Quick id:** `260730-mun`  
**Date:** 2026-07-30  
**Scope:** Unified Faceplate shell, `deviceType` → Controls path, Compressor Controls asset, legacy per-device faceplates, openers/nav, extension pattern, Pushover for screenshot proof  
**Out of scope:** Full UDT/CSV leaf inventory per device (parallel research); live Designer pixel polish

---

## Verdict

BH already has a **Scout-style shared Faceplate shell** with tabs that hide when empty. **Controls is the only tab that is device-specific today** — and only `Compressor` is wired. Configuration / Interlocks / Trend / Alarm Configuration / Alarms are **shared browse/filter assets**. Legacy Pump/Evaporator/etc. popups still open from nav and most device graphics; they do **not** use the unified shell.

**Recommended extension pattern:** keep shared tabs; add **per-device Controls views** under `_Assets/{Device}/Controls`, expand the shell `case(deviceType, …)` and `hasControlsAsset` list, and migrate openers to `Faceplate` + `deviceType`. Do **not** invent a single map-driven Controls mega-view for v1 — KPIs/commands diverge too much (Compressor Quantum vs lean Pump vs Sensor). Optionally extract shared Mode chips later if OPER/MAINT/PROG become common.

**Web GUI:** header button only; visible iff `deviceType = 'Compressor'` **and** non-empty `webGuiUrl`. Already removed from Controls body (matches mun CONTEXT).

---

## 1. Architecture map

```
Device graphic / Nav / shared.Alerts.showFaceplate
        │
        ▼
Navigation.Faceplate.openFaceplate(id, tagPath, view, …, params)
        │
        ├─ legacy: view = 01_Popups/00_Faceplates/{Pump|Evaporator|…}
        │            params = { tagPath } only  → simple Status/Temp popup
        │
        └─ unified: view = 01_Popups/00_Faceplates/Faceplate
                     params = { tagPath, deviceType, webGuiUrl, show* }
                            │
                            ▼
              Faceplate shell (header + tabs + EmbeddedView)
                            │
        ┌───────────────────┼───────────────────────────────┐
        │ Controls          │ shared tabs                     │
        │ case(deviceType)  │ Configuration / Interlocks /    │
        │ → _Assets/{Dev}/  │ Trend / AlarmConfiguration /    │
        │    Controls       │ Alarms                          │
        └───────────────────┴───────────────────────────────┘
```

**Only Compressor** currently takes the unified path from the device graphic. Nav `_Config` / docked Navigation still points instances at **legacy** faceplate viewPaths.

---

## 2. Faceplate shell (`01_Popups/00_Faceplates/Faceplate`)

### 2.1 Params (all input)

| Param | Default | Role |
|-------|---------|------|
| `tagPath` | `""` | Device UDT root |
| `deviceType` | `"Compressor"` | Selects Controls embed path; gates Web GUI |
| `webGuiUrl` | `""` | External vendor GUI (header only) |
| `showControls` … `showAlarms` / `showInterlocks` | `true` | Caller **hints** ANDed with `tagFlags` |
| `hiddenFromTrend` / `hiddenFromConfiguration` / `hiddenFromAlarmConfiguration` / `hiddenFromAlarms` | `""` | CSV/semicolon deny-lists for browse tabs |

### 2.2 Tab visibility (`custom.tagFlags`)

Script transform on expr-struct of params:

| Tab | Show rule |
|-----|-----------|
| **Controls** | `caller showControls` **AND** `deviceType in ('Compressor', '')` ← **extension choke point** |
| **Configuration** | caller AND browse finds writable non-alarm leaves (minus hidden) |
| **Interlocks** | caller AND Good quality on `…/Interlock/Sts_IntlkOK` or `Cfg_CondTxt00` or `Sts_Intlk` |
| **Trend** | caller AND historized analog leaf exists |
| **Alarm Configuration / Alarms** | caller AND any leaf with configured alarms |

`defaultTab` = first visible in order Controls → Configuration → Interlocks → Trend → Alarm Configuration → Alarms. `onChange` on `tagFlags` resets `selected` if current tab became hidden.

`visibleTabCount` drives CSS `faceplate-buttons-{N}`.

### 2.3 Controls path selection (critical)

Embedded body `props.path`:

```
case(selected,
  "Controls",
    case(deviceType,
      "Compressor", "…/_Assets/Compressor/Controls",
      "…/_Assets/Compressor/Controls"),   // fallback = Compressor
  "Configuration", "…/_Assets/Configuration/Configuration",
  "Interlocks",    "…/_Assets/Interlocks",
  "Trend",         "…/_Assets/Trend",
  "Alarm Configuration", "…/_Assets/AlarmConfiguration",
  "Alarms",        "…/_Assets/Alarms",
  fallback Controls → Compressor)
```

**Today:** non-Compressor `deviceType` still resolves Compressor Controls if the tab were shown — but `hasControlsAsset` **hides** Controls for any other type. Extension must update **both** the `case` arms **and** `hasControlsAsset`.

Embedded params forwarded: `tagPath`, `hiddenTags` (from selected tab’s hide list). **`webGuiUrl` is not passed into Controls** (header-owned).

### 2.4 Web GUI (header-only, compressor rule)

| Rule | Implementation |
|------|----------------|
| Location | Header button next to Close (`meta.name` = `WebGui`) |
| Visible when | `deviceType = 'Compressor' && len(coalesce(webGuiUrl,'')) > 0` |
| Action | `system.perspective.openURL(url)` |
| Controls body | **No** Web GUI section (removed post-m0m; mun locked) |

Non-compressor devices must never show this button even if a URL is passed.

### 2.5 Thin wrapper

`01_Popups/00_Faceplates/Compressor` embeds the Faceplate shell with hardcoded `deviceType: "Compressor"` and forwards `tagPath` / `webGuiUrl`. Pattern for other devices if nav must keep stable viewPath names: thin wrappers → Faceplate, or point nav directly at Faceplate with params (nav openFaceplate today only passes `tagPath` — see §5).

---

## 3. Compressor Controls (`_Assets/Compressor/Controls`)

**Params:** `tagPath` only.

**Section stack (top → bottom)** — matches CONTEXT Mode → Status → KPI:

| Section | Behavior |
|---------|----------|
| **Mode** | OPER / MAINT / PROG chips; visible if any mode tag quality Good; writes mutual-exclusive booleans; gated by `session.custom.ReadOnly` |
| **Status** | `StatusIndicator` → `{tagPath}/Status`; text codes CP/SV Remote/Auto/Manual; command buttons Cmd_Start/Stop/Auto/Manual/Remote (Auto/Manual/Remote also write `CP_Mode/Value` 2/3/1) |
| **KPI** | RuntimeHours, MotorStarts, MaxRunTimePerStart (numeric labels); AnalogValue embeds for FLA/SVP/DisP/Amps; Rung text Off/Running/AntiRec/Starting |

CSS: `faceplate-section`, `faceplate-section-card`, `faceplate-section-title`, `faceplate-mode-chip` / `faceplate-mode-active`, `faceplate-kpi-row`, plus shared `font-*` / `container-button`.

Ticket Logger context menu + `ticketLog` handler present.

This view is **hardcoded compressor leaf names** — not a browse. That is intentional (Scout has no Controls tab; BH invented this layout in `260730-m0m`).

---

## 4. Shared non-Controls assets (already multi-device)

| Asset | Pattern | Device-specific? |
|-------|---------|------------------|
| `_Assets/Configuration/Configuration` (+ Row) | Browse writables → AnalogInput / MultiStateInput | No — works for any UDT with writables |
| `_Assets/Interlocks` (+ InterlockRow) | 16-ch FT-style from `…/Interlock/*` | No — shows if Interlock folder present |
| `_Assets/Trend` | Historized analogs | No |
| `_Assets/AlarmConfiguration` (+ Row) | Alarm configs under tagPath | No |
| `_Assets/Alarms` | AlarmStatusTable filtered to source | No |

**Implication:** extending Controls is the main product work; Config/Interlocks/Trend/Alarms ride along once UDTs have the right members and openers pass `deviceType` + `show*`.

---

## 5. Openers and click handlers

### 5.1 `Navigation.Faceplate.openFaceplate`

`gateways/standard/data/projects/BH/ignition/script-python/Navigation/Faceplate/code.py`

- Merges `params` with `tagPath`; default geometry **560×640**
- Docstring lists unified fields: `deviceType`, `webGuiUrl`, `showControls`, …

### 5.2 `shared.Alerts.showFaceplate`

Preferred API for unified open:

```python
showFaceplate(tagPath, deviceType="Compressor", webGuiUrl="", … show* …)
→ view "01_Popups/00_Faceplates/Faceplate"
→ popup id "comp-fp-{tagPath|title}"
```

### 5.3 `Navigation.Nav.navigate`

If `action == "faceplate"` or `viewPath` starts with `01_Popups/00_Faceplates/`:

```python
Navigation.Faceplate.openFaceplate(popupId, tagPath, viewPath, …)
# NO deviceType / show* / webGuiUrl — only tagPath
```

Docked Navigation / TempNav tree items use **legacy** viewPaths (`…/Evaporator`, `…/Pump`, `…/Compressor`, …). Opening Compressor from nav therefore hits the thin Compressor wrapper (unified), but Pump/etc. hit legacy simple faceplates.

### 5.4 Device graphics (`02_Components/01_Devices/*`)

| Device | Click behavior |
|--------|----------------|
| **Compressor** | If `faceplate ∈ {Compressor, Faceplate}` → open **unified Faceplate** with `deviceType='Compressor'`, all `show*=True`, `webGuiUrl` (default lab `https://127.0.0.1/` if empty). Else fall through to path-based popup. |
| **Pump, Evaporator(+Dual/Triple), Tank, Sensor, ExhaustFan, CoolingTower, SolenoidValve(+3Way)** | Legacy: `openPopup` to `01_Popups/00_Faceplates/{faceplate\|\|self.view.name}` with **only** `{tagPath}`; size **420×520** |

Migration for sweep: copy Compressor’s branch pattern — call `shared.Alerts.showFaceplate(..., deviceType='Pump'|…)` or open Faceplate with the same params dict.

---

## 6. Legacy faceplates

Present under `01_Popups/00_Faceplates/`:

Pump, Evaporator, CoolingTower, Tank, SolenoidValve, SolenoidValve3Way, Sensor, ExhaustFan (+ Compressor wrapper, Faceplate shell, AdhocTrend*).

**Typical shape (Pump / Evaporator):** single-column card — title from Metadata, `StatusIndicator`, one AnalogValue (Temp/etc.), no tabs, no Mode/commands/KPI stack, no ticket-logger parity with shell depth. Default size ~400×480.

These remain the production open target for non-compressor devices until openers + Controls assets + `hasControlsAsset` are extended.

---

## 7. Devices UDT landscape (extension context)

UDT types in `tag-type-definition/default/Devices/udts.json`:

`Pump`, `Compressor`, `VFD`, `Evaporator`, `ExhaustFan`, `CoolingTower`, `Tank`, `Valve`, `Sensor`

| Type | Controls readiness (as of mun start) |
|------|--------------------------------------|
| **Compressor** | Expanded (Mode Cmd KPI Interlock Config writables) — Controls live |
| **Pump** | Lean: Status, Temp, SummaryInstances, _Alarms — needs UDT sweep before rich Controls |
| Others | Vary; mun CONTEXT requires comprehensive UDT + CSV/PLC correlation before Controls |

Valve faceplate naming note: Devices UDT is `Valve`; legacy HMI views use `SolenoidValve` / `SolenoidValve3Way`. Extension must pick a `deviceType` string and map openers consistently (recommend UDT type name: `Valve`, with graphic `faceplate` param or alias table).

---

## 8. Pattern recommendation

### 8.1 Options

| Option | Pros | Cons |
|--------|------|------|
| **A. Per-device `_Assets/{Device}/Controls`** (recommended) | Matches existing shell `case(deviceType)`; Designer-editable; Compressor already proves it; divergent KPI/command layouts stay clear | Some section duplication (Mode chips, Status row) |
| **B. One shared Controls + deviceType KPI/command maps** | DRY bindings | Heavy script transforms; hard to Designer-edit; Sensor vs Compressor layouts fight one template; high regression risk |
| **C. Hybrid shared sections + thin device KPI embeds** | Reuse Mode/Status chrome | Extra view indirection; only pays off after 3+ motor-like devices share OPER/CMD |

### 8.2 Recommendation (locked for planning)

**Prefer A — per-device Controls under `_Assets/{Device}/Controls`.**

Rationale:

1. Shell and `tagFlags.hasControlsAsset` are already designed around a **deviceType → path** switch.
2. Shared browse tabs already cover cross-device Config/Interlocks/Trend/Alarms — Controls is the intentional specialization point.
3. Scout does not provide a Controls tab; BH’s Mode→Status→KPI stack is product-specific and **hardcoded leaf lists per device** (Scout research). Maps in one mega-view recreate Designer pain without Scout precedent.
4. Pump/Sensor/Valve Controls will be **simpler and differently shaped** than Compressor — separate views avoid conditional spaghetti.

**Reuse across devices (without option B):**

- Same CSS classes (`faceplate-section*`, mode chips, KPI rows)
- Same child embeds (`StatusIndicator`, `AnalogValue`, command button script idiom with ReadOnly)
- Same open API: `showFaceplate(..., deviceType=…)`
- Optional later: extract `_Assets/ControlsSections/ModeChips` if ≥3 devices share OPER/MAINT/PROG

**Do not** put Web GUI in any Controls view; header + compressor rule only.

### 8.3 Extension checklist (per new device)

1. Expand Devices UDT (+ sim CSV / PLC correlation) with Mode/Cmd/KPI/Interlock as warranted.
2. Create `_Assets/{Device}/Controls/view.json` (+ resource.json); Mode→Status→KPI as data allows; hide empty sections via quality/visibility expressions (Compressor Mode pattern).
3. Faceplate `props.path` `case`: add `"Device", "…/_Assets/Device/Controls"`.
4. `hasControlsAsset`: add `'Device'` to the allowed set.
5. Device graphic click → unified Faceplate/`showFaceplate` with `deviceType`.
6. Nav: either thin wrapper `01_Popups/00_Faceplates/{Device}` → Faceplate, **or** teach `Navigation.Nav` / nav tag payloads to open Faceplate with `deviceType` (today nav only passes `tagPath`).
7. Repair signatures + scan/projects; screenshot Controls via Pushover (§9).

Suggested `deviceType` strings (match UDT / case arms):  
`Compressor`, `Pump`, `Evaporator`, `ExhaustFan`, `CoolingTower`, `Tank`, `Valve`, `Sensor`  
(SolenoidValve graphics → `deviceType='Valve'` or keep SolenoidValve as alias in both case + hasControlsAsset.)

---

## 9. Pushover (screenshot notifications)

For mun AFK proof: send Controls screenshots per device type.

### 9.1 Env

From `.env` (gitignored; templated in `.env.example`):

| Var | Role |
|-----|------|
| `PUSHOVER_TOKEN` | Application API token |
| `PUSHOVER_USER` | User/group key |

Never commit real values.

### 9.2 Scripts

| Script | Attachment? | Use |
|--------|-------------|-----|
| `scripts/pushover_nav_screenshots.py` | **Yes** (multipart PNG) | Best template for faceplate Controls screenshots — `load_env()` from repo `.env`, `pushover_with_image(title, message, image: Path)` → `POST https://api.pushover.net/1/messages.json` |
| `scripts/monday_agent_job.py` → `pushover()` | Text only (urlencode) | Monday agent START/FINISH/ERROR / non-Dylan ticket alerts |

### 9.3 Suggested mun usage

1. Capture PNGs (Playwright / Designer / client) of Faceplate **Controls** tab per device into e.g. `docs/handoff/fp-controls-{device}.png`.
2. Reuse or fork `pushover_nav_screenshots.py`: swap the `shots` list for Controls paths; keep `load_env` + `pushover_with_image`.
3. Run: `python scripts/pushover_nav_screenshots.py` (or the fork) with `.env` populated.

---

## 10. Related artifacts

| Path | Why |
|------|-----|
| `.planning/quick/260730-mun-…/CONTEXT.md` | Locked mun decisions (Web GUI header-only; UDT sweep; Pushover proof) |
| `.planning/quick/260730-m0m-…/RESEARCH-bh-current.md` | Pre-m0m baseline (partially superseded — Interlocks/tagFlags/Controls commands now exist) |
| `.planning/quick/260730-m0m-…/RESEARCH-scout-controls.md` | Scout has **no** Controls tab; KPI = hardcoded / title |
| `.planning/quick/260730-m0m-…/260730-m0m-SUMMARY.md` | What Compressor Faceplate already shipped |
| `shared/Alerts/code.py` | `showFaceplate` |
| `Navigation/Faceplate/code.py` | `openFaceplate` |
| `Navigation/Nav/code.py` | Nav tree → popup (tagPath only) |

---

## 11. Open risks for execute

1. **Nav params gap** — opening Faceplate from nav without `deviceType` defaults to Compressor; migrating nav to unified shell requires payload/schema change or thin wrappers per device.
2. **hasControlsAsset whitelist** — forgetting to extend it leaves Controls tab hidden even after building the asset.
3. **Pump/Valve UDT thinness** — Controls UI without new tags will be Status-only; UDT sweep is a hard dependency.
4. **Naming** — `Valve` vs `SolenoidValve` vs `SolenoidValve3Way` must be decided once for `deviceType` + case arms.
5. **Popup geometry** — unified 560×640 vs legacy 420×520; prefer unified when migrating.
6. **Web GUI URLs** — Compressor opener still defaults empty URL to `https://127.0.0.1/` (lab). Real plant URLs need page embeds / Metadata / `_Config` map later; out of mun “non-compressor Web GUI” scope.
