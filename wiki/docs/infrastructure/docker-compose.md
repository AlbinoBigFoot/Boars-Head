---
title: Docker Compose
sidebar_position: 1
description: Every service in docker-compose.yml with its ports, volumes, environment and start arguments, plus everyday commands.
sources:
  - docker-compose.yml
  - .env.example
  - trial-watch/Dockerfile
  - wiki/Dockerfile
last_verified: 2026-10-23
---

# Docker Compose

File: `docker-compose.yml` at the repo root. Values in `${...}` come from `.env` (template `.env.example`).

## Services

| Service | Container | Image | Host Ports → Container | Data | Required |
|---|---|---|---|---|---|
| `ignition-standard` | `bh-ignition-standard` | `inductiveautomation/ignition:8.3.7` | **19088**→8088 HTTP, 19043→8043 HTTPS, 18060→8060 GAN | bind `./gateways/standard/data` → `/usr/local/bin/ignition/data` | yes |
| `ignition-edge` | `bh-ignition-edge` | `inductiveautomation/ignition:8.3.7` (`IGNITION_EDITION=edge`) | 19188→8088, 19143→8043, 18160→8060 | bind `./gateways/edge/data` | no |
| `ignition-trial-watch` | `bh-ignition-trial-watch` | built from `./trial-watch` (`bors-ignition-trial-watch`) | none | none | yes (lab) |
| `mssql` | `bh-mssql` | `mcr.microsoft.com/mssql/server:2022-latest` | **11433**→1433 | named volume `bh-mssql-data` → `/var/opt/mssql` | yes |
| `wiki` | `bh-wiki` | built from `./wiki` | **3030**→3000 | bind `./wiki` → `/app`, volume `bh-wiki-node-modules` → `/app/node_modules` | no |

All services join the bridge network **`bh-ot`** and use `TZ=America/New_York`. Every service has
`restart: unless-stopped`, so they come back after a Docker Desktop restart unless you stopped them.

### `ignition-standard`

```yaml
environment:
  ACCEPT_IGNITION_EULA: "Y"
  GATEWAY_ADMIN_USERNAME: "${GATEWAY_ADMIN_USERNAME:-admin}"
  GATEWAY_ADMIN_PASSWORD: "${GATEWAY_ADMIN_PASSWORD:?Set GATEWAY_ADMIN_PASSWORD in .env}"
  IGNITION_EDITION: standard
  GATEWAY_NETWORK_ALLOWJAVASERIALIZATION: "${GATEWAY_NETWORK_ALLOWJAVASERIALIZATION:-false}"
command: -n bh-standard -a localhost -h ${STANDARD_HTTP_PORT} -s ${STANDARD_HTTPS_PORT} -m ${STANDARD_MAX_MEMORY_MB:-6144}
```

| Argument | Meaning |
|---|---|
| `-n bh-standard` | Gateway system name |
| `-a localhost`, `-h 19088`, `-s 19043` | The public address/ports the gateway advertises (so links and the Designer Launcher use the host ports) |
| `-m 6144` | Max heap in MB ([Memory](../gateway/memory-and-performance.md)) |

`:?` makes compose refuse to start when the variable is missing: you get a clear error instead of a gateway with no
admin password.

### `ignition-trial-watch`

Polls `http://ignition-standard:8088/data/api/v1/trial` (internal port, over `bh-ot`) and resets the trial
([Trial And Licensing](../gateway/trial-and-licensing.md)). Environment: `IGNITION_GATEWAY_HOST`,
`IGNITION_GATEWAY_PORT`, `IGNITION_API_TOKEN` (required), `TRIAL_WATCH_LOG_LEVEL`, `TRIAL_WATCH_MAX_POLL_S` (20).

### `mssql`

SQL Server 2022 Developer edition (`MSSQL_PID`). Health check runs `sqlcmd ... SELECT 1` every 30 s. The SA
password must meet complexity rules or the container exits. See [MSSQL](mssql.md).

### `wiki`

Builds this site and serves it ([The Wiki Service](wiki-service.md)).

## Volumes And Networks

| Name | Type | Holds | Survives `down`? |
|---|---|---|---|
| `./gateways/standard/data` | bind mount | the Standard gateway's entire data folder | yes (it's the repo) |
| `./gateways/edge/data` | bind mount | the Edge gateway's data folder | yes |
| `bh-mssql-data` | named volume | SQL Server databases | yes; **deleted by `down -v`** |
| `bh-wiki-node-modules` | named volume | the wiki container's `node_modules` | yes |
| `bh-ot` | bridge network | service-to-service DNS (`ignition-standard`, `mssql`, `ignition-edge`, `wiki`) | recreated by compose |

## Everyday Commands

```powershell
docker compose up -d ignition-standard mssql ignition-trial-watch   # the lab
docker compose up -d ignition-edge                                    # optional Edge gateway
docker compose up -d --build wiki                                     # the wiki
docker ps --format "{{.Names}}|{{.Status}}"
docker logs --tail 100 bh-ignition-standard
docker restart bh-ignition-standard                                   # full project reload, about 40 s
docker compose up -d --force-recreate ignition-standard               # after changing .env (ports, memory)
docker exec bh-ignition-standard sed -n '1,20p' /usr/local/bin/ignition/data/projects/BH/project.json
docker stats --no-stream
```

## Linux Hosts

The Ignition container runs as uid/gid **2003**. On Linux the bind-mounted `gateways/*/data` must be owned by 2003
(`sudo chown -R 2003:2003 gateways/standard/data gateways/edge/data`) or init fails with
`init.properties: Permission denied`. Docker Desktop on Windows doesn't need this. Ask the system integrator for the full Linux/VM
notes (starting `dockerd` without systemd, the fresh-data-folder `core` fault).
