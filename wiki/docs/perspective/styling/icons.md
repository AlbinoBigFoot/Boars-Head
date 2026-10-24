---
title: Icons
sidebar_position: 5
description: Icons in the BH HMI - Material icons, the gateway equipment icon library, the status icon elements and the rule that status icons must be backed by PLC members.
sources:
  - "gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/icons/**/*"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/03_Elements/01_Status/**/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/Legend/view.json"
last_verified: 2026-10-24
---

# Icons

An Icon component (`ia.display.icon`) and a nav tree item both take an icon **path** `<library>/<id>`, for example
`material/notifications` or `equipment/pump`.

| Library | Where | Notes |
|---|---|---|
| `material/*` | Built into Ignition (Google Material icons) | Most UI icons: nav folders, header buttons, toolbar actions. The generated page lists every one in use. |
| `equipment/*` | Gateway icon library `gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/icons/equipment/equipment.svg` | BH's own symbols: `alarm_critical` / `_high` / `_medium` / `_low`, `devices`, `alarm_journal`, `trending`, `pump`, `exhaust_fan`, `compressor`, `valve`, `conveyor`, `rupture-disk`. |

The full list with labels and usage counts is on [Themes And Icons](../reference/themes-and-icons.md).

## Adding An Equipment Icon

`equipment.svg` is one SVG file with one `<g class="icon" id="<id>">` per icon inside a 24 x 24 `<svg>`, preceded by
a `<!-- Label -->` comment. To add one:

1. Draw it in Figma at 24 x 24 and export it as SVG.
2. Open the SVG in a text editor and copy its shapes into a `<g class="icon" id="my_icon">...</g>` block, with a
   `<!-- Label -->` comment before it, inside the library's `equipment.svg`.
3. Gateway web UI > **Config > Perspective > Icons** > the `equipment` library > upload the edited `equipment.svg`.
4. Use it as `equipment/my_icon` in an icon component's `props.path`.

Icon libraries are gateway config: a project export does **not** carry them. That is why the header logos are data
URIs inside the views instead (see [Branding](./branding.md)), and why another gateway needs the library copied.

## Status Icons And The Legend

`03_Elements/01_Status/Icons/*` are one small view per device state: Auto, Hand, Operator, Program, Maintenance,
Override, NoMode, Interlock, OutOfService, Simulate, Remote, Faceplate (and older Stale, NotAtSetpoint, Exclude,
DoorStatus). `IconHeader` shows the strip of icons for a device; `NotificationIcons/Alarms/*` and `CommLoss` are the
alarm and comm badges. `StatusIndicator` derives its **COMM LOSS** label (red) from the quality of the device's key member,
and `StatusDot` takes a `blink` param (style class `status-dot-blink`, used by the Machine Room AD lamps in alarm). The right **Legend** dock (`00_Pages/00_Docked/Legend`) explains them.

**Rule:** an icon state is offered only when a PLC UDT actually carries the member (P_Motor, P_ValveSO, P_AIn,
P_DIn ... imported with the L5K tool into `tag-type-definition/default/PLC/`). Don't invent members such as
`Sts_OoS` or Stale for an icon. Current backed set: Comm Loss (quality), Out Of Service (`Sts_Disabled` / the
instance `Enabled` flag), Interlocked, Maintenance, Hand, Operator, Program, Override (`Sts_Ovrd`), No Mode
(`Sts_NoMode`), Simulation (`Inp_Sim`).

## Icon Colours

Icons take `--icon` / `--neutral-*` colours so they follow the theme (class `color-icon`); alarm icons keep the fixed
`--alarm-*` colours. Avoid a fixed `color` on an icon unless it is an alarm or a status accent.
