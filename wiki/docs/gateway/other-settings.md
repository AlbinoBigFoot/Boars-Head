---
title: Other Gateway Settings
sidebar_position: 18
description: System properties, gateway network, Enterprise Administration, Edge sync, redundancy, keyboard layouts and translations.
sources:
  - gateways/standard/data/config/resources/core/ignition/system-properties/config.json
  - gateways/standard/data/config/resources/core/ignition/gateway-network-settings/config.json
  - gateways/standard/data/config/resources/core/ignition/edge-sync-settings/config.json
  - gateways/standard/data/config/resources/core/com.inductiveautomation.eam/module-settings/config.json
  - docker-compose.yml
last_verified: 2026-10-23
---

# Other Gateway Settings

## System Properties

**Where:** Platform > System > Gateway Settings (`ignition/system-properties/config.json`).

| Setting | Value |
|---|---|
| System name | `bh-standard` (also set by the container's `-n` argument) |
| Homepage | `/web/home` |
| Designer RAM | 4096 MB |
| Tag reference store | on |
| Script message encoding | Protobuf |
| Scheduled backups | off (see [Backups](backups.md)) |
| Automatic thread dumps | off (70% CPU for 10 s would trigger one) |
| Multicast discovery | on (231.1.1.1, ports 4445/4446) |
| Error report e-mail | not configured |

## Gateway Network

**Where:** Network > Gateway Network (`ignition/gateway-network-settings/config.json`). The gateway network connects
gateways for Enterprise Administration, remote tag providers, remote history and alarm journals.

| Setting | Value |
|---|---|
| Allow incoming | yes |
| Require SSL / two-way auth | yes / yes |
| Security policy | `ApprovedOnly` (new connections must be approved on the receiving side) |
| Allow Java serialization | yes in the resource; compose passes `GATEWAY_NETWORK_ALLOWJAVASERIALIZATION=false` for Standard (only needed for 8.1 ↔ 8.3) |
| GAN port | 8060 in the container, 18060 on the host |

No outgoing connections are configured today. The planned Standard ↔ Edge pairing: on Standard, Network > Gateway
Network > Connections > add outgoing to `ignition-edge:8060` (Docker network) and approve it on Edge
([Edge Gateway](../infrastructure/edge-gateway.md)).

## Enterprise Administration (EAM)

**Where:** Network > Enterprise > Configure. The EAM module is installed with its default agent group and event
thresholds; the gateway is not an EAM controller or agent yet. EAM is the planned way to push the project from
Standard to Edge.

## Edge Sync Settings

`ignition/edge-sync-settings`: all off (no remote history, journal or audit forwarding). These matter only on an Edge
gateway that forwards to a central one.

## Redundancy

Platform > System > Redundancy: **Independent** (no redundant pair).

## Deployment Modes

Platform > System > Modes: no deployment mode set (`deploymentMode: ""`). 8.3 deployment modes allow different
resource values per environment (dev/test/prod); not used yet, but a candidate for lab vs production differences
such as the RCP1 hostname ([Promote To Production](../deployment/promote-to-production.md)).

## Keyboard Layouts, Translations, Quickstart

Stock resources: on-screen keyboard layouts (`de_qwertz`, `es_qwerty`, `fr_azerty`, `it_qwerty`), an empty
translations resource, and the 8.3 quickstart state. Nothing project-specific.
