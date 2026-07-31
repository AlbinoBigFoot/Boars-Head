# CONTEXT — Interlock UDT + per-device RCP1/_Root sweep

**Quick:** `260731-5un`

## Locked (user 2026-07-31)
1. `AutoEN`, `Fail_Timer_PRE`, `Min_Runtime_Set` must be `_Root` UDT members.
2. Create **`Config/Interlock`** UDT; replace bare Interlock AtomicTags on devices with that UDT instance.
3. Per-device subagents (GSD): after Compressor finish → **Pump, Valve, Tank, Sensor** each:
   - RCP1 OPC tags for a test instance folder
   - Trim Devices UDT to PLC-backed only
   - Every tag `_Root` or `Config/Interlock`
4. Pushover when fully done.

## Order
Compressor finish → Pump → Valve → Tank → Sensor → Pushover
