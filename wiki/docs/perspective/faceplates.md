---
title: Faceplates
sidebar_position: 4
description: The BH faceplate shell and its tabs, how faceplates open, the Interlocks tab rule, value quality, write paths and the PLC write lock, and the PLC rack pop-out cards.
sources:
  - docs/faceplates.md
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Faceplate/view.json"
  - "gateways/standard/data/projects/BH/ignition/script-python/Navigation/Faceplate/code.py"
  - "gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/01_Popups/00_Faceplates/Alerts/Alert/view.json"
  - "docs/plc-write-lock.md"
last_verified: 2026-10-24
---

# Faceplates

A **faceplate** is the popup that opens when you click a device: its status, commands, configuration, interlocks,
trend and alarms. All faceplates live under `01_Popups/00_Faceplates/` (and only there). Most devices use one
shared tabbed **shell**; a few have their own popup.

![Pump faceplate, Controls tab](/img/perspective/faceplate-pump-controls.png)

## The Shell (`01_Popups/00_Faceplates/Faceplate`)

[Reference page](./reference/views/01-popups/00-faceplates/faceplate.md). Default size 560 x 656.

```text
root (bg-component container-card faceplate faceplate-tabs-vertical)
  Header   Title (device label), WebGui button (compressors), Close X
  Content
    Tabs   Controls | Configuration | Interlocks | Trend | Alarm Configuration | Alarms   (older shell: Discrete Inputs, no longer used by tanks)
    Body   EmbeddedView  (props.path bound: selected tab + deviceType -> a tab body view)
```

**Params:** `tagPath` (the UDT instance), `deviceType` (`Compressor`, `Pump`, `Valve`, `Sensor`, `ExhaustFan`,
`Evaporator`, `CoolingTower`, `Tank`, `SuctionSequence`), `webGuiUrl`, `show*` flags per tab, `hiddenFrom*` lists
(comma separated member paths to leave out of a tab; a trailing `/` matches a folder), `initialTab` and `popupId`.

**Tab bodies** are chosen by one expression on `Body/EmbeddedView.props.path`:

| Tab | View (`01_Popups/00_Faceplates/_Assets/...`) |
|---|---|
| Controls | `<Device>/Controls` (Compressor, SuctionSequence, Pump, ExhaustFan, Valve, Tank, Sensor, Evaporator, CoolingTower) |
| Configuration | `<Device>/Configuration` for Valve, Pump, Evaporator, Compressor, Tank, Sensor; otherwise the generic `Configuration/Configuration` (browses the instance's `Cfg_*` members) |
| Interlocks | `<Device>/Interlocks` for Valve, Pump, Evaporator, Compressor; otherwise `Interlocks` |
| Discrete Inputs | `DiscreteInputs` (only `deviceType = Tank`) |
| Trend | `Trend` (the device's historized members, `shared.FaceplateTrend`) |
| Alarm Configuration | `AlarmConfiguration` (`AlarmConfigurationRow` per alarm) |
| Alarms | `<Device>/Alarms` for Valve, Pump, Sensor; otherwise `Alarms` |

| Configuration | Interlocks | Alarms |
|---|---|---|
| ![Configuration](/img/perspective/faceplate-pump-configuration.png) | ![Interlocks](/img/perspective/faceplate-pump-interlocks.png) | ![Alarms](/img/perspective/faceplate-pump-alarms.png) |

**Which tabs show.** `custom.tagFlags` (expr-struct) ANDs each `show*` param with what the device has, and
`custom.visibleTabCount` sizes the tab buttons. `initialTab` (set from `showFaceplate(initialTab=...)`) selects a tab
in the root's `onStartup`; the Interlocks button on a CG page and the Tank Overview's pump buttons use it.

**Tabs are vertical** (`custom.verticalTabs = true`, the `faceplate-tabs-vertical` class) on the left, as in the
screenshots. While the Trend tab is selected the root adds `faceplate-trend-wide` so the popup widens.

## Device-Specific Popups

| Popup | Used for | Notes |
|---|---|---|
| `TankOverview` (1100 x 760) | Tanks (HTR, HPR, LTR, CSV) | Redesigned 2026-10-24 (`fp-*` style classes). Header "&lt;TANK&gt; Tank" with a level-state chip (or a red "Comm Loss" chip). Tabs Overview, Configuration, Interlocks (only tanks with pumps), Trend, Alarm Configuration, Alarms. The **Overview** has a Vessel Level card on the left (PV + unit, state pill, gauge with HH / H / L / LL markers at their real heights, mode, Lock Operator, Reset / Ack) and on the right **Level Switches** (the same read-only `OverviewStatusTile` tiles as the Machine Room page; a click opens the DI faceplate), **Pressures** (pumps and suction) and **Recirculator Pumps** (lead pump, start pressure, one card per pump with an Interlocks button that opens the Pump faceplate on Interlocks and an Open Faceplate button). Cards hide when the tank has no such parts (HPR shows the gauge and its one switch). |
| `DiscreteInput` (600 x 600) | Level switches, AD / FD lamps, rupture disks | Redesigned 2026-10-24. P_DIn: a Status tab (Current State card, Input card with PV From Input / Source / Substitute Value, Alarm card with Target Disagree and Reset / Ack), a Configuration tab (Input Processing: Debounce; Engineering and Options rows hidden without `Engineering/View`), then Alarm Configuration and Alarms. The title is `Cfg_Label` with the description as a muted subtitle; the state chip is green at the normal state, red otherwise, and a red "Comm Loss" chip replaces it while the link is down. |
| `SuctionSequence` (820 x 700), `DischargeSequence` (1180 x 740) | HSS / LSS suction, HSD discharge | Compressor sequencing set points. |
| `Interlock` | `InterlockButton` clicks | Wraps `_Assets/InterlockPanel` (P_Intlk conditions, first out, bypass). |
| `PlcRack/CardDetail` | PLC rack pop-out | See below. |
| `Compressor`, `Pump`, `SolenoidValve`, `Evaporator`, `Sensor`, `Tank`, `ExhaustFan`, `CoolingTower`, `SolenoidValve3Way` | Nav tree faceplate leaves (`data.viewPath`) | Thin wrappers that embed the shell with their `tagPath`. |
| `AdhocTrend`, `AdhocTrendConfig` | The trend faceplate | See [Trending](./pages/trending.md). |
| `Alerts/Alert` | Confirm and message dialogs (`shared.Alerts.showAlert`) | Popup id `alertDialog`. |
| `Alerts/ContextMenu`, `Alerts/Menu` | Right-click menus | |
| `Alerts/OutOfService` | The Out Of Service memo dialog | See [Out Of Service Log](./pages/out-of-service.md). |

![Tank Overview faceplate (values gray because the SecureLink is down)](/img/perspective/faceplate-tank-overview.png)

![Discrete Input faceplate, Status tab (rupture disk)](/img/perspective/faceplate-di-status.png)

Faceplate rules baked in: every PLC member is read once into a gated view custom prop (`if(isGood(tag(p)), tag(p), null)`)
so a bad or stale member shows the gray dash, never a red error overlay (this covers the Interlocks panel, Configuration, Controls, Alarms and Modes tabs too, so with the PLC link down the faceplate shows dashes instead of red errors); a PLC limit of +/-1.5e38 ("no limit") is
treated as null; every command goes through the guarded path (`shared.Alerts.confirmApplyWrite`, which refuses while the
PLC write lock is on); DI edits need `Engineering/Edit`, tank commands need Maintenance; Lock / Unlock use the real
`Mode/OCmd_AcqLock` / `Mode/OCmd_UnlockRel` members. Source of truth: `docs/faceplates.md`.

## How Faceplates Open

Always through the project scripts, never with a bare `system.perspective.openPopup` in a view:

| Call | Use |
|---|---|
| `shared.Alerts.showFaceplate(tagPath, deviceType, webGuiUrl, title, show*..., width, height, hiddenFrom*..., initialTab)` | Opens the shell. Applies per-type defaults (for Valve it hides the command / status members from Configuration). |
| `Navigation.Faceplate.openFaceplate(id, tagPath, view, modal, title, width, height, params)` | Opens any faceplate view. **Checks `Faceplates/Open` first** (`shared.Security.require`) and returns `False` without it. Draggable, resizable, viewport-bound, no native close icon (the view's own X closes it via `popupId`). |
| `Navigation.Faceplate.openDevice(tagPath, title)` | Picks the faceplate from the instance's UDT type (`Devices/Tank` -> TankOverview, `Devices/DiscreteInput` -> DiscreteInput, sequences -> their popups, the shell for Pump, Compressor, Valve, Sensor, ExhaustFan, Evaporator, CoolingTower). Used by nav leaves and table rows. |

Device components (`02_Components/01_Devices/*`) call one of these from their root `onClick`. The popup id includes
the tag path (for example `nav-fp-<tagPath>`, `ev-fp-<tagPath>`), so a second click on the same device refocuses
its popup instead of opening another, and different devices open side by side.

A session without `Faceplates/Open` (Read Only) gets no faceplates: the click does nothing, and the components
hide their hover outline (`session.custom.CanOpenFaceplates`).

## The Interlocks Tab Rule

The Interlocks tab shows **only when the device has an interlock object** (user decision 8.1, 2026-10-23,
`docs/pax-mapping/16-user-answers-2026-10-23.md`):

- the shell's `tagFlags.showInterlocks` reads the instance member `ShowInterlocks` (true when the device's `Intlk`
  part, a P_Intlk, is enabled) and is ANDed with the `showInterlocks` param;
- valves keep the tab (their P_ValveSO has its own interlock / bypass members);
- sensors (P_AIn) and exhaust fans (P_DIn) have none, so no tab (`NO_INTERLOCKS = ('Sensor',)` in
  `Navigation.Faceplate`);
- the condenser fans and pumps read the shared P_Intlk `EC1_INTLK`, so they keep it;
- cooling towers keep it by type.

The Interlocks tab body is `_Assets/InterlockPanel` for pumps and compressors: "P_Intlk - Interlocks With First
Out", one row per condition (green check or red cross), a Reset button, and a Maintenance section with **Enable
Bypass** checkboxes. The condition texts come from the PLC (`Cfg_CondTxt`).

## Value Quality (Gray Italic Dash)

A value that is missing, null or not Good never shows `null`, a red binding overlay or a misleading number. The
shared value elements show an **em dash in gray italic** (style class `value-bad`: `color: var(--neutral-60)`,
`font-style: italic`) instead:

- elements: `03_Elements/01_Status/_Assets/Numeric` (AnalogValue), `00_Control/AnalogInput`, `TimeInput`,
  `StringInput`, `_Assets/Configuration/ConfigField`, and the table cells `03_Elements/03_Table/{Numeric, StateText,
  Boolean}` ;
- PlantPAx's "no limit" value (+/-1.5e38) counts as no value too;
- **loading:** a ConfigField shows a single gray dash until its first value arrives, and icon checkboxes are
  indeterminate, so nothing flashes a wrong state while a slow PLC tag subscribes (first values on `[RCP1]` can take
  several seconds).

The "is it good" test used by those elements is an expression, for example:

```js
{view.params.tagPath} != '' && coalesce(try(isGood(tag({view.params.tagPath})), false), false)
  && !isNull(try(tag({view.params.tagPath}), null))
  && coalesce(try(abs(toFloat(tag({view.params.tagPath}))) < 1e30, true), true)
```

`value-alarm` (`color: var(--error)`, bold) is the matching class for a value in alarm.

## Write Paths And The PLC Write Lock

Every write from a faceplate goes through one of three gateway-side functions, which audit it and enforce the
locks:

1. **Configuration values** (setpoints, timers, `Cfg_*`): the input element calls
   `shared.Alerts.confirmApplyWrite(label, tagPath, newValue, oldValue)`. That opens the "Apply configuration?"
   dialog (old and new value, in words for enum members via `shared.Enums.describe`). **Apply** calls
   `shared.Audit.writeTag(...)`, which writes the tag and an OpsAudit entry; **Cancel** writes nothing. Equal old and
   new values open no dialog.
2. **Commands and modes** (Start, Stop, Reset, Oper / Prog / Maint): `shared.ValveCommands.*` (`startPump`,
   `setPumpMode`, `setMode` ...).
3. **Out Of Service:** only through `shared.OutOfService` (memo dialog). `shared.Audit.writeTag` refuses direct
   `.Enabled` writes from sessions.

Guards, in order:

- `session.custom.ReadOnly` (no `Faceplates/Operate`): command scripts return at once, inputs are disabled.
- **PAX-mapped devices are read only in the HMI.** Command and mode scripts start with
  `if self.view.custom.pax: return  # pax-bindings: live PLC object, read only`. `custom.pax` is the device's PAX
  part key (`Motor`, `Valve`, `Comp`, `CG` ...; see [Bindings](./bindings.md#pax-member-paths)), so once a device type
  is mapped to the live controller its buttons do nothing until the commands are released.
- **PLC write lock (tag level):** while `[default]_Config/PlcWriteLock/Locked` is `true` (the default),
  `shared.PlcWriteLock.writeAllowed(tagPath)` is false for anything that resolves to `[RCP1]`, and
  `confirmApplyWrite`, `Audit.writeTag` and `ValveCommands._writeRaw` refuse with a "PLC Writes Locked" message. The
  same boolean also sets `readOnly` on every RCP1 tag. While unlocked, the header shows a red **PLC Writes
  Unlocked** pill (`00_Pages/00_Docked/_Assets/PlcWriteLock`).
- **OPC UA server block:** the device `RCP1` grants no Write or Call to any role, so even an unlocked tag write is
  refused by the gateway's OPC UA server (the HMI shows the old value). Both layers must be open for a write to
  reach the PLC.

The full lock design and how to unlock for testing are on [Deployment](../deployment/index.md) and in
`docs/plc-write-lock.md`. Nobody unlocks either layer outside an agreed test.

## PLC Rack Pop-Out Cards

On the [PLC Rack](./pages/plc-rack.md) page, **Open In Faceplate** calls
`shared.PlcRack.openCard(sitePath, member, slot, kind, title, viewportW, viewportH)`. It opens
`01_Popups/00_Faceplates/PlcRack/CardDetail` with the id `plcRackCard-<member>` (one per card, so several cards
open side by side), draggable and resizable, placed bottom-centre over the detail area at a staggered offset per
slot. The popup embeds the same `02_Components/03_PLC/ModuleDetail` the page uses, with `inPopup = true` to hide
the pop-out button. It does not use `showFaceplate`, because that opens the device shell with one fixed id.

![PLC rack pop-out](/img/perspective/plc-rack-popout.png)

## Building Or Changing A Faceplate

- Design it in Figma first and export the graphics as SVG, see [Figma Workflow](./styling/figma-workflow.md).
- Tab bodies are views under `_Assets/<Device>/`; add the device type to the shell's `props.path` expression and
  to `Navigation.Faceplate.SHELL_TYPES` / `DEVICE_POPUPS` if it is new.
- Copy an existing faceplate view of a similar device as the starting point (Designer: right-click the view >
  Duplicate), then rename it under `01_Popups/00_Faceplates/`.
- Keep every write on the paths above, and gate controls on `session.custom.Permissions` (see
  [Security In The UI](./security-ui.md)).
