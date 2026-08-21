# -*- coding: utf-8 -*-
"""Build KPI widget + Groveport/Globe pages (Lightspeed card density)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEWS = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective/views"
)
ZERO_SIG = "0" * 64
OVERLAYS_OFF = {
    "bad": False,
    "error": False,
    "pending": False,
    "stale": False,
    "unknown": False,
    "disabled": False,
}

SPARK_SCRIPT = (
    "\t# Placeholder sparkline until historian: ~24 hourly points around live value.\n"
    "\traw = value\n"
    "\ttry:\n"
    "\t\tbase = float(raw)\n"
    "\texcept:\n"
    "\t\ttry:\n"
    "\t\t\ts = str(raw or '0').replace(',', '').replace(u'\\u2014', '').strip()\n"
    "\t\t\tbase = float(s) if s else 0.0\n"
    "\t\texcept:\n"
    "\t\t\tbase = 0.0\n"
    "\tnow = int(system.date.toMillis(system.date.now()))\n"
    "\thour_ms = 3600 * 1000\n"
    "\tseed = abs(hash(str(round(base, 3)))) % 10007\n"
    "\tdata = []\n"
    "\tvals = []\n"
    "\tfor i in range(24):\n"
    "\t\t# Deterministic wobble ~+/-8% so refresh does not scramble the series.\n"
    "\t\tphase = ((seed + i * 37) % 100) / 100.0\n"
    "\t\twobble = 0.92 + 0.16 * phase\n"
    "\t\tif abs(base) < 1e-9:\n"
    "\t\t\tv = float((seed + i * 13) % 50) / 10.0\n"
    "\t\telse:\n"
    "\t\t\tv = base * wobble\n"
    "\t\tts = now - (23 - i) * hour_ms\n"
    "\t\tdata.append([ts, round(v, 2)])\n"
    "\t\tvals.append(v)\n"
    "\tmn = min(vals) if vals else 0.0\n"
    "\tmx = max(vals) if vals else 0.0\n"
    "\tavg = (sum(vals) / float(len(vals))) if vals else 0.0\n"
    "\tdef fmt(n):\n"
    "\t\ttry:\n"
    "\t\t\treturn '{:,.1f}'.format(float(n))\n"
    "\t\texcept:\n"
    "\t\t\treturn u'\\u2014'\n"
    "\treturn {\n"
    "\t\t'series': [{'name': 'Trend', 'data': data}],\n"
    "\t\t'min': fmt(mn),\n"
    "\t\t'max': fmt(mx),\n"
    "\t\t'avg': fmt(avg),\n"
    "\t}\n"
)

def resource_json() -> dict:
    return {
        "scope": "G",
        "version": 1,
        "restricted": False,
        "overridable": True,
        "files": ["view.json"],
        "attributes": {
            "lastModificationSignature": ZERO_SIG,
            "lastModification": {
                "actor": "external",
                "timestamp": "2026-08-20T18:20:00Z",
            },
        },
    }


def write_view(rel: str, view: dict) -> Path:
    folder = VIEWS / rel
    folder.mkdir(parents=True, exist_ok=True)
    view_path = folder / "view.json"
    view_path.write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8")
    (folder / "resource.json").write_text(
        json.dumps(resource_json(), indent=2) + "\n", encoding="utf-8"
    )
    return folder / "resource.json"


def kpi_widget() -> dict:
    live_numeric_expr = (
        "if(len(coalesce({view.params.tagPath}, '')) > 0, "
        "coalesce(try(if(isBadOrError(tag({view.params.tagPath})), null, "
        "tag({view.params.tagPath})), null), 0), "
        "try(toFloat(replace(coalesce({view.params.value}, '0'), ',', '')), 0))"
    )
    live_display_expr = (
        "if(len(coalesce({view.params.tagPath}, '')) > 0, "
        "numberFormat(coalesce(try(if(isBadOrError(tag({view.params.tagPath})), null, "
        "tag({view.params.tagPath})), null), 0), '#,##0.#'), "
        "coalesce({view.params.value}, '\u2014'))"
    )

    return {
        "custom": {
            "liveNumeric": 0,
            "spark": {
                "series": [],
                "min": "\u2014",
                "max": "\u2014",
                "avg": "\u2014",
            },
        },
        "params": {
            "title": "Metric",
            "category": "",
            "unit": "",
            "tagPath": "",
            "value": "\u2014",
        },
        "propConfig": {
            "params.title": {"paramDirection": "input", "persistent": True},
            "params.category": {"paramDirection": "input", "persistent": True},
            "params.unit": {"paramDirection": "input", "persistent": True},
            "params.tagPath": {"paramDirection": "input", "persistent": True},
            "params.value": {"paramDirection": "input", "persistent": True},
            "custom.liveNumeric": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": live_numeric_expr},
                    "overlays": OVERLAYS_OFF,
                }
            },
            "custom.spark": {
                "binding": {
                    "type": "property",
                    "config": {"path": "view.custom.liveNumeric"},
                    "transforms": [{"type": "script", "code": SPARK_SCRIPT}],
                }
            },
        },
        "props": {"defaultSize": {"height": 280, "width": 320}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "justify": "flex-start",
                "style": {
                    "classes": "container-card container-card-border kpi-card",
                    "boxSizing": "border-box",
                    "gap": "8px",
                    "height": "100%",
                    "minHeight": "240px",
                    "overflow": "hidden",
                    "padding": "12px 16px",
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
                            "position": {"shrink": 0},
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
                                            "expression": "len(coalesce({view.params.category}, '')) > 0"
                                        },
                                    }
                                },
                            },
                        },
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Title"},
                            "position": {"shrink": 0},
                            "props": {
                                "text": "Metric",
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
                        "justify": "flex-start",
                        "style": {"gap": "8px", "width": "100%"},
                    },
                    "children": [
                        {
                            "type": "ia.display.label",
                            "meta": {"name": "Value"},
                            "position": {"shrink": 0},
                            "props": {
                                "text": "\u2014",
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
                                        "config": {"expression": live_display_expr},
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
                                            "expression": "len(coalesce({view.params.unit}, '')) > 0"
                                        },
                                    }
                                },
                            },
                        },
                    ],
                },
                {
                    "type": "kyvislabs.display.apexchart",
                    "meta": {"name": "Chart"},
                    "position": {"grow": 1, "shrink": 1, "basis": "140px"},
                    "props": {
                        "type": "line",
                        "series": [],
                        "options": {
                            "chart": {
                                "type": "line",
                                "height": 140,
                                "width": "100%",
                                "animations": {"enabled": False},
                                "toolbar": {"show": False},
                                "zoom": {"enabled": False},
                                "selection": {"enabled": False},
                                "redrawOnParentResize": True,
                                "redrawOnWindowResize": True,
                                "events": {
                                    "animationEnd": False,
                                    "beforeMount": False,
                                    "beforeResetZoom": False,
                                    "beforeZoom": False,
                                    "brushScrolled": False,
                                    "click": False,
                                    "dataPointMouseEnter": False,
                                    "dataPointMouseLeave": False,
                                    "dataPointSelection": False,
                                    "legendClick": False,
                                    "markerClick": False,
                                    "mounted": False,
                                    "mouseLeave": False,
                                    "mouseMove": False,
                                    "scrolled": False,
                                    "selection": False,
                                    "updated": False,
                                    "xAxisLabelClick": False,
                                    "zoomed": False,
                                },
                            },
                            "colors": ["#0C7BB3"],
                            "dataLabels": {"enabled": False},
                            "fill": {"opacity": 0.15, "type": "solid"},
                            "grid": {
                                "show": False,
                                "padding": {"top": 0, "right": 4, "bottom": 0, "left": 4},
                            },
                            "legend": {"show": False},
                            "markers": {"size": 0},
                            "stroke": {"curve": "stepline", "width": 2},
                            "tooltip": {
                                "enabled": True,
                                "x": {"format": "HH:mm", "show": True},
                            },
                            "xaxis": {
                                "type": "datetime",
                                "labels": {"show": False, "datetimeUTC": False},
                                "axisBorder": {"show": False},
                                "axisTicks": {"show": False},
                                "tooltip": {"enabled": False},
                            },
                            "yaxis": {
                                "labels": {"show": False},
                                "axisBorder": {"show": False},
                                "axisTicks": {"show": False},
                            },
                        },
                        "style": {
                            "classes": "kpi-chart",
                            "height": "140px",
                            "minHeight": "140px",
                            "overflow": "hidden",
                            "width": "100%",
                        },
                    },
                    "propConfig": {
                        "props.series": {
                            "binding": {
                                "type": "property",
                                "config": {"path": "view.custom.spark.series"},
                            }
                        }
                    },
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Metrics"},
                    "position": {"shrink": 0},
                    "props": {
                        "direction": "row",
                        "justify": "space-between",
                        "style": {"classes": "kpi-metrics", "gap": "12px", "width": "100%"},
                    },
                    "children": [
                        _metric_cell("Min", "view.custom.spark.min"),
                        _metric_cell("Max", "view.custom.spark.max"),
                        _metric_cell("Avg", "view.custom.spark.avg"),
                    ],
                },
            ],
        },
    }


def _metric_cell(label: str, path: str) -> dict:
    return {
        "type": "ia.container.flex",
        "meta": {"name": label},
        "position": {"grow": 1, "basis": "0px"},
        "props": {
            "direction": "column",
            "alignItems": "center",
            "style": {"gap": "2px", "minWidth": "0"},
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": f"{label}Label"},
                "props": {
                    "text": label,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "letterSpacing": "0.04em",
                        "textAlign": "center",
                        "textTransform": "uppercase",
                    },
                },
            },
            {
                "type": "ia.display.label",
                "meta": {"name": f"{label}Value"},
                "props": {
                    "text": "\u2014",
                    "style": {
                        "classes": "font-value",
                        "fontSize": "13px",
                        "fontWeight": "600",
                        "textAlign": "center",
                    },
                },
                "propConfig": {
                    "props.text": {
                        "binding": {"type": "property", "config": {"path": path}}
                    }
                },
            },
        ],
    }


def tag_path_expr(area_expr: str, domain: str, leaf: str) -> str:
    return f"'[default]KPI/Groveport/' + {area_expr} + '/{domain}/{leaf}'"


def kpi_embed(
    name: str,
    category: str,
    title: str,
    unit: str,
    *,
    tag_path: str | None = None,
    tag_path_expr: str | None = None,
    value: str = "\u2014",
) -> dict:
    params = {
        "category": category,
        "title": title,
        "unit": unit,
        "tagPath": tag_path or "",
        "value": value,
    }
    node = {
        "type": "ia.display.view",
        "meta": {"name": name},
        "position": {"basis": "300px", "grow": 1, "shrink": 1},
        "props": {
            "path": "02_Components/02_Widgets/KPI",
            "params": params,
            "style": {
                "height": "auto",
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


def domain_view(domain: str, cards: list[tuple[str, str, str, str]]) -> dict:
    children = [
        kpi_embed(
            name=n,
            category=domain,
            title=t,
            unit=u,
            tag_path_expr=tag_path_expr("{view.params.area}", domain, leaf),
        )
        for n, t, u, leaf in cards
    ]
    return {
        "custom": {},
        "params": {"area": "Freezer"},
        "propConfig": {"params.area": {"paramDirection": "input", "persistent": True}},
        "props": {"defaultSize": {"height": 560, "width": 1100}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "row",
                "wrap": "wrap",
                "alignContent": "flex-start",
                "style": {
                    "classes": "bg-page kpi-dashboard-grid",
                    "gap": "16px",
                    "height": "100%",
                    "minHeight": "0",
                    "overflowY": "auto",
                    "padding": "4px",
                    "width": "100%",
                },
            },
            "children": children,
        },
    }


def site_overview() -> dict:
    cards = [
        ("kWh", "EPMS", "Site kWh (MTD)", "kWh", "Site", "EPMS", "kWh"),
        ("Kvar", "EPMS", "Reactive", "kvar", "Site", "EPMS", "Kvar"),
        ("Therm", "Utility", "Natural Gas", "therm", "Site", "Utility", "Therm"),
        ("H2O", "Utility", "Water", "H2O", "Site", "Utility", "H2O"),
        ("Prod", "Production", "Production Volume", "lb", "Site", "Production", "ProdVol"),
        ("Temp", "Utility", "Outdoor Temp (avg)", "\u00b0F", "Site", "Utility", "AmbientAvgF"),
    ]
    children = [
        kpi_embed(
            name=name,
            category=cat,
            title=title,
            unit=unit,
            tag_path=f"[default]KPI/Groveport/{area}/{domain}/{leaf}",
        )
        for name, cat, title, unit, area, domain, leaf in cards
    ]
    return {
        "custom": {},
        "params": {"plantName": "Groveport"},
        "propConfig": {
            "params.plantName": {"paramDirection": "input", "persistent": True}
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
                        "text": "Groveport \u2014 Site KPI",
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
                        "text": "Site rollup placeholders (EPMS / Utility / Production).",
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


def area_dashboard() -> dict:
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
                                        "coalesce({view.params.site}, 'Groveport') + ' \u2014 ' + "
                                        "coalesce({view.params.area}, '') + ' \u2014 ' + "
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
                        "text": "Placeholder KPIs from Utility Tracker sample (memory tags).",
                        "style": {"classes": "font-label"},
                    },
                },
                {
                    "type": "ia.display.view",
                    "meta": {"name": "DomainBody"},
                    "position": {"grow": 1, "shrink": 1, "basis": "0px"},
                    "props": {
                        "path": "00_Pages/Groveport/Domains/Utility",
                        "params": {"area": "Freezer"},
                        "style": {
                            "height": "100%",
                            "minHeight": "0",
                            "overflow": "auto",
                            "width": "100%",
                        },
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


def patch_globe() -> Path:
    path = VIEWS / "00_Pages/LandingPage/Globe/view.json"
    view = json.loads(path.read_text(encoding="utf-8"))
    # Find KpiRail children and upgrade first 4 to KPI @ 240px; leave rest MetricCard.
    rail = None
    for child in view["root"]["children"]:
        if child.get("meta", {}).get("name") == "KpiRail":
            rail = child
            break
    if rail is None:
        raise RuntimeError("KpiRail not found on Globe")

    kpi_specs = [
        ("Card_kWh", "EPMS", "Site kWh (MTD)", "kWh", "595,200"),
        ("Card_Therm", "Utility", "Natural Gas", "therm", "\u2014"),
        ("Card_Water", "Utility", "Water Use", "H2O", "\u2014"),
        ("Card_Prod", "Production", "Production Volume", "lb", "130,031"),
    ]
    metric_specs = [
        ("Card_Demand", "EPMS", "Reactive (kvar)", "kvar", "444.5"),
        ("Card_Temp", "Utility", "Outdoor Temp (avg)", "\u00b0F", "42.0"),
    ]

    children = []
    for name, cat, title, unit, value in kpi_specs:
        children.append(
            {
                "type": "ia.display.view",
                "meta": {"name": name},
                "position": {"basis": "240px", "shrink": 0},
                "props": {
                    "path": "02_Components/02_Widgets/KPI",
                    "params": {
                        "category": cat,
                        "title": title,
                        "unit": unit,
                        "tagPath": "",
                        "value": value,
                    },
                    "style": {
                        "height": "240px",
                        "minHeight": "240px",
                        "minWidth": "280px",
                        "overflow": "hidden",
                        "width": "100%",
                    },
                },
            }
        )
    for name, cat, title, unit, value in metric_specs:
        children.append(
            {
                "type": "ia.display.view",
                "meta": {"name": name},
                "position": {"basis": "140px", "shrink": 0},
                "props": {
                    "path": "02_Components/02_Widgets/MetricCard",
                    "params": {
                        "category": cat,
                        "title": title,
                        "unit": unit,
                        "value": value,
                    },
                    "style": {
                        "height": "140px",
                        "minHeight": "140px",
                        "minWidth": "280px",
                        "overflow": "hidden",
                        "width": "100%",
                    },
                },
            }
        )
    rail["children"] = children
    path.write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8")
    return path.parent / "resource.json"


def main() -> None:
    resources: list[Path] = []
    resources.append(write_view("02_Components/02_Widgets/KPI", kpi_widget()))
    resources.append(
        write_view(
            "00_Pages/Groveport/Domains/EPMS",
            domain_view(
                "EPMS",
                [
                    ("kWh", "kWh (MTD)", "kWh", "kWh"),
                    ("Kvar", "Reactive", "kvar", "Kvar"),
                    ("Avg3", "3yr Month Avg", "kWh", "Avg3Yr"),
                    ("Avg7", "7yr Month Avg", "kWh", "Avg7Yr"),
                ],
            ),
        )
    )
    resources.append(
        write_view(
            "00_Pages/Groveport/Domains/Utility",
            domain_view(
                "Utility",
                [
                    ("Therm", "Natural Gas", "therm", "Therm"),
                    ("H2O", "Water", "H2O", "H2O"),
                    ("CO2", "CO\u2082", "tons", "CO2"),
                    ("AmbAvg", "Outdoor Temp (avg)", "\u00b0F", "AmbientAvgF"),
                    ("AmbMax", "Outdoor Temp (max)", "\u00b0F", "AmbientMaxF"),
                ],
            ),
        )
    )
    resources.append(
        write_view(
            "00_Pages/Groveport/Domains/Production",
            domain_view(
                "Production",
                [
                    ("ProdVol", "Production Volume", "lb", "ProdVol"),
                    ("ProdAvg", "7-day Avg Volume", "lb", "ProdVolAvg7d"),
                    ("Intensity", "kWh / lb", "kWh/lb", "kWhPerLb"),
                ],
            ),
        )
    )
    resources.append(write_view("00_Pages/Groveport/Site/Overview", site_overview()))
    resources.append(write_view("00_Pages/Groveport/Area/Dashboard", area_dashboard()))
    globe_rj = patch_globe()
    resources.append(globe_rj)

    # Touch Globe resource.json signature placeholder for repair
    if not globe_rj.exists():
        globe_rj.write_text(json.dumps(resource_json(), indent=2) + "\n", encoding="utf-8")

    print("Wrote:")
    for p in resources:
        print(" ", p.parent.relative_to(ROOT))


if __name__ == "__main__":
    main()
