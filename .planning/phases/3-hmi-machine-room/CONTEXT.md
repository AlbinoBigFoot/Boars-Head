# Phase 3: Machine Room HMI — Context

**Gathered:** 2026-07-29
**Status:** Figma refined (colored piping) — awaiting Dylan approval before Ignition import
**Roadmap home:** Phase 3 — HMI standards & screen migration (pilot screen)

<domain>
## Phase Boundary

Design (Figma first) then later implement a BH Perspective **Machine Room** overview page under `00_Pages/Machine Room` (or similar), using existing BH device components. Spatial layout follows the FactoryTalk MACHINE ROOM screenshot; visual language is **BH modern** (themes + CSS-only) — not a 1:1 FactoryTalk clone.

**This slice stops at Figma** until Dylan approves. Do **not** create/edit Ignition views, page-config, tags, or stylesheet for Machine Room until that gate opens.

**In-scope equipment (locked):** tanks, valves, pumps, compressors, and process pipe runs only.

</domain>

<figma_deliverable>
## Figma deliverable

| | |
|--|--|
| **File** | Dev Jam `Q8EmmXokQsiX91aPMtLm2w` |
| **Page** | Machine Room — `248:1953` |
| **Frame** | Machine Room — P&ID — `248:1954` |
| **URL** | https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w/Dev-Jam?node-id=248-1954 |
| **Piping** | Colored (FactoryTalk-adapted): cyan HSS/HTRL · dark blue LSS/LTRL · orange HPL/HTRS |
| **FT reference** | Page image `244:2270` (“image 1”) above the P&ID frame — spatial routing reference only |
| **Gate** | Awaiting Dylan approval before Ignition import |

</figma_deliverable>

<decisions>
## Implementation Decisions

### Workflow / gates
- **D-01:** Figma first; Ignition Perspective only after Dylan approves the Figma design.
- **D-02:** Figma target = **new page inside existing Dev Jam file** `fileKey` `Q8EmmXokQsiX91aPMtLm2w` — **not** a new Figma file. **Done:** page `248:1953`, frame `248:1954`.

### Page / layout
- **D-03:** Root = **coordinate container**.
- **D-04:** Intended Ignition path (post-approval): `00_Pages/Machine Room` (or similar naming under `00_Pages/`).
- **D-05:** Spatial layout (FactoryTalk reference on Machine Room page):
  - **Top:** HTR, HPR, LTR tanks with level gauges
  - **Middle:** HTRL pumps (2), LTRL pumps (2) + solenoid/isolation valves
  - **Bottom:** COMP #7, #6, #5, #4, #1
  - **Piping:** orthogonal process runs — cyan HSS/HTRL · dark blue LSS/LTRL · orange HPL/HTRS (FT-inspired, BH stroke weight)
  - **Out of scope for now:** pump pressure / PSIG / other sensor indicators (do not restore)

### Style
- **D-06:** Match BH modern style (Perspective themes + Advanced Stylesheet CSS-only). Should look better than FactoryTalk; do not pixel-clone FT chrome.
- **D-07:** Piping colors in Figma: **colored** (not black). Process colors adapted from FactoryTalk for BH:
  - Cyan / light blue ≈ HSS / HTRL
  - Dark blue ≈ LSS / LTRL
  - Orange ≈ HPL / high-pressure liquid / HTRS

### Components to use (BH)
- **D-08:** Tank, Valve (SolenoidValve / SolenoidValve3Way), Pump, Compressor for equipment.
- **D-09:** Piping for PID lines (BH approach — rectangles/joints in Figma; no dedicated Piping view yet in Ignition).
- **D-10:** Sensors / PSIG indicators — **deferred** (not on this screen for now). Figma Sensor symbol exists; Ignition Sensor view not in BH yet.

### Explicit exclusions (do not design or implement)
- **D-11:** Suction SP buttons
- **D-12:** Top nav (page uses docked BH nav; no FT top nav clone)
- **D-13:** Date/time / PLC status (left strip)
- **D-14:** E-stop
- **D-15:** LTU transfer counts / alarm SP
- **D-16:** Top-right fans / safetys panel
- **D-17:** Pump pressure indicators / PSIG / other standalone sensors (locked out for this Figma pass)

### Claude's Discretion
- Exact Figma page name / frame structure within Dev Jam (as long as it is a **new page** in `Q8EmmXokQsiX91aPMtLm2w`) — **resolved:** Machine Room / Machine Room — P&ID
- Improved spacing/hierarchy vs FT while preserving equipment topology
- Placeholder vs bound labels in Figma (static art until tag decision)
- Respect Dylan’s on-canvas cleanup; refine remaining layout rather than restoring deleted chrome

</decisions>

<specifics>
## Specific Ideas

- Reference: FactoryTalk **MACHINE ROOM** screenshot placed on the Machine Room page (`244:2270`) for spatial pipe routing — not 1:1 chrome.
- Reuse chrome patterns from existing BH devices (Poppins label, analog + EU, status row) — see `.cursor/rules/figma-ignition-hmi.mdc`.
- Pilot for tracker IDs **2 / 11** (screen migration + graphics cleanup) within Phase 3.

</specifics>

<canonical_refs>
## Canonical References

### Figma / HMI rules
- `.cursor/rules/figma-ignition-hmi.mdc` — Dev Jam fileKey, device nodes, Figma-first gate, Ignition path conventions
- `.cursor/rules/perspective-css-only.mdc` — styling only via Advanced Stylesheet
- `.cursor/rules/perspective-reference.mdc` — Scout/Designer JSON shapes, ticket logger, status colors
- `docs/theme-figma-tokens.md` — theme tokens; Sensor node `145:2443` (deferred for this screen)

### Planning
- `.planning/ROADMAP.md` — Phase 3
- `.planning/PRIORITIES.md` — Need ranking for screens (IDs 2, 11)

### Deliverable
- [Machine Room — P&ID](https://www.figma.com/design/Q8EmmXokQsiX91aPMtLm2w/Dev-Jam?node-id=248-1954) (`248:1954`)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets (BH Perspective)

Base: `gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/`

| Role | Device / faceplate / page paths |
|------|----------------------------------|
| **Tank** | `02_Components/01_Devices/Tank` · faceplate `01_Popups/00_Faceplates/Tank` · page `00_Pages/Tanks/Overview` · Figma `215:2238` |
| **Valve** | `02_Components/01_Devices/SolenoidValve` · `SolenoidValve3Way` · faceplates under `01_Popups/00_Faceplates/` · page `00_Pages/Valves/Overview` · Figma `216:2101` / `217:2302` |
| **Pump** | `02_Components/01_Devices/Pump` · faceplate `01_Popups/00_Faceplates/Pump` · pages `00_Pages/Pumps/Overview`, `Pumps/Graphic` · Figma `145:2033` |
| **Compressor** | `02_Components/01_Devices/Compressor` · faceplate `01_Popups/00_Faceplates/Compressor` · pages `00_Pages/Compressors/Overview`, `Compressors/Graphic` · Figma `148:2020` |
| **Sensor** | **Deferred for Machine Room** — Figma only (`145:2443`); no Ignition device yet. Closest: `03_Elements/00_Control/AnalogValue`. |
| **Piping** | **No** reusable Piping view. Stub: `00_Pages/Devices/DesignOverview`. Theme tokens: `--pipePrimaryFill` / `--pipeStroke` (generic IA pipe). Process colors (HSS/LSS/HPL) to be defined in CSS when Ignition build opens. |

### Established Patterns
- Device embeds: `ia.display.view` + `params.tagPath` / `params.faceplate`
- CSS-only look-and-feel via `stylesheet/stylesheet.css` classes
- Coordinate P&ID-style layouts already sketched in DesignOverview

### Integration Points (post-Figma approval only)
- New page under `00_Pages/Machine Room/` + `page-config/config.json` route
- Ticket logger on root (per perspective-ticket-logger rule)
- Tag binding deferred until Dylan decides (see open questions)

</code_context>

<deferred>
## Deferred Ideas

- Full Ignition build of Machine Room (blocked on Figma approval)
- Pump pressure / PSIG / Sensor indicators on this screen
- Tag/UDT binding for HTR/HPR/LTR, HTRL/LTRL pumps, COMP 7/6/5/4/1
- FT chrome excluded above (SP buttons, E-stop, LTU counts, fans/safetys panel, etc.)
- Pulling Sensor into Ignition from Figma (separate device ticket)
- Ignition CSS tokens for HSS cyan / LSS dark blue / HPL orange (mirror Figma when build opens)

</deferred>

## Open questions (Dylan)

1. **Tag binding timing:** Bind tags in first Ignition build, or layout-only placeholders until Phase 2 UDTs exist?
2. **Page route / nav label:** Exact path + docked-nav entry (e.g. `/machine-room` vs `/machine-room/overview`)?
3. **Valve usage on this screen:** Confirm current Figma set (MAIN LIQ SV, HTR-SV, LTR-SV, HTRL-ISO, LTRL-ISO) is final for v1.
4. **Sensors later:** When (if) to add PSIG / Sensor embeds — separate pass after Figma approval?

---

*Phase: 3-hmi-machine-room*
*Updated: 2026-07-29*
