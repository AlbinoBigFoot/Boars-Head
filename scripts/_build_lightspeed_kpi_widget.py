# -*- coding: utf-8 -*-
"""Build Lightspeed-inspired KPI widget + rebuild Groveport dashboards to use it."""
from __future__ import print_function

import json
import os

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

OVERLAYS_OFF = {
    "bad": False,
    "error": False,
    "pending": False,
    "stale": False,
    "unknown": False,
    "disabled": False,
}

SPARK_SCRIPT = r"""
	# Placeholder sparkline until KPI tags have historian.
	# Deterministic wave around live value so cards look like Lightspeed KPI chrome.
	import math
	import time

	try:
		base = float(value)
	except:
		base = 0.0

	now_ms = int(time.time() * 1000)
	hour_ms = 3600 * 1000
	points = []
	vals = []
	for i in range(24):
		t = now_ms - (23 - i) * hour_ms
		wave = 0.08 * math.sin(i * 0.55) + 0.03 * math.sin(i * 1.7)
		if abs(base) < 1e-9:
			v = 10.0 + 2.0 * math.sin(i * 0.4)
		else:
			v = base * (1.0 + wave)
		v = round(v, 3)
		points.append([t, v])
		vals.append(v)

	mn = min(vals) if vals else 0.0
	mx = max(vals) if vals else 0.0
	avg = (sum(vals) / float(len(vals))) if vals else 0.0
	return {
		'series': [{'name': 'value', 'data': points, 'color': '#0C7BB3'}],
		'min': mn,
		'max': mx,
		'avg': avg,
	}
""".lstrip("\n")

LIVE_NUM_EXPR = (
    "if(len(trim(coalesce({view.params.tagPath}, ''))) > 0, "
    "coalesce(try(if(isBadOrError(tag({view.params.tagPath})), null, "
    "tag({view.params.tagPath})), null), 0), "
    "coalesce(try(toFloat({view.params.value}), null), 0))"
)

LIVE_TEXT_EXPR = (
    "numberFormat("
    "if(len(trim(coalesce({view.params.tagPath}, ''))) > 0, "
    "coalesce(try(if(isBadOrError(tag({view.params.tagPath})), null, "
    "tag({view.params.tagPath})), null), 0), "
    "coalesce(try(toFloat({view.params.value}), null), 0))"
    ", '#,##0.#')"
)


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
                "timestamp": "2026-08-20T18:30:00Z",
            },
        },
    }


def metric_col(name, label, spark_key):
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 1, "basis": "0%"},
        "props": {
            "direction": "column",
            "alignItems": "flex-start",
            "style": {"gap": "2px", "minWidth": "0"},
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": label + "Lbl"},
                "props": {
                    "text": label,
                    "style": {
                        "classes": "font-label",
                        "letterSpacing": "0.04em",
                        "textTransform": "uppercase",
                        "opacity": "0.75",
                    },
                },
            },
            {
                "type": "ia.display.label",
                "meta": {"name": label + "Val"},
                "props": {
                    "text": "—",
                    "style": {"classes": "font-livedata-entry", "fontSize": "0.95rem"},
                },
                "propConfig": {
                    "props.text": {
                        "binding": {
                            "type": "expr",
                            "config": {
                                "expression": (
                                    "numberFormat(coalesce({view.custom.spark.%s}, 0), '#,##0.#')"
                                    % spark_key
                                )
                            },
                            "overlays": OVERLAYS_OFF,
                        }
                    }
                },
            },
        ],
    }


def build_kpi_view():
    return {
        "custom": {
            "spark": {
                "series": [],
                "min": 0,
                "max": 0,
                "avg": 0,
            }
        },
        "params": {
            "title": "KPI",
            "category": "",
            "unit": "",
            "tagPath": "",
            "value": "0",
        },
        "propConfig": {
            "params.title": {"paramDirection": "input", "persistent": True},
            "params.category": {"paramDirection": "input", "persistent": True},
            "params.unit": {"paramDirection": "input", "persistent": True},
            "params.tagPath": {"paramDirection": "input", "persistent": True},
            "params.value": {"paramDirection": "input", "persistent": True},
            "custom.spark": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": LIVE_NUM_EXPR},
                    "transforms": [{"type": "script", "code": SPARK_SCRIPT}],
                    "overlays": OVERLAYS_OFF,
                },
                "persistent": True,
            },
        },
        "props": {"defaultSize": {"height": 260, "width": 360}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": (
                        "container-card container-card-border plant-feature-card kpi-card"
                    ),
                    "boxSizing": "border-box",
                    "gap": "8px",
                    "height": "100%",
                    "minHeight": "240px",
                    "overflow": "hidden",
                    "padding": "12px 14px",
                    "width": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Header"},
                    "position": {"shrink": 0},
                    "props": {
                        "direction": "column",
                        "style": {"classes": "kpi-card-header", "gap": "2px", "width": "100%"},
                    },
                    "children": [
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Category"},
                            "props": {
                                "text": "",
                                "style": {
                                    "classes": "font-label",
                                    "letterSpacing": "0.04em",
                                    "textTransform": "uppercase",
                                },
                            },
                            "propConfig": {
                                "props.text": {
                                    "binding": {
                                        "type": "property",
                                        "config": {"path": "view.params.category"},
                                    }
                                },
                                "meta.visible": {
                                    "binding": {
                                        "type": "expr",
                                        "config": {
                                            "expression": (
                                                "len(coalesce({view.params.category}, '')) > 0"
                                            )
                                        },
                                    }
                                },
                            },
                        },
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Title"},
                            "props": {
                                "text": "KPI",
                                "style": {"classes": "font-title plant-feature-title"},
                            },
                            "propConfig": {
                                "props.text": {
                                    "binding": {
                                        "type": "property",
                                        "config": {"path": "view.params.title"},
                                    }
                                }
                            },
                        },
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "ValueRow"},
                    "position": {"shrink": 0},
                    "props": {
                        "direction": "row",
                        "alignItems": "baseline",
                        "style": {"gap": "8px", "width": "100%"},
                    },
                    "children": [
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Value"},
                            "position": {"shrink": 0},
                            "props": {
                                "text": "—",
                                "style": {
                                    "classes": "font-livedata-entry kpi-value",
                                    "fontSize": "1.85rem",
                                    "lineHeight": "1.1",
                                },
                            },
                            "propConfig": {
                                "props.text": {
                                    "binding": {
                                        "type": "expr",
                                        "config": {"expression": LIVE_TEXT_EXPR},
                                        "overlays": OVERLAYS_OFF,
                                    }
                                }
                            },
                        },
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Unit"},
                            "position": {"shrink": 0},
                            "props": {
                                "text": "",
                                "style": {"classes": "font-label", "fontSize": "0.95rem"},
                            },
                            "propConfig": {
                                "props.text": {
                                    "binding": {
                                        "type": "property",
                                        "config": {"path": "view.params.unit"},
                                    }
                                },
                                "meta.visible": {
                                    "binding": {
                                        "type": "expr",
                                        "config": {
                                            "expression": (
                                                "len(coalesce({view.params.unit}, '')) > 0"
                                            )
                                        },
                                    }
                                },
                            },
                        },
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "ChartWrap"},
                    "position": {"grow": 1, "basis": "120px"},
                    "props": {
                        "direction": "column",
                        "style": {
                            "classes": "kpi-chart",
                            "minHeight": "120px",
                            "overflow": "hidden",
                            "width": "100%",
                        },
                    },
                    "children": [
                        {
                            "type": "kyvislabs.display.apexchart",
                            "meta": {"name": "Spark"},
                            "position": {"grow": 1},
                            "props": {
                                "type": "line",
                                "series": [],
                                "options": {
                                    "chart": {
                                        "animations": {"enabled": False},
                                        "background": "transparent",
                                        "fontFamily": "sans-serif",
                                        "height": 140,
                                        "sparkline": {"enabled": True},
                                        "toolbar": {"show": False},
                                        "type": "line",
                                        "zoom": {"enabled": False},
                                    },
                                    "colors": ["#0C7BB3"],
                                    "dataLabels": {"enabled": False},
                                    "fill": {
                                        "opacity": 0.15,
                                        "type": "solid",
                                    },
                                    "grid": {"show": False},
                                    "legend": {"show": False},
                                    "markers": {"size": 0},
                                    "stroke": {"curve": "stepline", "width": 2},
                                    "tooltip": {
                                        "enabled": True,
                                        "theme": "dark",
                                        "x": {
                                            "format": "MMM dd HH:mm",
                                            "show": True,
                                        },
                                    },
                                    "xaxis": {
                                        "labels": {"show": False},
                                        "type": "datetime",
                                    },
                                    "yaxis": {"labels": {"show": False}, "show": False},
                                },
                                "style": {
                                    "height": "100%",
                                    "minHeight": "120px",
                                    "overflow": "hidden",
                                    "width": "100%",
                                },
                            },
                            "propConfig": {
                                "props.series": {
                                    "binding": {
                                        "type": "property",
                                        "config": {"path": "view.custom.spark.series"},
                                        "overlays": OVERLAYS_OFF,
                                    }
                                }
                            },
                        }
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Metrics"},
                    "position": {"shrink": 0},
                    "props": {
                        "direction": "row",
                        "justify": "space-between",
                        "style": {
                            "classes": "kpi-metrics",
                            "gap": "12px",
                            "paddingTop": "8px",
                            "width": "100%",
                        },
                    },
                    "children": [
                        metric_col("MinCol", "Min", "min"),
                        metric_col("MaxCol", "Max", "max"),
                        metric_col("AvgCol", "Avg", "avg"),
                    ],
                },
            ],
        },
    }


def kpi_embed(name, title, category, unit, tag_path_expr=None, tag_path_literal=None):
    """Embed of 02_Components/02_Widgets/KPI with optional tagPath binding."""
    params = {
        "title": title,
        "category": category,
        "unit": unit,
        "tagPath": tag_path_literal or "",
        "value": "0",
    }
    node = {
        "type": "ia.display.view",
        "meta": {"name": name},
        "position": {"basis": "320px", "grow": 1, "shrink": 1},
        "props": {
            "path": "02_Components/02_Widgets/KPI",
            "params": params,
            "style": {
                "height": "260px",
                "maxWidth": "420px",
                "minHeight": "240px",
                "minWidth": "280px",
                "overflow": "hidden",
                "width": "100%",
            },
        },
    }
    if tag_path_expr:
        node["propConfig"] = {
            "props.params.tagPath": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": tag_path_expr},
                    "overlays": OVERLAYS_OFF,
                }
            }
        }
    return node


def domain_page(area_default, cards):
    """cards: list of (name, title, category, unit, leaf_under_domain) where domain folder in tag."""
    children = []
    for name, title, category, unit, leaf in cards:
        # leaf is like 'EPMS/kWh' relative under Groveport/{area}/
        expr = (
            "'[default]KPI/Groveport/' + coalesce({view.params.area}, '%s') + '/%s'"
            % (area_default, leaf)
        )
        children.append(kpi_embed(name, title, category, unit, tag_path_expr=expr))
    return {
        "custom": {},
        "params": {"area": area_default},
        "propConfig": {
            "params.area": {"paramDirection": "input", "persistent": True},
        },
        "props": {"defaultSize": {"height": 560, "width": 1200}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "row",
                "wrap": "wrap",
                "alignContent": "flex-start",
                "style": {
                    "classes": "kpi-dashboard-grid",
                    "gap": "16px",
                    "height": "100%",
                    "overflowY": "auto",
                    "padding": "4px",
                    "width": "100%",
                },
            },
            "children": children,
        },
    }


def site_overview():
    site_cards = [
        ("kWh", "Site kWh (MTD)", "EPMS", "kWh", "Site/EPMS/kWh"),
        ("Kvar", "Reactive", "EPMS", "kvar", "Site/EPMS/Kvar"),
        ("Therm", "Natural Gas", "Utility", "therm", "Site/Utility/Therm"),
        ("H2O", "Water", "Utility", "H2O", "Site/Utility/H2O"),
        ("Prod", "Production Volume", "Production", "lb", "Site/Production/ProdVol"),
        ("Temp", "Outdoor Temp (avg)", "Utility", "°F", "Site/Utility/AmbientAvgF"),
    ]
    children = []
    for name, title, category, unit, leaf in site_cards:
        literal = "[default]KPI/Groveport/%s" % leaf
        children.append(
            kpi_embed(name, title, category, unit, tag_path_literal=literal)
        )
    return {
        "custom": {},
        "params": {"plantName": "Groveport"},
        "propConfig": {
            "params.plantName": {"paramDirection": "input", "persistent": True},
        },
        "props": {"defaultSize": {"height": 800, "width": 1400}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "bg-page kpi-dashboard-page",
                    "gap": "16px",
                    "height": "100%",
                    "overflowY": "auto",
                    "padding": "20px 24px",
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
                            "Site KPI rollup — live value, sparkline, Min / Max / Avg "
                            "(placeholder history until historian)."
                        ),
                        "style": {"classes": "font-label"},
                    },
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Cards"},
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
                    "children": children,
                },
            ],
        },
    }


def area_dashboard():
    return {
        "custom": {},
        "params": {
            "site": "Groveport",
            "area": "Freezer",
            "domain": "Utility",
        },
        "propConfig": {
            "params.site": {"paramDirection": "input", "persistent": True},
            "params.area": {"paramDirection": "input", "persistent": True},
            "params.domain": {"paramDirection": "input", "persistent": True},
        },
        "props": {"defaultSize": {"height": 800, "width": 1400}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "bg-page kpi-dashboard-page",
                    "gap": "16px",
                    "height": "100%",
                    "overflow": "hidden",
                    "padding": "20px 24px",
                    "width": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.display.label",
                    "meta": {"name": "Title"},
                    "position": {"shrink": 0},
                    "props": {
                        "text": "Groveport KPI",
                        "style": {
                            "classes": "font-title",
                            "fontSize": "22px",
                            "fontWeight": "700",
                        },
                    },
                    "propConfig": {
                        "props.text": {
                            "binding": {
                                "type": "expr",
                                "config": {
                                    "expression": (
                                        "coalesce({view.params.site}, 'Groveport') + ' — ' + "
                                        "coalesce({view.params.area}, '') + ' — ' + "
                                        "coalesce({view.params.domain}, '')"
                                    )
                                },
                            }
                        }
                    },
                },
                {
                    "type": "ia.display.label",
                    "meta": {"name": "Subtitle"},
                    "position": {"shrink": 0},
                    "props": {
                        "text": (
                            "Area domain KPIs — Lightspeed-style cards with sparkline "
                            "and Min / Max / Avg."
                        ),
                        "style": {"classes": "font-label"},
                    },
                },
                {
                    "type": "ia.display.view",
                    "meta": {"name": "DomainBody"},
                    "position": {"grow": 1},
                    "props": {
                        "path": "00_Pages/Groveport/Domains/Utility",
                        "params": {"area": "Freezer"},
                        "style": {"height": "100%", "width": "100%"},
                    },
                    "propConfig": {
                        "props.path": {
                            "binding": {
                                "type": "expr",
                                "config": {
                                    "expression": (
                                        "case(lower(coalesce({view.params.domain}, 'utility')), "
                                        "'epms', '00_Pages/Groveport/Domains/EPMS', "
                                        "'utility', '00_Pages/Groveport/Domains/Utility', "
                                        "'production', '00_Pages/Groveport/Domains/Production', "
                                        "'00_Pages/Groveport/Domains/Utility')"
                                    )
                                },
                            }
                        },
                        "props.params.area": {
                            "binding": {
                                "type": "property",
                                "config": {"path": "view.params.area"},
                            }
                        },
                    },
                },
            ],
        },
    }


KPI_CSS = """
/* Groveport / Lightspeed-inspired KPI dashboard */
.psc-kpi-card {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  min-height: 240px;
  overflow: hidden;
}
.psc-kpi-card-header {
  width: 100%;
}
.psc-kpi-value {
  font-variant-numeric: tabular-nums;
}
.psc-kpi-chart {
  flex: 1 1 auto;
  min-height: 120px;
  width: 100%;
}
.psc-kpi-metrics {
  display: flex;
  width: 100%;
  gap: 12px;
  padding-top: 8px;
  border-top: 1px solid color-mix(in srgb, var(--neutral-50, #888) 35%, transparent);
}
.psc-kpi-dashboard-grid {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  align-items: stretch;
  gap: 16px;
  width: 100%;
}
.psc-kpi-dashboard-page {
  padding: 20px 24px;
  box-sizing: border-box;
}
"""


def ensure_css():
    with open(STYLESHEET, "r", encoding="utf-8") as f:
        css = f.read()
    marker = "/* Groveport / Lightspeed-inspired KPI dashboard */"
    if marker in css:
        # replace from marker to EOF or next major section — append once only
        start = css.index(marker)
        # drop old block if present through end of our classes
        end_marker = ".psc-kpi-dashboard-page {"
        if end_marker in css[start:]:
            # find closing brace of that rule
            sub = css[start:]
            # keep everything before marker, append fresh
            css = css[:start].rstrip() + "\n\n" + KPI_CSS.lstrip("\n")
        else:
            css = css[:start].rstrip() + "\n\n" + KPI_CSS.lstrip("\n")
    else:
        css = css.rstrip() + "\n\n" + KPI_CSS.lstrip("\n")
    with open(STYLESHEET, "w", encoding="utf-8", newline="\n") as f:
        f.write(css if css.endswith("\n") else css + "\n")
    print("updated stylesheet.css")


def main():
    kpi_dir = os.path.join(VIEWS, "02_Components", "02_Widgets", "KPI")
    write_json(os.path.join(kpi_dir, "view.json"), build_kpi_view())
    write_json(os.path.join(kpi_dir, "resource.json"), resource_stub())

    epms = domain_page(
        "Freezer",
        [
            ("kWh", "kWh (MTD)", "EPMS", "kWh", "EPMS/kWh"),
            ("Kvar", "Reactive", "EPMS", "kvar", "EPMS/Kvar"),
            ("Avg3", "3yr Month Avg", "EPMS", "kWh", "EPMS/Avg3Yr"),
            ("Avg7", "7yr Month Avg", "EPMS", "kWh", "EPMS/Avg7Yr"),
        ],
    )
    utility = domain_page(
        "Freezer",
        [
            ("Therm", "Natural Gas", "Utility", "therm", "Utility/Therm"),
            ("H2O", "Water", "Utility", "H2O", "Utility/H2O"),
            ("CO2", "CO2", "Utility", "lb", "Utility/CO2"),
            ("Ambient", "Outdoor Temp (avg)", "Utility", "°F", "Utility/AmbientAvgF"),
        ],
    )
    production = domain_page(
        "Freezer",
        [
            ("ProdVol", "Production Volume", "Production", "lb", "Production/ProdVol"),
            ("Avg7d", "7d Avg Volume", "Production", "lb", "Production/ProdVolAvg7d"),
            ("Intensity", "kWh / lb", "Production", "kWh/lb", "Production/kWhPerLb"),
        ],
    )

    # If Production tags differ, keep what seed script created — check leaves
    write_json(
        os.path.join(VIEWS, "00_Pages", "Groveport", "Domains", "EPMS", "view.json"),
        epms,
    )
    write_json(
        os.path.join(VIEWS, "00_Pages", "Groveport", "Domains", "Utility", "view.json"),
        utility,
    )
    write_json(
        os.path.join(
            VIEWS, "00_Pages", "Groveport", "Domains", "Production", "view.json"
        ),
        production,
    )
    write_json(
        os.path.join(VIEWS, "00_Pages", "Groveport", "Site", "Overview", "view.json"),
        site_overview(),
    )
    write_json(
        os.path.join(VIEWS, "00_Pages", "Groveport", "Area", "Dashboard", "view.json"),
        area_dashboard(),
    )

    for rel in (
        "00_Pages/Groveport/Domains/EPMS",
        "00_Pages/Groveport/Domains/Utility",
        "00_Pages/Groveport/Domains/Production",
        "00_Pages/Groveport/Site/Overview",
        "00_Pages/Groveport/Area/Dashboard",
    ):
        rpath = os.path.join(VIEWS, *rel.split("/"), "resource.json")
        if not os.path.isfile(rpath):
            write_json(rpath, resource_stub())

    ensure_css()
    print("done — run repair-resource-signatures.py next")


if __name__ == "__main__":
    main()
