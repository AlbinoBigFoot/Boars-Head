---
title: Components
sidebar_position: 5
description: The reusable BH Perspective components - device graphics, status tiles, value entry elements, ConfigSection, MultiStateInput and the PLC module views - with their params and usage.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/02_Components/**/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/**/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Utility/OverviewStatusTile/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/_Assets/Configuration/**/view.json"
last_verified: 2026-10-24
---

# Components

Value-bearing components follow the quality rule (red COMM LOSS for a device whose data is not Good, gray dash for a
bad value): see [Bindings](./bindings.md#value-quality) and [Comm Loss And Value Quality](../features/comm-loss-quality.md).

A **component** here means a reusable Perspective view that other views embed (an `ia.display.view` or a flex
repeater instance) and configure through **params**. You place one in the Designer by dragging the view from the
Project Browser onto a container, then set its params in the Property Editor (`props.params`).

Conventions for every component:

- **`tagPath`** is the UDT instance (or member) the component shows, for example
  `[default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 1`. Keep the default **empty** (no Designer placeholder
  paths); an empty `tagPath` renders a blank, harmless component.
- Device graphics read members by appending to `tagPath` in expressions
  (`{view.params.tagPath} + '/Motor/Val_Sts'`). See [Bindings](./bindings.md).
- Every component root has the Ticket Logger right-click menu and the `ticketLog` handler
  ([common patterns](./reference/common-patterns.md)); device graphics add Out Of Service and Add To Trend items.
- Sizes below are each view's default size (`props.defaultSize`).

## Device Graphics (`02_Components/01_Devices/`)

| Component | Size | Params | Notes |
|---|---|---|---|
| [Pump](./reference/views/02-components/01-devices/pump.md) | 96 x 136 | `tagPath`, `faceplate`, `analog` | Running from `Motor/Val_Sts` (2 or 8), run hours from `RunTime/Val_TotRunHrs`, status icon strip (IconHeader), alarm frame from `_Alarms/*`. |
| [Compressor](./reference/views/02-components/01-devices/compressor.md) | 156 x 168 | `tagPath`, `faceplate`, `webGuiUrl` | CP / SV mode labels, FLA % and SVP % strip. `webGuiUrl` is passed to the faceplate's web GUI button. |
| [SolenoidValve](./reference/views/02-components/01-devices/solenoidvalve.md) | 71 x 133 | `tagPath`, `faceplate`, `label`, `feedback`, `orientation` | `orientation` = `{horizontal, horizontalReverse, vertical, verticalReverse}` booleans; change scripts keep exactly one true. OPEN / CLOSED word. |
| [Tank](./reference/views/02-components/01-devices/tank.md) | 168 x 191 | `tagPath`, `faceplate`, `orientation` (`{standard, reverse}`) | Level fill and %, sight glass, level switch marks; click opens TankOverview. |
| [Sensor](./reference/views/02-components/01-devices/sensor.md) | 160 x 100 | `tagPath`, `faceplate`, `label`, `feedback`, `orientation`, `valuePosition` (`auto` / `top` ...) | P_AIn value with units; click opens the shell with `deviceType = Sensor`. |
| [Evaporator](./reference/views/02-components/01-devices/evaporator.md) | 96 x 167 | `tagPath`, `faceplate`, `label`, `navPage` | Zone air temp and status word. With `navPage` a click navigates (Utility Overview); otherwise it opens the faceplate. |
| [ExhaustFan](./reference/views/02-components/01-devices/exhaustfan.md) | 130 x 158 | `tagPath`, `faceplate`, `analog` | Spinning fan (`fan-spin`) while running; status only (P_DIn). |
| [Condenser](./reference/views/02-components/01-devices/condenser.md) | 320 x 190 | `tagPath`, `label`, `fans` (count), `fanMap`, `fanLabels`, `analog`, `analogPath`, `state`, `faceplate` | One fan symbol per fan, each opening its own P_Motor faceplate. |
| [SafetyRelay](./reference/views/02-components/01-devices/safetyrelay.md) | 536 x 404 | `tagPath`, `label`, `state`, `input0Name`, `input1Name` | 440C-CR30 drawing; `state` is a preview value for the Designer. |
| [LTU](./reference/views/02-components/01-devices/ltu.md) | 227 x 126 | `tagPath` | Liquid transfer unit: transfer counts, alarm setpoint (`AnalogInput`), **Reset Count** button (writes `PlcResetCount` -> `[RCP1]HMI_Ltu_Clear`, a momentary 1 that the PLC clears itself; is one click (no confirm dialog), goes through the PLC write lock and the permissions `Faceplates/Operate` and `LTU/Command`, so it is disabled while the lock is on or the quality is bad). |
| [CoolingTower](./reference/views/02-components/01-devices/coolingtower.md) | 100 x 206 | `tagPath`, `faceplate` | Spray animation (`ct-spray-run`) while running. |
| [VesselGeneric](./reference/views/02-components/01-devices/vesselgeneric.md) | 160 x 80 | `tagPath`, `label`, `orientation` (`horizontal` / `vertical`) | Drawing only (TSV on Condensers). |
| `EvapCoilSerpentine` | 45 x 39 | none | Coil drawing on the CG pages. |

**The `faceplate` param** says which faceplate the click opens (for example `Sensor`); `null` or empty means the
component is not clickable. The components open faceplates through `Navigation.Faceplate.openFaceplate` /
`shared.Alerts.showFaceplate` (see [Faceplates](./faceplates.md)).

**Out Of Service.** Each device computes `custom.oos` from `.Enabled`:

```js
// custom.oos
if(coalesce({view.params.tagPath}, '') = '', false, !coalesce(try(toBoolean(tag({view.params.tagPath} + '.Enabled')), true), true))
```

While true, only the OOS icon and `OUT OF SERVICE` show (class `device-oos`).

**Alarm frame.** Indirect tag bindings on `{tagPath}/_Alarms/_Active`, `_ActiveHighPriority` and `_Unack` drive the
frame colour (fixed `--alarm-*` tokens) and the blink.

## OverviewStatusTile

[`00_Pages/Groveport/Utility/OverviewStatusTile`](./reference/views/00-pages/groveport/utility/overviewstatustile.md),
156 x 44 by default (100 x 44 on the Machine Room). A caption over a value box: used for AD / FD lamps, tank level
switches, rupture disks and condenser level switches.

| Param | Meaning |
|---|---|
| `label` | Caption (FT text), bold fs-10, no wrap |
| `diPath` | The DiscreteInput instance (or member) the tile belongs to; opens its faceplate on click |
| `tagPath` | The boolean shown, usually `<diPath>/Sts_PV/Value` or `<diPath>/DIn/Sts` |
| `okValue` | The value that means OK (`false` for alarms) |
| `alarmText` | Fallback text for the alarm state |

The texts come from the instance (`Cfg_0StText` / `Cfg_1StText`), the box goes dark in the alarm state, and a bad
quality shows a dash. Example (Machine Room HTR HLCO):

```json
{"label": "HTR-HLCO", "diPath": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR/DI_HLCO",
 "tagPath": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR/DI_HLCO/Sts_PV/Value",
 "okValue": false, "alarmText": "HI"}
```

## Controls And Widgets

| Component | Params | Use |
|---|---|---|
| [NavButton](./reference/views/02-components/00-controls/navbutton.md) (168 x 36) | `label`, `page`, `viewPath` | A labelled button that navigates (Machine Room CONDENSERS / HSD box). |
| [InterlockButton](./reference/views/02-components/00-controls/interlockbutton.md) (120 x 28) | `tagPath`, `title` | Green "Interlocks OK" / red when not; opens the `Interlock` popup. |
| [Safetys](./reference/views/02-components/02-widgets/safetys.md) (233 x 393) | `mrAdTagPath`, `vlAdTagPath`, `rdisksTagPath`, `fireTagPath`, `mrEfTagPath`, `brEfTagPath`, `resetTagPath`, `silenceTagPath`, `lightTagPath`, `circuitTagPath`, `title` | Machine Room safety lamps, exhaust fans, Reset / Silence. |
| `KPI`, `MetricCard`, `SiteCard` | `title`, `value`, `unit`, `category`, `tagPath` / `siteName`, `region`, `page`, `tagRoot` | Enterprise dashboard widgets. |

## Value Entry Elements (`03_Elements/00_Control/`) {#value-entry-elements}

Used in faceplates and the CG panel; all write only through `shared.Alerts.confirmApplyWrite` (Apply / Cancel
dialog, then `shared.Audit.writeTag`).

| Element | Size | Params | Behaviour |
|---|---|---|---|
| [AnalogInput](./reference/views/03-elements/00-control/analoginput.md) | 372 x 28 | `tagPath`, `label`, `permission`, `faceplate`, `Basis` (`{eu, input, label}` column widths) | Label, value with units, pencil icon. Click the pencil to edit (if `permission` and the session is not read only); the edit closes on a timeout. |
| [MultiStateInput](./reference/views/03-elements/00-control/multistateinput.md) | 372 x 28 | as AnalogInput plus `enumPath`, `confirmLabel` | Dropdown of words for a coded member. Options come from the enum DataSet at `enumPath` (for example `[default]_Config/Enums/Evaporator/DefrostStartMode`, rows with `selectable`). The dropdown snaps back to the tag value; only Apply writes. |
| [TimeInput](./reference/views/03-elements/00-control/timeinput.md) | 372 x 28 | as AnalogInput | Time of day (HH:MM) members such as defrost TOD slots. |
| [StringInput](./reference/views/03-elements/00-control/stringinput.md) | 160 x 28 | `tagPath`, `label`, `permission` | Text members (labels, descriptions). |
| `AnalogValue` | 100 x 20 | `tagPath`, `setpoint`, `permissions`, `spacing` | Inline numeric entry. |

The enum DataSets are the one place mode and state words live (`[default]_Config/Enums/<Group>/<Name>`, columns
`value`, `label`, `short`, `selectable`); expressions read them with `lookup()` and scripts with `shared.Enums`. Don't
add another hard-coded `case()` copy.

## Status Elements (`03_Elements/01_Status/`)

| Element | Params | Use |
|---|---|---|
| `StatusIndicator` | `tagPath`, `outOfService` | Coloured status chip (`Refridgeration_STS sts-<TOKEN>`: COOLING, IDLE, DEFROST, FAULT, COMM LOSS ...). The label derives **COMM LOSS (red)** from the quality of the key member, so a stale value never shows RUN / IDLE. |
| `StatusDot` | `label`, `tagPath`, `okValue` | Small lamp with caption. |
| `AnalogValue` (`_Assets/Numeric`) | `tagPath`, `spTagPath`, `compact`, `spacing`, `forceColor` | Read-only value with units; red when PV is above SP. Shows the gray dash on bad quality. |
| `IconHeader` | `tagPath`, `statusPath`, `hide`, `justify` | Mode / state icon strip from the PLC members (Hand, Maintenance, Override, Program, Operator, No Mode, Interlock, Out Of Service, Simulate, Comm Loss). Only states the PLC UDTs carry are shown. |
| `AlarmHeader` | `tagPath` | Alarm priority icon (`NotificationIcons/Alarms/*`). |
| `Icons/*`, `NotificationIcons/*` | none | The individual icons; the Legend dock explains them. |

Note: `StatusIndicator` and `03_Elements/03_Table/DeviceLabelAlarmIndicator` still carry old placeholder defaults
(`[default]Evaporators/...`) in `tagPath` / `value`; every embed overrides them.

## Configuration Rows (`01_Popups/00_Faceplates/_Assets/Configuration/`)

| View | Params | Use |
|---|---|---|
| [ConfigSection](./reference/views/01-popups/00-faceplates/assets/configuration/configsection.md) (400 x 140) | `title`, `tagPath` (device base), `rowsJson`, `engineering` | A titled card whose rows are a flex repeater of ConfigField. `rowsJson` is a JSON list of `{leaf, kind, label}` (or an explicit `tagPath`); each leaf is resolved to the live PAX member with `shared.Pax.resolve`, so mapped devices read the PLC object. |
| [ConfigField](./reference/views/01-popups/00-faceplates/assets/configuration/configfield.md) (400 x 40) | `tagPath`, `label`, `inputKind` (`checkbox`, `numeric`, ...), `engineering`, `enumPath`, `readOnly` | One configuration row; edits go through `confirmApplyWrite`. Shows a gray dash until its first value arrives. |
| `Configuration` / `ConfigurationRow` | `tagPath`, `hiddenTags` / `highlightRow` | The generic Configuration tab: lists the instance's members. |

```json
{"title": "PLC Timers", "tagPath": "",
 "rowsJson": "[{\"leaf\":\"Min_Runtime_Set\",\"kind\":\"numeric\",\"label\":\"Minimum Runtime\"},{\"leaf\":\"Fail_Timer_PRE\",\"kind\":\"numeric\",\"label\":\"Fail Timer Preset\"}]"}
```

## Table Cell Renderers (`03_Elements/03_Table/`)

A Perspective Table column can render each cell with an embedded view (`render: view`). BH uses `Numeric`,
`Boolean`, `StateText` (`states` map or a number `format`), `CgHit`, `DisplayTrend` and
`DeviceLabelAlarmIndicator`. Each gets the cell `value` (and `row` / `rowData`) as params, and shows the gray dash
for a missing value. `StateText` also has a `commLoss` param: the Details tables set it for state-word columns, so a
column shows **COMM LOSS** instead of a stale word. The Details tables' **Device** cell (`DeviceLabelAlarmIndicator`)
never shows null; it falls back to the device name.

## PLC Module Views (`02_Components/03_PLC/`)

| View | Size | Params | Use |
|---|---|---|---|
| `Controller_CompactLogix_5370` | 114 x 280 | `tagPath`, `member`, `selected`, `state`, `label` | Controller drawing: RUN / OK / NS / LNK LEDs, mode. |
| `Module_1769_IF8`, `_IA16`, `_IQ16`, `_OA16`, `_OW16` | 54 x 280 | `tagPath`, `slot`, `member`, `selected`, `state`, `name` | One card each: OK LED, point LEDs or channel values, door label with the Studio 5000 module name. Fluid SVG (scales with its flex basis). |
| `EndCap_1769_ECR` | 24 x 280 | none | Right end cap. |
| `RackSlot` | 54 x 280 | `tagPath`, `kind` (controller / card / endcap), `catalog`, `slot`, `member`, `selected`, `name` | The flex-repeater cell that picks the drawing by `kind`/`catalog`. Click selects, hover sends `plcRackHover`. |
| `ModuleHover` | 340 x 156 | `tagPath`, `kind`, `title` | The hover card. |
| `ModuleDetail` | 1100 x 284 | `sitePath`, `member`, `inPopup` | The 2-column detail; reads the selected slot from `{sitePath}/Rack` itself. |
| `PointRow` | 520 x 24 | `tagPath`, `point`, `kind` (DI / DO), `description` | One point line in the detail. |

See [PLC Rack](./pages/plc-rack.md).

## Previewing A Component

`98_Configuration/ComponentPreview/*` (for example `Condenser-SafetyRelay`, `VesselGeneric`) are Designer test
pages that place components with sample params, so you can check a component without opening a plant page.
