# Phase — Valve (`260731-5un`)

## Done
- Trimmed **`Devices/Valve`**: removed `SummaryInstances`; **`Interlock`** → `UdtInstance` `typeId: Config/Interlock` (dropped bare Folder + `Cfg_CondTxt*`).
- All remaining leaves are `_Root/*` or `Config/*`.
- Created **`RCP1/Main Liq SV/`** OPC tags → PLC `MAIN_LIQ_CV5` (`P_ValveSO`).
- Wired **`Units/Machine Room/Main Liq SV`** Value `sourceTagPath`s → `[default]RCP1/Main Liq SV/...`.
- Valve Controls faceplate: Comm label polarity fixed (`FAULT` when Comm/IOFault true).
- Sim: Valve defaults aligned to Config/Interlock (no `Cfg_CondTxt`; `Sts_FirstOut` Int32); regenerated CSV.

## Devices/Valve final members

| Member | typeId |
|--------|--------|
| ClosedLS | `_Root/Digital` |
| Cmd_Close | `_Root/Digital` |
| Cmd_Open | `_Root/Digital` |
| Cmd_Reset | `_Root/Digital` |
| Comm | `_Root/Digital` |
| Failed | `_Root/Digital` |
| Interlock | `Config/Interlock` |
| MAINT | `_Root/Digital` |
| OPER | `_Root/Digital` |
| OpenLS | `_Root/Digital` |
| PROG | `_Root/Digital` |
| Status | `_Root/Multistate` |
| TravelTime | `_Root/Analog` |
| _Alarms | `Config/_Alarms` |

## RCP1 path
`gateways/standard/data/config/resources/core/ignition/tag-definition/default/RCP1/Main Liq SV/`

OPC item root: `ns=1;s=[RCP1]MAIN_LIQ_CV5.*`

### Member → PLC mapping
| Devices / RCP1 | PLC |
|----------------|-----|
| ClosedLS | Inp_ClosedLS |
| OpenLS | Inp_OpenLS |
| Cmd_Open / Cmd_Close / Cmd_Reset | OCmd_* |
| OPER / MAINT / PROG | Sts_Oper / Sts_Maint / Sts_Prog |
| Status | Val_Sts |
| Comm | Sts_IOFault |
| Failed | Sts_FullStall |
| TravelTime | Cfg_TransitStallT |
| Interlock/Sts_IntlkOK | Inp_IntlkOK |
| Interlock/Sts_NBIntlkOK | Inp_NBIntlkOK |
| Interlock/Sts_BypActive | Sts_BypActive |
| Interlock/OCmd_Reset, Rdy_Reset | OCmd_Reset, Rdy_Reset |
| Interlock/MSet_*, Cfg_Bypassable, Sts_FirstOut, Sts_Intlk | best-effort stand-ins (no nested `P_Intlk` on `MAIN_LIQ_CV5`) |

No bare AtomicTags / Folders on Valve (Interlock is Config UDT; RCP1 Interlock is OPC Folder only).
