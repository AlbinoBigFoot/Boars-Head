---
title: Device List Pages
sidebar_position: 6
description: The device-type pages (/pumps, /valves, /tanks, /sensors, /compressors, /exhaust-fans and the /condensers/* pages) - Details table and Design graphics.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Groveport/Machine Room/Utility/*/Overview/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/Boars Head/Devices/TypeTable/view.json"
last_verified: 2026-10-24
---

# Device List Pages

One page per device type and area lists every device of that type. Each page has a **Details / Design** toggle:
**Details** is a table of live values (one row per device), **Design** shows the device graphics. A row or a
graphic click opens the device's faceplate.

![Pumps](/img/perspective/pumps.png)

## Routes

| Route | Page view (under `00_Pages/Groveport/`) | `tagPath` param (folder) | `typeId` param |
|---|---|---|---|
| `/pumps` | `Machine Room/Utility/Pumps/Overview` | `[default]Boars_Head/GrovePort/Machine Room/Pumps` | `Devices/Pump` |
| `/valves` | `Machine Room/Utility/Valves/Overview` | `.../Machine Room/Valves` | `Devices/Valve` |
| `/tanks` | `Machine Room/Utility/Tanks/Overview` | `.../Machine Room/Tanks` | `Devices/Tank` |
| `/sensors` | `Machine Room/Utility/Sensors/Overview` | `.../Machine Room/Sensors` | `Devices/Sensor` |
| `/compressors` | `Machine Room/Utility/Compressors/Overview` | `.../Machine Room/Compressors` | `Devices/Compressor` |
| `/exhaust-fans` | `Machine Room/Utility/ExhaustFans/Overview` | `.../Machine Room/ExhaustFans` | `Devices/ExhaustFan` |
| `/condensers/condenser-fans` | `Condensers/Utility/CondenserFans/Overview` | `.../Condensers/Condensers` | `Devices/Pump` |
| `/condensers/pumps` | `Condensers/Utility/Pumps/Overview` | `.../Condensers/Pumps` | `Devices/Pump` |
| `/condensers/sensors`, `/tanks`, `/valves` | `Condensers/Utility/<Type>/Overview` | `.../Condensers/<Type>` | matching type |

The page-config route passes no params: each page view carries its folder and type as **param defaults**. That is
why the same body views serve both the Machine Room and the Condensers.

## How A Page Is Put Together

```text
<Type>/Overview  (routed page: title, Details / Design toggle, custom.overviewMode)
  Content  ia.display.view, props.path bound:
    'details' -> 00_Pages/Boars Head/<Type>/Details  -> embeds 00_Pages/Boars Head/Devices/TypeTable
    'design'  -> 00_Pages/Boars Head/<Type>/Design   -> device graphics (02_Components/01_Devices/<Type>)
    anything else -> 00_Pages/Boars Head/NoViewPath
```

Compressors are the exception: their bodies are `00_Pages/Groveport/Machine Room/Utility/Compressors/Details` and
`.../Design` (the Details body still embeds TypeTable).

```js
// <Type>/Overview root/Content props.path
if(coalesce({view.custom.overviewMode},'details')='details','00_Pages/Boars Head/Pumps/Details',
  if(coalesce({view.custom.overviewMode},'details')='design','00_Pages/Boars Head/Pumps/Design',
    '00_Pages/Boars Head/NoViewPath'))
```

The toggle buttons are two flex containers with `onClick` scripts that set `custom.overviewMode`. Their classes
(`theme-toggle-option`, `theme-toggle-option-selected`) come from expressions on the same property.

## The Details Table (TypeTable)

[`00_Pages/Boars Head/Devices/TypeTable`](../reference/views/00-pages/boars-head/devices/typetable.md) is shared by
all types.

- `props.columns` and `props.data` are **expr-struct** bindings over `tagPath`, `typeId` and the folder's cached
  `<folder>/Overview/Instances/Value` document, with script transforms:
  - with a `typeId` (mixed folders) the rows come from `shared.Overview.buildInstancesPayloadForType`;
  - otherwise from the cached `Overview/Instances` document, or a live browse (`shared.Overview.buildInstancesPayload`);
  - columns go through `shared.DevicePages.applyColumns` (plain-English headers, the default column set, hidden
    internals; the list is `shared.DevicePages.COLUMNS`);
  - rows go through `shared.Pax.mapRows`, which points each cell at the PlantPAx member that holds the live value.
- Cells are rendered by the `03_Elements/03_Table/*` views (`Numeric`, `StateText`, `Boolean`): bad or missing
  values show the gray italic dash (see [Bindings](../bindings.md#value-quality)).
- **Device and Status columns (2026-10-24):** the **Device** cell always shows the device name (never `null`), and the
  **Status** column shows the state word (for example Running) and **COMM LOSS** when the device's data is not Good
  (`StateText` has a `commLoss` parameter for state-word columns). This applies to the Pumps, Compressors and Exhaust
  Fans tables. See [Comm Loss And Value Quality](../../features/comm-loss-quality.md).
- `onRowClick` opens the same faceplate the graphic and the nav leaf open:

```python
if tagPath and shared.DevicePages.hasFaceplate(self.view.params.typeId):
    Navigation.Faceplate.openDevice(tagPath)
```

Status-only types (exhaust fans) open nothing; their rows show the default mouse pointer.

## The Design View

`00_Pages/Boars Head/<Type>/Design` embeds one device graphic per instance, sized in the Designer.
Compressor Design embeds carry the Machine Room's `webGuiUrl` params, so the faceplate's web GUI button works
from either page.

## Adding A Device

Create the UDT instance in the right folder (see [Tags](../../tags/index.md)). The Details table picks it up on its
own (live browse, or the next `Overview/Instances` rebuild). The Design view and the nav tree need an embed and a
nav leaf added.
