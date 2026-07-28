# BH HMI theme tokens (Figma extract)

Extracted for Agent 1 theme work on `feature/themes`. **Do not treat this as a gateway CSS edit** — implementers map these into Perspective themes / Advanced Stylesheet separately.

**Scope:** themes drive **everything that isn’t alarm coloring** — device components, faceplates, adhoc trends, Ticket Logger, nav, headers, page/view backgrounds, cards, buttons, icons. **Only `--alarm-*` / alarm-priority UI stays fixed** across modes.

| Figma Theme (component property) | BH / Ignition theme | Cold ↔ Cool |
|---|---|---|
| `Light` | `light` / `light-cool` | cool |
| `Dark` | `dark` / `dark-cool` | cool |
| `Light Warm` | `light-warm` | warm |
| `Dark Warm` | `dark-warm` | warm |

---

## Sources

### Primary — Dev Jam (BH customs)

| Item | Value |
|---|---|
| File | [Dev](https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w) (`Q8EmmXokQsiX91aPMtLm2w`) |
| Pages | **Only one page:** `Dev Jam` (`25:2`) |
| Theme matrix | Component property `Theme` = Light \| Dark \| Light Warm \| Dark Warm |

### Secondary — library search

| Library | Key (abbrev) | Notes |
|---|---|---|
| **Components & Elements Rev 1.29.0** | `lk-65b6bf55…` | Org library. Alarm vars, Base Views / Faceplates **fill styles** (names only via MCP — no multi-mode hex matrix in Dev Jam). Catalog mirrored on Dev Jam as frame `86:873`. |
| Material 3 / SDS / Apple kits | community | Not BH HMI sources. |

No separate Figma page/frame for “theme matrix” chrome (masthead × 4 modes, faceplate × 4, trend × 4, Ticket Logger × 4) exists in this file. Device Theme variants **are** the authoritative BH component token source.

---

## Node index (Dev Jam `25:2`)

| Frame / set | Node ID | Theme variants |
|---|---|---|
| Evaporator | `28:1055` | fans × Theme (16 symbols) |
| Evaporator `Theme=Light` (fans=1) | `28:873` | light-cool |
| Evaporator `Theme=Dark` (fans=1) | `147:1953` | dark-cool |
| Evaporator `Theme=Light Warm` (fans=1) | `147:1975` | light-warm |
| Evaporator `Theme=Dark Warm` (fans=1) | `147:1997` | dark-warm |
| Pump | `145:2033` | Light `46:935`, Dark `145:1997`, Light Warm `145:2009`, Dark Warm `145:2021` |
| Exhaust Fan | `145:2088` | Light `63:873`, Dark `145:2034`, Light Warm `145:2052`, Dark Warm `145:2070` |
| Fan | `145:2128` | Light `50:873`, Dark `145:2089`, Light Warm `145:2102`, Dark Warm `145:2115` |
| Cooling Tower — Cutaway | `145:2403` | Light `96:1953`, Dark `145:2220`, Light Warm `145:2281`, Dark Warm `145:2342` |
| Sensor | `145:2443` | Light `135:1953`, Dark `145:2404`, Light Warm `145:2417`, Dark Warm `145:2430` |
| NH3 Compressor — A | `148:2020` | Light `148:1953`, Dark `148:1954`, Light Warm `148:1976`, Dark Warm `148:1998` |
| Nav Tree Icons | `141:1953` | Ink note: `#161616` (light); themed via `--icon-nav` |
| Hoffman Library — Dev Jam | `86:873` | Single (light) catalog instance |
| Labels / Values / Alarms items | `89:1546` | Alarm + chrome samples (light defaults) |
| alarm-border-priority | `89:1581` | `--color-alarm-critical` |
| alarm-border | `89:1586` | `--color-alarm-critical` |
| alarmButton | `89:1647` | alarm + button neutrals |

---

## Token tables by mode

Hex values below are from Figma **`get_variable_defs`** on Evaporator / Pump Theme symbols unless noted. Same Theme property yields the same semantic vars across devices (Pump matches Evaporator).

### light-cool (`Theme=Light`) — nodes `28:873`, `46:935`

| Role | Figma token | Hex | Maps to BH semantic |
|---|---|---|---|
| Text primary | `--text` / `--neutral-100` | `#161616` | `--text` |
| Text secondary / muted | `--text-muted` / `--neutral-60` | `#767676` | `--text-muted`, `--icon-muted` |
| Device / housing fill | `--neutral-30` | `#D8D8D8` | `--surface-component`, device body |
| Blade / mid fill | `--neutral-60` | `#767676` | mid gray fills |
| Raised / card surface | `--surface-raised` | `#FFFFFF` | `--surface-raised`, `--surface-card` |
| Accent (analog value, CTA cool) | `--accent` | `#114599` | `--accent` / cool CTA (align `--qual-8`) |
| Status RUN fill | `--sts-run` | `#228B22` | status chrome (see notes) |
| Status RUN stroke | `--sts-run-stroke` | `#005000` | status chrome |

Hoffman light catalog extras (`86:873` / `89:1546`): `--neutral-10` `#FAFAFA`, `--neutral-20` `#F4F4F4`, `--neutral-40` `#BDBDBD`, `--neutral-50` `#A1A1A1`, `--neutral-70` `#5E5E5E`, `qual-8` `#114599`, `naviIcon` `#767676`, `deviceFill-stopped` `#767676`, `deviceFill-faulted` `#161616`.

### dark-cool (`Theme=Dark`) — nodes `147:1953`, `145:1997`

| Role | Figma token | Hex | Maps to BH semantic |
|---|---|---|---|
| Text primary | `--text` / `--neutral-100` | `#FAFAFA` | `--text` |
| Text muted | `--text-muted` / `--neutral-60` | `#A1A1A1` | `--text-muted` |
| Device / housing fill | `--neutral-30` | `#515151` | `--surface-component` |
| Raised / card surface | `--surface-raised` | `#323232` | `--surface-raised`, `--surface-card` |
| Accent | `--accent` | `#53BAED` | `--accent` (cool dark) |
| Status RUN fill | `--sts-run` | `#3CB371` | status chrome (lighter for dark bg) |
| Status RUN stroke | `--sts-run-stroke` | `#1B5E20` | status chrome |

### light-warm (`Theme=Light Warm`) — nodes `147:1975`, `145:2009`

| Role | Figma token | Hex | Maps to BH semantic |
|---|---|---|---|
| Text primary | `--text` / `--neutral-100` | `#171414` | `--text` |
| Text muted | `--text-muted` / `--neutral-60` | `#736F6F` | `--text-muted` |
| Device / housing fill | `--neutral-30` | `#CAC5C4` | `--surface-component` |
| Raised / card surface | `--surface-raised` | `#FFFFFF` | `--surface-raised` |
| Accent | `--accent` | `#C45C26` | `--accent` / `--accent-warm` |
| Status RUN fill | `--sts-run` | `#228B22` | same as light-cool |
| Status RUN stroke | `--sts-run-stroke` | `#005000` | same as light-cool |

### dark-warm (`Theme=Dark Warm`) — nodes `147:1997`, `145:2021`

| Role | Figma token | Hex | Maps to BH semantic |
|---|---|---|---|
| Text primary | `--text` / `--neutral-100` | `#F7F3F2` | `--text` |
| Text muted | `--text-muted` / `--neutral-60` | `#8F8B8B` | `--text-muted` |
| Device / housing fill | `--neutral-30` | `#3C3838` | `--surface-component` |
| Raised / card surface | `--surface-raised` | `#272525` | `--surface-raised` |
| Accent | `--accent` | `#E8894F` | `--accent` (warm dark — brighter than light-warm CTA) |
| Status RUN fill | `--sts-run` | `#3CB371` | same as dark-cool |
| Status RUN stroke | `--sts-run-stroke` | `#1B5E20` | same as dark-cool |

---

## Cross-mode matrix (implementer cheat sheet)

| Token / surface | light-cool | dark-cool | light-warm | dark-warm |
|---|---|---|---|---|
| **Page / view bg** (recommended) | cool-10 `#F2F4F8` | cool-100 `#121619` | warm-10 `#F7F3F2` | warm-100 `#171414` |
| **Header / masthead** | cool-30 `#C1C7CD` | cool-80 `#343A3F` | warm-30 `#CAC5C4` | warm-80 `#3C3838` |
| **Card / popup / faceplate shell** | `#FFFFFF` / cool-20 | `#323232` / cool-90 | `#FFFFFF` / warm-20 | `#272525` / warm-90 |
| **Nav bg** | cool-20 `#DDE1E6` | cool-90 `#21272A` | warm-20 `#E5E0DF` | warm-90 `#272525` |
| **Text primary** | `#161616` | `#FAFAFA` | `#171414` | `#F7F3F2` |
| **Text secondary / muted** | `#767676` | `#A1A1A1` | `#736F6F` | `#8F8B8B` |
| **Border** | `#D8D8D8` / cool-30 | `#515151` / cool-80 | `#CAC5C4` | `#3C3838` |
| **Button fill (default chrome)** | `#D8D8D8` | `#515151` | `#CAC5C4` | `#3C3838` |
| **Button / icon ink** | `#161616` | `#FAFAFA` | `#171414` | `#F7F3F2` |
| **Accent / analog / CTA** | `#114599` | `#53BAED` | `#C45C26` | `#E8894F` |
| **Icons (nav muted)** | `#4D5358` (`--icon-nav` on `141:1953`) | invert via `--icon` / `--icon-nav` | warm mid | warm mid |
| **Device body fill** | `#D8D8D8` | `#515151` | `#CAC5C4` | `#3C3838` |
| **Device stroke** | `#161616` | `#FAFAFA` | `#171414` | `#F7F3F2` |

### Full cool / warm neutral ramps (page chrome)

These match BH Advanced Stylesheet anchors / Lightspeed gateway themes (not every step appears on device Theme symbols, but they drive nav, page, cards):

**Cool**

| Step | Hex |
|---|---|
| 10 | `#F2F4F8` |
| 20 | `#DDE1E6` |
| 30 | `#C1C7CD` |
| 40 | `#A2A9B0` |
| 50 | `#878D96` |
| 60 | `#697077` |
| 70 | `#4D5358` |
| 80 | `#343A3F` |
| 90 | `#21272A` |
| 100 | `#121619` |

**Warm**

| Step | Hex |
|---|---|
| 10 | `#F7F3F2` |
| 20 | `#E5E0DF` |
| 30 | `#CAC5C4` |
| 40 | `#ADA8A8` |
| 50 | `#8F8B8B` |
| 60 | `#736F6F` |
| 70 | `#565151` |
| 80 | `#3C3838` |
| 90 | `#272525` |
| 100 | `#171414` |

Light themes: `--neutral-N` = cool/warm-N. Dark themes: invert (`--neutral-10` = cool/warm-100, …).

---

## Themeable vs fixed (ISA-101)

### Themeable (must follow mode)

- Page / view backgrounds (`--surface-page`)
- Nav, headers, footers, cards, containers
- Faceplate shells, popup cards, Ticket Logger chrome, adhoc trend panels/toolbars
- Device component fills, strokes, labels, analog **accent** values
- Buttons, icons, borders, text primary/secondary
- Status **RUN** chrome **as Figma Theme variants show** (`#228B22` light / `#3CB371` dark) — readability on dark surfaces, still green attention

### Fixed — do **not** change with theme

Alarm priority palette (library vars + BH stylesheet). Figma MCP resolved critical hex; other priorities named in **Components & Elements Rev 1.29.0** `globals` — use BH locked values:

| Token | Hex | Figma name |
|---|---|---|
| `--alarm-critical` | `#E22028` | `--color-alarm-critical` (confirmed on `89:1581`, `89:1586`, `89:1647`) |
| `--alarm-high` | `#EC8629` | `--color-alarm-high` |
| `--alarm-medium` | `#F5E11B` | `--color-alarm-medium` |
| `--alarm-low` | `#916AAD` | `--color-alarm-low` |
| `--alarm-notification` | *(library var present; keep product default)* | `--color-alarm-notification` |
| Ack variants | `#8B1519` / `#9A5619` / `#9E9012` / `#5A3F6C` | BH stylesheet only |

Also keep fixed (attention / not ambient chrome):

| Token | Hex | Notes |
|---|---|---|
| `--sts-fault` | `#C62828` | Fault attention (StatusIndicator / STS chip) |
| `--sts-defrost` | `#EF6C00` | Defrost notice (STS chip; StatusIndicator uses Figma pink) |
| `deviceFill-faulted` | `#161616` | Hoffman / labels (`89:1546`) — fault encoding, not theme wash |
| `Breaker - Closed` / `breakerClosed` | `#F94449` | Electrical alarm-like cue in Hoffman catalog |

Alarm borders, alarm icons, alarm button glow (`89:1581`–`89:1647`) stay on `--color-alarm-*` regardless of Theme.

---

## Faceplates, trends, Ticket Logger (gaps + guidance)

| Surface | In Figma Dev Jam Theme matrix? | Implementer guidance |
|---|---|---|
| Device faceplates (`01_Popups/00_Faceplates/…`) | **No** 4-mode frame. Library has fill styles: `Faceplates/Faceplate Card - Fill`, tab Neutral 40/50, text Neutral 90 | Theme via `--surface-card` / `--surface-raised`, `--text`, `--border`, `--accent`. Tabs: selected `--neutral-40`, unselected `--neutral-50` (light baseline from style names). |
| Adhoc trends / pens / toolbars | **Not present** as themed screens | Use `--surface-page`, `--surface-card`, `--surface-header`, `--text`, `--text-muted`, `--border`, `--accent` for chart chrome, buttons, labels. Pen series colors can stay qualitative (`--qual-*`) if already data-encoding. |
| Ticket Logger / issue logger popups | **Not present** | Same shared popup card tokens as trend faceplates (`--surface-card`, header `--surface-header`, close hover `--neutral-40`). |
| Masthead / nav / footer | Library **style names** only: `Base Views/Masthead - Fill Color - Nuetral 30`, `Navi Bar- Fill Color`, `Navigation Background Default- Fill Color - Nuetral 30`, `Footer - Fill`, masthead border / subheader text | Map Neutral 30 → header/nav fills; Neutral 100 → primary text; Neutral 80 → secondary masthead text. Apply cool/warm + light/dark inversion from ramps above. |
| Labels / values / alarm chrome | `89:1546` (light defaults) | Values → `--accent` / `qual-8`; EU → `--text-muted`; labels → `--text`; setpoint box → `--neutral-10` fill + `--neutral-100` border. |

**Library styles found (no per-mode hex via MCP):**

- `Faceplates/Faceplate Card - Fill`
- `Faceplates/Faceplate - Tab - Selected - Fill Color - Neutral 40`
- `Faceplates/Faceplate - Tab - Unselected - Fill Color - Neutral 50`
- `Faceplates/Faceplate - Text Color - Fill Color - Neutral 90`
- `Base Views/Masthead - Fill Color - Nuetral 30`
- `Base Views/Masthead - Border`
- `Base Views/Masthead - Sub-header 1 text - Fill - Neutral 80`
- `Base Views/Masthead - Sub-header 2 text - Fill - Neutral 100`
- `Base Views/Navi Bar- Fill Color`
- `Base Views/Navigation Background Default- Fill Color - Nuetral 30`
- `Base Views/Footer - Fill`

---

## Accent / CTA notes

| Mode | Figma device `--accent` | Notes vs gateway drafts |
|---|---|---|
| light-cool | `#114599` | Matches Hoffman `qual-8`. Cooler/deeper than some Lightspeed `--callToAction` `#0C7BB3`. Prefer Figma for **device analog** + BH cool accent alignment. |
| dark-cool | `#53BAED` | Matches dark `--qual-2` / Lightspeed primary-40. |
| light-warm | `#C45C26` | Matches stylesheet `--accent-warm`. |
| dark-warm | `#E8894F` | Brighter warm accent on dark; gateway draft using `#C45C26` for dark-warm should likely lift toward `#E8894F` for parity with Figma. |

---

## Recommended semantic mapping (shared tokens)

Use one set of CSS variables for **all** non-alarm UI (devices + faceplates + trends + Ticket Logger + nav):

| Semantic | Source |
|---|---|
| `--surface-page` | neutral-10 (theme ramp) |
| `--surface-header` / `--surface-container` | neutral-30 |
| `--surface-nav` | neutral-20 |
| `--surface-card` / `--surface-raised` | Figma `--surface-raised` or neutral-20 |
| `--surface-component` (device body) | Figma `--neutral-30` |
| `--text` | Figma `--text` |
| `--text-muted` | Figma `--text-muted` |
| `--border` | neutral-30 |
| `--accent` | Figma `--accent` per mode |
| `--icon` / `--icon-nav` | neutral-90 / neutral-70 (invert in dark) |
| `--alarm-*` | **fixed** table above |

---

## Extraction method

1. `get_metadata` on `25:2` (page inventory)
2. `get_variable_defs` on Theme symbols (Evaporator + Pump × 4)
3. `get_design_context` + `skillNames: resource:figma-design-to-code` on `28:1055`, `89:1546`
4. `search_design_system` / `get_libraries` against Components & Elements Rev 1.29.0
5. Cross-check BH `stylesheet.css` semantic aliases and alarm locks

---

## Open items for later agents

1. Resolve hex for `--color-alarm-high|medium|low|notification` and `fireAlarmZone` directly from the library file (MCP search returns names; only critical hex confirmed on Dev Jam instances).
2. If designers add a chrome Theme matrix (masthead / faceplate / trend), re-extract and replace the “recommended” page-chrome cells with measured fills.
3. Align gateway `--callToAction` per mode with Figma `--accent` (especially dark-warm `#E8894F` and light-cool `#114599` vs `#0C7BB3`).
4. Do **not** edit gateway theme CSS in this agent pass.
