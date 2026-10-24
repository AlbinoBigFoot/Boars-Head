---
title: Git Workflow
description: The repository, its branches and naming, the approval rule, and links to the change process.
sources:
  - .gitignore
last_verified: 2026-10-23
---

# Git Workflow

## The Repository

| Item | Value |
|---|---|
| Remote | `origin` = `https://github.com/AlbinoBigFoot/Boars-Head.git` (use `gh` for GitHub tasks) |
| Default branch | **`main`**: what is deployed / deployable |
| Long-lived branch | `dev` (integration branch used in the past; check with the owner before targeting it) |
| Line endings | `core.autocrlf=true` on the Windows lab machine; no `.gitattributes` |
| Author | Your global git identity; the repo sets none. Don't change git config for others |
| Worktree | `C:/Users/dylan.jones/Documents/Bors-groveport` on `ship/groveport-kpi` (owner's; don't delete it or reuse its branch) |

## The Approval Rule

**No `git commit, `git push`, PR creation or update, amend, rebase or force-push without the project owner's explicit
go-ahead** ("commit this", "push", "open a PR", "ship it"). Reading git and making local
edits is always fine. When work is ready: summarise what would be committed and ask.

## Branch Names

| Pattern | For | Example |
|---|---|---|
| `feature/<topic>` or `feat/<topic>` | New functionality | `feature/central-alarming`, `feat/rcp1-simulate` |
| `fix/<topic>` | Bug fixes | `fix/evap-status-labels` |
| `ticket/<monday-item-id>-<topic>` | Work from a Monday.com ticket | `ticket/12652699666-evap-status-modes` |
| `ship/<topic>` | Release preparation | `ship/groveport-kpi` |

## Commit Messages

Short imperative sentences, or conventional-commit style; both appear in history:

```text
Sanitize RCP1 tag documentation bloat.
Ship Groveport KPI nav dashboard polish to main.
feat: Pump faceplate P_Motor Controls-Alarms parity with SIM start/stop
fix: stop valve faceplate tab-switch binding flashes
chore(tags): commit Plant Sensors/Tanks udts; always-commit-tags rule
```

PRs are numbered on GitHub (`Machine Room: type folders + Design/Details device overviews (#14)`).

## In This Section

| Page | Covers |
|---|---|
| [Tracked Vs Ignored](tracked-vs-ignored.md) | What `.gitignore` keeps out, the tag whitelist, `.resources` churn, local-only docs |
| [Making A Change](making-a-change.md) | The process: branch, change in the Designer, test in a session, commit, PR, review, deploy, tag |
| [Merge Conflicts](merge-conflicts.md) | Resolving conflicts in project and tag files after a merge, and what to check in the Designer |
