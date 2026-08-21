# -*- coding: utf-8 -*-
"""SiteCard = site name + live metric pens only (no gauge)."""
from __future__ import print_function

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEWS = ROOT / (
    "gateways/standard/data/projects/BH/"
    "com.inductiveautomation.perspective/views"
)
TEMP = Path(os.environ.get("TEMP", "/tmp"))

OVERLAYS = {
    "bad": False,
    "error": False,
    "pending": False,
    "stale": False,
    "unknown": False,
    "disabled": False,
}

CLICK_NAV = (
    "\tpage = str(self.view.params.page or '').strip()\n"
    "\tif not page:\n"
    "\t\treturn\n"
    "\tNavigation.Nav.navigate({'action': 'page', 'page': page})\n"
)


def tag_text(path_expr, fmt="#,##0"):
    return {
        "binding": {
            "type": "expr",
            "config": {
                "expression": (
                    "numberFormat(coalesce(try(if(isBadOrError(tag(%s)), null, tag(%s)), null), 0), '%s')"
                    % (path_expr, path_expr, fmt)
                )
            },
            "overlays": OVERLAYS,
        }
    }


def pen(name, label, unit, path_expr, fmt="#,##0"):
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"basis": "28px", "shrink": 0},
        "props": {
            "direction": "row",
            "alignItems": "center",
            "justify": "space-between",
            "style": {
                "classes": "site-card-pen",
                "gap": "8px",
                "minHeight": "28px",
                "overflow": "hidden",
                "width": "100%",
            },
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "Lbl"},
                "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                "props": {
                    "text": label,
                    "style": {
                        "classes": "font-label site-card-pen-label",
                        "fontSize": "12px",
                        "opacity": "0.85",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                        "whiteSpace": "nowrap",
                    },
                },
            },
            {
                "type": "ia.container.flex",
                "meta": {"name": "ValueUnit"},
                "position": {"shrink": 0, "grow": 0},
                "props": {
                    "direction": "row",
                    "alignItems": "baseline",
                    "justify": "flex-end",
                    "style": {"gap": "6px", "flexShrink": "0"},
                },
                "children": [
                    {
                        "type": "ia.display.label",
                        "meta": {"name": "Val"},
                        "position": {"shrink": 0},
                        "props": {
                            "text": "—",
                            "style": {
                                "classes": "font-livedata-entry site-card-pen-value",
                                "fontSize": "14px",
                                "fontWeight": "600",
                                "textAlign": "right",
                                "whiteSpace": "nowrap",
                            },
                        },
                        "propConfig": {"props.text": tag_text(path_expr, fmt)},
                    },
                    {
                        "type": "ia.display.label",
                        "meta": {"name": "Unit"},
                        "position": {"basis": "40px", "shrink": 0},
                        "props": {
                            "text": unit,
                            "style": {
                                "classes": "font-label",
                                "fontSize": "11px",
                                "opacity": "0.7",
                                "whiteSpace": "nowrap",
                            },
                        },
                    },
                ],
            },
        ],
    }


def build():
    kwh = "coalesce({view.params.tagRoot}, '') + '/EPMS/kWh'"
    therm = "coalesce({view.params.tagRoot}, '') + '/Utility/Therm'"
    prod = "coalesce({view.params.tagRoot}, '') + '/Production/ProdVol'"
    temp = "coalesce({view.params.tagRoot}, '') + '/Utility/AmbientAvgF'"

    return {
        "custom": {},
        "params": {
            "siteName": "Plant",
            "region": "",
            "page": "",
            "tagRoot": "",
        },
        "propConfig": {
            "params.siteName": {"paramDirection": "input", "persistent": True},
            "params.region": {"paramDirection": "input", "persistent": True},
            "params.page": {"paramDirection": "input", "persistent": True},
            "params.tagRoot": {"paramDirection": "input", "persistent": True},
        },
        "props": {"defaultSize": {"height": 156, "width": 380}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "events": {
                "dom": {
                    "onClick": {
                        "config": {"script": CLICK_NAV},
                        "scope": "G",
                        "type": "script",
                    }
                }
            },
            "props": {
                "direction": "column",
                "style": {
                    "classes": "container-card container-card-border site-card",
                    "boxSizing": "border-box",
                    "cursor": "pointer",
                    "gap": "8px",
                    "height": "100%",
                    "minHeight": "0",
                    "overflow": "visible",
                    "padding": "12px 14px 14px",
                    "width": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "TitleRow"},
                    "position": {"shrink": 0, "basis": "22px"},
                    "props": {
                        "direction": "row",
                        "alignItems": "baseline",
                        "justify": "space-between",
                        "style": {"gap": "8px", "width": "100%"},
                    },
                    "children": [
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "SiteName"},
                            "position": {"grow": 1, "shrink": 1},
                            "props": {
                                "text": "Plant",
                                "style": {
                                    "classes": "font-title",
                                    "fontSize": "15px",
                                    "fontWeight": "700",
                                    "overflow": "hidden",
                                    "textOverflow": "ellipsis",
                                    "whiteSpace": "nowrap",
                                },
                            },
                            "propConfig": {
                                "props.text": {
                                    "binding": {
                                        "type": "property",
                                        "config": {"path": "view.params.siteName"},
                                    }
                                }
                            },
                        },
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Region"},
                            "position": {"shrink": 0},
                            "props": {
                                "text": "",
                                "style": {
                                    "classes": "font-label",
                                    "fontSize": "11px",
                                    "opacity": "0.75",
                                    "whiteSpace": "nowrap",
                                },
                            },
                            "propConfig": {
                                "props.text": {
                                    "binding": {
                                        "type": "property",
                                        "config": {"path": "view.params.region"},
                                    }
                                }
                            },
                        },
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Pens"},
                    "position": {"grow": 1, "shrink": 1},
                    "props": {
                        "direction": "column",
                        "justify": "space-between",
                        "style": {
                            "gap": "2px",
                            "minWidth": "0",
                            "overflow": "visible",
                            "width": "100%",
                        },
                    },
                    "children": [
                        pen("PenKwh", "kWh (MTD)", "kWh", kwh, "#,##0"),
                        pen("PenTherm", "Natural Gas", "therm", therm, "#,##0"),
                        pen("PenProd", "Production", "lb", prod, "#,##0"),
                        pen("PenTemp", "Outdoor Temp", "°F", temp, "#,##0.#"),
                    ],
                },
            ],
        },
    }


def patch_globe(g):
    def walk(node):
        if isinstance(node, dict):
            if node.get("props", {}).get("path") == "02_Components/02_Widgets/SiteCard":
                node["position"] = {"basis": "156px", "shrink": 0, "grow": 0}
                node["props"]["style"] = {
                    "height": "156px",
                    "maxHeight": "156px",
                    "minHeight": "156px",
                    "marginBottom": "4px",
                    "overflow": "visible",
                    "width": "100%",
                }
            for val in node.values():
                walk(val)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(g)
    return g


def main():
    sc = build()
    sc_tmp = TEMP / "sitecard-view.json"
    sc_tmp.write_text(json.dumps(sc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sc_path = VIEWS / "02_Components/02_Widgets/SiteCard/view.json"
    try:
        sc_path.write_text(sc_tmp.read_text(encoding="utf-8"), encoding="utf-8")
        print("SiteCard host ok")
    except OSError as e:
        print("SiteCard host fail:", e)

    gl_path = VIEWS / "00_Pages/LandingPage/Globe/view.json"
    g = patch_globe(json.loads(gl_path.read_text(encoding="utf-8")))
    gl_tmp = TEMP / "globe-view-edit.json"
    gl_tmp.write_text(json.dumps(g, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Globe temp ok")


if __name__ == "__main__":
    main()
