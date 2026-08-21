#!/usr/bin/env python3
"""Wire Globe SiteRail cards to MapMarkerHover (hot/dim classes + auto-scroll)."""
from __future__ import annotations

import json
from pathlib import Path

GLOBE = Path(__file__).resolve().parents[1] / (
    "gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
    "/views/00_Pages/LandingPage/Globe/view.json"
)

SITES = [
    ("Site_Groveport", "/plants/groveport"),
    ("Site_NewCastle", "/plants/new-castle"),
    ("Site_ForrestCity", "/plants/forrest-city"),
    ("Site_Petersburg", "/plants/petersburg"),
    ("Site_Holland", "/plants/holland"),
]

HOVER_SCROLL_JS = r"""
(function(){
  var tryScroll = function(n){
    var el = document.querySelector('.psc-site-rail .psc-site-rail-card--hot');
    var rail = document.querySelector('.psc-site-rail');
    if (el && rail) {
      el.scrollIntoView({behavior: 'smooth', block: 'nearest', inline: 'nearest'});
      var er = el.getBoundingClientRect();
      var rr = rail.getBoundingClientRect();
      if (er.bottom > rr.bottom + 2 || er.top < rr.top - 2) {
        rail.scrollTop += (er.top - rr.top) - Math.max(0, (rr.height - er.height) / 2);
      }
      return;
    }
    if (n > 0) setTimeout(function(){ tryScroll(n - 1); }, 50);
  };
  tryScroll(30);
})();
""".strip()

# Runs on SiteRail custom.hoverPage change (component script → browser session).
RAIL_HOVER_ONCHANGE = (
    "\tpage = currentValue.value\n"
    "\tif page is None or str(page).strip() == '':\n"
    "\t\treturn\n"
    "\tjs = " + json.dumps(HOVER_SCROLL_JS) + "\n"
    "\ttry:\n"
    "\t\tif hasattr(system.perspective, 'runJavaScriptAsync'):\n"
    "\t\t\tsystem.perspective.runJavaScriptAsync(js)\n"
    "\t\telif hasattr(system.perspective, 'runJavaScript'):\n"
    "\t\t\tsystem.perspective.runJavaScript(js)\n"
    "\texcept:\n"
    "\t\tpass\n"
)


def hover_class_expr(page: str) -> str:
    return (
        f"if(coalesce({{view.custom.hoverPage}}, '') = '', '', "
        f"if({{view.custom.hoverPage}} = '{page}', 'site-rail-card--hot', 'site-rail-card--dim'))"
    )


def main() -> None:
    view = json.loads(GLOBE.read_text(encoding="utf-8"))
    custom = view.setdefault("custom", {})
    custom["hoverPage"] = ""
    prop_config = view.setdefault("propConfig", {})
    # View only binds the tag — scrolling is handled on SiteRail (client-friendlier).
    prop_config["custom.hoverPage"] = {
        "binding": {
            "type": "tag",
            "config": {
                "tagPath": "[default]_Config/MapMarkerHover",
                "mode": "direct",
                "fallbackDelay": 2.5,
            },
            "transforms": [
                {
                    "type": "expression",
                    "expression": "coalesce({value}, '')",
                }
            ],
        },
        "persistent": True,
    }

    root = view["root"]
    for child in root["children"]:
        if child.get("meta", {}).get("name") != "SiteRail":
            continue
        style = child["props"].setdefault("style", {})
        classes = style.get("classes", "")
        if "site-rail" not in classes.split():
            style["classes"] = (classes + " site-rail").strip()
        if "padding" not in style or "44px" not in str(style.get("padding", "")):
            style["padding"] = "12px 8px 12px 44px"

        child.setdefault("custom", {})["hoverPage"] = ""
        child_pc = child.setdefault("propConfig", {})
        child_pc["custom.hoverPage"] = {
            "binding": {
                "type": "property",
                "config": {"path": "view.custom.hoverPage"},
            },
            "onChange": {
                "enabled": None,
                "script": RAIL_HOVER_ONCHANGE,
            },
            "persistent": True,
        }

        for embed in child.get("children", []):
            name = embed.get("meta", {}).get("name")
            page = next((p for n, p in SITES if n == name), None)
            if not page:
                continue
            st = embed["props"].setdefault("style", {})
            st.pop("classes", None)
            pc = embed.setdefault("propConfig", {})
            pc["props.style.classes"] = {
                "binding": {
                    "type": "expr",
                    "config": {"expression": hover_class_expr(page)},
                }
            }
        break

    # Keep ticketLog; drop unused globeSiteHoverScroll if present
    scripts = root.setdefault("scripts", {})
    handlers = [
        h
        for h in (scripts.get("messageHandlers") or [])
        if h.get("messageType") != "globeSiteHoverScroll"
    ]
    scripts["messageHandlers"] = handlers
    scripts.setdefault("customMethods", [])
    if "extensionFunctions" not in scripts:
        scripts["extensionFunctions"] = None

    GLOBE.write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8")
    json.loads(GLOBE.read_text(encoding="utf-8"))
    print("Globe: SiteRail onChange → runJavaScript scrollIntoView")


if __name__ == "__main__":
    main()
