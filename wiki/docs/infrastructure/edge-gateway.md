---
title: Edge Gateway
sidebar_position: 3
description: The optional Ignition Edge 8.3.7 container, what is in its data folder, how it would pair with Standard, and the edition limits to check.
sources:
  - docker-compose.yml
  - README.md
  - docs/local-groveport-mode.md
last_verified: 2026-10-23
---

# Edge Gateway

The stack defines a second gateway, **`ignition-edge`** (container `bh-ignition-edge`), running the same image with
`IGNITION_EDITION=edge`:

| Item | Value |
|---|---|
| URL | http://localhost:19188 (HTTPS 19143, GAN 18160) |
| System name | `bh-edge` (`-n`) |
| Heap | `EDGE_MAX_MEMORY_MB` = 1024 |
| Data | bind mount `./gateways/edge/data` (tracked: only the Perspective themes; it has its own `projects/Edge`) |
| `GATEWAY_NETWORK_ALLOWJAVASERIALIZATION` | `true` default for Edge |
| Status | **not running** in the lab today (`docker compose up -d ignition-edge` to start it) |

## Why It Exists

The plan (2026-10) is that the **local Groveport HMI moves to an Edge gateway at the plant**, while the Standard
gateway stays the enterprise / SCADA gateway. The project already has a local mode for that
([Deployment Modes](../deployment/deployment-modes.md)); the move itself is in
[The Edge Move](../deployment/edge-move.md).

## Pairing It With Standard (When Needed)

1. Start both gateways.
2. On Standard: Network > Gateway Network > Connections > add an outgoing connection to `ignition-edge` port 8060
   (Docker DNS on `bh-ot`), or the host ports for gateways outside Docker.
3. On Edge: approve the incoming connection (security policy `ApprovedOnly`, SSL and two-way auth required).
4. Use Enterprise Administration (EAM) project sync, or a project export/import, to put `BH` on Edge.

Both are 8.3.7, so Java serialization on the gateway network is not required.

## Edition Limits To Check

Ignition Edge is a cut-down, cheaper edition for the plant floor. Before moving anything, confirm each of these
against Inductive Automation's documentation for **8.3 Edge** and the license you will buy:

| Need | Used By | Risk On Edge |
|---|---|---|
| A **SQL database connection** to MSSQL | Forms, Out Of Service, report templates, saved trends, OpsAudit | Edge historically has no general database connections; may need a remote DB through Standard |
| **DB alarm journal** | `/alarms/journal`, Reports alarm source | Same |
| **Reporting module** | Forms PDFs, Report Builder PDF | Confirm availability/licensing |
| **Tag history** | Trending, Utility Overview charts | Local historian with limited retention; sync to Standard for long trends |
| **Perspective co-branding** | Login screen | Standard/Cloud only: Edge keeps the stock login |
| **Perspective session count** | Operator stations | Edge editions limit concurrent sessions |
| **Third-party modules** (Integration Toolkit, ApexCharts) | Most bindings and charts | Confirm they install on Edge |
| **Device connections** | RCP1 | Edge supports drivers; confirm the count limit |
