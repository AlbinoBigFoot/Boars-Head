# Central Alarming

Perspective views and styling for the plant-wide alarm area (BH project).

## Pages

| URL | View | Role |
|-----|------|------|
| `/alarms` | `00_Pages/Alarms/Summary` | Central Alarm Status page |

## Views

| Path | Role |
|------|------|
| `00_Pages/Alarms/_Assets/AlarmStatusTable` | Reusable built-in Alarm Status Table (`ia.display.alarmstatustable`) |
| `00_Pages/Alarms/Summary` | Thin page shell that embeds the table |

### AlarmStatusTable params

| Param | Default | Meaning |
|-------|---------|---------|
| `sourceFilter` | `*` | Bound to `filters.active.conditions.source` (device faceplates can pass a scoped filter later) |

Columns shown: **priority**, **state**, **label**, **activeTime**. Sort: `isAcked` → `priority` → `activeTime`.

## Row colors (CSS)

Defined in `stylesheet/stylesheet.css` as tokens and `.psc-alarm-row-*` classes.

| Priority | Active unack (matches icons) | Active ack (darker) |
|----------|------------------------------|---------------------|
| Critical | `#E22028` / `--alarm-critical` | `#8B1519` / `--alarm-critical-ack` |
| High | `#EC8629` / `--alarm-high` | `#9A5619` / `--alarm-high-ack` |
| Medium | `#F5E11B` / `--alarm-medium` | `#9E9012` / `--alarm-medium-ack` |
| Low | `#916AAD` / `--alarm-low` | `#5A3F6C` / `--alarm-low-ack` |

Unack rows use full icon colors. Acked active rows use the darker `-ack` variants. Cleared rows use `alarm-row-cleared` (neutral).

`rowStyles` also sets matching `backgroundColor` / `color` so the Alarm Status Table paints reliably; CSS classes keep the palette centralized for reuse.

## Demo alarms (taginstances)

Showcase evaporators **EV-22–EV-33** each have an Ignition alarm on `Fan 1/Fault/Value` (`WhenTrue`, `ackMode: Manual`) so they appear in the Alarm Status Table:

| EVs | Priority |
|-----|----------|
| EV-22, EV-26, EV-30 | Critical |
| EV-23, EV-27, EV-31 | High |
| EV-24, EV-28, EV-32 | Medium |
| EV-25, EV-29, EV-33 | Low |

`Fan 1/Fault/Value` is memory `true` so the alarm is active and unacked until you ack it from the table. `_Alarms/_Active` / `_Unack` / priorities are set to match the badges.

Re-import `taginstances.json` after pulling changes.

## Not in this pass

- Alarm Journal
- Unacked row blink
- Live PLC alarm pipeline beyond these demo memory tags
- Row blink / `_Config/Flash` binding
