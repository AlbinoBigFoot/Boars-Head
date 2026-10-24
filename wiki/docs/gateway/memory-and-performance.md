---
title: Memory And Performance
sidebar_position: 14
description: Gateway heap (STANDARD_MAX_MEMORY_MB), Designer RAM, WSL and VmmemWSL limits on Windows, SQL Server memory, and what loads the gateway.
sources:
  - docker-compose.yml
  - .env.example
  - gateways/standard/data/ignition.conf
  - gateways/standard/data/config/resources/core/ignition/system-properties/config.json
last_verified: 2026-10-23
---

# Memory And Performance

## Gateway Heap

The Java heap is set by the container's `-m` start argument, which compose fills from `.env`:

```yaml
command: >
  -n bh-standard -a localhost -h ${STANDARD_HTTP_PORT} -s ${STANDARD_HTTPS_PORT}
  -m ${STANDARD_MAX_MEMORY_MB:-6144}
```

| Setting | Value | Where |
|---|---|---|
| `STANDARD_MAX_MEMORY_MB` | **5120** live (6144 in `.env.example`) | `.env` |
| `wrapper.java.initmemory` / `maxmemory` | 256 / written from `-m` at start | `gateways/standard/data/ignition.conf` (generated, don't edit) |
| `EDGE_MAX_MEMORY_MB` | 1024 | `.env` |
| Designer RAM | 4096 MB (`designerRAM: MB4096`) | Platform > System > Gateway Settings |

History of the value: 6144 → 3072 (2026-10-22, heap peak about 2.1 GB) → 5120 (raised for the 206,000-tag `_RCP1_`
browse and import; revisit now that `_RCP1_` is pruned to about 35,000 tags).

**Change it:** edit `STANDARD_MAX_MEMORY_MB` in `.env`, then recreate the container so the new argument applies:

```powershell
docker compose up -d --force-recreate ignition-standard
docker inspect bh-ignition-standard --format '{{json .Args}}'   # ... "-m","5120"
```

`docker restart` alone keeps the old arguments.

**Watch it:** Diagnostics > Performance (heap graph), or `docker stats --no-stream`. The container itself uses more
than the heap (about 5.3 GB with a 5 GB heap).

## Windows: WSL 2 And VmmemWSL

Docker Desktop runs containers in a WSL 2 VM, which shows in Task Manager as **VmmemWSL**. By default WSL may take most
of the host's RAM and is slow to give it back.

`%UserProfile%\.wslconfig` on the lab machine:

```ini
[wsl2]
memory=12GB

[experimental]
autoMemoryReclaim=gradual
```

- `memory` caps the VM; the gateway heap + SQL Server + overhead must fit inside it.
- `autoMemoryReclaim=gradual` lets WSL return freed memory to Windows.
- Apply with `wsl --shutdown` (stops Docker Desktop's VM; restart Docker Desktop and the stack afterwards).

## SQL Server Memory

SQL Server takes all available memory unless capped. The lab caps it at **2048 MB** (`sp_configure 'max server
memory (MB)', 2048`, persists in the database volume). See [MSSQL](../infrastructure/mssql.md).

## What Loads The Gateway

| Load | Notes |
|---|---|
| RCP1 driver | Link-bound (about 15 requests/s over SecureLink); tag group demand tuned down 5x ([Tag Groups](tag-providers-and-groups.md#tag-groups)) |
| `_RCP1_` tags | 35,000 tags. A full browse (197,751 tags) needed the bigger heap; keep it pruned |
| Write lock flip | Reconfigures about 37,000 tags in 5,000-tag chunks (30 to 60 s) |
| History writes | About 18,800 historized tags into monthly partitions |
| Perspective sessions | Each open faceplate subscribes its Leased members |

Thread dumps: Diagnostics > Threads (automatic thread dumps are off: `automaticThreadDumpsEnabled: false`).
