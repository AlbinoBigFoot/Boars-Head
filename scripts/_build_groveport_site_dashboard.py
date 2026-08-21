#!/usr/bin/env python3
"""Extract Utility Tracker Dashboard series + rebuild Groveport Site Overview.

Mirrors Excel Dashboard tab:
  - Temperature (36 months): 7yr high/low band, 3yr AVG, Current Month AVG
  - kWh (48 months): 7yr high/low band, 3yr AVG, kWh Actual

Adds metering-initiative + future KPI shells (YoY, line-break restart).
"""
from __future__ import annotations

import json
import re
import zipfile
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
XLSX = ROOT / "docs/kpi/Utility Tracker_template.xlsx"
SERIES_OUT = ROOT / "docs/kpi/dashboard-series.json"
OVERVIEW = (
    ROOT
    / "gateways/standard/data/projects/BH/com.inductiveautomation.perspective"
    / "views/00_Pages/Groveport/Site/Overview/view.json"
)
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

# Excel Dashboard defaults
TEMP_MONTHS = 36
KWH_MONTHS = 48


def _ss(z: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in z.namelist():
        return []
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    out: list[str] = []
    for si in root.findall("m:si", NS):
        texts = [
            t.text or ""
            for t in si.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")
        ]
        out.append("".join(texts))
    return out


def _sheet_grid(z: zipfile.ZipFile, name: str) -> dict[int, dict[str, object]]:
    ss = _ss(z)
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    rid_to = {r.attrib["Id"]: r.attrib["Target"] for r in rels}
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    path = None
    for s in wb.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet"):
        if s.attrib.get("name") == name:
            rid = s.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
            path = "xl/" + rid_to[rid].lstrip("/")
            break
    if not path:
        raise KeyError(name)
    sh = ET.fromstring(z.read(path))
    grid: dict[int, dict[str, object]] = {}
    for c in sh.findall(".//m:c", NS):
        ref = c.attrib.get("r")
        v = c.find("m:v", NS)
        if not ref or v is None or v.text is None:
            continue
        m = re.match(r"([A-Z]+)(\d+)", ref)
        if not m:
            continue
        col, row = m.group(1), int(m.group(2))
        val: object = v.text
        if c.attrib.get("t") == "s":
            val = ss[int(v.text)]
        else:
            try:
                val = float(v.text)
            except ValueError:
                pass
        grid.setdefault(row, {})[col] = val
    return grid


def _f(v: object) -> float | None:
    if v is None or v == "":
        return None
    try:
        return float(v)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def _label(v: object) -> str:
    s = str(v or "").replace("'", "").strip()
    # "January 24" / "January 16" → "Jan '24"
    m = re.match(r"([A-Za-z]+)\s+(\d{2})", s)
    if m:
        return f"{m.group(1)[:3]} '{m.group(2)}"
    return s


def extract_series() -> dict:
    with zipfile.ZipFile(XLSX) as z:
        temp = _sheet_grid(z, "Temp")
        kwh = _sheet_grid(z, "kWh")

    temp_rows = []
    for row in sorted(r for r in temp if r >= 2):
        g = temp[row]
        lab = _label(g.get("A"))
        high, low = _f(g.get("R")), _f(g.get("S"))
        avg3, cur = _f(g.get("P")), _f(g.get("Q"))
        if not lab or None in (high, low, avg3, cur):
            continue
        temp_rows.append(
            {
                "label": lab,
                "high": high,
                "low": low,
                "avg3": avg3,
                "current": cur,
            }
        )
    temp_rows = temp_rows[-TEMP_MONTHS:]

    kwh_rows = []
    for row in sorted(r for r in kwh if r >= 2):
        g = kwh[row]
        lab = _label(g.get("J") or g.get("A"))
        high, low = _f(g.get("N")), _f(g.get("O"))
        avg3, actual = _f(g.get("L")), _f(g.get("K"))
        if not lab or None in (high, low, avg3, actual):
            continue
        kwh_rows.append(
            {
                "label": lab,
                "high": high,
                "low": low,
                "avg3": avg3,
                "actual": actual,
            }
        )
    kwh_rows = kwh_rows[-KWH_MONTHS:]

    return {
        "source": "Utility Tracker_template.xlsx / Dashboard lengths",
        "temperature": {"months": TEMP_MONTHS, "rows": temp_rows},
        "kWh": {"months": KWH_MONTHS, "rows": kwh_rows},
        "notes": [
            "Add Eneroi line break restart avg",
            "Add Cascade line break restart avg",
            "YoY kWh + Therm chart",
            "Production KPI YoY",
            "Plant-wide metering initiative",
        ],
    }


def _apex_events() -> dict:
    keys = [
        "animationEnd",
        "beforeMount",
        "beforeResetZoom",
        "beforeZoom",
        "brushScrolled",
        "click",
        "dataPointMouseEnter",
        "dataPointMouseLeave",
        "dataPointSelection",
        "legendClick",
        "markerClick",
        "mounted",
        "mouseLeave",
        "mouseMove",
        "scrolled",
        "selection",
        "updated",
        "xAxisLabelClick",
        "zoomed",
    ]
    return {k: False for k in keys}


def benchmark_chart(
    *,
    name: str,
    categories: list[str],
    band_high: list[float],
    band_low: list[float],
    avg3: list[float],
    primary: list[float],
    primary_name: str,
    y_title: str,
    height: int = 280,
) -> dict:
    """ApexCharts combo: rangeArea band + two lines (Excel Dashboard style)."""
    band = [{"x": c, "y": [lo, hi]} for c, lo, hi in zip(categories, band_low, band_high)]
    line3 = [{"x": c, "y": v} for c, v in zip(categories, avg3)]
    line_p = [{"x": c, "y": v} for c, v in zip(categories, primary)]
    chart = {
        "type": "kyvislabs.display.apexchart",
        "meta": {"name": f"{name}Apex"},
        "props": {
            "type": "rangeArea",
            "series": [
                {"name": "7yr Month High–Low", "type": "rangeArea", "data": band},
                {"name": "3yr Month AVG", "type": "line", "data": line3},
                {"name": primary_name, "type": "line", "data": line_p},
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
                # Mid-bright palette — readable on light and dark themes
                "colors": ["#5FAE6E", "#F0A030", "#3D9BE9"],
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
                    "padding": {"left": 8, "right": 8, "bottom": 0, "top": 0},
                },
                "markers": {"size": 0},
                "tooltip": {"shared": True, "intersect": False},
                "xaxis": {
                    "type": "category",
                    "categories": categories,
                    "labels": {
                        "rotate": -45,
                        "rotateAlways": False,
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


def _chart_shell(name: str, chart: dict, height: int) -> dict:
    """Fixed-height host so Apex cannot introduce nested scrollbars."""
    # Apex child must not grow/stretch inside the shell
    chart = dict(chart)
    chart["position"] = {"grow": 0, "shrink": 0, "basis": f"{height}px"}
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 0, "shrink": 0, "basis": f"{height}px"},
        "props": {
            "direction": "column",
            "style": {
                "classes": "kpi-chart-shell",
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


def _label_node(name: str, text: str, classes: str, **style) -> dict:
    return {
        "type": "ia.display.label",
        "meta": {"name": name},
        "props": {"text": text, "style": {"classes": classes, **style}},
    }


def _hero_pen(name: str, label: str, value_expr: str, unit: str) -> dict:
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 0, "shrink": 0, "basis": "168px"},
        "props": {
            "direction": "column",
            "justify": "center",
            "style": {
                "classes": "container-card container-card-border kpi-hero-pen",
                "gap": "2px",
                "padding": "10px 12px",
                "minWidth": "160px",
                "maxWidth": "200px",
                "width": "168px",
                "flexShrink": "0",
                "overflow": "hidden",
            },
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "Lbl"},
                "props": {
                    "text": label,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "13px",
                        "opacity": "0.8",
                    },
                },
            },
            {
                "type": "ia.container.flex",
                "meta": {"name": "Row"},
                "props": {
                    "direction": "row",
                    "alignItems": "baseline",
                    "style": {"gap": "6px"},
                },
                "children": [
                    {
                        "type": "ia.display.label",
                        "meta": {"name": "Val"},
                        "props": {
                            "text": "—",
                            "style": {
                                "classes": "font-livedata-entry",
                                "fontSize": "22px",
                                "fontWeight": "600",
                            },
                        },
                        "propConfig": {
                            "props.text": {
                                "binding": {
                                    "type": "expr",
                                    "config": {"expression": value_expr},
                                    "overlays": {
                                        "bad": False,
                                        "error": False,
                                        "pending": False,
                                        "stale": False,
                                        "unknown": False,
                                        "disabled": False,
                                    },
                                }
                            }
                        },
                    },
                    {
                        "type": "ia.display.label",
                        "meta": {"name": "Unit"},
                        "props": {
                            "text": unit,
                            "style": {
                                "classes": "font-label",
                                "fontSize": "13px",
                                "opacity": "0.7",
                            },
                        },
                    },
                ],
            },
        ],
    }


GROVEPORT_AREAS = [
    "Freezer",
    "SuperChill",
    "Club",
    "Palletizing",
    "East PH",
    "West PH",
    "Dock",
    "Machine Room",
]

# Demo metering-by-area (status, kWh MTD, therm MTD) — shown until live meters feed
METERING_DEMO = {
    "Freezer": ("Online", 84210, 2140),
    "SuperChill": ("Online", 61180, 1825),
    "Club": ("Online", 22140, 910),
    "Palletizing": ("Online", 18450, 420),
    "East PH": ("Online", 33420, 1180),
    "West PH": ("Online", 29780, 1095),
    "Dock": ("Planned", 0, 0),
    "Machine Room": ("Installing", 15220, 780),
}

# Excel Dashboard reference table (line-break baselines)
CASCADE_SITES = [
    ("New York", "March"),
    ("Groveport", "October"),
    ("Holland", "November"),
]
ENEROI_SITES = [
    ("Petersburg", "January"),
    ("Jarratt", "December"),
    ("Holland", "December"),
]


def _status_chip(name: str, text: str) -> dict:
    return {
        "type": "ia.display.label",
        "meta": {"name": name},
        "props": {
            "text": text,
            "style": {
                "classes": "font-label",
                "fontSize": "11px",
                "opacity": "0.75",
                "padding": "2px 8px",
                "borderRadius": "4px",
                "backgroundColor": "color-mix(in srgb, var(--callToAction) 18%, transparent)",
                "color": "var(--callToAction)",
                "flexShrink": "0",
            },
        },
    }


def _section_head(name: str, title: str, status: str) -> dict:
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 0, "shrink": 0},
        "props": {
            "direction": "row",
            "justify": "flex-start",
            "alignItems": "center",
            "style": {"gap": "10px", "width": "100%", "flexWrap": "wrap"},
        },
        "children": [
            _label_node("Title", title, "font-heading", fontSize="15px", fontWeight="600"),
            _status_chip("Status", status),
        ],
    }


def _expr_label(name: str, expression: str, *, classes: str = "font-livedata-entry", **style) -> dict:
    return {
        "type": "ia.display.label",
        "meta": {"name": name},
        "position": {"grow": 0, "shrink": 0},
        "props": {"text": "—", "style": {"classes": classes, **style}},
        "propConfig": {
            "props.text": {
                "binding": {
                    "type": "expr",
                    "config": {"expression": expression},
                    "overlays": {
                        "bad": False,
                        "error": False,
                        "pending": False,
                        "stale": False,
                        "unknown": False,
                        "disabled": False,
                    },
                }
            }
        },
    }


def _meter_area_row(area: str, tag_root_expr: str) -> dict:
    """One metering row — demo values baked in (tags remain for future live feed)."""
    safe = area.replace(" ", "")
    status, kwh, therm = METERING_DEMO.get(area, ("Planned", 0, 0))
    return {
        "type": "ia.container.flex",
        "meta": {"name": f"Meter{safe}"},
        "position": {"basis": "32px", "shrink": 0, "grow": 0},
        "props": {
            "direction": "row",
            "alignItems": "center",
            "justify": "flex-start",
            "style": {
                "classes": "kpi-coming-meter-row",
                "gap": "8px",
                "width": "100%",
                "maxWidth": "420px",
                "padding": "3px 0",
                "borderBottom": "1px solid rgba(0,0,0,0.06)",
                "overflow": "hidden",
            },
        },
        "children": [
            {
                "type": "ia.display.label",
                "meta": {"name": "Area"},
                "position": {"grow": 0, "basis": "110px", "shrink": 0},
                "props": {
                    "text": area,
                    "style": {
                        "classes": "font-label",
                        "fontSize": "13px",
                        "width": "110px",
                        "minWidth": "110px",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                        "whiteSpace": "nowrap",
                    },
                },
            },
            _label_node(
                "Status",
                status,
                "font-label",
                fontSize="12px",
                opacity="0.8",
                width="70px",
                minWidth="70px",
                textAlign="left",
            ),
            _label_node(
                "Kwh",
                f"{kwh:,.0f}",
                "font-livedata-entry",
                fontSize="13px",
                fontWeight="600",
                width="56px",
                minWidth="56px",
                textAlign="right",
            ),
            {
                "type": "ia.display.label",
                "meta": {"name": "KwhUnit"},
                "position": {"grow": 0, "shrink": 0},
                "props": {
                    "text": "kWh",
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "opacity": "0.65",
                        "width": "28px",
                    },
                },
            },
            _label_node(
                "Therm",
                f"{therm:,.0f}",
                "font-livedata-entry",
                fontSize="13px",
                fontWeight="600",
                width="40px",
                minWidth="40px",
                textAlign="right",
            ),
            {
                "type": "ia.display.label",
                "meta": {"name": "ThermUnit"},
                "position": {"grow": 0, "shrink": 0},
                "props": {
                    "text": "therm",
                    "style": {
                        "classes": "font-label",
                        "fontSize": "11px",
                        "opacity": "0.65",
                        "width": "36px",
                    },
                },
            },
        ],
    }


def _linebreak_block(name: str, title: str, sites: list[tuple[str, str]], tag_path: str, tag_root_expr: str) -> dict:
    demo_avg = {"Cascade": 18.4, "Eneroi": 24.1}.get(name, 0.0)
    demo_baseline = {"Cascade": "October", "Eneroi": "—"}.get(name, "—")
    rows = []
    for i, (site, month) in enumerate(sites):
        highlight = site == "Groveport"
        rows.append(
            {
                "type": "ia.container.flex",
                "meta": {"name": f"Row{i}"},
                "props": {
                    "direction": "row",
                    "justify": "space-between",
                    "alignItems": "center",
                    "style": {
                        "gap": "8px",
                        "width": "100%",
                        "padding": "3px 0",
                        "fontWeight": "600" if highlight else "400",
                    },
                },
                "children": [
                    _label_node(
                        "Site",
                        site,
                        "font-label",
                        fontSize="13px",
                        opacity="1" if highlight else "0.85",
                    ),
                    _label_node(
                        "Month",
                        month,
                        "font-label",
                        fontSize="13px",
                        opacity="0.8",
                    ),
                ],
            }
        )
    return {
        "type": "ia.container.flex",
        "meta": {"name": f"Block{name}"},
        "position": {"grow": 0, "shrink": 0, "basis": "260px"},
        "props": {
            "direction": "column",
            "style": {
                "gap": "6px",
                "minWidth": "240px",
                "maxWidth": "320px",
                "width": "280px",
                "padding": "8px 10px",
                "classes": "kpi-coming-subcard",
                "overflow": "hidden",
            },
        },
        "children": [
            _label_node("Title", title, "font-heading", fontSize="14px", fontWeight="600"),
            {
                "type": "ia.container.flex",
                "meta": {"name": "AvgRow"},
                "props": {
                    "direction": "row",
                    "alignItems": "baseline",
                    "style": {"gap": "8px"},
                },
                "children": [
                    _label_node("AvgLbl", "Restart avg", "font-label", fontSize="12px", opacity="0.75"),
                    _label_node(
                        "AvgVal",
                        f"{demo_avg:.1f}",
                        "font-livedata-entry",
                        fontSize="20px",
                        fontWeight="600",
                    ),
                    _label_node("AvgUnit", "min", "font-label", fontSize="12px", opacity="0.7"),
                ],
            },
            _label_node(
                "Baseline",
                f"Baseline: {demo_baseline}",
                "font-label",
                fontSize="12px",
                opacity="0.8",
            ),
            _label_node("Ref", "Reference months", "font-label", fontSize="11px", opacity="0.65"),
            *rows,
        ],
    }


def _demo_yoy_series(kind: str) -> tuple[list[float], list[float], float]:
    """Seasonal demo series for YoY charts. Returns (this_year, last_year, y_max)."""
    # Relative monthly shape (peaks summer for kWh/therm intensity, flatter for prod)
    shape = [0.92, 0.88, 0.90, 0.94, 1.02, 1.10, 1.14, 1.12, 1.04, 0.98, 0.93, 0.95]
    if kind == "kWh":
        base_ty, base_ly = 560_000.0, 590_000.0
    elif kind == "therm":
        base_ty, base_ly = 26_000.0, 28_500.0
    else:  # production lb
        base_ty, base_ly = 122_000.0, 118_000.0
        shape = [0.96, 0.94, 1.00, 1.02, 1.04, 1.06, 0.98, 1.01, 1.03, 1.05, 1.02, 0.99]
    this_year = [round(base_ty * s, 0) for s in shape]
    last_year = [round(base_ly * s * 1.02, 0) for s in shape]
    y_max = max(this_year + last_year) * 1.12
    return this_year, last_year, y_max


def _stub_yoy_chart(name: str, title: str, y_title: str, *, kind: str = "kWh") -> dict:
    """Demo YoY chart — illustrative this-year vs last-year until historian feeds."""
    cats = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    this_year, last_year, y_max = _demo_yoy_series(kind)
    chart_h = 160
    apex = {
        "type": "kyvislabs.display.apexchart",
        "meta": {"name": "ChartApex"},
        "props": {
            "type": "line",
            "series": [
                {"name": "This year", "data": this_year},
                {"name": "Last year", "data": last_year},
            ],
            "options": {
                "chart": {
                    "type": "line",
                    "height": chart_h,
                    "width": "100%",
                    "animations": {"enabled": False},
                    "toolbar": {"show": False},
                    "zoom": {"enabled": False},
                    "events": _apex_events(),
                },
                "colors": ["#3D9BE9", "#A8B4C0"],
                "stroke": {"curve": "smooth", "width": [2, 2], "dashArray": [0, 6]},
                "dataLabels": {"enabled": False},
                "legend": {
                    "show": True,
                    "position": "top",
                    "fontSize": "10px",
                    "labels": {"colors": "var(--text)"},
                },
                "grid": {"borderColor": "rgba(128,128,128,0.18)", "strokeDashArray": 3},
                "markers": {"size": 0},
                "xaxis": {
                    "categories": cats,
                    "labels": {"style": {"fontSize": "9px", "colors": "var(--text)"}},
                },
                "yaxis": {
                    "title": {"text": y_title, "style": {"fontSize": "10px", "color": "var(--text)"}},
                    "min": 0,
                    "max": y_max,
                    "tickAmount": 4,
                    "labels": {"style": {"fontSize": "9px", "colors": "var(--text)"}},
                },
                "tooltip": {"enabled": True, "theme": "dark"},
            },
        },
    }
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 0, "shrink": 0, "basis": "auto"},
        "props": {
            "direction": "column",
            "style": {
                "classes": "container-card container-card-border kpi-coming-chart",
                "gap": "6px",
                "padding": "10px 12px 8px",
                "width": "100%",
                "maxWidth": "720px",
                "overflow": "hidden",
                "flexShrink": "0",
            },
        },
        "children": [
            {
                "type": "ia.container.flex",
                "meta": {"name": "Head"},
                "position": {"grow": 0, "shrink": 0},
                "props": {
                    "direction": "row",
                    "justify": "flex-start",
                    "alignItems": "center",
                    "style": {"width": "100%", "gap": "12px", "flexWrap": "wrap"},
                },
                "children": [
                    _label_node("Title", title, "font-heading", fontSize="14px", fontWeight="600"),
                    _status_chip("Status", "Demo"),
                ],
            },
            _chart_shell("ChartShell", apex, chart_h),
        ],
    }


def _coming_online_section(tag_root_expr: str) -> list[dict]:
    """Concrete placeholders from Excel Dashboard notes + metering initiative."""
    meter_rows = [_meter_area_row(a, tag_root_expr) for a in GROVEPORT_AREAS]
    return [
        {
            "type": "ia.display.label",
            "meta": {"name": "FutureHeading"},
            "props": {
                "text": "Coming online — metering & future KPIs",
                "style": {
                    "classes": "font-heading",
                    "fontSize": "15px",
                    "fontWeight": "600",
                    "marginTop": "4px",
                },
            },
        },
        {
            "type": "ia.container.flex",
            "meta": {"name": "CardMetering"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "container-card container-card-border",
                    "gap": "8px",
                    "padding": "14px 16px",
                    "width": "100%",
                },
            },
            "children": [
                _section_head("Head", "Plant metering by area", "Planned"),
                _label_node(
                    "Hint",
                    "Submeter rollout — bind area kWh / therm / H2O as meters are installed. "
                    "Coverage % on the hero tracks installed ÷ planned.",
                    "font-label",
                    fontSize="12px",
                    opacity="0.8",
                    whiteSpace="normal",
                ),
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Counts"},
                    "props": {
                        "direction": "row",
                        "style": {"gap": "20px", "marginBottom": "4px"},
                    },
                    "children": [
                        {
                            "type": "ia.container.flex",
                            "meta": {"name": "Installed"},
                            "props": {"direction": "row", "alignItems": "baseline", "style": {"gap": "6px"}},
                            "children": [
                                _label_node("L", "Installed", "font-label", fontSize="12px", opacity="0.75"),
                                _expr_label(
                                    "V",
                                    f"numberFormat(coalesce(try(if(isBadOrError(tag({tag_root_expr} + '/ComingOnline/MeteringInstalledCount')), null, "
                                    f"tag({tag_root_expr} + '/ComingOnline/MeteringInstalledCount')), null), 0), '0') + ' / ' + "
                                    f"numberFormat(coalesce(try(if(isBadOrError(tag({tag_root_expr} + '/ComingOnline/MeteringPlannedCount')), null, "
                                    f"tag({tag_root_expr} + '/ComingOnline/MeteringPlannedCount')), null), 8), '0')",
                                    fontSize="16px",
                                    fontWeight="600",
                                ),
                            ],
                        },
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "ColHeaders"},
                    "props": {
                        "direction": "row",
                        "justify": "space-between",
                        "style": {"gap": "10px", "opacity": "0.65", "paddingBottom": "2px"},
                    },
                    "children": [
                        _label_node("H1", "Area", "font-label", fontSize="11px"),
                        _label_node("H2", "Status · kWh · therm", "font-label", fontSize="11px"),
                    ],
                },
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "MeterRows"},
                    "props": {"direction": "column", "style": {"width": "100%", "gap": "0"}},
                    "children": meter_rows,
                },
            ],
        },
        {
            "type": "ia.container.flex",
            "meta": {"name": "CardLineBreak"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "container-card container-card-border",
                    "gap": "10px",
                    "padding": "14px 16px",
                    "width": "100%",
                },
            },
            "children": [
                _section_head("Head", "Line-break restart averages", "Placeholder"),
                _label_node(
                    "Hint",
                    "From Utility Tracker Dashboard notes — Cascade / Eneroi restart averages "
                    "with site baseline months. Values stay 0 until event history is wired.",
                    "font-label",
                    fontSize="12px",
                    opacity="0.8",
                    whiteSpace="normal",
                ),
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "Blocks"},
                    "props": {
                        "direction": "row",
                        "wrap": "wrap",
                        "style": {"gap": "12px", "width": "100%"},
                    },
                    "children": [
                        _linebreak_block(
                            "Cascade",
                            "Cascade",
                            CASCADE_SITES,
                            "Cascade",
                            tag_root_expr,
                        ),
                        _linebreak_block(
                            "Eneroi",
                            "Eneroi",
                            ENEROI_SITES,
                            "Eneroi",
                            tag_root_expr,
                        ),
                    ],
                },
            ],
        },
        {
            "type": "ia.container.flex",
            "meta": {"name": "CardYoy"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "container-card container-card-border",
                    "gap": "10px",
                    "padding": "14px 16px",
                    "width": "100%",
                },
            },
            "children": [
                _section_head("Head", "Year-over-year KPIs", "Backlog"),
                _label_node(
                    "Hint",
                    "Excel backlog: YoY kWh + Therm chart, and production volume YoY. "
                    "Shells use zero series until meters / historian provide monthly totals.",
                    "font-label",
                    fontSize="12px",
                    opacity="0.8",
                    whiteSpace="normal",
                ),
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "YoyCharts"},
                    "props": {
                        "direction": "row",
                        "wrap": "wrap",
                        "style": {"gap": "12px", "width": "100%"},
                    },
                    "children": [
                        _stub_yoy_chart("YoyKwh", "kWh · YoY", "kWh"),
                        _stub_yoy_chart("YoyTherm", "Therm · YoY", "therm"),
                        _stub_yoy_chart("YoyProd", "Production · YoY", "lb"),
                    ],
                },
            ],
        },
        {
            "type": "ia.container.flex",
            "meta": {"name": "CardInnovative"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "container-card container-card-border",
                    "gap": "8px",
                    "padding": "14px 16px",
                    "width": "100%",
                },
            },
            "children": [
                _section_head("Head", "Innovative", "Future"),
                _label_node(
                    "Body",
                    "Placeholder from Dashboard notes (“Add Innovative”). Reserved for future "
                    "initiative KPIs — no metrics bound yet.",
                    "font-label",
                    fontSize="13px",
                    opacity="0.85",
                    whiteSpace="normal",
                ),
                _expr_label(
                    "StatusTag",
                    f"coalesce(try(if(isBadOrError(tag({tag_root_expr} + '/ComingOnline/InnovativeStatus')), null, "
                    f"tag({tag_root_expr} + '/ComingOnline/InnovativeStatus')), null), 'Future')",
                    classes="font-label",
                    fontSize="12px",
                    opacity="0.75",
                ),
            ],
        },
    ]


def _future_card(name: str, title: str, body: str, status: str) -> dict:
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"grow": 1, "shrink": 1, "basis": "0%"},
        "props": {
            "direction": "column",
            "style": {
                "classes": "container-card container-card-border",
                "gap": "8px",
                "padding": "14px 16px",
                "minWidth": "0",
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
                "children": [
                    _label_node(
                        "Title",
                        title,
                        "font-heading",
                        fontSize="15px",
                        fontWeight="600",
                    ),
                    {
                        "type": "ia.display.label",
                        "meta": {"name": "Status"},
                        "props": {
                            "text": status,
                            "style": {
                                "classes": "font-label",
                                "fontSize": "11px",
                                "opacity": "0.75",
                                "padding": "2px 8px",
                                "borderRadius": "4px",
                                "backgroundColor": "rgba(12,123,179,0.12)",
                            },
                        },
                    },
                ],
            },
            _label_node(
                "Body",
                body,
                "font-label",
                fontSize="13px",
                opacity="0.85",
                whiteSpace="normal",
            ),
        ],
    }


def _domain_panel(
    name: str,
    subtitle: str,
    *,
    tab_index: int,
    pens: list[dict],
    body: list[dict],
) -> dict:
    """One KPI domain panel for the Option B tab container."""
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "position": {"tabIndex": tab_index},
        "props": {
            "direction": "column",
            "style": {
                "classes": "kpi-domain-panel",
                "gap": "10px",
                "padding": "12px 14px 14px",
                "width": "100%",
                "height": "100%",
                "overflowX": "hidden",
                "overflowY": "auto",
                "boxSizing": "border-box",
                "minHeight": "0",
                "justifyContent": "flex-start",
                "alignContent": "flex-start",
            },
        },
        "children": [
            _label_node(
                "Sub",
                subtitle,
                "font-label",
                fontSize="13px",
                opacity="0.8",
                whiteSpace="normal",
            ),
            {
                "type": "ia.container.flex",
                "meta": {"name": "Pens"},
                "props": {
                    "direction": "row",
                    "wrap": "wrap",
                    "style": {
                        "gap": "8px",
                        "width": "100%",
                        "alignItems": "flex-start",
                        "justifyContent": "flex-start",
                    },
                },
                "children": pens,
            },
            *body,
        ],
    }


def _chart_card(name: str, title: str, subtitle: str, chart: dict) -> dict:
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "props": {
            "direction": "column",
            "style": {
                "classes": "kpi-dashboard-chart-card",
                "gap": "4px",
                "padding": "0",
                "minWidth": "0",
                "width": "100%",
                "maxWidth": "960px",
                "overflow": "hidden",
                "flexShrink": "0",
                "alignSelf": "flex-start",
            },
        },
        "children": [
            {
                "type": "ia.container.flex",
                "meta": {"name": "Head"},
                "props": {
                    "direction": "column",
                    "style": {"gap": "2px", "width": "100%"},
                },
                "children": [
                    _label_node(
                        "Title", title, "font-heading", fontSize="15px", fontWeight="600"
                    ),
                    _label_node(
                        "Sub", subtitle, "font-label", fontSize="12px", opacity="0.75"
                    ),
                ],
            },
            chart,
        ],
    }


def _subsection(name: str, title: str, status: str, children: list[dict]) -> dict:
    return {
        "type": "ia.container.flex",
        "meta": {"name": name},
        "props": {
            "direction": "column",
            "style": {
                "classes": "kpi-domain-subsection",
                "gap": "6px",
                "padding": "10px 12px",
                "width": "100%",
                "maxWidth": "100%",
                "boxSizing": "border-box",
                "overflow": "hidden",
                "flexShrink": "0",
            },
        },
        "children": [
            _section_head("Head", title, status),
            *children,
        ],
    }


def _metering_grid(tag_root_expr: str) -> dict:
    """Compact 2-column metering placeholders under EPMS."""
    rows = [_meter_area_row(a, tag_root_expr) for a in GROVEPORT_AREAS]
    mid = (len(rows) + 1) // 2
    return {
        "type": "ia.container.flex",
        "meta": {"name": "MeterGrid"},
        "props": {
            "direction": "row",
            "wrap": "wrap",
            "alignItems": "flex-start",
            "justify": "flex-start",
            "style": {
                "gap": "24px",
                "width": "100%",
                "alignItems": "flex-start",
                "justifyContent": "flex-start",
            },
        },
        "children": [
            {
                "type": "ia.container.flex",
                "meta": {"name": "ColA"},
                "position": {"grow": 0, "shrink": 0, "basis": "420px"},
                "props": {
                    "direction": "column",
                    "style": {
                        "gap": "0",
                        "width": "420px",
                        "maxWidth": "420px",
                        "overflow": "hidden",
                        "flexShrink": "0",
                    },
                },
                "children": rows[:mid],
            },
            {
                "type": "ia.container.flex",
                "meta": {"name": "ColB"},
                "position": {"grow": 0, "shrink": 0, "basis": "420px"},
                "props": {
                    "direction": "column",
                    "style": {
                        "gap": "0",
                        "width": "420px",
                        "maxWidth": "420px",
                        "overflow": "hidden",
                        "flexShrink": "0",
                    },
                },
                "children": rows[mid:],
            },
        ],
    }


def build_overview(series: dict) -> dict:
    temp = series["temperature"]["rows"]
    kwh = series["kWh"]["rows"]
    t_cats = [r["label"] for r in temp]
    k_cats = [r["label"] for r in kwh]

    tag = "coalesce({view.params.tagRoot}, '[default]KPI/Groveport/Site')"

    # Taller charts — Option B shows one domain at a time
    chart_temp = benchmark_chart(
        name="TempChart",
        categories=t_cats,
        band_high=[r["high"] for r in temp],
        band_low=[r["low"] for r in temp],
        avg3=[r["avg3"] for r in temp],
        primary=[r["current"] for r in temp],
        primary_name="Current Month AVG",
        y_title="°F",
        height=260,
    )
    chart_kwh = benchmark_chart(
        name="KwhChart",
        categories=k_cats,
        band_high=[r["high"] for r in kwh],
        band_low=[r["low"] for r in kwh],
        avg3=[r["avg3"] for r in kwh],
        primary=[r["actual"] for r in kwh],
        primary_name="kWh Actual",
        y_title="kWh",
        height=260,
    )

    panel_epms = _domain_panel(
        "PanelEPMS",
        "Site energy — Utility Tracker kWh benchmarks and area metering rollout.",
        tab_index=0,
        pens=[
            _hero_pen(
                "PenKwh",
                "kWh (MTD)",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/EPMS/kWh')), null, tag({tag} + '/EPMS/kWh')), null), 0), '#,##0')",
                "kWh",
            ),
            _hero_pen(
                "PenKvar",
                "Reactive",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/EPMS/Kvar')), null, tag({tag} + '/EPMS/Kvar')), null), 0), '#,##0.0')",
                "kvar",
            ),
            _hero_pen(
                "PenAvg3",
                "3yr month avg",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/EPMS/Avg3Yr')), null, tag({tag} + '/EPMS/Avg3Yr')), null), 0), '#,##0')",
                "kWh",
            ),
            _hero_pen(
                "PenMeter",
                "Metering coverage",
                "'75'",
                "% areas",
            ),
        ],
        body=[
            _chart_card(
                "CardKwh",
                "kWh",
                f"Last {KWH_MONTHS} months · 7yr high/low band · 3yr AVG · actual",
                chart_kwh,
            ),
            _subsection(
                "EpmsMetering",
                "Area metering",
                "Demo",
                [
                    _label_node(
                        "Hint",
                        "Submeter rollout by area — installed count and kWh / therm MTD (demo values).",
                        "font-label",
                        fontSize="12px",
                        opacity="0.8",
                        whiteSpace="normal",
                    ),
                    {
                        "type": "ia.container.flex",
                        "meta": {"name": "Counts"},
                        "props": {
                            "direction": "row",
                            "alignItems": "baseline",
                            "style": {"gap": "6px"},
                        },
                        "children": [
                            _label_node(
                                "L", "Installed", "font-label", fontSize="12px", opacity="0.75"
                            ),
                            _label_node(
                                "V",
                                "6 / 8",
                                "font-livedata-entry",
                                fontSize="15px",
                                fontWeight="600",
                            ),
                        ],
                    },
                    _metering_grid(tag),
                ],
            ),
            _subsection(
                "EpmsYoy",
                "kWh year-over-year",
                "Demo",
                [_stub_yoy_chart("YoyKwh", "kWh · YoY", "kWh", kind="kWh")],
            ),
        ],
    )

    panel_utility = _domain_panel(
        "PanelUtility",
        "Ambient temperature benchmarks with natural gas, water, and CO₂ pens (demo utility values).",
        tab_index=1,
        pens=[
            _hero_pen(
                "PenTherm",
                "Natural Gas",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Utility/Therm')), null, tag({tag} + '/Utility/Therm')), null), 28450), '#,##0')",
                "therm",
            ),
            _hero_pen(
                "PenH2O",
                "Water",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Utility/H2O')), null, tag({tag} + '/Utility/H2O')), null), 1260), '#,##0')",
                "H2O",
            ),
            _hero_pen(
                "PenCO2",
                "CO₂",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Utility/CO2')), null, tag({tag} + '/Utility/CO2')), null), 41200), '#,##0')",
                "lb",
            ),
            _hero_pen(
                "PenTemp",
                "Outdoor Temp",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Utility/AmbientAvgF')), null, tag({tag} + '/Utility/AmbientAvgF')), null), 0), '0')",
                "°F",
            ),
        ],
        body=[
            _chart_card(
                "CardTemp",
                "Temperature",
                f"Last {TEMP_MONTHS} months · 7yr high/low band · 3yr AVG · current month AVG",
                chart_temp,
            ),
            _subsection(
                "UtilityYoy",
                "Therm year-over-year",
                "Demo",
                [_stub_yoy_chart("YoyTherm", "Therm · YoY", "therm", kind="therm")],
            ),
        ],
    )

    panel_production = _domain_panel(
        "PanelProduction",
        "Volume and intensity pens, YoY comparison, and Cascade / Eneroi line-break restart averages.",
        tab_index=2,
        pens=[
            _hero_pen(
                "PenProd",
                "Production",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Production/ProdVol')), null, tag({tag} + '/Production/ProdVol')), null), 0), '#,##0')",
                "lb",
            ),
            _hero_pen(
                "PenProd7d",
                "7d avg volume",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Production/ProdVolAvg7d')), null, tag({tag} + '/Production/ProdVolAvg7d')), null), 0), '#,##0')",
                "lb",
            ),
            _hero_pen(
                "PenIntensity",
                "Energy intensity",
                f"numberFormat(coalesce(try(if(isBadOrError(tag({tag} + '/Production/kWhPerLb')), null, tag({tag} + '/Production/kWhPerLb')), null), 0), '0.0')",
                "kWh/lb",
            ),
        ],
        body=[
            _subsection(
                "ProdYoy",
                "Production year-over-year",
                "Demo",
                [_stub_yoy_chart("YoyProd", "Production · YoY", "lb", kind="prod")],
            ),
            _subsection(
                "ProdLineBreak",
                "Line-break restart averages",
                "Demo",
                [
                    _label_node(
                        "Hint",
                        "Utility Tracker baselines — Cascade (Groveport October) and Eneroi site months. Restart avg is demo.",
                        "font-label",
                        fontSize="12px",
                        opacity="0.8",
                        whiteSpace="normal",
                    ),
                    {
                        "type": "ia.container.flex",
                        "meta": {"name": "Blocks"},
                        "props": {
                            "direction": "row",
                            "wrap": "wrap",
                            "style": {"gap": "12px", "width": "100%"},
                        },
                        "children": [
                            _linebreak_block(
                                "Cascade", "Cascade", CASCADE_SITES, "Cascade", tag
                            ),
                            _linebreak_block(
                                "Eneroi", "Eneroi", ENEROI_SITES, "Eneroi", tag
                            ),
                        ],
                    },
                ],
            ),
            _subsection(
                "ProdInnovative",
                "Innovative",
                "Demo",
                [
                    _label_node(
                        "Body",
                        "Future initiative KPIs — demo rollup until programs are instrumented.",
                        "font-label",
                        fontSize="13px",
                        opacity="0.85",
                        whiteSpace="normal",
                    ),
                    {
                        "type": "ia.container.flex",
                        "meta": {"name": "InnovMetrics"},
                        "props": {
                            "direction": "row",
                            "wrap": "wrap",
                            "style": {"gap": "16px", "width": "100%", "marginTop": "4px"},
                        },
                        "children": [
                            {
                                "type": "ia.container.flex",
                                "meta": {"name": "Init"},
                                "props": {
                                    "direction": "column",
                                    "style": {"gap": "2px", "minWidth": "120px"},
                                },
                                "children": [
                                    _label_node(
                                        "L", "Active initiatives", "font-label", fontSize="11px", opacity="0.7"
                                    ),
                                    _label_node(
                                        "V",
                                        "3",
                                        "font-livedata-entry",
                                        fontSize="22px",
                                        fontWeight="600",
                                    ),
                                ],
                            },
                            {
                                "type": "ia.container.flex",
                                "meta": {"name": "Sav"},
                                "props": {
                                    "direction": "column",
                                    "style": {"gap": "2px", "minWidth": "160px"},
                                },
                                "children": [
                                    _label_node(
                                        "L", "Est. annual savings", "font-label", fontSize="11px", opacity="0.7"
                                    ),
                                    {
                                        "type": "ia.container.flex",
                                        "meta": {"name": "Row"},
                                        "props": {
                                            "direction": "row",
                                            "alignItems": "baseline",
                                            "style": {"gap": "6px"},
                                        },
                                        "children": [
                                            _label_node(
                                                "V",
                                                "128,400",
                                                "font-livedata-entry",
                                                fontSize="22px",
                                                fontWeight="600",
                                            ),
                                            _label_node(
                                                "U", "kWh", "font-label", fontSize="12px", opacity="0.7"
                                            ),
                                        ],
                                    },
                                ],
                            },
                            {
                                "type": "ia.container.flex",
                                "meta": {"name": "Pilot"},
                                "props": {
                                    "direction": "column",
                                    "style": {"gap": "2px", "minWidth": "200px", "flex": "1"},
                                },
                                "children": [
                                    _label_node(
                                        "L", "Pilot areas", "font-label", fontSize="11px", opacity="0.7"
                                    ),
                                    _label_node(
                                        "V",
                                        "Freezer · Dock · Machine Room",
                                        "font-label",
                                        fontSize="14px",
                                        fontWeight="600",
                                    ),
                                ],
                            },
                        ],
                    },
                ],
            ),
        ],
    )

    return {
        "custom": {},
        "params": {
            "tagRoot": "[default]KPI/Groveport/Site",
        },
        "propConfig": {},
        "props": {"defaultSize": {"width": 1400, "height": 900}},
        "root": {
            "type": "ia.container.flex",
            "meta": {"name": "root"},
            "props": {
                "direction": "column",
                "style": {
                    "classes": "bg-page kpi-dashboard-page",
                    "gap": "12px",
                    "padding": "16px 20px 20px",
                    "overflow": "hidden",
                    "minHeight": "0",
                    "height": "100%",
                },
            },
            "children": [
                {
                    "type": "ia.container.flex",
                    "meta": {"name": "TitleBlock"},
                    "position": {"grow": 0, "shrink": 0},
                    "props": {
                        "direction": "column",
                        "style": {"gap": "4px", "width": "100%"},
                    },
                    "children": [
                        _label_node(
                            "Title",
                            "Groveport — Site Dashboard",
                            "font-heading",
                            fontSize="22px",
                            fontWeight="700",
                        ),
                        _label_node(
                            "Subtitle",
                            "EPMS · Utility · Production — switch domains with the tabs below.",
                            "font-label",
                            fontSize="13px",
                            opacity="0.8",
                            whiteSpace="normal",
                        ),
                    ],
                },
                {
                    "type": "ia.container.tab",
                    "meta": {"name": "DomainTabs"},
                    "position": {"grow": 1, "shrink": 1, "basis": "0%"},
                    "props": {
                        "currentTabIndex": 0,
                        "tabs": ["EPMS", "Utility", "Production"],
                        "tabSize": {"width": 132, "height": 40},
                        "style": {
                            "classes": "kpi-domain-tabs",
                            "flex": "1 1 0%",
                            "minHeight": "0",
                            "height": "100%",
                            "width": "100%",
                            "overflow": "hidden",
                        },
                    },
                    "children": [panel_epms, panel_utility, panel_production],
                },
            ],
        },
    }


def main() -> None:
    series = extract_series()
    SERIES_OUT.write_text(json.dumps(series, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {SERIES_OUT} temp={len(series['temperature']['rows'])} "
        f"kWh={len(series['kWh']['rows'])}"
    )
    overview = build_overview(series)
    OVERVIEW.write_text(json.dumps(overview, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OVERVIEW}")


if __name__ == "__main__":
    main()
