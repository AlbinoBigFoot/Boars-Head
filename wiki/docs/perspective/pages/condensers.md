---
title: Condensers
sidebar_position: 5
description: The /condensers page - evaporative condensers EC-1A / EC-1B with their fans, sump pumps, CSV tank, make-up valves, level switches and the discharge sequence.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Condensers/Utility/Overview/view.json"
last_verified: 2026-10-24
---

# Condensers

The condenser area: the two evaporative condensers EC-1A and EC-1B (two fan motors each), the three condenser sump
pumps, the condenser sump vessel (CSV) with its make-up water valves and level switches, the main hot gas valve,
the outside air temperature and the High Stage Discharge sequence.

![Condensers](/img/perspective/condensers.png)

| | |
|---|---|
| Route | `/condensers` (title "Condensers") |
| View | [`00_Pages/Groveport/Condensers/Utility/Overview`](../reference/views/00-pages/groveport/condensers/utility/overview.md) |
| View param | `tagPath` = `[default]Boars_Head/GrovePort/Condensers` |
| Nav | Groveport > Condensers; Devices > Condensers / Pumps / Valves / Sensors / Tanks / Level Switches / Sequences under it |
| Device pages | `/condensers/condenser-fans`, `/condensers/pumps`, `/condensers/valves`, `/condensers/sensors`, `/condensers/tanks` (see [Device List Pages](./device-lists.md)) |

## What It Shows

| On the page | Component | Tag (under `[default]Boars_Head/GrovePort/Condensers/`) |
|---|---|---|
| EC-1A, EC-1B with fan state words | [`Condenser`](../reference/views/02-components/01-devices/condenser.md) | `Condensers/EC-1A`, `Condensers/EC-1B` (each fan is a P_Motor, for example `CD1A_FAN1` in the PLC) |
| HSD-PT3 (discharge pressure) | `Sensor` | the Machine Room sensor `[default]Boars_Head/GrovePort/Machine Room/Sensors/HSD-Discharge Pressure` (static param) |
| OUTSIDE AIR TEMP | label tile (click = Sensor faceplate) | `Sensors/Outside Air Temp/AIn/Val` |
| MAIN HG SV, CSV MAKEUP SV, CSV MAKEUP BACKUP SV | `SolenoidValve` | `Valves/Main HG CV6`, `Valves/Main MW CV25`, `Valves/Backup MW CV26` |
| CSV level | `Tank` | `Tanks/CSV` (analog level only) |
| RS-LVL-OL2, RS-LVL-OL3, RS-LLCO2 | `OverviewStatusTile` | `LevelSwitches/<name>` (DiscreteInput, tile reads `<name>/DIn/Sts`) |
| Sump Pump 1-3 | `Pump` | `Pumps/Sump Pump 1` ... |
| TSV vessel | `VesselGeneric` | drawing only |
| Discharge SP | button | `Sequences/HSD`: opens the DischargeSequence faceplate (1180 x 740) |

The piping (TSR, TSS, HPL, HSD, CWR, WATER) is drawn with flex containers and labels; the user draws and adjusts
it in the Designer.

## Key Bindings

```python
# root/Canvas/Discharge-SP  onActionPerformed
tagPath = '[default]Boars_Head/GrovePort/Condensers/Sequences/HSD'
title = 'High Stage Discharge'
Navigation.Faceplate.openFaceplate('seq-fp-%s' % tagPath, tagPath, '01_Popups/00_Faceplates/DischargeSequence',
    False, title, 1180, 740, {'title': title})
```

The condenser fans have the shared P_Intlk `EC1_INTLK` (L5X routine `Condensers/Interlocks`), so their faceplates
keep the Interlocks tab (see [Faceplates](../faceplates.md#the-interlocks-tab-rule)).

With the PLC link down the fan, pump and valve graphics show COMM LOSS (red) and the values show the gray dash
(see [Comm Loss And Value Quality](../../features/comm-loss-quality.md)).

The Machine Room page links here twice: the CONDENSERS button and the HSD pressure box.
