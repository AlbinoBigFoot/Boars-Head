# Monday ticket → local HMI fix (Cursor Agent CLI)

You are running **locally** on Dylan Jones's Windows machine against the Boars Head (`Bors`) Ignition lab repo. This job was triggered by a Monday.com Tickets board `create_item` webhook after a Dylan-only filter.

## Mandatory first reads

1. `docs/cloud-agent/SUMMARY.md`
2. `docs/cloud-agent/ignition-scan.json` (scan API token — use for POST after edits)
3. Relevant `.cursor/rules` (CSS-only stylesheet, `HBT`→`shared`, faceplates under `01_Popups/00_Faceplates/`, Perspective JSON conventions, Ticket Logger)

## Goal

Implement a fix for the Monday ticket described at the bottom of this prompt. Leave work on a **ticket branch** for Dylan to review locally (and optionally hand off to a Desktop agent). **Do not land on `main`.**

## Workflow (fully automatic — do not wait for a human)

1. **Branch:** from current default/`main` (or the repo's primary branch), create and check out:
   `ticket/<monday_item_id>-<short-slug>`
   Example: `ticket/12652699666-ev01-status`
2. **Understand:** use the ticket title + description (+ updates). Prefer editing BH Perspective / scripts under `gateways/standard/data/projects/BH/`.
3. **Implement** following BH conventions:
   - Styling → Advanced Stylesheet only (`stylesheet/stylesheet.css`); `props.style.classes` = simple class names
   - Scripts: `shared.*` never `HBT.*`; faceplates only under `01_Popups/00_Faceplates/`
   - Perspective JSON: scoped `propConfig` keys; tab-indented script bodies; `\n` only (no `\r\n`) in expression/code/script strings
   - New/edited views: Ticket Logger context-menu + `ticketLog` handler per project rules
4. **Signatures (projects):** after any edit under `gateways/*/data/projects/`, run `python scripts/repair-resource-signatures.py` then `python scripts/repair-resource-signatures.py --check` (must exit 0). Skipping this causes Designer `ProtoSerializationException` / `No value present`. See `docs/ignition-resource-signatures.md`.
5. **Scan:** after project/config edits, POST Ignition scan using `docs/cloud-agent/ignition-scan.json` (`scan/projects` and/or `scan/config` as appropriate). Prefer `127.0.0.1` over `localhost` on Windows.
6. **Commit on the ticket branch only** with a clear message focused on why (only when the fix is real). Do **not** commit `.env`, tokens, or secrets. Do **not** commit gateway runtime churn under `projects/.resources/*` unless unavoidable.
7. **Push ticket branch (allowed):** `git push -u origin ticket/<…>` so Dylan can checkout from Desktop / another machine.
8. **Draft PR into `main` (review aid only):** if `gh` is available and authenticated, open a **draft** PR targeting `main`. Do **not** merge. If `gh` is missing or the PR conflicts, leave the branch pushed and note that in the handoff.
9. **Handoff doc (required):** write `docs/handoff/ticket-<monday_item_id>.md` with:
   - Monday item id + URL
   - Branch name
   - Summary of intent / what was done
   - Files changed
   - How to verify
   - Known risks / incomplete pieces
   - **Continue from here** instructions for the next Cursor Desktop agent
   Commit this file on the same ticket branch (and push again if needed).
10. **Stop** when the draft PR exists (or branch is committed/pushed if PR impossible) and the handoff file is on the branch. Summarize what changed in your final reply (include branch name + handoff path + draft PR URL if any).

The Monday webhook job script will move the item to **Pending Review** and post a Monday update after you exit successfully — you do not need to call the Monday API yourself for that.

## Forbidden (never do these)

- Checkout `main` as a place to land the fix, or merge the ticket branch into `main`
- Push to `main` / update remote `main`
- Force-push `main` (or any force-push to protected branches)
- Merge the draft PR
- Recreate Designer Style Class folders
- Invent `01_Faceplates/`
- Commit secrets

## Allowed

- Create/commit/push `origin ticket/<monday_item_id>-…`
- Open a **draft** PR into `main` (do not merge)
- Write `docs/handoff/ticket-<id>.md` on the ticket branch

## Success criteria

- Fix matches the ticket (or handoff clearly states what is incomplete)
- Conventions respected
- Signature repair + `--check` exit 0 when projects changed
- Scan performed when files under projects/config changed
- Work is on `ticket/…` only — **not on main**
- Handoff markdown written; draft PR preferred
- Final summary includes: branch name, handoff path, draft PR URL (if any), “not on main”
