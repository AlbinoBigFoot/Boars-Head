# CONTEXT — Fix standalone memory → `_Root` bases

**Quick:** `260731-1qz`

## Locked
User: every Devices tag must use `_Root` as base — no standalone memory AtomicTags for process/HMI members.

## Scope
1. Convert all Bucket A KPI/config/limit floats/ints → `_Root/Analog`
2. Convert mode/cmd bools (`OPER`/`MAINT`/`PROG`/`Cmd_*`/`AutoEN`/`HMIEnable`/etc.) → `_Root/Digital` (user: every tag)
3. Convert Interlock children: bools/status → `_Root/Digital`; numeric → `_Root/Analog`; string CondTxt — use best `_Root` available or Document if exists
4. Fix instance `_Alarms` AtomicTag malformations → `UdtInstance` `Config/_Alarms`
5. Fix Sensor/instance overrides that flatten Analog children
6. Update faceplate bindings that used bare `{tagPath}/OPER` to `{tagPath}/OPER/Value` where needed
7. Update sim CSV paths (`…/RuntimeHours` → `…/RuntimeHours/Value`)
8. Scan + repair signatures

## Reference
`.planning/quick/260730-mun-…/AUDIT-root-bases.md`
Compressor Digital/Analog shapes for copy.
