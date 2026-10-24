---
title: Alarms
sidebar_label: Alarms
sidebar_position: 4
description: Where Ignition alarms are defined (UDT members only), priorities, the PLC alarm-enable gating, associated data, the alarm journal, the alarm pages and the CG Too Hot / Too Cold behaviour.
sources:
  - gateways/standard/data/config/resources/core/ignition/alarm-journal/**/config.json
  - gateways/standard/data/config/resources/core/ignition/general-alarm-settings/**/config.json
  - gateways/standard/data/projects/BH/ignition/script-python/shared/Alarms/code.py
last_verified: 2026-10-23
---

# Alarms

The BH HMI uses **Ignition alarms** (configured on tags, evaluated by the gateway, shown in the alarm status table,
the header bell and the device badges, stored in the journal). The PLC has its own PlantPAx alarm logic (`Alm_*`
bits, `Cfg_Has*Alm` enables); the Ignition alarms are configured to **follow** it, not to add new thresholds.

Every alarm definition in the tag configuration is listed, generated, in the [Alarm Index](reference/alarm-index.md).

## Rule: Alarms Live On UDT Members, Never On Instances

User rule (2026-09-25): every alarm is created on the member **inside the UDT definition**, so every instance of a
device type behaves the same and a new device gets its alarms automatically. An alarm on an instance or a plain tag
is a bug (the Alarm Index lists them in a second table, which should be empty).

### How To Add Or Change An Alarm

1. Designer > Tag Browser > **UDT Definitions** tab. Open the type that holds the member:
   - the PLC library members (`PLC/P_Motor`, `P_AIn`, `P_DIn`, `P_ValveSO`, `Screw_Compressor`, `CG_RL_Evap`,
     `CR30_Input`);
   - a read-only controller-tag atomic of a `Devices` type (today only LTU `PlcCountAlarm`);
   - the PLC rack alarms (Module Fault, Controller Communication Lost, Major / Minor / I/O Fault, Not In Run Mode) are
     on the `PLC/Modules/*` and `PLC/Controllers/CompactLogix_5370` types.
2. Select the member, open the tag editor (right-click > **Edit Tag**) and go to the **Alarming** section. Add or edit
   the alarm: name, mode, setpoint, priority, display path, and the `enabled` expression (gated on the PLC object's
   own enable, for example `coalesce({[.]Cfg_HasHiAlm}, false)`).
3. Add the associated data `Site`, `Area`, `Device` to the alarm so the Alarm Status table and the journal can filter
   it. Copy it from a neighbouring alarm.
4. Click **OK**. Every instance of the type follows the definition.
5. Don't alarm two members that read the same PLC bit. Never put an alarm on an instance.

The faceplate **Alarm Configuration** tab shows these Ignition alarm definitions (not PLC alarm setpoints).

## The Alarms

| Type (member) | Alarm | Priority | Enabled when |
|---|---|---|---|
| P_Motor `Alm_IOFault` | IO Fault | Critical | always |
| P_Motor `Alm_FailToStart` / `Alm_FailToStop` | Fail To Start / Fail To Stop | High | always |
| P_Motor `Alm_IntlkTrip` | Interlock Trip | Medium | always |
| P_AIn `Sts_Fail` | Input Failure | High | `Cfg_HasFailAlm` = 1 |
| P_AIn `Sts_HiHi` / `Sts_LoLo` | High-High / Low-Low | High | `Cfg_HasHiHiAlm` / `Cfg_HasLoLoAlm` = 1 |
| P_AIn `Sts_Hi` / `Sts_Lo` | High / Low | Medium | `Cfg_HasHiAlm` / `Cfg_HasLoAlm` = 1 |
| P_DIn `Sts_TgtDisagree` | Target Disagree | Medium | `Cfg_HasTgtDisagreeAlm` = 1 |
| P_DIn `Sts` | State Alarm (display path = `Description`) | High | parameter `AlarmOnSts` = 1 (only the tank pump alarm DIs) |
| P_ValveSO `Alm_IOFault`, `Alm_FullStall`, `Alm_TransitStall` | IO Fault, Full Stall, Transit Stall | High | always |
| P_ValveSO `Alm_IntlkTrip` | Interlock Trip | Medium | always |
| Screw_Compressor `Failed` | Failed | Critical | always |
| Screw_Compressor `Cutout` | Cutout | High | always |
| Screw_Compressor `Alm` | Compressor Alarm | Medium | always |
| Screw_Compressor `Comm` | Comm Error | Low | always |
| CR30_Input `MajorFault` / `ConnectionFaulted` | Safety Relay Major Fault / Comm Loss | High | always |
| CR30_Input `SOF01ResetRequired` / `SOF02ResetRequired` | LSS / HSS HLCO Output 0 / 1 Reset Required | Medium | always |
| Devices/LTU `PlcCountAlarm` | Transfer Count High | Medium | always |
| PLC/Modules `Faulted` (all cards) | Module Fault | High | always |
| PLC/Controllers/CompactLogix_5370 | Controller Communication Lost (`CommLoss`, 12 s delay), Major Fault | Critical | always |
| PLC/Controllers/CompactLogix_5370 `IOFault`, `NotRun` / `MinorFault` | Controller I/O Fault, Not In Run Mode / Minor Fault | High / Low | always; gated on `Connected` |

All are `WhenTrue` alarms on a Boolean member that the PLC computes. Priorities match the old HMI.

## Follow The PLC Alarm Enables (FT Parity)

PlantPAx objects have per-instance alarm enables (`Cfg_HasHiAlm`, `Cfg_HasLoLoAlm`, `Cfg_HasTgtDisagreeAlm` ...): the
plant chose, for each transmitter or input, which alarms exist. The old FactoryTalk HMI only alarmed where these are
on. The first version of the library alarms fired regardless, and raised alarms FT never showed (for example LTR
Low / Low-Low, where `LT_LVL` has every alarm disabled in the PLC, and six Target Disagree alarms).

Since 2026-10-23 (user decision N2) each P_AIn / P_DIn alarm has an **enabled expression** on the PLC enable next to
it in the same UDT:

```text
enabled = coalesce({[.]Cfg_HasHiAlm}, false)
```

The enable members are polled in the `PAX_Config` group (Direct, 30 s), so the gating works with no faceplate open.
A bad or missing enable counts as off. Result: active Groveport alarms went from 13 to 3 (the CG Too Hot / Too Cold bits no longer
alarm, see below). Motor, valve, compressor and relay alarms already alarm on the PLC's own `Alm_*` /
fault bits.

## Associated Data: Site, Area, Device

Every alarm gets three associated data properties from the tag path, so the alarm table and filters know where it is
without per-alarm setup:

```text
Site   = try(split({PathToTag}, '/')[1, 0], '')   -> GrovePort
Area   = try(split({PathToTag}, '/')[2, 0], '')   -> Machine Room
Device = try(split({PathToTag}, '/')[4, 0], '')   -> HTLR-Pump 1
```

(for `[default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 1/Motor/Alm_IOFault`). That is why devices must
follow the `Boars_Head/<Site>/<Area>/<Type>/<Device>` layout ([Tags](index.md#the-device-tree-convention)).

## Out Of Service

Taking a device **Out Of Service** (only through `shared.OutOfService`, with a memo) disables the whole UDT instance
(`Enabled = false`), so its alarms stop with it; there is no per-alarm enable for it. See
[Features](../features/index.md).

## Device Badges, Colors And The Bell

Each device UDT nests `Config/_Alarms`, which reads the instance's built-in **Alarm Metrics** (active, unacknowledged,
highest priority) and maps the highest priority to `_Color` / `_Icon` through `[default]_Config/Colors/Alarms/*` and
`_Config/Icons/Alarms/*`, with `_Flash` driven by `_Config/Flash`
([_Root, Config And Overview](udts/root-and-config.md#config_alarms)). The device tiles, the faceplate alarm frame and
the header bell use these. Row colors of the alarm tables are CSS tokens (`--alarm-critical` #E22028, `--alarm-high`
#EC8629, `--alarm-medium` #F5E11B, `--alarm-low` #916AAD, darker `-ack` variants for acknowledged rows).

Acknowledge from a faceplate: `shared.Alarms.acknowledgeForTag(tagPath, ...)` acknowledges the unacknowledged alarms of
that device (source filter on the device path).

## Alarm Pages

| Page | Route | View |
|---|---|---|
| Alarm Status (live) | `/alarms` | `00_Pages/Boars Head/Alarms/Summary` (built-in Alarm Status Table) |
| Alarm Journal (history) | `/alarms/journal` | `00_Pages/Boars Head/Alarms/Journal` (built-in Alarm Journal Table) |

Both have **Device Type** and **Area** multi-select filters; `shared.Alarms.sourceFilter(deviceTypes, areas)` builds
the source wildcard (OR within one dropdown, AND across them, for example `*/Machine Room/*Pumps*`). Nav: Groveport >
Operations > Alarm Status / Alarm Journal. View details: [Perspective](../perspective/index.md).

## The Alarm Journal

Gateway: **Config > Alarming > Journal**, profile **`MSSQL`** (resource `ignition/alarm-journal/MSSQL`):

| Setting | Value |
|---|---|
| Type | Database (datasource `ignition`, the MSSQL container) |
| Tables | `alarm_events`, `alarm_event_data` |
| Store and forward | on |
| Minimum priority stored | Diagnostic (everything) |
| Stores shelved events, enabled-change events | yes |
| Static / dynamic associated data | stored |
| Pruning | off |

The journal table on `/alarms/journal` queries this profile by name; don't create a second journal profile. General
alarm settings (Config > Alarming > General): startup suppression 10 s, live event limit 5.

## CG Zone Air Temp Too Hot / Too Cold

The CG zone-temperature alarms now come **only from the ZAT `P_AIn` Hi / HiHi / Lo / LoLo alarms**, gated on the
PLC enables. The CG bits `CG[n].TooHot` / `TooCold` **no longer alarm**; they only turn the value red. They are
**real PLC conditions**: the PLC sets `TooHot` when the zone air temp reaches setpoint + 3 °F (`ZAT_HiHi = Cfg_ZoneAirTemp + 3`)
and holds it while ZAT stays above the setpoint (latched); `TooCold` is the mirror image. The HMI invents no
threshold. While either bit is on, the zone air temp value is shown **red** (style class `value-alarm`, theme
`--error`) on the CG tiles, the CG page and the evaporator faceplate; a bad value stays gray.

![CG-E4 Zone Air Temp Too Hot](/img/tags/cg-e4-too-hot.png)

Live 2026-10-23: CG-E4 Too Hot (36.48 °F against 33 + 3), CG-A1 Too Cold (32.78 °F against 38 - 3), CG-G5 Too Cold
(latched); those three showed red. The P_AIn ZAT alarm limits are wider and were not active. See [CG Evaporators](pax-mapping/cg-evaporators.md#too-hot--too-cold-and-the-red-value).
