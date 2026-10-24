---
title: Style Classes And Stylesheet
sidebar_position: 3
description: Project style classes vs the Advanced Stylesheet - what goes where, how Perspective emits them, the cascade traps, and the 2026-09 cleanup that set the rules.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/stylesheet/stylesheet.css"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/style-classes/**/style.json"
  - "docs/stylesheet-cleanup.md"
last_verified: 2026-10-24
---

# Style Classes And Stylesheet

BH has two places for CSS classes. Both are applied the same way, by name in a component's `props.style.classes`.

| | Project style classes | Advanced Stylesheet |
|---|---|---|
| Files | `com.inductiveautomation.perspective/style-classes/<name>/style.json` | `com.inductiveautomation.perspective/stylesheet/stylesheet.css` |
| Designer | Project Browser > Perspective > Styles (one resource per class; edit in the style editor) | Styles > Advanced Stylesheet (one CSS file) |
| Count (2026-10-23) | about 160 | about 4,450 lines |
| Holds | Shared single-class looks: `Fonts/*`, `fs-*` / `fw-*` / `text-*`, `bg-page`, `faceplate-section*`, `theme-toggle*`, `value-bad`, `value-alarm`, `form-*`, `report-*`, `admin-*`, `fp-*` (the redesigned Discrete Input and Tank Overview faceplates) | Semantic tokens and `--alarm-*`; rules on IA internals (`.ia_popup__header`, tree, table); ApexCharts; descendant, `:hover` on children, `:has()`, `@container`, `@keyframes`, `@media`; layout properties |
| Reference | [Style Class Catalog](../reference/style-classes.md) | [Stylesheet Index](../reference/stylesheet.md) |

## How Perspective Emits Them (Measured, Don't Relearn)

- Style classes are written **after the whole stylesheet**, **sorted by name**, as plain `.psc-<name> {}` rules.
  So a style class beats a stylesheet rule of the same specificity, and among style classes the one later in the
  alphabet wins. That is why `font-label`-type overrides that sort earlier than their base stayed in CSS.
- The style-class compiler **silently drops** the shorthands `background` and `border` and the layout properties
  `gap`, `min-width`, `min-height`, `align-items`, `justify-content` and `transition`. Use longhands
  (`backgroundColor`, `borderColor` ...), or keep that part in the stylesheet.
- In the stylesheet, address a project class as `.psc-<name>`; a slash is escaped: `.psc-Fonts\/Label`.
- **Descendant rules only reach views inside that ancestor**, including through embedded views.
- **Perspective injects inline layout styles** (`overflow: auto` on containers, flex from grow / shrink / basis,
  coordinate sizes). An "identical" inline value removed in favour of a class can let the injected default win. Keep
  layout props inline or `!important` in CSS.
- **Charts re-layout after load.** Keep the `!important` height / flex / `min-*` rules on the Adhoc Trend and
  `.apexcharts-*` chain; dropping one collapsed the trend axis.

## The Base Font Classes

`Fonts/Label`, `Fonts/Value`, `Fonts/Title`, `Fonts/Heading`, `Fonts/Header`, `Fonts/BadData`, `Fonts/LiveData`,
`Fonts/LiveDataEntry` and `Fonts/Button` are the base text classes (Scout-style names). `Fonts/Label` and
`Fonts/Value` keep their `color` in a small CSS remnant. Size, weight and colour variations on top of them use the
[utilities](./utilities-and-design-classes.md).

## The 2026-09 Cleanup

The stylesheet had grown to 4,257 lines and 879 `!important`, with views carrying 3 to 5 times the inline styles of
the reference projects, because views carried full inline styles as well as a class, and the CSS grew `!important` to
win. The cleanup (`docs/stylesheet-cleanup.md`):

| | Before | After |
|---|---|---|
| Inline style props in views | 14,664 | 8,607 |
| `!important` | 879 | 739 |
| Dead rules | 33 | 0 |
| Views | 278 | 205 (73 unreachable views deleted; the project has grown again since) |
| Inline font overrides on font classes | 1,499 | about 106 |

Every step was checked with a 21-page screenshot diff and computed-style snapshots. Phase 2 moved 33 shared
single-class rules to style classes; phase 3 renamed the base font classes to `Fonts/*` (1,625 references).

Gotcha found then: the imported AdhocTrend views carried dangling Scout class names (`Fonts/Label` ...) that
suddenly applied once BH created classes with those names. **Before creating a style class, grep the views for its
name** (`Colors/*` and `Container/*` are still dangling there).

## Workflow

1. Edit the class in the Designer: Project Browser > Perspective > **Styles** (a style class), or the **Stylesheet**
   resource (Advanced Stylesheet) for IA-internal, layout and state rules.
2. Prefer the utility classes (`fs-`, `fw-`, `text-`) over inline font overrides on a component: select the component,
   add the utility to `props.style.classes` and clear the inline value.
3. Save and check all four themes. Search the generated [Stylesheet Index](../reference/stylesheet.md)
   for the class to see every selector that uses it.
