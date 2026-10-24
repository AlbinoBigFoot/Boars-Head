---
title: Tracked Vs Ignored
sidebar_position: 1
description: What .gitignore keeps out of git, the whitelist for gateway tags and config, the .resources churn and local-only files.
sources:
  - .gitignore
  - wiki/.gitignore
last_verified: 2026-10-23
---

# Tracked Vs Ignored

## The Gateway Data Folder: Ignore All, Then Whitelist

`.gitignore` starts with `gateways/**/data/**` (ignore everything the gateway writes) and then re-includes specific
folders with `!` lines.

| Tracked (whitelisted) | Path under `gateways/<gw>/data/` |
|---|---|
| Projects | `projects/**` (both gateways) |
| Perspective themes and icon libraries | `config/resources/core/com.inductiveautomation.perspective/{themes,icons}/**` |
| UDT definitions | `config/resources/core/ignition/tag-type-definition/**` (Standard) |
| Tag folders (Standard, `tag-definition/default/`) | `CoolingTowers`, `Evaporators`, `Compressors`, `Pumps`, `ExhaustFans`, `Tanks`, `Valves`, `Sensors`, `RCP1` (legacy folders), `_Config/tags.json` + `unary-resource.json`, `_Config/{Security,Forms,Reports,Enums,PlcWriteLock}/**`, `Boars_Head/unary-resource.json`, `Boars_Head/GrovePort/unary-resource.json`, `Boars_Head/GrovePort/{Production,Machine Room,Freezer,SuperChill,Club,Dock,East PH,West PH,Palletizing,Condensers}/**` |
| Tag groups | `config/resources/core/ignition/tag-group/default/{RCP1_Status,RCP1_Faceplate,PAX_Status,PAX_Faceplate,PAX_Config}/**` |
| Audit profiles | `config/resources/core/ignition/audit-profile/**` |
| Co-branding | `config/resources/core/ignition/cobranding/**` |
| S&F auditing status tags | `tag-definition/System/Gateway/StoreAndForward/ignition/Pipelines/Auditing/**` |

| **Not** tracked (on purpose) | Why |
|---|---|
| `tag-definition/default/_RCP1_/**` | 35,000 browsed PLC tags; rebuilt from a browse of the PLC, backups outside git |
| `tag-definition/default/Boars_Head/GrovePort/PLC/**` | Old RCP1 stand-ins |
| `tag-definition/default/KPI/**` | Enterprise KPI tags (not whitelisted) |
| `com.inductiveautomation.opcua/device/**` (RCP1) | Device config; per-environment |
| `database-connection`, `user-source`, `api-token`, `opc-connection`, `identity-provider` ... | Contain encrypted secrets or per-environment values |
| `config.idb`, `db/`, `logs/`, `local/`, `certificates/`, caches | Runtime state |
| `gateways/**/data/projects/.resources/*` | Tracked by the whitelist but **never commit its churn** (below) |

**New tag or config folders need a whitelist line**, or they will never be committed. Add both the folder and its
`/**` (git needs each parent re-included):

```gitignore
!gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/NewThing/
!gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/NewThing/**
```

Check any path: `git check-ignore -v "<path>"` prints the rule that matches (no output = tracked).

## The `.resources` Churn

The gateway rewrites `projects/.resources/*` by itself, so `git status` always shows deleted/added files there. Never
stage them. See [Bind Mount And .resources](../infrastructure/bind-mount-and-resources.md#the-resources-churn).

## Tag Definition Rules For Commits

- Commit `tag-definition/**` and `tag-type-definition/**` changes **with the work that needs them**.
- If a folder flipped between `udts.json` and `tags.json` + `unary-resource.json` storage, commit the **full
  consistent set** (the deletion and the addition).
- Exclude `tag-definition/System/Gateway/**` noise (except the whitelisted Auditing folder) and anything with
  secrets.

## Other Ignored Things

| Path | Why |
|---|---|
| `.env`, `.env.local`, `*.pem`, `*.key`, `.ignition-scan.json` | Secrets |
| `docs/handoff/` (incl. `HANDOFF.md`) | Local-only session log; older tracked files in it stay tracked |
| `logs/` | Tool output |
| `__pycache__/`, `*.pyc`, `.venv/` | Python |
| `wiki/node_modules/`, `wiki/build/`, `wiki/.docusaurus/` (+ `wiki/.gitignore`: `build-*/`, `.docusaurus-*/`) | Wiki build output |
| `graphify-out/.graphify_*`, `graphify-out/cost.json` | Knowledge-graph temp files |
| `*.gwbk` | Never commit gateway backups (they contain everything, including secrets) |

The lab API settings file in `docs/` **is** tracked (it holds the lab API token for scan calls). Treat it as a lab
secret: never copy its value anywhere else, and don't reuse that token in production.
