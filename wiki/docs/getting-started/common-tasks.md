---
title: Common Tasks
sidebar_position: 8
description: Short Designer and Gateway web UI recipes for the changes made most often - add a device, rename a label, add a nav item, add a permission, add an alarm, change a theme colour, add a graphic from Figma, back up and restore.
sources:
  - docs/local-groveport-mode.md
  - docs/central-alarming.md
  - docs/themes.md
last_verified: 2026-10-24
---

# Common Tasks

Every recipe is a Designer or Gateway web UI change. The Designer saves the project files itself; after each recipe
**save** (`Ctrl+S`) and **test in a Perspective session** (Designer > Perspective > Launch Session). Then commit the
changed project and tag files ([Making A Change](../git-workflow/making-a-change.md)).

Where things are in the Designer:

| Panel | Holds |
|---|---|
| **Project Browser** > Perspective > **Views** | every view (`00_Pages`, `01_Popups`, `02_Components`, `03_Elements`) |
| Project Browser > Perspective > **Page Configuration** | URL routes |
| Project Browser > Perspective > **Styles** and **Stylesheet** | style classes and the Advanced Stylesheet |
| Project Browser > **Scripting** > Project Library | the `shared.*` scripts; **Gateway Events** are next to it |
| Project Browser > **Data** > Named Queries | SQL queries |
| **Tag Browser** (All Tags, UDT Definitions tabs) | tags and UDTs |

## 1. Add A Device

1. Tag Browser > All Tags > `[default]Boars_Head` > `GrovePort` > the area > the type folder (for example `Pumps`).
2. Right-click the type folder > **New Tag > Data Type Instance** (or copy a sibling and rename it). Choose the UDT
   (for example `Devices/Pump`).
3. Fill in the parameters (`PlcDevice` and the `<Part>Tag` values, the PLC object names) and tick **Enabled** on the
   PLC parts the controller really has (`Motor`, `Intlk`, ...).
4. Add a nav item for it if it needs one (recipe 5). Device list pages pick up new instances by themselves.
5. Open its faceplate in a session and check every field shows a value or the gray dash.

More: [Device UDTs](../tags/udts/device-udts.md#adding-a-new-device).

## 2. Rename A Label Or Change Text

1. Open the view (Project Browser > Perspective > Views, or double-click the component in a session with the Designer
   open and use **Open In Designer**).
2. Select the label in the canvas or the **Component Tree**.
3. Edit `props.text`. If the text is bound, edit the binding or the tag it reads instead. Use **Title Case**.
4. Save and check the page.

## 3. Change How A Setpoint Or Value Is Shown

1. Open the view and select the numeric component (a label or a value element).
2. Property Editor > `props.text` (or `props.value`): change the binding's format. In an expression use
   `numberFormat(value, '0.0')` for one decimal; units come from the `props.unit` / a neighbouring label.
3. Keep the null-safe wrapper: `if(isGood(tag(p)), tag(p), null)` so a bad value shows the gray dash.
4. Save and test.

## 4. Change An Alarm Limit

- **On one device:** open its faceplate > **Alarm Configuration** tab (Engineering and up) and change the limit or
  priority.
- **For every device of a type:** Tag Browser > UDT Definitions > the library type (for example `PLC/P_AIn`) > the
  member (`Sts_Hi`) > Edit Tag > **Alarming**. See [Alarms](../features/alarms.md#how-to-change-it).

## 5. Add A Nav Item

1. Create the view and a route: Project Browser > Perspective > Page Configuration > add a page with the URL and the
   view path.
2. Open `00_Pages/00_Docked/Navigation`, select the root, and edit `custom.items` in the Property Editor: add an item
   under the right folder with `action: "page"`, `page` (the URL), `viewPath` and an icon. Add `data.permission` if it is
   not for everyone.
3. Copy `custom.items` (right-click > Copy) and paste it into the tag `[default]_Config/Navigation` (Tag Browser >
   `_Config` > `Navigation` > Edit Tag > Value).
4. Save and check the nav and the page title.

More: [Navigation](../perspective/navigation.md).

## 6. Hide Or Move A Nav Item

In `custom.items` of the Navigation view set `data.hidden: true` on the node (hidden nodes are kept), or cut and paste
the node under its new parent. Copy the items into `_Config/Navigation` as in recipe 5.

## 7. Add A Permission Row

1. Tag Browser > `[default]_Config` > `RolesPermissions` > Edit Tag > edit the **Value** dataset: add a row with
   `Devices`, `Actions`, `Description`, and tick the roles that may use it.
2. Optionally add a line for it in `_Config/Security/PermissionCatalog` (Key, Category, Label, Order) so it lands in
   the right group on the Roles & Permissions page.
3. Gate the control: set its `enabled` or `visible` binding to `session.custom.Permissions.<Device>.<Action>`, and
   check it on the server with `shared.Security.require(...)` in the script it calls.
4. Test with a user of each role.

More: [Roles And Permissions](../features/roles-permissions.md#how-to-change-it).

## 8. Add A User Or Change A User's Roles

Open the HMI page **Admin > User Management** (Administrator only) and add or edit the user, or use the Gateway web
UI: Config > Security > User Sources > `default`.

## 9. Add A Source To The Report Builder

Add the named queries (Project Browser > Named Queries > `Reports`), a fetcher in `shared.Reports` (Project Library),
the source's entry in the Document tag `[default]_Config/Reports/Catalog` (raise its `version`), and a
`Reports/<Source>` permission row. Steps:
[Report Builder](../features/custom-reports.md#how-to-change-it).

## 10. Change A Theme Colour

1. For a one-off view, don't use a raw colour: set `props.style.classes` to a theme class (`bg-page`,
   `container-card`, `text-muted`).
2. For the theme itself: Designer > Project Browser > Perspective > Styles > Themes > the theme (`light-cool`,
   `dark-cool`, `light-warm`, `dark-warm`) and edit its variables (neutral scale, accents).
3. Alarm colours (`--alarm-critical` and so on) are fixed on purpose: don't change them.
4. Save, hard-refresh the client (`Ctrl+F5`) and check all four themes.

More: [Themes](../perspective/styling/themes.md).

## 11. Add A Historized Tag To A Trend

1. Tag Browser > the tag (for a device member, the UDT definition member) > Edit Tag > **History**: enable it, sample
   mode On Change, deadband, tag group, provider `historian`.
2. In a session right-click any value that shows it > **Add To Trend**, then open Operations > Trending.
3. If a component has no right-click menu, add the `onContextMenu` event that calls `shared.TrendContext.menu(...)`
   ([Trending](../features/trending.md#how-to-change-it)).

## 12. Change A Tag Group Rate

Gateway web UI > Config > Tags > Tag Groups > select the group > change Mode / Rate / Leased Rate > Save. See
[History And Polling](../tags/history.md#how-to-change-it).

## 13. Add A Code-To-Text Enum

Tag Browser > `_Config/Enums/<Group>` > New Memory Tag (DataSet) with columns `value`, `label`, `short`, `selectable`.
Details: [Defrost Enums](../features/defrost-enums.md#how-to-change-it).

## 14. Add An Operator To The Forms

Tag Browser > `[default]_Config/Forms/Operators` > append `, New Name` to the value.

## 15. Add A PLC Card Or A PLC To The Rack Page

Tag Browser > UDT Definitions > `PLC/Modules` (card) or `PLC/Sites` (site), then the instance and `Rack` document and a
nav item. Steps: [PLC Rack UDTs](../tags/udts/plc-rack.md#how-to-add-a-card-or-a-plc). New point labels from an L5X
export are loaded by the system integrator.

## 16. Switch Between Local And Enterprise Mode

Tag Browser > `[default]_Config` > `DemoEnterpriseNav` > set the value (`false` local, `true` enterprise).
See [Deployment Modes](../deployment/deployment-modes.md#how-to-switch-modes).

## 17. Add A Named Query

Project Browser > Named Queries > right-click > **New Named Query**; choose the type and database `ignition`, paste the
SQL, add parameters, **Test Query**, save, and call it with `system.db.runNamedQuery('<Folder>/<Query>', {...})`.
See [Named Queries](../scripting/named-queries.md#adding-a-query).

## 18. Add A Graphic From Figma

1. In Figma select the frame or component. In the right panel use **Export** > **SVG** > **Export**.
2. In the Designer open the target view and **drag the `.svg` file** from File Explorer onto the view canvas.
3. When the Designer asks how to import it, choose **Embedded**: the SVG is embedded in the view instead of linked to
   an external file.
4. Position and size it (Property Editor `position`), then bind its fill, stroke or visibility to tags as needed.
5. Save and test in all four themes.

More: [Figma Workflow](../perspective/styling/figma-workflow.md).

## 19. Back Up And Restore

- **Back up:** Gateway web UI > Platform > System > Backup & Restore > **Download Backup** (a `.gwbk`). Take one before
  any restart you are unsure about and before and after a deployment. Keep it outside the repo and never commit it.
- **Restore:** same page > **Restore** > choose the `.gwbk`. The gateway restarts with that configuration.
- **Tags only:** Tag Browser > right-click a folder > **Export Tags**; restore with **Import Tags**.
- **Project only:** Designer > File > Export / Import.

More: [Backups](../gateway/backups.md).

## 20. Change A Gateway Setting

Use the [Gateway UI Map](../gateway/gateway-ui-map.md): it lists where each setting lives (devices, databases,
historian, alarm journal, audit profiles, security, co-branding, tag groups) in the Gateway web UI.
