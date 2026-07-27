# Ignition project resource signatures

## Why this exists

Ignition 8.3 projects are file-based. Each resource folder has a `resource.json` whose `attributes.lastModificationSignature` is a SHA-256 over scope, docs, version, flags, **content file digests**, and other attributes.

Content bytes are also stored content-addressed under:

`gateways/standard/data/projects/.resources/<sha256-hex>`

When agents (or humans) edit `view.json`, `code.py`, `stylesheet.css`, named-query SQL, etc. on disk and **do not** refresh the signature and CAS blob:

1. Designer **pull** / gateway RPC serialization looks up the digest for that file.
2. The digest is missing or out of date → `Optional` empty.
3. Result: `ProtoSerializationException` / `ImmutableResourceSerializer` / `NoSuchElementException: No value present`.

Gateway logs often show:

`Failed to open input stream for ResourceId{...}/view.json`  
`java.nio.file.NoSuchFileException: .../projects/.resources/<old-or-missing-digest>`

## Required workflow after project edits

```powershell
python scripts/repair-resource-signatures.py
python scripts/repair-resource-signatures.py --check   # must exit 0

$cfg = Get-Content docs/cloud-agent/ignition-scan.json | ConvertFrom-Json
$h = @{ "X-Ignition-API-Token" = $cfg.apiToken }
Invoke-RestMethod -Method POST -Uri $cfg.scanProjectsUrl -Headers $h
```

| Flag | Meaning |
|------|---------|
| (default) | Repair missing, zero, stale signatures, and missing CAS digests |
| `--all` | Force-recompute every BH `resource.json` |
| `--check` | Report only; exit 1 if any issue |
| `--path <resource.json>` | Single resource |

Legacy alias: `scripts/_repair_resource_signatures.py` → same script.

## What not to commit

`.resources/*` churn is often gateway runtime noise. Prefer committing corrected `resource.json` (and the content files you meant to change). See `AGENTS.md`. Agents must still **write** CAS digests locally so the running gateway can pull — whether those blobs are committed is a separate choice.

## Related

- Always-apply Cursor rule: `.cursor/rules/ignition-resource-signatures.mdc`
- Scan API: `docs/cloud-agent/SUMMARY.md`, `.cursor/rules/ignition-8-3-scan-api.mdc`
