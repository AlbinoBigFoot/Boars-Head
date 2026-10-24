---
title: Clone And Run The Stack
sidebar_position: 2
description: Clone the repo, create .env from .env.example, start the Docker stack and wait for the gateway.
sources:
  - docker-compose.yml
  - .env.example
  - trial-watch/README.md
last_verified: 2026-10-23
---

# Clone And Run The Stack

## 1. Clone

```powershell
cd $HOME\Documents
git clone https://github.com/AlbinoBigFoot/Boars-Head.git Bors
cd Bors
git status            # on main, clean
```

The folder name `Bors` is what every doc and script assumes (`C:\Users\<you>\Documents\Bors`). Paths inside the repo
are always relative, so another location works, but keep the name to make copy-paste from this wiki painless.

## 2. Create `.env`

`.env` holds secrets and host ports. It is **gitignored**; the tracked template is `.env.example`.

```powershell
Copy-Item .env.example .env
notepad .env
```

Set at least these keys (ask the project owner for the real values; never commit them or paste them in chat, tickets
or this wiki):

| Key | Used By | Notes |
|---|---|---|
| `GATEWAY_ADMIN_USERNAME` / `GATEWAY_ADMIN_PASSWORD` | both gateways | Commissioning admin. Compose fails fast if the password is unset |
| `MSSQL_SA_PASSWORD` | `bh-mssql` | 8+ characters with upper, lower, digit and symbol, or SQL Server refuses to start |
| `IGNITION_API_TOKEN` | `ignition-trial-watch` | **`Name:secret`** form (for example `Access:...`). A bare secret returns HTTP 401 |
| `STANDARD_HTTP_PORT` ... | compose port mapping | Defaults in `.env.example`: 19088 / 19043 / 18060 (Standard), 19188 / 19143 / 18160 (Edge), 11433 (SQL), 3030 (wiki) |
| `STANDARD_MAX_MEMORY_MB` | gateway heap (`-m`) | 6144 in the template; see [Memory And Performance](../gateway/memory-and-performance.md) |

:::danger Never print secrets
Don't `cat .env`, don't paste it into a ticket, and don't echo `IGNITION_API_TOKEN` anywhere.
:::

## 3. Get A Gateway Data Folder

The gateway's whole data directory is bind-mounted from `gateways/standard/data`. Git tracks only part of it (the `BH`
project, themes, icons, UDTs, a whitelist of tag folders, audit profiles, co-branding; see
[Tracked Vs Ignored](../git-workflow/tracked-vs-ignored.md)). The rest (`config.idb`, the RCP1 device, `_RCP1_` tags,
database connection, users, the Logix driver settings) is **not** in git. So a fresh clone is not a complete gateway.

Pick one:

- **Recommended: restore a gateway backup.** Ask the project owner for a current `.gwbk`. Start the stack (step 4),
  log in to the Gateway web UI and use **Platform > System > Backup & Restore > Restore**. Then `git status`: the
  restore rewrites tracked files to the backup's state; discard what you didn't mean to change
  (`git restore <path>`), or keep the backup's version if it is newer than `main` and tell the owner.
- **Empty lab from scratch.** Run `.\scripts\seed-gateway-data.ps1` once, which copies the default data folder out of
  the images into `gateways/*/data`.
  - The script still names the `8.1.43` image for Standard. Change it to `8.3.7` before running it, because the stack
    is 8.3.7.
  - On a fresh data folder the committed `config/resources/core` makes the first boot fault ("Resource collection
    path ... exists but is not empty"). Move `core` aside, boot once, then copy the committed
    `com.inductiveautomation.perspective/{themes,icons}` and the other tracked folders back into `core` and restart
    (ask the system integrator for the exact steps).
  - You then still need the gateway pieces that are not in git: the `ignition` database connection, the RCP1 device,
    the users. Without RCP1 the HMI shows gray "no value" placeholders.

## 4. Start The Stack

```powershell
docker compose up -d ignition-standard mssql ignition-trial-watch   # the Edge gateway is optional
docker ps --format "{{.Names}}|{{.Status}}"
```

Expected:

```text
bh-ignition-standard|Up 2 minutes (healthy)
bh-mssql|Up 2 minutes (healthy)
bh-ignition-trial-watch|Up 2 minutes
```

Wait for the gateway (about 40 s, longer on first boot and while RCP1 tags load):

```powershell
curl.exe -s http://localhost:19088/StatusPing      # {"state":"RUNNING"}
```

:::note `curl` vs `curl.exe`
In Windows PowerShell `curl` is an alias for `Invoke-WebRequest`. Always type `curl.exe`.
:::

If `docker` fails with `dockerDesktopLinuxEngine ... cannot find the file`, Docker Desktop isn't running. Start it
from the Start menu and retry.

## 5. The Trial Clock

The lab gateway runs on an Ignition **trial** that expires every 2 hours. The `ignition-trial-watch` container polls
`/data/api/v1/trial` every 20 s and resets it on expiry, so you normally never notice. A `403` in its log only means
"not expired yet". Details: [Trial And Licensing](../gateway/trial-and-licensing.md).

## 6. SQL Schema (Fresh Database Only)

The MSSQL data lives in the named volume `bh-mssql-data`, so it survives `docker compose down`. On a brand new volume,
create the database and apply the scripts in `sql/` with **`-I`** (QUOTED_IDENTIFIER ON, needed for the filtered
indexes):

```powershell
docker exec -i bh-mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "<sa password>" -C -Q "CREATE DATABASE ignition"
Get-Content sql\adhoc_trend_configs.sql | docker exec -i bh-mssql /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "<sa password>" -C -I -d ignition
```

Repeat for `operations_forms.sql`, `out_of_service_log.sql`, `report_template.sql`, `report_run.sql` and `ticket_outbox.sql`. The historian,
alarm journal and audit tables are created by the gateway itself. Schema details: [Database](../database/index.md).

## 7. Stop And Restart

```powershell
docker compose stop                       # keeps containers and volumes
docker compose up -d ignition-standard    # start again
docker restart bh-ignition-standard       # forces a full project reload (about 40 s)
docker logs --tail 100 bh-ignition-standard
```

`docker compose down` removes the containers but keeps the bind-mounted data and the `bh-mssql-data` volume.
**Never** run `docker compose down -v` unless you mean to delete the SQL database.

Next: [First Login](first-login.md).
