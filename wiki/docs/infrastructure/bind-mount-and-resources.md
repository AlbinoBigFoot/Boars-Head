---
title: Bind Mount And .resources
sidebar_position: 2
description: Why the gateway data folder is bind-mounted into git, what the content-addressed .resources store is, and how to handle its churn.
sources:
  - docker-compose.yml
  - .gitignore
last_verified: 2026-10-23
---

# Bind Mount And .resources

## The Bind Mount

The compose file mounts `./gateways/standard/data` over the container's `/usr/local/bin/ignition/data`. So the
**gateway's live data folder is a folder of this repo**:

- A Designer save writes `view.json` into `gateways/standard/data/projects/BH/...` on your disk, visible to git.
- `git checkout` or `git pull` of another branch changes the gateway's project files under its feet (use File >
  Update Project in the Designer, or restart the gateway, afterwards).

Only part of the folder is tracked: the project, themes, icons, UDTs, whitelisted tag folders, tag groups, audit
profiles, co-branding. Runtime files (`config.idb`, logs, caches, certificates, `local/`, the rest of `config/`) are
ignored ([Tracked Vs Ignored](../git-workflow/tracked-vs-ignored.md)).

## Resources, Signatures And The CAS

Ignition 8.3 projects are file-based. Each resource folder has:

```text
views/00_Pages/Groveport/Utility/Overview/
├── view.json          content
├── thumbnail.png      content
└── resource.json      metadata: scope, version, files, attributes.lastModificationSignature
```

- **`lastModificationSignature`** is a SHA-256 over the resource's scope, documentation, version, flags, other
  attributes and the **digest of every content file**.
- The gateway also keeps each content file **content-addressed** in `gateways/standard/data/projects/.resources/<sha256>`
  (the "CAS").
- The Designer and the gateway keep both up to date on every save. **Never hand-edit `resource.json` or the
  `.resources` store.**
- If a resource file is damaged (for example by a bad merge) the Designer fails with errors such as
  `ProtoSerializationException` or `NoSuchElementException: No value present`. Restore the resource's last good
  version from git, reopen the project in the Designer and save ([Merge Conflicts](../git-workflow/merge-conflicts.md)).

## The `.resources` Churn

The running gateway **rehashes and rewrites `projects/.resources/*`** on its own (after saves, scans, restarts). In
`git status` that shows as many deleted and added files under `gateways/standard/data/projects/.resources/`. It is
expected and **never committed**:

```powershell
git status --short -- gateways/standard/data/projects/.resources | Measure-Object   # usually hundreds
git restore --staged gateways/standard/data/projects/.resources                    # if you staged it by accident
```

Only the human-authored files (`view.json`, `resource.json`, `code.py`, `stylesheet.css`, `config.json` ...) matter.
Whether those blobs are committed doesn't matter, because the gateway recreates the store from the content files.

## Gateway Config Resources

The same structure applies to `config/resources/core/**` (devices, tag groups, themes ...). Prefer changing those
through the Gateway web UI or the Designer (they keep the metadata right). Themes are edited in the Designer
(Project Browser > Perspective > Themes) or the Gateway web UI ([Perspective](../perspective/index.md)).
