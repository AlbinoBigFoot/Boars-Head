---
title: "Themes And Icons"
sidebar_label: "Themes And Icons"
description: "Gateway Perspective themes (folders, imports, neutral scale) and the icon libraries."
generated: true
sidebar_position: 9
---

:::note

:::


Themes and icon libraries are **gateway** config resources under `gateways/standard/data/config/resources/core/com.inductiveautomation.perspective`, not part of the project. `session.props.theme` picks the theme folder.

## Themes

### dark

14 files (full base). index.css imports: `./variables.css`, `../light/fonts.css`, `./globals.css`, `../light/app/index.css`, `../light/common/index.css`, `../light/designer/index.css`, `../light/palette/index.css`, `./palette/index.css`.

| Neutral | Value |
|---|---|
| `--neutral-10` | `#121619` |
| `--neutral-20` | `#21272A` |
| `--neutral-30` | `#343A3F` |
| `--neutral-40` | `#4D5358` |
| `--neutral-50` | `#697077` |
| `--neutral-60` | `#878D96` |
| `--neutral-70` | `#A2A9B0` |
| `--neutral-80` | `#C1C7CD` |
| `--neutral-90` | `#DDE1E6` |
| `--neutral-100` | `#F2F4F8` |

### dark-cool

4 files (thin variant). index.css imports: `./variables.css`, `../light/fonts.css`, `../dark/globals.css`, `../light/app/index.css`, `../light/common/index.css`, `../light/designer/index.css`, `../light/palette/index.css`, `../dark/palette/index.css`. variables.css imports `../dark/variables.css`.

| Neutral | Value |
|---|---|
| `--neutral-10` | `#121619` |
| `--neutral-20` | `#21272A` |
| `--neutral-30` | `#343A3F` |
| `--neutral-40` | `#4D5358` |
| `--neutral-50` | `#697077` |
| `--neutral-60` | `#878D96` |
| `--neutral-70` | `#A2A9B0` |
| `--neutral-80` | `#C1C7CD` |
| `--neutral-90` | `#DDE1E6` |
| `--neutral-100` | `#F2F4F8` |

### dark-warm

4 files (thin variant). index.css imports: `./variables.css`, `../light/fonts.css`, `../dark/globals.css`, `../light/app/index.css`, `../light/common/index.css`, `../light/designer/index.css`, `../light/palette/index.css`, `../dark/palette/index.css`. variables.css imports `../dark/variables.css`.

| Neutral | Value |
|---|---|
| `--neutral-10` | `#171414` |
| `--neutral-20` | `#272525` |
| `--neutral-30` | `#3C3838` |
| `--neutral-40` | `#565151` |
| `--neutral-50` | `#736F6F` |
| `--neutral-60` | `#8F8B8B` |
| `--neutral-70` | `#ADA8A8` |
| `--neutral-80` | `#CAC5C4` |
| `--neutral-90` | `#E5E0DF` |
| `--neutral-100` | `#F7F3F2` |

### light

74 files (full base). index.css imports: `./variables.css`, `./fonts.css`, `./globals.css`, `./app/index.css`, `./common/index.css`, `./designer/index.css`, `./palette/index.css`.

| Neutral | Value |
|---|---|
| `--neutral-10` | `#F2F4F8` |
| `--neutral-20` | `#DDE1E6` |
| `--neutral-30` | `#C1C7CD` |
| `--neutral-40` | `#A2A9B0` |
| `--neutral-50` | `#878D96` |
| `--neutral-60` | `#697077` |
| `--neutral-70` | `#4D5358` |
| `--neutral-80` | `#343A3F` |
| `--neutral-90` | `#21272A` |
| `--neutral-100` | `#121619` |

### light-cool

4 files (thin variant). index.css imports: `./variables.css`, `../light/fonts.css`, `../light/globals.css`, `../light/app/index.css`, `../light/common/index.css`, `../light/designer/index.css`, `../light/palette/index.css`. variables.css imports `../light/variables.css`.

| Neutral | Value |
|---|---|
| `--neutral-10` | `#F2F4F8` |
| `--neutral-20` | `#DDE1E6` |
| `--neutral-30` | `#C1C7CD` |
| `--neutral-40` | `#A2A9B0` |
| `--neutral-50` | `#878D96` |
| `--neutral-60` | `#697077` |
| `--neutral-70` | `#4D5358` |
| `--neutral-80` | `#343A3F` |
| `--neutral-90` | `#21272A` |
| `--neutral-100` | `#121619` |

### light-warm

4 files (thin variant). index.css imports: `./variables.css`, `../light/fonts.css`, `../light/globals.css`, `../light/app/index.css`, `../light/common/index.css`, `../light/designer/index.css`, `../light/palette/index.css`. variables.css imports `../light/variables.css`.

| Neutral | Value |
|---|---|
| `--neutral-10` | `#F7F3F2` |
| `--neutral-20` | `#E5E0DF` |
| `--neutral-30` | `#CAC5C4` |
| `--neutral-40` | `#ADA8A8` |
| `--neutral-50` | `#8F8B8B` |
| `--neutral-60` | `#736F6F` |
| `--neutral-70` | `#565151` |
| `--neutral-80` | `#3C3838` |
| `--neutral-90` | `#272525` |
| `--neutral-100` | `#171414` |

## Icon Libraries

Use an icon in a view as `<library>/<id>` (the Icon component `props.path`, or a nav item icon). `material/*` icons come with Ignition.

### equipment

File `gateways/standard/data/config/resources/core/com.inductiveautomation.perspective/icons/equipment/equipment.svg`, 13 icons.

| Icon path | Label | Views using it |
|---|---|---|
| `equipment/alarm_critical` | Alarm Critical | 0 |
| `equipment/alarm_high` | Alarm High | 0 |
| `equipment/alarm_medium` | Alarm Medium | 0 |
| `equipment/alarm_low` | Alarm Low | 0 |
| `equipment/devices` | Devices (Figma nav/devices) — hub / cross | 2 |
| `equipment/alarm_journal` | Alarm Journal — Option A: knockout bell + ring/hands clock | 2 |
| `equipment/trending` | Trending (Figma nav/trending) — chart axes + sparkline | 3 |
| `equipment/pump` | Pump (Figma nav/pump, base removed) — volute + shaft | 2 |
| `equipment/exhaust_fan` | Exhaust Fan — square radiator housing + feet + grille + impeller (matches device) | 2 |
| `equipment/compressor` | Compressor — bold oil sep + head + motor on skid (no rib cutouts) | 2 |
| `equipment/valve` | Valve — solenoid body (two wedges) + stem + actuator (matches SolenoidValve) | 2 |
| `equipment/conveyor` | Production — Conveyor (bold fill, optical match to material/offline\_bolt) | 2 |
| `equipment/rupture-disk` | Rupture disk (Figma nav/rupture-disk 358:1961) - disk holder with burst arrows | 2 |

## Material Icons In Use

<details>
<summary>104 material icons referenced in views</summary>

| Icon path | References |
|---|---|
| `material/ac_unit` | 157 |
| `material/device_hub` | 98 |
| `material/check_box_outline_blank` | 74 |
| `material/domain` | 25 |
| `material/check` | 22 |
| `material/miscellaneous_services` | 17 |
| `material/offline_bolt` | 16 |
| `material/close` | 15 |
| `material/opacity` | 13 |
| `material/location_on` | 11 |
| `material/show_chart` | 11 |
| `material/fullscreen` | 11 |
| `material/add` | 9 |
| `material/history` | 8 |
| `material/chevron_right` | 7 |
| `material/save` | 7 |
| `material/bookmarks` | 6 |
| `material/lock` | 6 |
| `material/build` | 5 |
| `material/memory` | 5 |
| `material/folder` | 5 |
| `material/get_app` | 5 |
| `material/info` | 5 |
| `material/check_circle` | 5 |
| `material/edit` | 5 |
| `material/notifications` | 4 |
| `material/sticky_note_2` | 4 |
| `material/person` | 4 |
| `material/settings` | 4 |
| `material/verified_user` | 4 |
| `material/toggle_on` | 4 |
| `material/format_list_numbered` | 4 |
| `material/notifications_active` | 4 |
| `material/refresh` | 4 |
| `material/lock_open` | 3 |
| `material/stop` | 3 |
| `material/folder_open` | 3 |
| `material/arrow_right` | 3 |
| `material/arrow_drop_down` | 3 |
| `material/check_box` | 3 |
| `material/delete_outline` | 3 |
| `material/print` | 3 |
| `material/settings_ethernet` | 3 |
| `material/crop_free` | 3 |
| `material/pan_tool` | 3 |
| `material/settings_backup_restore` | 3 |
| `material/assessment` | 3 |
| `material/public` | 2 |
| `material/home` | 2 |
| `material/developer_board` | 2 |
| `material/admin_panel_settings` | 2 |
| `material/unfold_more` | 2 |
| `material/unfold_less` | 2 |
| `material/arrow_back` | 2 |
| `material/assignment_ind` | 2 |
| `material/link` | 2 |
| `material/open_in_new` | 2 |
| `material/grid_on` | 2 |
| `material/3d_rotation` | 2 |
| `material/view_module` | 2 |
| `material/play_arrow` | 2 |
| `material/bookmark_border` | 2 |
| `material/error` | 2 |
| `material/delete` | 2 |
| `material/description` | 2 |
| `material/remove` | 2 |
| `material/fiber_manual_record` | 2 |
| `material/wb_sunny` | 1 |
| `material/nights_stay` | 1 |
| `material/whatshot` | 1 |
| `material/login` | 1 |
| `material/swap_horiz` | 1 |
| `material/menu` | 1 |
| `material/supervisor_account` | 1 |
| `material/arrow_forward` | 1 |
| `material/search_off` | 1 |
| `material/clear_all` | 1 |
| `material/person_add` | 1 |
| `material/person_remove` | 1 |
| `material/person_search` | 1 |
| `material/chevron_left` | 1 |
| `material/visibility` | 1 |
| `material/done` | 1 |
| `material/schedule` | 1 |
| `material/warning` | 1 |
| `material/replay` | 1 |
| `material/share` | 1 |
| `material/title` | 1 |
| `material/arrow_upward` | 1 |
| `material/arrow_downward` | 1 |
| `material/picture_as_pdf` | 1 |
| `material/tune` | 1 |
| `material/expand_more` | 1 |
| `material/hourglass_top` | 1 |
| `material/inbox` | 1 |
| `material/error_outline` | 1 |
| `material/block` | 1 |
| `material/content_copy` | 1 |
| `material/notification_important` | 1 |
| `material/not_interested` | 1 |
| `material/zoom_in` | 1 |
| `material/zoom_out` | 1 |
| `material/vertical_align_top` | 1 |
| `material/vertical_align_bottom` | 1 |

</details>
