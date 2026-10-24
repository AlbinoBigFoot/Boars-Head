---
title: Perspective Co-Branding
sidebar_position: 10
description: The Boar's Head login and loading screens, how to apply them in the Gateway web UI, and what to redo on another gateway.
sources:
  - gateways/standard/data/config/resources/core/ignition/cobranding/config.json
  - docs/branding.md
  - docs/branding/boars-head/SOURCES.md
last_verified: 2026-10-23
---

# Perspective Co-Branding

**Where:** Home > Perspective > **Brand Settings** (`config/resources/core/ignition/cobranding/config.json`, tracked).

Co-branding styles the screens Perspective shows **before** a project loads: the login page, "Logging In" and the
loading spinner. It is **gateway configuration, not part of the project**, so a project export doesn't carry it; set
it on every gateway.

| Setting | Value |
|---|---|
| Enabled | yes |
| Background | `#F3F3F5` |
| Text | `#1E242E` |
| Buttons / button text | Boar's Head ribbon red `#B00828` / `#FFFFFF` |
| Logo | `bh-cobrand-logo-320.png` (medallion on a transparent 320x320 square) |
| Favicon | `bh-favicon-180.png` |
| App icon | `bh-appicon-180.png` (opaque black: Ignition renders transparent app icons black) |

The images are stored as base64 inside `config.json`. Source and derived files: `docs/branding/boars-head/`
(`SOURCES.md` records where each official file came from, with SHA-256 hashes).

## Applying It

In the Gateway web UI open **Config > Perspective > Brand Customization** (called Brand Settings in some 8.3 builds),
upload the three PNGs (logo, favicon, app icon), set the colours from the table above and save. No restart is needed.
- Edge edition: co-branding is a Standard/Cloud feature. On Edge the login screen stays stock.

## In-Project Branding (Not Gateway)

The header logos travel with the project: `00_Pages/00_Docked/_Assets/BrandLogo` (Boar's Head lockup, light/dark
variants as data URIs) and `_Assets/IntegratorLogo` + `IntegratorContact` (One Shot badge and contact card). See
[Perspective](../perspective/index.md).

:::note Trademark
"Boar's Head" and the medallion are registered trademarks of Boar's Head Brand, used here only to brand Boar's Head's
own HMI. Before production, confirm the client approves, or swap in official brand files and upload them
again on the Brand Customization page.
:::
