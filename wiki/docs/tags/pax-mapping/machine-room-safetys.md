---
title: Machine Room SAFETYS Lamps
sidebar_label: 14 Machine Room SAFETYS
sidebar_position: 15
description: The eight Digitals behind the Machine Room SAFETYS widget (FIRE, RDISKS, MR AD, VL AD, alarm light / circuit, Reset / Silence) and what they reference.
sources:
  - docs/pax-mapping/14-machine-room-safetys.md
last_verified: 2026-10-23
---

# Machine Room SAFETYS Lamps

Source doc: `docs/pax-mapping/14-machine-room-safetys.md`. The **SAFETYS** box on `/machine-room`
(`02_Components/02_Widgets/Safetys`) is not a device UDT: it reads eight `_Root/Digital` instances in
`[default]Boars_Head/GrovePort/Machine Room/Digitals` ([page](../reference/devices/machine-room-digitals.md)), whose
`Value` is a **read-only reference** to a live PLC member.

![Machine Room page with the SAFETYS box](/img/tags/machine-room-page.png)

| Instance | `Value` references (read only) | FT evidence |
|---|---|---|
| `FIRE` | `[default]_RCP1_/Program:RCP_Alarm_Circuit/FD_Alarm` | SAFETYS "FIRE" (`Program:RCP_Alarm_Circuit.FD_Alarm`) |
| `RDISKS` | `[default]_RCP1_/Program:RCP_Alarm_Circuit/PS_Alarm` | SAFETYS "RDISKS" |
| `MR AD` | `Machine Room/Detectors/MR-AD1/DIn/Alm_TgtDisagree` | SAFETYS "MR AD" (`AD_MR1`) |
| `VL AD` | `Machine Room/Detectors/VL-AD/DIn/Alm_TgtDisagree` | SAFETYS "VL AD" (`AD_VL`) |
| `Alarm Light` | `[default]_RCP1_/Controller:Global/Alarm_Light/Sts_Out` | P_DOut `Alarm_Light` (Reset lamp) |
| `Alarm Circuit` | `[default]_RCP1_/Controller:Global/Alarm_Circuit/Sts_Out` | P_DOut `Alarm_Circuit` (horn / Silence lamp) |
| `Alarm Reset` | `[default]_RCP1_/Controller:Global/ALARM/HMI_Reset` | FT RESET button writes `ALARM.HMI_Reset` |
| `Alarm Silence` | `[default]_RCP1_/Controller:Global/ALARM/HMI_Silence` | FT SILENCE button writes `ALARM.HMI_Silence` |

These are the only places the HMI reads `_RCP1_` directly; the referenced `_RCP1_` tags keep their values because the
references subscribe them. The MR EF / BR EF fans in the same widget are the [exhaust fans](exhaust-fans.md).

## Reset / Silence

As on FT: **RESET** shows while `Alarm_Light.Sts_Out` is on, **SILENCE** while `Alarm_Circuit.Sts_Out` is on; a click
sets the bit to one (`setToOne`, no confirm). The click first checks `shared.PlcWriteLock.writeAllowed`: while
`[default]_Config/PlcWriteLock/Locked` is true (it is) it shows the **"PLC Writes Locked"** alert and writes nothing;
otherwise it writes through `shared.Audit.writeTag(<tag>, True)` (guarded again). Verified by code review only: both
buttons are hidden (light and horn off), and no click was attempted.

## MR AD / VL AD Lamps

They follow `AD_MR1.Alm_TgtDisagree` / `AD_VL.Alm_TgtDisagree` exactly like FT (`Cfg_HasTgtDisagreeAlm` = 1 on these
two, so this is the PLC's own alarm). Live both 0 = green (FT lime). Like FT, in alarm the lamps **blink red / yellow**
(style class `status-dot-blink`; to change the blink, edit that class in Project Browser > Perspective > Stylesheet).

## Not Mapped (Nothing To Map)

- Production / FCM line KPIs (`Production/FCM/**`, memory placeholders): the FCM line is not on RCP1; out of scope in
  local Groveport mode.
- `Overview/*` instances: HMI bookkeeping.
- The legacy `Freezer/UnderfloorTemp` / `SuperChill/UnderfloorTemp` memory tags were deleted (nothing read them).

When `_RCP1_` is retired, `FIRE` / `RDISKS` / `Alarm Light` / `Alarm Circuit` / Reset / Silence must be repointed to
OPC atomics or a small alarm-circuit device first.
