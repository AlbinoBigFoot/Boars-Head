#!/usr/bin/env python3
"""Patch globe marker hover → SiteCard highlight."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GLOBE_CFG = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.webdev/resources/globe/index/config.json"
)
DO_POST = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.webdev/resources/globe/mapMarkers/doPost.py"
)
TAGS = (
    ROOT
    / "gateways/standard/data/config/resources/core/ignition/tag-definition/default/_Config/tags.json"
)

OLD_POINTER = '''    g.events.on("pointerover", () => {
      nameLabel.set("text", dc.name ? String(dc.name) : "");
      // nameLabel.set("text", g.get("x"));
      row1_status.set("text", g.get("fill").toString() === "#ec8629" ? "Alarm" : "Normal");
      let hex = g.get("fill").toString().toUpperCase();
      setAlarmIcon(hex);
    });'''

NEW_POINTER = '''    g.events.on("pointerover", () => {
      nameLabel.set("text", dc.name ? String(dc.name) : "");
      // nameLabel.set("text", g.get("x"));
      row1_status.set("text", g.get("fill").toString() === "#ec8629" ? "Alarm" : "Normal");
      let hex = g.get("fill").toString().toUpperCase();
      setAlarmIcon(hex);
      // Highlight matching SiteCard in the Perspective rail
      try {
        var hoverUrl = (MAP_MARKER_URL instanceof URL ? MAP_MARKER_URL : new URL(MAP_MARKER_URL, window.location.href));
        fetch(hoverUrl.toString(), {
          method: "POST",
          credentials: "same-origin",
          headers: { "Accept": "application/json", "Content-Type": "application/json" },
          body: JSON.stringify({ "__hover": true, "page": dc.page || "", "name": dc.name || "" })
        });
      } catch (e) {}
    });

    g.events.on("pointerout", () => {
      try {
        var clearUrl = (MAP_MARKER_URL instanceof URL ? MAP_MARKER_URL : new URL(MAP_MARKER_URL, window.location.href));
        fetch(clearUrl.toString(), {
          method: "POST",
          credentials: "same-origin",
          headers: { "Accept": "application/json", "Content-Type": "application/json" },
          body: JSON.stringify({ "__hover": true, "page": "" })
        });
      } catch (e) {}
    });'''

DO_POST_BODY = '''def doPost(request, session):
\tdata = request['data']
\t# Site-rail hover highlight: {"__hover": true, "page": "/plants/groveport"}
\ttry:
\t\tisHover = data is not None and data.get('__hover') == True
\texcept:
\t\tisHover = False
\tif isHover:
\t\tpage = ''
\t\ttry:
\t\t\tpage = str(data.get('page') or '')
\t\texcept:
\t\t\tpage = ''
\t\tsystem.tag.writeBlocking(['[default]_Config/MapMarkerHover'], [page])
\t\treturn

\t# GeoJSON FeatureCollection updates markers.
\ttry:
\t\tisGeo = data is not None and data['type'] == 'FeatureCollection'
\texcept:
\t\tisGeo = False
\tif isGeo:
\t\tsystem.tag.writeBlocking(['[default]_Config/MapMarkerGeoJson'], [data])
\t\treturn

\t# Navigation document write: {"__nav": true, "items": [...]}
\ttry:
\t\tisNav = data is not None and data.get('__nav') == True and data.get('items') is not None
\texcept:
\t\tisNav = False
\tif isNav:
\t\tsystem.tag.writeBlocking(['[default]_Config/Navigation'], [{'items': data['items']}])
\t\ttry:
\t\t\tNavigation.Nav.flushCache()
\t\texcept:
\t\t\tpass
\t\treturn

\tsystem.tag.writeBlocking(['[default]_Config/MapMarkerNavigation'], [data])
'''


def patch_globe() -> None:
    cfg = json.loads(GLOBE_CFG.read_text(encoding="utf-8"))
    text = cfg["text"]
    if "__hover" in text and "pointerout" in text:
        print("globe index: hover already patched")
    else:
        if OLD_POINTER not in text:
            raise SystemExit("globe pointerover block not found — abort")
        text = text.replace(OLD_POINTER, NEW_POINTER, 1)
        cfg["text"] = text
        GLOBE_CFG.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
        print("globe index: patched pointerover/pointerout hover")

    DO_POST.write_text(DO_POST_BODY, encoding="utf-8")
    print("doPost: wrote MapMarkerHover handler")

    tags = json.loads(TAGS.read_text(encoding="utf-8"))
    if any(n.get("name") == "MapMarkerHover" for n in tags):
        print("tags: MapMarkerHover already present")
    else:
        for i, n in enumerate(tags):
            if n.get("name") == "MapMarkerNavigation":
                tags.insert(
                    i + 1,
                    {
                        "valueSource": "memory",
                        "dataType": "String",
                        "name": "MapMarkerHover",
                        "defaultValue": "",
                        "tagType": "AtomicTag",
                    },
                )
                break
        TAGS.write_text(json.dumps(tags, indent=2) + "\n", encoding="utf-8")
        print("tags: added MapMarkerHover")


if __name__ == "__main__":
    patch_globe()
