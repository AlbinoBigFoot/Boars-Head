# RCP1 / COMP 7 OPC tag folder (reference Value test)

Test OPC source folder for `_Root` **reference** `Value` tags on `Devices/Compressor`.

**Convention (corrected 2026-07-31):**

- **`[default]RCP1/...`** = **OPC AtomicTags only** (no `typeId`, no `_Root`).
- **`_Root/*` / `Config/*`** live on **Devices / Units** plant instances.
- Units `sourceTagPath`s point at `[default]RCP1/COMP 7/<member>` (the OPC leaf), **not** `…/Value` under RCP1.

See `.planning/quick/260731-5un-config-interlock-udt-rcp1-udt-root-sweep/ROOT-FIX.md`.

## Paths

| Layer | Path |
|-------|------|
| Ignition OPC tags | `[default]RCP1/COMP 7/<PLC member>` |
| OPC item path | `ns=1;s=[RCP1]COMP[7].<member>` |
| FT View (legacy) | `{[RCP1]COMP[7].<member>}` |
| Devices `_Root` Value | reference → RCP1 path above |

No live OPC device named `RCP1` is configured in this lab gateway yet. Tags are proper OPC
`valueSource` AtomicTags using the Logix-style node id from
`PLC/Screw_Compressor` UDT bindings (`DeviceName=RCP1`, `TagPrefix=COMP[7]`).

## Devices → RCP1 mapping (wired on `Units/Machine Room` / `COMP 7`)

| Devices/Compressor | RCP1 OPC leaf | PLC evidence |
|--------------------|---------------|--------------|
| Alm/Value | Alm | Screw_Compressor.Alm |
| Amps/Value | Amps | Screw_Compressor.Amps |
| AutoEN/Value | AutoEN | Screw_Compressor.AutoEN |
| CP_Mode/Value | CP_Mode | Screw_Compressor.CP_Mode |
| Color/Value | Color | Screw_Compressor.Color |
| Comm/Value | Comm | Screw_Compressor.Comm |
| Cutout/Value | Cutout | Screw_Compressor.Cutout |
| DisP/Value | DisP | Screw_Compressor.DisP |
| FLA/Value | FLA | Screw_Compressor.FLA |
| Fail_Timer_PRE/Value | Fail_Timer/PRE | Screw_Compressor.Fail_Timer.PRE |
| Failed/Value | Failed | Screw_Compressor.Failed |
| Min_Runtime_Set/Value | Min_Runtime_Set | Screw_Compressor.Min_Runtime_Set |
| Rung/Value | Rung | Screw_Compressor.Rung |
| TotalRuntime/Value | TotalRuntime | Screw_Compressor.TotalRuntime (FT Runtimes) |
| SVP/Value | SVP | Screw_Compressor.SVP |
| SV_Mode/Value | SV_Mode | Screw_Compressor.SV_Mode |
| Started/Value | Started | Screw_Compressor.Started |
| Start_Req/Value | Start_Req | closest PLC bool (not Cmd_Start) |
| Stop_Req/Value | Stop_Req | closest PLC bool (not Cmd_Stop) |
| Interlock/MSet_Bypass00–15 | Interlock/MSet_Bypass00–15 | P_Intlk |
| Interlock/Sts_* / OCmd_Reset / Rdy_Reset / Cfg_Bypassable | same under Interlock/ | P_Intlk |

## Removed from Devices/Compressor (no Screw_Compressor leaf)

Trimmed HMI/demo-only members. StatusIndicator / overview use **Rung**.
`_Alarms` (`Config/_Alarms`) kept as HMI rollup.

| Removed member | Notes |
|----------------|-------|
| Status | Was HMI multistate; use Rung/Color |
| OPER / MAINT / PROG | No nested P_Mode on Screw_Compressor |
| Cmd_Auto / Cmd_Manual / Cmd_Remote | No matching bools; Mode_Change is Int4 |
| MotorStarts / MaxRunTimePerStart | Not present on Screw_Compressor |
| DisP/SP, FLA/SP, SVP/SP | HMI Analog SP children |
| Interlock/Cfg_CondTxt00–15 | HMI strings; not in P_Intlk |
| SummaryInstances | Expression rollup; not PLC |
| RuntimeHours / Cmd_Start / Cmd_Stop | Renamed to TotalRuntime / Start_Req / Stop_Req |

## Consumer

`Units/Machine Room` → `COMP 7` UdtInstance overrides set `sourceTagPath` on each wired
Devices `…/Value` (type `_Root/*`, `valueSource: reference`) to
`[default]RCP1/COMP 7/<member>`.
