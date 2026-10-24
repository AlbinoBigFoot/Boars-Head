---
title: Branding
sidebar_position: 12
description: The Boar's Head header logo, the One Shot Automation integrator badge and contact card, and the gateway login / loading screen co-branding - what lives in the project and what must be set on every gateway.
sources:
  - docs/branding.md
last_verified: 2026-10-23
---

# Branding

## What it does

- The **Boar's Head logo** sits in the header after the hamburger menu (theme-aware: dark wordmark on light
  themes, white on dark; the gold medallion stays). Click = home (`/`).
- The **One Shot Automation** integrator badge sits on the right of the header, before the lock icon. Click opens
  a plain-text **contact card** (no links, for the OT network), visible to every role.
- The **login, "Logging In" and project loading screens** carry Boar's Head co-branding (medallion, light grey
  background, Boar's Head red buttons).

![Header with both logos (light theme)](/img/features/branding/header-light.png)

On narrow screens the logos collapse to their marks: under 1024 px the One Shot logo becomes its mark, under 900 px
the Boar's Head logo becomes the medallion, under 700 px the badge hides.

## Where the pieces live

| Piece | Level | Where | Travels with the project export? |
|---|---|---|---|
| Header logo | project | `00_Pages/00_Docked/_Assets/BrandLogo`, Header child `BrandLogo` (`meta.domId` `bh-logo`) | yes |
| Integrator badge + card | project | `_Assets/IntegratorLogo`, `_Assets/IntegratorContact`, Header child `IntegratorBadge` (popup `integratorContact`) | yes |
| Narrow-header rules | project | `stylesheet.css` block `/* Header branding ... */ ... /* end Header branding */` | yes |
| Login / loading screens | **gateway** | Perspective Co-Branding, `config/resources/core/ignition/cobranding/` | **no**: set on every gateway |
| Logo files | repo | `docs/branding/boars-head/` (`SOURCES.md`), `docs/branding/one-shot/` (`README.md`) | git |

The header logos are **base64 data URIs inside the views** (`view.custom.logo.*`), not gateway images, so they
travel with the project and git (gateway image libraries do not).

Co-branding settings: background `#F3F3F5`, text `#1E242E`, button `#B00828`, button text `#FFFFFF`; logo
`bh-cobrand-logo-320.png` (the medallion: IA's logo slots are square), favicon and app icon `*-180.png`.

## How To Change It

**Replace the header logo (Designer):**
1. Convert the new logo (PNG or SVG, light and dark variants) to a data URI (`data:image/png;base64,...`).
2. Project Browser > Perspective > Views > `00_Pages/00_Docked/_Assets` > `BrandLogo`. Replace the values under
   `view.custom.logo` (light and dark), save.
3. The Header view (`00_Pages/00_Docked/Header`) child `BrandLogo` shows it; test in a session in light and dark
   themes and at a narrow width.

**Replace the integrator badge or contact card:** same steps on `_Assets/IntegratorLogo` (badge image) and
`_Assets/IntegratorContact` (the plain-text contact card).

**Narrow-header rules:** Project Browser > Perspective > Stylesheet, the block between
`/* Header branding ... */` and `/* end Header branding */`.

**Login and loading screens:** Gateway web UI > Config > Perspective > Brand Customization (see
[Co-Branding](../gateway/cobranding.md)).

### Production checklist (every gateway that serves BH)

1. Co-branding needs Ignition **Standard** (or Cloud); **Edge** keeps the stock screens (the header logos still
   work).
2. Confirm Boar's Head approves the logo use (or use the files they supply).
3. Gateway web UI: **Config > Perspective > Brand Customization**, turn on Custom Branding, set the logo, favicon,
   app icon and the four colours above, save.
4. Verify: log out and in, check "Logging In", the IdP page, "Loading project" and the browser tab icon. Every other
   Perspective project on the gateway is branded too.

## Known limitations

- Co-branding is gateway-wide (the lab's Lightspeed-FrontEnd project is branded as well).
- IA keeps "Powered by Ignition" and its own wording on the login pages.
