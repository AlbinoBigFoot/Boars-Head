# Phase 1 — Compressor finish (`260731-5un`)

## Done
- Added **`Config/Interlock`** UDT (`tag-type-definition/default/Config/udts.json`).
- **`Devices/Compressor.Interlock`**: Folder → `UdtInstance` `typeId: Config/Interlock`.
- **`AutoEN`**, **`Fail_Timer_PRE`**, **`Min_Runtime_Set`**: already `_Root/Digital` / `_Root/Analog` (unchanged).
- **Units/Machine Room/COMP 7**: Interlock override Folder → `UdtInstance`; Value `sourceTagPath`s unchanged (`[default]RCP1/COMP 7/Interlock/...`).
- Faceplate `_Assets/Interlocks` paths (`…/Interlock/<member>/Value`) still valid; no view edit.
- `Sts_FirstOut` corrected to **`_Root/Analog`** (PLC `P_Intlk` Int2).

## Config/Interlock members (24)

| Member | typeId |
|--------|--------|
| Cfg_Bypassable | `_Root/Analog` |
| MSet_Bypass00–15 | `_Root/Digital` |
| OCmd_Reset | `_Root/Digital` |
| Rdy_Reset | `_Root/Digital` |
| Sts_BypActive | `_Root/Digital` |
| Sts_FirstOut | `_Root/Analog` |
| Sts_Intlk | `_Root/Analog` |
| Sts_IntlkOK | `_Root/Digital` |
| Sts_NBIntlkOK | `_Root/Digital` |

## Devices/Compressor final members

| Member | typeId |
|--------|--------|
| Alm | `_Root/Digital` |
| Amps | `_Root/Analog` |
| AutoEN | `_Root/Digital` |
| CP_Mode | `_Root/Multistate` |
| Start_Req | `_Root/Digital` |
| Stop_Req | `_Root/Digital` |
| Color | `_Root/Multistate` |
| Comm | `_Root/Digital` |
| Cutout | `_Root/Digital` |
| DisP | `_Root/Analog` |
| FLA | `_Root/Analog` |
| Fail_Timer_PRE | `_Root/Analog` |
| Failed | `_Root/Digital` |
| Interlock | `Config/Interlock` |
| Min_Runtime_Set | `_Root/Analog` |
| Rung | `_Root/Multistate` |
| TotalRuntime | `_Root/Analog` |
| SVP | `_Root/Analog` |
| SV_Mode | `_Root/Multistate` |
| Started | `_Root/Digital` |
| _Alarms | `Config/_Alarms` |

No bare AtomicTags / Folders on Compressor.
