---
title: PLC Rack 3D View
sidebar_position: 16
description: The interactive 3D model of the RCP1 CompactLogix rack inside Perspective - how to open it, orbit, zoom to a module, tooltips, touch, demo mode, login rule and live LEDs.
sources:
  - docs/plc-rack-3d.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Rack3d/code.py
last_verified: 2026-10-24
---

# PLC Rack 3D View

## What it does

A three-dimensional model of the RCP1 CompactLogix 5370 rack: controller, a bank power supply, the 19 I/O cards and
the end cap, mounted on a DIN rail. It sits **next to** the 2D rack ([PLC Rack / IO](./plc-rack-io.md)) and is
**read only**: it only reads tags below `[default]Boars_Head/`, never writes, and never touches the PLC itself.

<video controls preload="metadata" poster="/video/plc-rack-3d-demo-poster.png" width="100%">
  <source src="/video/plc-rack-3d-demo.mp4" type="video/mp4" />
  Your browser cannot play this video. It shows a 30 second tour of the 3D rack in demo mode.
</video>

The video (re-rendered 2026-10-24) is the 3D view in demo mode: orbit, fly straight-on into the controller, open a card
door, tap terminals, fly to an analog card (IF8) and back to the rack.

![The 3D rack in demo mode](/img/features/plc-rack-3d/demo-full.png)

## How to use it

**Open it:** Groveport > Operations > PLCs > RCP1 shows the 2D rack; click the **3D View** button in its summary row.
The route is `/operations/plcs/RCP1/3d` (`/operations/plcs/:plc/3d` for another PLC). There is no navigation item.
The **2D View** button on the 3D page goes back.

| Control | Does |
|---|---|
| Drag | Orbit around the rack |
| Mouse wheel | Zoom in / out |
| Right-drag | Pan |
| Hover a module | Outline plus a tooltip with its name, catalog number and status |
| Click or tap a module (card, controller, power supply, end cap) | The camera flies **straight on** to the module (square to its face, no tilt), its door swings open, the others dim and a side panel lists every point with its label and live state (or the channel value and unit) |
| Click or tap another module while zoomed | Flies straight to that module |
| **Back To Rack**, **Esc**, a click on empty space, or the browser Back button | Returns to the overview pose and closes the door |
| **Reset View** | Same as Back when zoomed; otherwise flies to the default pose |
| Hover a terminal (door open) | Amber highlight and a tooltip: terminal, point, label and live ON / OFF (or value plus unit) |
| **Touch screens** | A tap does what a hover or click does. Tapping a terminal pins its tooltip; it moves on the next terminal tap and closes on a tap on empty space, Esc or zooming out. A drag is an orbit, not a tap |

If the operating system asks for reduced motion, every transition is instant. If the browser has no WebGL the page
says "3D View Unavailable" and points to the 2D page.

![The straight-on zoom on a card](/img/features/plc-rack-3d/zoom-straight-on.png)

![A card zoomed in, door open, side panel](/img/features/plc-rack-3d/demo-door-open.png)

![A terminal tooltip](/img/features/plc-rack-3d/terminal-hover.png)

## What is modelled

- **Power supply:** a separate 70 mm 1769 expansion power supply with a POWER lamp, a terminal door and three
  terminals. The CompactLogix 5370 **L3 has no embedded power supply**, so it is drawn as its own module; its catalog
  number is not in the controller export, and its face says "Catalog Not In L5X".
- **Labels:** every point shows the label taken from the controller program (for example the pump the point feeds) in
  the side panel and in terminal tooltips; spare points read "Spare (Not In Logic)".
- **Analog IF8 card:** drawn like the real module, with **two terminal blocks of four staggered screw columns of nine
  (36 terminals)**: `V/I in n-`, `ANLG Com`, `V in n+`, `I in n+` and `NC`. Hovering or tapping a channel terminal
  shows its role (for example "Channel 0 Voltage Input (V In +)"), the point label and the live value with its unit;
  `ANLG Com` and `NC` show only their role.
- **Discrete cards:** the 1769-RTBN18 layout (9 rows of 2) with the even points on the right, as on the door label.
- **Screw type:** terminal screws are drawn **Phillips** by default. See How To Change It to switch a PLC to **flat
  (slotted)** screws.

## Live data, comm loss and demo mode

- **Live LEDs:** the page polls every 2 seconds. Green = on, gray = off or no data, red = fault (a card's OK LED
  when it is faulted, the controller I/O / OK LEDs on an I/O or major fault). Output points follow the read-back.
  The controller's **keyswitch** turns to RUN / REM / PROG from the live mode.
- **Comm loss:** while the PLC driver is not connected every live value is empty: all LEDs turn gray, a
  "Communication Lost" banner shows and the status chip reads **Comm Loss**. The keyswitch stays at the last known
  position, gray, labelled "Last Known, Not Live". This is the normal picture while the SecureLink to the PLC is down.
- **Demo mode:** add `?demo=1` to the frame address (`/system/webdev/BH/rack3d/view?plc=RCP1&demo=1`, after logging in
  to the HMI) to show a static sample with a "Demo" badge. It does not poll and does not read any tag, so it works
  with the PLC offline.
- **Login required:** the page, its data and its files need a logged-in BH session in the same browser; an anonymous
  request gets a 401. See [Security Access](./security-access.md). Any signed-in user can open it; there is no extra
  permission row.

![The 3D page inside Perspective with the PLC link down](/img/features/plc-rack-3d/perspective-3d-live.png)

## Where the pieces live

| Piece | Where |
|---|---|
| Page | Designer > Project Browser > Perspective > Views > `00_Pages` > `Groveport` > `Machine Room` > `Utility` > `PlcRack` > `Rack3d`: a title row and an Inline Frame; its `props.src` is an expression binding to `/system/webdev/BH/rack3d/view?plc=...&theme=...` (theme from `session.props.theme`) |
| Route | Designer > Perspective > Page Configuration: `/operations/plcs/:plc/3d` |
| WebDev | Designer > Web Dev > `rack3d`: `view` (HTML), `state` (JSON), `lib` (the 3D library and scripts). Python resources, GET only |
| Script library | `shared.Rack3d` (builds the state, serves the files) and `shared.WebAuth` (the login check) |
| Button | on the 2D page `PlcRack/Overview`, the **3D View** button in the summary row |

The state answer contains rack and I/O status only: controller name, catalog, mode, fault flags, firmware, module
counts, per-slot status, point bits or channel values, and the point labels. It never returns an IP address, tag
paths or secrets, and only reads below `[default]Boars_Head/`. The 3D library (three.js) is stored on the gateway,
so the page works on a plant network without internet.

## How To Change It

- **Switch the terminal screw head (Phillips or flat) for a PLC:** Designer > Tag Browser > `[default]_Config` >
  `PLCs` > `List` > double-click the tag to open the Tag Editor > the Value (a Document). Find the PLC's entry (for
  example `RCP1`) and add or edit `"screwType": "phillips"` or `"screwType": "flat"` (anything else, or no key, means
  Phillips) > OK. The setting is read when the page loads, so reload the 3D page. There is no toggle in the 3D screen.
  The installation sheets do not state the head style, so check the real hardware.

- **Change the Inline Frame address or theme handling:** Designer > open `Rack3d` > select the Inline Frame >
  Property Editor > `props.src` > edit the expression binding.
- **Move or remove the 3D View button:** Designer > open `PlcRack/Overview` > select the button in the summary row.
  Deleting it (and the route in Page Configuration) removes the feature from the HMI without touching the 2D page.
- **Show the 3D page for another PLC:** add the PLC to the tag `[default]_Config/PLCs/List` (Tag Browser > edit the
  Document value) and make sure its site UDT instance has a `Rack` document, as described in
  [PLC Rack / IO](./plc-rack-io.md). Then open `/operations/plcs/<name>/3d`.
- **Restrict who can open it:** add a row to `[default]_Config/RolesPermissions` and gate the 3D View button's
  `props.enabled` or `position.display` on `session.custom.Permissions`, as in
  [Roles And Permissions](./roles-permissions.md).
- **Edit the scene itself** (colours, LED layout, tooltips): Designer > Web Dev > `rack3d` > the resource script, and
  the `shared.Rack3d` script in the Project Library. A new card type also needs its catalog number added to the
  `Rack` document of the site UDT.

## Known limitations and parked items

- The FORCE, SD and LINK 2 lamps have no source tag and always show gray.
- The bank power supply catalog number is not in the controller export; its face says "Catalog Not In L5X". The bank split
  (how many supplies and banks the 19 cards need) is drawn as one bank and is to be confirmed on the panel.
- The terminal screw head style (see `screwType`) and the discrete cards' terminal layout come from the door labels and
  manuals; verify them on the real hardware. The IF8 layout follows its installation sheet.

Source of truth: `docs/plc-rack-3d.md`.
