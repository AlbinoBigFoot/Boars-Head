---
title: Safety Relay 3D View
sidebar_position: 21
description: The interactive 3D model of the HLCO safety relay inside Perspective - the 2D / 3D toggle, controls, terminal tooltips, live LEDs, comm loss, demo mode, login rule and the panel details still to confirm.
sources:
  - docs/safety-relay-3d.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Relay3d/code.py
last_verified: 2026-10-24
---

# Safety Relay 3D View

## What it does

A three-dimensional model of the **HLCO safety relay**: an Allen-Bradley Guardmaster **440C-CR30-22BBB/A** configurable
safety relay with a **440C-ENET** EtherNet/IP plug-in and a **2080-IQ4-OB4** plug-in (4 inputs, 4 outputs). It sits next to
the 2D Safety Relay page ([Safety Relay And Rupture Disks](../perspective/pages/safeties.md)) and is **read only**: it only
reads tags and never writes. It uses the same 3D framework as the [PLC Rack 3D View](./plc-rack-3d.md).

![The 3D relay inside Perspective with live LEDs](/img/features/safety-relay-3d/perspective-3d-live.png)

## How to use it

**Open it:** open the 2D page (`/safety-relay`, from the Machine Room page or Groveport > Machine Room > Devices) and
press **3D View**. The 3D page is `/safety-relay/3d`; its **2D View** button goes back. There is no navigation item
of its own.

![The 2D page with the 3D View button](/img/features/safety-relay-3d/2d-page.png)

| Control | Does |
|---|---|
| Drag | Orbit around the relay |
| Mouse wheel | Zoom in / out |
| Right-drag | Pan |
| Hover a terminal (any time) | A tooltip: terminal name, row, its true role from the manual, the project description and the live **ON / OFF** (red **COMM LOSS** when the link is down) |
| Tap a terminal (touch) | Pins the tooltip; tap another to move it, tap empty space or press Esc to close |
| Click or tap the relay | The camera flies **straight on** to the face (about 0.8 s) and the side panel opens |
| **Back**, **Esc**, a click on empty space, or the browser Back button | Returns to the overview |

If the operating system asks for reduced motion the transitions are instant. If the browser has no WebGL the page says
so and points to the 2D page.

![Straight-on zoom with the info panel](/img/features/safety-relay-3d/zoom-straight-on.png)

The side panel shows: status, run mode, major fault code and type, minor fault, connection, "SOF01 / SOF02 reset
required", the reset alarm, the plug-ins, then the point list (inputs 0 to 9, outputs 0 to 5, plug-in inputs and
outputs).

![A terminal tooltip while zoomed in](/img/features/safety-relay-3d/terminal-tooltip-zoomed.png)

## Live data, comm loss and demo mode

- **Live LEDs:** the page polls the relay tags. They match the 2D page: RUN green, FAULT red, inputs and outputs green
  when on. Output lamps 4 and 5 are SOF05 / SOF06 (as on FactoryTalk and the 2D page).
- **Comm loss:** when the relay connection is bad or faulted every lamp turns gray, the **COM lamp is red**, the status
  reads **COMM LOSS**, and a "Communication Lost" banner and the chip "Comm Loss" appear. A single value with bad
  quality reads "No Data" in gray. This is the normal picture whenever the PLC link is down.
- **Demo mode:** add `&demo=1` to the frame address (`/system/webdev/BH/relay3d/view?plc=RCP1&demo=1`, after logging
  in to the HMI) for a static sample taken from a real read; it reads no tags and works with the PLC offline.
- **Light and dark:** the model follows the session theme.
- **Login required:** the page, its data and its files need a logged-in BH session in the same browser; an anonymous
  request gets 401 and anything other than GET gets 501. Any signed-in user can open it; there is no permission row. See
  [Security Access](./security-access.md).

![Demo mode, dark theme](/img/features/safety-relay-3d/demo-dark.png)

## Where the pieces live

| Piece | Where |
|---|---|
| 3D page | Designer > Project Browser > Perspective > Views > `00_Pages` > `Groveport` > `Machine Room` > `Utility` > `SafetyRelay` > `Relay3d` (a header and an Inline Frame; `props.src` is an expression binding to `/system/webdev/BH/relay3d/view?plc=RCP1&device=HLCO%20Safety%20Relay&theme=...`) |
| 2D page and the 3D View button | the `SafetyRelay` > `Overview` view in the same folder |
| WebDev | Designer > Web Dev > `relay3d`: `view`, `state`, `lib` (Python resources, GET only) |
| Script library | `shared.Relay3d` (state and the whitelisted files) and `shared.WebAuth` (login check on every request) |
| three.js | not duplicated: the page loads it from `rack3d/lib`, so upgrading that library covers both 3D pages |
| Tags | `[default]Boars_Head/GrovePort/Machine Room/SafetyRelays/<device>/IO/*` (device UDT `Devices/SafetyRelay`, members from `PLC/CR30_Input`), `PlcMajorFault`, `PlcResetAlm` |

The state answer holds only the relay status, the point bits and fault codes; it returns no addresses, tag paths or
secrets. Points read: Pt00 to Pt09, Pt18 to Pt21, SOF01 / 02 / 05 / 06, SOF01 / 02 reset required, RunMode,
ConnectionFaulted, MajorFault code and type, MinorFault. Labels: In 0 = LSS HLCO, In 1 = HSS HLCO; Out 0 = LSS HLCO Output
0, Out 1 = HSS HLCO Output 1.

## How To Change It

- **Change the Inline Frame address, device or theme handling:** Designer > open `Relay3d` > select the Inline Frame >
  Property Editor > `props.src` > edit the expression binding. `device=` selects the relay folder under
  `SafetyRelays/`; the terminals and labels are HLCO-specific today.
- **Change the 3D View button or the route:** Designer > open the 2D `Overview` view and select the button; Designer >
  Perspective > Page Configuration for `/safety-relay/3d`.
- **Switch the terminal screw head (Phillips or flat):** the same Designer-only setting as the rack: Tag Browser >
  `[default]_Config` > `PLCs` > `List` > double-click the tag > the `RCP1` entry (the relay hangs off RCP1) >
  `"screwType": "phillips"` or `"flat"`; reload the 3D page. There is no toggle in the screen.
- **Edit the scene, terminal roles or LED rules:** Designer > Web Dev > `relay3d` (the page resources) and the
  `shared.Relay3d` script in the Project Library. The layout constants are at the top of the page script.
- **Add another relay:** add its device instance under `SafetyRelays/` and open the 3D page with `device=<name>`; its
  terminal roles and labels need their own entries.

## Known limitations and items to confirm on the panel

There are no product photos or dimensioned drawings in the project; every texture is drawn from the Rockwell 440C-UM001
manual and the FactoryTalk display. These are approximations to confirm on the real panel:

- The row assignment (inputs on top; A1, A2 and 12 to 21 on the bottom), the terminal pitch and the plug-in positions
  follow the manual text and figure descriptions, not a dimensioned drawing.
- The USB Type-B and RS-232 ports are drawn on the left side wall; the manual does not state their position.
- The 2080-IQ4-OB4 terminal block (two columns of five: I-00 to I-03, IC, O-00 to O-03, OC) is labelled by assumption;
  the plug-in installation sheet is needed.
- Lamps with no tag: LOCK (not used), IN 10 and 11, terminals 10 to 17. POWER and the ENET MS / NS / LNK lamps are
  implied by the module connection.
- Not yet tested: the live COMM LOSS look (the link was up when verified; same code as the rack) and real touch hardware.

Source of truth: `docs/safety-relay-3d.md`.
