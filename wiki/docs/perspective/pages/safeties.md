---
title: Safety Relay And Rupture Disks
sidebar_position: 7
description: The /safety-relay page (HLCO safety relay drawing) and the /rupture-disks page (34 rupture disk pressure switches).
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/01_Devices/SafetyRelay/view.json"
last_verified: 2026-10-24
---

# Safety Relay And Rupture Disks

Two Machine Room safety pages, both reached from the Machine Room page and from Groveport > Machine Room >
Devices in the nav.

## Safety Relay (`/safety-relay`)

A **3D View** button opens the interactive 3D model at `/safety-relay/3d`; see [Safety Relay 3D View](../../features/safety-relay-3d.md).

![Safety Relay](/img/perspective/safety-relay.png)

| | |
|---|---|
| Route | `/safety-relay` |
| View | [`00_Pages/Groveport/Machine Room/Utility/SafetyRelay/Overview`](../reference/views/00-pages/groveport/machine-room/utility/safetyrelay/overview.md) |
| Component | [`02_Components/01_Devices/SafetyRelay`](../reference/views/02-components/01-devices/safetyrelay.md), drawn at a fixed 536 x 404 and zoomed to the viewport by the stylesheet class `safety-relay-zoom` (`zoom: 1.25`, `1.6` on screens of 1600 x 860 and up) |
| Tag | `[default]Boars_Head/GrovePort/Machine Room/SafetyRelays/HLCO Safety Relay` (UDT `Devices/SafetyRelay`) |
| Changing it | Edit the component in the Designer; the relay graphic is an SVG exported from Figma ([Figma Workflow](../styling/figma-workflow.md)) |

The drawing is the 440C-CR30 HLCO safety relay with its 440C-ENET module and 2080-IQ4-OB4 plug-in, built from the
FT `(STELLAR)SafetyRelay` display. Inputs 0 and 1 are labelled "In 0: LSS HLCO" and "In 1: HSS HLCO" (params
`input0Name` / `input1Name`).

- Point LEDs read the module input members `<relay>/IO/Pt00Data` ... `Pt21Data`, `IO/Plugin2InPt0xData`,
  `IO/Plugin2OutPt0xData`, the run mode `IO/RunMode` and the safety output flags `IO/SOF05` / `SOF06`.
- The **ENET comm LED** flashes green while the connection is good (`IO/ConnectionFaulted` false; the
  stylesheet class `led-comm-flash` runs a 1 s blink, off under `prefers-reduced-motion`) and goes static red on
  comm loss.
- Like every device graphic, the relay and the rupture disk tiles follow the quality rule: with the PLC link down they
  show COMM LOSS or the gray dash instead of the last values ([Comm Loss And Value Quality](../../features/comm-loss-quality.md)).
- The relay is a module-defined type in the PLC (`[RCP1]SafetyRelay:I.*`), so it is not in the L5K UDT export; the
  UDT members are defined by hand on the `Devices/SafetyRelay` UDT.

## Rupture Disks (`/rupture-disks`)

![Rupture Disks](/img/perspective/rupture-disks.png)

| | |
|---|---|
| Route | `/rupture-disks` |
| View | [`00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview`](../reference/views/00-pages/groveport/machine-room/utility/rupturedisks/overview.md) |
| Tiles | 34 x [`OverviewStatusTile`](../components.md#overviewstatustile) |
| Tags | `[default]Boars_Head/GrovePort/Machine Room/RuptureDisks/<PSnn name>` (UDT `Devices/DiscreteInput`), backed by the PLC P_DIn array `PS[n]` |
| Changing it | Copy a tile on the page, rename it `<PSnn name>` and point its `tagPath` at the instance (Tag Browser, UDT `Devices/DiscreteInput`) |

Each tile is one rupture disk pressure switch (PS01 EC1A-1 ... PS33 HTR-VESSEL-2), laid out like the FT
`(STELLAR)RDisks` display in five columns. The tile text is the switch's `Cfg_0StText` / `Cfg_1StText` chosen by its
state; a click opens the DiscreteInput faceplate. The Machine Room page opens this page from its Rupture Disks
button and from the RDISKS lamp in the Safetys widget.
