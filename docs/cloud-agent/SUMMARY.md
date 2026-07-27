# Cloud agent summary — Boars Head (BH) Ignition HMI

**Read this file first** when working in this repo as a Cursor Cloud Agent (or any remote agent without local chat history).

| Item | Value |
|------|--------|
| Repo | Boars Head / `Bors` — Ignition Perspective HMI for Boar’s Head refrigeration lab |
| Primary project | `BH` under `gateways/standard/data/projects/BH/` |
| Gateway | Docker `bh-ignition-standard`, Ignition **8.3.x**, HTTP **19088** |
| Perspective client | `http://127.0.0.1:19088/data/perspective/client/BH/` (prefer `127.0.0.1` over `localhost` on Windows) |
| Scan credentials | [`ignition-scan.json`](./ignition-scan.json) in this folder (committed for cloud agents) |

---

## 1. Mandatory: resource signatures + reload from disk

Ignition 8.3 is **file-based**. Editing files under `gateways/*/data/projects/` or `gateways/*/data/config/` does **nothing** until you scan.

### 1a. Resource signatures (projects only — do this FIRST)

Disk edits that change resource content (`view.json`, `code.py`, `stylesheet.css`, …) **must** refresh `attributes.lastModificationSignature` and copy content digests into `projects/.resources/`. Skipping this causes Designer/gateway `ProtoSerializationException` / `ImmutableResourceSerializer` / `No value present`.

```powershell
python scripts/repair-resource-signatures.py
python scripts/repair-resource-signatures.py --check   # must exit 0
```

Details: [`docs/ignition-resource-signatures.md`](../ignition-resource-signatures.md). Cursor rule: `.cursor/rules/ignition-resource-signatures.mdc`.

### 1b. Scan API

### Credentials (committed)

File: `docs/cloud-agent/ignition-scan.json`

```json
{
  "apiToken": "Access:<plaintextKey>",
  "scanProjectsUrl": "http://localhost:19088/data/api/v1/scan/projects",
  "scanConfigUrl": "http://localhost:19088/data/api/v1/scan/config"
}
```

Header: `X-Ignition-API-Token: Access:<key>`  
Format is always **`Name:plaintextKey`** (example name: `Access`).

### PowerShell examples

```powershell
$cfg = Get-Content docs/cloud-agent/ignition-scan.json | ConvertFrom-Json
$h = @{ "X-Ignition-API-Token" = $cfg.apiToken }

# After Perspective views / stylesheet / project scripts:
Invoke-RestMethod -Method POST -Uri $cfg.scanProjectsUrl -Headers $h

# After gateway themes, tags-as-resources, OPC device CSV, gateway config:
Invoke-RestMethod -Method POST -Uri $cfg.scanConfigUrl -Headers $h
```

Local Cursor also has a hook that POSTs these automatically; **cloud agents must call scan themselves**.

If scan returns 401/403: the API key needs **Gateway Write Permissions** (Platform → Security → General Settings) and must exist under Platform → Security → API Keys.

Also usable: repo-root `.env` keys `IGNITION_API_TOKEN` / `IGNITION_API_BASE` (gitignored) — prefer the committed `docs/cloud-agent/ignition-scan.json` when `.env` is absent in the cloud VM.

---

## 2. Repo layout (what to edit)

| Area | Path |
|------|------|
| Perspective views | `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/` |
| Advanced Stylesheet (CSS only) | `…/stylesheet/stylesheet.css` |
| Session props | `…/session-props/props.json` |
| Page routes / docks | `…/page-config/config.json` |
| Session must-login | `…/session-permissions/` (requires security level **Authenticated**) |
| Project scripts | `…/ignition/script-python/shared/` (`HBT` → **`shared`**, never recreate `HBT`) |
| Gateway themes | `gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/` |
| Icon library (nav) | `…/perspective/icons/equipment/` (`equipment.svg`, etc.) |
| Tags (partially tracked) | `…/tag-definition/`, `…/tag-type-definition/` — see `.gitignore` exceptions |
| Plant sim CSV | `sim/bh-plant-sim.csv` (generator: `sim/build_plant_sim.py`) |
| Theme docs | `docs/themes.md`, `docs/ignition-theme-architecture.md`, `docs/theme-figma-tokens.md` |
| Funnel docs | `docs/tailscale-funnel.md` |

**Do not invent Designer Style Classes.** All look-and-feel goes in Advanced Stylesheet; views set `props.style.classes` to simple class names (`bg-page`, `container-card`, `font-label`, `fan-spin`, …).

**Faceplates** live only under:

`views/01_Popups/00_Faceplates/`

Never create `01_Faceplates/`.

---

## 3. Perspective JSON conventions

1. **`propConfig` keys need a scope prefix:** `props.text`, `props.style.backgroundColor`, `params.tagPath`, `custom.*`, `position.*`. Bare `text` fails deserialization.
2. **Script transforms / event scripts:** body lines tab-indented (`\t`), Designer style. No flush-left Python in `"code"` / `"script"`.
3. **Newlines in JSON strings:** use `\n` only — **never** `\r\n` in expression/code/script strings (see `.cursor/rules` / `perspective-reference`).
4. Prefer real Designer/Scout shapes from  
   `C:\Program Files\Inductive Automation\Perspective-8-3-Scout\data`  
   when available; gateway is 8.3 (same major as Scout).

---

## 4. Themes (critical)

### How themes work

1. Operator picks theme → writes `session.props.theme` (`light` | `dark` | `light-warm` | `dark-warm`).
2. Gateway serves that folder’s theme CSS **first**.
3. Advanced Stylesheet loads **after** and must **consume** `var(--neutral-*)` / semantic aliases — **never redefine `--neutral-*` in stylesheet.css** (that stomps every theme).
4. There is **no** reliable `data-theme` DOM attribute for stylesheet scoping. Theme swap = swap CSS file.

UI: top-right **settings gear** → ChangeTheme (not inside login popup).  
Animations: `session.props.animations` gates `fan-spin`, `ct-fan-side-spin`, `ct-spray-run`, `alarm-flash`, etc.

### What themes vs what stays fixed

- **Themeable:** surfaces, text, borders, nav, cards, device chrome fills, page backgrounds, faceplates, trends, Ticket Logger chrome, accents.
- **Fixed:** **`--alarm-*` only** (alarm priority colors).

Deep docs: `docs/themes.md`, `docs/ignition-theme-architecture.md`, Figma tokens `docs/theme-figma-tokens.md`.  
Figma: https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w (Dev Jam — Theme = Light / Dark / Light Warm / Dark Warm).

### Cooling tower water color (do this correctly)

**Wrong (do not ship):**

- Binding `fill.paint` to `{session.props.theme}` with a script that returns `'#7FD1F5' if theme.startswith('dark') else 'var(--accent)'`.
- Fragile `props.elements[N]` indices + hardcoded hex in transforms.
- Expecting Advanced Stylesheet alone to “detect” dark mode without theme variables.

**Right:**

1. Add `--ct-water` (or `--device-water`) to **every** theme `variables.css` (`light`, `dark`, `light-warm`, `dark-warm`, and cool aliases).
2. Use a **water blue** in dark **and** warm themes (do **not** use `var(--accent)` for water — warm accents are orange).
3. In `CoolingTower/view.json`, set basin-water / spray fills to static `"paint": "var(--ct-water)"`.
4. `POST` **scan/config** (and scan/projects if the view changed).
5. Verify computed `--ct-water` in the client for all four themes.

If theme CSS appears not to apply, **debug the theme pipeline** (scan permissions, which CSS URL loads, computed vars) — do **not** fall back to session.theme paint bindings.

---

## 5. Tags, Overview rebuild, sim

- Evaporators: `[default]Evaporators/EV-01`…`EV-16` (single-fan).
- Cooling towers: `[default]CoolingTowers/CT-01`…`CT-03` — Status + Temp OPC to `[Sim]CoolingTowers/...`.
- Overview Instances: `shared.Overview` — only direct children with `typeId` under `Devices/*` (not nested VFDs). Rebuild via `[default]_Config/Rebuild` → `rebuildAllOverviews()`.
- Sim: edit `sim/build_plant_sim.py`, run it, import `sim/bh-plant-sim.csv` into Programmable Device Simulator (often mirrored at gateway `opcua/device/Sim/instructions.csv`).

---

## 6. Navigation & Devices page

Tree:

```text
Plant → / (NoViewPath)
 └─ Area → /
     └─ System → /
         └─ Devices → /devices
             ├─ Evaporators → /evaporators → faceplates
             ├─ Cooling Towers / Compressors / Pumps / Exhaust Fans → …
Operations → alarms / trending
```

`/devices` shell: embedded view path toggles **Details** | **Design** (default Details → `00_Pages/Devices/DetailsOverview`). Design is a P&ID stub. Pattern: one Embedded View + path binding (Scout NoViewPath style), not stacked visible panes.

Nav icons: `equipment/*` from the committed equipment icon library (not missing `material/air`).

---

## 7. Auth & public access

- Perspective **requires Authenticated** (`session-permissions`). Anonymous users see login first.
- Optional Tailscale Funnel docs: `docs/tailscale-funnel.md`. Prefer a non-admin demo user for external viewers.

---

## 8. Git / ignore pitfalls

- Root `.env` and `.ignition-scan.json` are **gitignored**. Cloud agents should use **`docs/cloud-agent/ignition-scan.json`**.
- Most of `gateways/**/data/**` is ignored; **exceptions** track projects, Perspective themes, icons, and some tag paths — see `.gitignore`.
- Icon library: must keep `!…/perspective/icons/**` exceptions or `equipment.svg` will not ship.
- Do not commit: `*.gwbk`, `wiki/node_modules`, secrets outside `docs/cloud-agent/ignition-scan.json` unless the owner explicitly requests.

---

## 9. Success checklist for any change

1. Match BH conventions (CSS-only, `shared.*`, faceplate paths, tab-indented scripts, LF-only).
2. Edit the right tree (project vs config).
3. If project resources changed: **`python scripts/repair-resource-signatures.py`** then `--check` (exit 0).
4. **Scan** projects and/or config with the token above.
5. Hard-refresh Perspective client (`127.0.0.1:19088`).
6. For theme/visual work: verify all four themes; keep `--alarm-*` unchanged.
7. Commit only when asked; don’t force-push `main`.

---

## 10. Quick path index for agents

```text
docs/cloud-agent/SUMMARY.md          ← you are here
docs/cloud-agent/ignition-scan.json  ← API token for scans
docs/ignition-resource-signatures.md ← signature + CAS repair (mandatory)
scripts/repair-resource-signatures.py
docs/themes.md
docs/ignition-theme-architecture.md
docs/theme-figma-tokens.md
docs/tailscale-funnel.md
docs/evaporator-hmi-components.md
sim/build_plant_sim.py
sim/bh-plant-sim.csv
gateways/standard/data/projects/BH/
gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/
```

**Tell the cloud agent:** *Read `docs/cloud-agent/SUMMARY.md` and `docs/cloud-agent/ignition-scan.json` before editing or scanning. After project edits, run `scripts/repair-resource-signatures.py` then scan.*
