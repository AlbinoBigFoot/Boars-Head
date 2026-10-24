---
title: CG Pages
sidebar_position: 3
description: The 19 control group pages (/cg-a1 ... /cg-g5) - one shared AhuEvapDisplay body with the valve train, evaporator, control panel and history charts.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/_Shared/CG/**/view.json"
  - "docs/pax-mapping/06-evaporators.md"
last_verified: 2026-10-24
---

# CG Pages

A **CG** (control group) is one evaporator (air handler) with its suction, liquid, hot gas and (on some CGs) bleed
solenoid valves. Groveport has 19: A1-A2 (Freezer), B1-B2 (SuperChill), C1 (Club), D1 (Palletizing), E1-E4
(East PH), F1-F4 (West PH) and G1-G5 (Dock). Every CG has its own route, but they all render **one shared view**.

![CG-E2](/img/perspective/cg-e2.png)

| | |
|---|---|
| Routes | `/cg-a1`, `/cg-a2`, `/cg-b1`, `/cg-b2`, `/cg-c1`, `/cg-d1`, `/cg-e1` ... `/cg-e4`, `/cg-f1` ... `/cg-f4`, `/cg-g1` ... `/cg-g5` |
| Route views | `00_Pages/Groveport/<Area>/Utility/CG-xx`, for example [CG-E2](../reference/views/00-pages/groveport/east-ph/utility/cg-e2.md). Each is a thin page that embeds the shared display with its own `tagPath`. |
| Shared body | [`00_Pages/Groveport/_Shared/CG/AhuEvapDisplay`](../reference/views/00-pages/groveport/shared/cg/ahuevapdisplay.md) |
| Parts | [`AhuEvapPanel`](../reference/views/00-pages/groveport/shared/cg/ahuevappanel.md) (Controls / Defrost / Temperature panel), [`AhuEvapHistory`](../reference/views/00-pages/groveport/shared/cg/ahuevaphistory.md) (charts and status table), `AhuEvapStatusBar` |
| Nav | Groveport > (area) > CG-xx; under it Devices > Evaporator and Devices > Valves open faceplates |

## What It Shows

- **Back To Overview** (to the Utility Overview) and **previous / next** arrows that step through the CGs in
  `custom.cgOrder`.
- **Valve train drawing:** Bleed SV, Suction SV, Hot Gas SV and Liquid SV (`02_Components/01_Devices/SolenoidValve`)
  on the MTRS / HGD / MTRL lines, and the evaporator coil. Each valve shows its state word (OPEN / CLOSED) and
  opens its faceplate. The Bleed valve is drawn only when the CG has one: `custom.hasBleed` reads
  `<cg>/CG/Cfg_HasBleedValve` (live and L5X: C1, D1, G2-G5 have three valves).
- **Evaporator** (`02_Components/01_Devices/Evaporator`) with zone air temp and status; click opens the
  Evaporator faceplate.
- **Panel** (`AhuEvapPanel`):
  - **Controls:** state, Evaporator Enabled, Start / Stop Defrost, Set Back, the Interlocks button
    (`02_Components/00_Controls/InterlockButton`, opens the faceplate on its Interlocks tab).
  - **Defrost:** Defrost Mode (ToD / Cooling / Runtime) and Cycle Fans (Off / Cycle / On) as multi-state buttons,
    the four time-of-day slots (`TimeInput`), and the step timers (Pump Out, Hot Gas, Bleed, Fan Delay).
  - **Temperature:** zone air temp, Target SP, Deadband and the set-back Min / Max / Start / Stop.
- **History** (`AhuEvapHistory`): Zone Air Temp for the last 12 h, Status Hours and Defrost Modes bar charts, and a
  state table (State, Start Time, End Time, Duration). **All of it is real historian data** since 2026-10-24
  (`shared.UtilityMetrics.cg`, one query for `ZAT/Val` and `CG/Sts_State`, cached 3 minutes per CG): the temperature
  line is the Good samples grouped into at most 90 buckets, the hours are per `Sts_State` state, and with no history
  the charts show "No Data" and the table is empty. `Sts_State` history only exists from 2026-10-24 about 13:35, so
  earlier hours are empty. Nothing is synthetic. See
  [Utility Overview](./utility-overview.md#real-data-no-synthetic-values).

## Where The Data Comes From

`tagPath` is the CG UDT instance, for example `[default]Boars_Head/GrovePort/East PH/Utility/CG-E2` (UDT
`Devices/Evaporator`). The panel reads the PlantPAx-mapped members under `<cg>/CG/...`:

| Panel field | Member |
|---|---|
| Defrost Mode | `/CG/Cfg_DefrostStartMode` (words from `[default]_Config/Enums/Evaporator/DefrostStartMode`) |
| Cycle Fans | `/CG/Cfg_CycFans` (`[default]_Config/Enums/Evaporator/CycleFans`) |
| TOD 1st - 4th | `/CG/Cfg_Def1stTOD` ... `/CG/Cfg_Def4thTOD` |
| Step timers | `/CG/Cfg_PumpOut`, `/CG/Cfg_MainHotGas`, `/CG/Cfg_Bleed`, `/CG/Cfg_FanDelay` |
| Target SP / Deadband | `/CG/Cfg_ZoneAirTemp`, `/CG/Cfg_ZoneAirTempDB` |
| Set back | `/CG/SB_Enable`, `/CG/SB_StartTime`, `/CG/SB_StopTime`, `/CG/ZAT_MinSet`, `/CG/ZAT_MaxSet` |
| Commands | `/CG/HMIEnable`, `/CG/HMIStartDefrost`, `/CG/HMIStopDefrost` |
| Too hot / cold | `/CG/TooHot`, `/CG/TooCold` |
| Valves | `<cg>/Valves/Bleed SV`, `/Suction SV`, `/Hot Gas SV`, `/Liquid SV` |
| History | `/HmiStatus` and `/ZAT/Val` through tag history (`shared.Pax.livePath` resolves the live member) |

Since the PAX mapping of 2026-10-23 (`docs/pax-mapping/06-evaporators.md`) these parts are nested controller UDTs
that read the live `[RCP1]` objects of CG number `n`: `CG` = `CG[n]` (site UDT `CG_RL_Evap`), `ZAT` = `CG_ZAT[n]`
(P_AIn), `Intlk` = `CG_Interlock[n]` (P_Intlk), `Fans` = `CG_Fans[n]` (P_Motor) and `FansRunTime`. Before that the
CG values were static placeholders. Every write (setpoint edit, Start Defrost ...) goes through a confirm dialog
and is refused while the PLC write lock is on; see
[Faceplates](../faceplates.md#write-paths-and-the-plc-write-lock). The tag side is on [Tags](../../tags/index.md).

## Key Bindings

```js
// AhuEvapDisplay custom.hasBleed: the PLC flag wins while it is Good, the page param is the fallback
if(coalesce(try(isGood(tag({view.params.tagPath} + '/CG/Cfg_HasBleedValve')), false), false),
   coalesce(try(toBoolean(tag({view.params.tagPath} + '/CG/Cfg_HasBleedValve')), null),
            toBoolean(coalesce({view.params.bleed}, true))),
   toBoolean(coalesce({view.params.bleed}, true)))

// AhuEvapDisplay Bleed SV embed props.params.tagPath
if(!toBoolean(coalesce({view.custom.hasBleed}, true)) || {view.params.tagPath} = "", "",
   {view.params.tagPath} + "/Valves/Bleed SV")
```

**Comm loss.** Every value on the panel and history is quality-gated: a field whose tag is not Good shows the gray dash,
the valves and evaporator show COMM LOSS (red), and the charts say No Data. The CG zone air temperature turns red while
`/CG/TooHot` or `/CG/TooCold` is set (the separate Ignition alarms on those two members were removed on 2026-10-24).
See [Comm Loss And Value Quality](../../features/comm-loss-quality.md).

The field rows (`AnalogInput`, `TimeInput`, `MultiStateInput`) take the member path in `tagPath` and write only
through `shared.Alerts.confirmApplyWrite`. See [Components](../components.md#value-entry-elements).

## Changing It

Change the shared body once and all 19 pages follow. To add a CG: add a thin route view (copy one `CG-xx` view and
set its `tagPath`), a page-config route, the nav node, and the CG in the `cgOrder` list that drives the previous / next arrows (in the shared body's custom properties).
