---
title: PLC Rack
sidebar_position: 12
description: The read-only RCP1 PLC rack page (/operations/plcs/:plc) - fluid card drawings, hover card, detail panel and pop-out card faceplates.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/03_PLC/**/view.json"
  - "docs/plc-rack-io.md"
last_verified: 2026-10-24
---

# PLC Rack

A read-only drawing of the RCP1 CompactLogix controller (1769-L36ERM, named "BoarsHead") and its 19 local 1769 I/O
cards, with live LEDs and channel values. Hover a card for a summary, click it for the full point list, or pop it
out into its own faceplate. Nothing on this page writes.

![PLC Rack](/img/perspective/plc-rack.png)

| | |
|---|---|
| Routes | `/operations/plcs` (PLC Overview), `/operations/plcs/:plc` (for example `/operations/plcs/RCP1`; `:plc` = the site UDT instance name), `/operations/plcs/:plc/3d` (3D model, below), `/plc-rack` (alias that opens RCP1) |
| View | [`00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview`](../reference/views/00-pages/groveport/machine-room/utility/plcrack/overview.md), param `plc` |
| Components | `02_Components/03_PLC/*`: `Controller_CompactLogix_5370`, `Module_1769_IF8` / `_IA16` / `_IQ16` / `_OA16` / `_OW16`, `EndCap_1769_ECR`, `RackSlot`, `ModuleHover`, `ModuleDetail`, `PointRow`; the overview uses `PlcCard` and `PlcCardLed` (one segment of the health bar) |
| Pop-out | [`01_Popups/00_Faceplates/PlcRack/CardDetail`](../reference/views/01-popups/00-faceplates/plcrack/carddetail.md) |
| Tags | `[default]Boars_Head/GrovePort/Machine Room/PLC/RCP1` (UDT `PLC/Sites/BH_Groveport_RCP1`, members read OPC directly and are read only) |
| Changing it | [PLC Rack / IO](../../features/plc-rack-io.md#how-to-change-it) |
| Nav | Groveport > Operations > PLCs (folder, opens the PLC Overview) > RCP1 (the rack) |
| Design notes | `docs/plc-rack-io.md` |

## PLC Overview (`/operations/plcs`)

Clicking the **PLCs** folder in the nav opens `00_Pages/Groveport/Operations/PlcOverview`: a title with the PLC count,
then a wrapping flex repeater of one [`02_Components/03_PLC/PlcCard`](../reference/views/02-components/03-plc/plccard.md)
(400 x 440, no horizontal scroll) per PLC. The cards come from the memory Document tag
`[default]_Config/PLCs/List` (`{plcs: [{name, path, description, location, page, show: {Field: bool}}]}`); the live
list is yours, so **adding a PLC is a tag edit, not a view edit**. Each card shows
(per `show<Field>` param; automatic = shown when the instance has the member) Description, Catalog, Firmware, IP,
Driver, Comm Loss, Mode, Major / Minor / I/O fault, last fault, modules faulted (n / N), module types, active alarms
(count and top alarm) and a rack strip (a segmented health bar, one `PlcCardLed` segment per card: green OK, red faulted, gray while comm is lost). The
status pill reads COMM LOSS (red) / MAJOR FAULT / the mode / NO DATA, the Modules summary shows a red COMM LOSS, and
status rows show `--` while disconnected.
Clicking a card opens `params.page` (default `/operations/plcs/<name>`).

![PLC rack page with the controller communication lost (SecureLink down): summary cards, rack, detail panel](/img/perspective/plc-rack.png)

## 3D View (`/operations/plcs/:plc/3d`)

The **3D View** button in the summary row of the rack page opens `00_Pages/Groveport/Machine Room/Utility/PlcRack/Rack3d`:
a title row (with a **2D View** button back) and an Inline Frame whose `props.src` is an expression binding to the WebDev
resource `/system/webdev/BH/rack3d/view?plc=<plc>&theme=<light or dark>`. The frame shows a three.js model of the
controller, power supply and the 19 cards, with click-to-zoom, terminal tooltips and live LEDs from the `rack3d/state`
resource. It is read only and, like every WebDev resource, needs a logged-in BH session (anonymous = 401). See
[PLC Rack 3D View](../../features/plc-rack-3d.md).

## PLC Alarms

The controller family UDT `PLC/Controllers/CompactLogix_5370` carries the alarms **Controller Communication Lost**
(`CommLoss` = not Connected, Critical, 12 s active delay so SecureLink blips ride through), **Major Fault** (Critical),
**I/O Fault** (High), **Not In Run Mode** (High) and **Minor Fault** (Low); every card has a **Module Fault**
(High). Every dependent member is gated on the driver connection, so with comm lost only "RCP1 Communication Lost"
is active (the summary cards show "1 - Controller Communication Lost"). Counts come from `system.alarm.queryStatus`
on the site path (script transform, 10 s). See [Alarms](../../tags/alarms.md).

## Navigation Fix (`_hasRoute`)

The nav item RCP1 used to go nowhere: `Navigation.Nav._hasRoute` compared page-config routes exactly, so
`/operations/plcs/RCP1` never matched `/operations/plcs/:plc`. It now matches `:param` segments. Any new nav item that
points at a parameterised route works the same way; an item whose page is missing from page-config still opens
`/no-view`.

## How It Works

- **Site path from the URL.** The page derives the site tag folder from the route parameter:

```js
// custom.sitePath
'[default]Boars_Head/GrovePort/Machine Room/PLC/' + if(coalesce({view.params.plc}, '') = '', 'RCP1', {view.params.plc})
```

- **One rack document.** `custom.rack` is an indirect tag binding to `{site}/Rack` (a Document member of the site
  UDT). It lists the controller, cards and end cap, each with its catalog, slot, `units` (drawing width) and labels.
  The summary cards at the top read `{site}/Run`, `/Mode`, `/Connected`, `/ModulesFaulted`, `/ModuleCount`,
  `/MajorFaultRecordCode`.
- **Card layout v5.** A slim 20-unit door band (module name on the label, catalog under it), discrete cards with LEDs
  and numbers in two columns, IF8 channels on two lines (LED + number and unit, then the value right-aligned), a compact
  controller power band. The page padding is 16 / 24 / 24 / 24 px and it scrolls vertically if a screen is too short.
- **Scale to fit, no script.** The rack is one flex repeater over `Rack.items`. Each item's `flex-basis` is its units
  / 1164 %, and the repeater keeps `aspect-ratio: 1164 / 280`, so all 21 items always fit the width. A stylesheet
  container query (`.psc-plcrack-host`, `@container (max-width: 1000px)`) switches to two banks on narrow screens.
- **Hover card.** A card's `onMouseEnter` / `onMouseLeave` send the page message `plcRackHover`; the page shows
  `ModuleHover` beside the card (CSS `clamp()` keeps it on screen, `pointer-events: none`).

![Hover card](/img/perspective/plc-rack-hover.png)

- **Click = select.** A click selects the card (green outline) and fills `ModuleDetail` below: 16 points in two
  columns for discrete cards (number, LED, L5X description, state, and the command for outputs), 8 channels with
  value, unit, range status and raw count for the 1769-IF8, or 16 controller fields.
- **Open In Faceplate** calls `shared.PlcRack.openCard(sitePath, member, slot, kind, title, viewportW, viewportH)`.
  Each card gets its own popup id (`plcRackCard-<member>`), so several can be open side by side. The popup embeds
  the same `ModuleDetail` with `inPopup = true`. `shared.Alerts.showFaceplate` is not used here because it opens
  the tabbed device shell with one fixed id.

![Pop-out card](/img/perspective/plc-rack-popout.png)

## Add Another PLC

1. Add a site UDT (or reuse one) and an instance under `Boars_Head/<Site>/<Area>/PLC/<Name>`; load its point
   labels into the instance's `Rack` document (contact the system integrator for a whole new L5X).
2. Add a nav item `<Name>` under PLCs with page `/operations/plcs/<Name>`. The page resolves `sitePath` from the
   `[default]_Config/PLCs/List` entry named `:plc` (fallback `Boars_Head/GrovePort/Machine Room/PLC/<plc>`).
3. Set the instance's `ControllerName` / `IPAddress` parameters (overridden per instance, so no view holds a PLC
   constant) and add the PLC to `_Config/PLCs/List` for its overview card.
