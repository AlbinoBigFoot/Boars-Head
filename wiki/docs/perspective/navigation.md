---
title: Navigation
sidebar_position: 2
description: The BH nav tree (00_Docked/Navigation custom.items mirrored in the _Config/Navigation tag), its data flags, local vs enterprise mode, the /no-view fallback and the Header route guard.
sources:
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/Navigation/view.json"
  - "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views/00_Pages/00_Docked/Header/view.json"
  - "gateways/standard/data/projects/BH/ignition/script-python/Navigation/Nav/code.py"
  - "gateways/standard/data/projects/BH/ignition/script-python/Navigation/Faceplate/code.py"
  - "docs/local-groveport-mode.md"
last_verified: 2026-10-24
---

# Navigation

The left dock (`plant-nav`) shows one Perspective **Tree** component. Every row in it is an item in a JSON list,
and a click on a row either navigates to a page, opens a faceplate, or just expands a folder.

![Nav dock](/img/perspective/nav-dock.png)

| What | Where |
|---|---|
| Tree view | `00_Pages/00_Docked/Navigation` ([reference](./reference/views/00-pages/00-docked/navigation.md)), Tree component `root/Tree` |
| Item list (source) | the view's custom property **`view.custom.items`** |
| Mirror tag | `[default]_Config/Navigation` (Document tag, a copy of the same list) |
| Script | `Navigation.Nav` (navigate, page titles, item lookups) and `Navigation.Faceplate` (open a faceplate) - see [Scripting](../scripting/index.md) |
| Full current tree | [Nav Tree Items](./reference/nav-tree.md) (generated) |

## Why There Are Two Copies

- The **Tree** shows `view.custom.items` of the Navigation view (through a transform, below).
- **`Navigation.Nav.getNavItems()`** reads the **tag** `[default]_Config/Navigation`. Page titles in the nav header
  (`Navigation.Nav.pageTitle`), alarm-to-page lookups and `findItemPath` use it.

The two must match. **After you edit the tree in the Designer, copy the view's `custom.items` into the tag** (see
[Sync The Tag](#sync-the-tag) below), or page titles drift (this once titled `/sensors` as "GROVEPORT").
`00_Pages/00_Docked/TempNav` is an older copy of the Navigation view; nothing docks it.

## The Current Tree (Local Groveport Mode)

```text
Boars Head                      -> Utility Overview (home icon in local mode)
  Groveport                     -> Utility Overview
    Utility Overview            /plants/groveport/utility-overview
    Freezer, SuperChill, Club, Palletizing, East PH, West PH, Dock
      CG-xx                     /cg-xx  (each CG has Devices > Evaporator / Valves -> faceplates)
    Machine Room                /machine-room
      Devices > Tanks, Comps, Valves, Pumps, Exhaust Fans, Sensors, Rupture Disks, Safety Relays ...
    Condensers                  /condensers
      Devices > Condensers (fans), Pumps, Valves, Sensors, Tanks, Level Switches, Sequences
    Operations
      Alarm Status              /alarms
      Alarm Journal             /alarms/journal
      Trending                  /trending
      Saved Trends              /trending/saved
      Out Of Service Log        /operations/out-of-service      (permission OutOfService/View)
      Forms > Daily Rounds Log, NH3 Shift Log, Annual P&ID Verification, Form History
      Reports                   /operations/reports             (permission Reports/Page)
      PLCs > RCP1               /operations/plcs/RCP1
    Admin
      Audit Log                 /operations/audit               (permission AuditLog/View)
      User Management           /operations/users               (permission UserManagement/Edit)
      Roles & Permissions       /operations/roles-permissions   (permission RolesPermissions/Edit)
```

Folders such as Freezer have no page of their own: clicking them only expands them (the per-area dashboards were
removed on 2026-09-29).

## Item Shape

Each item is a Perspective tree item (`label`, `icon`, `expanded`, `items`) plus a `data` object that BH uses for
behaviour:

```json
{
  "label": "Out Of Service Log",
  "icon": {"path": "material/sticky_note_2"},
  "data": {
    "action": "page",
    "page": "/operations/out-of-service",
    "viewPath": "00_Pages/Boars Head/Operations/OutOfService/OutOfServiceLog",
    "tagPath": "",
    "permission": "OutOfService/View",
    "title": "Groveport Out Of Service Log"
  },
  "items": []
}
```

| `data` key | Meaning |
|---|---|
| `action` | `page` (navigate), `faceplate` (open a popup), or `''` (folder: expand only). |
| `page` | A page-config URL. Navigation only happens if the route exists. |
| `viewPath` | The view behind the page, or the faceplate view to open (`01_Popups/00_Faceplates/...`). |
| `tagPath` | For a faceplate item: the device UDT instance, for example `[default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 2`. A leaf with only a `tagPath` opens that device's faceplate through `Navigation.Faceplate.openDevice` (it reads the instance's `typeId`). |
| `title` | Overrides the computed page title shown at the top of the nav dock. |
| `hidden` | `true` = kept in the list but not shown. Use this instead of deleting a node. |
| `demo` | Shown despite `hidden` when enterprise mode is on (`[default]_Config/DemoEnterpriseNav = true`). |
| `demoPage` / `localPage` | Where the item goes in enterprise / local mode (Boars Head: `/enterprise` vs the Utility Overview). |
| `localIcon` | Icon used in local mode (Boars Head shows `material/home` instead of the globe). |
| `flattenLocal` | In local mode the folder is removed and its children are lifted into the parent (area > Utility > CG becomes area > CG). |
| `permission` | A Roles & Permissions row `Device/Action`. The item is shown only when `session.custom.Permissions.<Device>.<Action>` is true. A folder whose children were all withheld this way disappears too. |
| `adminOnly` | Older flag: shown only when `session.custom.Administrator` is true. `permission` wins when both are set. |
| `parkedPage` / `parkedViewPath` | Notes of where an item used to go before it was parked. Not read by the scripts. |

## How The Tree Is Filtered

`root/Tree.props.items` is an **expr-struct** binding over `view.custom.items`, `session.custom.Administrator`,
`session.custom.Permissions` and the enterprise switch tag, with a script transform that:

1. drops items whose `permission` is not granted, or `adminOnly` items for non-admins;
2. drops `hidden` items, unless enterprise mode is on and the item has `demo`;
3. drops a folder whose children were all withheld by permission;
4. in local mode, lifts the children of `flattenLocal` folders into their parent and swaps in `localIcon`.

Because the binding depends on `session.custom.Permissions`, the tree re-filters on login, logout and role change
without a page reload. A change script on `props.items` then widens the dock (260 to 480 px) so the longest
expanded label fits without a horizontal scrollbar (`system.perspective.alterDock('plant-nav', ...)`).

Other Tree pieces:

- `custom.itemPath` (expr-struct over `page.props.path` and the items) finds the item for the current page with
  `Navigation.Nav.findItemIndex`, and its change script expands and selects that branch, collapsing branches it
  auto-expanded for the previous page.
- `onItemClicked` calls `Navigation.Nav.navigate(event.data)`. It returns `False` for a folder, so the selection
  stays on the current page.
- The **Search** box at the bottom filters by label: matches get the `nav-search-hit` class, their parents
  `nav-search-parent`.
- The nav header label is `Navigation.Nav.pageTitle(page.props.path)`: the chain of labels to the current page,
  skipping grouping folders (Boars Head, Utility, Devices, Operations, Admin), for example "Groveport Machine Room
  Tanks". A node's `data.title` overrides it.

## What A Click Does (`Navigation.Nav.navigate`)

1. If the item has `demoPage` / `localPage`, pick the one for the current mode.
2. `action = faceplate` (or a `viewPath` under `01_Popups/00_Faceplates/`): open the faceplate with
   `Navigation.Faceplate.openFaceplate` (popup id `nav-fp-<tagPath>`). This checks `Faceplates/Open` first; a
   session without it gets nothing.
3. `action = page` or a `page` value: navigate **only if the route exists** in page-config (the route list is read
   with `system.perspective.getProjectInfo()` and cached 60 s). Otherwise nothing happens.
4. A leaf with only `tagPath`: open that device's faceplate (`Navigation.Faceplate.openDevice`).
5. A few legacy `viewPath` values map to fixed routes (`/trending`, `/alarms`, ...).

## The `/no-view` Fallback

`/no-view` opens `00_Pages/Boars Head/NoViewPath`, an empty placeholder (one blank label, so the page body
renders blank, as in the screenshot below). It means "this item has no page yet".

- The constant `Navigation.Nav.NO_VIEW_PAGE` names it.
- Since 2026-09-24 the nav tree no longer sends folders or unknown routes there: `navigate()` simply stays on the
  current page.
- It is still used by embedded content switches: the device-type pages (`/pumps` ...) fall back to `NoViewPath`
  when `custom.overviewMode` has an unexpected value, and the Evaporator component's `navPage` click goes through
  `navigate()`.

![No view placeholder](/img/perspective/no-view.png)

## Local vs Enterprise Mode

The project serves two deployments behind one Boolean tag, **`[default]_Config/DemoEnterpriseNav`**:

| Mode | Tag | Nav | `/` and enterprise URLs |
|---|---|---|---|
| **Local Groveport** (default, live) | `false` | Groveport only, area Utility folders flattened, home icon | Redirect to `/plants/groveport/utility-overview` |
| Enterprise demo | `true` | Other plants, Enterprise Operations, Production, every area's EPMS / Production nodes | Open normally (`/enterprise` is the globe) |

Switch it in the Designer Tag Browser (`[default]_Config` > `DemoEnterpriseNav`, set the value). Never edit the tag
file on disk (that blanks the live value). Read the tag to see the current mode.

Nothing enterprise was deleted: the views, routes, tags and nav nodes are all still in the project. The full
procedure, the list of hidden routes and how to add a plant or area are in `docs/local-groveport-mode.md` and on
[Deployment](../deployment/index.md).

### The Route Guard

The Header (docked on every page) has a custom property **`custom.localRouteGuard`**:

- Its **expression** returns `/plants/groveport/utility-overview` when the switch is off **and**
  `page.props.path` is one of the enterprise routes (a `|`-separated list inside the expression), otherwise `''`.
- Its **change script** runs `system.perspective.navigate(...)` when the value is not empty. That is the only
  script part, a one-shot command.
- **Fail-safe:** a missing or bad tag reads as enterprise (`coalesce(..., true)`), so a cold binding never bounces
  an enterprise user.

When you add an enterprise route in Page Configuration, add its path to the route list in this expression so local
mode redirects it.

## How To

### Hide Or Show A Node

1. In the Designer open `00_Pages/00_Docked/Navigation`, select the root, and edit **custom > items** in the
   Property Editor (expand the tree to the node).
2. Set `data.hidden: true` on the node (add `data.demo: true` if it should still show in enterprise mode). Don't
   delete nodes.
3. [Sync the tag](#sync-the-tag), save, and test in a session.

### Add A Page To The Nav

1. Create the view and add a route in **Page Configuration** (`page-config/config.json`).
2. Add an item under the right folder with `action: "page"`, `page`, `viewPath` and an icon. Gate it with
   `data.permission` (a Roles & Permissions row) if it isn't for everyone.
3. [Sync the tag](#sync-the-tag), save, then check the title at the top of the nav dock.

### Move A Node

In `custom.items` cut the node's object and paste it into the `children` list of its new parent (or reorder it within
its list), [sync the tag](#sync-the-tag), save, and test.

### Sync The Tag

1. Designer > Project Browser > Perspective > Views > `00_Pages/00_Docked/Navigation`, select the root.
2. In the Property Editor right-click `custom.items` > **Copy**.
3. Tag Browser > `[default]_Config` > `Navigation` > open the tag editor > **Value** > paste the copied JSON > OK.
4. Check the title at the top of the nav dock on a page you changed.

### Add A Device Faceplate Leaf

Add an item with `action: "faceplate"`, `viewPath` = the faceplate view and `tagPath` = the UDT instance, or just
the `tagPath` and let `openDevice` pick the faceplate from the UDT type.
