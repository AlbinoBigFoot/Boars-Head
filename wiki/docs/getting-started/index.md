---
title: Getting Started
description: The learning path for a developer joining the Boar's Head SCADA project.
sources:
  - README.md
  - docker-compose.yml
  - .env.example
last_verified: 2026-10-23
---

# Getting Started

This section takes you from an empty laptop to a merged change. Follow it in order the first time.

| Step | Page | You End Up With |
|---|---|---|
| 1 | [Prerequisites](prerequisites.md) | Docker Desktop, Git, Python, Node and the Ignition Designer Launcher installed |
| 2 | [Clone And Run The Stack](clone-and-run.md) | The repo on disk, a `.env`, the gateway and SQL Server running |
| 3 | [First Login](first-login.md) | The HMI open in a browser, the Gateway web UI open, the Designer connected to the `BH` project |
| 4 | [Repository Tour](repo-tour.md) | A map of every folder that matters |
| 5 | [Windows And Encoding Gotchas](windows-gotchas.md) | The PowerShell and UTF-8 traps that have bitten this project before |
| 6 | [Glossary](glossary.md) | The Ignition, PlantPAx and project jargon |
| 7 | [Your First Change](first-change.md) | One small Designer change made, tested and ready to commit, end to end |
| 8 | [Common Tasks](common-tasks.md) | Short Designer recipes for the changes you will make most often |

## The Short Version

```powershell
git clone https://github.com/AlbinoBigFoot/Boars-Head.git Bors
cd Bors
Copy-Item .env.example .env          # then set the passwords and IGNITION_API_TOKEN in .env
docker compose up -d ignition-standard mssql ignition-trial-watch
curl.exe -s http://localhost:19088/StatusPing   # repeat until {"state":"RUNNING"}
start http://localhost:19088/data/perspective/client/BH
```

:::warning The PLC is real
The gateway connects to **RCP1, the live production PLC**. Everything that reads it is read only and the OPC UA
server refuses writes to it. Never undo either protection to "try something". See
[RCP1 Device And Write Protection](../gateway/devices-rcp1.md).
:::

## Who Owns What

- **Client**: Boar's Head (Groveport plant). **Integrator**: One Shot Automation.
- **Repo**: `AlbinoBigFoot/Boars-Head` on GitHub, default branch `main`.
- **Approvals**: nothing is committed, pushed or opened as a PR without the project owner's explicit go-ahead
  ([Git Workflow](../git-workflow/index.md)).
