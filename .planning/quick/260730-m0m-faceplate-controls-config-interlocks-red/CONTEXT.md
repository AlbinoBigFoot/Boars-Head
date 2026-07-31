# Quick context — Faceplate Controls / Config / Interlocks redesign

**Quick id:** `260730-m0m`  
**Slug:** `faceplate-controls-config-interlocks-red`

## Locked decisions (user 2026-07-30)

### Controls (grid sections, top → bottom)
1. **Mode** (if applicable) — Maintenance / Program / Operator (and associated controls)
2. **Status** — with control buttons: start/stop, auto, manual, remote
3. **KPI** — device-specific (runtime hours, motor starts, max run time per start, etc.)
4. **Compressors only** — button to open external **Web GUI** (`webGuiUrl` param)

### Configuration (Scout-like)
- Edit SPs, enable/disable
- Device-specific (e.g. pump: time after start for feedback before fault)
- Interlock permissives and bypasses where they belong in Scout Config
- Compressors: many Config fields N/A — show only what applies; structure must work for pumps/other devices later

### Tabs
- **Hide tab if it would be empty** (no associated data)
- Add **Interlocks** tab when applicable — compressors have interlocks (old FT had dedicated faceplate)
- Existing: Controls, Configuration, Trend, Alarm Configuration, Alarms (+ Interlocks)

### Visual
- Faceplate currently rough → **professional, modern** look (CSS Advanced Stylesheet; match BH theme tokens; Scout structure + BH visual language)

## Assumptions to confirm in research (do not invent blindly)
- How Scout binds Op/Prog/Maint vs BH Devices/Compressor (may need new tags or session-role UI)
- How Scout detects “tab has data” for show/hide
- Compressor interlock tag sources (PLC Screw_Compressor / FT faceplate / Devices UDT gaps)

## Out of scope
- Full port of every Scout device Config field in one pass — Compressor-first + shell/sections reusable for Pump
- Redesigning Trend/Alarms (recently fixed) beyond tab visibility + chrome polish
