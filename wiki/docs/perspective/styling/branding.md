---
title: Branding
sidebar_position: 6
description: The Boar's Head header logo, the One Shot Automation integrator badge and contact card, and the gateway Perspective co-branding of the login and loading screens.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/BrandLogo/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/IntegratorLogo/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/_Assets/IntegratorContact/view.json"
  - "docs/branding.md"
last_verified: 2026-10-23
---

# Branding

![Header](/img/perspective/header.png)

```text
[=] [Boar's (medallion) Head]  ......  [ONE SHOT AUTOMATION] | [lock] [user] [oos] [bell] [trend] [gear]
```

| Piece | Level | Where | Travels with the project export? |
|---|---|---|---|
| Boar's Head header logo | project | View `00_Pages/00_Docked/_Assets/BrandLogo`, Header child `BrandLogo` | yes |
| One Shot badge and contact card | project | `_Assets/IntegratorLogo`, `_Assets/IntegratorContact`, Header child `IntegratorBadge` | yes |
| Narrow-header collapse | project | `stylesheet.css` block `/* Header branding ... */ ... /* end Header branding */` | yes |
| Login, "Logging In" and loading screens | **gateway** | Perspective Co-Branding (`config/resources/core/ignition/cobranding/`) | **no**: set it on every gateway |
| Logo source files | repo | `docs/branding/boars-head/` (`SOURCES.md`), `docs/branding/one-shot/` (`README.md`) | git |

To change them, see the "How To Change It" steps below.

## Header Logo (`BrandLogo`)

- Right after the hamburger, 176 x 30 px. The logos are **base64 data URIs** in `view.custom.logo.*`, not a gateway
  image or icon library, so they travel with the project and git.
- The wordmark is near black on light themes and white on dark themes; the medallion stays gold. The image source is
  an expression on the theme: `left(lower(coalesce({session.props.theme}, '')), 4) = 'dark'`.
- Click = a Navigation action to `/` (tooltip "Home", `meta.domId` `bh-logo`).

## Integrator Badge (`IntegratorBadge`)

- Before the lock icon: the One Shot Automation logo (slate and red on light themes, white on dark) and a 1 px
  divider (`--border-strong`).
- Click toggles the popup `integratorContact` (`_Assets/IntegratorContact`, 300 x 212 at top 56 / right 350,
  overlay dismiss): a plain-text contact card with no links (OT network), visible to every role.

## Narrow Headers

`.psc-app-header` is `overflow: hidden`, and the logos collapse to their marks: below 1024 px the One Shot logo
becomes its mark, below 900 px the Boar's Head logo becomes the medallion, below 700 px the badge hides. Each logo
view collapses only when its `params.collapsible` is true.

Keep the Header children `BrandLogo` and `IntegratorBadge` (and their names) when you rearrange the Header.

## How To Change It

- **Header logo:** Designer > Project Browser > Perspective > Views > `00_Pages/00_Docked/_Assets/BrandLogo` >
  replace the data URIs under `view.custom.logo` (light and dark), save, and test in light and dark themes at a
  narrow width. Convert the logo file to a `data:image/png;base64,...` string first.
- **Integrator badge or contact card:** same, on `_Assets/IntegratorLogo` and `_Assets/IntegratorContact`.
- **Narrow-header rules:** Project Browser > Perspective > Stylesheet, the `/* Header branding ... */` block.
- **Login and loading screens:** Gateway web UI, see below.
- A graphic designed in Figma goes in through the SVG route in [Figma Workflow](./figma-workflow.md).

## Gateway Co-Branding

Lab settings (2026-10-22): enabled, background `#F3F3F5`, text `#1E242E`, button Boar's Head red `#B00828`, button
text `#FFFFFF`; logo `bh-cobrand-logo-320.png` (the medallion only, because the logo slots are square), favicon
`bh-favicon-180.png`, app icon `bh-appicon-180.png`. It brands the "You must log in" page, the IdP login page,
"Logging In / Out", the "Loading project" page and the browser tab icon.

Co-branding is gateway-wide (every project on that gateway gets it) and is available on Standard, not on Edge.
To set it on another gateway: Gateway web UI **Home > Perspective > Brand Customization** (Custom Branding on,
the files from `docs/branding/boars-head/`, the four colours). The production checklist is in `docs/branding.md` and on [Deployment](../../deployment/index.md).
