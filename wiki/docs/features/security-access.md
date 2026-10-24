---
title: Security Access (Login Required)
sidebar_position: 15
description: Every Perspective page, popup and WebDev resource in the BH project requires a login. What an anonymous browser can reach, and how the WebDev session check works.
sources:
  - docs/security-access.md
  - gateways/standard/data/projects/BH/ignition/script-python/shared/WebAuth/code.py
last_verified: 2026-10-24
---

# Security Access (Login Required)

## What it does

Decision (2026-10-24): **nothing in the project is open to a browser that has not logged in.** An anonymous visitor
who types any HMI address, including a deep link to a page or a popup, sees only the "You must log in to continue"
screen. The same holds for the pages the HMI embeds from the gateway's WebDev module (the globe map and the 3D PLC
rack).

## What is locked down

| Area | Setting | Where to see it |
|---|---|---|
| Perspective project `BH` | Project session permission is **Authenticated** (all of). Every page, deep link and popup, including `/no-view`, needs a login. | Designer > Project > Properties > Perspective > Permissions |
| Perspective project `Lightspeed-FrontEnd` | Same | same, in that project |
| WebDev `BH/globe/map` (globe page) | Served only to a browser that holds a logged-in BH Perspective session; otherwise a 401 JSON answer | Designer > Web Dev > `globe` > `map` |
| WebDev `BH/globe/mapMarkers` | Reads need a logged-in session (or HTTP Basic for tools); the hover / navigate relay also needs a signed token; config writes need HTTP Basic plus an admin role | Designer > Web Dev > `globe` > `mapMarkers` |
| WebDev `BH/rack3d/*` | Same session check; see [PLC Rack 3D](./plc-rack-3d.md) | Designer > Web Dev > `rack3d` |
| WebDev `Lightspeed-FrontEnd/*` | HTTP Basic with the `default` user source; writes also need the Administrator role | each resource's Require Auth setting |

### The WebDev session check

WebDev's own **Require Auth** option is HTTP Basic, which would pop a browser login dialog inside the Perspective
iframe. Text resources have no auth option at all. So the BH WebDev resources are small **Python resources** that
call the project script library function `shared.WebAuth.perspectiveUser(request)`. It reads the HTTP session of the
request (the same cookie the Perspective client uses), finds the BH Perspective session in it and accepts it only
when that session is logged in **and** authorized. An anonymous request gets a **401** JSON answer with no Basic
prompt; a logged-in user sees nothing extra. This relies on Perspective internals of Ignition 8.3.7, so recheck the
WebDev pages after a gateway upgrade.

## What an anonymous browser can still reach

The gateway web UI is unchanged: Config > Security > General keeps Gateway Access, Read / Write and Designer on
authenticated roles. Only what the login screens and health checks need stays public:

| URL | Anonymous result |
|---|---|
| `/StatusPing` | 200, `{"state":"RUNNING"}` (health checks, the trial watcher) |
| `/system/gwinfo` | 200 (version, edition; the Designer Launcher) |
| gateway web UI `/app/*` | the shell only: "You must be logged in" |
| `/data/api/v1/trial` | 200 (trial seconds left) |
| every other `/data/api/v1/*` | 401 |
| `/data/perspective/client/<project>/*` | the client shell plus the login screen |
| Perspective themes, icons, fonts, co-branding logo | 200 (static, needed by the login screen) |

## How to check it

1. Open a private browser window and go to
   `http://localhost:19088/data/perspective/client/BH/operations/plcs/RCP1`. You must get only the login screen.
2. Open `http://localhost:19088/system/webdev/BH/globe/map` in the same window. You must get a 401.
3. Log in to the HMI in another tab; the globe and the 3D rack iframes then load without a second prompt.

## How To Change It

- **Perspective session permission:** Designer > Project > Properties > Perspective > Permissions. Keep
  **Require Authentication** on with an Authenticated security level; page-level permissions are not used.
- **Gateway access (web UI, Designer):** Gateway web UI > Config > Security > General > Gateway Access, Read, Write
  and Designer permissions.
- **A new WebDev resource in BH:** create a Python resource (Designer > Web Dev > right-click > New Python Resource)
  and begin `doGet` with the session check:

  ```python
  if not shared.WebAuth.perspectiveUser(request):
  	return shared.WebAuth.deny(request)   # 401 JSON, no Basic prompt
  ```

  Clients that are not a browser (other systems) should use the resource's per-method **Require Auth**
  (HTTP Basic) instead.
- **A resource you delete** keeps answering 500 until the next gateway restart, then 404.

## Known limitations and parked items

Open decisions (OPC UA server access, the SQL Server port, the wiki, the Edge gateway, published ports and the
charting library CDN) are listed in `docs/TODO.md` under "Needs A Decision (Security, 2026-10-24)".

Source of truth: `docs/security-access.md`.
