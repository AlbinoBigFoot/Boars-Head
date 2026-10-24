---
title: Styling Overview
sidebar_label: Overview
sidebar_position: 1
description: The four styling layers of the BH HMI - gateway themes, the Advanced Stylesheet, project style classes and view props - and where each kind of rule belongs.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/style-classes/**/style.json"
  - "docs/themes.md"
  - "docs/stylesheet-cleanup.md"
last_verified: 2026-10-24
---

# Styling Overview

Perspective renders views as HTML, so everything you see is CSS. In BH the CSS comes from four layers, loaded in this
order (a later layer wins at equal specificity):

| # | Layer | Where | Owns |
|---|---|---|---|
| 1 | **Gateway theme** | `gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/themes/<theme>/` (gateway resource) | The neutral scale `--neutral-10 ... --neutral-100`, Ignition's own component chrome (buttons, tables, inputs), fonts, accents like `--callToAction`. Picked by `session.props.theme`. |
| 2 | **Advanced Stylesheet** | `projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css` (Designer: Styles > Advanced Stylesheet) | BH semantic tokens on top of the theme (`--surface-page`, `--text`, `--border`, `--nav-*`), the fixed alarm colours `--alarm-*`, everything a style class can't express: IA internals, ApexCharts, descendant / `:has()` / state rules, animations, layout. |
| 3 | **Project style classes** | `style-classes/<name>/style.json` (Designer: Styles) | Shared single-class looks: the type scale `fs-*`, `fw-*`, `text-*`, `Fonts/*`, faceplate sections, theme toggle, `bg-page`, the form / report / admin design classes, `value-bad`. Emitted **after** the stylesheet, sorted by name. |
| 4 | **View props** | `props.style` on each component | Inline styles and the `classes` string. Keep these to layout (position, size, flex) and use classes for looks. |

A view uses a class by name in `props.style.classes` (space separated). Perspective prefixes project classes with
`psc-`, so the stylesheet selector for `bg-page` is `.psc-bg-page`, and `Fonts/Label` becomes
`.psc-Fonts\/Label`.

## Where Does A New Rule Go?

1. **A colour or surface that should follow light / dark / warm / cool**: a semantic token in the stylesheet that
   points at `var(--neutral-*)`, plus a class. Never a hex in a view. See [Themes](./themes.md).
2. **A reusable single-class look** (font size, weight, a card): a project style class. Check
   [Style Classes And Stylesheet](./style-classes-and-stylesheet.md) for what style classes silently drop
   (`background` / `border` shorthands, `gap`, `min-*`, `align-*`, `justify-*`, `transition`).
3. **Anything with a descendant, `:hover` on a child, `:has()`, `@container`, `@keyframes`, or a rule on an IA
   internal class** (`.ia_popup__header`, `.apexcharts-*`): the stylesheet.
4. **Layout of one component**: inline props.

## Pages In This Section

- [Themes](./themes.md): the four themes, how they load, semantic tokens, the alarm colour lock.
- [Style Classes And Stylesheet](./style-classes-and-stylesheet.md): the two class systems and their cascade
  rules; the cleanup history.
- [Utilities And Design Classes](./utilities-and-design-classes.md): `fs-` / `fw-` / `text-` utilities and
  inline-style cleanup, `value-bad` / `value-alarm`, and the `form-*`, `report-*`, `admin-*` and `fp-*` families.
- [Icons](./icons.md): Material icons and the `equipment` library.
- [Branding](./branding.md): header logos, integrator badge, gateway co-branding.
- [Figma Workflow](./figma-workflow.md): export an SVG from Figma and drag it onto a view in the Designer.

Generated: [Style Class Catalog](../reference/style-classes.md) (every class with its CSS and users),
[Stylesheet Index](../reference/stylesheet.md) (every section, class and variable with line numbers),
[Themes And Icons](../reference/themes-and-icons.md).
