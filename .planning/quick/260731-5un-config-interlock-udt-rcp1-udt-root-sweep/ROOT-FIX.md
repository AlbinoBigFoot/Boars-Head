# ROOT-FIX — `260731-5un` Devices UDT `_Root` / Interlock repair

**Date:** 2026-07-31  
**Commit message:** `fix(260731-5un): Devices UDT members use _Root and Config/Interlock`

## Real bug (Designer evidence)

Designer Tag Browser under **`[default]_types_/Devices`** showed:

1. **`Interlock` as empty Folder** (no expand) — must be `UdtInstance` `typeId: Config/Interlock`
2. **`AutoEN` / `Fail_Timer_PRE` / `Min_Runtime_Set` as AtomicTag** — must be `_Root/Digital` / `_Root/Analog`

**Not** an RCP1 problem. RCP1 stays OPC AtomicTags only; Units bind `sourceTagPath` into `_Root` `Value` members.

## Disk vs Designer (Compressor)

On disk in `tag-type-definition/default/Devices/udts.json`, Compressor **already had**:

| Member | typeId |
|--------|--------|
| AutoEN | `_Root/Digital` |
| Fail_Timer_PRE | `_Root/Analog` |
| Min_Runtime_Set | `_Root/Analog` |
| Interlock | `Config/Interlock` (UdtInstance, empty overrides OK — type owns 24 members) |

Designer showing AtomicTags / empty Interlock Folder for Compressor = **stale gateway memory or unresolved `Config/Interlock`**, not missing typeIds on those leaves. Force `POST scan/config` + Tag Browser refresh / Designer reconnect.

## Real on-disk debt (this fix)

Still broken as bare `Interlock` **Folder** (no `typeId`), 40 nested kids:

| Devices type | Before | After |
|--------------|--------|-------|
| **CoolingTower** | `Folder` (40 kids) | `UdtInstance` `Config/Interlock` |
| **ExhaustFan** | `Folder` (40 kids) | `UdtInstance` `Config/Interlock` |
| **Evaporator** | `Folder` (40 kids) | `UdtInstance` `Config/Interlock` |

Already correct on disk (no change this commit):

- **Valve / Compressor / Pump** — Interlock → `Config/Interlock`
- **Tank / Sensor / VFD** — no Interlock member
- Full Devices audit: **zero** remaining bare `AtomicTag` / `Folder` members without `typeId`

## Config/Interlock health

`tag-type-definition/default/Config/udts.json` → `Interlock` UdtType with **24** members (`Cfg_Bypassable`, `MSet_Bypass00–15`, `OCmd_Reset`, `Rdy_Reset`, `Sts_*`). Healthy.

## Correct architecture

1. **`_types_/Devices/*`** members = `_Root/*` or `Config/Interlock` or `Config/_Alarms` — never bare AtomicTag, never empty Folder for Interlock
2. **`RCP1/`** = OPC AtomicTags only — do **not** put `_Root` into RCP1
3. Units reference RCP1 OPC paths into `_Root` Value members

## Tooling

- Edit: `gateways/standard/data/config/resources/core/ignition/tag-type-definition/default/Devices/udts.json`
- Scan: `POST /data/api/v1/scan/config` with `X-Ignition-API-Token: Name:plaintextKey` from `.env` `IGNITION_API_TOKEN`
- If Designer still stale after HTTP 200: refresh Tag Browser or reconnect Designer
