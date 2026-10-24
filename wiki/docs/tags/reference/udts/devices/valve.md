---
title: "Devices/Valve"
sidebar_label: "Valve"
description: "UDT definition Devices/Valve: valve"
generated: true
---

:::note

:::
# UDT `Devices/Valve`

valve

Valve HMI layer; valveType SO/MO/MP/C selects command UI (SO=Cmd 0/1, MO=Cmd\_Open/Cmd\_Close, MP/C=Cmd\_Position)

| | |
|---|---|
| Designer location | Tag Browser &gt; default &gt; Data Types &gt; Devices &gt; Valve |
| Tag path | `[default]_types_/Devices/Valve` |
| File | `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json` |
| Inherits from | - |
| Inherited by | - |
| Own members | 6 (1 atomic, 5 nested UDT, 0 folders) |
| Status | in use |

## Parameters

| Parameter | Data type | Default | Defined |
|---|---|---|---|
| `PlcDevice` | String | - | own |
| `ValveTag` | String | - | own |
| `IntlkTag` | String | - | own |

Parameters are referenced in member settings as `{Name}` and are set per instance (Designer: right-click the instance > Edit Tag > Parameters).

## Structure

```mermaid
flowchart LR
  n0["Devices/Valve"]
  style n0 stroke-width:3px
  n0 -- "Cmd_Position" --> n1["_Root/Analog"]
  n0 -- "_Alarms" --> n2["Config/_Alarms"]
  n0 -- "valveType" --> n3["_Root/String"]
  n0 -- "Valve" --> n4["PLC/P_ValveSO"]
  n0 -- "Intlk" --> n5["PLC/P_Intlk"]
```

## Members

| Member | Data type | Source | Tag group | Read only | History | Units / format | Alarms | Documentation |
|---|---|---|---|---|---|---|---|---|
| `Cmd_Position` | UDT | nested [\_Root/Analog](../root/analog.md) | | | | | | MP/C position command 0-100% |
| `_Alarms` | UDT | nested [Config/\_Alarms](../config/alarms.md) | | | | | | |
| `valveType` | UDT | nested [\_Root/String](../root/string.md) | | | | | | |
| `Valve` | UDT | nested [PLC/P\_ValveSO](../plc/p-valveso.md) | | | | | | Live PLC object \[\{PlcDevice\}\]\{ValveTag\} (PLC/P\_ValveSO); enabled on mapped instances only |
| `Intlk` | UDT | nested [PLC/P\_Intlk](../plc/p-intlk.md) | | | | | | Live PLC object \[\{PlcDevice\}\]\{IntlkTag\} (PLC/P\_Intlk); enabled on mapped instances only |
| `ShowInterlocks` | Boolean | expr `if(isGood({[.]Intlk/Sts_IntlkOK}), ((trim(coalesce({[.]Intlk/Cfg_Cond…` (full below) | | yes | | | | Derived from the PLC part (read only): if(isGood(\{\[.\]Intlk/Sts\_IntlkOK\}), ((trim(coalesce(\{\[.\]Intlk/Cfg\_CondTxt/Cfg\_CondTxt\_0\_\}, '')) != '' &amp;&amp; left(trim(coales… |

<details>
<summary>Full expressions / references (1)</summary>

**`ShowInterlocks`** (expr)

```
if(isGood({[.]Intlk/Sts_IntlkOK}), ((trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_0_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_0_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_1_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_1_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_2_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_2_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_3_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_3_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_4_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_4_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_5_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_5_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_6_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_6_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_7_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_7_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_8_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_8_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_9_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_9_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_10_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_10_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_11_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_11_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_12_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_12_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_13_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_13_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_14_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_14_}, '')), 17) != 'Enter Description') || (trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_15_}, '')) != '' && left(trim(coalesce({[.]Intlk/Cfg_CondTxt/Cfg_CondTxt_15_}, '')), 17) != 'Enter Description')), true)
```


</details>

## Nested UDTs

| Member | Type | Parameter bindings | Default state |
|---|---|---|---|
| `Cmd_Position` | [\_Root/Analog](../root/analog.md) | - | enabled |
| `_Alarms` | [Config/\_Alarms](../config/alarms.md) | - | enabled |
| `valveType` | [\_Root/String](../root/string.md) | - | enabled |
| `Valve` | [PLC/P\_ValveSO](../plc/p-valveso.md) | `DeviceName = {PlcDevice}; TagPrefix = {ValveTag}` | disabled |
| `Intlk` | [PLC/P\_Intlk](../plc/p-intlk.md) | `DeviceName = {PlcDevice}; TagPrefix = {IntlkTag}` | disabled |

`disabled` parts subscribe nothing until an instance enables them (instance override `enabled: true`). See the device instance pages for which instances enable which part.

## Alarms

_No alarms defined on this type._

## Used By

Nested in: [Devices/Evaporator](evaporator.md) (as `Valves/Liquid SV`), [Devices/Evaporator](evaporator.md) (as `Valves/Suction SV`), [Devices/Evaporator](evaporator.md) (as `Valves/Bleed SV`), [Devices/Evaporator](evaporator.md) (as `Valves/Hot Gas SV`)

4 direct instance(s):

| Instance | Instance page |
|---|---|
| `[default]Boars_Head/GrovePort/Condensers/Valves/Main HG CV6` | [Condensers/Valves](../../devices/condensers-valves.md) |
| `[default]Boars_Head/GrovePort/Condensers/Valves/Main MW CV25` | [Condensers/Valves](../../devices/condensers-valves.md) |
| `[default]Boars_Head/GrovePort/Condensers/Valves/Backup MW CV26` | [Condensers/Valves](../../devices/condensers-valves.md) |
| `[default]Boars_Head/GrovePort/Machine Room/Valves/Main Liq SV` | [Machine Room/Valves](../../devices/machine-room-valves.md) |
