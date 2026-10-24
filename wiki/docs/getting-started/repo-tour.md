---
title: Repository Tour
sidebar_position: 4
description: Every folder in the repo that matters, and what lives in it.
sources:
  - .gitignore
  - docker-compose.yml
  - gateways/README.md
last_verified: 2026-10-23
---

# Repository Tour

The repo is a **Docker Compose Ignition lab**: there is no application source in the usual sense. The deliverable is
the `BH` Perspective project, which you maintain in the Ignition Designer.

```text
Bors/
├── README.md                  Quick start
├── docker-compose.yml         The stack: two gateways, SQL Server, trial watcher, wiki
├── .env.example               Template for .env (secrets + host ports; .env is gitignored)
├── gateways/
│   ├── standard/data/         Bind mount = the Standard gateway's whole data folder
│   │   ├── projects/BH/       THE PROJECT: views, styles, scripts, named queries, reports, events
│   │   ├── projects/.resources/   Content-addressed blobs the gateway rewrites (never commit the churn)
│   │   └── config/resources/core/ Gateway config as files: tags, UDTs, tag groups, themes, icons, devices ...
│   └── edge/data/             Bind mount for the optional Edge gateway
├── sql/                       MSSQL schema scripts (trend configs, forms, Out Of Service, reports)
├── trial-watch/               The trial reset container (Dockerfile + watch_trial.py)
├── docs/                      Engineering notes per feature (the source material for this wiki)
│   ├── handoff/HANDOFF.md     Running work log (local only, gitignored)
│   ├── pax-mapping/           Device-by-device PlantPAx mapping reviews
│   ├── branding/              Official logo files + derived PNGs
├── wiki/                      This Docusaurus site (docs/, tools/gen_*.py, check_docs.py)
├── verify-screenshots/        Before/after captures from test passes
└── .planning/                 Planning documents (priorities, roadmap, state)
```

## Inside The Project (`gateways/standard/data/projects/BH/`)

| Folder | Content | Wiki Section |
|---|---|---|
| `com.inductiveautomation.perspective/views/` | Every Perspective view as `view.json` + `resource.json` (+ `thumbnail.png`) | [Perspective](../perspective/index.md) |
| `.../page-config/config.json` | URL routes and docks (header, nav, legend) | [Perspective](../perspective/index.md) |
| `.../style-classes/` | Perspective style classes (`Fonts/*`, `fs-*`, `faceplate-*` ...) | [Perspective](../perspective/index.md) |
| `.../stylesheet/stylesheet.css` | The Advanced Stylesheet (IA-internal, layout and state rules) | [Perspective](../perspective/index.md) |
| `.../session-props/`, `session-permissions/` | Session custom props (`session.custom.*`), login requirement | [Perspective](../perspective/index.md) |
| `ignition/script-python/` | Project library: `shared.*` (most logic), `Navigation.*`, `L5K.*` | [Scripting](../scripting/index.md) |
| `ignition/tag-change/`, `ignition/timer/` | Gateway event scripts | [Gateway Event Scripts](../gateway/event-scripts.md) |
| `ignition/named-query/` | Named queries (`AdhocTrend`, `OpsForms`, `OutOfService`, `Reports` ...) | [Scripting](../scripting/index.md), [Database](../database/index.md) |
| `com.inductiveautomation.reporting/reports/` | PDF reports (`OpsForms/*`, `Reports/CustomReport`) | [Features](../features/index.md) |
| `com.inductiveautomation.webdev/resources/` | WebDev resources (the `globe` page) | [Scripting](../scripting/index.md) |
| `com.inductiveautomation.vision/` | Leftover Vision client tags (Vision is not used) | |

## Inside Gateway Config (`gateways/standard/data/config/resources/core/`)

Ignition 8.3 stores gateway configuration as **resource files** (`config.json` + `resource.json`) instead of only in
the internal database. Most of it is gitignored; the tracked parts are listed in
[Tracked Vs Ignored](../git-workflow/tracked-vs-ignored.md).

| Folder | Content | Tracked |
|---|---|---|
| `ignition/tag-definition/default/**` | Tag instances of the `default` provider (`tags.json` per folder) | Whitelisted folders only |
| `ignition/tag-type-definition/**` | UDT definitions (`udts.json`) | Yes |
| `ignition/tag-group/default/*` | Tag groups (`RCP1_*`, `PAX_*`, `Default`) | `RCP1_*`, `PAX_*` |
| `com.inductiveautomation.perspective/themes/`, `icons/` | Gateway Perspective themes and icon libraries | Yes |
| `ignition/audit-profile/` | `DevAudit`, `OpsAudit` | Yes |
| `ignition/cobranding/` | Login/loading screen branding | Yes |
| `com.inductiveautomation.opcua/device/RCP1/` | The PLC driver config (with the write block) | **No** |
| `ignition/database-connection/`, `user-source/`, `api-token/` ... | Connections and security (contain encrypted secrets) | **No** |

Details for each: [Gateway](../gateway/index.md).

## Where To Look For ...

| Question | Look In |
|---|---|
| "Where is this view in the Designer?" | The view's reference page in [Perspective](../perspective/index.md): it lists the Project Browser path |
| "Why was this done?" | `docs/<feature>.md`, then `docs/handoff/HANDOFF.md` (search by date or keyword) |
| "What tags does this device have?" | [Tags](../tags/index.md) reference pages, or the Designer Tag Browser |
| "What script does this button run?" | The view's reference page in [Perspective](../perspective/index.md), then [Scripting](../scripting/index.md) |
| "Is this setting tracked in git?" | `git check-ignore -v <path>` (prints the matching `.gitignore` line) |
