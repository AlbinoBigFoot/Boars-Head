# -*- coding: utf-8 -*-
"""Port Lightspeed WebDev globe into BH project with BH theme CSS."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = Path(
	r"C:\Users\dylan.jones\Documents\Cursor\Ignition QA\assets\Lightspeed-Frontend"
	r"\projects\Lightspeed-FrontEnd\com.inductiveautomation.webdev\resources\globe"
)
DST = ROOT / "gateways/standard/data/projects/BH/com.inductiveautomation.webdev/resources/globe"
THEMES = ROOT / (
	"gateways/standard/data/config/resources/core/"
	"com.inductiveautomation.perspective/themes"
)


def flatten_theme_css(theme: str) -> str:
	theme_dir = THEMES / theme
	css = (theme_dir / "variables.css").read_text(encoding="utf-8")
	m = re.search(r'@import\s+"([^"]+)";', css)
	if m:
		imported = (theme_dir / m.group(1)).resolve().read_text(encoding="utf-8")
		css = imported + "\n" + re.sub(r'@import\s+"[^"]+";\s*', "", css)
	css = css.replace("\r\n", "\n").replace("\r", "\n")
	css += """
:root {
	--globe-ocean: var(--neutral-40);
	--globe-land: var(--neutral-20);
	--globe-land-active: var(--neutral-30);
	--globe-land-stroke: var(--neutral-70);
	--globe-marker: var(--callToAction, #114599);
}
html, body {
	margin: 0;
	width: 100%;
	height: 100%;
	background: var(--neutral-10);
	overflow: hidden;
}
"""
	return css


def main() -> None:
	if not SRC.is_dir():
		raise SystemExit("Lightspeed globe source missing: %s" % SRC)
	if DST.exists():
		shutil.rmtree(DST)
	shutil.copytree(SRC, DST)

	for path in DST.rglob("*"):
		if not path.is_file():
			continue
		try:
			text = path.read_text(encoding="utf-8")
		except UnicodeDecodeError:
			continue
		text = text.replace("\r\n", "\n").replace("\r", "\n")
		text = text.replace("Lightspeed-FrontEnd", "BH")
		path.write_text(text, encoding="utf-8", newline="\n")

	for theme in ("light", "light-cool", "light-warm", "dark", "dark-cool", "dark-warm"):
		out = DST / "css" / (theme + ".css") / "config.json"
		cfg = {
			"resource-type": "text-resource",
			"content-type": "text/css",
			"text": flatten_theme_css(theme),
		}
		out.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")

	idx = DST / "index" / "config.json"
	cfg = json.loads(idx.read_text(encoding="utf-8"))
	html = cfg["text"].replace("\r\n", "\n").replace("\r", "\n")
	html = html.replace("fill: am5.color(0xFFFFE7)", "fill: cssVar('--globe-land', '#DDE1E6')")
	html = html.replace("fill: am5.color(0xFFFFD6)", "fill: cssVar('--globe-land-active', '#C1C7CD')")
	html = html.replace("stroke: am5.color(0x000000)", "stroke: cssVar('--globe-land-stroke', '#4D5358')")
	html = html.replace("fill: cssVar('--neutral-40')", "fill: cssVar('--globe-ocean', '#A2A9B0')")
	html = html.replace("stroke: cssVar('--neutral-40')", "stroke: cssVar('--globe-ocean', '#A2A9B0')")
	# Groveport OH (~ -82.94, 39.84)
	html = html.replace("to: 70,", "to: 83,")
	html = html.replace("to: -40,", "to: -40,")
	cfg["text"] = html
	idx.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")

	for rj_path in DST.rglob("resource.json"):
		data = json.loads(rj_path.read_text(encoding="utf-8"))
		attrs = data.setdefault("attributes", {})
		attrs["lastModificationSignature"] = "0" * 64
		attrs["lastModification"] = {
			"actor": "cursor",
			"timestamp": "2026-08-01T18:30:00Z",
		}
		rj_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8", newline="\n")

	print("ported", DST)
	print("files", sum(1 for p in DST.rglob("*") if p.is_file()))


if __name__ == "__main__":
	main()
