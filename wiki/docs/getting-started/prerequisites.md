---
title: Prerequisites
sidebar_position: 1
description: Software and access you need before working on the BH project.
sources:
  - docker-compose.yml
  - wiki/package.json
last_verified: 2026-10-23
---

# Prerequisites

The lab runs on a Windows 11 workstation with Docker Desktop. Linux works too (see
[Docker Compose](../infrastructure/docker-compose.md) for the uid 2003 ownership note).

## Software

| Tool | Version Used | Why |
|---|---|---|
| **Docker Desktop** (Linux engine, WSL 2 backend) | current | Runs the gateway, SQL Server, trial watcher and the wiki as containers |
| **Git** (Git for Windows, includes Git Bash) | 2.4x+ | The repo; `core.autocrlf=true` on this machine |
| **GitHub CLI** `gh` | current | PRs and issues (`gh pr create` ...) |
| **Python** | 3.10+ on `PATH` as `python` | The wiki's reference-page tools. Stdlib only: nothing to `pip install` |
| **Node.js** | 20+ (22/24 tested) | Only for building this wiki (`wiki/`) |
| **Ignition Designer Launcher** | 8.3.7 | Opens the Designer against the lab gateway. Download it from the gateway itself (see [First Login](first-login.md)) |
| A Chromium browser | current | The Perspective HMI and the 8.3 Gateway web UI |
| Editor | VS Code or similar | View JSON, Python, Markdown. Set it to **UTF-8 without BOM** and **LF** for new files |

Optional:
- **Microsoft SQL Server Management Studio** or **Azure Data Studio**, to browse the `ignition` database at
  `localhost,11433`.
- **sqlcmd** is already inside the `bh-mssql` container, so you don't need it on the host.

## Machine Resources

- **RAM**: the gateway heap is set by `STANDARD_MAX_MEMORY_MB` (6144 MB default in `.env.example`; the running lab
  uses 5120 MB). SQL Server is capped at 2 GB. Give WSL at least 12 GB (`%UserProfile%\.wslconfig`,
  `memory=12GB`). See [Memory And Performance](../gateway/memory-and-performance.md).
- **Disk**: about 3 GB for images plus the repo; the MSSQL volume grows with history.

## Access You Need

| Access | From Whom | Notes |
|---|---|---|
| GitHub repo `AlbinoBigFoot/Boars-Head` | Project owner | Read to clone; write to push branches |
| `.env` values | Project owner (never in git, never in this wiki) | Gateway admin password, SQL `sa` password, the `IGNITION_API_TOKEN` |
| A gateway user in the internal user source `default` | A gateway Administrator | Your HMI / Designer login; its roles decide what you can do |
| SecureLink (plant VPN) | Boar's Head IT / project owner | Only if you need RCP1 live data in the lab; see [PLC Connectivity](../infrastructure/plc-connectivity.md) |

:::info No dependency managers
Apart from this wiki (`npm`), the repo has no package manager, lint, test runner or CI. The project is maintained in
the Ignition Designer and the Gateway web UI; git records the files they save.
:::
