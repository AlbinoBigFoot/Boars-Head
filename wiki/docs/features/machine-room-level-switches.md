---
title: Machine Room Level Switches
sidebar_position: 14
description: The nine tank level-switch / safety tiles on the Machine Room page (HLCO, HI LEVEL, OPL, LOLO), their data source and faceplate.
sources:
  - docs/faceplates.md
  - docs/machine-room-level-switches.md
last_verified: 2026-10-23
---

# Machine Room Level Switches

## What it does

The Machine Room page (`/machine-room`) shows the **tank level switches** (FactoryTalk `GO_P_DIn` objects) as small
status tiles, exactly where FactoryTalk's `(STELLAR)MachineRoom` display has them. These are the vessel safeties:

| Tile | Meaning (FT caption) | Member under `[default]Boars_Head/GrovePort/Machine Room/Tanks/` | FT tag |
|---|---|---|---|
| `DI-HTR-HLCO` | HTR high level cut out | `HTR/DI_HLCO` | `[RCP1]HTR_HLCO` |
| `DI-HTR-HiLevel` | HTR HI LEVEL | `HTR/DI_HiLevel` | `[RCP1]HTR_HIHI` |
| `DI-HTR-OPL` | HTR OPL | `HTR/DI_OPL` | `[RCP1]HTR_OPL` |
| `DI-HTR-LoLo` | HTR LOLO LEVEL | `HTR/DI_LoLo` | `[RCP1]HTR_LOLO` |
| `DI-LTR-HLCO`, `-HiLevel`, `-OPL`, `-LoLo` | the same four on the LTR | `LTR/DI_*` | `[RCP1]LTR_*` |
| `DI-HPR-LoLo` | HPR-LO LEVEL | `HPR/DI_LoLo` | `[RCP1]HPR_LOLO` |

## How to read a tile

- Status text: the switch's state-0 text while the input is false (for example "OK"), its state-1 text (or the
  tile's `alarmText`: "HI", "ALARM", "LO") when true. The value box turns dark when the input is true (FT's black
  value box) and shows a dash on bad quality.
- Click: opens the **Discrete Input** faceplate (`01_Popups/00_Faceplates/DiscreteInput`, needs `Faceplates/Open`);
  its title comes from the tag's `Cfg_Label`.

The **Tank Overview faceplate shows the same switches** (redesign 2026-10-24): its Overview tab has a **Level Switches**
card with the same `OverviewStatusTile` tiles (HTR / LTR: HLCO, HI LEVEL, OPL, LOLO LEVEL; HPR: LO LEVEL). They are read
only, a click opens the DI faceplate, and a tile appears only when the tank's P_DIn part is enabled. There is still no
Discrete Inputs tab or section on the tank faceplate.

![Tank faceplate with the Level Switches card](/img/perspective/faceplate-tank-overview.png)

## Where the pieces live (developers)

| Piece | Where |
|---|---|
| Tiles | 9 embeds of `00_Pages/Groveport/Utility/OverviewStatusTile` on `00_Pages/Groveport/Machine Room/Utility/Overview`, params `label`, `diPath` (the old `DI_*` member path, used for the faceplate), `tagPath` (the value read), `okValue false`, `alarmText`; 100 x 44 each |
| Data | since the PAX mapping, `tagPath` reads the nested PlantPAx part of the tank, for example `[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR/HlcoDIn/Sts` (live PLC value, read only) |
| Positions | The tiles' positions on the page are set in the Designer; the Tank Overview faceplate has no Discrete Inputs section or tab |

## Data source and PLC mapping

The first version (2026-10-22) read **memory** DiscreteInput members (`<tank>/DI_*/Sts_PV`, not live). The PAX
mapping of 2026-10-23 nests PlantPAx `P_DIn` parts (`HlcoDIn`, `HiHiDIn`, `OplDIn`, `LoLoDIn`) in the tank UDT,
maps them to the controller tags above, and the tiles' `tagPath` now reads `<tank>/<Part>/Sts` (checked on the page
2026-10-23); the PAX cleanup removed the old flat `DI_*` sub-devices from `Devices/Tank`. See
`docs/pax-mapping/02-tanks.md` and [Tags](../tags/index.md) for the bindings. The table above lists the original
`DI_*` member names because the tiles' `diPath` still uses them.

:::warning Before relying on the faceplate writes
The Discrete Input faceplate has Reset / Ack, Substitute PV, Source, Debounce and `Cfg_*` text fields. On PLC-mapped
members these are PLC writes, and substituting an HLCO PV bypasses a safety cut-out. They are blocked today by the
[PLC Write Lock](./plc-write-lock.md) and by PLC-mapped devices being read only; gate them to Engineering (or keep
them read only) before the lock is ever lifted.
:::

## How To Change It

All steps are Designer edits; save, then test in a session.

- **Move or resize a tile:** Project Browser > Perspective > Views > `00_Pages/Groveport/Machine Room/Utility` >
  `Overview`; select the `DI-<tank>-<switch>` embed and change its position. Don't make a tile narrower than 90 px:
  "HTR-LOLO LEVEL" needs 89.
- **Change a tile's caption, alarm text or data path:** select the embed and edit its params: `label`, `alarmText`,
  `okValue`, `diPath` (used for the faceplate) and `tagPath` (the value read).
- **Add a tile:** copy an existing `OverviewStatusTile` embed on the page, rename it `DI-<tank>-<switch>` and set the
  params. The tank's UDT needs the matching `P_DIn` part (`HlcoDIn`, `HiHiDIn`, `OplDIn`, `LoLoDIn`) enabled on the
  instance (Tag Browser, the tank instance).
- **The faceplate card:** Views > `01_Popups/00_Faceplates/Tank` (Overview tab, Level Switches card), and
  `01_Popups/00_Faceplates/DiscreteInput` for the click-through.

## Known limitations

- The HPR tile caption follows FT ("HPR-LO LEVEL") but the tag label says "HPR-LOLO LEVEL", so the popup title
  differs.
- Member names differ between our UDT (`Cfg_State0Txt` / `Sts_PV`) and the PLC P_DIn (`Cfg_0StText`, `.Sts`); if a
  mapping renames members, update the tile bindings.
- Do not make the tiles narrower: "HTR-LOLO LEVEL" needs 89 of the 90 px.
