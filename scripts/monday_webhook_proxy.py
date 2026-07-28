#!/usr/bin/env python3
"""Monday.com webhook receiver → local Cursor agent (Dylan-only filter).

- Echoes Monday URL-verification challenge.
- On create_item / create_pulse: enrich via Monday API when possible, filter for
  Dylan Jones as the *filer* (Employee Name / Email / Created By — not the API
  token owner), then spawn local `agent` CLI headlessly. Non-Dylan → Pushover only.
- On agent exit 0: job moves item to Monday **Pending Review** + posts handoff
  update (branch / docs/handoff/ticket-<id>.md / draft PR). Never merges to main.
- No Cursor Cloud Automations forward.

Usage:
  python scripts/monday_webhook_proxy.py [--port 9876]
  python scripts/monday_webhook_proxy.py --self-test
  python scripts/monday_webhook_proxy.py --dry-run   # accept webhooks but do not spawn agent
"""

from __future__ import annotations

import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

# Ensure repo scripts/ is importable when launched via absolute path / Task Scheduler
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
	sys.path.insert(0, str(_SCRIPTS))

from monday_agent_job import (  # noqa: E402
	env,
	handle_webhook_payload,
	load_dotenv,
	self_test,
)


class Handler(BaseHTTPRequestHandler):
	dry_run = False

	def log_message(self, fmt: str, *args) -> None:
		sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

	def _read_json(self):
		length = int(self.headers.get("Content-Length") or 0)
		raw = self.rfile.read(length) if length else b"{}"
		try:
			return json.loads(raw.decode("utf-8") or "{}")
		except json.JSONDecodeError:
			return {"_raw": raw.decode("utf-8", errors="replace")}

	def _send_json(self, status: int, payload: dict) -> None:
		body = json.dumps(payload).encode("utf-8")
		self.send_response(status)
		self.send_header("Content-Type", "application/json")
		self.send_header("Content-Length", str(len(body)))
		self.end_headers()
		self.wfile.write(body)

	def do_GET(self) -> None:
		self._send_json(
			200,
			{
				"ok": True,
				"service": "monday-local-agent-proxy",
				"mode": "local-agent",
				"dry_run": bool(self.dry_run),
			},
		)

	def do_POST(self) -> None:
		payload = self._read_json()

		# Monday URL verification: must echo {"challenge": "..."}
		if isinstance(payload, dict) and "challenge" in payload:
			self._send_json(200, {"challenge": payload["challenge"]})
			return

		try:
			result = handle_webhook_payload(payload, dry_run=bool(self.dry_run))
		except Exception as exc:  # noqa: BLE001
			sys.stderr.write("handler error: %s\n" % exc)
			self._send_json(200, {"ok": False, "error": str(exc)})
			return

		# Always 200 to Monday so it does not disable the webhook on skips/errors
		self._send_json(
			200,
			{
				"ok": True,
				"skipped": result.get("skipped", False),
				"reason": result.get("reason"),
				"item_id": (result.get("ticket") or {}).get("item_id"),
				"job": result.get("job"),
				"dry_run": bool(self.dry_run),
			},
		)


def main() -> int:
	load_dotenv()
	parser = argparse.ArgumentParser(description="Monday → local Cursor agent webhook proxy")
	parser.add_argument("--port", type=int, default=int(env("MONDAY_WEBHOOK_PORT") or "9876"))
	parser.add_argument("--bind", default=env("MONDAY_WEBHOOK_BIND") or "127.0.0.1")
	parser.add_argument("--dry-run", action="store_true", help="Filter/log only; do not spawn agent")
	parser.add_argument("--self-test", action="store_true", help="Run filter self-tests and exit")
	args = parser.parse_args()

	if args.self_test:
		return self_test()

	Handler.dry_run = bool(args.dry_run) or env("MONDAY_AGENT_DRY_RUN").lower() in (
		"1",
		"true",
		"yes",
	)

	server = HTTPServer((args.bind, args.port), Handler)
	sys.stderr.write(
		"monday-local-agent-proxy listening on http://%s:%s  dry_run=%s\n"
		% (args.bind, args.port, Handler.dry_run)
	)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		sys.stderr.write("shutting down\n")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
