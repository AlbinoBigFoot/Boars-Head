---
title: PLC Rack / IO
sidebar_position: 7
description: The read-only drawing of the RCP1 CompactLogix rack and its 19 I/O cards - hover, click, pop-out faceplates, the L5X import that labels every point, and the tag layers behind it.
sources:
  - docs/plc-rack-io.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/PlcRack/code.py
last_verified: 2026-10-24
---

# PLC Rack / IO

## What it does

A **read-only** 2D drawing of the RCP1 controller (CompactLogix 5370 L3, 1769-L36ERM, named "BoarsHead") and its
19 local I/O cards, like Studio 5000's I/O tree but live:

- every card shows its OK / fault LED, per-point LEDs (discrete cards) or channel values in V / mA (analog cards)
  and its Studio 5000 module name;
- the controller shows RUN / OK / NS / LNK and its mode;
- a **separate 1769 power supply** is drawn beside the controller (the 5370 L3 has no embedded supply; its catalog
  number is not in the controller export, so it is labelled "Catalog Not In L5X" and the controller detail says
  "Separate 1769 Power Supply (Catalog Not In L5X)");
- **hover** a card for a summary card, **click** it for a two-column detail of every point (L5X description, tag,
  live state), **Open In Faceplate** to pop it out (several side by side).

Nothing on the page writes anything: the UDTs read OPC directly with every member `readOnly`, and clicks only
change UI state.

![Rack at 1920 px](/img/features/plc-rack/v4-full-1920.png)

![Hover card on a discrete input card](/img/features/plc-rack/v4-hover-DI-1920.png)

## How to use it

Nav: **Groveport > Operations > PLCs** opens the **PLC Overview** (`/operations/plcs`): one card per PLC from the
memory Document tag `[default]_Config/PLCs/List` (status pill, firmware, IP, faults, active alarms,
a module health bar). Click a card, or **PLCs > RCP1**, for the rack (`/operations/plcs/RCP1`; the old `/plc-rack` still
works). Details: [PLC Rack page](../perspective/pages/plc-rack.md).

The **PLC Overview card** (updated 2026-10-24) shows the name and a status pill (COMM LOSS, MAJOR FAULT, the mode, or
NO DATA), description, catalog, firmware, IP, driver, the fault rows, the module types, the active alarms (count and
top alarm) and one **Modules** row: a **segmented health bar** with one equal-width segment per card (green OK, red
faulted, gray when the PLC link is lost) and a summary under it: "19 / 19 OK" in green, "2 Faulted - 17 / 19 OK" in
red, or a red **COMM LOSS** while the link is down. The separate Modules Faulted row was merged into this row. Hover
a segment for its slot and module name. While disconnected the status rows show a dash and the identity rows keep
their last known value.

The rack page has a **3D View** button that opens the [3D rack](./plc-rack-3d.md).

![PLC rack with the controller offline (SecureLink down)](/img/perspective/plc-rack.png)

| Slot | Module | Card | Points |
|---|---|---|---|
| 1-4 | IF8_S1 ... S4 | 1769-IF8/A analog in | 8 channels each (zone air temps, tank levels, system pressures) |
| 5, 6, 10, 11 | IA16_S* | 1769-IA16/A 120 V AC in | 16 |
| 7-9 | IQ16_S* | 1769-IQ16/A 24 V DC in | 16 (rupture disks PS1-41, RCP Reset) |
| 12-17 | OA16_S* | 1769-OA16/A AC out | 16 (CG valves, main liquid / hot gas, make-up water) |
| 18-19 | OW16_S* | 1769-OW16/A relay out | 16 (recirculator pumps, condenser fans / pumps, CG fans, RCP MCR) |

272 points: 230 labelled from the L5X, 42 "Spare (Not In Logic)"; 49 inputs are inverted in logic ("Inverted").
28 analog channels are **0-5 V** and 4 are **4-20 mA** (from the L5X channel configuration); the HMI shows each in its
own unit.

## Where to find it

- **HMI**: nav Groveport > Operations > PLCs (overview) > RCP1 (rack).
- **Designer**: Project Browser > Perspective > Views > `00_Pages` > `Groveport` > `Machine Room` > `Utility` >
  `PlcRack` > `Overview`, the parts under `02_Components` > `03_PLC`, and `00_Pages` > `Groveport` > `Operations` >
  `PlcOverview`. Tags: Tag Browser > `default` > `Boars_Head` > `GrovePort` > `Machine Room` > `PLC` > `RCP1`, list tag
  `_Config` > `PLCs` > `List`; UDTs under the Tag Browser's Data Types folder (`PLC` > `Modules`, `Controllers`, `Sites`).
- **Gateway web UI**: Connections > Devices > Connections > `RCP1` (the driver that reports Connected / Disconnected); the
  RCP1 alarms appear in Status > Alarming too.

## Where the pieces live (developers)

| Piece | Where |
|---|---|
| Page | `00_Pages/Groveport/Machine Room/Utility/PlcRack/Overview`, route `/operations/plcs/:plc` (`sitePath` is derived from `:plc`) |
| Components | `02_Components/03_PLC/*`: `Controller_CompactLogix_5370`, `Module_1769_IF8/_IA16/_IQ16/_OA16/_OW16`, `EndCap_1769_ECR` (fluid SVGs), `RackSlot`, `ModuleDetail`, `PointRow`, `ModuleHover` |
| Pop-out | `01_Popups/00_Faceplates/PlcRack/CardDetail` (embeds `ModuleDetail`), opened by `shared.PlcRack.openCard` (popup id per card) |
| Tags | UDTs `PLC/Modules/_Discrete16In`, `_Discrete16Out`, `1769_IA16`, `1769_IQ16`, `1769_OA16`, `1769_OW16`, `1769_IF8`; family `PLC/Controllers/CompactLogix_5370`; site `PLC/Sites/BH_Groveport_RCP1` (Slot01-19 + the `Rack` document); instance `[default]Boars_Head/GrovePort/Machine Room/PLC/RCP1` |
| Alarms | On UDT members: Controller Communication Lost (Critical, 12 s delay), Major Fault (Critical), I/O Fault (High), Not In Run Mode (High), Minor Fault (Low), and a Module Fault (High) per card; dependents are gated on `Connected`, so comm loss raises only the Communication Lost alarm |
| Overview | `00_Pages/Groveport/Operations/PlcOverview` + `02_Components/03_PLC/PlcCard`, data tag `[default]_Config/PLCs/List` |

Where the labels come from: the L5X export has no alias tags; program `BufferIO` has one rung per point
(`XIC(Local:5:I.Data.7) OTE(LTR_PUMPS[1].Inp_RunFdbk)`), so each point is labelled from the PAX object it feeds
(array element comment, then tag description, Title Case with acronyms kept), with the tag in brackets.

Layout: one flex repeater over `Rack.items` with `flex-basis` = units / 1164 % and a fixed aspect ratio, so all 21
items scale to the width with no scroll; under 1000 px a container query switches to two banks. Hover / select are
page messages `plcRackHover` / `plcRackSelect`.

## How To Change It

All steps are Designer edits; save, then test in a session. Don't change the PLC tags while the write lock is being
flipped.

- **One point label or a changed slot:** Tag Browser > `[default]Boars_Head/GrovePort/Machine Room/PLC/RCP1` > the
  `Rack` member (a Document tag). Edit the JSON for that slot's item (its points list). The page redraws from the
  tag.
- **A whole new L5X export** (new point labels for every card): the L5X is read by the system integrator's tooling
  and the result is written into the `Rack` document. Contact the system integrator for this step. Check afterwards
  that the labels read the way operators expect.
- **A new card type:** UDT Definitions > `PLC/Modules`: copy a similar card UDT (16-point cards inherit
  `_Discrete16In` / `_Discrete16Out`), set its OPC item paths
  (`[{DeviceName}]Local:{Slot}:I|O|C.*`) and the Module Fault alarm. Then add a module view under
  `02_Components/03_PLC` (copy a similar `Module_1769_*` view) and add the slot to the `Rack` document.
- **Another PLC:**
  1. UDT Definitions > `PLC/Sites`: copy `BH_Groveport_RCP1` for the new site.
  2. Tag Browser: add an instance under `Boars_Head/<Site>/<Area>/PLC/<Name>` of the new site UDT, with the
     controller name and IP parameters, and edit its `Rack` document.
  3. Add an entry to `[default]_Config/PLCs/List` (feeds the PLC overview cards).
  4. Add a nav item under PLCs in the Navigation view's `custom.items` with `/operations/plcs/<Name>`
     ([Navigation](../perspective/navigation.md)).
- **Alarms:** edit them on the UDT members (Controller Communication Lost, Major Fault, I/O Fault, Not In Run Mode,
  Minor Fault, Module Fault), see [Alarms](alarms.md#how-to-change-it).
- Gotcha: when an existing UDT gains a parent type, instances may not update until you remove and re-add the
  definition; test on a copy first.
- Nav note: `Navigation.Nav._hasRoute` matches `:param` route segments, which is what makes `/operations/plcs/:plc`
  reachable from the nav.

### Changing the PLC Overview card

Designer > Views > `02_Components/03_PLC` > `PlcCard`. Each row has a `show<Field>` view parameter (empty = automatic,
shown when the PLC instance has that member; `true` / `false` forces it). The Modules row is `showRackStrip`. Which
PLCs get a card is the Document tag `[default]_Config/PLCs/List`.

## Known limitations and parked items

1. Bank layout / extra 1769 power supplies: not in the L5X; confirm on the panel.
2. FORCE / SD lamps need a GSV routine in the PLC (controls engineer).
3. Slot 4 Ch1 / Ch2 (underfloor temps TS_UF1 / TS_UF2) read 0 / Under Range: check sensors and wiring.
4. Analog signal types: the L5X says 28 channels are 0-5 V; confirm field devices if it matters.
5. Module fault codes show only the raw `Fault` word.
