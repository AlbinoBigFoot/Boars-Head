# -*- coding: utf-8 -*-
"""Tighten SiteCard: no scrollbars, no pen overlap, less gauge dead space."""
from __future__ import print_function

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEWS = ROOT / (
    "gateways/standard/data/projects/BH/"
    "com.inductiveautomation.perspective/views"
)
CSS = ROOT / (
    "gateways/standard/data/projects/BH/"
    "com.inductiveautomation.perspective/stylesheet/stylesheet.css"
)

OVERLAYS = {
    "bad": False,
    "error": False,
    "pending": False,
    "stale": False,
    "unknown": False,
    "disabled": False,
}

PCT_EXPR = (
    "if(len(trim(coalesce({view.params.tagRoot}, ''))) = 0, 0, "
    "min(120, max(0, coalesce(try("
    "if(coalesce(try(if(isBadOrError(tag(coalesce({view.params.tagRoot}, '') + '/EPMS/Avg7Yr')), null, "
    "tag(coalesce({view.params.tagRoot}, '') + '/EPMS/Avg7Yr')), null), 0) = 0, 0, "
    "100.0 * coalesce(try(if(isBadOrError(tag(coalesce({view.params.tagRoot}, '') + '/EPMS/kWh')), null, "
    "tag(coalesce({view.params.tagRoot}, '') + '/EPMS/kWh')), null), 0) / "
    "coalesce(try(if(isBadOrError(tag(coalesce({view.params.tagRoot}, '') + '/EPMS/Avg7Yr')), null, "
    "tag(coalesce({view.params.tagRoot}, '') + '/EPMS/Avg7Yr')), null), 1)"
    "), null), 0))))"
)

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
    # Label left (ellipsis). Value+unit right, never shrink — no overlap.
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"basis": "26px", "shrink": 0},
        "props": {
            "direction": "row",
            "alignItems": "center",
            "justify": "space-between",
            "style": {
                "classes": "site-card-pen",
                "gap": "6px",
                "minHeight": "26px",
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
                    "style": {"gap": "4px", "flexShrink": "0"},
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
                                "fontSize": "13px",
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
                        "position": {"basis": "36px", "shrink": 0},
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

    # Full-circle radial fills the box; no empty band under a semi-arc.
    radial = {
        "type": "kyvislabs.display.apexchart",
        "meta": {"name": "LoadGauge"},
        "position": {"shrink": 0, "basis": "120px"},
        "props": {
            "type": "radialBar",
            "series": [0],
            "options": {
                "chart": {
                    "type": "radialBar",
                    "height": 120,
                    "width": 120,
                    "animations": {"enabled": False},
                    "sparkline": {"enabled": True},
                    "toolbar": {"show": False},
                    "offsetY": 0,
                },
                "colors": ["#0C7BB3"],
                "labels": ["vs 7yr"],
                "legend": {"show": False},
                "plotOptions": {
                    "radialBar": {
                        "hollow": {"size": "62%"},
                        "track": {
                            "background": "rgba(128,128,128,0.22)",
                            "strokeWidth": "97%",
                        },
                        "dataLabels": {
                            "name": {
                                "show": True,
                                "fontSize": "10px",
                                "offsetY": 14,
                                "color": "#888",
                            },
                            "value": {
                                "show": True,
                                "fontSize": "16px",
                                "fontWeight": 700,
                                "offsetY": -6,
                                "formatter": (
                                    "function (val) { return Math.round(val) + '%'; }"
                                ),
                            },
                        },
                    }
                },
                "stroke": {"lineCap": "round"},
            },
            "style": {
                "classes": "site-card-gauge",
                "height": "120px",
                "maxHeight": "120px",
                "overflow": "hidden",
                "width": "120px",
            },
        },
        "propConfig": {
            "props.series": {
                "binding": {
                    "type": "property",
                    "config": {"path": "view.custom.pct"},
                    "transforms": [
                        {
                            "type": "script",
                            "code": (
                                "\ttry:\n"
                                "\t\tv = float(value)\n"
                                "\texcept:\n"
                                "\t\tv = 0.0\n"
                                "\tif v < 0:\n"
                                "\t\tv = 0.0\n"
                                "\tif v > 100:\n"
                                "\t\tv = 100.0\n"
                                "\treturn [round(v, 1)]\n"
                            ),
                        }
                    ],
                    "overlays": OVERLAYS,
                }
            }
        },
    }

    return {
        "custom": {"pct": 0},
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
            "custom.pct": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": PCT_EXPR},
                    "overlays": OVERLAYS,
                },
                "persistent": True,
            },
        },
        "props": {"defaultSize": {"height": 168, "width": 400}},
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
                    "cursor": "pointer",
                    "gap": "6px",
                    "height": "100%",
                    "minHeight": "0",
                    "overflow": "hidden",
                    "padding": "10px 12px",
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
                    "meta": {"name": "Body"},
                    "position": {"grow": 1, "shrink": 1},
                    "props": {
                        "direction": "row",
                        "alignItems": "flex-start",
                        "style": {
                            "gap": "8px",
                            "minHeight": "0",
                            "overflow": "hidden",
                            "width": "100%",
                        },
                    },
                    "children": [
                        {
                            "type": "ia.container.flex",
                            "meta": {"name": "GaugeCol"},
                            "position": {"basis": "120px", "shrink": 0, "grow": 0},
                            "props": {
                                "direction": "column",
                                "alignItems": "center",
                                "justify": "center",
                                "style": {
                                    "height": "120px",
                                    "overflow": "hidden",
                                    "width": "120px",
                                },
                            },
                            "children": [radial],
                        },
                        {
                            "type": "ia.container.flex",
                            "meta": {"name": "Pens"},
                            "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                            "props": {
                                "direction": "column",
                                "justify": "space-between",
                                "style": {
                                    "gap": "0px",
                                    "minWidth": "0",
                                    "overflow": "hidden",
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
            ],
        },
    }


def patch_globe(g):
    def bump(node):
        if isinstance(node, dict):
            if node.get("props", {}).get("path") == "02_Components/02_Widgets/SiteCard":
                node["position"] = {"basis": "168px", "shrink": 0, "grow": 0}
                node["props"]["style"] = {
                    "height": "168px",
                    "maxHeight": "168px",
                    "minHeight": "168px",
                    "overflow": "hidden",
                    "width": "100%",
                }
            # Site rail: scroll the list, never the cards
            if node.get("meta", {}).get("name") == "SiteRail":
                st = node.setdefault("props", {}).setdefault("style", {})
                st["overflowY"] = "auto"
                st["overflowX"] = "hidden"
                st["gap"] = "10px"
            for val in node.values():
                bump(val)
        elif isinstance(node, list):
            for item in node:
                bump(item)

    bump(g)
    return g


def patch_css(text):
    block = """/* Lightspeed-inspired site picker + overview cards */
.psc-site-card {
	box-sizing: border-box;
	min-height: 0 !important;
	overflow: hidden !important;
	padding-bottom: 10px;
	transition: box-shadow 120ms ease, border-color 120ms ease;
}
.psc-site-card:hover {
	border-color: var(--callToAction, #0C7BB3);
	box-shadow: var(--boxShadow2, 0 4px 14px rgba(0,0,0,0.18));
}
.psc-site-card-gauge,
.psc-site-card-gauge .apexcharts-canvas {
	overflow: hidden !important;
	max-height: 120px !important;
}
.psc-site-card-pen {
	min-width: 0;
	overflow: hidden;
}
.psc-site-card-pen-label {
	min-width: 0;
}
.psc-site-card-pen-value {
	flex-shrink: 0;
	white-space: nowrap;
}
.psc-overview-card {
	box-sizing: border-box;
	min-width: 0;
}
"""
    marker = "/* Lightspeed-inspired site picker + overview cards */"
    if marker in text:
        start = text.index(marker)
        rest = text[start:]
        end_rel = rest.find(".psc-overview-card")
        if end_rel >= 0:
            sub = rest[end_rel:]
            brace = sub.find("}")
            end = start + end_rel + brace + 1
            return text[:start].rstrip() + "\n\n" + block + text[end:].lstrip("\n")
        return text[:start].rstrip() + "\n\n" + block
    return text.rstrip() + "\n\n" + block


def main():
    out_dir = Path(os.environ.get("TEMP", "/tmp"))
    sc_path = VIEWS / "02_Components/02_Widgets/SiteCard/view.json"
    gl_path = VIEWS / "00_Pages/LandingPage/Globe/view.json"

    sc = build()
    sc_tmp = out_dir / "sitecard-view.json"
    sc_tmp.write_text(json.dumps(sc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    try:
        sc_path.write_text(sc_tmp.read_text(encoding="utf-8"), encoding="utf-8")
        print("SiteCard written host")
    except OSError as e:
        print("SiteCard host write failed:", e)

    g = json.loads(gl_path.read_text(encoding="utf-8"))
    g = patch_globe(g)
    gl_tmp = out_dir / "globe-view-edit.json"
    gl_tmp.write_text(json.dumps(g, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Globe temp ready")

    css_text = patch_css(CSS.read_text(encoding="utf-8"))
    css_tmp = out_dir / "bh-stylesheet-edit.css"
    css_tmp.write_text(css_text, encoding="utf-8")
    print("CSS temp ready")
    print("TMP_SITE", sc_tmp)
    print("TMP_GLOBE", gl_tmp)
    print("TMP_CSS", css_tmp)


if __name__ == "__main__":
    main()
