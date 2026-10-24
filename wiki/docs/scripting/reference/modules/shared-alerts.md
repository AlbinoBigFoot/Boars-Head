---
title: "shared.Alerts"
sidebar_label: "shared.Alerts"
description: "Script module shared.Alerts: every function, its docstring and its callers."
generated: true
custom_edit_url: null
---

:::note

:::

**Source:** `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`  
**Lines:** 323. **Functions:** 9. **Called as:** `shared.Alerts.<function>(...)`

## What the source says

```text
Alert Popup Script

This script allows for easy interaction with the alert popup view.  It
allows to repeatable control of the popup

The following functions are available
    * showAlert - Opens the alert popup
    * showAdhocTrend - Opens the AdhocTrend faceplate popup (in-page trending)
    * showAdhocTrendConfig - Opens Trend Configuration beside the AdhocTrend faceplate
    * showFaceplate - Opens the shared tabbed Faceplate shell (deviceType + tabs)
```

## At a glance

| | |
|---|---|
| Ignition APIs used | `system.perspective` |
| Calls modules | [Navigation.Faceplate](./navigation-faceplate.md), [shared.Audit](./shared-audit.md), [shared.Enums](./shared-enums.md), [shared.PlcWriteLock](./shared-plcwritelock.md), [shared.Security](./shared-security.md) |
| Called by modules | [Navigation.Faceplate](./navigation-faceplate.md), [shared.Reports](./shared-reports.md), [shared.Security](./shared-security.md), [shared.TrendContext](./shared-trendcontext.md), [shared.UserAdmin](./shared-useradmin.md) |

<details>
<summary>Module constants (9)</summary>

| Name | Value |
|---|---|
| `POPUP_ADHOC_TREND` | `'AdhocTrend'` |
| `VIEW_ADHOC_TREND` | `'01_Popups/00_Faceplates/AdhocTrend'` |
| `POPUP_ADHOC_TREND_CONFIG` | `'AdhocTrendConfig'` |
| `VIEW_ADHOC_TREND_CONFIG` | `'01_Popups/00_Faceplates/AdhocTrendConfig'` |
| `ADHOC_TREND_WIDTH` | `960` |
| `ADHOC_TREND_HEIGHT` | `780` |
| `ADHOC_TREND_CONFIG_WIDTH` | `340` |
| `ADHOC_TREND_CONFIG_HEIGHT` | `520` |
| `ADHOC_TREND_GAP` | `12` |
</details>

## Functions

| Function | Summary | Callers outside the module |
|---|---|---|
| [`_describe`](#_describe) (internal) | | 0 |
| [`confirmApplyWrite`](#confirmapplywrite) | Confirm before writing a config value. Cancel does not write. | 134 |
| [`promptConfigWrite`](#promptconfigwrite) | Snap the widget back to oldValue, then confirm. Tag writes only on Apply. | 1 |
| [`showAlert`](#showalert) | Opens the alert popup | 38 |
| [`showAdhocTrend`](#showadhoctrend) | Open (or refocus) the Adhoc trending faceplate on the current page. | 2 |
| [`showAdhocTrendConfig`](#showadhoctrendconfig) | Open Trend Configuration as a floating companion to the AdhocTrend faceplate. | 0 |
| [`closeAdhocTrendConfig`](#closeadhoctrendconfig) | Close the companion Trend Configuration popup if open. | 0 |
| [`contextMenuTicketLog`](#contextmenuticketlog) | | 252 |
| [`showFaceplate`](#showfaceplate) | Open the shared tabbed Faceplate shell (Scout-style). | 16 |

### \_describe {#_describe}

```python
def _describe(tagPath, value, enumPath=None)
```
Line 25 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

_No docstring._

Used inside the module by: `confirmApplyWrite`

### confirmApplyWrite {#confirmapplywrite}

```python
def confirmApplyWrite(label, tagPath, newValue, oldValue=None, title='Apply configuration', extraPayload=None, btnTextApply='Apply')
```
Line 32 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

```text
Confirm before writing a config value. Cancel does not write.

No dialog (and no write) if newValue equals oldValue.
```

<details>
<summary>Called from 134 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardControls/Defrost/BtnStartDefrost event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardControls/Defrost/BtnStopDefrost event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardControls/Enable/BtnEnable event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardControls/SetBack/BtnSetback event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Fans/FansSeg/Opt0 event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Fans/FansSeg/Opt1 event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Fans/FansSeg/Opt2 event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Mode/ModeSeg/Opt0 event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Mode/ModeSeg/Opt1 event component.onActionPerformed` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapPanel` | view | `root/CardDefrost/Mode/ModeSeg/Opt2 event component.onActionPerformed` |
| `01_Popups/00_Faceplates/DiscreteInput` | view | `root/Content/Body/Status/Alarm/TargetDisagree/Reset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/DiscreteInput` | view | `root/Content/Body/Status/Input/Source/Source/Input event component.onActionPerformed` |
| `01_Popups/00_Faceplates/DiscreteInput` | view | `root/Content/Body/Status/Input/Source/Source/Substitute event component.onActionPerformed` |
| `01_Popups/00_Faceplates/DiscreteInput` | view | `root/Content/Body/Status/Input/SubstValue/SubstValue/Value0 event component.onActionPerformed` |
| `01_Popups/00_Faceplates/DiscreteInput` | view | `root/Content/Body/Status/Input/SubstValue/SubstValue/Value1 event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root/Fields/PrioritySection/PriorityDropdown binding props.value` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root/Fields/PrioritySection/PriorityDropdown event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root/Fields/SetpointSection/SetpointEntry binding props.value` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root/Fields/TriggerSection/TriggerDropdown binding props.value` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root/Fields/TriggerSection/TriggerDropdown event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/CommandsSection/DefrostRow/BtnStartDefrost event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/CommandsSection/DefrostRow/BtnStopDefrost event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/CommandsSection/EnableRow/BtnEnable event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/CommandsSection/EnableRow/BtnSetBack event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls` | view | `root/CommandsSection/ResetRow/BtnReset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond00/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond00/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond00/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond01/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond01/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond01/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond02/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond02/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond02/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond03/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond03/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond03/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond04/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond04/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond04/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond05/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond05/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond05/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond06/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond06/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond06/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond07/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond07/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond07/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond08/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond08/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond08/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond09/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond09/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond09/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond10/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond10/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond10/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond11/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond11/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond11/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond12/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond12/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond12/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond13/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond13/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond13/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond14/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond14/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond14/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond15/CanBypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond15/MustReset event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page2/Cond15/OkState event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond00/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond01/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond02/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond03/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond04/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond05/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond06/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond07/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond08/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond09/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond10/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond11/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond12/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond13/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond14/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Engineering/Page3/Cond15/HasNav event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Home/StatusRow/BtnReset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond00/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond01/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond02/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond03/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond04/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond05/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond06/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond07/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond08/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond09/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond10/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond11/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond12/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond13/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond14/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root/Content/Body/Maintenance/Bypass/Cond15/Bypass event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root/Left/AinMaint/SetTrack/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root/Right/AinOptions/DefaultMode/DefOper event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root/Right/AinOptions/DefaultMode/DefProg event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root/Right/AinOptions/HasChan/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root/Right/AinOptions/PCmdClear/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root/Right/AinOptions/Subst/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | view | `root/Left/AinMaint/SetTrack/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | view | `root/Right/AinOptions/DefaultMode/DefToggle event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | view | `root/Right/AinOptions/HasChan/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | view | `root/Right/AinOptions/PCmdClear/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | view | `root/Right/AinOptions/Subst/Chk event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/AinHome/ModeRow/BtnLock event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/AinHome/ModeRow/BtnReset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/AinHome/ModeRow/BtnUnlock event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/PumpsSection/LeadRow/Lead1 event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/PumpsSection/LeadRow/Lead2 event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Level/Commands/Lock event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Level/Commands/Reset event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Right/Pumps/LeadPump/Lead/Lead1 event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Right/Pumps/LeadPump/Lead/Lead2 event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root/DeviceBypass/Body/Cmds/BtnBypass event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root/DeviceBypass/Body/Cmds/BtnDisable event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root/DeviceBypass/Body/Cmds/BtnEnable event component.onActionPerformed` |
| `03_Elements/00_Control/AnalogInput` | view | `root/EditValue binding custom.editedValue` |
| `03_Elements/00_Control/MultiStateInput` | view | `root/StateSelect binding props.value` |
| `03_Elements/00_Control/StringInput` | view | `root/EditIcon event dom.onClick` |
| `03_Elements/00_Control/StringInput` | view | `root/EditValue event component.onActionPerformed` |
| `03_Elements/00_Control/TimeInput` | view | `root/EditValue binding custom.editedValue` |
</details>

Used inside the module by: `promptConfigWrite`

### promptConfigWrite {#promptconfigwrite}

```python
def promptConfigWrite(component, propPath, tagPath, label, newValue, oldValue)
```
Line 99 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

```text
Snap the widget back to oldValue, then confirm. Tag writes only on Apply.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` | view | `root/Chk binding props.selected` |

### showAlert {#showalert}

```python
def showAlert(state='info', title='', message='', showCloseBtn=True, btnTextPrimary='', btnTextSecondary='', btnIconPrimary='', btnIconSecondary='', btnIconAlignment='right', btnActionPrimary=None, btnActionSecondary=None, payload={}, overlayDismiss=True)
```
Line 123 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

```text
Opens the alert popup

Parameters
----------
state : str
    Affects styling of the popup.  Options are info, warning, error, success
title : str
    The title to display for the popup.
message : str
    The message to display in the body of the popup
showCloseBtn : bool
    Controls visibility of the close button in the top right corner of the popup
btnTextPrimary : str
    The text to display on the primary button
btnTextSecondary : str
    The text to display on the secondary button
btnIconPrimary : str
        The icon path to display on the primary button
btnIconSecondary : str
        The icon path to display on the secondary button
btnActionPrimary : str
        The message handler to invoke when the primary button is clicked
btnActionSecondary : str
        The message handler to invoke when the secondary button is clicked
btnIconAlignment : str
    The icon alignment inside the primary and secondary buttons
```

<details>
<summary>Called from 38 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpBulk` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpDiscard` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpSave` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler rpSaveConfirmed` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umAdd` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umDelete` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umDiscard` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleDelete` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umRoleSave` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umSave` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler umSelect` |
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | view | `root message handler nrCreateConfirmed` |
| `00_Pages/Boars Head/Operations/_Admin/NewRole` | view | `root/ActionBar/Create event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root/Footer/Bar/ActionBar/Clear event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root/Footer/Bar/ActionBar/Submit event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root/Cycle/Row/Btns/Complete event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root/Footer/Bar/ActionBar/Clear event component.onActionPerformed` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root/Footer/Bar/ActionBar/Submit event component.onActionPerformed` |
| `01_Popups/00_Faceplates/Alerts/ContextMenu` | view | `root/AddToTrend event dom.onClick` |
| `01_Popups/Reports/ReportBuilder` | view | `root/Body/Step4/Rail/Save/Body/TplRow/Delete event component.onActionPerformed` |
| `01_Popups/Reports/_Assets/SavedListRow` | view | `root/Actions/Delete event dom.onClick` |
| `02_Components/01_Devices/LTU` | view | `root/ResetRow/ResetCount event component.onActionPerformed` |
| `02_Components/02_Widgets/Safetys` | view | `root/TopRow/AlarmButtons/Reset event component.onActionPerformed` |
| `02_Components/02_Widgets/Safetys` | view | `root/TopRow/AlarmButtons/Silence event component.onActionPerformed` |
| `03_Elements/00_Control/_Assets/Numeric` | view | `root/NumericEntryField binding props.value` |
| `98_Configuration/IntegrationSection` | view | `root/Body/Buttons/Save event component.onActionPerformed` |
| `98_Configuration/IntegrationSection` | view | `root/Body/Buttons/Test event component.onActionPerformed` |
| `98_Configuration/IntegrationSection` | view | `root/Body/TokenRow/Replace event component.onActionPerformed` |
| `98_Configuration/Integrations` | view | `root/AddRow/Add event component.onActionPerformed` |
| `98_Configuration/TicketLoggerSettings` | view | `root/Content/Destinations/DryRun/Head/Toggle event component.onActionPerformed` |
| `98_Configuration/TicketRouting` | view | `root/Content/ActionBar/Save event component.onActionPerformed` |
| `shared.Reports.open` | script | |
| `shared.Security._deny` | script | |
| `shared.UserAdmin.commit` | script | |
| `shared.UserAdmin.deleteRole` | script | |
| `shared.UserAdmin.deleteUser` | script | |
| `shared.UserAdmin.saveRole` | script | |
| `shared.UserAdmin.saveUser` | script | |
</details>

Used inside the module by: `confirmApplyWrite`

### showAdhocTrend {#showadhoctrend}

```python
def showAdhocTrend()
```
Line 190 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

```text
Open (or refocus) the Adhoc trending faceplate on the current page.

Bottom-right placement matches Ticket Logger / contextMenuTicketLog.
Faceplate embeds Trend in faceplateMode (no tag browser tree); pens come
from ContextMenu Add to trend / session.custom.AdhocTrend.
```

**Callers:**

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/Alerts/ContextMenu` | view | `root/AddToTrend event dom.onClick` |
| `01_Popups/00_Faceplates/Alerts/ContextMenu` | view | `root/OpenTrend event dom.onClick` |

### showAdhocTrendConfig {#showadhoctrendconfig}

```python
def showAdhocTrendConfig()
```
Line 214 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

```text
Open Trend Configuration as a floating companion to the AdhocTrend faceplate.

Non-modal (no viewport dim). Placed immediately left of AdhocTrend using the
same bottom offset. Binds to session.custom.AdhocTrend — closing config does
not close the trend faceplate.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### closeAdhocTrendConfig {#closeadhoctrendconfig}

```python
def closeAdhocTrendConfig()
```
Line 238 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

```text
Close the companion Trend Configuration popup if open.
```

_No caller found in views, scripts, events, WebDev or reports (it may be called by name from the Designer script console or a dynamic string)._

### contextMenuTicketLog {#contextmenuticketlog}

```python
def contextMenuTicketLog(tagPath='', viewName=None)
```
Line 249 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

_No docstring._

<details>
<summary>Called from 252 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `00_Pages/00_Docked/Header` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/Legend` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/Navigation` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/TempNav` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/AlarmNotification` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/BrandLogo` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/ChangeTheme` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/IntegratorContact` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/IntegratorLogo` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/OosNotification` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/User` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/UserRoles&Login` | view | `root message handler ticketLog` |
| `00_Pages/00_Docked/_Assets/UserSettings` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Alarms/Journal` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Alarms/Summary` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Alarms/_Assets/AlarmJournalTable` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Alarms/_Assets/AlarmStatusTable` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Compressors/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Devices/DesignOverview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Devices/DetailsOverview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Devices/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Devices/TypeTable` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/ExhaustFans/Design` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/ExhaustFans/Details` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/ExhaustFans/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/LandingPage/Globe` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/LandingPage/PlantPlaceholder` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Machine Room/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/NoViewPath` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Operations/AuditLog` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Operations/RolesPermissions` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Operations/UserManagement/UserManagement` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Pumps/Design` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Pumps/Details` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Pumps/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Sensors/Design` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Sensors/Details` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Sensors/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Tanks/Design` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Tanks/Details` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Tanks/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Unit/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Valves/Design` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Valves/Details` | view | `root message handler ticketLog` |
| `00_Pages/Boars Head/Valves/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Area/DomainKpis` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Club/Utility/CG-C1` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/CondenserFans/Design` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/CondenserFans/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Pumps/Design` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Pumps/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Sensors/Design` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Sensors/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Tanks/Design` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Tanks/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Valves/Design` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Condensers/Utility/Valves/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Dock/Utility/CG-G1` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Dock/Utility/CG-G2` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Dock/Utility/CG-G3` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Dock/Utility/CG-G4` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Dock/Utility/CG-G5` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Domains/EPMS` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Domains/Production` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Domains/Utility` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/East PH/Utility/CG-E1` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/East PH/Utility/CG-E2` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/East PH/Utility/CG-E3` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/East PH/Utility/CG-E4` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Freezer/Utility/CG-A1` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Freezer/Utility/CG-A2` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Compressors/Design` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Compressors/Details` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Compressors/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/ExhaustFans/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Pumps/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/RuptureDisks/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Sensors/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Tanks/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Machine Room/Utility/Valves/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Operations/Forms/DailyRounds` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Operations/Forms/History` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Operations/Forms/PidVerification` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Operations/Forms/ShiftLog` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Operations/Forms/_Assets/HistoryActions` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Palletizing/Utility/CG-D1` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level1/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level2/Forming` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level2/Kpis` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level2/Packaging` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level2/Prep` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/Handtman` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/Hopper` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/Kpis` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/LazySusan` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/Loaders` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/RollStock` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/ShrinkTunnel` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Production/Level3/VatDumper` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Site/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Site/OverviewClassic` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Site/OverviewExecutive` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/SuperChill/Utility/CG-B1` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/SuperChill/Utility/CG-B2` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Utility/Overview` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Utility/OverviewKpis` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Utility/OverviewStatusTile` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/Utility/OverviewStatuses` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/West PH/Utility/CG-F1` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/West PH/Utility/CG-F2` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/West PH/Utility/CG-F3` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/West PH/Utility/CG-F4` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapDisplay` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapHistory` | view | `root message handler ticketLog` |
| `00_Pages/Groveport/_Shared/CG/AhuEvapStatusBar` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/AdhocTrend` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/AdhocTrendConfig` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Alerts/Alert` | view | `dialog message handler ticketLog` |
| `01_Popups/00_Faceplates/Alerts/ContextMenu` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Alerts/ContextMenu` | view | `root/TicketLogger event dom.onClick` |
| `01_Popups/00_Faceplates/Alerts/OutOfService` | view | `dialog message handler ticketLog` |
| `01_Popups/00_Faceplates/Compressor` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/CoolingTower` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/DischargeSequence` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/DiscreteInput` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Evaporator` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/ExhaustFan` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Faceplate` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Interlock` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Pump` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Sensor` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/SolenoidValve` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/SolenoidValve3Way` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/SuctionSequence` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/Tank` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/TankOverview` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfiguration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/AlarmConfigurationRow` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Alarms` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Configuration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Compressor/Interlocks` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigField` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigSection` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Configuration/Configuration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Configuration/ConfigurationRow` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/CoolingTower/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/DischargeSequence/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/DiscreteInputs` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Configuration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Interlocks` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/ExhaustFan/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/InterlockPanel` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Interlocks` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Modes` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Pump/Alarms` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Pump/Configuration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Pump/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Pump/Interlocks` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Alarms` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Configuration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Sensor/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/SuctionSequence/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Tank/Configuration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Interlocks` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Trend` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Valve/Alarms` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_MO` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_Position` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Valve/Cmd_SO` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Valve/Configuration` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Valve/Controls` | view | `root message handler ticketLog` |
| `01_Popups/00_Faceplates/_Assets/Valve/Interlocks` | view | `root message handler ticketLog` |
| `01_Popups/Reports/ReportBuilder` | view | `root message handler ticketLog` |
| `02_Components/00_Controls/InterlockButton` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/Compressor` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/Condenser` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/CoolingTower` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/Evaporator` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/ExhaustFan` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/LTU` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/Pump` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/SafetyRelay` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/Sensor` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/SolenoidValve` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/Tank` | view | `root message handler ticketLog` |
| `02_Components/01_Devices/VesselGeneric` | view | `root message handler ticketLog` |
| `02_Components/02_Widgets/KPI` | view | `root message handler ticketLog` |
| `02_Components/02_Widgets/MetricCard` | view | `root message handler ticketLog` |
| `02_Components/02_Widgets/Safetys` | view | `root message handler ticketLog` |
| `02_Components/02_Widgets/SiteCard` | view | `root message handler ticketLog` |
| `02_Components/03_PLC/Controller_CompactLogix_5370` | view | `root message handler ticketLog` |
| `02_Components/03_PLC/Module_1769_IA16` | view | `root message handler ticketLog` |
| `02_Components/03_PLC/Module_1769_IF8` | view | `root message handler ticketLog` |
| `02_Components/03_PLC/Module_1769_IQ16` | view | `root message handler ticketLog` |
| `02_Components/03_PLC/Module_1769_OA16` | view | `root message handler ticketLog` |
| `02_Components/03_PLC/Module_1769_OW16` | view | `root message handler ticketLog` |
| `03_Elements/00_Control/AnalogInput` | view | `root message handler ticketLog` |
| `03_Elements/00_Control/AnalogValue` | view | `root message handler ticketLog` |
| `03_Elements/00_Control/MultiStateInput` | view | `root message handler ticketLog` |
| `03_Elements/00_Control/StringInput` | view | `root message handler ticketLog` |
| `03_Elements/00_Control/TimeInput` | view | `root message handler ticketLog` |
| `03_Elements/00_Control/_Assets/Numeric` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/AlarmHeader` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/IconHeader` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Auto` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/DoorStatus` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Exclude` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Faceplate` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Hand` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Interlock` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Maintenance` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/NoMode` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/NotAtSetpoint` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Operator` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/OutOfService` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Override` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Program` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Remote` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Simulate` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/Icons/Stale` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/NotificationIcons/Blank` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/NotificationIcons/CommLoss` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/StatusDot` | view | `root message handler ticketLog` |
| `03_Elements/01_Status/StatusIndicator` | view | `root message handler ticketLog` |
| `03_Elements/03_Table/DeviceLabelAlarmIndicator` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/Trend` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/UserSavedTrendConfig` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/LoadDeleteTrend` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/NamePlot` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/Pen` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/PenColor` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/PenDelete` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/PenEnable` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/PenPlot` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/Plot` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/RemovePlot` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/SaveTrendConfig` | view | `root message handler ticketLog` |
| `98_Configuration/AdhocTrend/_Assets/ToolBar` | view | `root message handler ticketLog` |
| `98_Configuration/ComponentPreview/Condenser-SafetyRelay` | view | `root message handler ticketLog` |
| `98_Configuration/ComponentPreview/VesselGeneric` | view | `root message handler ticketLog` |
| `98_Configuration/TicketLogger` | view | `root message handler ticketLog` |
| `98_Configuration/Tools/L5K/Message` | view | `root message handler ticketLog` |
| `98_Configuration/Tools/L5K/Parser` | view | `root message handler ticketLog` |
| `98_Configuration/Tools/L5K/Tags` | view | `root message handler ticketLog` |
| `shared.TrendContext.menu_action` | script | |
</details>

### showFaceplate {#showfaceplate}

```python
def showFaceplate(tagPath='', deviceType='Compressor', webGuiUrl='', title=None, showControls=True, showConfiguration=True, showInterlocks=True, showTrend=True, showAlarmConfiguration=True, showAlarms=True, width=560, height=656, hiddenFromConfiguration='', hiddenFromTrend='', hiddenFromAlarmConfiguration='', hiddenFromAlarms='', initialTab='')
```
Line 266 of `gateways/standard/data/projects/BH/ignition/script-python/shared/Alerts/code.py`.

```text
Open the shared tabbed Faceplate shell (Scout-style).

Caller show* flags are hints ANDed with Faceplate tagFlags (empty tabs hide).
deviceType selects Controls embeds under 01_Popups/00_Faceplates/_Assets/...
hiddenFrom* are comma-separated paths; entries ending with / match a folder prefix.
initialTab opens on that tab (e.g. 'Interlocks') instead of Controls.
```

<details>
<summary>Called from 16 place(s) outside the module</summary>

| Caller | Kind | Where |
|---|---|---|
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveBleedSV event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveHotGasSV event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveLiquidSV event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Evaporator/Controls` | view | `root/DevicesSection/ValveChips/ValveSuctionSV event dom.onClick` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/PumpsSection/IntlkRow/Pump1Intlk event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/Tank/Controls` | view | `root/PumpsSection/IntlkRow/Pump2Intlk event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Right/Pumps/Cards/Pump1/Buttons/Interlocks event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Right/Pumps/Cards/Pump1/Buttons/Open event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Right/Pumps/Cards/Pump2/Buttons/Interlocks event component.onActionPerformed` |
| `01_Popups/00_Faceplates/_Assets/TankOverview/Overview` | view | `root/Right/Pumps/Cards/Pump2/Buttons/Open event component.onActionPerformed` |
| `02_Components/01_Devices/Condenser` | view | `root/Graphic/Fan1 event dom.onClick` |
| `02_Components/01_Devices/Condenser` | view | `root/Graphic/Fan2 event dom.onClick` |
| `02_Components/01_Devices/Condenser` | view | `root/Graphic/Fan3 event dom.onClick` |
| `02_Components/01_Devices/Pump` | view | `root event dom.onClick` |
| `02_Components/01_Devices/SolenoidValve` | view | `root event dom.onClick` |
| `Navigation.Faceplate.openDevice` | script | |
</details>
