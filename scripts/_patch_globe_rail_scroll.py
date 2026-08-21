#!/usr/bin/env python3
"""Install client-side SiteRail auto-scroll from the globe iframe (no Perspective scripting)."""
from __future__ import annotations

import json
import re
from pathlib import Path

GLOBE_CFG = Path(__file__).resolve().parents[1] / (
    "gateways/standard/data/projects/BH/com.inductiveautomation.webdev"
    "/resources/globe/index/config.json"
)

MARKER = "/* __bhEnsureSiteRailScroll */"

ENSURE_RAIL_SCROLL = r"""
function __bhScrollSiteRailTo(page, name) {
  try {
    var doc = window.parent && window.parent.document;
    if (!doc) return;
    var rail = doc.querySelector(".psc-site-rail");
    if (!rail) return;
    var cards = rail.querySelectorAll("[class*='site-rail-card'], .view-parent");
    var target = null;
    var hot = rail.querySelector(".psc-site-rail-card--hot");
    if (hot) target = hot;
    if (!target && name) {
      var needle = String(name).toLowerCase();
      for (var i = 0; i < cards.length; i++) {
        var t = (cards[i].textContent || "").toLowerCase();
        if (needle && t.indexOf(needle) >= 0) { target = cards[i]; break; }
      }
    }
    if (!target && page) {
      var order = [
        "/plants/groveport",
        "/plants/new-castle",
        "/plants/forrest-city",
        "/plants/petersburg",
        "/plants/holland"
      ];
      var idx = order.indexOf(String(page));
      if (idx >= 0 && cards[idx]) target = cards[idx];
    }
    if (!target) return;
    var hr = target.getBoundingClientRect();
    var rr = rail.getBoundingClientRect();
    if (hr.top >= rr.top - 2 && hr.bottom <= rr.bottom + 2) return;
    target.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "nearest" });
    var hr2 = target.getBoundingClientRect();
    var rr2 = rail.getBoundingClientRect();
    if (hr2.top < rr2.top - 2 || hr2.bottom > rr2.bottom + 2) {
      rail.scrollTop += (hr2.top - rr2.top) - Math.max(0, (rr2.height - hr2.height) / 2);
    }
  } catch (e) {}
}

function __bhEnsureSiteRailScroll() {
  try {
    var w = window.parent;
    if (!w) return;
    if (w.__bhSiteRailScrollInstalled) return;
    w.__bhSiteRailScrollInstalled = true;
    var tick = function () {
      try {
        var doc = w.document;
        var hot = doc.querySelector(".psc-site-rail-card--hot");
        var rail = doc.querySelector(".psc-site-rail");
        if (!hot || !rail) return;
        var hr = hot.getBoundingClientRect();
        var rr = rail.getBoundingClientRect();
        if (hr.top < rr.top - 2 || hr.bottom > rr.bottom + 2) {
          __bhScrollSiteRailTo("", "");
        }
      } catch (e) {}
    };
    // Perspective class updates are not always MutationObserver-visible; poll.
    setInterval(tick, 120);
  } catch (e) {}
}
__bhEnsureSiteRailScroll();
try {
  window.__bhScrollSiteRailTo = __bhScrollSiteRailTo;
  window.__bhEnsureSiteRailScroll = __bhEnsureSiteRailScroll;
} catch (e) {}
""".strip()

POINTEROVER_INJECT = (
    'g.events.on("pointerover", () => {\n'
    "      __bhEnsureSiteRailScroll();\n"
    "      __bhScrollSiteRailTo(dc.page || '', dc.name || '');\n"
    "      setTimeout(function(){ __bhScrollSiteRailTo(dc.page || '', dc.name || ''); }, 200);"
)


def main() -> None:
    cfg = json.loads(GLOBE_CFG.read_text(encoding="utf-8"))
    text = cfg["text"]

    # Replace or insert marked block
    if MARKER in text:
        start = text.find(MARKER)
        end = text.find(MARKER, start + len(MARKER))
        if end < 0:
            raise SystemExit("broken marker pair")
        end += len(MARKER)
        text = text[:start] + MARKER + "\n" + ENSURE_RAIL_SCROLL + "\n" + MARKER + text[end:]
    else:
        insert_at = text.find("am5.ready(function()")
        if insert_at < 0:
            raise SystemExit("am5.ready not found")
        brace = text.find("{", insert_at)
        insert_at = brace + 1
        block = "\n" + MARKER + "\n" + ENSURE_RAIL_SCROLL + "\n" + MARKER + "\n"
        text = text[:insert_at] + block + text[insert_at:]

    # Normalize pointerover header (idempotent; strip prior inject junk)
    text = re.sub(
        r'g\.events\.on\("pointerover",\s*\(\)\s*=>\s*\{\s*'
        r'(?:__bhEnsureSiteRailScroll\(\);\s*)?'
        r"(?:__bhScrollSiteRailTo\([^;]+;\s*)?"
        r"(?:setTimeout\(function\(\)\{\s*__bhScrollSiteRailTo\([^;]+;\s*\},\s*200\);\s*)?"
        r"(?:\}\s*,\s*200\);\s*)*",
        POINTEROVER_INJECT + "\n",
        text,
        count=1,
    )

    cfg["text"] = text
    GLOBE_CFG.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")

    # Sanity: pointerover must not contain duplicated timeout close
    if "}, 200); }, 200)" in text:
        raise SystemExit("pointerover still corrupted")
    print("Patched globe iframe rail-scroll (direct + poll)")


if __name__ == "__main__":
    main()
