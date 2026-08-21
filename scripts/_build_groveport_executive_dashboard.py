#!/usr/bin/env python3
"""Build Groveport Site Executive Overview from the utility-executive-dashboard canvas.

Keeps domain-tab UI available at OverviewClassic (/plants/groveport/classic).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERIES_PATH = ROOT / "docs/kpi/dashboard-series.json"
OVERVIEW = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
    / "views/00_Pages/Groveport/Site/Overview/view.json"
)
HORIZON = 12  # canvas default

# Canvas plant matrix (placeholder until multi-site tags exist)
SITES = [
    ("Cascade", "New York", "NY", "March", "298k", "5,400", "1,480k", "0.201", "620", "0.94", "Optimal"),
    ("Cascade", "Groveport", "OH", "October", "340k", "6,800", "1,520k", "0.224", "710", "0.89", "PF Alert"),
    ("Cascade", "Holland", "MI", "November", "275k", "4,900", "1,350k", "0.204", "580", "0.95", "Optimal"),
    ("Eneroi", "Petersburg", "VA", "January", "312k", "5,900", "1,410k", "0.221", "660", "0.93", "Optimal"),
    ("Eneroi", "Jarratt", "VA", "December", "283k", "5,200", "1,290k", "0.219", "590", "0.91", "Optimal"),
    ("Eneroi", "Holland", "MI", "December", "295k", "5,600", "1,380k", "0.214", "630", "0.92", "Optimal"),
    ("Innovative", "Expansion L1", "TX", "Q3 future", "380k", "7,200", "1,950k", "0.195", "820", "0.98", "Model Pilot"),
]

INNOVATIONS = [
    ("Weather-normalized EnPI", "High ROI", "Subtract HDD/CDD effects so summer/winter spikes don't look like inefficiency."),
    ("15-min peak demand predictor", "Demand shaving", "Alert before a new monthly kW peak sets a 12-month ratchet charge."),
    ("Activity-based $/lb costing", "Activity costing", "Tie utility cost to MES batches / SKUs instead of P&L overhead."),
    ("Power factor sentinel", "Power quality", "Groveport PF alert path — kVAR monitoring + capacitor bank triggers."),
    ("Scope 1 & 2 GHG accounting", "ESG", "eGRID factors → one-click carbon reports from metered kWh / therms."),
    ("Idle / phantom load detector", "AI / analytics", "Historian clustering for weekend baseload and non-op waste."),
]


def _apex_events() -> dict:
    keys = [
        "animationEnd", "beforeMount", "beforeResetZoom", "beforeZoom", "brushScrolled",
        "click", "dataPointMouseEnter", "dataPointMouseLeave", "dataPointSelection",
        "legendClick", "markerClick", "mounted", "mouseLeave", "mouseMove", "scrolled",
        "selection", "updated", "xAxisLabelClick", "zoomed",
    ]
    return {k: False for k in keys}


def _label(name: str, text: str, classes: str = "font-label", **style) -> dict:
    return {
        "type": "ia.display.label",
        "meta": {"name": name},
        "props": {"text": text, "style": {"classes": classes, **style}},
    }


def _expr_label(name: str, expression: str, *, classes: str = "font-livedata-entry", **style) -> dict:
    return {
        "type": "ia.display.label",
        "meta": {"name": name},
        "props": {"text": "—", "style": {"classes": classes, **style}},
        "propConfig": {
            "props.text": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": expression},
                    "overlays": {
                        "bad": False, "error": False, "pending": False,
                        "stale": False, "unknown": False, "disabled": False,
                    },
                }
            }
        },
    }


def _stat_card(name: str, label: str, value_expr: str | None, unit: str, hint: str, static: str | None = None) -> dict:
    val_child = (
        {
            "type": "ia.display.label",
            "meta": {"name": "Val"},
            "props": {
                "text": static or "—",
                "style": {
                    "classes": "font-livedata-entry",
                    "fontSize": "20px",
                    "fontWeight": "700",
                },
            },
        }
        if static is not None
        else _expr_label(
            "Val",
            value_expr or "'—'",
            fontSize="20px",
            fontWeight="700",
        )
    )
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 1, "shrink": 1, "basis": "0%"},
        "props": {
            "direction": "column",
            "style": {
                "classes": "container-card container-card-border kpi-exec-stat",
                "gap": "4px",
                "padding": "12px 14px",
                "minWidth": "140px",
            },
        },
        "children": [
            _label("Lbl", label, fontSize="12px", opacity="0.75"),
            {
                "type": "ia.container.flex",
                "meta": {"name": "Row"},
                "props": {
                    "direction": "row",
                    "alignItems": "baseline",
                    "style": {"gap": "6px"},
                },
                "children": [
                    val_child,
                    _label("Unit", unit, fontSize="12px", opacity="0.7"),
                ],
            },
            _label("Hint", hint, fontSize="11px", opacity="0.65", whiteSpace="normal"),
        ],
    }


def _chart_shell(name: str, chart: dict, height: int) -> dict:
    """Fixed-height chart host — prevents Perspective flex overflow scrollbars."""
    chart = dict(chart)
    chart["position"] = {"grow": 0, "shrink": 0, "basis": f"{height}px"}
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 0, "shrink": 0, "basis": f"{height}px"},
        "props": {
            "direction": "column",
            "style": {
                "classes": "kpi-exec-chart",
                "width": "100%",
                "height": f"{height}px",
                "minHeight": f"{height}px",
                "maxHeight": f"{height}px",
                "overflow": "hidden",
                "flexShrink": "0",
            },
        },
        "children": [chart],
    }


def _band_chart(
    name: str,
    *,
    categories: list[str],
    band_high: list[float],
    band_low: list[float],
    avg3: list[float],
    actual: list[float],
    y_title: str,
    height: int = 300,
) -> dict:
    """7yr high–low shaded band + 3yr AVG + actual (rangeArea, not high/low lines)."""
    band = [{"x": c, "y": [lo, hi]} for c, lo, hi in zip(categories, band_low, band_high)]
    line3 = [{"x": c, "y": v} for c, v in zip(categories, avg3)]
    line_a = [{"x": c, "y": v} for c, v in zip(categories, actual)]
    chart = {
        "type": "kyvislabs.display.apexchart",
        "meta": {"name": f"{name}Apex"},
        "props": {
            "type": "rangeArea",
            "series": [
                {"name": "7yr Month High–Low", "type": "rangeArea", "data": band},
                {"name": "3yr Month AVG", "type": "line", "data": line3},
                {"name": "kWh Actual", "type": "line", "data": line_a},
            ],
            "options": {
                "chart": {
                    "type": "rangeArea",
                    "height": height,
                    "width": "100%",
                    "animations": {"enabled": False},
                    "toolbar": {"show": False},
                    "zoom": {"enabled": False},
                    "selection": {"enabled": False},
                    "redrawOnParentResize": True,
                    "redrawOnWindowResize": True,
                    "events": _apex_events(),
                },
                "colors": ["#8FBF88", "#E67E22", "#2C3E50"],
                "dataLabels": {"enabled": False},
                "fill": {
                    "opacity": [0.35, 1, 1],
                    "type": ["solid", "solid", "solid"],
                },
                "stroke": {"curve": "smooth", "width": [0, 2, 2.5]},
                "legend": {
                    "show": True,
                    "position": "top",
                    "horizontalAlign": "left",
                    "fontSize": "11px",
                },
                "grid": {
                    "borderColor": "rgba(0,0,0,0.08)",
                    "strokeDashArray": 3,
                    "padding": {"left": 8, "right": 8},
                },
                "markers": {"size": 0},
                "tooltip": {"shared": True, "intersect": False},
                "xaxis": {
                    "type": "category",
                    "categories": categories,
                    "labels": {
                        "rotate": -45,
                        "hideOverlappingLabels": True,
                        "style": {"fontSize": "10px"},
                    },
                    "tickAmount": 8,
                },
                "yaxis": {
                    "title": {"text": y_title, "style": {"fontSize": "11px"}},
                    "labels": {"style": {"fontSize": "10px"}},
                    "decimalsInFloat": 0,
                },
            },
        },
    }
    return _chart_shell(name, chart, height)


def _line_chart(
    name: str,
    *,
    categories: list[str],
    series: list[dict],
    colors: list[str],
    y_title: str,
    height: int = 280,
) -> dict:
    chart = {
        "type": "kyvislabs.display.apexchart",
        "meta": {"name": f"{name}Apex"},
        "props": {
            "type": "line",
            "series": series,
            "options": {
                "chart": {
                    "type": "line",
                    "height": height,
                    "width": "100%",
                    "animations": {"enabled": False},
                    "toolbar": {"show": False},
                    "zoom": {"enabled": False},
                    "events": _apex_events(),
                },
                "colors": colors,
                "stroke": {"curve": "smooth", "width": 2},
                "dataLabels": {"enabled": False},
                "legend": {"show": True, "position": "top", "fontSize": "11px"},
                "grid": {"borderColor": "rgba(0,0,0,0.08)", "strokeDashArray": 3},
                "markers": {"size": 0},
                "tooltip": {"shared": True},
                "xaxis": {
                    "categories": categories,
                    "labels": {"rotate": -45, "style": {"fontSize": "10px"}},
                },
                "yaxis": {
                    "title": {"text": y_title, "style": {"fontSize": "11px"}},
                    "labels": {"style": {"fontSize": "10px"}},
                },
            },
        },
    }
    return _chart_shell(name, chart, height)


def _bar_chart(name: str, *, categories: list[str], data: list[float], y_title: str, height: int = 240) -> dict:
    chart = {
        "type": "kyvislabs.display.apexchart",
        "meta": {"name": f"{name}Apex"},
        "props": {
            "type": "bar",
            "series": [{"name": y_title, "data": data}],
            "options": {
                "chart": {
                    "type": "bar",
                    "height": height,
                    "width": "100%",
                    "animations": {"enabled": False},
                    "toolbar": {"show": False},
                    "events": _apex_events(),
                },
                "colors": ["#5C6B7A"],
                "dataLabels": {"enabled": False},
                "legend": {"show": False},
                "grid": {"borderColor": "rgba(0,0,0,0.08)", "strokeDashArray": 3},
                "xaxis": {
                    "categories": categories,
                    "labels": {"rotate": -45, "style": {"fontSize": "10px"}},
                },
                "yaxis": {
                    "title": {"text": y_title, "style": {"fontSize": "11px"}},
                    "labels": {"style": {"fontSize": "10px"}},
                },
            },
        },
    }
    return _chart_shell(name, chart, height)


def _card(name: str, title: str, children: list[dict], *, trailing: str | None = None) -> dict:
    head_kids = [
        _label("Title", title, "font-heading", fontSize="15px", fontWeight="600"),
    ]
    if trailing:
        head_kids.append(
            {
                "type": "ia.display.label",
                "meta": {"name": "Pill"},
                "props": {
                    "text": trailing,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "padding": "2px 8px",
                        "borderRadius": "4px",
                        "backgroundColor": "rgba(12,123,179,0.12)",
                        "opacity": "0.9",
                    },
                },
            }
        )
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "props": {
            "direction": "column",
            "style": {
                "classes": "container-card container-card-border",
                "gap": "10px",
                "padding": "14px 16px",
                "width": "100%",
                "boxSizing": "border-box",
                "overflow": "hidden",
            },
        },
        "children": [
            {
                "type": "ia.container.flex",
                "meta": {"name": "Head"},
                "props": {
                    "direction": "row",
                    "justify": "space-between",
                    "alignItems": "center",
                    "style": {"gap": "8px", "width": "100%"},
                },
                "children": head_kids,
            },
            *children,
        ],
    }


def _nav_button(name: str, text: str, page: str) -> dict:
    return {
        "type": "ia.input.button",
        "meta": {"name": name},
        "props": {
            "text": text,
            "primary": False,
            "style": {"classes": "font-label", "fontSize": "12px"},
        },
        "events": {
            "component": {
                "onActionPerformed": {
                    "type": "script",
                    "scope": "G",
                    "config": {
                        "script": f"Navigation.Nav.navigate({{'action': 'page', 'page': '{page}'}})"
                    },
                }
            }
        },
    }


def build(series: dict) -> dict:
    tag = "coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site')"
    kwh_rows = series["kWh"]["rows"][-HORIZON:]
    temp_rows = series["temperature"]["rows"][-HORIZON:]

    # Align temp to kwh length if needed (use last N of each)
    cats = [r["label"] for r in kwh_rows]
    kwh_actual = [round(r["actual"] / 1000.0, 1) for r in kwh_rows]
    kwh_avg3 = [round(r["avg3"] / 1000.0, 1) for r in kwh_rows]
    kwh_high = [round(r["high"] / 1000.0, 1) for r in kwh_rows]
    kwh_low = [round(r["low"] / 1000.0, 1) for r in kwh_rows]

    # Temp: match by taking last HORIZON from temp series (labels may differ slightly)
    t_cats = [r["label"] for r in temp_rows]
    t_vals = [round(r["current"], 1) for r in temp_rows]

    # Therm placeholder from seasonal pattern (Excel Therm sheet empty) — scale with temp inverse
    therm_stub = [max(2000, int(18000 - (t * 180))) for t in t_vals]
    # Production stub from canvas-ish scale (k-lb) — use tag ProdVol as latest only for strip
    prod_stub = [120 + (i % 5) * 8 + (i % 3) * 4 for i in range(len(cats))]

    total_kwh = sum(r["actual"] for r in kwh_rows)
    # Intensity uses live tags on strip; chart uses stubs until monthly prod historian exists

    panel_exec = {
        "type": "ia.container.flex",
        "meta": {"name": "PanelExecutive"},
        "position": {"tabIndex": 0},
        "props": {
            "direction": "column",
            "style": {
                "gap": "14px",
                "padding": "14px 16px 18px",
                "overflow": "auto",
                "height": "100%",
                "minHeight": "0",
            },
        },
        "children": [
            _card(
                "CardPower",
                "Primary power — monthly electricity (k-kWh) vs baselines",
                [
                    _label(
                        "Blurb",
                        "Actual demand vs 3-yr average and 7-yr high/low envelope "
                        f"(last {HORIZON} months from Utility Tracker).",
                        fontSize="12px",
                        opacity="0.8",
                        whiteSpace="normal",
                    ),
                    _band_chart(
                        "KwhChart",
                        categories=cats,
                        band_high=kwh_high,
                        band_low=kwh_low,
                        avg3=kwh_avg3,
                        actual=kwh_actual,
                        y_title="k-kWh",
                        height=300,
                    ),
                ],
                trailing="EPMS",
            ),
            {
                "type": "ia.container.flex",
                "meta": {"name": "DualCharts"},
                "props": {
                    "direction": "row",
                    "wrap": "wrap",
                    "style": {"gap": "14px", "width": "100%"},
                },
                "children": [
                    {
                        "type": "ia.container.flex",
                        "meta": {"name": "WrapProd"},
                        "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                        "props": {"direction": "column", "style": {"minWidth": "320px"}},
                        "children": [
                            _card(
                                "CardProd",
                                "Production volume (placeholder monthly)",
                                [
                                    _label(
                                        "Blurb",
                                        "Monthly k-lb series is stubbed until production historian rolls up. "
                                        "Live MTD volume is on the KPI strip.",
                                        fontSize="12px",
                                        opacity="0.8",
                                        whiteSpace="normal",
                                    ),
                                    _bar_chart(
                                        "ProdChart",
                                        categories=cats,
                                        data=prod_stub,
                                        y_title="k-lb (stub)",
                                        height=240,
                                    ),
                                ],
                                trailing="Production",
                            )
                        ],
                    },
                    {
                        "type": "ia.container.flex",
                        "meta": {"name": "WrapTherm"},
                        "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                        "props": {"direction": "column", "style": {"minWidth": "320px"}},
                        "children": [
                            _card(
                                "CardTherm",
                                "Thermal load vs ambient temperature",
                                [
                                    _label(
                                        "Blurb",
                                        "Temp from Utility Tracker. Therm series is a weather-shaped stub "
                                        "until gas meters feed.",
                                        fontSize="12px",
                                        opacity="0.8",
                                        whiteSpace="normal",
                                    ),
                                    _line_chart(
                                        "ThermTempChart",
                                        categories=t_cats if len(t_cats) == len(therm_stub) else cats[: len(therm_stub)],
                                        series=[
                                            {"name": "Natural Gas (therm stub)", "data": therm_stub},
                                            {
                                                "name": "Mean Temp °F (×150)",
                                                "data": [round(t * 150, 0) for t in t_vals],
                                            },
                                        ],
                                        colors=["#C0392B", "#E67E22"],
                                        y_title="Therm / scaled °F",
                                        height=240,
                                    ),
                                ],
                                trailing="Utility",
                            )
                        ],
                    },
                ],
            },
        ],
    }

    # Benchmarking table header + rows
    headers = ["Division", "Plant", "St", "Restart", "kWh", "Therm", "Prod", "kWh/lb", "Peak kW", "PF", "Status"]
    header_row = {
        "type": "ia.container.flex",
        "meta": {"name": "TableHead"},
        "props": {
            "direction": "row",
            "style": {
                "gap": "6px",
                "width": "100%",
                "padding": "6px 4px",
                "borderBottom": "1px solid rgba(0,0,0,0.12)",
            },
        },
        "children": [
            _label(
                f"H{i}",
                h,
                fontSize="11px",
                fontWeight="700",
                opacity="0.7",
                flex=f"{2 if i < 2 else 1} 1 0%",
                minWidth="0",
            )
            for i, h in enumerate(headers)
        ],
    }
    site_rows = []
    for i, row in enumerate(SITES):
        highlight = row[1] == "Groveport"
        site_rows.append(
            {
                "type": "ia.container.flex",
                "meta": {"name": f"Site{i}"},
                "props": {
                    "direction": "row",
                    "style": {
                        "gap": "6px",
                        "width": "100%",
                        "padding": "7px 4px",
                        "borderBottom": "1px solid rgba(0,0,0,0.06)",
                        "backgroundColor": "rgba(12,123,179,0.06)" if highlight else "transparent",
                    },
                },
                "children": [
                    _label(
                        f"C{j}",
                        str(cell),
                        fontSize="12px",
                        fontWeight="600" if highlight else "400",
                        flex=f"{2 if j < 2 else 1} 1 0%",
                        minWidth="0",
                        overflow="hidden",
                        textOverflow="ellipsis",
                        whiteSpace="nowrap",
                    )
                    for j, cell in enumerate(row)
                ],
            }
        )

    panel_matrix = {
        "type": "ia.container.flex",
        "meta": {"name": "PanelMatrix"},
        "position": {"tabIndex": 1},
        "props": {
            "direction": "column",
            "style": {
                "gap": "12px",
                "padding": "14px 16px 18px",
                "overflow": "auto",
                "height": "100%",
                "minHeight": "0",
            },
        },
        "children": [
            _label(
                "MatrixTitle",
                "Enterprise multi-facility scorecard (placeholder)",
                "font-heading",
                fontSize="16px",
                fontWeight="700",
            ),
            _label(
                "MatrixSub",
                "Cascade / Eneroi / Innovative matrix from the executive canvas. "
                "Groveport row highlighted — bind to live site tags as metering rolls out.",
                fontSize="12px",
                opacity="0.8",
                whiteSpace="normal",
            ),
            _card(
                "CardTable",
                "Plant matrix",
                [header_row, *site_rows],
            ),
            {
                "type": "ia.container.flex",
                "meta": {"name": "RestartProtocol"},
                "props": {
                    "direction": "row",
                    "wrap": "wrap",
                    "style": {"gap": "12px", "width": "100%"},
                },
                "children": [
                    {
                        "type": "ia.container.flex",
                        "meta": {"name": "WrapRestart"},
                        "position": {"grow": 1, "basis": "0%"},
                        "props": {"direction": "column", "style": {"minWidth": "280px"}},
                        "children": [
                            _card(
                                "CardRestart",
                                "Line restart baseline protocol",
                                [
                                    _label("R1", "Cascade NY — March", fontSize="13px", opacity="0.85"),
                                    _label("R2", "Cascade Groveport — October", fontSize="13px", fontWeight="600"),
                                    _label("R3", "Cascade Holland — November", fontSize="13px", opacity="0.85"),
                                    _label("R4", "Eneroi Petersburg — January", fontSize="13px", opacity="0.85"),
                                    _label("R5", "Eneroi Jarratt / Holland — December", fontSize="13px", opacity="0.85"),
                                ],
                            )
                        ],
                    }
                ],
            },
        ],
    }

    innov_cards = []
    for i, (title, pill, body) in enumerate(INNOVATIONS):
        innov_cards.append(
            {
                "type": "ia.container.flex",
                "meta": {"name": f"Innov{i}"},
                "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                "props": {"direction": "column", "style": {"minWidth": "280px", "maxWidth": "100%"}},
                "children": [_card(f"CardInnov{i}", title, [_label("B", body, fontSize="13px", opacity="0.85", whiteSpace="normal")], trailing=pill)],
            }
        )

    panel_innov = {
        "type": "ia.container.flex",
        "meta": {"name": "PanelInnovations"},
        "position": {"tabIndex": 2},
        "props": {
            "direction": "column",
            "style": {
                "gap": "12px",
                "padding": "14px 16px 18px",
                "overflow": "auto",
                "height": "100%",
                "minHeight": "0",
            },
        },
        "children": [
            _label(
                "InnovTitle",
                "Future innovations roadmap",
                "font-heading",
                fontSize="16px",
                fontWeight="700",
            ),
            _label(
                "InnovSub",
                "From the executive canvas — Ignition Perspective capabilities to close utility gaps.",
                fontSize="12px",
                opacity="0.8",
                whiteSpace="normal",
            ),
            {
                "type": "ia.container.flex",
                "meta": {"name": "InnovGrid"},
                "props": {
                    "direction": "row",
                    "wrap": "wrap",
                    "style": {"gap": "12px", "width": "100%"},
                },
                "children": innov_cards,
            },
        ],
    }

    gwh = f"{total_kwh / 1_000_000:.2f}"

    return {
        "custom": {},
        "params": {"tagRoot": "[default]KPI/Groveport/Site"},
        "propConfig": {},
        "props": {"defaultSize": {"width": 1400, "height": 900}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "bg-page kpi-dashboard-page kpi-exec-page",
                    "gap": "12px",
                    "padding": "14px 18px 16px",
                    "overflow": "hidden",
                    "height": "100%",
                    "minHeight": "0",
                },
            },
            "children": [
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Header"},
                    "position": {"grow": 0, "shrink": 0},
                    "props": {
                        "direction": "column",
                        "style": {
                            "classes": "container-card container-card-border",
                            "gap": "8px",
                            "padding": "12px 16px",
                            "width": "100%",
                        },
                    },
                    "children": [
                        {
                            "type": "ia.container.flex",
                            "meta": {"name": "TitleRow"},
                            "props": {
                                "direction": "row",
                                "justify": "space-between",
                                "alignItems": "center",
                                "wrap": "wrap",
                                "style": {"gap": "10px", "width": "100%"},
                            },
                            "children": [
                                {
                                    "type": "ia.container.flex",
                                    "meta": {"name": "Titles"},
                                    "props": {"direction": "column", "style": {"gap": "2px"}},
                                    "children": [
                                        _label(
                                            "Title",
                                            "Groveport — Executive utility & energy",
                                            "font-heading",
                                            fontSize="20px",
                                            fontWeight="700",
                                        ),
                                        _label(
                                            "Sub",
                                            "Canvas-adapted SPoG · live pens + Utility Tracker baselines · metering roadmap",
                                            fontSize="12px",
                                            opacity="0.8",
                                        ),
                                    ],
                                },
                                {
                                    "type": "ia.container.flex",
                                    "meta": {"name": "HeaderActions"},
                                    "props": {
                                        "direction": "row",
                                        "alignItems": "center",
                                        "style": {"gap": "8px"},
                                    },
                                    "children": [
                                        _label(
                                            "Horizon",
                                            f"Horizon: {HORIZON} months",
                                            fontSize="12px",
                                            opacity="0.75",
                                            padding="4px 8px",
                                            borderRadius="4px",
                                            backgroundColor="rgba(0,0,0,0.04)",
                                        ),
                                        _nav_button(
                                            "BtnClassic",
                                            "Classic domain tabs",
                                            "/plants/groveport/classic",
                                        ),
                                    ],
                                },
                            ],
                        }
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Callout"},
                    "position": {"grow": 0, "shrink": 0},
                    "props": {
                        "direction": "column",
                        "style": {
                            "classes": "kpi-exec-callout",
                            "gap": "2px",
                            "padding": "10px 14px",
                            "borderRadius": "8px",
                            "backgroundColor": "rgba(12,123,179,0.08)",
                            "borderLeft": "4px solid #0C7BB3",
                            "width": "100%",
                        },
                    },
                    "children": [
                        _label(
                            "CallTitle",
                            "Session context",
                            fontSize="12px",
                            fontWeight="700",
                        ),
                        _label(
                            "CallBody",
                            "Groveport site dashboard with enterprise matrix placeholders (Cascade / Eneroi / Innovative). "
                            "Line-break restart baselines from Utility Tracker. Area metering coverage on classic EPMS tab.",
                            fontSize="12px",
                            opacity="0.85",
                            whiteSpace="normal",
                        ),
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "KpiStrip"},
                    "position": {"grow": 0, "shrink": 0},
                    "props": {
                        "direction": "row",
                        "wrap": "wrap",
                        "style": {"gap": "10px", "width": "100%"},
                    },
                    "children": [
                        _stat_card(
                            "StatGwh",
                            "Period consumption",
                            None,
                            "GWh",
                            f"{HORIZON}M aggregate (Tracker)",
                            static=gwh,
                        ),
                        _stat_card(
                            "StatIntensity",
                            "Energy intensity",
                            f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Production/kWhPerLb')), null, tag({tag} + '/Production/kWhPerLb')), null), 0), '0.000')",
                            "kWh/lb",
                            "Live tag · target ≤ 0.205",
                        ),
                        _stat_card(
                            "StatTherm",
                            "Natural gas (MTD)",
                            f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Utility/Therm')), null, tag({tag} + '/Utility/Therm')), null), 0), '#,##0')",
                            "therm",
                            "Awaiting meter feed",
                        ),
                        _stat_card(
                            "StatProd",
                            "Production (MTD)",
                            f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Production/ProdVol')), null, tag({tag} + '/Production/ProdVol')), null), 0), '#,##0')",
                            "lb",
                            "MES / Tracker seed",
                        ),
                        _stat_card(
                            "StatPf",
                            "Power factor (est.)",
                            None,
                            "PF",
                            "From latest kWh / kvar",
                            static="0.89",
                        ),
                        _stat_card(
                            "StatMeter",
                            "Metering coverage",
                            f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/ComingOnline/MeteringCoveragePct')), null, tag({tag} + '/ComingOnline/MeteringCoveragePct')), null), 0), '0')",
                            "% areas",
                            "Plant metering initiative",
                        ),
                    ],
                },
                {
                    "type": "ia.container.tab",
                    "meta": {"name": "ExecTabs"},
                    "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                    "props": {
                        "currentTabIndex": 0,
                        "tabs": ["Executive SPoG", "Plant matrix", "Future innovations"],
                        "tabSize": {"width": 150, "height": 36},
                        "style": {
                            "classes": "kpi-domain-tabs container-card container-card-border",
                            "flex": "1 1 0%",
                            "minHeight": "0",
                            "height": "100%",
                            "width": "100%",
                            "overflow": "hidden",
                        },
                    },
                    "children": [panel_exec, panel_matrix, panel_innov],
                },
            ],
        },
    }


def main() -> None:
    series = json.loads(SERIES_PATH.read_text(encoding="utf-8"))
    overview = build(series)
    OVERVIEW.write_text(json.dumps(overview, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OVERVIEW}")


if __name__ == "__main__":
    main()
