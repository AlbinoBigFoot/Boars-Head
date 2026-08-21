# -*- coding: utf-8 -*-
"""Rebuild home Site cards + denser Groveport Overview (Lightspeed-inspired)."""
from __future__ import print_function

import json
import os
from copy import deepcopy

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BH = os.path.join(
    ROOT,
    "gateways",
    "standard",
    "data",
    "projects",
    "BH",
    "com.inductiveautomation.perspective",
)
VIEWS = os.path.join(BH, "views")
STYLESHEET = os.path.join(BH, "stylesheet", "stylesheet.css")

OVERLAYS = {
    "bad": False,
    "error": False,
    "pending": False,
    "stale": False,
    "unknown": False,
    "disabled": False,
}

SITES = [
    {
        "name": "Groveport",
        "region": "Ohio",
        "page": "/plants/groveport",
        "tagRoot": "[default]KPI/Groveport/Site",
        "hasData": True,
    },
    {
        "name": "New Castle",
        "region": "Indiana",
        "page": "/plants/new-castle",
        "tagRoot": "[default]KPI/NewCastle/Site",
        "hasData": False,
    },
    {
        "name": "Forrest City",
        "region": "Arkansas",
        "page": "/plants/forrest-city",
        "tagRoot": "[default]KPI/ForrestCity/Site",
        "hasData": False,
    },
    {
        "name": "Petersburg",
        "region": "Virginia",
        "page": "/plants/petersburg",
        "tagRoot": "[default]KPI/Petersburg/Site",
        "hasData": False,
    },
    {
        "name": "Holland",
        "region": "Michigan",
        "page": "/plants/holland",
        "tagRoot": "[default]KPI/Holland/Site",
        "hasData": False,
    },
]

CLICK_NAV = (
    "\tpage = str(self.view.params.page or '').strip()\n"
    "\tif not page:\n"
    "\t\treturn\n"
    "\tNavigation.Nav.navigate({'action': 'page', 'page': page})\n"
)

SPARK_SCRIPT = """\t# Placeholder spark until historian — deterministic wobble around live value.
\traw = value
\ttry:
\t\tbase = float(raw)
\texcept:
\t\ttry:
\t\t\ts = str(raw or '0').replace(',', '').replace(u'\\u2014', '').strip()
\t\t\tbase = float(s) if s else 0.0
\t\texcept:
\t\t\tbase = 0.0
\tnow = int(system.date.toMillis(system.date.now()))
\thour_ms = 3600 * 1000
\tseed = abs(hash(str(round(base, 3)))) % 10007
\tdata = []
\tvals = []
\tfor i in range(24):
\t\tphase = ((seed + i * 37) % 100) / 100.0
\t\twobble = 0.92 + 0.16 * phase
\t\tif abs(base) < 1e-9:
\t\t\tv = float((seed + i * 13) % 50) / 10.0
\t\telse:
\t\t\tv = base * wobble
\t\tts = now - (23 - i) * hour_ms
\t\tdata.append([ts, round(v, 2)])
\t\tvals.append(v)
\tmn = min(vals) if vals else 0.0
\tmx = max(vals) if vals else 0.0
\tavg = (sum(vals) / float(len(vals))) if vals else 0.0
\tdef fmt(n):
\t\ttry:
\t\t\treturn '{:,.1f}'.format(float(n))
\t\texcept:
\t\t\treturn u'\\u2014'
\treturn {
\t\t'series': [{'name': 'Trend', 'data': data}],
\t\t'min': fmt(mn),
\t\t'max': fmt(mx),
\t\t'avg': fmt(avg),
\t}
"""


def dumps(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def write_json(path, obj):
    parent = os.path.dirname(path)
    if not os.path.isdir(parent):
        os.makedirs(parent)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(dumps(obj))
    print("wrote", os.path.relpath(path, ROOT))


def resource_stub():
    return {
        "scope": "G",
        "version": 1,
        "restricted": False,
        "overridable": True,
        "files": ["view.json"],
        "attributes": {
            "lastModificationSignature": "0" * 64,
            "lastModification": {
                "actor": "external",
                "timestamp": "2026-08-20T19:00:00Z",
            },
        },
    }


def tag_expr(path_expr, fmt="#,##0.#"):
    return (
        "numberFormat(coalesce(try(if(isBadOrError(tag(%s)), null, tag(%s)), null), 0), '%s')"
        % (path_expr, path_expr, fmt)
    )


def live_tag_binding(path_expr, fmt="#,##0.#"):
    return {
        "binding": {
            "type": "expr",
            "config": {"expression": tag_expr(path_expr, fmt)},
            "overlays": OVERLAYS,
        }
    }


def metric_pen_row(name, label, unit, tag_suffix_expr):
    """Inline pen row (label | value | unit) — Lightspeed AnalogValuePen density."""
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"basis": "28px", "shrink": 0},
        "props": {
            "direction": "row",
            "alignItems": "center",
            "justify": "space-between",
            "style": {"gap": "8px", "width": "100%", "minHeight": "28px"},
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "Lbl"},
                "position": {"grow": 1},
                "props": {
                    "text": label,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "12px",
                        "opacity": "0.85",
                    },
                },
            },
            {
                "type": "ia.display.label",
                "meta": {"name": "Val"},
                "position": {"shrink": 0},
                "props": {
                    "text": "—",
                    "style": {
                        "classes": "font-livedata-entry",
                        "fontSize": "13px",
                        "fontWeight": "600",
                        "textAlign": "right",
                        "minWidth": "72px",
                    },
                },
                "propConfig": {
                    "props.text": live_tag_binding(tag_suffix_expr),
                },
            },
            {
                "type": "ia.display.label",
                "meta": {"name": "Unit"},
                "position": {"basis": "42px", "shrink": 0},
                "props": {
                    "text": unit,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "opacity": "0.7",
                    },
                },
            },
        ],
    }


def build_site_card():
    """Lightspeed Site-style summary card for one BH plant."""
    # tagRoot + leaf paths
    kwh = "coalesce({view.params.tagRoot}, '') + '/EPMS/kWh'"
    avg7 = "coalesce({view.params.tagRoot}, '') + '/EPMS/Avg7Yr'"
    therm = "coalesce({view.params.tagRoot}, '') + '/Utility/Therm'"
    prod = "coalesce({view.params.tagRoot}, '') + '/Production/ProdVol'"
    temp = "coalesce({view.params.tagRoot}, '') + '/Utility/AmbientAvgF'"

    # Gauge: kWh as % of 7yr avg (0–120)
    gauge_expr = (
        "if(len(trim(coalesce({view.params.tagRoot}, ''))) = 0, 0, "
        "min(120, max(0, "
        "coalesce(try("
        "if(coalesce(try(if(isBadOrError(tag(%s)), null, tag(%s)), null), 0) = 0, 0, "
        "100.0 * coalesce(try(if(isBadOrError(tag(%s)), null, tag(%s)), null), 0) / "
        "coalesce(try(if(isBadOrError(tag(%s)), null, tag(%s)), null), 1)"
        "), null), 0))))" % (avg7, avg7, kwh, kwh, avg7, avg7)
    )

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
        "props": {"defaultSize": {"height": 200, "width": 400}},
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
                    "gap": "8px",
                    "height": "100%",
                    "minHeight": "190px",
                    "overflow": "hidden",
                    "padding": "12px 14px",
                    "width": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "TitleRow"},
                    "position": {"shrink": 0},
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
                            "position": {"grow": 1},
                            "props": {
                                "text": "Plant",
                                "style": {
                                    "classes": "font-title",
                                    "fontSize": "16px",
                                    "fontWeight": "700",
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
                                    "fontSize": "12px",
                                    "opacity": "0.75",
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
                    "position": {"grow": 1},
                    "props": {
                        "direction": "row",
                        "style": {"gap": "10px", "height": "100%", "width": "100%"},
                    },
                    "children": [
                        {
                            "type": "ia.container.flex",
                            "meta": {"name": "GaugeCol"},
                            "position": {"basis": "110px", "shrink": 0},
                            "props": {
                                "direction": "column",
                                "alignItems": "center",
                                "justify": "center",
                                "style": {"gap": "2px", "overflow": "hidden"},
                            },
                            "children": [
                                {
                                    "type": "ia.display.label",
                                    "meta": {"name": "GaugeLbl"},
                                    "props": {
                                        "text": "kWh vs 7yr",
                                        "style": {
                                            "classes": "font-label",
                                            "fontSize": "10px",
                                            "letterSpacing": "0.04em",
                                            "textAlign": "center",
                                            "textTransform": "uppercase",
                                        },
                                    },
                                },
                                {
                                    "type": "ia.chart.simple-gauge",
                                    "meta": {"name": "LoadGauge"},
                                    "position": {"grow": 1, "basis": "90px"},
                                    "props": {
                                        "animate": True,
                                        "value": 0,
                                        "minValue": 0,
                                        "maxValue": 120,
                                        "startAngle": 270,
                                        "endAngle": 630,
                                        "arc": {"width": 10, "cornerRadius": 1, "color": "#0C7BB3"},
                                        "arcBackground": {"opacity": 0.25},
                                        "label": {
                                            "units": "%",
                                            "size": 11,
                                            "maxDecimal": 0,
                                            "offsetY": 8,
                                        },
                                        "style": {
                                            "height": "100%",
                                            "marginTop": "-6px",
                                            "width": "100%",
                                        },
                                    },
                                    "propConfig": {
                                        "props.value": {
                                            "binding": {
                                                "type": "expr",
                                                "config": {"expression": gauge_expr},
                                                "overlays": OVERLAYS,
                                            }
                                        }
                                    },
                                },
                            ],
                        },
                        {
                            "type": "ia.container.flex",
                            "meta": {"name": "Pens"},
                            "position": {"grow": 1},
                            "props": {
                                "direction": "column",
                                "justify": "space-evenly",
                                "style": {"gap": "2px", "minWidth": "0", "width": "100%"},
                            },
                            "children": [
                                metric_pen_row("PenKwh", "kWh (MTD)", "kWh", kwh),
                                metric_pen_row("PenTherm", "Natural Gas", "therm", therm),
                                metric_pen_row("PenProd", "Production", "lb", prod),
                                metric_pen_row("PenTemp", "Outdoor Temp", "°F", temp),
                            ],
                        },
                    ],
                },
            ],
        },
    }


def site_embed(site):
    return {
        "type": "ia.display.view",
        "meta": {"name": "Site_" + site["name"].replace(" ", "")},
        "position": {"basis": "200px", "shrink": 0},
        "props": {
            "path": "02_Components/02_Widgets/SiteCard",
            "params": {
                "siteName": site["name"],
                "region": site["region"],
                "page": site["page"],
                "tagRoot": site["tagRoot"],
            },
            "style": {
                "height": "200px",
                "minHeight": "190px",
                "overflow": "hidden",
                "width": "100%",
            },
        },
    }


def patch_globe():
    path = os.path.join(VIEWS, "00_Pages", "LandingPage", "Globe", "view.json")
    with open(path, encoding="utf-8") as f:
        globe = json.load(f)

    site_rail = {
        "type": "ia.container.flex",
        "meta": {"name": "SiteRail"},
        "position": {"basis": "420px", "shrink": 0},
        "props": {
            "direction": "column",
            "style": {
                "classes": "themed-scroll",
                "gap": "12px",
                "height": "100%",
                "minHeight": "0",
                "overflowY": "auto",
                "padding": "12px 12px 12px 4px",
            },
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "RailTitle"},
                "position": {"shrink": 0},
                "props": {
                    "text": "Sites",
                    "style": {
                        "classes": "font-title",
                        "fontSize": "14px",
                        "fontWeight": "700",
                        "letterSpacing": "0.06em",
                        "textTransform": "uppercase",
                    },
                },
            },
            {
                "type": "ia.display.label",
                "meta": {"name": "RailHint"},
                "position": {"shrink": 0},
                "props": {
                    "text": "Open a plant overview",
                    "style": {"classes": "font-label", "fontSize": "12px", "opacity": "0.75"},
                },
            },
        ]
        + [site_embed(s) for s in SITES],
    }

    children = globe["root"]["children"]
    # Replace KpiRail / SiteRail
    new_children = []
    replaced = False
    for ch in children:
        name = ch.get("meta", {}).get("name")
        if name in ("KpiRail", "SiteRail"):
            new_children.append(site_rail)
            replaced = True
        else:
            new_children.append(ch)
    if not replaced:
        new_children.append(site_rail)
    globe["root"]["children"] = new_children
    write_json(path, globe)


def overview_card(name, title, left_children, right_child=None, time_default="24"):
    """Lightspeed Container/Card: title + time range + split Data."""
    header = {
        "type": "ia.container.flex",
        "meta": {"name": "LabelTimeRange"},
        "position": {"shrink": 0},
        "props": {
            "direction": "row",
            "alignItems": "center",
            "justify": "space-between",
            "style": {"gap": "12px", "width": "100%"},
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "CardTitle"},
                "position": {"grow": 1},
                "props": {
                    "text": title,
                    "style": {
                        "classes": "font-title",
                        "fontSize": "15px",
                        "fontWeight": "700",
                    },
                },
            },
            {
                "type": "ia.input.dropdown",
                "meta": {"name": "timeRange"},
                "position": {"basis": "150px", "shrink": 0},
                "props": {
                    "value": time_default,
                    "options": [
                        {"label": "Last Hour", "value": "1"},
                        {"label": "Last 24 hours", "value": "24"},
                        {"label": "Last Week", "value": "168"},
                        {"label": "Last Month", "value": "730"},
                    ],
                    "style": {"width": "100%"},
                },
            },
        ],
    }

    data_children = [
        {
            "type": "ia.container.flex",
            "meta": {"name": "Left"},
            "position": {"grow": 1, "basis": "42%"},
            "props": {
                "direction": "column",
                "style": {"gap": "8px", "minWidth": "0", "paddingRight": "8px"},
            },
            "children": left_children,
        }
    ]
    if right_child:
        data_children.append(
            {
                "type": "ia.container.flex",
                "meta": {"name": "Right"},
                "position": {"grow": 1, "basis": "58%"},
                "props": {
                    "direction": "column",
                    "style": {"gap": "4px", "minHeight": "180px", "minWidth": "0"},
                },
                "children": [right_child],
            }
        )

    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "props": {
            "direction": "column",
            "style": {
                "classes": "container-card container-card-border overview-card",
                "gap": "10px",
                "height": "100%",
                "minHeight": "280px",
                "overflow": "hidden",
                "padding": "14px 16px",
                "width": "100%",
            },
        },
        "children": [
            header,
            {
                "type": "ia.container.flex",
                "meta": {"name": "Data"},
                "position": {"grow": 1},
                "props": {
                    "direction": "row",
                    "style": {"gap": "8px", "height": "100%", "minHeight": "0", "width": "100%"},
                },
                "children": data_children,
            },
        ],
    }


def kpi_embed_inline(name, title, category, unit, tag_path):
    return {
        "type": "ia.display.view",
        "meta": {"name": name},
        "position": {"grow": 1},
        "props": {
            "path": "02_Components/02_Widgets/KPI",
            "params": {
                "title": title,
                "category": category,
                "unit": unit,
                "tagPath": tag_path,
                "value": "0",
            },
            "style": {"height": "100%", "minHeight": "220px", "width": "100%"},
        },
    }


def big_value(name, label, unit, tag_path):
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"shrink": 0},
        "props": {
            "direction": "column",
            "style": {"gap": "2px", "width": "100%"},
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "L"},
                "props": {
                    "text": label,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "letterSpacing": "0.04em",
                        "textTransform": "uppercase",
                    },
                },
            },
            {
                "type": "ia.container.flex",
                "meta": {"name": "Row"},
                "props": {
                    "direction": "row",
                    "alignItems": "baseline",
                    "style": {"gap": "8px"},
                },
                "children": [
                    {
                        "type": "ia.display.label",
                        "meta": {"name": "V"},
                        "props": {
                            "text": "—",
                            "style": {
                                "classes": "font-livedata-entry kpi-value",
                                "fontSize": "2rem",
                                "lineHeight": "1.1",
                            },
                        },
                        "propConfig": {
                            "props.text": live_tag_binding("'%s'" % tag_path),
                        },
                    },
                    {
                        "type": "ia.display.label",
                        "meta": {"name": "U"},
                        "props": {
                            "text": unit,
                            "style": {"classes": "font-label", "fontSize": "0.95rem"},
                        },
                    },
                ],
            },
        ],
    }


def build_groveport_overview():
    root_tag = "[default]KPI/Groveport/Site"
    epms_left = [
        big_value("HeroKwh", "Site energy (MTD)", "kWh", root_tag + "/EPMS/kWh"),
        {
            "type": "ia.chart.simple-gauge",
            "meta": {"name": "VsAvg"},
            "position": {"basis": "120px", "shrink": 0},
            "props": {
                "animate": True,
                "value": 0,
                "minValue": 0,
                "maxValue": 120,
                "startAngle": 270,
                "endAngle": 630,
                "arc": {"width": 12, "cornerRadius": 1, "color": "#0C7BB3"},
                "arcBackground": {"opacity": 0.25},
                "label": {"units": "% of 7yr avg", "size": 10, "maxDecimal": 0, "offsetY": 10},
                "style": {"height": "120px", "width": "100%"},
            },
            "propConfig": {
                "props.value": {
                    "binding": {
                        "type": "expr",
                        "config": {
                            "expression": (
                                "min(120, max(0, if(coalesce(try(if(isBadOrError("
                                "tag('%s/EPMS/Avg7Yr')), null, tag('%s/EPMS/Avg7Yr')), null), 0) = 0, 0, "
                                "100.0 * coalesce(try(if(isBadOrError(tag('%s/EPMS/kWh')), null, "
                                "tag('%s/EPMS/kWh')), null), 0) / "
                                "coalesce(try(if(isBadOrError(tag('%s/EPMS/Avg7Yr')), null, "
                                "tag('%s/EPMS/Avg7Yr')), null), 1))))"
                                % ((root_tag,) * 6)
                            )
                        },
                        "overlays": OVERLAYS,
                    }
                }
            },
        },
        metric_pen_row(
            "Kvar", "Reactive", "kvar", "'%s/EPMS/Kvar'" % root_tag
        ),
        metric_pen_row(
            "Avg3", "3yr month avg", "kWh", "'%s/EPMS/Avg3Yr'" % root_tag
        ),
        metric_pen_row(
            "Avg7", "7yr month avg", "kWh", "'%s/EPMS/Avg7Yr'" % root_tag
        ),
    ]

    util_left = [
        big_value("HeroTherm", "Natural gas", "therm", root_tag + "/Utility/Therm"),
        metric_pen_row("H2O", "Water", "H2O", "'%s/Utility/H2O'" % root_tag),
        metric_pen_row("CO2", "CO₂", "lb", "'%s/Utility/CO2'" % root_tag),
        metric_pen_row(
            "Tavg", "Outdoor avg", "°F", "'%s/Utility/AmbientAvgF'" % root_tag
        ),
        metric_pen_row(
            "Tmax", "Outdoor max", "°F", "'%s/Utility/AmbientMaxF'" % root_tag
        ),
        metric_pen_row(
            "Tmin", "Outdoor min", "°F", "'%s/Utility/AmbientMinF'" % root_tag
        ),
    ]

    prod_left = [
        big_value(
            "HeroProd", "Production volume", "lb", root_tag + "/Production/ProdVol"
        ),
        metric_pen_row(
            "Avg7d", "7d avg volume", "lb", "'%s/Production/ProdVolAvg7d'" % root_tag
        ),
        metric_pen_row(
            "Intensity", "Energy intensity", "kWh/lb", "'%s/Production/kWhPerLb'" % root_tag
        ),
    ]

    grid_style = {
        "classes": "bg-page kpi-dashboard-page",
        "display": "grid",
        "gap": "16px",
        "gridTemplateColumns": "1fr 1fr",
        "gridTemplateRows": "auto 1fr 1fr",
        "height": "100%",
        "minHeight": "0",
        "overflowY": "auto",
        "padding": "20px 24px",
        "width": "100%",
    }

    title_block = {
        "type": "ia.container.flex",
        "meta": {"name": "TitleBlock"},
        "props": {
            "direction": "column",
            "style": {
                "gap": "4px",
                "gridColumn": "1 / -1",
                "width": "100%",
            },
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "Title"},
                "props": {
                    "text": "Groveport — Site Overview",
                    "style": {
                        "classes": "font-title",
                        "fontSize": "22px",
                        "fontWeight": "700",
                    },
                },
            },
            {
                "type": "ia.display.label",
                "meta": {"name": "Subtitle"},
                "props": {
                    "text": (
                        "EPMS · Utility · Production rollup. Trends use placeholder sparklines "
                        "until historian is connected; time range is ready for tag history."
                    ),
                    "style": {"classes": "font-label"},
                },
            },
        ],
    }

    epms = overview_card(
        "CardEPMS",
        "Energy (EPMS)",
        epms_left,
        kpi_embed_inline(
            "EpmsSpark", "kWh trend", "EPMS", "kWh", root_tag + "/EPMS/kWh"
        ),
    )
    epms["props"]["style"]["gridColumn"] = "1"
    epms["props"]["style"]["gridRow"] = "2"

    util = overview_card(
        "CardUtility",
        "Utilities",
        util_left,
        kpi_embed_inline(
            "UtilSpark",
            "Outdoor temp",
            "Utility",
            "°F",
            root_tag + "/Utility/AmbientAvgF",
        ),
    )
    util["props"]["style"]["gridColumn"] = "2"
    util["props"]["style"]["gridRow"] = "2"

    prod = overview_card(
        "CardProduction",
        "Production",
        prod_left,
        kpi_embed_inline(
            "ProdSpark",
            "Volume trend",
            "Production",
            "lb",
            root_tag + "/Production/ProdVol",
        ),
    )
    prod["props"]["style"]["gridColumn"] = "1 / -1"
    prod["props"]["style"]["gridRow"] = "3"
    prod["props"]["style"]["minHeight"] = "260px"

    return {
        "custom": {},
        "params": {"plantName": "Groveport"},
        "propConfig": {
            "params.plantName": {"paramDirection": "input", "persistent": True},
        },
        "props": {"defaultSize": {"height": 900, "width": 1400}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {"direction": "column", "style": grid_style},
            "children": [title_block, epms, util, prod],
        },
    }


def area_tag_expr(area_default, domain, leaf):
    return (
        "'[default]KPI/Groveport/' + coalesce({view.params.area}, '%s') + '/%s/%s'"
        % (area_default, domain, leaf)
    )


def densify_domain(domain, area_default, metrics):
    """Overview-style hero card + KPI spark grid for a Groveport domain page."""
    primary = metrics[0]

    left = [
        {
            "type": "ia.container.flex",
            "meta": {"name": "Hero"},
            "props": {"direction": "column", "style": {"gap": "2px"}},
            "children": [
                {
                    "type": "ia.display.label",
                    "meta": {"name": "HL"},
                    "props": {
                        "text": primary["title"],
                        "style": {
                            "classes": "font-label",
                            "fontSize": "11px",
                            "textTransform": "uppercase",
                        },
                    },
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "HV"},
                    "props": {
                        "direction": "row",
                        "alignItems": "baseline",
                        "style": {"gap": "8px"},
                    },
                    "children": [
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Val"},
                            "props": {
                                "text": "—",
                                "style": {
                                    "classes": "font-livedata-entry kpi-value",
                                    "fontSize": "2rem",
                                },
                            },
                            "propConfig": {
                                "props.text": live_tag_binding(
                                    area_tag_expr(area_default, domain, primary["leaf"])
                                ),
                            },
                        },
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "U"},
                            "props": {
                                "text": primary["unit"],
                                "style": {"classes": "font-label"},
                            },
                        },
                    ],
                },
            ],
        }
    ]
    for m in metrics[1:]:
        left.append(
            metric_pen_row(
                m["name"],
                m["title"],
                m["unit"],
                area_tag_expr(area_default, domain, m["leaf"]),
            )
        )

    spark_path_expr = area_tag_expr(area_default, domain, primary["leaf"])

    spark = {
        "type": "ia.display.view",
        "meta": {"name": "PrimarySpark"},
        "position": {"grow": 1},
        "props": {
            "path": "02_Components/02_Widgets/KPI",
            "params": {
                "title": primary["title"] + " trend",
                "category": domain,
                "unit": primary["unit"],
                "tagPath": "",
                "value": "0",
            },
            "style": {"height": "100%", "minHeight": "240px", "width": "100%"},
        },
        "propConfig": {
            "props.params.tagPath": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": spark_path_expr},
                    "overlays": OVERLAYS,
                }
            }
        },
    }

    card = overview_card("DomainCard", "%s — %s" % (domain, area_default), left, spark)
    # Bind card title to area
    card["children"][0]["children"][0]["propConfig"] = {
        "props.text": {
            "binding": {
                "type": "expr",
                "config": {
                    "expression": (
                        "'%s — ' + coalesce({view.params.area}, '%s')"
                        % (domain, area_default)
                    )
                },
            }
        }
    }

    secondary = []
    for m in metrics:
        expr = (
            "'[default]KPI/Groveport/' + coalesce({view.params.area}, '%s') + '/%s/%s'"
            % (area_default, domain, m["leaf"])
        )
        secondary.append(
            {
                "type": "ia.display.view",
                "meta": {"name": m["name"]},
                "position": {"basis": "300px", "grow": 1, "shrink": 1},
                "props": {
                    "path": "02_Components/02_Widgets/KPI",
                    "params": {
                        "title": m["title"],
                        "category": domain,
                        "unit": m["unit"],
                        "tagPath": "",
                        "value": "0",
                    },
                    "style": {
                        "height": "auto",
                        "maxWidth": "420px",
                        "minHeight": "240px",
                        "minWidth": "280px",
                        "width": "100%",
                    },
                },
                "propConfig": {
                    "props.params.tagPath": {
                        "binding": {
                            "type": "expr",
                            "config": {"expression": expr},
                            "overlays": OVERLAYS,
                        }
                    }
                },
            }
        )

    return {
        "custom": {},
        "params": {"area": area_default},
        "propConfig": {
            "params.area": {"paramDirection": "input", "persistent": True},
        },
        "props": {"defaultSize": {"height": 720, "width": 1200}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "kpi-dashboard-page",
                    "gap": "16px",
                    "height": "100%",
                    "overflowY": "auto",
                    "padding": "4px",
                    "width": "100%",
                },
            },
            "children": [
                {
                    **card,
                    "position": {"shrink": 0},
                    "props": {
                        **card["props"],
                        "style": {
                            **card["props"]["style"],
                            "minHeight": "320px",
                        },
                    },
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "MetricGrid"},
                    "position": {"grow": 1},
                    "props": {
                        "direction": "row",
                        "wrap": "wrap",
                        "alignContent": "flex-start",
                        "style": {
                            "classes": "kpi-dashboard-grid",
                            "gap": "16px",
                            "width": "100%",
                        },
                    },
                    "children": secondary,
                },
            ],
        },
    }


CSS_EXTRA = """
/* Lightspeed-inspired site picker + overview cards */
.psc-site-card {
	transition: box-shadow 120ms ease, border-color 120ms ease;
}
.psc-site-card:hover {
	border-color: var(--callToAction, #0C7BB3);
	box-shadow: var(--boxShadow2, 0 4px 14px rgba(0,0,0,0.18));
}
.psc-overview-card {
	box-sizing: border-box;
	min-width: 0;
}
"""


def ensure_css():
    with open(STYLESHEET, encoding="utf-8") as f:
        css = f.read()
    marker = "/* Lightspeed-inspired site picker + overview cards */"
    if marker in css:
        start = css.index(marker)
        css = css[:start].rstrip() + "\n\n" + CSS_EXTRA.lstrip("\n")
    else:
        css = css.rstrip() + "\n\n" + CSS_EXTRA.lstrip("\n")
    with open(STYLESHEET, "w", encoding="utf-8", newline="\n") as f:
        f.write(css if css.endswith("\n") else css + "\n")
    print("updated stylesheet.css")


def main():
    sc_dir = os.path.join(VIEWS, "02_Components", "02_Widgets", "SiteCard")
    write_json(os.path.join(sc_dir, "view.json"), build_site_card())
    write_json(os.path.join(sc_dir, "resource.json"), resource_stub())

    patch_globe()

    ov = os.path.join(VIEWS, "00_Pages", "Groveport", "Site", "Overview")
    write_json(os.path.join(ov, "view.json"), build_groveport_overview())

    epms = densify_domain(
        "EPMS",
        "Freezer",
        [
            {"name": "kWh", "title": "kWh (MTD)", "unit": "kWh", "leaf": "kWh"},
            {"name": "Kvar", "title": "Reactive", "unit": "kvar", "leaf": "Kvar"},
            {"name": "Avg3", "title": "3yr Month Avg", "unit": "kWh", "leaf": "Avg3Yr"},
            {"name": "Avg7", "title": "7yr Month Avg", "unit": "kWh", "leaf": "Avg7Yr"},
        ],
    )
    utility = densify_domain(
        "Utility",
        "Freezer",
        [
            {"name": "Therm", "title": "Natural Gas", "unit": "therm", "leaf": "Therm"},
            {"name": "H2O", "title": "Water", "unit": "H2O", "leaf": "H2O"},
            {"name": "CO2", "title": "CO₂", "unit": "lb", "leaf": "CO2"},
            {
                "name": "AmbAvg",
                "title": "Outdoor Temp (avg)",
                "unit": "°F",
                "leaf": "AmbientAvgF",
            },
            {
                "name": "AmbMax",
                "title": "Outdoor Temp (max)",
                "unit": "°F",
                "leaf": "AmbientMaxF",
            },
        ],
    )
    production = densify_domain(
        "Production",
        "Freezer",
        [
            {
                "name": "ProdVol",
                "title": "Production Volume",
                "unit": "lb",
                "leaf": "ProdVol",
            },
            {
                "name": "Avg7d",
                "title": "7d Avg Volume",
                "unit": "lb",
                "leaf": "ProdVolAvg7d",
            },
            {
                "name": "Intensity",
                "title": "kWh / lb",
                "unit": "kWh/lb",
                "leaf": "kWhPerLb",
            },
        ],
    )

    for name, obj in (
        ("EPMS", epms),
        ("Utility", utility),
        ("Production", production),
    ):
        d = os.path.join(VIEWS, "00_Pages", "Groveport", "Domains", name)
        write_json(os.path.join(d, "view.json"), obj)

    # Area dashboard subtitle tweak
    ad_path = os.path.join(
        VIEWS, "00_Pages", "Groveport", "Area", "Dashboard", "view.json"
    )
    with open(ad_path, encoding="utf-8") as f:
        ad = json.load(f)
    for ch in ad["root"]["children"]:
        if ch.get("meta", {}).get("name") == "Subtitle":
            ch["props"]["text"] = (
                "Area domain overview — hero metrics, gauges, and trend cards "
                "(Lightspeed-style composition)."
            )
    write_json(ad_path, ad)

    ensure_css()
    print("done")


if __name__ == "__main__":
    main()
