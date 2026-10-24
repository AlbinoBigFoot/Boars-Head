---
title: "Devices/Pump"
sidebar_label: "Pump"
description: "UDT definition Devices/Pump: pump"
generated: true
---

:::note

:::
# UDT `Devices/Pump`

pump

pump (Devices HMI layer). Mapped instances nest the live PlantPAx objects read only: Motor=PLC/P\_Motor, Intlk=PLC/P\_Intlk, RunTime=PLC/P\_RunTime, AlmDI=PLC/P\_DIn (parameters PlcDevice + MotorTag / IntlkTag / RunTimeTag / AlmTag). The other members are the HMI layer (PLC/RCP1 stand-ins, SIM, alarms).

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; Devices &gt; Pump |
| Tag path | `[default]_types_/Devices/Pump` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 5 (1 atomic, 4 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `PlcDevice` | String | - | own |
| `MotorTag` | String | - | own |
| `IntlkTag` | String | - | own |
| `RunTimeTag` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## Structure

```mermaid
flowchart LR
  n0["Devices/Pump"]
  style n0 stroke-width:3px
  n0 -- "_Alarms" --> n1["Config/_Alarms"]
  n0 -- "Motor" --> n2["PLC/P_Motor"]
  n0 -- "Intlk" --> n3["PLC/P_Intlk"]
  n0 -- "RunTime" --> n4["PLC/P_RunTime"]
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `_Alarms` | UDT | nested [Config/\_Alarms](../config/alarms.md) | | | | | | |
| `Motor` | UDT | nested [PLC/P\_Motor](../plc/p-motor.md) | | | | | | Live PLC object \[\{PlcDevice\}\]\{MotorTag\} (PLC/P\_Motor); enabled on mapped instances only |
| `Intlk` | UDT | nested [PLC/P\_Intlk](../plc/p-intlk.md) | | | | | | Live PLC object \[\{PlcDevice\}\]\{IntlkTag\} (PLC/P\_Intlk); enabled on mapped instances only |
| `RunTime` | UDT | nested [PLC/P\_RunTime](../plc/p-runtime.md) | | | | | | Live PLC object \[\{PlcDevice\}\]\{RunTimeTag\} (PLC/P\_RunTime); enabled on mapped instances only |
| `ShowInterlocks` | Boolean | expr `((trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_0_}, '')) != '' &&…` (full below) | | yes | | | | Derived from the PLC part (read only): ((trim(coalesce(\{\[.\]Intlk/Cfg\_CondTxt/Cfg\_CondTxt\_0\_\}, '')) != '' &amp;&amp; left(trim(coalesce(\{\[.\]Intlk/Cfg\_CondTxt/Cfg\_CondTx… |

<details>
<summary>Full expressions / references (1)</summary>

**`ShowInterlocks`** (expr)

```
((trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_0_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_0_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_1_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_1_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_2_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_2_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_3_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_3_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_4_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_4_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_5_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_5_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_6_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_6_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_7_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_7_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_8_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_8_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_9_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_9_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_10_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_10_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_11_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_11_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_12_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_12_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_13_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_13_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_14_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_14_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_15_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_15_}, '')), 17) != 'Enter Description'))
```


</details>

## Nested UDTs

| Member | Type | Parameter bindings | Default state |
|---|---|---|---|
| `_Alarms` | [Config/\_Alarms](../config/alarms.md) | - | enabled |
| `Motor` | [PLC/P\_Motor](../plc/p-motor.md) | `DeviceName = {PlcDevice}; TagPrefix = {MotorTag}` | disabled |
| `Intlk` | [PLC/P\_Intlk](../plc/p-intlk.md) | `DeviceName = {PlcDevice}; TagPrefix = {IntlkTag}` | disabled |
| `RunTime` | [PLC/P\_RunTime](../plc/p-runtime.md) | `DeviceName = {PlcDevice}; TagPrefix = {RunTimeTag}` | disabled |

`disabled` parts subscribe nothing until an instance enables them (instance override `enabled: true`). See the device instance pages for which instances enable which part.

## Alarms

_No alarms defined on this type._

## Used By

11 direct instance(s):

| Instance | Instance page |
|---|---|
| `[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 1` | [Condensers/Condensers/EC-1A](../../devices/condensers-condensers-ec-1a.md) |
| `[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 2` | [Condensers/Condensers/EC-1A](../../devices/condensers-condensers-ec-1a.md) |
| `[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1B/Fan 1` | [Condensers/Condensers/EC-1B](../../devices/condensers-condensers-ec-1b.md) |
| `[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1B/Fan 2` | [Condensers/Condensers/EC-1B](../../devices/condensers-condensers-ec-1b.md) |
| `[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 1` | [Condensers/Pumps](../../devices/condensers-pumps.md) |
| `[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 2` | [Condensers/Pumps](../../devices/condensers-pumps.md) |
| `[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 3` | [Condensers/Pumps](../../devices/condensers-pumps.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 2` | [Machine Room/Pumps](../../devices/machine-room-pumps.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Pumps/LTLR-Pump 2` | [Machine Room/Pumps](../../devices/machine-room-pumps.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Pumps/LTLR-Pump 1` | [Machine Room/Pumps](../../devices/machine-room-pumps.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 1` | [Machine Room/Pumps](../../devices/machine-room-pumps.md) |
