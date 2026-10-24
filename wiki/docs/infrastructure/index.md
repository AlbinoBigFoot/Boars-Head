---
title: Infrastructure
description: The Docker Compose lab - services, ports, volumes, networks, the bind mount, the Edge gateway, PLC connectivity, MSSQL and the wiki service.
sources:
  - docker-compose.yml
  - .env.example
last_verified: 2026-10-23
---

# Infrastructure

The whole lab is one `docker-compose.yml` on Docker Desktop (Linux engine on WSL 2), on the Windows workstation.

```mermaid
flowchart TB
  subgraph Host["Windows host"]
    Browser["Browser / Designer"]
    Proxy["netsh portproxy<br/>(to SecureLink tunnel)"]
    Repo["Repo: gateways/standard/data<br/>gateways/edge/data, wiki/"]
  end
  subgraph Docker["Docker network bh-ot (bridge)"]
    STD["ignition-standard<br/>bh-ignition-standard<br/>8088 / 8043 / 8060"]
    EDGE["ignition-edge (optional)<br/>bh-ignition-edge"]
    SQL["mssql<br/>bh-mssql :1433"]
    TW["ignition-trial-watch"]
    WIKI["wiki<br/>bh-wiki :3000"]
  end
  Browser -- "19088 / 19043" --> STD
  Browser -- "19188" --> EDGE
  Browser -- "3030" --> WIKI
  Browser -- "11433 (SSMS)" --> SQL
  STD -- "jdbc mssql:1433" --> SQL
  TW -- "http ignition-standard:8088" --> STD
  STD -- "host.docker.internal" --> Proxy
  Proxy -- "SecureLink" --> PLC["RCP1 PLC (plant)"]
  Repo -. "bind mount" .- STD
  Repo -. "bind mount" .- EDGE
  Repo -. "bind mount" .- WIKI
```

| Page | Covers |
|---|---|
| [Docker Compose](docker-compose.md) | Every service, port, volume, network, environment variable; common commands |
| [Bind Mount And .resources](bind-mount-and-resources.md) | Why the gateway data folder lives in git, the content-addressed `.resources` store and its churn |
| [Edge Gateway](edge-gateway.md) | The optional Edge 8.3.7 container and its edition limits |
| [PLC Connectivity](plc-connectivity.md) | How the lab reaches RCP1 through SecureLink (concept, no addresses) |
| [MSSQL](mssql.md) | The SQL Server 2022 container, the `ignition` database, memory cap, backups |
| [The Wiki Service](wiki-service.md) | How this site is built and served (`bh-wiki`, port 3030) |
| [Remote Viewing](remote-viewing.md) | Showing the HMI to someone off-site (Tailscale Funnel) and its risks |
