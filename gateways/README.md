# Gateway data (host-mounted)

Bind-mounted into containers at `/usr/local/bin/ignition/data`.

- `standard/` — Ignition Standard **8.3.7** (source of truth for project development)
- `edge/` — Ignition Edge **8.3.7** (local mirror target)

Both use the 8.3 host layout (`config/`, `projects/`, `modules.json`) — same shape as Lightspeed exports.

Volatile paths (logs/cache) are gitignored. After first `docker compose up`, commit intentional project exports / `projects/` content once Ignition creates them.

Do not put secrets in tracked files; use `.env` for admin passwords.
