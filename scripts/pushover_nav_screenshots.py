# -*- coding: utf-8 -*-
"""Send Pushover notifications with screenshot attachments for BH nav verification."""
from __future__ import annotations

import json
import mimetypes
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def load_env() -> None:
	env_path = REPO / ".env"
	if not env_path.is_file():
		return
	for line in env_path.read_text(encoding="utf-8", errors="replace").splitlines():
		line = line.strip()
		if not line or line.startswith("#") or "=" not in line:
			continue
		k, v = line.split("=", 1)
		k, v = k.strip(), v.strip().strip('"').strip("'")
		if k and k not in os.environ:
			os.environ[k] = v


def pushover_with_image(title: str, message: str, image: Path) -> bool:
	token = os.environ.get("PUSHOVER_TOKEN") or ""
	user = os.environ.get("PUSHOVER_USER") or ""
	if not token or not user:
		print("missing PUSHOVER_TOKEN/USER", file=sys.stderr)
		return False
	if not image.is_file():
		print("missing image %s" % image, file=sys.stderr)
		return False

	boundary = "----bhNavBoundary7MA4YWxkTrZu0gW"
	mime = mimetypes.guess_type(str(image))[0] or "image/png"
	img_bytes = image.read_bytes()

	def part(name: str, value: bytes, filename: str | None = None, content_type: str | None = None) -> bytes:
		disp = 'Content-Disposition: form-data; name="%s"' % name
		if filename:
			disp += '; filename="%s"' % filename
		chunks = [("--%s" % boundary).encode(), disp.encode()]
		if content_type:
			chunks.append(("Content-Type: %s" % content_type).encode())
		chunks.append(b"")
		chunks.append(value)
		return b"\r\n".join(chunks)

	body = b"\r\n".join(
		[
			part("token", token.encode()),
			part("user", user.encode()),
			part("title", title[:250].encode("utf-8")),
			part("message", message[:1024].encode("utf-8")),
			part("attachment", img_bytes, filename=image.name, content_type=mime),
			("--%s--" % boundary).encode(),
			b"",
		]
	)
	req = urllib.request.Request(
		"https://api.pushover.net/1/messages.json",
		data=body,
		method="POST",
		headers={"Content-Type": "multipart/form-data; boundary=%s" % boundary},
	)
	try:
		with urllib.request.urlopen(req, timeout=60) as resp:
			print(image.name, resp.status, resp.read()[:200])
		return True
	except urllib.error.HTTPError as exc:
		print("HTTPError", exc.code, exc.read()[:500], file=sys.stderr)
		return False
	except Exception as exc:  # noqa: BLE001
		print("error", exc, file=sys.stderr)
		return False


def main() -> int:
	load_env()
	handoff = REPO / "docs" / "handoff"
	# Default: Faceplate Controls proof shots (260730-mun Wave C).
	# Pass --nav to send the older docked-nav verification set instead.
	if "--nav" in sys.argv:
		shots = [
			(
				handoff / "pushover-nav-root.png",
				"BH Nav — root",
				"Docked nav shows Plant + Operations from _Config/Navigation (Lightspeed lazy pattern). Search bar visible.",
			),
			(
				handoff / "nav-ok-search2.png",
				"BH Nav — search",
				"Search 'compress' filters tree (Compressors etc). Tag-driven nav + search working.",
			),
			(
				handoff / "nav-final-root.png",
				"BH Nav — loaded",
				"Perspective client after scan; Plant/Operations present. Machine Room under Plant in Document tag.",
			),
		]
	else:
		shots = [
			(
				handoff / "fp-controls-Compressor.png",
				"BH Controls: Compressor",
				"Unified Faceplate Controls — COMP-01. Header Web GUI visible (compressor-only). Mode/Status/KPI.",
			),
			(
				handoff / "fp-controls-Pump.png",
				"BH Controls: Pump",
				"Unified Faceplate Controls — PMP-01. Mode/Status/commands/KPI; no Web GUI.",
			),
			(
				handoff / "fp-controls-ExhaustFan.png",
				"BH Controls: ExhaustFan",
				"Unified Faceplate Controls — EFAN-01. Mode/Status/KPI; no Web GUI.",
			),
			(
				handoff / "fp-controls-CoolingTower.png",
				"BH Controls: CoolingTower",
				"Unified Faceplate Controls — CT-01. Mode/Status/KPI; no Web GUI.",
			),
			(
				handoff / "fp-controls-Valve.png",
				"BH Controls: Valve",
				"Unified Faceplate Controls — valve instance. Open/Close/Reset; no Web GUI.",
			),
			(
				handoff / "fp-controls-Tank.png",
				"BH Controls: Tank",
				"Unified Faceplate Controls — LTR-01. Level/Status; no Web GUI.",
			),
			(
				handoff / "fp-controls-Sensor.png",
				"BH Controls: Sensor",
				"Unified Faceplate Controls — sensor instance. PV/limits; no Web GUI.",
			),
			(
				handoff / "fp-controls-Evaporator.png",
				"BH Controls: Evaporator",
				"Unified Faceplate Controls — EV-01. Defrost/Status/KPI; no Web GUI.",
			),
		]
	ok = 0
	for path, title, msg in shots:
		if pushover_with_image(title, msg, path):
			ok += 1
	print("sent", ok, "of", len(shots))
	return 0 if ok else 1


if __name__ == "__main__":
	raise SystemExit(main())
