---
title: "Navigation.Faceplate"
sidebar_label: "Navigation.Faceplate"
description: "Script module Navigation.Faceplate: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Faceplate/code.py`  
**Lines:** 84. **Functions:** 2. **Called as:** `Navigation.Faceplate.<function>(...)`

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.perspective`, `system.tag` |
| Calls modules | [shared.Alerts](./shared-alerts.md), [shared.Security](./shared-security.md) |
| Called by modules | [Navigation.Nav](./navigation-nav.md), [shared.Alerts](./shared-alerts.md) |

<details>
<summary>Module constants (3)</summary>

| Name | Value |
|---|---|
| `DEVICE_POPUPS` | `{'Tank': ('tankov-fp-', '01_Popups/00_Faceplates/TankOver...` |
| `NO_INTERLOCKS` | `('Sensor',)` |
| `SHELL_TYPES` | `('Pump', 'Compressor', 'Valve', 'Sensor', 'ExhaustFan', '...` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`openFaceplate`](#openfaceplate) | Open a device faceplate popup (Scout Navigation.Faceplate pattern, BH geometry). | 21 |
| [`openDevice`](#opendevice) | Open the device's faceplate from its tag path alone (nav tree leaves, device tables). Returns False when the | 5 |

### openFaceplate {#openfaceplate}

```python
def openFaceplate(id, tagPath, view, modal=False, title=None, width=560, height=656, params=None)
```
Line 1 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Faceplate/code.py`.

```text
Open a device faceplate popup (Scout Navigation.Faceplate pattern, BH geometry).

params may include tagPath plus unified Faceplate fields:
  deviceType, webGuiUrl, showControls, showConfiguration,
  showTrend, showAlarmConfiguration, showAlarms
```

<details>
<summary>Called from 21 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Unit/Overview` | view | `root/Table event component.onRowClick` |
| `00_Pages/Groveport/Condensers/Utility/Overview` | view | `root/Canvas/Discharge-SP event component.onActionPerformed` |
| `00_Pages/Groveport/Condensers/Utility/Overview` | view | `root/Canvas/OAT event dom.onClick` |
| `00_Pages/Groveport/Machine Room/Utility/Overview` | view | `root/Canvas/HSS-SuctionSP event component.onActionPerformed` |
| `00_Pages/Groveport/Machine Room/Utility/Overview` | view | `root/Canvas/LSS-SuctionSP event component.onActionPerformed` |
| `00_Pages/Groveport/Utility/Overview` | view | `root/Draw/UndFreezer event dom.onClick` |
| `00_Pages/Groveport/Utility/Overview` | view | `root/Draw/UndSuperchill event dom.onClick` |
| `00_Pages/Groveport/Utility/OverviewStatusTile` | view | `root event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_HLCO event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_HiLevel event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_LoLo event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root/Inputs/Grid/DI_OPL event dom.onClick` |
| `02_Components/00_Controls/InterlockButton` | view | `root/Btn event component.onActionPerformed` |
| `02_Components/01_Devices/Compressor` | view | `root event dom.onClick` |
| `02_Components/01_Devices/CoolingTower` | view | `root event dom.onClick` |
| `02_Components/01_Devices/Evaporator` | view | `root event dom.onClick` |
| `02_Components/01_Devices/ExhaustFan` | view | `root event dom.onClick` |
| `02_Components/01_Devices/Sensor` | view | `root event dom.onClick` |
| `02_Components/01_Devices/Tank` | view | `root event dom.onClick` |
| `Navigation.Nav.navigate` | script | |
| `shared.Alerts.showFaceplate` | script | |
</details>

Used inside the module by: `openDevice`

### openDevice {#opendevice}

```python
def openDevice(tagPath, title=None)
```
Line 53 of `gateways/standard/data/projects/BH/ignition/script-python/Navigation/Faceplate/code.py`.

```text
Open the device's faceplate from its tag path alone (nav tree leaves, device tables). Returns False when the
path is not a device with a faceplate (folders, LTU, PLC stand-ins).
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root/Table event component.onRowClick` |
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `root/Content/Detail/Record/Body/Actions/OpenFaceplate event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | view | `root/Columns/Middle/SensorSection/Level event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | view | `root/Columns/Middle/SensorSection/Pressure event dom.onClick` |
| `Navigation.Nav.navigate` | script | |
