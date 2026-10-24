---
title: First Login
sidebar_position: 3
description: Open the BH HMI, the 8.3 Gateway web UI and the Designer against the lab gateway.
sources:
  - gateways/standard/data/config/resources/core/ignition/security-properties/config.json
  - gateways/standard/data/config/resources/core/ignition/identity-provider/default/config.json
  - gateways/standard/data/config/resources/core/ignition/cobranding/config.json
  - gateways/standard/data/projects/BH/com.inductiveautomation.perspective/page-config/config.json
last_verified: 2026-10-24
---

# First Login

You need a user in the gateway's internal user source **`default`**. Ask a gateway Administrator to create one
(Admin > User Management in the HMI, or Platform > Security > User Sources in the Gateway web UI). Your roles decide
what you can do: see [Security](../gateway/security.md).

## The HMI (Perspective Client)

Open **http://localhost:19088/data/perspective/client/BH**.

1. The gateway shows the Boar's Head **co-branded** login screen (medallion, `#F3F3F5` background, red `#B00828`
   buttons). It is served by the identity provider `default`, which authenticates against the user source `default`.
2. Sign in. The project requires the **Authenticated** security level for every session (project
   `session-permissions`), so there is no anonymous view.
3. In Local Groveport mode you land on **`/plants/groveport/utility-overview`** (the Utility Overview). The left dock
   is the plant navigation tree, the top dock is the header.

![The BH HMI: Groveport Utility Overview in a dark theme](/img/getting-started/hmi-utility-overview.png)

What you are looking at:

| Area | View | Notes |
|---|---|---|
| Header (top dock) | `00_Pages/00_Docked/Header` | Hamburger, Boar's Head logo (click = home), One Shot badge (contact card), lock / permissions badge, user, Out Of Service notes, alarm bell with count, trend, settings gear (theme) |
| Navigation (left dock) | `00_Pages/00_Docked/Navigation` | Tree of `view.custom.items`, mirrored in the `[default]_Config/Navigation` tag; search box and clock at the bottom |
| Page body | the page's primary view | Here `00_Pages/Groveport/Utility/Overview`, built by `scripts/_build_groveport_utility_overview.py` |
| Legend (right dock, on demand) | `00_Pages/00_Docked/Legend` | Status icon legend |

More in [Perspective](../perspective/index.md).

- **Session timeout**: the identity provider ends an idle session after 30 minutes.
- **Themes**: the settings gear switches between `light-cool`, `dark-cool`, `light-warm` and `dark-warm`
  (`session.props.theme`).
- **Bookmarks**: every page has a URL (93 routes in `page-config`), so you can bookmark a CG page such as `/cg-e2`.

## The Gateway Web UI

Open **http://localhost:19088** and sign in with a user that has the **Administrator** role (the gateway's read and
write permissions both require `Authenticated/Roles/Administrator`; API keys with the `Write` level can also write).

The 8.3 UI has six sections in the left rail: **Home, Platform, Connections, Network, Services, Diagnostics**. The
search box at the top ("Search Gateway") jumps to any settings page. The [Gateway UI Map](../gateway/gateway-ui-map.md)
lists where every setting used by this project lives.

## The Designer

The Designer is the desktop IDE for Ignition projects.

1. In the Gateway web UI go to **Home > Designer > Download** and install the **Designer Launcher** for Windows.
2. Start the Designer Launcher, click **Add Designer**, and add the gateway by URL: `http://localhost:19088`.
   It appears as `bh-standard`.
3. Click **Open Designer**, sign in (your user needs the **Administrator** role; Designer access is restricted to it
   in Platform > Security > General Settings), and open the project **BH**.
4. The gateway gives the Designer up to 4096 MB of RAM (`designerRAM` in the gateway settings).

Where things are in the Designer:

| Designer Location | What | Files On Disk (under `gateways/standard/data/projects/BH/`) |
|---|---|---|
| Project Browser > Perspective > Views | All views (`00_Pages`, `01_Popups`, `02_Components`, `03_Elements`, `98_Configuration`) | `com.inductiveautomation.perspective/views/**/view.json` |
| Project Browser > Perspective > Styles | Style classes | `com.inductiveautomation.perspective/style-classes/**` |
| Project Browser > Perspective > Page Configuration | Routes, docks | `com.inductiveautomation.perspective/page-config/config.json` |
| Project Browser > Perspective > Session Events / Session Props | Session custom props | `com.inductiveautomation.perspective/session-props/` |
| Project > Project Properties > Perspective > Stylesheet | The Advanced Stylesheet | `com.inductiveautomation.perspective/stylesheet/stylesheet.css` |
| Project Browser > Scripting > Project Library | `shared.*`, `Navigation.*`, `L5K.*` | `ignition/script-python/**/code.py` |
| Project Browser > Scripting > Gateway Events | Tag change and timer scripts | `ignition/tag-change/**`, `ignition/timer/**` |
| Project Browser > Data > Named Queries | SQL named queries | `ignition/named-query/**` |
| Project Browser > Reports | PDF reports | `com.inductiveautomation.reporting/reports/**` |
| Project Browser > Web Dev | WebDev endpoints (globe, PLC rack 3D) | `com.inductiveautomation.webdev/resources/**` |
| Tag Browser (bottom left) | Tags, UDT definitions (`_types_`), tag groups (Edit Tag Groups icon) | `config/resources/core/ignition/tag-definition/**`, `tag-type-definition/**`, `tag-group/**` |

:::caution Designer saves
A Designer save writes the project's `view.json` and `resource.json` files on disk, so every save shows up in
`git status`. Save only what you mean to change, and commit it with the work that needs it.
:::

Designer saves go through the gateway, which writes correct resource metadata itself. After a `git pull`, merge or
checkout use **File > Update Project** in the Designer ([Merge Conflicts](../git-workflow/merge-conflicts.md)).
