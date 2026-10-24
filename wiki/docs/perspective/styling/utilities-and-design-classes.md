---
title: Utilities And Design Classes
sidebar_position: 4
description: The fs- / fw- / text- utility classes, value-bad and value-alarm, and the form-*, report-* and admin-* design system classes.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/style-classes/**/style.json"
  - "docs/operations-forms.md"
  - "docs/report-builder.md"
last_verified: 2026-10-24
---

# Utilities And Design Classes

## Type Scale Utilities

Project style classes that set one property each:

| Family | Classes | Sets |
|---|---|---|
| Size | `fs-9`, `fs-10`, `fs-11`, `fs-12`, `fs-13`, `fs-14`, `fs-15`, `fs-16`, `fs-18`, `fs-20`, `fs-22` | `font-size` in px |
| Weight | `fw-400`, `fw-600`, `fw-700` | `font-weight` |
| Colour | `text-muted` (`var(--text-muted)`), `text-cta` (`var(--cta)`), `text-ok` (`#2E7D32`) | `color` |

Combine them with a base font class: `"classes": "Fonts/Label fs-10 fw-700"`. Because style classes are emitted
after the stylesheet, a utility beats the base class's own size, exactly like an inline value would.

### Use Utilities Instead Of Inline Values

On a component that carries a base font class, don't set inline `fontSize`, `fontWeight` or `color`. In the Designer
select the component, add the utility to `props.style.classes` (`fs-<n>` for 9-22 px, `fw-<n>` for 400 / 600 / 700,
`text-muted` / `text-cta` / `text-ok` for the three colours), and clear the inline value in the Property Editor. Keep
inline values when a style or classes are bound by an expression, when a class carries `!important`, or when a scoped
compound rule can reach the view: the utility could render differently there.

## Value States

| Class | CSS | Use |
|---|---|---|
| `value-bad` | `color: var(--neutral-60); font-style: italic` | The em dash shown for a missing / bad-quality value (see [Faceplates](../faceplates.md#value-quality-gray-italic-dash)) |
| `value-alarm` | `color: var(--error); font-weight: 700` | A value in its alarm state |
| `Fonts/BadData` | base font class | Older bad-data text style |

## Form Design System (`form-*`)

Built for the Operations Forms (2026-10-23), designed in Figma first, meant for reuse on any data-entry page:

| Class | Part |
|---|---|
| `form-card` | Card: 6 px radius, 1 px `--border` |
| `form-title`, `form-subtitle` | Page title 22 / 700, subtitle 13 muted |
| `form-section-head`, `form-section-title` | Section header bar and its 14 / 700 title |
| `form-label`, `form-required-marker` | Field label 12 / 600, red `*` (`var(--error)`) |
| `form-input`, `form-input-required` | Input: 13 px text, `--input` fill, 1 px `--border-strong`, 4 px radius (the 32 px height is set by the layout), red outline while a required value is empty |
| `form-th`, `form-row-label` | Table-like readings grid: header cell (11 px uppercase muted), row label 13 / 700 |
| `form-check`, `form-calc`, `form-hint`, `form-note` | Checkbox, calculated value, hints and notes |
| `form-banner`, `form-banner-error`, `form-banner-ok` | Banners with a 4 px left bar |
| `form-status`, `form-status-error` | Action bar status line |
| `form-btn`, `form-btn-primary` | Secondary and primary buttons (36 px) |

The page container `form-page` (max 1440 px, container-query box) is a stylesheet class.

## Report Builder Classes (`report-*`)

The Report Builder popup (`01_Popups/Reports/ReportBuilder`, 2026-10-23) uses its own family:
steps (`report-step-dot`, `-dot-on`, `-label`, `-label-current`, `-label-done`, `-line`, `-line-done`, `-num`), tiles
and choices (`report-tile`, `-tile-selected`, `-tile-title`, `-tile-desc`, `-tile-meta`, `report-choice`,
`-choice-selected`, `-choice-btn`, `-choice-label`, `-choice-detail`, `report-icon-box`, `-icon-box-selected`),
KPIs (`report-kpi`, `-kpi-label`, `-kpi-value`, `-kpi-detail`), layout (`report-surface`, `report-bar-top`,
`-bar-mid`, `-bar-bottom`, `report-tab`, `-tab-active`, `report-row`, `-row-name`, `report-advanced`,
`-advanced-open`) and text (`report-title`, `-subtitle`, `-heading`, `-hint`, `-sum-value`).

## Admin Classes (`admin-*`)

The redesigned admin pages (User Management, Roles & Permissions, 2026-10-23) use `admin-*`:
lists and rows (`admin-list-item`, `-list-item-selected`, `admin-row`, `-row-label`, `admin-cell`, `-cell-text`,
`-cell-text-muted`, `-cell-click`, `-cell-changed`), the matrix (`admin-matrix-head`, `admin-head-label`,
`admin-head-sub`, `admin-group`, `admin-group-name`), tabs (`admin-tabs`, `admin-tab`, `admin-tab-active`),
chips and status (`admin-chip`, `admin-count`, `admin-dot`, `admin-status-pending`, `admin-bar-pending`), icons
(`admin-ico-on`, `-ico-off`, `-ico-muted`), avatars (`admin-avatar`, `-avatar-selected`) and text (`admin-role-name`,
`admin-item-title`, `admin-desc`, `admin-note`, `admin-sub`, `admin-key`, `admin-section-label`, `admin-empty-title`,
`admin-toolbar`, `admin-option`, `admin-option-on`, `admin-btn-danger`).

## Faceplate Classes

`faceplate-section`, `-section-card`, `-section-title`, `faceplate-title`, `faceplate-kpi-label`,
`faceplate-fault-chip`, `-fault-code`, `faceplate-cmd-btn`, `-cmd-btn-active`, `-cmd-btn-bypass`,
`faceplate-mode-btn-label`, `-mode-code`, `faceplate-interlock-sts`, `faceplate-bypass-banner`,
`faceplate-alarm-name`, `-alarm-notes`, `faceplate-config-empty`, `faceplate-stub`. The shell's own layout classes
(`faceplate`, `faceplate-tabs-vertical`, `faceplate-trend-wide`, `faceplate-content`, `faceplate-buttons-<n>`) are in
the stylesheet.

Every class's exact CSS and the views that use it are in the generated
[Style Class Catalog](../reference/style-classes.md).
