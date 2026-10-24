---
title: Themes
sidebar_position: 2
description: The four BH operator themes (light-cool, dark-cool, light-warm, dark-warm), how session.props.theme loads them, the semantic token layer and the theme-invariant alarm colours.
sources:
  - "gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/**/*.css"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/ChangeTheme/view.json"
  - "docs/themes.md"
  - "docs/ignition-theme-architecture.md"
last_verified: 2026-10-24
---

# Themes

Operators pick one of four themes from the **gear icon** in the header (the ChangeTheme popup): Light / Dark and
Cool / Warm, plus Animations On / Off.

![ChangeTheme popup](/img/perspective/change-theme.png)

| Selection | `session.props.theme` | Meaning |
|---|---|---|
| Light + Cool | `light-cool` | Light surfaces, cool grays (**default**, set in session props) |
| Dark + Cool | `dark-cool` | Dark surfaces, cool grays |
| Light + Warm | `light-warm` | Light surfaces, warm grays |
| Dark + Warm | `dark-warm` | Dark surfaces, warm grays |

The choice lives only in `session.props.theme` (no tag, no user property). Tabs of the same browser share one
Perspective session, so they switch together; use a private window for an independent session.

| Light cool | Dark cool |
|---|---|
| ![Machine Room light](/img/perspective/machine-room.png) | ![Machine Room dark](/img/perspective/machine-room-dark.png) |

## How A Theme Loads

1. The client reads `session.props.theme`, a folder name under the gateway's `themes/`.
2. The gateway serves that theme's `config.json` entrypoint (`index.css`): variables, fonts, IA component chrome.
3. The project **Advanced Stylesheet** loads after it and defines BH tokens with `var(--neutral-*)`.
4. Switching theme swaps the whole theme stylesheet; everything built on the neutrals updates. There is no
   `[data-theme]` attribute.

Gateway folders (`gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/`):

| Folder | Kind |
|---|---|
| `light`, `dark` | **Full bases**: variables, fonts, globals, `app/`, `common/`, `designer/`, `palette/` |
| `light-cool`, `dark-cool`, `light-warm`, `dark-warm` | **Thin variants**: their own `variables.css` (neutral overrides, warm accents) plus `@import` of the base chrome from `../light` / `../dark` |

Thin themes need the full bases next to them; a gateway with only the thin folders (as Edge had) breaks them. The
generated [Themes And Icons](../reference/themes-and-icons.md) page lists every folder's imports and neutral values.
ChangeTheme writes the `*-cool` names because the stock `light` / `dark` bundles don't carry the BH variable
overrides; legacy `light` / `dark` values are upgraded on the next click.

Edit a theme in the Designer (Project Browser > Perspective > Styles > Themes) or in the Gateway web UI, then
hard-refresh the client (`Ctrl+F5`).

## The Semantic Token Layer

The stylesheet maps meaning onto the theme's neutral scale (excerpt):

```css
:root {
  --surface-page: var(--neutral-10);       /* page background (class bg-page) */
  --surface-card: var(--neutral-20);       /* cards (container-card) */
  --surface-component: var(--neutral-30);  /* bg-component */
  --surface-header: var(--neutral-30);     /* header (app-header) */
  --surface-nav: var(--neutral-20);        /* nav dock */
  --text: var(--neutral-100);
  --text-secondary: var(--neutral-80);
  --text-muted: var(--neutral-60);
  --border: var(--neutral-30);
  --border-strong: var(--neutral-50);
  --deviceFill-running: var(--neutral-10);
  --deviceFill-stopped: var(--neutral-60);
  --deviceFill-faulted: var(--neutral-100);
}
```

`--neutral-10` is the page end of the scale in every theme (near white in light, near black in dark) and
`--neutral-100` the text end, so the same token works in all four.

Rules:

- **Never redefine `--neutral-*` in the stylesheet**: it would pin every theme to one set of hex values.
- **Never hard-code a chrome colour in a view** (`#D8D8D8`, `#1A2329`): use a class such as `bg-page`,
  `bg-component`, `bg-container`, `container-card`, `app-header`, `nav-*`.
- New themed surface: add a token that points at a neutral, add a class that uses it, put the class on the view,
  and check all four themes.

## What Never Changes: Alarm Colours

Only the alarm tokens are **fixed hex**, so a priority looks the same in every theme (ISA-101 style):

| Token | Active | Acknowledged |
|---|---|---|
| Critical | `--alarm-critical: #e22028` | `--alarm-critical-ack: #8b1519` |
| High | `--alarm-high: #ec8629` | `--alarm-high-ack: #9a5619` |
| Medium | `--alarm-medium: #f5e11b` | `--alarm-medium-ack: #9e9012` |
| Low | `--alarm-low: #916aad` | `--alarm-low-ack: #5a3f6c` |

They paint the Alarm Status rows, the device alarm frames and badges and the header bell. Status chips for normal
states (Cooling, Idle, Off) follow the theme; attention states (Fault, Defrost) keep saturated accents on the
status text, and the device body fill is coloured only for Comm Loss (`--deviceFill-commLoss`, a theme-invariant red `#C62828` defined in the Advanced Stylesheet; apply the class `device-comm-loss`). A bad value is never coloured: it shows the gray italic dash (`value-bad`). Both were re-confirmed on 2026-10-24 (an earlier attempt made COMM LOSS gray and was reverted). Always keep a text
status next to a colour.

## Animations

ChangeTheme's Animations Off sets `session.props.animations = false`. The Header root then gets
`app-header animations-off`, and stylesheet rules under `body:has(.psc-animations-off)` stop the known motion
classes (`fan-spin`, `ct-fan-side-spin`, `ct-spray-run`, `alarm-flash`, `container-fade-in`). Colours don't change.

## Deep Dives

`docs/themes.md` (operator and implementer guide), `docs/ignition-theme-architecture.md` (8.3 file layout,
`resource.json` rules, import graphs, checklist) and `docs/theme-figma-tokens.md` (hex per mode).
