---
title: Machine Room
sidebar_position: 4
description: The /machine-room page - receivers, recirculator pumps, compressors, suction sequences, level switches, safeties, LTU and AD tiles.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/Overview/view.json"
  - "docs/machine-room-level-switches.md"
last_verified: 2026-10-24
---

# Machine Room

The ammonia machine room drawn as a P&ID-style page: the high temperature receiver (HTR), high pressure receiver
(HPR) and low temperature receiver (LTR), the four recirculator pumps, the five screw compressors, the suction
headers, the tank level switches, the Safetys widget, the liquid transfer unit (LTU) and the ammonia detector tiles.

![Machine Room](/img/perspective/machine-room.png)

| | |
|---|---|
| Route | `/machine-room` (title "Machine Room") |
| View | [`00_Pages/Groveport/Machine Room/Utility/Overview`](../reference/views/00-pages/groveport/machine-room/utility/overview.md) |
| View param | `tagPath` = `[default]Boars_Head/GrovePort/Machine Room` (the area folder; every device path is built from it) |
| Parts | Level switch tiles, LTU + AD tiles, Reset / Silence buttons, the scale-to-fit box and the device click wiring are all components of this view |
| Nav | Groveport > Machine Room (Devices underneath it lists every device) |

## What It Shows

| On the page | Component | Tag (under `[default]Boars_Head/GrovePort/Machine Room/`) | Click |
|---|---|---|---|
| HTR, HPR, LTR | `Tank` | `Tanks/HTR`, `Tanks/HPR`, `Tanks/LTR` | Tank Overview faceplate (pumps, start pressure, trend) |
| HTLR-Pump 1/2, LTLR-Pump 1/2 | `Pump` | `Pumps/HTLR-Pump 1` ... | Pump faceplate |
| COMP 1, 4, 5, 6, 7 | `Compressor` (CP / SV mode, FLA %, SVP %) | `Compressors/COMP n` | Compressor faceplate (with the compressor's web GUI link) |
| HSS-PT2, HSL-PSIG, LSL-PSIG, LSS-PT1 | `Sensor` | `Sensors/HSS-Pumps Pressure` ... | Sensor faceplate |
| MAIN LIQ SV | `SolenoidValve` | `Valves/Main Liq SV` | Valve faceplate |
| OPL 1 (two symbols) | `SolenoidValve` | none yet (drawn without a `tagPath`) | nothing |
| HSD pressure box (136.1 PSIG) and CONDENSERS | `NavButton` | `Sensors/HSD-Discharge Pressure/AIn/Val` | Opens `/condensers` |
| HTR / LTR / HPR level switches (9 tiles) | `OverviewStatusTile` | `Tanks/<tank>/DI_HLCO`, `DI_HiLevel`, `DI_OPL`, `DI_LoLo` | DiscreteInput faceplate |
| SAFETYS (MR AD and VL AD blink red / yellow in alarm via the `status-dot-blink` style class; RDISKS, FIRE, MR EF, BR EF, Reset, Silence) | `02_Components/02_Widgets/Safetys` | `Digitals/*`, `ExhaustFans/*` | RDISKS opens `/rupture-disks`; Reset / Silence write the alarm system bits |
| LTU (Transfer Counts, Alarm Setpoint) | `LTU` | LTU instance | Alarm Setpoint is an `AnalogInput` (confirm dialog); **Reset Count** button (see below) |
| MR-AD1, VL-AD, MASTER-AD1 | `OverviewStatusTile` | DiscreteInput instances | DiscreteInput faceplate |
| HSS Suction SP, LSS Suction SP | buttons | `Sequences/HSS`, `Sequences/LSS` | SuctionSequence faceplate |
| Rupture Disks | button | | Opens `/rupture-disks` |

The level switch tiles follow the FT `(STELLAR)MachineRoom` display. The text is `Cfg_State0Txt` / `Cfg_State1Txt`
(for example OK / HI / ALARM / LO), the box turns dark when `Sts_PV` is true, and it shows a dash on bad quality.
They read memory DiscreteInput members until those are mapped to the PLC; see `docs/machine-room-level-switches.md`.

**Reset / Silence** in the Safetys widget are the only plain command buttons on this page. They are audited writes
(`shared.Audit.writeTag`) to the alarm system bits, are visible only while the alarm light / circuit is on, and
need `AlarmSummary/Acknowledge` and a session that is not read only.

## Key Bindings

Every device embed builds its path from the page param:

```js
// root/Canvas/HTR props.params.tagPath
{view.params.tagPath} + "/Tanks/HTR"
```

The HSD box label reads the discharge pressure null-safely and falls back to an em dash:

```js
coalesce(try(numberFormat(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure/AIn/Val'), '#,##0.0')
  + ' ' + coalesce(try(tag({view.params.tagPath} + '/Sensors/HSD-Discharge Pressure/AIn/Val.EngUnit'), ''), ''),
  null), '—')
```

The suction set-point buttons open the sequence faceplate directly (a script action, because it passes a size and
title):

```python
tagPath = '[default]Boars_Head/GrovePort/Machine Room/Sequences/HSS'
title = 'High Stage Suction'
Navigation.Faceplate.openFaceplate('seq-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/SuctionSequence',
    False, title, 820, 700, {'title': title})
```

## Changing It

- Move components in the Designer (the canvas is a coordinate container). If the drawing's overall extent changes,
  resize the scale-to-fit box (the `content` container the scale expression reads) to match the new extent.
- To add a tile, copy an existing one (for example an `OverviewStatusTile`), rename it and set its params; see
  [Machine Room Level Switches](../../features/machine-room-level-switches.md#how-to-change-it).
- Click wiring: a device graphic opens its faceplate through `Navigation.Faceplate.openFaceplate` in its `onClick`
  handler; copy the handler from a neighbouring device.
- The dark theme is a good check that new pieces use theme classes, not fixed colours:

![Machine Room, dark theme](/img/perspective/machine-room-dark.png)

## LTU Card And Reset Count

The LTU card (`02_Components/01_Devices/LTU`, embedded on this page) shows, top to bottom: the centred title, the
**Transfer Count** (red when it is at or above the alarm setpoint), the **Alarm Setpoint** with its pencil, and the
centred **Reset Count** button; the discrete input beside it opens the Discrete Input faceplate. The card is 162 px
high so the button row fits, and the ammonia detector tiles below it sit lower to match.

**Reset Count** sends the PLC's own reset (a momentary 1 that the PLC clears itself) through the LTU's
`PlcResetCount` member. As on the FactoryTalk screen it is **one click with no confirmation dialog**; the write is
still checked in order (write lock first, then permissions) and logged. It does nothing, and is shown disabled with a
tooltip, when:

- the PLC link is down (the count is not Good, see [Comm Loss And Value Quality](../../features/comm-loss-quality.md));
- the user lacks the permissions `Faceplates/Operate` **and** `LTU/Command` (both are checked on the gateway too);
- the [PLC write lock](../../features/plc-write-lock.md) is on (`_Config/PlcWriteLock/Locked` = true), which is the
  normal state. The reset therefore only works after the project owner unlocks PLC writes.

The write is logged in the [Audit Log](../../features/audit-log.md). A live test is pending the PLC link.

To move or resize parts of the card: Designer > open the Machine Room page > select the LTU embed and edit its size in
the Property Editor, or open the `LTU` component view to change its rows.
