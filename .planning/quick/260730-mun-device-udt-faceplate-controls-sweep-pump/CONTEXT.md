# Quick context — Device UDT + Faceplate Controls sweep

**Quick id:** `260730-mun`

## Locked (user)

1. **Web GUI:** Header next to Close only; remove from Controls body; visible **only for Compressors** (for now).
2. Update **Devices UDTs** comprehensively for: Pump, Valve, Tank, Sensor, ExhaustFan, Evaporator (Compressor already expanded — keep consistent).
3. Correlate **CSV** (`sim/bh-plant-sim.csv` + any FT tag CSVs in repo/Displays docs) **and** PLC UDTs in `tag-type-definition/default/PLC/`.
4. Update or **create missing Overview** pages for each device family.
5. Update **Faceplate Controls** (and Config/Interlocks as data warrants) per device from discovered tags.
6. **Demo** all new tags in sim properly; metadata/states/engUnits correct (`_Root` bases).
7. Thorough; GSD + up to 8 subagents; **Pushover screenshots** of Controls tab for **each** component type while Dylan is AFK.

## Deliverable proof
Pushover with screenshots: Faceplate Controls for Compressor, Pump, Valve, Tank, Sensor, ExhaustFan, Evaporator (and CoolingTower if in Devices).

## Out of scope
- Perfect live PLC OPC for every leaf (sim/demo OK)
- Non-compressor Web GUI
