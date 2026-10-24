# Custom report builder engine (Production KPIs, Alarms, ... any source in the catalog).
# Written by .cursor/tasks/report-builder/build.py (source: reports_library.py there) - edit the builder, not this copy.
# Design: docs/report-builder.md.
#
# Catalog   [default]_Config/Reports/Catalog (Document tag; FALLBACK below is the builder's copy, used when the tag is
#           missing / older). Sources declare measures, scope tree, breakdowns, filters, sections, Top N lists.
# Engine    run(session, definition) -> {ok, meta, sections:[{type, title, note, cards | charts | columns+rows}]}.
#           Permission (Reports/Use + the source's own row) is checked here on the gateway; the username always comes
#           from session.props.auth.user. Time buckets (hour / shift / day / week / total) and the shift schedule
#           (A 07-15, B 15-23, C 23-07) are built here; each source has one fetcher (FETCHERS) that returns per bucket x
#           scope records keyed by the catalog 'field' names.
# Fetchers  production: demo generator shared.ProductionMetrics.l1 (the Production Overview dashboard's own code) per
#           day / shift / unit, replaced per time bucket by SQL historian data (FCM tag history) where the history
#           covers the bucket (each value keeps its source internally; the outputs carry no data-source labels -
#           user 2026-10-13: "get rid of all the demo data stuff").
#           alarms: alarm journal aggregates (named queries Reports/Alarms/*) + system.alarm.queryStatus for "now".
# Output    PDF = Reporting resource Reports/CustomReport (one generic layout; payload JSON -> reportData below),
#           Excel = system.dataset.toExcel (one sheet per section), CSV = one file, or a zip of one per section.
# Templates dbo.report_template via Reports/Templates/* (personal / shared; owner or Reports/ManageTemplates edits).

import json as _json
from java.lang import Throwable

LOG = system.util.getLogger("shared.Reports")
PROJECT = "BH"
NQ = "Reports/"
CATALOG_TAG = "[default]_Config/Reports/Catalog"
DEPLOY_TAG = "[default]_Config/DemoEnterpriseNav"      # deployment switch: True = enterprise demo, else local Groveport
POPUP_ID = "reportBuilder"
POPUP_VIEW = "01_Popups/Reports/ReportBuilder"
REPORT_PATH = "Reports/CustomReport"
FALLBACK = _json.loads(r'''{"presets": [{"def": {"breakdown": "day", "measures": ["activations", "highPriority", "avgAck", "avgClear"], "scope": ["all"], "sections": [{"on": true, "type": "cards"}, {"n": 10, "on": true, "orderBy": "count", "topN": "alarms", "type": "topn"}, {"on": true, "type": "trend"}, {"on": false, "type": "table"}], "shifts": [], "source": "alarms", "time": {"preset": "last7"}, "title": "Top Alarms - Last 7 Days"}, "detail": "Last 7 Days", "id": "topAlarms", "label": "Top Alarms"}, {"def": {"breakdown": "hour", "measures": ["zatAvg", "zatMin", "zatMax"], "scope": ["all"], "sections": [{"on": true, "type": "cards"}, {"n": 10, "on": true, "orderBy": "avg", "topN": "warmest", "type": "topn"}, {"on": true, "type": "trend"}], "shifts": [], "source": "zoneTemps", "time": {"preset": "lastShift"}, "title": "Zone Temperatures - Last Shift"}, "detail": "Last Shift, By Hour", "id": "zoneTempsShift", "label": "Zone Temps"}, {"def": {"breakdown": "none", "measures": ["runHrs", "starts", "totHrs"], "scope": ["all"], "sections": [{"on": true, "type": "cards"}, {"n": 15, "on": true, "orderBy": "hours", "topN": "runHours", "type": "topn"}], "shifts": [], "source": "runtime", "time": {"preset": "last7"}, "title": "Equipment Run Hours - Last 7 Days"}, "detail": "Last 7 Days", "id": "runHours7", "label": "Run Hours"}, {"def": {"breakdown": "week", "measures": ["taken", "returned", "oosHours", "outNow"], "scope": ["all"], "sections": [{"on": true, "type": "cards"}, {"n": 10, "on": true, "orderBy": "hours", "topN": "devices", "type": "topn"}, {"on": true, "type": "records"}], "shifts": [], "source": "oos", "time": {"preset": "last30"}, "title": "Out Of Service - Last 30 Days"}, "detail": "Last 30 Days", "id": "oos30", "label": "Out Of Service"}, {"def": {"breakdown": "day", "measures": ["rate"], "scope": ["line"], "sections": [{"on": true, "type": "cards"}, {"on": true, "type": "trend"}, {"on": true, "type": "table"}], "shifts": [], "source": "production", "time": {"preset": "last7"}, "title": "LBS/HR - Last 7 Days"}, "detail": "Last 7 Days", "id": "lbsHrOnly", "label": "LBS/HR Only"}, {"def": {"breakdown": "none", "measures": ["rate", "vsTarget", "throughput", "oee", "availability", "performance", "quality", "yield", "reject", "uptime", "runTime", "downtime", "downtimeEvents"], "scope": ["line"], "sections": [{"on": true, "type": "cards"}, {"on": true, "type": "table"}, {"n": 5, "on": true, "orderBy": "minutes", "topN": "downtime", "type": "topn"}], "shifts": ["B"], "source": "production", "time": {"preset": "yesterday"}, "title": "Shift B Summary - Yesterday"}, "detail": "Yesterday, Shift B", "id": "singleShift", "label": "Single Shift Summary"}], "sectionTypes": [{"id": "cards", "label": "Summary Cards"}, {"id": "trend", "label": "Trend Chart"}, {"id": "table", "label": "Table"}, {"id": "shifts", "label": "Shift Comparison"}, {"id": "topn", "label": "Top N"}, {"id": "records", "label": "Event List"}, {"id": "notes", "label": "Notes"}], "sources": [{"breakdowns": [{"id": "none", "label": "Total (No Breakdown)"}, {"id": "hour", "label": "By Hour"}, {"id": "shift", "label": "By Shift"}, {"id": "day", "label": "By Day"}, {"id": "week", "label": "By Week"}], "defaultBreakdown": "day", "defaultMeasures": ["activations", "highPriority", "avgAck", "avgClear"], "defaultScope": ["all"], "defaultSections": ["cards", "topn", "table"], "description": "Alarm Counts, Response Times And Top Offenders By Area And Device.", "fetcher": "alarms", "filters": [{"id": "shifts", "label": "Shifts", "options": [{"label": "Shift A (07:00-15:00)", "value": "A"}, {"label": "Shift B (15:00-23:00)", "value": "B"}, {"label": "Shift C (23:00-07:00)", "value": "C"}]}, {"id": "priorities", "label": "Priorities", "options": [{"label": "Diagnostic", "value": "0"}, {"label": "Low", "value": "1"}, {"label": "Medium", "value": "2"}, {"label": "High", "value": "3"}, {"label": "Critical", "value": "4"}]}], "groups": [{"id": "activity", "label": "Activity"}, {"id": "response", "label": "Response"}, {"id": "current", "label": "Current Status"}], "icon": "material/notifications", "id": "alarms", "label": "Alarm History", "measures": [{"agg": "sum", "decimals": 0, "field": "activations", "group": "activity", "id": "activations", "label": "Alarm Activations", "unit": "alarms"}, {"agg": "sum", "decimals": 0, "field": "highCount", "group": "activity", "id": "highPriority", "label": "High / Critical Activations", "unit": "alarms"}, {"agg": "ratio", "decimals": 1, "den": "activations", "field": "", "group": "response", "id": "ackedPct", "label": "Acknowledged", "num": "acked", "scale": 100.0, "unit": "%"}, {"agg": "ratio", "decimals": 1, "den": "acked", "field": "", "group": "response", "id": "avgAck", "label": "Avg Time To Ack", "num": "ackSec", "scale": 0.016666666666666666, "unit": "min"}, {"agg": "ratio", "decimals": 1, "den": "cleared", "field": "", "group": "response", "id": "avgClear", "label": "Avg Time To Clear", "num": "clrSec", "scale": 0.016666666666666666, "unit": "min"}, {"agg": "max", "decimals": 1, "field": "clrMaxMin", "group": "response", "id": "maxClear", "label": "Longest Active", "unit": "min"}, {"agg": "sum", "decimals": 0, "field": "clrMin", "group": "response", "id": "totalActive", "label": "Total Active Time", "unit": "min"}, {"agg": "last", "current": true, "decimals": 0, "field": "activeNow", "group": "current", "id": "activeNow", "label": "Active Now", "unit": "alarms"}, {"agg": "last", "current": true, "decimals": 0, "field": "unackedNow", "group": "current", "id": "unackedNow", "label": "Unacknowledged Now", "unit": "alarms"}], "meta": "Alarm Journal \u00b7 Since 07/25/2026", "permission": "Reports/Alarms", "records": true, "scope": [{"id": "all", "label": "All Areas", "level": "all", "parent": ""}], "scopeLevels": [{"id": "all", "label": "All"}, {"id": "area", "label": "Area"}, {"id": "device", "label": "Device"}], "scopeMulti": true, "scopeOptions": "dynamic", "sections": ["cards", "trend", "table", "shifts", "topn", "records", "notes"], "topN": [{"id": "alarms", "label": "Top Alarms", "orderBy": [{"label": "Count", "value": "count"}, {"label": "Total Active Time", "value": "duration"}, {"label": "Avg Time To Ack", "value": "ack"}]}, {"id": "devices", "label": "Top Devices", "orderBy": [{"label": "Count", "value": "count"}, {"label": "Total Active Time", "value": "duration"}]}, {"id": "areas", "label": "Top Areas", "orderBy": [{"label": "Count", "value": "count"}, {"label": "Total Active Time", "value": "duration"}]}]}, {"breakdowns": [{"id": "none", "label": "Total (No Breakdown)"}, {"id": "hour", "label": "By Hour"}, {"id": "shift", "label": "By Shift"}, {"id": "day", "label": "By Day"}, {"id": "week", "label": "By Week"}], "defaultBreakdown": "hour", "defaultMeasures": ["zatAvg", "zatMin", "zatMax"], "defaultScope": ["all"], "defaultSections": ["cards", "topn", "trend"], "defaultTime": "today", "description": "Average, Low And High Zone Air Temperature For Every Evaporator (CG) Unit.", "fetcher": "history", "filters": [{"id": "shifts", "label": "Shifts", "options": [{"label": "Shift A (07:00-15:00)", "value": "A"}, {"label": "Shift B (15:00-23:00)", "value": "B"}, {"label": "Shift C (23:00-07:00)", "value": "C"}]}], "groups": [{"id": "temp", "label": "Zone Air Temperature"}], "historyRoot": "[default]Boars_Head/GrovePort/", "icon": "material/ac_unit", "id": "zoneTemps", "label": "Zone Temperatures", "measures": [{"agg": "avg", "decimals": 1, "field": "zatAvg", "group": "temp", "hist": {"member": "ZAT/Val", "mode": "avg"}, "id": "zatAvg", "label": "Avg Zone Air Temp", "unit": "\u00b0F"}, {"agg": "min", "decimals": 1, "field": "zatMin", "group": "temp", "hist": {"member": "ZAT/Val", "mode": "min"}, "id": "zatMin", "label": "Lowest Zone Air Temp", "unit": "\u00b0F"}, {"agg": "max", "decimals": 1, "field": "zatMax", "group": "temp", "hist": {"member": "ZAT/Val", "mode": "max"}, "id": "zatMax", "label": "Highest Zone Air Temp", "unit": "\u00b0F"}, {"agg": "max", "decimals": 1, "field": "zatSpread", "group": "temp", "hist": {"member": "ZAT/Val", "mode": "spread"}, "id": "zatSpread", "label": "Temperature Swing (High - Low)", "unit": "\u00b0F"}], "meta": "Historian \u00b7 19 Units", "permission": "Reports/ZoneTemps", "scope": [{"id": "all", "label": "All Units", "level": "all", "parent": ""}, {"id": "area:Freezer", "label": "Freezer", "level": "area", "parent": "all"}, {"id": "dev:Freezer/CG-A1", "kind": "", "label": "CG-A1", "level": "device", "parent": "area:Freezer", "path": "Freezer/Utility/CG-A1"}, {"id": "dev:Freezer/CG-A2", "kind": "", "label": "CG-A2", "level": "device", "parent": "area:Freezer", "path": "Freezer/Utility/CG-A2"}, {"id": "area:SuperChill", "label": "SuperChill", "level": "area", "parent": "all"}, {"id": "dev:SuperChill/CG-B1", "kind": "", "label": "CG-B1", "level": "device", "parent": "area:SuperChill", "path": "SuperChill/Utility/CG-B1"}, {"id": "dev:SuperChill/CG-B2", "kind": "", "label": "CG-B2", "level": "device", "parent": "area:SuperChill", "path": "SuperChill/Utility/CG-B2"}, {"id": "area:Club", "label": "Club", "level": "area", "parent": "all"}, {"id": "dev:Club/CG-C1", "kind": "", "label": "CG-C1", "level": "device", "parent": "area:Club", "path": "Club/Utility/CG-C1"}, {"id": "area:Palletizing", "label": "Palletizing", "level": "area", "parent": "all"}, {"id": "dev:Palletizing/CG-D1", "kind": "", "label": "CG-D1", "level": "device", "parent": "area:Palletizing", "path": "Palletizing/Utility/CG-D1"}, {"id": "area:East PH", "label": "East PH", "level": "area", "parent": "all"}, {"id": "dev:East PH/CG-E1", "kind": "", "label": "CG-E1", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E1"}, {"id": "dev:East PH/CG-E2", "kind": "", "label": "CG-E2", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E2"}, {"id": "dev:East PH/CG-E3", "kind": "", "label": "CG-E3", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E3"}, {"id": "dev:East PH/CG-E4", "kind": "", "label": "CG-E4", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E4"}, {"id": "area:West PH", "label": "West PH", "level": "area", "parent": "all"}, {"id": "dev:West PH/CG-F1", "kind": "", "label": "CG-F1", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F1"}, {"id": "dev:West PH/CG-F2", "kind": "", "label": "CG-F2", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F2"}, {"id": "dev:West PH/CG-F3", "kind": "", "label": "CG-F3", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F3"}, {"id": "dev:West PH/CG-F4", "kind": "", "label": "CG-F4", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F4"}, {"id": "area:Dock", "label": "Dock", "level": "area", "parent": "all"}, {"id": "dev:Dock/CG-G1", "kind": "", "label": "CG-G1", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G1"}, {"id": "dev:Dock/CG-G2", "kind": "", "label": "CG-G2", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G2"}, {"id": "dev:Dock/CG-G3", "kind": "", "label": "CG-G3", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G3"}, {"id": "dev:Dock/CG-G4", "kind": "", "label": "CG-G4", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G4"}, {"id": "dev:Dock/CG-G5", "kind": "", "label": "CG-G5", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G5"}], "scopeLevels": [{"id": "all", "label": "All"}, {"id": "area", "label": "Area"}, {"id": "device", "label": "Device"}], "scopeMulti": true, "sections": ["cards", "trend", "table", "shifts", "topn", "notes"], "topN": [{"dir": "desc", "id": "warmest", "label": "Warmest Units", "measure": "zatAvg", "orderBy": [{"label": "Avg Temp", "value": "avg"}]}, {"dir": "asc", "id": "coldest", "label": "Coldest Units", "measure": "zatAvg", "orderBy": [{"label": "Avg Temp", "value": "avg"}]}, {"dir": "desc", "id": "swing", "label": "Largest Temperature Swing", "measure": "zatSpread", "orderBy": [{"label": "Swing", "value": "spread"}]}]}, {"breakdowns": [{"id": "none", "label": "Total (No Breakdown)"}, {"id": "hour", "label": "By Hour"}, {"id": "shift", "label": "By Shift"}, {"id": "day", "label": "By Day"}, {"id": "week", "label": "By Week"}], "defaultBreakdown": "hour", "defaultMeasures": ["sucP", "disP", "amps", "runHrs"], "defaultScope": ["all"], "defaultSections": ["cards", "table", "trend"], "defaultTime": "today", "description": "Suction And Discharge Pressure, Amps, kW And Run Hours Per Compressor.", "fetcher": "history", "filters": [{"id": "shifts", "label": "Shifts", "options": [{"label": "Shift A (07:00-15:00)", "value": "A"}, {"label": "Shift B (15:00-23:00)", "value": "B"}, {"label": "Shift C (23:00-07:00)", "value": "C"}]}], "groups": [{"id": "press", "label": "Pressures"}, {"id": "power", "label": "Power"}, {"id": "run", "label": "Runtime"}], "historyRoot": "[default]Boars_Head/GrovePort/", "icon": "material/settings", "id": "compressors", "label": "Compressors", "measures": [{"agg": "avg", "decimals": 1, "field": "sucP", "group": "press", "hist": {"member": "Comp/SucP", "mode": "avg"}, "id": "sucP", "label": "Avg Suction Pressure", "unit": "psig"}, {"agg": "avg", "decimals": 1, "field": "disP", "group": "press", "hist": {"member": "Comp/DisP", "mode": "avg"}, "id": "disP", "label": "Avg Discharge Pressure", "unit": "psig"}, {"agg": "max", "decimals": 1, "field": "disPMax", "group": "press", "hist": {"member": "Comp/DisP", "mode": "max"}, "id": "disPMax", "label": "Highest Discharge Pressure", "unit": "psig"}, {"agg": "avg", "decimals": 1, "field": "amps", "group": "power", "hist": {"member": "Comp/Amps", "mode": "avg"}, "id": "amps", "label": "Avg Motor Amps", "unit": "A"}, {"agg": "max", "decimals": 1, "field": "ampsMax", "group": "power", "hist": {"member": "Comp/Amps", "mode": "max"}, "id": "ampsMax", "label": "Peak Motor Amps", "unit": "A"}, {"agg": "avg", "decimals": 1, "field": "kw", "group": "power", "hist": {"member": "Comp/KW", "mode": "avg"}, "id": "kw", "label": "Avg kW", "unit": "kW"}, {"agg": "sum", "decimals": 1, "field": "runHrs", "group": "run", "hist": {"cap": 1.05, "member": "Comp/TotalRuntime", "mode": "delta"}, "id": "runHrs", "label": "Run Hours In Period", "unit": "h"}, {"agg": "sum", "decimals": 0, "field": "totHrs", "group": "run", "hist": {"member": "Comp/TotalRuntime", "mode": "last"}, "id": "totHrs", "label": "Total Run Hours (Meter)", "unit": "h"}], "meta": "Historian \u00b7 5 Compressors", "permission": "Reports/Compressors", "scope": [{"id": "all", "label": "All Compressors", "level": "all", "parent": ""}, {"id": "area:Machine Room", "label": "Machine Room", "level": "area", "parent": "all"}, {"id": "dev:Machine Room/COMP 1", "kind": "", "label": "Comp 1", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Compressors/COMP 1"}, {"id": "dev:Machine Room/COMP 4", "kind": "", "label": "Comp 4", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Compressors/COMP 4"}, {"id": "dev:Machine Room/COMP 5", "kind": "", "label": "Comp 5", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Compressors/COMP 5"}, {"id": "dev:Machine Room/COMP 6", "kind": "", "label": "Comp 6", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Compressors/COMP 6"}, {"id": "dev:Machine Room/COMP 7", "kind": "", "label": "Comp 7", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Compressors/COMP 7"}], "scopeLevels": [{"id": "all", "label": "All"}, {"id": "area", "label": "Area"}, {"id": "device", "label": "Device"}], "scopeMulti": true, "sections": ["cards", "trend", "table", "shifts", "topn", "notes"], "topN": [{"dir": "desc", "id": "runHours", "label": "Most Run Hours", "measure": "runHrs", "orderBy": [{"label": "Run Hours", "value": "hours"}]}, {"dir": "desc", "id": "amps", "label": "Highest Peak Amps", "measure": "ampsMax", "orderBy": [{"label": "Peak Amps", "value": "amps"}]}]}, {"breakdowns": [{"id": "none", "label": "Total (No Breakdown)"}, {"id": "hour", "label": "By Hour"}, {"id": "shift", "label": "By Shift"}, {"id": "day", "label": "By Day"}, {"id": "week", "label": "By Week"}], "defaultBreakdown": "none", "defaultMeasures": ["runHrs", "starts"], "defaultScope": ["all"], "defaultSections": ["cards", "topn", "table"], "defaultTime": "last7", "description": "Run Hours And Starts For Pumps, Condenser Fans And Evaporator Fans.", "fetcher": "history", "filters": [{"id": "shifts", "label": "Shifts", "options": [{"label": "Shift A (07:00-15:00)", "value": "A"}, {"label": "Shift B (15:00-23:00)", "value": "B"}, {"label": "Shift C (23:00-07:00)", "value": "C"}]}], "groups": [{"id": "run", "label": "Runtime"}, {"id": "starts", "label": "Starts"}], "historyRoot": "[default]Boars_Head/GrovePort/", "icon": "material/timer", "id": "runtime", "label": "Equipment Runtime", "measures": [{"agg": "sum", "decimals": 1, "field": "runHrs", "group": "run", "hist": {"cap": 1.05, "members": {"fans": "FansRunTime/Val_TotRunHrs", "motor": "RunTime/Val_TotRunHrs"}, "mode": "delta"}, "id": "runHrs", "label": "Run Hours In Period", "unit": "h"}, {"agg": "sum", "decimals": 0, "field": "totHrs", "group": "run", "hist": {"members": {"fans": "FansRunTime/Val_TotRunHrs", "motor": "RunTime/Val_TotRunHrs"}, "mode": "last"}, "id": "totHrs", "label": "Total Run Hours (Meter)", "unit": "h"}, {"agg": "sum", "decimals": 0, "field": "starts", "group": "starts", "hist": {"cap": 120, "members": {"fans": "FansRunTime/Val_Starts", "motor": "RunTime/Val_Starts"}, "mode": "delta"}, "id": "starts", "label": "Starts In Period", "unit": "starts"}, {"agg": "sum", "decimals": 0, "field": "totStarts", "group": "starts", "hist": {"members": {"fans": "FansRunTime/Val_Starts", "motor": "RunTime/Val_Starts"}, "mode": "last"}, "id": "totStarts", "label": "Total Starts (Meter)", "unit": "starts"}], "meta": "Historian \u00b7 30 Devices", "permission": "Reports/Runtime", "scope": [{"id": "all", "label": "All Equipment", "level": "all", "parent": ""}, {"id": "area:Machine Room", "label": "Machine Room", "level": "area", "parent": "all"}, {"id": "dev:Machine Room/HTLR-Pump 1", "kind": "motor", "label": "HTLR-Pump 1", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Pumps/HTLR-Pump 1"}, {"id": "dev:Machine Room/HTLR-Pump 2", "kind": "motor", "label": "HTLR-Pump 2", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Pumps/HTLR-Pump 2"}, {"id": "dev:Machine Room/LTLR-Pump 1", "kind": "motor", "label": "LTLR-Pump 1", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Pumps/LTLR-Pump 1"}, {"id": "dev:Machine Room/LTLR-Pump 2", "kind": "motor", "label": "LTLR-Pump 2", "level": "device", "parent": "area:Machine Room", "path": "Machine Room/Pumps/LTLR-Pump 2"}, {"id": "area:Condensers", "label": "Condensers", "level": "area", "parent": "all"}, {"id": "dev:Condensers/Sump Pump 1", "kind": "motor", "label": "Sump Pump 1", "level": "device", "parent": "area:Condensers", "path": "Condensers/Pumps/Sump Pump 1"}, {"id": "dev:Condensers/Sump Pump 2", "kind": "motor", "label": "Sump Pump 2", "level": "device", "parent": "area:Condensers", "path": "Condensers/Pumps/Sump Pump 2"}, {"id": "dev:Condensers/Sump Pump 3", "kind": "motor", "label": "Sump Pump 3", "level": "device", "parent": "area:Condensers", "path": "Condensers/Pumps/Sump Pump 3"}, {"id": "dev:Condensers/EC-1A Fan 1", "kind": "motor", "label": "EC-1A Fan 1", "level": "device", "parent": "area:Condensers", "path": "Condensers/Condensers/EC-1A/Fan 1"}, {"id": "dev:Condensers/EC-1A Fan 2", "kind": "motor", "label": "EC-1A Fan 2", "level": "device", "parent": "area:Condensers", "path": "Condensers/Condensers/EC-1A/Fan 2"}, {"id": "dev:Condensers/EC-1B Fan 1", "kind": "motor", "label": "EC-1B Fan 1", "level": "device", "parent": "area:Condensers", "path": "Condensers/Condensers/EC-1B/Fan 1"}, {"id": "dev:Condensers/EC-1B Fan 2", "kind": "motor", "label": "EC-1B Fan 2", "level": "device", "parent": "area:Condensers", "path": "Condensers/Condensers/EC-1B/Fan 2"}, {"id": "area:Freezer", "label": "Freezer", "level": "area", "parent": "all"}, {"id": "dev:Freezer/CG-A1 Fans", "kind": "fans", "label": "CG-A1 Fans", "level": "device", "parent": "area:Freezer", "path": "Freezer/Utility/CG-A1"}, {"id": "dev:Freezer/CG-A2 Fans", "kind": "fans", "label": "CG-A2 Fans", "level": "device", "parent": "area:Freezer", "path": "Freezer/Utility/CG-A2"}, {"id": "area:SuperChill", "label": "SuperChill", "level": "area", "parent": "all"}, {"id": "dev:SuperChill/CG-B1 Fans", "kind": "fans", "label": "CG-B1 Fans", "level": "device", "parent": "area:SuperChill", "path": "SuperChill/Utility/CG-B1"}, {"id": "dev:SuperChill/CG-B2 Fans", "kind": "fans", "label": "CG-B2 Fans", "level": "device", "parent": "area:SuperChill", "path": "SuperChill/Utility/CG-B2"}, {"id": "area:Club", "label": "Club", "level": "area", "parent": "all"}, {"id": "dev:Club/CG-C1 Fans", "kind": "fans", "label": "CG-C1 Fans", "level": "device", "parent": "area:Club", "path": "Club/Utility/CG-C1"}, {"id": "area:Palletizing", "label": "Palletizing", "level": "area", "parent": "all"}, {"id": "dev:Palletizing/CG-D1 Fans", "kind": "fans", "label": "CG-D1 Fans", "level": "device", "parent": "area:Palletizing", "path": "Palletizing/Utility/CG-D1"}, {"id": "area:East PH", "label": "East PH", "level": "area", "parent": "all"}, {"id": "dev:East PH/CG-E1 Fans", "kind": "fans", "label": "CG-E1 Fans", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E1"}, {"id": "dev:East PH/CG-E2 Fans", "kind": "fans", "label": "CG-E2 Fans", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E2"}, {"id": "dev:East PH/CG-E3 Fans", "kind": "fans", "label": "CG-E3 Fans", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E3"}, {"id": "dev:East PH/CG-E4 Fans", "kind": "fans", "label": "CG-E4 Fans", "level": "device", "parent": "area:East PH", "path": "East PH/Utility/CG-E4"}, {"id": "area:West PH", "label": "West PH", "level": "area", "parent": "all"}, {"id": "dev:West PH/CG-F1 Fans", "kind": "fans", "label": "CG-F1 Fans", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F1"}, {"id": "dev:West PH/CG-F2 Fans", "kind": "fans", "label": "CG-F2 Fans", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F2"}, {"id": "dev:West PH/CG-F3 Fans", "kind": "fans", "label": "CG-F3 Fans", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F3"}, {"id": "dev:West PH/CG-F4 Fans", "kind": "fans", "label": "CG-F4 Fans", "level": "device", "parent": "area:West PH", "path": "West PH/Utility/CG-F4"}, {"id": "area:Dock", "label": "Dock", "level": "area", "parent": "all"}, {"id": "dev:Dock/CG-G1 Fans", "kind": "fans", "label": "CG-G1 Fans", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G1"}, {"id": "dev:Dock/CG-G2 Fans", "kind": "fans", "label": "CG-G2 Fans", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G2"}, {"id": "dev:Dock/CG-G3 Fans", "kind": "fans", "label": "CG-G3 Fans", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G3"}, {"id": "dev:Dock/CG-G4 Fans", "kind": "fans", "label": "CG-G4 Fans", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G4"}, {"id": "dev:Dock/CG-G5 Fans", "kind": "fans", "label": "CG-G5 Fans", "level": "device", "parent": "area:Dock", "path": "Dock/Utility/CG-G5"}], "scopeLevels": [{"id": "all", "label": "All"}, {"id": "area", "label": "Area"}, {"id": "device", "label": "Device"}], "scopeMulti": true, "sections": ["cards", "trend", "table", "shifts", "topn", "notes"], "topN": [{"dir": "desc", "id": "runHours", "label": "Most Run Hours", "measure": "runHrs", "orderBy": [{"label": "Run Hours", "value": "hours"}]}, {"dir": "desc", "id": "starts", "label": "Most Starts", "measure": "starts", "orderBy": [{"label": "Starts", "value": "starts"}]}]}, {"breakdowns": [{"id": "none", "label": "Total (No Breakdown)"}, {"id": "hour", "label": "By Hour"}, {"id": "shift", "label": "By Shift"}, {"id": "day", "label": "By Day"}, {"id": "week", "label": "By Week"}], "defaultBreakdown": "day", "defaultMeasures": ["taken", "returned", "oosHours", "outNow"], "defaultScope": ["all"], "defaultSections": ["cards", "topn", "records"], "description": "Who Took Which Device Out Of Service, Why, And For How Long.", "fetcher": "oos", "filters": [], "groups": [{"id": "activity", "label": "Activity"}, {"id": "time", "label": "Time Out Of Service"}, {"id": "current", "label": "Current Status"}], "icon": "material/build", "id": "oos", "label": "Out Of Service", "measures": [{"agg": "sum", "decimals": 0, "field": "taken", "group": "activity", "id": "taken", "label": "Times Taken Out Of Service", "unit": "events"}, {"agg": "sum", "decimals": 0, "field": "returned", "group": "activity", "id": "returned", "label": "Returned To Service", "unit": "events"}, {"agg": "max", "decimals": 0, "field": "devices", "group": "activity", "id": "devices", "label": "Devices Affected", "unit": "devices"}, {"agg": "sum", "decimals": 1, "field": "oosHours", "group": "time", "id": "oosHours", "label": "Hours Out Of Service", "unit": "h"}, {"agg": "ratio", "decimals": 1, "den": "returned", "field": "", "group": "time", "id": "avgOos", "label": "Avg Time Out Of Service", "num": "durHours", "scale": 1.0, "unit": "h"}, {"agg": "last", "current": true, "decimals": 0, "field": "outNow", "group": "current", "id": "outNow", "label": "Out Of Service Now", "unit": "devices"}], "meta": "Out Of Service Log", "permission": "Reports/OutOfService", "records": true, "scope": [{"id": "all", "label": "All Devices", "level": "all", "parent": ""}], "scopeLevels": [{"id": "all", "label": "All"}, {"id": "area", "label": "Area"}, {"id": "device", "label": "Device"}], "scopeMulti": true, "scopeOptions": "dynamic", "sections": ["cards", "table", "topn", "records", "trend", "notes"], "topN": [{"id": "devices", "label": "Top Devices", "orderBy": [{"label": "Hours Out Of Service", "value": "hours"}, {"label": "Times Taken Out", "value": "count"}]}, {"id": "reasons", "label": "Top Reasons", "orderBy": [{"label": "Times Taken Out", "value": "count"}, {"label": "Hours Out Of Service", "value": "hours"}]}]}, {"breakdowns": [{"id": "none", "label": "Total (No Breakdown)"}, {"id": "hour", "label": "By Hour"}, {"id": "shift", "label": "By Shift"}, {"id": "day", "label": "By Day"}, {"id": "week", "label": "By Week"}], "defaultBreakdown": "day", "defaultMeasures": ["subs", "abnormal", "releases", "openItems"], "defaultScope": ["all"], "defaultSections": ["cards", "records"], "description": "Daily Rounds And NH3 Shift Log Submissions, Abnormal Shifts And Releases.", "fetcher": "forms", "filters": [{"id": "shifts", "label": "Shifts", "options": [{"label": "Shift A (07:00-15:00)", "value": "A"}, {"label": "Shift B (15:00-23:00)", "value": "B"}, {"label": "Shift C (23:00-07:00)", "value": "C"}]}], "groups": [{"id": "subs", "label": "Submissions"}, {"id": "flags", "label": "Shift Log Flags"}], "icon": "material/assignment", "id": "forms", "label": "Operations Forms", "measures": [{"agg": "sum", "decimals": 0, "field": "subs", "group": "subs", "id": "subs", "label": "Forms Submitted", "unit": "forms"}, {"agg": "sum", "decimals": 0, "field": "daily", "group": "subs", "id": "daily", "label": "Daily Rounds Logs", "unit": "forms"}, {"agg": "sum", "decimals": 0, "field": "shiftLogs", "group": "subs", "id": "shiftLogs", "label": "NH3 Shift Logs", "unit": "forms"}, {"agg": "sum", "decimals": 0, "field": "abnormal", "group": "flags", "id": "abnormal", "label": "Abnormal Shifts", "unit": "shifts"}, {"agg": "sum", "decimals": 0, "field": "releases", "group": "flags", "id": "releases", "label": "Releases Logged", "unit": "forms"}, {"agg": "sum", "decimals": 0, "field": "openItems", "group": "flags", "id": "openItems", "label": "Logs With Open Items", "unit": "forms"}], "meta": "Operations Forms", "permission": "Reports/Forms", "records": true, "scope": [{"id": "all", "label": "All Forms", "level": "all", "parent": ""}, {"id": "form:DailyRounds", "label": "Daily Rounds Log", "level": "form", "parent": "all"}, {"id": "form:ShiftLog", "label": "NH3 Shift Log", "level": "form", "parent": "all"}], "scopeLevels": [{"id": "all", "label": "All"}, {"id": "form", "label": "Form"}], "scopeMulti": true, "sections": ["cards", "table", "topn", "records", "trend", "notes"], "topN": [{"id": "people", "label": "Submissions By Person", "orderBy": [{"label": "Count", "value": "count"}]}]}, {"breakdowns": [{"id": "none", "label": "Total (No Breakdown)"}, {"id": "hour", "label": "By Hour"}, {"id": "shift", "label": "By Shift"}, {"id": "day", "label": "By Day"}, {"id": "week", "label": "By Week"}], "defaultBreakdown": "day", "defaultMeasures": ["rate", "oee", "throughput"], "defaultScope": ["line"], "defaultSections": ["cards", "trend", "table"], "deployment": "enterprise", "description": "Line, Zone And Unit KPIs Of The FCM Line - The Production Overview Figures.", "fetcher": "production", "filters": [{"id": "shifts", "label": "Shifts", "options": [{"label": "Shift A (07:00-15:00)", "value": "A"}, {"label": "Shift B (15:00-23:00)", "value": "B"}, {"label": "Shift C (23:00-07:00)", "value": "C"}]}], "groups": [{"id": "throughput", "label": "Throughput"}, {"id": "oee", "label": "OEE"}, {"id": "quality", "label": "Quality"}, {"id": "downtime", "label": "Uptime & Downtime"}, {"id": "state", "label": "Time In State"}, {"id": "alarms", "label": "Alarms"}], "historyRoot": "[default]Boars_Head/GrovePort/Production/FCM/", "icon": "material/show_chart", "id": "production", "label": "Production - FCM Chipotle Chicken Line", "measures": [{"agg": "avg", "decimals": 0, "field": "lineRate", "group": "throughput", "history": {"line": "Line/Rate", "mode": "Average", "unit": "{unit}/Rate", "zone": "Zones/{zone}/Rate"}, "id": "rate", "label": "LBS/HR", "unit": "lb/hr"}, {"agg": "avg", "decimals": 1, "field": "rateVsTarget", "group": "throughput", "history": {"calc": "vsTarget"}, "id": "vsTarget", "label": "Vs Target", "unit": "%"}, {"agg": "sum", "decimals": 0, "field": "throughput", "group": "throughput", "id": "throughput", "label": "Throughput (Cases / Units)", "levels": ["line", "unit"], "unit": "count"}, {"agg": "avg", "decimals": 1, "field": "oee", "group": "oee", "history": {"calc": "oee", "mode": "Average", "unit": "{unit}/OEE", "zone": "Zones/{zone}/OEE"}, "id": "oee", "label": "OEE", "unit": "%"}, {"agg": "avg", "decimals": 1, "field": "availability", "group": "oee", "history": {"line": "Line/Availability", "mode": "Average"}, "id": "availability", "label": "Availability", "unit": "%"}, {"agg": "avg", "decimals": 1, "field": "performance", "group": "oee", "history": {"line": "Line/Performance", "mode": "Average"}, "id": "performance", "label": "Performance", "unit": "%"}, {"agg": "avg", "decimals": 1, "field": "quality", "group": "oee", "history": {"line": "Line/Quality", "mode": "Average"}, "id": "quality", "label": "Quality", "unit": "%"}, {"agg": "avg", "decimals": 1, "field": "yieldPct", "group": "quality", "history": {"line": "Line/Yield", "mode": "Average"}, "id": "yield", "label": "Yield", "unit": "%"}, {"agg": "avg", "decimals": 2, "field": "rejectPct", "group": "quality", "history": {"line": "Line/Reject", "mode": "Average", "unit": "{unit}/Reject"}, "id": "reject", "label": "Reject", "unit": "%"}, {"agg": "avg", "decimals": 1, "field": "uptimePct", "group": "downtime", "history": {"line": "Line/Uptime", "mode": "Average"}, "id": "uptime", "label": "Uptime", "unit": "%"}, {"agg": "sum", "decimals": 1, "field": "runHours", "group": "downtime", "id": "runTime", "label": "Run Time", "unit": "h"}, {"agg": "sum", "decimals": 0, "field": "downtimeMin", "group": "downtime", "id": "downtime", "label": "Downtime", "unit": "min"}, {"agg": "sum", "decimals": 0, "field": "dtEventCount", "group": "downtime", "id": "downtimeEvents", "label": "Downtime Events", "unit": "events"}, {"agg": "sum", "decimals": 1, "field": "tisRunning", "group": "state", "id": "tisRunning", "label": "Running", "unit": "h"}, {"agg": "sum", "decimals": 1, "field": "tisChangeover", "group": "state", "id": "tisChangeover", "label": "Changeover", "unit": "h"}, {"agg": "sum", "decimals": 1, "field": "tisIdle", "group": "state", "id": "tisIdle", "label": "Idle", "unit": "h"}, {"agg": "sum", "decimals": 1, "field": "tisFault", "group": "state", "id": "tisFault", "label": "Fault", "unit": "h"}, {"agg": "sum", "decimals": 0, "field": "alarmCount", "group": "alarms", "id": "alarmCount", "label": "Alarms", "unit": "alarms"}, {"agg": "sum", "decimals": 0, "field": "alarmHigh", "group": "alarms", "id": "alarmHigh", "label": "High Priority Alarms", "unit": "alarms"}, {"agg": "sum", "decimals": 0, "field": "alarmDurationMin", "group": "alarms", "id": "alarmDuration", "label": "Alarm Duration", "unit": "min"}], "meta": "Enterprise Demo \u00b7 FCM Line", "permission": "Reports/Production", "scope": [{"id": "line", "label": "FCM Line", "level": "line", "parent": ""}, {"id": "zone:Prep", "label": "Prep Zone", "level": "zone", "parent": "line"}, {"id": "zone:Forming", "label": "Forming Zone", "level": "zone", "parent": "line"}, {"id": "zone:Packaging", "label": "Packaging Zone", "level": "zone", "parent": "line"}, {"id": "unit:VD", "label": "Vat Dumper", "level": "unit", "parent": "zone:Prep"}, {"id": "unit:HOP", "label": "Hopper", "level": "unit", "parent": "zone:Prep"}, {"id": "unit:HND", "label": "Handtman", "level": "unit", "parent": "zone:Forming"}, {"id": "unit:LDR", "label": "Loaders", "level": "unit", "parent": "zone:Forming"}, {"id": "unit:RSM", "label": "Roll Stock", "level": "unit", "parent": "zone:Packaging"}, {"id": "unit:ST", "label": "Shrink Tunnel", "level": "unit", "parent": "zone:Packaging"}, {"id": "unit:LS", "label": "Lazy Susan", "level": "unit", "parent": "zone:Packaging"}], "scopeLevels": [{"id": "line", "label": "Line"}, {"id": "zone", "label": "Zone"}, {"id": "unit", "label": "Unit"}], "scopeMulti": true, "sections": ["cards", "trend", "table", "shifts", "topn", "notes"], "targets": {"line": 950, "unit": 130, "zone": 950}, "topN": [{"id": "downtime", "label": "Top Downtime Reasons", "orderBy": [{"label": "Minutes", "value": "minutes"}, {"label": "Events", "value": "events"}]}]}], "version": 7}''')
SHIFT_START = {"A": 7, "B": 15, "C": 23}
PDF_COLS = 8               # Reports/CustomReport rows table: key column + 7 value columns
PDF_MAX_ROWS = 1500        # per table in the PDF (Excel / CSV carry every row)
PREVIEW_ROWS = 25
MAX_PENS = 6
HOUR = 3600000
DAY = 86400000
RECORDS_DEFAULT = 200      # Event List rows (newest first); the section's n, 10..RECORDS_MAX
RECORDS_MAX = 2000
TIME_PRESETS = [("lastShift", "Last Shift"), ("today", "Today"), ("yesterday", "Yesterday"), ("last7", "Last 7 Days"),
	("last30", "Last 30 Days"), ("custom", "Custom")]
TIME_IDS = [k for k, v in TIME_PRESETS]
_state = {"catalog": None, "catalogAt": 0, "options": {}}


# ------------------------------------------------------------------------------------------------ session / access
def username(session):
	try:
		return str(session.props.auth.user.userName or "")
	except (Exception, Throwable):
		return ""


def displayName(session):
	u = username(session)
	try:
		usr = system.user.getUser("default", u)
		if usr is not None:
			full = ("%s %s" % (usr.get("firstname") or "", usr.get("lastname") or "")).strip()
			if full:
				return full
	except (Exception, Throwable):
		pass
	return u


def allowed(session, action="Use"):
	"""Reports/<action> for the session (Roles & Permissions matrix via shared.Security). No session -> False."""
	if session is None or username(session) == "":
		return False
	try:
		return bool(shared.Security.allowed(session, "Reports", action))
	except (Exception, Throwable) as e:
		LOG.warn("Reports permission check failed: %s" % e)
		return False


def sourceAllowed(session, src):
	if src is None or not allowed(session, "Use"):
		return False
	dev, _, act = str(src.get("permission") or "Reports/Use").partition("/")
	try:
		return bool(shared.Security.allowed(session, dev, act or "Use"))
	except (Exception, Throwable):
		return False


def context(session):
	return {"user": username(session), "name": displayName(session), "use": allowed(session, "Use"),
		"share": allowed(session, "ShareTemplates"), "manage": allowed(session, "ManageTemplates")}


# ------------------------------------------------------------------------------------------------ catalog
def catalog():
	"""The live catalog tag when it is valid and not older than the builder's copy (cached 30 s)."""
	now = system.date.toMillis(system.date.now())
	if _state["catalog"] is not None and now - _state["catalogAt"] < 30000:
		return _state["catalog"]
	cat = FALLBACK
	try:
		qv = system.tag.readBlocking([CATALOG_TAG])[0]
		if qv.quality.isGood() and qv.value is not None:
			live = _json.loads(unicode(qv.value))
			if isinstance(live, dict) and live.get("sources") and int(live.get("version") or 0) >= int(FALLBACK["version"]):
				cat = live
	except (Exception, Throwable) as e:
		LOG.debug("catalog tag unreadable, using the built-in copy: %s" % e)
	_state["catalog"] = cat
	_state["catalogAt"] = now
	return cat


def enterpriseMode():
	"""Deployment switch (docs/local-groveport-mode.md): True only while [default]_Config/DemoEnterpriseNav is a good
	True. Missing / bad tag = local Groveport mode, so enterprise-only sources stay hidden (cached 30 s)."""
	now = system.date.toMillis(system.date.now())
	if _state.get("modeAt") and now - _state["modeAt"] < 30000:
		return _state["mode"]
	mode = False
	try:
		qv = system.tag.readBlocking([DEPLOY_TAG])[0]
		mode = bool(qv.quality.isGood() and qv.value)
	except (Exception, Throwable):
		mode = False
	_state["mode"] = mode
	_state["modeAt"] = now
	return mode


def deployed(src):
	"""A source is offered unless it is enterprise-only ('deployment': 'enterprise') and the HMI is in local mode."""
	return src is not None and (src.get("deployment") != "enterprise" or enterpriseMode())


def sources():
	return [s for s in catalog()["sources"] if deployed(s)]


def source(sourceId):
	"""Catalog source by id; None for an unknown or a hidden (enterprise-only in local mode) source."""
	for s in catalog()["sources"]:
		if s["id"] == sourceId:
			return s if deployed(s) else None
	return None


def clientCatalog(session):
	"""Catalog for the builder view: only the sources the session may use, presets for those sources."""
	cat = catalog()
	srcs = [s for s in sources() if sourceAllowed(session, s)]
	ids = [s["id"] for s in srcs]
	return {"version": cat["version"], "sectionTypes": cat["sectionTypes"], "sources": srcs,
		"presets": [p for p in cat.get("presets") or [] if p["def"]["source"] in ids]}


def sourceOptions(session):
	return [{"value": s["id"], "label": s["label"]} for s in clientCatalog(session)["sources"]]


def _measure(src, mid):
	for m in src["measures"]:
		if m["id"] == mid:
			return m
	return None


def _applies(m, level):
	lv = m.get("levels")
	return not lv or level in lv


def scopeItems(session, sourceId):
	"""[{id, label, level, parent}] - static catalog tree, plus the fetcher's dynamic options (alarm areas / devices)."""
	src = source(sourceId)
	if src is None or not sourceAllowed(session, src):
		return []
	items = list(src.get("scope") or [])
	if src.get("scopeOptions") == "dynamic":
		fn = FETCHERS.get(src["fetcher"], {}).get("options")
		if fn:
			items += fn(src)
	return items


def scopeTree(session, sourceId):
	"""Scope picker rows for the builder: [{id, label, level, indent, parent}] in tree order."""
	items = scopeItems(session, sourceId)
	kids = {}
	for it in items:
		kids.setdefault(it.get("parent") or "", []).append(it)
	out = []

	def walk(parent, depth):
		for it in kids.get(parent, []):
			out.append({"id": it["id"], "label": it["label"], "level": it["level"], "indent": depth,
				"parent": it.get("parent") or ""})
			walk(it["id"], depth + 1)

	walk("", 0)
	return out


def measureGroups(session, sourceId):
	"""[{id, label, measures:[{id, label, unit}]}] for the builder's grouped checkboxes."""
	src = source(sourceId)
	if src is None or not sourceAllowed(session, src):
		return []
	out = []
	for g in src.get("groups") or []:
		ms = [{"id": m["id"], "label": m["label"], "unit": m.get("unit") or ""} for m in src["measures"]
			if m.get("group") == g["id"]]
		if ms:
			out.append({"id": g["id"], "label": g["label"], "measures": ms})
	return out


# ------------------------------------------------------------------------------------------------ definition
def _py(obj):
	"""Perspective / Java structures -> plain Python (dates become epoch millis)."""
	if obj is None:
		return None
	try:
		return _json.loads(system.util.jsonEncode(obj))
	except (Exception, Throwable):
		return obj


def _ms(v):
	if v is None or v == "":
		return None
	try:
		if isinstance(v, (int, long, float)):
			return long(v)
		if hasattr(v, "getTime"):
			return long(v.getTime())
		s = unicode(v).strip()
		if len(s) >= 10 and s[4] == "-" and s[7] == "-":
			return long(system.date.toMillis(system.date.parse(s[:10], "yyyy-MM-dd")))
	except (Exception, Throwable):
		pass
	return None


def _ymd(ms):
	return system.date.format(system.date.fromMillis(ms), "yyyy-MM-dd")


def _ctxDay(v):
	"""yyyy-MM-dd for a context date: java Date, epoch ms or text; '' when empty / unreadable."""
	if v is None or v == "":
		return ""
	try:
		if isinstance(v, basestring):
			return str(v)[:10]
		if isinstance(v, (int, long, float)):
			return _ymd(long(v))
		return system.date.format(v, "yyyy-MM-dd")
	except (Exception, Throwable):
		return ""


def _defaultSections(src):
	on = src.get("defaultSections") or []
	out = []
	for st in [t["id"] for t in catalog()["sectionTypes"]]:
		if st not in src.get("sections", []):
			continue
		sec = {"type": st, "on": st in on}
		if st == "topn":
			tn = (src.get("topN") or [{}])[0]
			sec.update({"topN": tn.get("id", ""), "n": 10, "orderBy": ((tn.get("orderBy") or [{}])[0]).get("value", "")})
		elif st == "records":
			sec["n"] = RECORDS_DEFAULT
		out.append(sec)
	return out


def normalize(defn):
	"""Any (partial) definition -> a complete, valid one (unknown ids dropped, defaults filled)."""
	d = _py(defn) or {}
	src = source(d.get("source")) or (sources() or catalog()["sources"])[0]
	ids = [m["id"] for m in src["measures"]]
	meas = d.get("measures")
	if meas == "*":
		meas = ids
	meas = [m for m in (meas or []) if m in ids] or list(src.get("defaultMeasures") or ids[:1])
	scope_ids = [str(s) for s in (d.get("scope") or []) if s]
	if src.get("scopeOptions") != "dynamic":
		known = [s["id"] for s in src.get("scope") or []]
		scope_ids = [s for s in scope_ids if s in known]
	else:
		scope_ids = [s for s in scope_ids if s == "all" or s.startswith("area:") or s.startswith("device:")]
	scope_ids = scope_ids or list(src.get("defaultScope") or [])
	t = d.get("time") or {}
	preset = t.get("preset") if t.get("preset") in TIME_IDS else "last7"
	tt = {"preset": preset}
	if preset == "custom":
		s_ms = _ms(t.get("start")) or system.date.toMillis(system.date.midnight(system.date.now()))
		e_ms = _ms(t.get("end")) or s_ms
		if e_ms < s_ms:
			s_ms, e_ms = e_ms, s_ms
		tt.update({"start": _ymd(s_ms), "end": _ymd(e_ms)})
	shifts = [s for s in (d.get("shifts") or []) if s in ("A", "B", "C")]
	if len(shifts) == 3:
		shifts = []
	filt = {}
	for f in src.get("filters") or []:
		if f["id"] == "shifts":
			continue
		vals = [str(x["value"]) for x in f.get("options") or []]
		filt[f["id"]] = [str(v) for v in ((d.get("filters") or {}).get(f["id"]) or []) if str(v) in vals]
	bds = [b["id"] for b in src.get("breakdowns") or []]
	bd = d.get("breakdown") if d.get("breakdown") in bds else src.get("defaultBreakdown", "day")
	secs = []
	allowed_types = src.get("sections") or []
	seen = []
	for s in d.get("sections") or []:
		st = (s or {}).get("type")
		if st in allowed_types and st not in seen:
			seen.append(st)
			sec = {"type": st, "on": bool(s.get("on", True))}
			if st == "topn":
				tns = dict((x["id"], x) for x in src.get("topN") or [])
				tn = tns.get(s.get("topN")) or (src.get("topN") or [{}])[0]
				obs = [o["value"] for o in tn.get("orderBy") or []]
				try:
					n = max(1, min(100, int(s.get("n") or 10)))
				except (Exception, Throwable):
					n = 10
				sec.update({"topN": tn.get("id", ""), "n": n,
					"orderBy": s.get("orderBy") if s.get("orderBy") in obs else (obs[0] if obs else "")})
			elif st == "records":
				try:
					sec["n"] = max(10, min(RECORDS_MAX, int(s.get("n") or RECORDS_DEFAULT)))
				except (Exception, Throwable):
					sec["n"] = RECORDS_DEFAULT
			secs.append(sec)
	for s in _defaultSections(src):
		if s["type"] not in seen:
			s["on"] = False if d.get("sections") else s["on"]
			secs.append(s)
	fmt = d.get("format") if d.get("format") in ("PDF", "Excel", "CSV") else "PDF"
	return {"version": 1, "source": src["id"], "title": unicode(d.get("title") or "").strip()[:120],
		"notes": unicode(d.get("notes") or "").strip()[:2000], "measures": meas, "scope": scope_ids, "time": tt,
		"shifts": shifts, "filters": filt, "breakdown": bd, "sections": secs, "format": fmt}


def defaultDefinition(session, sourceId=None, ctx=None):
	"""Builder start state: the source's defaults + the opening page's context (scope, shift, day, areas)."""
	ctx = _py(ctx) or {}
	srcs = clientCatalog(session)["sources"]
	src = None
	for s in srcs:
		if s["id"] == sourceId:
			src = s
	src = src or (srcs[0] if srcs else catalog()["sources"][0])
	d = {"source": src["id"], "measures": src.get("defaultMeasures"), "scope": ctx.get("scope") or src.get("defaultScope"),
		"shifts": ctx.get("shifts") or [], "breakdown": src.get("defaultBreakdown", "day"),
		"time": {"preset": src.get("defaultTime") or "last7"}, "sections": _defaultSections(src), "format": "PDF"}
	if ctx.get("areas"):
		d["scope"] = ["area:" + a for a in ctx["areas"]]
	if ctx.get("forms"):                  # Form History filter (DailyRounds / ShiftLog)
		fs = [f for f in ctx["forms"] if ("form:" + f) in [x["id"] for x in src.get("scope") or []]]
		if fs:
			d["scope"] = ["form:" + f for f in fs]
	if ctx.get("start") or ctx.get("end"):      # a page's From / To filters (Date, epoch ms or yyyy-MM-dd text)
		today = _ymd(system.date.toMillis(system.date.now()))
		a = _ctxDay(ctx.get("start")) or today
		b = min(_ctxDay(ctx.get("end")) or today, today)
		d["time"] = {"preset": "custom", "start": min(a, b), "end": b}
	if ctx.get("dayOffset") is not None:
		try:
			off = int(ctx.get("dayOffset") or 0)
		except (Exception, Throwable):
			off = 0
		if off == 0:
			d["time"] = {"preset": "today"}
		elif off == 1:
			d["time"] = {"preset": "yesterday"}
		else:
			day = _ymd(system.date.toMillis(system.date.addDays(system.date.midnight(system.date.now()), -off)))
			d["time"] = {"preset": "custom", "start": day, "end": day}
		d["breakdown"] = "hour" if d["shifts"] else "shift"
	n = normalize(d)
	n["title"] = _autoTitle(n)
	return n


def _autoTitle(d):
	src = source(d["source"])
	ms = [(_measure(src, m) or {}).get("label", m) for m in d["measures"]]
	what = ms[0] if len(ms) == 1 else src["label"].split(" - ")[0]
	scopes = [s["label"] for s in _scopeObjs(src, d["scope"])]
	where = scopes[0] if len(scopes) == 1 else ("%s + %d More" % (scopes[0], len(scopes) - 1) if scopes else "")
	shift = (" - Shift " + ", ".join(d["shifts"])) if d.get("shifts") else ""
	return "%s - %s - %s%s" % (what, where, _windowLabel(d, short=True), shift)


def applyPreset(session, presetId):
	for p in clientCatalog(session).get("presets") or []:
		if p["id"] == presetId:
			return normalize(p["def"])
	return None


# ------------------------------------------------------------------------------------------------ time
def _now():
	return long(system.date.toMillis(system.date.now()))


def _mid(ms):
	return long(system.date.toMillis(system.date.midnight(system.date.fromMillis(ms))))


def _addD(ms, n):
	return long(system.date.toMillis(system.date.addDays(system.date.fromMillis(ms), n)))


def _addH(ms, n):
	return long(system.date.toMillis(system.date.addHours(system.date.fromMillis(ms), n)))


def _fmtT(ms, pattern):
	return system.date.format(system.date.fromMillis(ms), pattern)


def _shiftStart(ms):
	"""Start of the shift running at ms (A 07:00, B 15:00, C 23:00 - C starts the evening before after midnight)."""
	day = _mid(ms)
	h = int(system.date.getHour24(system.date.fromMillis(ms)))
	if h < 7:
		return _addH(_addD(day, -1), 23)
	return _addH(day, 7 if h < 15 else (15 if h < 23 else 23))


def window(d):
	now = _now()
	today = _mid(now)
	p = d["time"]["preset"]
	if p == "lastShift":
		cur = _shiftStart(now)
		return _addH(cur, -8), cur
	if p == "today":
		return today, now
	if p == "yesterday":
		return _addD(today, -1), today
	if p == "last7":
		return _addD(today, -6), now
	if p == "last30":
		return _addD(today, -29), now
	s = _mid(_ms(d["time"].get("start")) or today)
	e = _addD(_mid(_ms(d["time"].get("end")) or s), 1)
	return s, min(e, now)


def _windowLabel(d, short=False):
	s, e = window(d)
	p = d["time"]["preset"]
	names = dict(TIME_PRESETS)
	if p == "lastShift":
		lbl = "Shift %s %s - %s" % (shiftOf(int(system.date.getHour24(system.date.fromMillis(s)))), _fmtT(s, "MM/dd HH:mm"),
			_fmtT(e, "HH:mm"))
		return "Last Shift" if short else "Last Shift (%s)" % lbl
	last = e - 1 if e > s else s
	rng = _fmtT(s, "MM/dd/yyyy") if _mid(s) == _mid(last) else "%s - %s" % (_fmtT(s, "MM/dd/yyyy"), _fmtT(last, "MM/dd/yyyy"))
	if short:
		return names[p] if p != "custom" else rng
	return "%s (%s)" % (names[p], rng) if p != "custom" else rng


def shiftOf(hour):
	return "A" if 7 <= hour < 15 else ("B" if 15 <= hour < 23 else "C")


def buckets(s, e, grain, shifts):
	"""[{t, t1, label, shift, day}] local time; t = bucket start (shift start for 'shift', may precede s)."""
	out = []
	if grain == "hour":
		t = _addH(_mid(s), int((s - _mid(s)) // HOUR))
		while t < e:
			h = int(system.date.getHour24(system.date.fromMillis(t)))
			letter = shiftOf(h)
			if not shifts or letter in shifts:
				out.append({"t": t, "t1": min(_addH(t, 1), e), "label": _fmtT(t, "MM/dd HH:00"), "shift": letter,
					"day": _mid(t)})
			t = _addH(t, 1)
	elif grain == "shift":
		d = _addD(_mid(s), -1)
		while d < e:
			for letter in ("A", "B", "C"):
				t0 = _addH(d, SHIFT_START[letter])
				t1 = _addH(t0, 8)
				if t1 <= s or t0 >= e or (shifts and letter not in shifts):
					continue
				out.append({"t": t0, "t1": min(t1, e), "label": "%s Shift %s" % (_fmtT(t0, "MM/dd"), letter),
					"shift": letter, "day": d})
			d = _addD(d, 1)
	elif grain == "day":
		d = _mid(s)
		while d < e:
			out.append({"t": d, "t1": min(_addD(d, 1), e), "label": _fmtT(d, "EEE MM/dd"), "shift": "", "day": d})
			d = _addD(d, 1)
	elif grain == "week":
		d = _mid(s)
		dow = int(system.date.getDayOfWeek(system.date.fromMillis(d)))      # 1 = Sunday
		w = _addD(d, -((dow + 5) % 7))
		while w < e:
			out.append({"t": w, "t1": min(_addD(w, 7), e), "label": "Week Of %s" % _fmtT(w, "MM/dd"), "shift": "",
				"day": w})
			w = _addD(w, 7)
	else:
		out.append({"t": s, "t1": e, "label": "Total", "shift": "", "day": _mid(s)})
	return out


def _days(t0, t1):
	out = []
	d = _mid(t0)
	while d < t1:
		out.append(d)
		d = _addD(d, 1)
	return out


# ------------------------------------------------------------------------------------------------ aggregation
def _num(v):
	try:
		if v is None or v == "":
			return None
		return float(v)
	except (Exception, Throwable):
		return None


def mvalue(m, v):
	"""Measure value from a record keyed by fields (ratio = num / den x scale)."""
	if m.get("agg") == "ratio":
		n, dn = _num(v.get(m.get("num"))), _num(v.get(m.get("den")))
		if n is None or not dn:
			return None
		return n / dn * float(m.get("scale") or 1.0)
	return _num(v.get(m.get("field")))


def aggregate(m, recs):
	"""Aggregate one measure over records (catalog agg)."""
	agg = m.get("agg")
	if agg == "ratio":
		n = [_num(r.get(m.get("num"))) for r in recs]
		dn = [_num(r.get(m.get("den"))) for r in recs]
		n = sum(x for x in n if x is not None)
		dn = sum(x for x in dn if x is not None)
		return (n / dn * float(m.get("scale") or 1.0)) if dn else None
	vals = [mvalue(m, r) for r in recs]
	vals = [x for x in vals if x is not None]
	if not vals:
		return None
	if agg == "sum":
		return sum(vals)
	if agg == "min":
		return min(vals)
	if agg == "max":
		return max(vals)
	if agg == "last":
		return vals[-1]
	if agg == "count":
		return float(len(vals))
	return sum(vals) / float(len(vals))


def fmtValue(m, v, unit=False):
	if v is None:
		return "--"
	dec = int(m.get("decimals") or 0)
	s = ("{:,.%df}" % dec).format(float(v))
	if unit:
		u = m.get("unit") or ""
		if u == "%":
			s += " %"
		elif u not in COUNT_UNITS:
			s += " " + u
	return s


COUNT_UNITS = ("", "count", "alarms", "events", "devices", "forms", "shifts", "starts")


def header(m):
	u = m.get("unit") or ""
	if u in COUNT_UNITS:
		return m["label"]
	return "%s (%s)" % (m["label"], u)


# ------------------------------------------------------------------------------------------------ production fetcher
def _parseHM(s):
	try:
		h, _, rest = unicode(s).partition("h")
		return float(h.strip()) + float(rest.replace("m", "").strip() or 0) / 60.0
	except (Exception, Throwable):
		return None


def _summaryVal(rows, metric):
	for r in rows or []:
		if r.get("Metric") == metric:
			txt = unicode(r.get("Value") or "")
			try:
				return float(txt.split(" ")[0].replace(",", ""))
			except (Exception, Throwable):
				return None
	return None


def _flat(r, level):
	"""shared.ProductionMetrics.l1 output -> flat record keyed by the catalog 'field' names."""
	tis = list(r.get("tisValues") or [0, 0, 0, 0]) + [0, 0, 0, 0]
	dt = [float(x) for x in (r.get("dtValues") or [])]
	if level == "line":
		thr = r.get("casesToday")
	else:
		lab = unicode(r.get("throughputLabel") or "")
		thr = _num(lab.split(" ")[-1]) if lab.startswith("Units") else (0 if r.get("shiftPending") else None)
	return {"lineRate": r.get("lineRate"), "rateVsTarget": r.get("rateVsTarget"), "oee": r.get("oee"),
		"availability": r.get("availability"), "performance": r.get("performance"), "quality": r.get("quality"),
		"yieldPct": r.get("yieldPct"), "rejectPct": r.get("rejectPct"), "uptimePct": r.get("uptimePct"),
		"runHours": _parseHM(r.get("runTime")), "downtimeMin": sum(dt), "dtEventCount": r.get("dtEventCount"),
		"throughput": thr, "tisRunning": tis[0], "tisChangeover": tis[1], "tisIdle": tis[2], "tisFault": tis[3],
		"alarmCount": _summaryVal(r.get("alarmSummary"), "Total Alarms"),
		"alarmHigh": _summaryVal(r.get("alarmSummary"), "High Priority"),
		"alarmDurationMin": _summaryVal(r.get("alarmSummary"), "Total Duration"),
		"_win": 0.0 if r.get("shiftPending") else float(r.get("windowHours") or 0),
		"_dt": dict(zip([unicode(x) for x in (r.get("dtLabels") or [])], dt))}


def _combine(recs, aggs, weighted=True):
	"""Merge records (shifts of a day, days of a week, units of a zone) with each field's catalog aggregation."""
	recs = [r for r in recs if r is not None]
	out = {"_win": sum(r.get("_win") or 0 for r in recs), "_dt": {}}
	for r in recs:
		for k, v in (r.get("_dt") or {}).items():
			out["_dt"][k] = out["_dt"].get(k, 0) + v
	for f, agg in aggs.items():
		vals = [(r.get(f), r.get("_win") or 0) for r in recs if r.get(f) is not None]
		if not vals:
			out[f] = None
		elif agg == "sum":
			out[f] = sum(float(v) for v, w in vals)
		elif agg == "max":
			out[f] = max(float(v) for v, w in vals)
		elif agg == "min":
			out[f] = min(float(v) for v, w in vals)
		else:
			tw = sum(w for v, w in vals) if weighted else 0
			if tw > 0:
				out[f] = sum(float(v) * w for v, w in vals) / tw
			else:
				live = [float(v) for v, w in vals if not weighted or w > 0] or [float(v) for v, w in vals]
				out[f] = sum(live) / len(live)
	return out


class _Demo(object):
	"""Production demo generator per day / shift / scope (memoised shared.ProductionMetrics.l1 calls)."""

	def __init__(self, src):
		self.src = src
		self.cache = {}
		self.today = _mid(_now())
		self.aggs = {}
		self.zoneAggs = {}            # zone = its units: hours (run time, time in state) average, counts add up
		for m in src["measures"]:
			if m.get("field"):
				self.aggs[m["field"]] = m.get("agg") or "avg"
				self.zoneAggs[m["field"]] = "avg" if m.get("unit") == "h" else (m.get("agg") or "avg")
		self.units = dict((s["id"][5:], s) for s in src["scope"] if s["level"] == "unit")
		self.targets = src.get("targets") or {}

	def l1(self, day, letter, sel, dtRe=""):
		off = int(round((self.today - day) / float(DAY)))
		k = (off, letter, sel, dtRe)
		if k not in self.cache:
			self.cache[k] = shared.ProductionMetrics.l1({"sel": sel, "day": off, "shift": letter, "dtRe": dtRe})
		return self.cache[k]

	def scopeRec(self, day, letter, sc):
		lvl = sc["level"]
		if lvl == "line":
			return _flat(self.l1(day, letter, ""), "line")
		if lvl == "unit":
			return _flat(self.l1(day, letter, sc["id"][5:]), "unit")
		zid = sc["id"][5:]
		urecs = [_flat(self.l1(day, letter, uid), "unit") for uid, u in self.units.items()
			if u.get("parent") == sc["id"]]
		rec = _combine(urecs, self.zoneAggs, weighted=False)
		rec["_win"] = max([u.get("_win") or 0 for u in urecs] or [0])
		rec["throughput"] = None
		line = self.l1(day, letter, "")
		for z in line.get("zones") or []:
			if z.get("Zone") == zid:
				rec["lineRate"] = z.get("Rate")
				rec["oee"] = z.get("OEE")
				rec["downtimeMin"] = z.get("Downtime")
		if rec.get("lineRate") is not None:
			rec["rateVsTarget"] = round((float(rec["lineRate"]) / float(self.targets.get("zone") or 950) - 1.0) * 100.0, 1)
		return rec

	def dayRec(self, day, sc, shifts):
		if not shifts and day < self.today:
			return self.scopeRec(day, "", sc)
		return _combine([self.scopeRec(day, L, sc) for L in (shifts or ["A", "B", "C"])], self.aggs)

	def bucketRec(self, b, sc, grain, shifts, s, e):
		if grain == "shift":
			return self.scopeRec(b["day"], b["shift"], sc)
		if grain == "day":
			return self.dayRec(b["t"], sc, shifts)
		if grain == "hour":
			base = self.scopeRec(b["day"], b["shift"], sc)
			if not base.get("_win"):
				return None
			out = {"_win": 1.0, "_dt": {}}
			win = max(1.0, base["_win"])
			for f, agg in self.aggs.items():
				v = base.get(f)
				if v is None:
					out[f] = None
				elif agg == "sum":
					out[f] = float(v) / win
				else:
					j = ((abs(hash("%s|%s|%s" % (sc["id"], f, b["t"]))) % 2001) - 1000) / 1000.0
					out[f] = float(v) * (1.0 + 0.025 * j)
			for k, v in (base.get("_dt") or {}).items():
				out["_dt"][k] = v / win
			return out
		days = [d for d in _days(max(b["t"], s), min(b["t1"], e)) if d < e]
		return _combine([self.dayRec(d, sc, shifts) for d in days], self.aggs)


def _histPaths(src, m, sc):
	"""Tag paths (under historyRoot) a measure needs for this scope, or None when it has no history there."""
	h = m.get("history") or {}
	lvl = sc["level"]
	key = sc["id"].partition(":")[2]
	if h.get("calc") == "vsTarget":
		rate = _measure(src, "rate")
		return _histPaths(src, rate, sc) if rate else None
	if lvl in h:
		return [h[lvl].replace("{zone}", key).replace("{unit}", key) + "/Value"]
	if h.get("calc") == "oee" and lvl == "line":
		out = []
		for mid in ("availability", "performance", "quality"):
			p = _histPaths(src, _measure(src, mid), sc)
			if not p:
				return None
			out += p
		return out
	return None


def _histValue(src, m, sc, paths, hourly, hours):
	"""Bucket value of a measure from the hourly historian averages (None when no samples)."""
	def avg(path):
		vals = [hourly.get(path, {}).get(h) for h in hours]
		vals = [v for v in vals if v is not None]
		return (sum(vals) / len(vals)) if vals else None
	h = m.get("history") or {}
	if h.get("calc") == "vsTarget":
		r = avg(paths[0])
		tgt = float((src.get("targets") or {}).get(sc["level"]) or 950)
		return None if r is None else (r / tgt - 1.0) * 100.0
	if h.get("calc") == "oee" and sc["level"] == "line":
		vals = [avg(p) for p in paths]
		return None if None in vals else vals[0] * vals[1] * vals[2] / 10000.0
	return avg(paths[0])


def _historian(ctx, facts):
	"""Replace demo values by SQL historian averages where the tag history covers the whole bucket."""
	src = ctx["src"]
	root = src.get("historyRoot") or ""
	need = {}
	for m in ctx["measures"]:
		for sc in ctx["scopes"]:
			p = _histPaths(src, m, sc)
			if p:
				need[(m["id"], sc["id"])] = p
	if not need:
		return 0
	allp = sorted(set(p for ps in need.values() for p in ps))
	first = {}
	try:
		ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "History/Coverage",
			parameters={"paths": "|".join((root.split("]", 1)[-1] + p).lower() for p in allp)})
		for r in system.dataset.toPyDataSet(ds):
			first[unicode(r["tagpath"])] = long(r["first_ms"])
	except (Exception, Throwable) as e:
		LOG.warn("history coverage query failed: %s" % e)
		return 0

	def start_of(p):
		v = first.get((root.split("]", 1)[-1] + p).lower())
		return None if v is None else _addH(_mid(v), int((v - _mid(v)) // HOUR) + 1)  # first full hour

	covered_from = [start_of(p) for p in allp if start_of(p) is not None]
	if not covered_from:
		return 0
	q0 = max(ctx["start"], min(covered_from))
	if q0 >= ctx["end"]:
		return 0
	hourly = {}
	try:
		ds = system.tag.queryTagHistory(paths=[root + p for p in allp], startDate=system.date.fromMillis(q0),
			endDate=system.date.fromMillis(ctx["end"]), intervalMinutes=60, aggregationMode="Average",
			returnFormat="Wide", ignoreBadQuality=True)
		for r in range(ds.getRowCount()):
			t = long(system.date.toMillis(ds.getValueAt(r, 0)))
			hk = _addH(_mid(t), int((t - _mid(t)) // HOUR))
			for c, p in enumerate(allp):
				v = _num(ds.getValueAt(r, c + 1))
				if v is not None:
					hourly.setdefault(p, {})[hk] = v
	except (Exception, Throwable) as e:
		LOG.warn("history query failed: %s" % e)
		return 0
	used = 0
	scopes = dict((sc["id"], sc) for sc in ctx["scopes"])
	shifts = ctx["shifts"]
	for f in facts:
		hours = []
		t = max(f["t"], ctx["start"])
		while t < min(f["t1"], ctx["end"]):
			if not shifts or shiftOf(int(system.date.getHour24(system.date.fromMillis(t)))) in shifts:
				hours.append(t)
			t = _addH(t, 1)
		if not hours:
			continue
		for m in ctx["measures"]:
			paths = need.get((m["id"], f["scope"]))
			if not paths:
				continue
			starts = [start_of(p) for p in paths]
			if None in starts or max(starts) > max(f["t"], ctx["start"]):
				continue
			v = _histValue(src, m, scopes[f["scope"]], paths, hourly, hours)
			if v is not None:
				f["v"][m["field"] or m["id"]] = v
				f["src"][m["id"]] = "Historian"
				used += 1
	return used


def _prodFacts(ctx):
	demo = _Demo(ctx["src"])
	facts = []
	for b in ctx["buckets"]:
		for sc in ctx["scopes"]:
			rec = demo.bucketRec(b, sc, ctx["grain"], ctx["shifts"], ctx["start"], ctx["end"])
			if rec is None:
				continue
			srcmap = dict((m["id"], "Demo") for m in ctx["measures"] if _applies(m, sc["level"]))
			facts.append({"t": b["t"], "t1": b["t1"], "label": b["label"], "shift": b.get("shift") or "",
				"scope": sc["id"], "v": rec, "src": srcmap})
	_historian(ctx, facts)
	return {"facts": facts, "current": {}}


def _prodTopN(ctx, spec):
	"""Top downtime reasons over the window (demo generator; downtime has no tag history yet)."""
	demo = _Demo(ctx["src"])
	tot, ev = {}, {}
	days = [d for d in _days(ctx["start"], ctx["end"])]
	lets = ctx["shifts"] or None
	for sc in ctx["scopes"]:
		sels = [""] if sc["level"] == "line" else ([sc["id"][5:]] if sc["level"] == "unit" else
			[uid for uid, u in demo.units.items() if u.get("parent") == sc["id"]])
		for d in days:
			for L in (lets or (["A", "B", "C"] if d >= demo.today else [""])):
				for sel in sels:
					r = demo.l1(d, L, sel)
					for lab, val in zip(r.get("dtLabels") or [], r.get("dtValues") or []):
						tot[lab] = tot.get(lab, 0) + float(val)
						if float(val) > 0:
							ev[lab] = ev.get(lab, 0) + len(demo.l1(d, L, sel, lab).get("dtEvents") or [])
	grand = sum(tot.values()) or 1.0
	key = (lambda k: -ev.get(k, 0)) if spec.get("orderBy") == "events" else (lambda k: -tot[k])
	order = sorted(tot.keys(), key=key)[:int(spec.get("n") or 10)]
	cols = [("Rank", "key", "left"), ("Reason", "key", "left"), ("Minutes", "", "right"), ("Events", "", "right"),
		("% Of Downtime", "", "right")]
	raw = [[i + 1, k, round(tot[k], 0), ev.get(k, 0), round(tot[k] * 100.0 / grand, 1)] for i, k in enumerate(order)]
	return {"columns": cols, "raw": raw,
		"rows": [[unicode(r[0]), r[1], "{:,.0f}".format(r[2]), "{:,}".format(r[3]), "%.1f %%" % r[4]] for r in raw],
		"demo": True}


# ------------------------------------------------------------------------------------------------ alarms fetcher
def _almFilters(ctx, scopes=None):
	scopes = ctx["scopes"] if scopes is None else scopes
	areas = [sc["id"][5:] for sc in scopes if sc["id"].startswith("area:")]
	devs = [sc["id"][7:] for sc in scopes if sc["id"].startswith("device:")]
	return {"start": _fmtT(ctx["start"], "yyyy-MM-dd HH:mm:ss"), "end": _fmtT(ctx["end"], "yyyy-MM-dd HH:mm:ss"),
		"areas": "|".join(areas), "devices": "|".join(devs),
		"priorities": ",".join((ctx["filters"] or {}).get("priorities") or []), "shifts": ",".join(ctx["shifts"])}


def _almPath(src_path):
	"""Alarm source path -> (area, device) after Boars_Head/<Site>/<Area>/<Type>/<Device>; else Other."""
	p = unicode(src_path or "")
	if ":/tag:" in p:
		p = p.split(":/tag:", 1)[1]
	p = p.split(":/alm:", 1)[0]
	parts = p.split("/")
	if len(parts) >= 3 and parts[0] == "Boars_Head":
		return parts[2], (parts[4] if len(parts) > 5 else (parts[3] if len(parts) > 3 else "Other"))
	return "Other", "Other"


def _almCurrent(ctx):
	"""Active / unacknowledged alarm counts now per scope (system.alarm.queryStatus)."""
	out = dict((sc["id"], {"activeNow": 0, "unackedNow": 0}) for sc in ctx["scopes"])
	pri = (ctx["filters"] or {}).get("priorities") or []
	try:
		evs = system.alarm.queryStatus(state=["ActiveUnacked", "ActiveAcked"])
	except (Exception, Throwable) as e:
		LOG.warn("queryStatus failed: %s" % e)
		return out
	for ev in evs:
		try:
			if pri and str(int(ev.getPriority().ordinal())) not in pri:
				continue
			area, dev = _almPath(ev.getSource())
			unacked = "Unacked" in str(ev.getState())
		except (Exception, Throwable):
			continue
		for sc in ctx["scopes"]:
			sid = sc["id"]
			if sid == "all" or sid == "area:" + area or sid == "device:%s/%s" % (area, dev):
				out[sid]["activeNow"] += 1
				if unacked:
					out[sid]["unackedNow"] += 1
	return out


def _almFacts(ctx):
	by_t = dict((b["t"], b) for b in ctx["buckets"])
	facts = {}
	for b in ctx["buckets"]:
		for sc in ctx["scopes"]:
			facts[(b["t"], sc["id"])] = {"t": b["t"], "t1": b["t1"], "label": b["label"], "shift": b.get("shift") or "",
				"scope": sc["id"], "v": {"activations": 0, "highCount": 0, "acked": 0, "ackSec": 0.0, "cleared": 0,
				"clrSec": 0.0, "clrMaxMin": 0.0, "clrMin": 0.0}, "src": {}}
	groups = {}
	for sc in ctx["scopes"]:
		lvl = "device" if sc["id"].startswith("device:") else ("area" if sc["id"].startswith("area:") else "all")
		groups.setdefault(lvl, []).append(sc)
	grain = ctx["grain"] if ctx["grain"] in ("hour", "day", "week", "shift") else "none"
	for lvl, scs in groups.items():
		params = _almFilters(ctx, scs if lvl != "all" else [])
		params.update({"grain": grain, "groupBy": "" if lvl == "all" else lvl})
		ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "Alarms/Facts", parameters=params)
		for r in system.dataset.toPyDataSet(ds):
			t = long(system.date.toMillis(system.date.parse(unicode(r["bucket"]), "yyyy-MM-dd HH:mm:ss")))
			if grain == "none":
				t = ctx["buckets"][0]["t"]
			if t not in by_t:
				continue
			sid = "all" if lvl == "all" else ("%s:%s" % (lvl, r["grp"]))
			f = facts.get((t, sid))
			if f is None:
				continue
			v = f["v"]
			v["activations"] += int(r["activations"] or 0)
			v["highCount"] += int(r["high_cnt"] or 0)
			v["acked"] += int(r["acked"] or 0)
			v["ackSec"] += float(r["ack_sec"] or 0)
			v["cleared"] += int(r["cleared"] or 0)
			v["clrSec"] += float(r["clr_sec"] or 0)
			v["clrMin"] += float(r["clr_sec"] or 0) / 60.0
			v["clrMaxMin"] = max(v["clrMaxMin"], float(r["clr_max"] or 0) / 60.0)
	out = sorted(facts.values(), key=lambda f: (f["t"], f["scope"]))
	for f in out:
		f["src"] = dict((m["id"], "Journal") for m in ctx["measures"])
	cur = _almCurrent(ctx) if [m for m in ctx["measures"] if m.get("current")] else {}
	return {"facts": out, "current": cur}


def _almTopN(ctx, spec):
	dim = spec.get("topN") or "alarms"
	params = _almFilters(ctx)
	params.update({"dim": dim, "orderBy": spec.get("orderBy") or "count", "n": int(spec.get("n") or 10)})
	ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "Alarms/Top", parameters=params)
	pri = dict((str(i), n) for i, n in enumerate(["Diagnostic", "Low", "Medium", "High", "Critical"]))
	cols = [("Rank", "key", "left")]
	if dim == "alarms":
		cols += [("Alarm", "key", "left"), ("Device", "", "left"), ("Area", "", "left"), ("Priority", "", "left")]
	elif dim == "devices":
		cols += [("Device", "key", "left"), ("Area", "", "left")]
	else:
		cols += [("Area", "key", "left")]
	cols += [("Count", "", "right"), ("Avg Ack (min)", "", "right"), ("Avg Clear (min)", "", "right"),
		("Total Active (min)", "", "right")]
	raw, rows = [], []
	for i, r in enumerate(system.dataset.toPyDataSet(ds)):
		lead = [i + 1]
		if dim == "alarms":
			lead += [r["alarm"], r["device"], r["area"], pri.get(str(r["max_priority"]), str(r["max_priority"]))]
		elif dim == "devices":
			lead += [r["device"], r["area"]]
		else:
			lead += [r["area"]]
		nums = [int(r["cnt"] or 0), _num(r["avg_ack_min"]), _num(r["avg_clr_min"]), _num(r["total_min"])]
		raw.append(lead + nums)
		rows.append([unicode(x) for x in lead] + ["{:,}".format(nums[0])]
			+ ["--" if x is None else "{:,.1f}".format(x) for x in nums[1:]])
	return {"columns": cols, "raw": raw, "rows": rows, "demo": False}


def _almOptions(src):
	"""Area / device scope items from the journal's last 30 days (cached 10 min)."""
	now = _now()
	c = _state["options"].get(src["id"])
	if c and now - c[0] < 600000:
		return c[1]
	items = []
	try:
		s = _addD(_mid(now), -29)
		ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "Alarms/Options", parameters={
			"start": _fmtT(s, "yyyy-MM-dd HH:mm:ss"), "end": _fmtT(now, "yyyy-MM-dd HH:mm:ss"), "areas": "",
			"devices": "", "priorities": "", "shifts": ""})
		areas = []
		for r in system.dataset.toPyDataSet(ds):
			a, d = unicode(r["area"]), unicode(r["device"])
			if a not in areas:
				areas.append(a)
				items.append({"id": "area:" + a, "label": a, "level": "area", "parent": "all"})
			items.append({"id": "device:%s/%s" % (a, d), "label": d, "level": "device", "parent": "area:" + a})
	except (Exception, Throwable) as e:
		LOG.warn("alarm scope options failed: %s" % e)
	_state["options"][src["id"]] = (now, items)
	return items


def _almRecords(ctx, spec):
	"""Event List: the latest activations in the window (newest first)."""
	params = _almFilters(ctx)
	params["n"] = int(spec.get("n") or RECORDS_DEFAULT)
	ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "Alarms/Events", parameters=params)
	pri = dict((str(i), n) for i, n in enumerate(["Diagnostic", "Low", "Medium", "High", "Critical"]))
	cols = [("Active Time", "key", "left"), ("Alarm", "key", "left"), ("Device", "", "left"), ("Area", "", "left"),
		("Priority", "", "left"), ("Time To Ack (min)", "", "right"), ("Time To Clear (min)", "", "right")]
	raw, rows = [], []
	for r in system.dataset.toPyDataSet(ds):
		vals = [unicode(r["act"])[:16], r["alarm"], r["device"], r["area"], pri.get(str(r["priority"]), str(r["priority"])),
			_num(r["ack_min"]), _num(r["clr_min"])]
		raw.append(vals)
		rows.append([unicode(x) for x in vals[:5]] + ["--" if x is None else "{:,.1f}".format(x) for x in vals[5:]])
	return {"columns": cols, "raw": raw, "rows": rows}


# ------------------------------------------------------------------------------------------------ history fetcher
# Zone Temperatures, Compressors, Equipment Runtime: SQL historian (queryTagHistory, hourly) for the device members in
# the catalog (measures[].hist). Device scope items carry their tag path under historyRoot; area / all = their devices.
HIST_MODES = {"avg": ["Average"], "min": ["Minimum"], "max": ["Maximum"], "spread": ["Minimum", "Maximum"],
	"delta": ["Maximum"], "last": ["Maximum"]}


def _histDevices(src, sc):
	devs = [s for s in src.get("scope") or [] if s.get("level") == "device"]
	if sc["id"] == "all":
		return devs
	if sc["id"].startswith("area:"):
		return [s for s in devs if s.get("parent") == sc["id"]]
	return [s for s in devs if s["id"] == sc["id"]]


def _histMember(m, dev):
	h = m.get("hist") or {}
	if h.get("members"):
		return h["members"].get(dev.get("kind") or "")
	return h.get("member")


def _histHours(ctx, t0, t1):
	out = []
	t = _addH(_mid(max(t0, ctx["start"])), int((max(t0, ctx["start"]) - _mid(max(t0, ctx["start"]))) // HOUR))
	while t < min(t1, ctx["end"]):
		if not ctx["shifts"] or shiftOf(int(system.date.getHour24(system.date.fromMillis(t)))) in ctx["shifts"]:
			out.append(t)
		t = _addH(t, 1)
	return out


def _histData(ctx, devs, measures):
	"""{(path, ignitionMode): {hourStart: value}} for every device x measure member (one query per mode)."""
	root = ctx["src"].get("historyRoot") or ""
	need = {}
	for m in measures:
		for d in devs:
			mem = _histMember(m, d)
			if not mem:
				continue
			for mode in HIST_MODES.get((m.get("hist") or {}).get("mode"), []):
				need.setdefault(mode, set()).add(d["path"] + "/" + mem)
	out = {}
	allp = sorted(set(p for ps in need.values() for p in ps))
	if allp:
		bare = root.split("]", 1)[-1]
		try:
			ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "History/FirstSample",
				parameters={"paths": "|".join((bare + p).lower() for p in allp)})
			first = dict((unicode(r["tagpath"]), long(r["first_ms"])) for r in system.dataset.toPyDataSet(ds))
		except (Exception, Throwable) as e:
			LOG.warn("history start query failed: %s" % e)
			first = {}
		for p in allp:
			v = first.get((bare + p).lower())
			# first full hour after the live history row was created (earlier hours come back as 0)
			out[("__first__", p)] = (_addH(_mid(v), int((v - _mid(v)) // HOUR) + 1) if v is not None else None)
	for mode, paths in need.items():
		paths = sorted(paths)
		try:
			ds = system.tag.queryTagHistory(paths=[root + p for p in paths], startDate=system.date.fromMillis(ctx["start"]),
				endDate=system.date.fromMillis(ctx["end"]), intervalMinutes=60, aggregationMode=mode, returnFormat="Wide",
				ignoreBadQuality=True)
		except (Exception, Throwable) as e:
			LOG.warn("history query failed (%s): %s" % (mode, e))
			continue
		for r in range(ds.getRowCount()):
			t = long(system.date.toMillis(ds.getValueAt(r, 0)))
			hk = _addH(_mid(t), int((t - _mid(t)) // HOUR))
			for c, p in enumerate(paths):
				v = _num(ds.getValueAt(r, c + 1))
				if v is not None:
					out.setdefault((p, mode), {})[hk] = v
	return out


def _histDevValue(m, dev, data, hours):
	mem = _histMember(m, dev)
	if not mem:
		return None
	p = dev["path"] + "/" + mem
	h_ = m.get("hist") or {}
	mode = h_.get("mode")
	if ("__first__", p) in data:
		t0 = data[("__first__", p)]
		if t0 is None:
			return None                       # no live history for this member
		hours = [h for h in hours if h >= t0]

	def vals(ig):
		col = data.get((p, ig)) or {}
		return [col[h] for h in hours if col.get(h) is not None]
	if mode == "delta":
		# counter increase: sum of hour-to-hour rises of the hourly maximum; resets (drops), steps from 0 (a meter
		# that only just appeared) and steps above the catalog cap per hour are not counted
		col = data.get((p, "Maximum")) or {}
		seq = [(h, col[h]) for h in hours if col.get(h) is not None]
		if not seq:
			return None
		cap = _num(h_.get("cap"))
		live = [(h, v) for h, v in seq if v > 0]
		if live:
			# the meter's rise over the window when it is physically possible (the PLC keeps counting between
			# sparse history samples, so hour-to-hour steps can bunch up); otherwise the capped step sum below
			d = live[-1][1] - live[0][1]
			span = (live[-1][0] - live[0][0]) / float(HOUR) + 1.0
			if d >= 0 and (cap is None or d <= cap * span):
				return d
		tot = 0.0
		for (ha, a), (hb, b) in zip(seq, seq[1:]):
			inc = b - a
			if a > 0 and inc >= 0 and (cap is None or inc <= cap * max(1.0, (hb - ha) / float(HOUR))):
				tot += inc
		return tot
	if mode == "avg":
		v = vals("Average")
		return (sum(v) / len(v)) if v else None
	if mode == "min":
		v = vals("Minimum")
		return min(v) if v else None
	if mode == "max":
		v = vals("Maximum")
		return max(v) if v else None
	if mode == "spread":
		lo, hi = vals("Minimum"), vals("Maximum")
		if not lo or not hi:
			return None
		return max(0.0, max(hi) - min(lo))
	if mode == "last":
		v = vals("Maximum")
		return v[-1] if v else None
	return None


def _histScopeValue(m, devs, data, hours):
	"""Scope value from its devices: averages average, min / max / spread take the extreme, counters add up."""
	vals = [_histDevValue(m, d, data, hours) for d in devs]
	vals = [v for v in vals if v is not None]
	if not vals:
		return None
	mode = (m.get("hist") or {}).get("mode")
	if mode == "avg":
		return sum(vals) / len(vals)
	if mode == "min":
		return min(vals)
	if mode in ("max", "spread"):
		return max(vals)
	return sum(vals)


def _histFacts(ctx):
	src = ctx["src"]
	devs_by = dict((sc["id"], _histDevices(src, sc)) for sc in ctx["scopes"])
	alld = dict((d["id"], d) for ds in devs_by.values() for d in ds).values()
	data = _histData(ctx, list(alld), ctx["measures"])
	facts = []
	for b in ctx["buckets"]:
		hours = _histHours(ctx, b["t"], b["t1"])
		for sc in ctx["scopes"]:
			v = {}
			for m in ctx["measures"]:
				v[m["field"]] = _histScopeValue(m, devs_by[sc["id"]], data, hours) if hours else None
			facts.append({"t": b["t"], "t1": b["t1"], "label": b["label"], "shift": b.get("shift") or "", "scope": sc["id"],
				"v": v, "src": dict((m["id"], "Historian") for m in ctx["measures"])})
	return {"facts": facts, "current": {}}


def _histTopN(ctx, spec):
	"""Devices ranked by the Top N entry's measure over the whole window (+ the report's other measures)."""
	src = ctx["src"]
	tn = dict((x["id"], x) for x in src.get("topN") or []).get(spec.get("topN")) or (src.get("topN") or [{}])[0]
	key = _measure(src, tn.get("measure")) or ctx["measures"][0]
	ms = [key] + [m for m in ctx["measures"] if m["id"] != key["id"]]
	devs = []
	for sc in ctx["scopes"]:
		for d in _histDevices(src, sc):
			if d not in devs:
				devs.append(d)
	data = _histData(ctx, devs, ms)
	hours = _histHours(ctx, ctx["start"], ctx["end"])
	area = dict((s["id"], s["label"]) for s in src.get("scope") or [] if s.get("level") == "area")
	rows = []
	for d in devs:
		rows.append((d, [_histDevValue(m, d, data, hours) for m in ms]))
	desc = tn.get("dir") != "asc"
	rows.sort(key=lambda r: (r[1][0] is None, -(r[1][0] or 0) if desc else (r[1][0] or 0)))
	rows = rows[:int(spec.get("n") or 10)]
	cols = [("Rank", "key", "left"), ("Device", "key", "left"), ("Area", "", "left")] + [(header(m), "", "right") for m in ms]
	raw = [[i + 1, d["label"], area.get(d.get("parent"), "")] + vals for i, (d, vals) in enumerate(rows)]
	txt = [[unicode(r[0]), r[1], r[2]] + [fmtValue(m, v) for m, v in zip(ms, r[3:])] for r in raw]
	return {"columns": cols, "raw": raw, "rows": txt, "demo": False}


# ------------------------------------------------------------------------------------------------ out of service fetcher
def _localMs(txt):
	if txt is None or unicode(txt).strip() == "" or unicode(txt) == "None":
		return None
	try:
		return long(system.date.toMillis(system.date.parse(unicode(txt)[:19], "yyyy-MM-dd HH:mm:ss")))
	except (Exception, Throwable):
		return None


def _oosRows(ctx):
	ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "OOS/Records", parameters={
		"start": _fmtT(ctx["start"], "yyyy-MM-dd HH:mm:ss"), "end": _fmtT(ctx["end"], "yyyy-MM-dd HH:mm:ss")})
	out = []
	for r in system.dataset.toPyDataSet(ds):
		out.append({"device": unicode(r["device_name"] or ""), "area": unicode(r["area"] or ""), "type": unicode(r["device_type"] or ""),
			"reason": unicode(r["reason"] or "") or "Not Given", "by": unicode(r["taken_name"] or r["taken_by"] or ""),
			"t0": _localMs(r["taken_at"]), "t1": _localMs(r["returned_at"]), "retBy": unicode(r["returned_name"] or ""),
			"status": unicode(r["status"] or ""), "memo": unicode(r["memo"] or "")})
	return [r for r in out if r["t0"] is not None]


def _oosMatch(sc, r):
	sid = sc["id"]
	return sid == "all" or sid == "area:" + r["area"] or sid == "device:%s/%s" % (r["area"], r["device"])


def _oosOverlap(r, t0, t1, now):
	e = r["t1"] if r["t1"] is not None else now
	return max(0, min(e, t1) - max(r["t0"], t0))


def _oosFacts(ctx):
	rows = _oosRows(ctx)
	now = _now()
	facts = []
	for b in ctx["buckets"]:
		t0, t1 = max(b["t"], ctx["start"]), min(b["t1"], ctx["end"])
		for sc in ctx["scopes"]:
			rs = [r for r in rows if _oosMatch(sc, r)]
			ov = [(r, _oosOverlap(r, t0, t1, now)) for r in rs]
			ret = [r for r in rs if r["t1"] is not None and t0 <= r["t1"] < t1]
			v = {"taken": len([r for r in rs if t0 <= r["t0"] < t1]), "returned": len(ret),
				"devices": len(set((r["area"], r["device"]) for r, o in ov if o > 0)),
				"oosHours": sum(o for r, o in ov) / float(HOUR),
				"durHours": sum((r["t1"] - r["t0"]) for r in ret) / float(HOUR)}
			facts.append({"t": b["t"], "t1": b["t1"], "label": b["label"], "shift": b.get("shift") or "", "scope": sc["id"],
				"v": v, "src": dict((m["id"], "Log") for m in ctx["measures"])})
	cur = {}
	for sc in ctx["scopes"]:
		cur[sc["id"]] = {"outNow": len(set((r["area"], r["device"]) for r in rows if r["t1"] is None and _oosMatch(sc, r)))}
	return {"facts": facts, "current": cur}


def _oosTopN(ctx, spec):
	rows = [r for r in _oosRows(ctx) if any(_oosMatch(sc, r) for sc in ctx["scopes"])]
	now = _now()
	dim = spec.get("topN") or "devices"
	agg = {}
	for r in rows:
		k = (r["device"], r["area"]) if dim == "devices" else (r["reason"], "")
		a = agg.setdefault(k, {"count": 0, "hours": 0.0, "devs": set(), "open": False})
		if ctx["start"] <= r["t0"] < ctx["end"]:
			a["count"] += 1
		a["hours"] += _oosOverlap(r, ctx["start"], ctx["end"], now) / float(HOUR)
		a["devs"].add((r["area"], r["device"]))
		a["open"] = a["open"] or r["t1"] is None
	order = "count" if spec.get("orderBy") == "count" else "hours"
	keys = sorted(agg.keys(), key=lambda k: (-agg[k][order], -agg[k]["hours"], k))[:int(spec.get("n") or 10)]
	if dim == "devices":
		cols = [("Rank", "key", "left"), ("Device", "key", "left"), ("Area", "", "left"), ("Out Now", "", "left"),
			("Times Taken Out", "", "right"), ("Hours Out Of Service", "", "right")]
		raw = [[i + 1, k[0], k[1], "Yes" if agg[k]["open"] else "No", agg[k]["count"], round(agg[k]["hours"], 1)]
			for i, k in enumerate(keys)]
	else:
		cols = [("Rank", "key", "left"), ("Reason", "key", "left"), ("Times Taken Out", "", "right"),
			("Hours Out Of Service", "", "right"), ("Devices", "", "right")]
		raw = [[i + 1, k[0], agg[k]["count"], round(agg[k]["hours"], 1), len(agg[k]["devs"])] for i, k in enumerate(keys)]
	rows_txt = [[(("{:,.1f}".format(x) if isinstance(x, float) else ("{:,}".format(x) if isinstance(x, (int, long)) and j > 0
		else unicode(x)))) for j, x in enumerate(r)] for r in raw]
	return {"columns": cols, "raw": raw, "rows": rows_txt, "demo": False}


def _oosRecords(ctx, spec):
	rows = [r for r in _oosRows(ctx) if any(_oosMatch(sc, r) for sc in ctx["scopes"])][:int(spec.get("n") or RECORDS_DEFAULT)]
	now = _now()
	cols = [("Taken Out", "key", "left"), ("Device", "key", "left"), ("Area", "", "left"), ("Reason", "", "left"),
		("Taken By", "", "left"), ("Returned", "", "left"), ("Hours", "", "right"), ("Memo", "", "left")]
	raw = []
	for r in rows:
		hrs = ((r["t1"] if r["t1"] is not None else now) - r["t0"]) / float(HOUR)
		raw.append([_fmtT(r["t0"], "MM/dd/yyyy HH:mm"), r["device"], r["area"], r["reason"], r["by"],
			_fmtT(r["t1"], "MM/dd/yyyy HH:mm") if r["t1"] is not None else "Still Out", round(hrs, 1), r["memo"][:120]])
	return {"columns": cols, "raw": raw, "rows": [[unicode(x) if not isinstance(x, float) else "{:,.1f}".format(x)
		for x in r] for r in raw]}


def _oosOptions(src):
	now = _now()
	c = _state["options"].get(src["id"])
	if c and now - c[0] < 600000:
		return c[1]
	items = []
	try:
		areas = []
		for r in system.dataset.toPyDataSet(system.db.runNamedQuery(project=PROJECT, path=NQ + "OOS/Options", parameters={})):
			a, d = unicode(r["area"]), unicode(r["device"])
			if a not in areas:
				areas.append(a)
				items.append({"id": "area:" + a, "label": a, "level": "area", "parent": "all"})
			items.append({"id": "device:%s/%s" % (a, d), "label": d, "level": "device", "parent": "area:" + a})
	except (Exception, Throwable) as e:
		LOG.warn("out of service scope options failed: %s" % e)
	_state["options"][src["id"]] = (now, items)
	return items


# ------------------------------------------------------------------------------------------------ forms fetcher
FORM_LABELS = {"DailyRounds": "Daily Rounds Log", "ShiftLog": "NH3 Shift Log"}


def _formRows(ctx):
	s = ctx.get("session")
	user = username(s)
	try:
		view_all = bool(shared.Security.allowed(s, "Forms", "ViewAll"))
	except (Exception, Throwable):
		view_all = False
	ds = system.db.runNamedQuery(project=PROJECT, path=NQ + "Forms/Submissions", parameters={
		"start": _fmtT(ctx["start"], "yyyy-MM-dd HH:mm:ss"), "end": _fmtT(ctx["end"], "yyyy-MM-dd HH:mm:ss"),
		"username": user, "viewAll": view_all})
	out = []
	for r in system.dataset.toPyDataSet(ds):
		t = _localMs(r["submitted_at"])
		if t is None:
			continue
		if ctx["shifts"] and shiftOf(int(system.date.getHour24(system.date.fromMillis(t)))) not in ctx["shifts"]:
			continue
		out.append({"t": t, "type": unicode(r["form_type"] or ""), "date": unicode(r["form_date"] or ""),
			"by": unicode(r["submitted_name"] or r["submitted_by"] or ""), "status": unicode(r["shift_status"] or ""),
			"abnormal": bool(r["is_abnormal"]), "release": bool(r["release_logged"]), "open": bool(r["open_items"]),
			"summary": unicode(r["summary"] or "")})
	return out


def _formMatch(sc, r):
	return sc["id"] == "all" or sc["id"] == "form:" + r["type"]


def _formFacts(ctx):
	rows = _formRows(ctx)
	facts = []
	for b in ctx["buckets"]:
		t0, t1 = max(b["t"], ctx["start"]), min(b["t1"], ctx["end"])
		for sc in ctx["scopes"]:
			rs = [r for r in rows if _formMatch(sc, r) and t0 <= r["t"] < t1]
			v = {"subs": len(rs), "daily": len([r for r in rs if r["type"] == "DailyRounds"]),
				"shiftLogs": len([r for r in rs if r["type"] == "ShiftLog"]),
				"abnormal": len([r for r in rs if r["abnormal"]]), "releases": len([r for r in rs if r["release"]]),
				"openItems": len([r for r in rs if r["open"]])}
			facts.append({"t": b["t"], "t1": b["t1"], "label": b["label"], "shift": b.get("shift") or "", "scope": sc["id"],
				"v": v, "src": dict((m["id"], "Forms") for m in ctx["measures"])})
	return {"facts": facts, "current": {}}


def _formTopN(ctx, spec):
	rows = [r for r in _formRows(ctx) if any(_formMatch(sc, r) for sc in ctx["scopes"])]
	agg = {}
	for r in rows:
		a = agg.setdefault(r["by"], [0, 0, 0, 0])
		a[0] += 1
		a[1] += 1 if r["type"] == "DailyRounds" else 0
		a[2] += 1 if r["type"] == "ShiftLog" else 0
		a[3] += 1 if r["abnormal"] else 0
	keys = sorted(agg.keys(), key=lambda k: (-agg[k][0], k))[:int(spec.get("n") or 10)]
	cols = [("Rank", "key", "left"), ("Submitted By", "key", "left"), ("Forms Submitted", "", "right"),
		("Daily Rounds Logs", "", "right"), ("NH3 Shift Logs", "", "right"), ("Abnormal Shifts", "", "right")]
	raw = [[i + 1, k] + agg[k] for i, k in enumerate(keys)]
	return {"columns": cols, "raw": raw, "rows": [[unicode(x) for x in r] for r in raw], "demo": False}


def _formRecords(ctx, spec):
	rows = [r for r in _formRows(ctx) if any(_formMatch(sc, r) for sc in ctx["scopes"])][:int(spec.get("n") or RECORDS_DEFAULT)]
	cols = [("Submitted", "key", "left"), ("Form", "key", "left"), ("Form Date", "", "left"), ("Submitted By", "", "left"),
		("Shift Status", "", "left"), ("Flags", "", "left"), ("Summary", "", "left")]
	raw = []
	for r in rows:
		flags = ", ".join([x for x, on in (("Abnormal", r["abnormal"]), ("Release", r["release"]), ("Open Items", r["open"])) if on])
		raw.append([_fmtT(r["t"], "MM/dd/yyyy HH:mm"), FORM_LABELS.get(r["type"], r["type"]), r["date"], r["by"],
			r["status"] or "--", flags or "--", r["summary"][:160]])
	return {"columns": cols, "raw": raw, "rows": [[unicode(x) for x in r] for r in raw]}


FETCHERS = {
	"production": {"facts": _prodFacts, "topn": _prodTopN},
	"alarms": {"facts": _almFacts, "topn": _almTopN, "options": _almOptions, "records": _almRecords},
	"history": {"facts": _histFacts, "topn": _histTopN},
	"oos": {"facts": _oosFacts, "topn": _oosTopN, "options": _oosOptions, "records": _oosRecords},
	"forms": {"facts": _formFacts, "topn": _formTopN, "records": _formRecords},
}


# ------------------------------------------------------------------------------------------------ engine
def _scopeObjs(src, ids):
	items = dict((s["id"], s) for s in (src.get("scope") or []))
	out = []
	for i in ids:
		if i in items:
			out.append(items[i])
		elif i.startswith("area:"):
			out.append({"id": i, "label": i[5:], "level": "area", "parent": "all"})
		elif i.startswith("device:"):
			a, _, d = i[7:].partition("/")
			out.append({"id": i, "label": "%s / %s" % (a, d), "level": "device", "parent": "area:" + a})
	return out


def _context(d, src, grain=None, shifts=None):
	s, e = window(d)
	g = grain or d["breakdown"]
	sh = d["shifts"] if shifts is None else shifts
	return {"def": d, "src": src, "measures": [_measure(src, m) for m in d["measures"]],
		"scopes": _scopeObjs(src, d["scope"]), "start": s, "end": e, "grain": g, "shifts": sh,
		"filters": d.get("filters") or {}, "buckets": buckets(s, e, g, sh)}


def _srcNote(srcs):
	"""Section note about the data source: none (labels removed at the user's request)."""
	return ""


def _srcNoteUnused(srcs):
	kinds = sorted(set(srcs))
	if not kinds:
		return ""
	if kinds == ["Demo"]:
		return "Demo Data"
	if "Demo" in kinds:
		return "Mixed: Historian + Demo Data"
	return " + ".join(kinds)


def _cards(ctx, res):
	facts, cur = res["facts"], res.get("current") or {}
	multi = len(ctx["scopes"]) > 1
	scs = ctx["scopes"] if len(ctx["scopes"]) <= 4 else [None]
	if multi and len(scs) * len(ctx["measures"]) > 16:
		scs = scs[:1]          # many measures x scopes: cards for the first (top) scope, the table has the rest
	cards, srcs = [], []
	for sc in scs:
		fs = [f for f in facts if sc is None or f["scope"] == sc["id"]]
		for m in ctx["measures"]:
			if sc is not None and not _applies(m, sc["level"]):
				continue
			label = m["label"] if not multi else ("%s - %s" % (sc["label"] if sc else "All Selected", m["label"]))
			if m.get("current"):
				v = sum((cur.get(s2["id"]) or {}).get(m["field"], 0) for s2 in ([sc] if sc else ctx["scopes"]))
				cards.append({"label": label, "value": fmtValue(m, v, True), "sub": "Right Now", "raw": v,
					"unit": m.get("unit")})
				continue
			if sc is None:
				per = []
				for s2 in ctx["scopes"]:
					per.append(aggregate(m, [f["v"] for f in fs if f["scope"] == s2["id"]]))
				per = [x for x in per if x is not None]
				v = (sum(per) if m.get("agg") in ("sum", "count") else (sum(per) / len(per))) if per else None
			else:
				v = aggregate(m, [f["v"] for f in fs])
			sub = ""
			bvals = [mvalue(m, f["v"]) for f in fs]
			bvals = [x for x in bvals if x is not None]
			if len(fs) > 1 and m.get("agg") in ("avg", "ratio") and bvals:
				sub = "Min %s / Max %s" % (fmtValue(m, min(bvals)), fmtValue(m, max(bvals)))
			elif len(fs) > 1 and m.get("agg") == "sum":
				sub = "Total Of %d %s" % (len(set(f["t"] for f in fs)), _grainWord(ctx["grain"], len(set(f["t"] for f in fs))))
			ss = [f["src"].get(m["id"]) for f in fs if f["src"].get(m["id"])]
			srcs += ss
			cards.append({"label": label, "value": fmtValue(m, v, True), "sub": sub, "raw": v, "unit": m.get("unit")})
	return {"type": "cards", "title": "Summary", "note": _srcNote(srcs), "cards": cards}


def _grainWord(g, n):
	w = {"hour": "Hour", "shift": "Shift", "day": "Day", "week": "Week"}.get(g, "Period")
	return w + ("s" if n != 1 else "")


def _trend(ctx, res):
	facts = res["facts"]
	if ctx["grain"] == "none" or len(set(f["t"] for f in facts)) < 2:
		return {"type": "trend", "title": "Trend Chart",
			"note": "One Period Only - Pick A Finer Breakdown (Hour / Shift / Day / Week) For A Trend", "charts": []}
	pens = []
	for m in ctx["measures"]:
		if m.get("current"):
			continue
		for sc in ctx["scopes"]:
			if _applies(m, sc["level"]):
				pens.append((m, sc))
	by_unit = []
	for m, sc in pens:
		u = m.get("unit") or ""
		grp = None
		for g in by_unit:
			if g["unit"] == u and len(g["pens"]) < MAX_PENS:
				grp = g
		if grp is None:
			grp = {"unit": u, "pens": []}
			by_unit.append(grp)
		grp["pens"].append((m, sc))
	charts, srcs = [], []
	multi = len(ctx["scopes"]) > 1
	for g in by_unit:
		series = []
		labels = []
		for m, sc in g["pens"]:
			name = m["label"] if not multi else "%s %s" % (sc["label"], m["label"])
			pts = []
			for f in facts:
				if f["scope"] == sc["id"]:
					v = mvalue(m, f["v"])
					pts.append([f["t"], None if v is None else round(v, int(m.get("decimals") or 0) + 1)])
					if f["src"].get(m["id"]):
						srcs.append(f["src"][m["id"]])
			series.append({"name": name, "data": pts})
			if m["label"] not in labels:
				labels.append(m["label"])
		u = g["unit"]
		title = ", ".join(labels) + ("" if u in ("", "count") else " (%s)" % u)
		charts.append({"title": title, "unit": u, "series": series})
	return {"type": "trend", "title": "Trend Chart", "note": _srcNote(srcs), "charts": charts}


def _table(ctx, res, kind="table"):
	facts = res["facts"]
	multi = len(ctx["scopes"]) > 1
	ms = [m for m in ctx["measures"] if not m.get("current") and
		any(_applies(m, sc["level"]) for sc in ctx["scopes"])]
	cols = []
	if kind == "shifts":
		cols.append(("Shift", "key", "left"))
	elif ctx["grain"] != "none":
		cols.append(({"hour": "Hour", "shift": "Shift", "day": "Day", "week": "Week"}[ctx["grain"]], "key", "left"))
	if multi or not cols:
		cols.append(("Scope", "key", "left"))
	cols += [(header(m), "", "right") for m in ms]
	show_src = False          # no Data (Demo / Historian) column
	if show_src:
		cols.append(("Data", "", "left"))
	scope_order = dict((sc["id"], i) for i, sc in enumerate(ctx["scopes"]))
	labels = dict((sc["id"], sc["label"]) for sc in ctx["scopes"])
	levels = dict((sc["id"], sc["level"]) for sc in ctx["scopes"])
	groups = []
	if kind == "shifts":
		for L in ("A", "B", "C"):
			for sc in ctx["scopes"]:
				fs = [f for f in facts if f["shift"] == L and f["scope"] == sc["id"]]
				if fs:
					groups.append(("Shift " + L, sc["id"], fs))
	else:
		for f in sorted(facts, key=lambda f: (f["t"], scope_order.get(f["scope"], 0))):
			groups.append((f["label"], f["scope"], [f]))
	raw, rows, srcs = [], [], []
	for key, sid, fs in groups:
		lead = [key] if (kind == "shifts" or ctx["grain"] != "none") else []
		if multi or not lead:
			lead.append(labels.get(sid, sid))
		vals, txt = [], []
		ss = []
		for m in ms:
			if not _applies(m, levels.get(sid)):
				vals.append(None)
				txt.append("")
				continue
			v = aggregate(m, [f["v"] for f in fs])
			vals.append(v)
			txt.append(fmtValue(m, v))
			ss += [f["src"].get(m["id"]) for f in fs if f["src"].get(m["id"])]
		srcs += ss
		tail = []
		if show_src:
			k = sorted(set(ss))
			tail = ["Demo" if k == ["Demo"] else ("Historian" if k == ["Historian"] else ("Mixed" if k else ""))]
		raw.append(lead + vals + tail)
		rows.append([unicode(x) for x in lead] + txt + tail)
	title = {"shifts": "Shift Comparison", "table": "Table"}[kind]
	note = _srcNote(srcs)
	if kind == "shifts":
		note = ("All Three Shifts  |  " + note) if note else "All Three Shifts"
	return {"type": kind, "title": title, "note": note, "columns": cols, "raw": raw, "rows": rows}


def run(session, defn, preview=False):
	"""Run a report definition for the session: {ok, message, definition, meta, sections}."""
	t_start = _now()
	if not allowed(session, "Use"):
		shared.Security.require("Reports", "Use", "run report", session)
		return {"ok": False, "message": "Access Denied - Reports Need The Reports Permission (Maintenance Or Above).",
			"sections": [], "meta": {}}
	d = normalize(defn)
	src = source(d["source"])
	if not sourceAllowed(session, src):
		shared.Security.require("Reports", (src.get("permission") or "").partition("/")[2], "run report", session)
		return {"ok": False, "message": "Access Denied - No Permission For %s Reports." % src["label"],
			"sections": [], "meta": {}}
	fx = FETCHERS[src["fetcher"]]
	ctx = _context(d, src)
	ctx["session"] = session
	sections = []
	all_srcs = []
	try:
		res = None
		for sec in d["sections"]:
			if not sec.get("on"):
				continue
			st = sec["type"]
			if st in ("cards", "trend", "table") and res is None:
				res = fx["facts"](ctx)
				for f in res["facts"]:
					all_srcs += f["src"].values()
			if st == "cards":
				sections.append(_cards(ctx, res))
			elif st == "trend":
				sections.append(_trend(ctx, res))
			elif st == "table":
				sections.append(_table(ctx, res))
			elif st == "shifts":
				c2 = _context(d, src, grain="shift", shifts=[])
				c2["session"] = session
				r2 = fx["facts"](c2)
				for f in r2["facts"]:
					all_srcs += f["src"].values()
				sections.append(_table(c2, r2, "shifts"))
			elif st == "topn":
				tn = dict((x["id"], x) for x in src.get("topN") or []).get(sec.get("topN")) or {}
				r = fx["topn"](ctx, sec)
				obl = dict((o["value"], o["label"]) for o in tn.get("orderBy") or []).get(sec.get("orderBy"), "")
				if r.get("demo"):
					all_srcs.append("Demo")
				sections.append({"type": "topn", "title": "%s (Top %d By %s)" % (tn.get("label", "Top N"), sec["n"], obl),
					"note": "", "columns": r["columns"], "raw": r["raw"],
					"rows": r["rows"]})
			elif st == "records" and fx.get("records"):
				r = fx["records"](ctx, sec)
				sections.append({"type": "records", "title": "Event List", "note": "Newest First, Up To %d Rows" % sec.get(
					"n", RECORDS_DEFAULT), "columns": r["columns"], "raw": r["raw"], "rows": r["rows"]})
			elif st == "notes" and d.get("notes"):
				lines = [l for l in d["notes"].split("\n")]
				sections.append({"type": "notes", "title": "Notes", "note": "", "columns": [("Notes", "key", "left")],
					"raw": [[l] for l in lines], "rows": [[l] for l in lines]})
	except (Exception, Throwable) as e:
		LOG.error("report run failed (%s): %s" % (d["source"], e))
		return {"ok": False, "message": "Report Failed: %s" % e, "sections": [], "meta": {}, "definition": d}
	shift_txt = "All Shifts" if not d["shifts"] else ", ".join("Shift " + s for s in d["shifts"])
	scope_txt = ", ".join(sc["label"] for sc in ctx["scopes"]) or "All"
	filt_txt = ""
	if (d.get("filters") or {}).get("priorities"):
		pn = dict((o["value"], o["label"]) for f in src.get("filters") or [] if f["id"] == "priorities"
			for o in f["options"])
		filt_txt = "  |  Priority: " + ", ".join(pn.get(p, p) for p in d["filters"]["priorities"])
	bd = dict((b["id"], b["label"]) for b in src.get("breakdowns") or []).get(d["breakdown"], d["breakdown"])
	meta = {"title": d["title"] or _autoTitle(d), "source": src["id"], "sourceLabel": src["label"],
		"subtitle": "%s  |  %s  |  %s  |  %s  |  %s%s" % (src["label"], scope_txt, _windowLabel(d), shift_txt, bd,
			filt_txt),
		"dataNote": "", "isDemo": False, "generatedBy": displayName(session),
		"generatedAt": system.date.format(system.date.now(), "yyyy-MM-dd HH:mm"),
		"elapsedMs": _now() - t_start, "window": [ctx["start"], ctx["end"]], "empty": _isEmpty(sections),
		"sectionLabels": [s["title"] for s in sections]}
	return {"ok": True, "message": "", "definition": d, "meta": meta, "sections": sections}


def _isEmpty(sections):
	"""True when nothing in the report has data (every card blank / zero, every table without rows)."""
	for s in sections:
		if s["type"] == "cards":
			if any(c.get("raw") not in (None, 0, 0.0) for c in s["cards"]):
				return False
		elif s["type"] == "trend":
			if any(p[1] not in (None, 0, 0.0) for c in s.get("charts") or [] for se in c["series"] for p in se["data"]):
				return False
		elif s["type"] == "notes":
			continue
		elif s["type"] in ("table", "shifts"):
			nk = len([c for c in s["columns"] if c[1] == "key"])
			if any(isinstance(x, (int, long, float)) and x != 0 for r in s.get("raw") or [] for x in r[nk:]):
				return False
		elif s.get("rows"):
			return False
	return True


# ------------------------------------------------------------------------------------------------ builder view helpers
# builder preview geometry (px) - the view heights are computed from these so no embed over / underflows
CARD_ROW = 104             # preview KPI card 92 + 12 gap
CARDS_PER_ROW = 4
CHART_H = 236              # PreviewChart instance (title 18 + chart 210 + slack)
TABLE_HEAD = 36            # table header row
SEC_BAR = 32               # PreviewSection title 20 + gap 12
PREVIEW_W = 812            # minimum usable table width of the preview pane (1366 x 768 laptop popup)
PREVIEW_COLS = 9           # max columns of one preview table (wider tables split like the PDF)


def _tableCols(cols, rows=None, width=None):
	"""Perspective table columns that fit PREVIEW_W exactly: each column gets what its longest header word and its
	values need (headers never break inside a word), scaled to the pane; long values wrap (white-space normal) and
	every cell is aligned with its header."""
	rows = rows or []
	need = []
	for i, (title, kind, align) in enumerate(cols):
		word = max([len(w) for w in unicode(title).split()] or [4])
		vals = max([len(unicode(r[i])) for r in rows[:PREVIEW_ROWS]] or [4])
		need.append(max(word * 7.6 + 16, min(vals, 22) * 6.8 + 14, 44))
	W = float(width or PREVIEW_W)
	scale = W / float(sum(need) or 1)
	if scale < 1.0:   # too wide: shrink only the columns wider than their header word (text wraps instead)
		floor = [max(len(w) for w in (unicode(c[0]).split() or ["xxxx"])) * 7.6 + 16 for c in cols]
		extra = sum(n - f for n, f in zip(need, floor))
		over = sum(need) - W
		widths = [f + (n - f) * max(0.0, 1.0 - over / float(extra or 1)) for n, f in zip(need, floor)]
	else:
		widths = [n * scale for n in need]
	out = []
	for i, (title, kind, align) in enumerate(cols):
		w = int(widths[i])
		just = "left" if align == "left" else "right"
		out.append({"field": "c%d" % i, "visible": True, "editable": False, "render": "auto", "justify": just,
			"align": "center", "resizable": False, "sortable": False, "sort": "none", "strictWidth": True, "width": w,
			"style": {"classes": "Fonts/Value fs-12" + (" fw-600" if kind else ""), "textAlign": just,
				"whiteSpace": "normal", "lineHeight": "1.15", "overflow": "hidden", "wordBreak": "break-word"},
			"header": {"title": title, "justify": just, "align": "center",
				"style": {"classes": "Fonts/Label fw-600 fs-11", "whiteSpace": "normal", "lineHeight": "1.1",
					"textAlign": just, "wordBreak": "normal", "overflowWrap": "normal"}}})
	return out


def _tableParts(s):
	"""Split a table section into parts of <= PREVIEW_COLS columns (key columns repeated), like the PDF."""
	cols = s["columns"]
	keys = [i for i, c in enumerate(cols) if c[1] == "key"]
	vals = [i for i, c in enumerate(cols) if c[1] != "key"]
	per = max(1, PREVIEW_COLS - len(keys))
	parts = [vals[i:i + per] for i in range(0, len(vals), per)] or [[]]
	out = []
	for n, part in enumerate(parts):
		idx = keys + part
		title = s["title"] + ("" if len(parts) == 1 else " (%d Of %d)" % (n + 1, len(parts)))
		out.append((title, [cols[i] for i in idx], [[row[i] for i in idx] for row in s["rows"]]))
	return out


def paneWidth(vw=None):
	"""Usable table width of the preview pane for a browser viewport width (popupPosition sizes the popup)."""
	try:
		w = popupPosition(None)["width"] if not vw else int(max(min(POPUP_MIN[0], vw),
			min(POPUP_MAX[0], int(vw) - 2 * POPUP_MARGIN)))
	except (Exception, Throwable):
		return PREVIEW_W
	return max(PREVIEW_W, w - 48 - 24 - 360 - 40 - 14)     # body padding, gap, rail, panel padding, scrollbar


def preview(session, defn, width=None):
	"""Builder preview: cards, Apex series and the first PREVIEW_ROWS rows of each table (Perspective-ready)."""
	r = run(session, defn, preview=True)
	out = {"ok": r["ok"], "message": r.get("message", ""), "meta": r.get("meta") or {}, "sections": []}
	for s in r.get("sections") or []:
		base = {"type": s["type"], "title": s["title"], "note": s.get("note") or "", "cards": [], "charts": [],
			"columns": [], "data": [], "more": "", "rowHeight": 30}
		if s["type"] == "cards":
			p = dict(base)
			p["cards"] = [{"label": c["label"], "value": c["value"], "sub": c["sub"],
				"demo": False} for c in s["cards"]]
			out["sections"].append(p)
		elif s["type"] == "trend":
			p = dict(base)
			for c in s["charts"][:2]:
				p["charts"].append({"title": c["title"], "series": c["series"] or [{"name": "", "data": []}]})
			if len(s["charts"]) > 2:
				p["more"] = "Showing 2 Of %d Charts - Every Chart Is In The Output" % len(s["charts"])
			out["sections"].append(p)
		else:
			for title, cols, rows in _tableParts(s):
				p = dict(base)
				p["title"] = title
				p["columns"] = _tableCols(cols, rows, width)
				# header lines: the title wraps at the column width (~6.5 px per character at 11 px bold)
				lines = max([-(-len(c["header"]["title"]) * 13 // (2 * max(20, c["width"] - 14))) for c in p["columns"]] or [1])
				p["headHeight"] = 12 + 14 * max(1, lines)
				longest = max([len(unicode(row[i])) for row in rows[:PREVIEW_ROWS] for i, c in enumerate(cols)
					if c[2] == "left"] or [0])
				p["rowHeight"] = 34 if longest > 18 else 28
				p["data"] = [dict(("c%d" % i, v) for i, v in enumerate(row)) for row in rows[:PREVIEW_ROWS]]
				if len(rows) > PREVIEW_ROWS:
					p["more"] = "Showing %d Of %d Rows - The Full Table Is In The Output" % (PREVIEW_ROWS, len(rows))
				out["sections"].append(p)
	return out


def previewInstances(session, defn, vw=None):
	"""Flex repeater instances for the builder's preview pane (+ exact per-section height) and the run meta.
	vw = the browser viewport width (page.props.dimensions.viewport.width), so tables fill the pane."""
	p = preview(session, defn, paneWidth(vw))
	inst = []
	for s in p["sections"]:
		h = SEC_BAR + (22 if s["more"] else 0) + (18 if s["note"] else 0)
		if s["type"] == "cards":
			h += CARD_ROW * ((len(s["cards"]) + CARDS_PER_ROW - 1) // CARDS_PER_ROW)
		elif s["type"] == "trend":
			h += CHART_H * len(s["charts"]) if s["charts"] else 0
		else:
			h += max(TABLE_HEAD, s.get("headHeight") or 0) + 6 + s["rowHeight"] * max(1, len(s["data"])) + 12
		inst.append({"sec": s, "instancePosition": {"basis": "%dpx" % h, "grow": 0, "shrink": 0},
			"instanceStyle": {"classes": ""}})
	meta = p["meta"] or {}
	return {"ok": p["ok"], "message": p["message"], "meta": meta, "instances": inst,
		"empty": bool(p["ok"] and meta.get("empty")), "ran": True}


def sectionItems(session, defn):
	d = normalize(defn)
	src = source(d["source"])
	labels = dict((t["id"], t["label"]) for t in catalog()["sectionTypes"])
	tn = [{"value": x["id"], "label": x["label"]} for x in src.get("topN") or []]
	obs = dict((x["id"], [{"value": o["value"], "label": o["label"]} for o in x.get("orderBy") or []])
		for x in src.get("topN") or [])
	out = []
	for i, s in enumerate(d["sections"]):
		hint = ""
		if s["type"] == "records":
			hint = "Newest %d Rows" % s.get("n", RECORDS_DEFAULT)
		out.append({"sec": {"type": s["type"], "label": labels.get(s["type"], s["type"]), "on": s["on"],
			"first": i == 0, "last": i == len(d["sections"]) - 1, "topN": s.get("topN", ""), "n": s.get("n", 10),
			"orderBy": s.get("orderBy", ""), "topNOptions": tn, "orderOptions": obs.get(s.get("topN"), []),
			"hint": hint}, "instancePosition": {"basis": "80px" if s["type"] == "topn" else "44px", "grow": 0,
			"shrink": 0}})
	return out


# ------------------------------------------------------------------------------------------------ builder model
BD_SHORT = {"none": "Total", "hour": "By Hour", "shift": "By Shift", "day": "By Day", "week": "By Week"}
SCOPE_TITLES = {"alarms": "Areas & Devices", "zoneTemps": "Units", "compressors": "Compressors",
	"runtime": "Equipment", "oos": "Areas & Devices", "forms": "Forms", "production": "Line, Zones & Units"}
SHIFT_HOURS = (("A", "07:00 - 15:00"), ("B", "15:00 - 23:00"), ("C", "23:00 - 07:00"))


def _tile(id_, label, detail, selected, kind):
	return {"item": {"id": id_, "label": label, "detail": detail or "", "selected": bool(selected), "kind": kind}}


def _rangeText(preset):
	"""Second line of a time tile: the dates the preset covers right now."""
	s, e = window({"time": {"preset": preset}})
	last = e - 1 if e > s else s
	if preset == "lastShift":
		return "Shift %s, %s - %s" % (shiftOf(int(system.date.getHour24(system.date.fromMillis(s)))), _fmtT(s, "HH:mm"),
			_fmtT(e, "HH:mm"))
	if preset == "today":
		return "%s From 00:00" % _fmtT(s, "MM/dd")
	if preset == "yesterday":
		return _fmtT(s, "MM/dd")
	return "%s - %s" % (_fmtT(s, "MM/dd"), _fmtT(last, "MM/dd"))


def _joinLabels(labels, most=3):
	labels = [l for l in labels if l]
	if len(labels) <= most:
		return ", ".join(labels) or "--"
	return "%s + %d More" % (", ".join(labels[:most]), len(labels) - most)


def _unitText(m):
	u = m.get("unit") or ""
	return "" if u in COUNT_UNITS or u == "%" else " (%s)" % u


def builderModel(session, defn):
	"""Everything the report builder shows for one definition: Step 1 source cards and quick reports, Step 2 time /
	group-by / shift tiles, Step 3 scope and measure rows, advanced sections and filters, and the right-rail summary.
	The view has exactly one computing binding (this call); every component binds to a key of the result."""
	cc = clientCatalog(session)
	srcs = cc["sources"]
	if not srcs:
		return {"ok": False, "sources": [], "quick": [], "time": [], "groupBy": [], "shifts": [], "scope": [],
			"measures": [], "sections": [], "filters": [], "summary": [], "scopeTitle": "", "filterLabel": ""}
	d = normalize(defn)
	src = source(d["source"])
	cards = [{"item": {"id": s["id"], "label": s["label"], "description": s.get("description") or "",
		"meta": s.get("meta") or "", "icon": s.get("icon") or "material/assessment", "selected": s["id"] == d["source"]}}
		for s in srcs]
	quick = [_tile(p["id"], p["label"], p.get("detail") or "", False, "preset") for p in cc.get("presets") or []]
	tp = d["time"]["preset"]
	time = []
	for k, lbl in TIME_PRESETS:
		det = (_windowLabel(d, True) if tp == "custom" else "Pick Dates") if k == "custom" else _rangeText(k)
		time.append(_tile(k, lbl, det, tp == k, "time"))
	bds = [_tile(b["id"], BD_SHORT.get(b["id"], b["label"]), "", d["breakdown"] == b["id"], "breakdown")
		for b in src.get("breakdowns") or []]
	has_shifts = any(f["id"] == "shifts" for f in src.get("filters") or [])
	shifts = []
	if has_shifts:
		shifts.append(_tile("all", "All Shifts", "24 Hours", not d["shifts"], "shift"))
		for L, hh in SHIFT_HOURS:
			shifts.append(_tile(L, "Shift " + L, hh, L in d["shifts"], "shift"))
	on = set(d["scope"])
	scope = [{"item": {"id": s["id"], "label": s["label"], "on": s["id"] in on, "kind": "scope", "indent": s["indent"],
		"head": False}} for s in scopeTree(session, d["source"])]
	sel = set(d["measures"])
	mrows = []
	for g in measureGroups(session, d["source"]):
		mrows.append({"item": {"id": g["id"], "label": g["label"], "on": False, "kind": "group", "indent": 0, "head": True}})
		for mm in g["measures"]:
			m = _measure(src, mm["id"])
			mrows.append({"item": {"id": m["id"], "label": m["label"] + _unitText(m), "on": m["id"] in sel, "kind": "measure",
				"indent": 0, "head": False}})
	filters, flabel = [], ""
	for f in src.get("filters") or []:
		if f["id"] == "shifts":
			continue
		flabel = flabel or f["label"]
		cur = d["filters"].get(f["id"]) or []
		for o in f.get("options") or []:
			filters.append(_tile(str(o["value"]), o["label"], "", str(o["value"]) in cur, "filter:" + f["id"]))
	labels = dict((t["id"], t["label"]) for t in catalog()["sectionTypes"])
	summary = [{"key": "Data Source", "value": src["label"]},
		{"key": "Time Range", "value": "%s, %s" % (_windowLabel(d), BD_SHORT.get(d["breakdown"], d["breakdown"]))}]
	if has_shifts:
		summary.append({"key": "Shifts", "value": "All Shifts" if not d["shifts"] else ", ".join(
			"Shift " + s for s in d["shifts"])})
	summary += [{"key": SCOPE_TITLES.get(src["id"], "Scope"), "value": _joinLabels(
			[s["label"] for s in _scopeObjs(src, d["scope"])])},
		{"key": "Measures", "value": _joinLabels([(_measure(src, m) or {}).get("label", m) for m in d["measures"]], 4)},
		{"key": "Sections", "value": _joinLabels([labels.get(s["type"], s["type"]) for s in d["sections"] if s["on"]], 5)}]
	if filters and any(f["item"]["selected"] for f in filters):
		summary.append({"key": flabel, "value": ", ".join(f["item"]["label"] for f in filters if f["item"]["selected"])})
	return {"ok": True, "sources": cards, "quick": quick, "time": time, "groupBy": bds, "shifts": shifts, "scope": scope,
		"measures": mrows, "sections": sectionItems(session, d), "filters": filters, "summary": summary,
		"scopeTitle": SCOPE_TITLES.get(src["id"], "Scope"), "filterLabel": (flabel + " (None Ticked = All)") if flabel else "",
		"sourceLabel": src["label"], "title": d["title"], "notes": d["notes"], "format": d["format"],
		"custom": tp == "custom", "customStart": _customDate(d, "start"), "customEnd": _customDate(d, "end"), "hasShifts": has_shifts, "hasFilters": bool(filters), "summaryText": " | ".join(
			x["value"] for x in summary[1:3])}


def applyEdit(session, defn, edit):
	"""One builder change (message payload) -> the new normalized definition."""
	d = normalize(defn)
	e = _py(edit) or {}
	k = e.get("kind")
	if k == "source":
		if e.get("value") == d["source"]:
			return d
		return defaultDefinition(session, e.get("value"), {})
	if k == "preset":
		return applyPreset(session, e.get("id") or e.get("value")) or d
	auto = d["title"] in ("", _autoTitle(d))       # an untouched automatic title follows the edits
	n = _applyEdit(session, d, e, k)
	if auto and not (k == "set" and e.get("key") == "title"):
		n["title"] = _autoTitle(n)
	return n


def _applyEdit(session, d, e, k):
	src = source(d["source"])
	on = bool(e.get("on"))
	val = e.get("id") if e.get("id") is not None else e.get("value")
	if k == "measure" or k == "group":
		ids = [val] if k == "measure" else list(e.get("ids") or [])
		cur = set(d["measures"])
		for i in ids:
			if on:
				cur.add(i)
			else:
				cur.discard(i)
		d["measures"] = [m["id"] for m in src["measures"] if m["id"] in cur]
		if not d["measures"]:
			d["measures"] = [ids[0]] if ids else d["measures"]
	elif k == "scope":
		tree = scopeTree(session, d["source"])
		tops = [s["id"] for s in tree if not s["parent"]]
		cur = [s for s in d["scope"] if s != val]
		if on:
			# a top item (All ...) replaces the picks below it, and a pick below replaces the top item
			cur = [val] if val in tops else [s for s in cur if s not in tops] + [val]
		order = [s["id"] for s in tree]
		d["scope"] = sorted(cur, key=lambda s: order.index(s) if s in order else 999) or d["scope"]
	elif k == "shift":
		if val == "all":
			d["shifts"] = []
		else:
			cur = [s for s in d["shifts"] if s != val]
			if val not in d["shifts"]:
				cur.append(val)
			d["shifts"] = sorted(cur)
	elif k and k.startswith("filter:"):
		fid = k[7:]
		cur = [v for v in (d["filters"].get(fid) or []) if v != val]
		if val not in (d["filters"].get(fid) or []):
			cur.append(val)
		d["filters"][fid] = sorted(cur)
	elif k == "section":
		for s in d["sections"]:
			if s["type"] == e.get("type"):
				s["on"] = on
	elif k == "move":
		ix = [s["type"] for s in d["sections"]].index(e.get("type")) if e.get("type") in [s["type"] for s in d["sections"]] else -1
		j = ix + int(e.get("dir") or 0)
		if ix >= 0 and 0 <= j < len(d["sections"]):
			d["sections"][ix], d["sections"][j] = d["sections"][j], d["sections"][ix]
	elif k == "sectionSet":
		for s in d["sections"]:
			if s["type"] == e.get("type") and e.get("key") in ("topN", "n", "orderBy"):
				s[e["key"]] = e.get("value")
				if e["key"] == "topN":
					s["orderBy"] = ""
	elif k == "time":
		t = {"preset": e.get("preset") or val or d["time"]["preset"]}
		if t["preset"] == "custom":
			t["start"] = e.get("start") or d["time"].get("start") or _ymd(_mid(_now()))
			t["end"] = e.get("end") or d["time"].get("end") or t["start"]
		# smart group-by: short ranges read best by hour, long ranges by day
		bds = [b["id"] for b in src.get("breakdowns") or []]
		if t["preset"] in ("lastShift", "today", "yesterday") and d["breakdown"] in ("day", "week") and "hour" in bds:
			d["breakdown"] = "hour"
		elif t["preset"] in ("last7", "last30") and d["breakdown"] == "hour" and "day" in bds:
			d["breakdown"] = "day"
		d["time"] = t
	elif k == "breakdown":
		d["breakdown"] = val
	elif k == "set" and e.get("key") in ("title", "notes", "breakdown", "format"):
		d[e["key"]] = e.get("value")
	return normalize(d)


def _customDate(d, key):
	"""Custom start / end as epoch ms for the date inputs."""
	return _ms(d["time"].get(key)) or _mid(_now())


# ------------------------------------------------------------------------------------------------ saved + recent
def _runRows(session):
	labels = dict((s["id"], s["label"]) for s in clientCatalog(session)["sources"])
	out, seen = [], set()
	try:
		for r in system.dataset.toPyDataSet(_nq("Runs/Recent", {"username": username(session)})):
			if r["source"] not in labels or r["title"] in seen:
				continue
			seen.add(r["title"])
			out.append({"id": r["id"], "kind": "run", "name": r["title"], "icon": "material/history",
				"meta": u"%s  \u00b7  %s  \u00b7  %s" % (labels[r["source"]], r["format"],
					system.date.format(r["run_at"], "MM/dd HH:mm"))})
			if len(out) >= 10:
				break
	except (Exception, Throwable) as e:
		LOG.warn("recent runs failed: %s" % e)
	return out


def savedList(session, tab="templates"):
	"""Step 1 rail: saved templates (own + shared) or the session user's last 10 downloads."""
	if not allowed(session, "Use"):
		return []
	if tab == "recent":
		rows = _runRows(session)
	else:
		rows = [{"id": t["id"], "kind": "template", "name": t["name"], "icon": "material/description",
			"meta": u"%s  \u00b7  %s%s" % (t["sourceLabel"], t["kind"], (u"  \u00b7  " + t["owner"]) if t["shared"] else "")}
			for t in templates(session)]
	return [{"item": r} for r in rows]


def loadSaved(session, kind, savedId):
	"""Saved row click: {definition, templateId, name, shared, canEdit, message} or None."""
	if kind == "template":
		t = loadTemplate(session, savedId)
		if t is None:
			return None
		return {"definition": t["definition"], "templateId": t["id"], "name": t["name"], "shared": t["shared"],
			"canEdit": t["canEdit"], "message": "Loaded Template '%s'" % t["name"]}
	try:
		rows = system.dataset.toPyDataSet(_nq("Runs/Get", {"id": int(savedId or 0), "username": username(session)}))
		if not len(rows) or not sourceAllowed(session, source(rows[0]["source"])):
			return None
		d = normalize(_json.loads(rows[0]["definition"]))
		return {"definition": d, "templateId": 0, "name": "", "shared": False, "canEdit": False,
			"message": "Loaded Recent Report '%s'" % rows[0]["title"]}
	except (Exception, Throwable) as e:
		LOG.warn("recent run load failed: %s" % e)
		return None


def logRun(session, d, title):
	"""One row in dbo.report_run per download (Recent list). Never fails the download."""
	try:
		_nq("Runs/Insert", {"username": username(session), "source": d["source"], "title": unicode(title)[:200],
			"definition": _json.dumps(d), "format": d["format"], "now": system.date.now()})
	except (Exception, Throwable) as e:
		LOG.warn("report run log failed: %s" % e)


# ------------------------------------------------------------------------------------------------ output
def _safe(s):
	keep = "".join(ch if (ch.isalnum() or ch in "-_ ") else "_" for ch in unicode(s or "Report"))
	return "_".join(keep.split())[:60] or "Report"


def _pdfBlocks(r):
	"""Sections -> PDF blocks: {title, note, cards[[...12]], charts[{chartTitle, pens, rows}], head, rows}."""
	blocks = []
	for s in r["sections"]:
		if s["type"] == "cards":
			packed = []
			cs = s["cards"]
			for k in range(0, len(cs), 4):
				chunk = cs[k:k + 4] + [{"label": "", "value": "", "sub": ""}] * (4 - len(cs[k:k + 4]))
				packed.append([c["label"] for c in chunk] + [c["value"] for c in chunk] + [c["sub"] for c in chunk])
			blocks.append({"title": s["title"], "note": s["note"], "cards": packed, "charts": [], "head": [], "rows": []})
		elif s["type"] == "trend":
			charts = []
			for c in s["charts"]:
				ts = sorted(set(p[0] for se in c["series"] for p in se["data"]))
				idx = [dict((p[0], p[1]) for p in se["data"]) for se in c["series"]]
				rows = [[t] + [ix.get(t) for ix in idx] + [None] * (MAX_PENS - len(idx)) for t in ts]
				pens = [se["name"] for se in c["series"]] + [""] * (MAX_PENS - len(c["series"]))
				charts.append({"chartTitle": c["title"], "pens": pens, "rows": rows})
			blocks.append({"title": s["title"], "note": s["note"], "cards": [], "charts": charts, "head": [],
				"rows": [] if charts else [[s["note"]] + [""] * (PDF_COLS - 1)]})
		else:
			cols = s["columns"]
			keys = [i for i, c in enumerate(cols) if c[1] == "key"]
			vals = [i for i, c in enumerate(cols) if c[1] != "key"]
			kh = " / ".join(cols[i][0] for i in keys)
			per = PDF_COLS - 1
			parts = [vals[i:i + per] for i in range(0, len(vals), per)] or [[]]
			rows_all = s["rows"][:PDF_MAX_ROWS]
			for pi, part in enumerate(parts):
				head = [kh] + [cols[i][0] for i in part]
				head += [""] * (PDF_COLS - len(head))
				rows = []
				for row in rows_all:
					rr = [" / ".join(row[i] for i in keys)] + [row[i] for i in part]
					rows.append(rr + [""] * (PDF_COLS - len(rr)))
				title = s["title"] + ("" if len(parts) == 1 else " (%d Of %d)" % (pi + 1, len(parts)))
				note = s["note"]
				if len(s["rows"]) > PDF_MAX_ROWS:
					note = "First %d Of %d Rows (Excel / CSV Have All)" % (PDF_MAX_ROWS, len(s["rows"]))
				blocks.append({"title": title, "note": note, "cards": [], "charts": [], "head": head, "rows": rows})
	return blocks


def _datasets(r):
	"""Sections -> [(sheet name, dataset)] for Excel / CSV (raw numbers, one sheet per section)."""
	out = []
	names = []

	def name(base):
		n = _safe(base)[:28] or "Sheet"
		k, i = n, 2
		while k in names:
			k = "%s_%d" % (n[:25], i)
			i += 1
		names.append(k)
		return k

	meta = r["meta"]
	info = [["Title", meta["title"]], ["Source", meta["sourceLabel"]], ["Scope / Time", meta["subtitle"]],

		["Generated", "%s by %s" % (meta["generatedAt"], meta["generatedBy"])]]
	out.append((name("Report"), system.dataset.toDataSet(["Field", "Value"], info)))
	for s in r["sections"]:
		if s["type"] == "cards":
			rows = [[c["label"], c.get("raw"), c.get("unit") or "", c["sub"]] for c in s["cards"]]
			out.append((name(s["title"]), system.dataset.toDataSet(["Metric", "Value", "Unit", "Detail"], rows)))
		elif s["type"] == "trend":
			sers = []
			for c in s["charts"]:
				for se in c["series"]:
					u = c.get("unit") or ""
					sers.append(("%s (%s)" % (se["name"], u) if u not in ("", "count") else se["name"], se["data"]))
			if sers:
				ts = sorted(set(p[0] for nm, data in sers for p in data))
				idx = [dict((p[0], p[1]) for p in data) for nm, data in sers]
				rows = [[system.date.fromMillis(t)] + [ix.get(t) for ix in idx] for t in ts]
				out.append((name("Trend"), system.dataset.toDataSet(["Time"] + [nm for nm, data in sers], rows)))
		else:
			hdr = [c[0] for c in s["columns"]]
			out.append((name(s["title"]), system.dataset.toDataSet(hdr, [list(x) for x in s["raw"]])))
	return out


def output(session, defn):
	"""Run + render in the definition's format: (bytes, filename, contentType, message); bytes None when refused."""
	r = run(session, defn)
	if not r["ok"]:
		return None, None, None, r["message"]
	d = r["definition"]
	stamp = system.date.format(system.date.now(), "yyyyMMdd_HHmm")
	base = "%s_%s" % (_safe(r["meta"]["title"]), stamp)
	try:
		if d["format"] == "Excel":
			sets = _datasets(r)
			data = system.dataset.toExcel(True, [x[1] for x in sets], False, [x[0] for x in sets])
			return data, base + ".xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "Excel Ready"
		if d["format"] == "CSV":
			sets = _datasets(r)
			if len(sets) <= 2:
				return system.dataset.toCSV(sets[-1][1]).encode("utf-8"), base + ".csv", "text/csv", "CSV Ready"
			from java.io import ByteArrayOutputStream
			from java.lang import String
			from java.util.zip import ZipEntry, ZipOutputStream
			bos = ByteArrayOutputStream()
			z = ZipOutputStream(bos)
			for n, ds in sets:
				z.putNextEntry(ZipEntry(n + ".csv"))
				b = String(system.dataset.toCSV(ds)).getBytes("UTF-8")
				z.write(b, 0, len(b))
				z.closeEntry()
			z.close()
			return bos.toByteArray(), base + ".zip", "application/zip", "CSV Files Ready (Zip, One Per Section)"
		payload = {"meta": r["meta"], "blocks": _pdfBlocks(r)}
		data = system.report.executeReport(path=REPORT_PATH, project=PROJECT,
			parameters={"payload": _json.dumps(payload)}, fileType="pdf")
		return data, base + ".pdf", "application/pdf", "PDF Ready"
	except (Exception, Throwable) as e:
		LOG.error("report output failed: %s" % e)
		return None, None, None, "Output Failed: %s" % e


def download(session, defn):
	"""Generate button: browser download of the report. Returns a status message."""
	data, fname, ctype, msg = output(session, defn)
	if data is None:
		return msg
	system.perspective.download(fname, data, ctype)
	d = normalize(defn)
	logRun(session, d, d["title"] or _autoTitle(d))
	return "Downloaded " + fname


def reportData(data):
	"""Script data source of Reports/CustomReport (no session - output() checked access and ran the report)."""
	from system.report import QueryResults
	try:
		p = _json.loads(data["payload"] or "{}")
	except (Exception, Throwable):
		p = {}
	meta = p.get("meta") or {}
	data["reportTitle"] = meta.get("title") or "Custom Report"
	data["subtitle"] = meta.get("subtitle") or ""
	data["dataNote"] = meta.get("dataNote") or ""
	data["generated"] = "Generated %s by %s" % (meta.get("generatedAt") or "", meta.get("generatedBy") or "")
	data["isDemo"] = False
	data["footer"] = "BH HMI Custom Report  |  %s%s" % (meta.get("sourceLabel") or "",
		"")
	blocks = p.get("blocks") or []
	pq = QueryResults(system.dataset.toDataSet(["title", "note"], [[b.get("title") or "", b.get("note") or ""]
		for b in blocks]))
	cards, charts, rows = [], [], []
	ccols = ["label1", "label2", "label3", "label4", "value1", "value2", "value3", "value4", "sub1", "sub2", "sub3",
		"sub4"]
	hcols = ["h%d" % (i + 1) for i in range(PDF_COLS)] + ["c%d" % (i + 1) for i in range(PDF_COLS)]
	pcols = ["chartTitle"] + ["p%d" % (i + 1) for i in range(MAX_PENS)]
	scols = ["t_stamp"] + ["Pen%d" % (i + 1) for i in range(MAX_PENS)]
	for i, b in enumerate(blocks):
		cards.append(QueryResults(system.dataset.toDataSet(ccols, b.get("cards") or []), pq, i))
		chs = b.get("charts") or []
		cq = QueryResults(system.dataset.toDataSet(pcols, [[c["chartTitle"]] + list(c["pens"]) for c in chs]), pq, i)
		if chs:
			kids = []
			for ci, c in enumerate(chs):
				pts = [[system.date.fromMillis(long(r[0]))] + [None if v is None else float(v) for v in r[1:]]
					for r in c["rows"]]
				kids.append(QueryResults(system.dataset.toDataSet(scols, pts), cq, ci))
			cq.addNestedQueryResults("series", kids)
		charts.append(cq)
		head = list(b.get("head") or [])
		rows.append(QueryResults(system.dataset.toDataSet(hcols, [head + list(r) for r in b.get("rows") or []]
			if head else []), pq, i))
	pq.addNestedQueryResults("cards", cards)
	pq.addNestedQueryResults("charts", charts)
	pq.addNestedQueryResults("rows", rows)
	data["sections"] = pq


# ------------------------------------------------------------------------------------------------ templates
def _nq(path, params, getKey=False):
	return system.db.runNamedQuery(project=PROJECT, path=NQ + path, parameters=params, getKey=getKey)


def templates(session, sourceId=""):
	"""Own + shared templates: [{id, name, source, sourceLabel, owner, kind, canEdit, updated}]."""
	if not allowed(session, "Use"):
		return []
	me = username(session)
	manage = allowed(session, "ManageTemplates")
	labels = dict((s["id"], s["label"]) for s in clientCatalog(session)["sources"])
	out = []
	try:
		for r in system.dataset.toPyDataSet(_nq("Templates/List", {"username": me})):
			if r["source"] not in labels or (sourceId and r["source"] != sourceId):
				continue
			own = r["owner_username"] == me
			rule, title = "--", ""
			try:
				dd = normalize(_json.loads(r["definition"]))
				rule, title = _rangeRule(dd), dd.get("title") or ""
			except (Exception, Throwable):
				pass
			out.append({"id": r["id"], "name": r["name"], "source": r["source"], "sourceLabel": labels[r["source"]],
				"range": rule, "title": title,
				"owner": r["owner_name"] or r["owner_username"], "ownerUser": r["owner_username"],
				"kind": "Shared" if r["is_shared"] else "Personal", "shared": bool(r["is_shared"]),
				"canEdit": own or (manage and bool(r["is_shared"])),
				"updated": system.date.format(r["updated_at"], "yyyy-MM-dd HH:mm")})
	except (Exception, Throwable) as e:
		LOG.warn("template list failed: %s" % e)
	return out


def templateOptions(session, sourceId=""):
	return [{"value": t["id"], "label": "%s%s" % (t["name"], "  (Shared - %s)" % t["owner"] if t["shared"] else "")}
		for t in templates(session, sourceId)]


def loadTemplate(session, templateId):
	if not allowed(session, "Use"):
		return None
	try:
		rows = system.dataset.toPyDataSet(_nq("Templates/Get", {"id": int(templateId or 0), "username": username(session)}))
	except (Exception, Throwable) as e:
		LOG.warn("template load failed: %s" % e)
		return None
	if not len(rows):
		return None
	r = rows[0]
	src = source(r["source"])
	if not sourceAllowed(session, src):
		return None
	try:
		d = normalize(_json.loads(r["definition"]))
	except (Exception, Throwable):
		return None
	return {"id": r["id"], "name": r["name"], "shared": bool(r["is_shared"]), "definition": d,
		"canEdit": r["owner_username"] == username(session) or (bool(r["is_shared"]) and allowed(session, "ManageTemplates"))}


def saveTemplate(session, templateId, name, defn, isShared=False, saveAs=False):
	"""Save (owner / manager) or Save As (a new template owned by the session user): {ok, id, message}."""
	if not allowed(session, "Use"):
		return {"ok": False, "id": 0, "message": "Access Denied"}
	name = unicode(name or "").strip()[:120]
	if len(name) < 3:
		return {"ok": False, "id": 0, "message": "Enter A Template Name (3+ Characters)"}
	share = bool(isShared)
	if share and not allowed(session, "ShareTemplates"):
		return {"ok": False, "id": 0, "message": "Sharing Needs The Reports / Share Templates Permission"}
	d = normalize(defn)
	if not sourceAllowed(session, source(d["source"])):
		return {"ok": False, "id": 0, "message": "Access Denied For This Source"}
	me = username(session)
	tid = 0 if saveAs else int(templateId or 0)
	try:
		taken = system.dataset.toPyDataSet(_nq("Templates/NameTaken", {"username": me, "name": name, "id": tid}))
		if taken[0]["n"]:
			return {"ok": False, "id": tid, "message": "You Already Have A Template Named '%s'" % name}
		params = {"name": name, "source": d["source"], "definition": _json.dumps(d), "isShared": share,
			"now": system.date.now(), "username": me}
		if tid:
			params.update({"id": tid, "manage": allowed(session, "ManageTemplates")})
			n = _nq("Templates/Update", params)
			if not n:
				return {"ok": False, "id": tid, "message": "Only The Owner Can Change This Template - Use Save As"}
			return {"ok": True, "id": tid, "message": "Saved '%s'" % name}
		params["ownerName"] = displayName(session)
		new_id = _nq("Templates/Insert", params, getKey=True)
		return {"ok": True, "id": int(new_id or 0), "message": "Saved '%s'%s" % (name, " (Shared)" if share else "")}
	except (Exception, Throwable) as e:
		LOG.error("template save failed: %s" % e)
		return {"ok": False, "id": tid, "message": "Save Failed: %s" % e}


def deleteTemplate(session, templateId):
	if not allowed(session, "Use"):
		return {"ok": False, "message": "Access Denied"}
	try:
		n = _nq("Templates/Delete", {"id": int(templateId or 0), "username": username(session),
			"manage": allowed(session, "ManageTemplates")})
	except (Exception, Throwable) as e:
		return {"ok": False, "message": "Delete Failed: %s" % e}
	return {"ok": bool(n), "message": "Template Deleted" if n else "Only The Owner Can Delete This Template"}


def startState(session, sourceId="", ctx=None, templateId=0):
	"""Builder view startup: access context, source options, the start definition (template or page context)."""
	st = {"ctx": context(session), "sources": sourceOptions(session), "templateId": 0, "templateName": "",
		"templateShared": False, "templateCanEdit": False, "def": None, "msg": ""}
	if not st["ctx"]["use"]:
		return st
	t = loadTemplate(session, templateId) if templateId else None
	if t is not None:
		st.update({"def": t["definition"], "templateId": t["id"], "templateName": t["name"],
			"templateShared": t["shared"], "templateCanEdit": t["canEdit"], "msg": "Loaded Template '%s'" % t["name"]})
	else:
		st["def"] = defaultDefinition(session, sourceId or None, ctx)
		src = source(sourceId) if sourceId else None
		if src is not None and sourceAllowed(session, src):
			st["msg"] = "%s Selected%s" % (src["label"], (" From " + unicode((_py(ctx) or {}).get("origin")))
				if (_py(ctx) or {}).get("origin") else "")
	st["noSources"] = not clientCatalog(session)["sources"]
	st["step"] = 4 if st["templateId"] else 1
	c = _py(ctx) or {}
	if t is None and c.get("runId"):              # Saved Reports > Recent Runs > Run Again
		r = loadSaved(session, "run", c.get("runId"))
		if r is not None:
			st.update({"def": r["definition"], "msg": r["message"], "step": 4})
	elif t is None and c.get("preset"):           # Report Builder page quick report
		pd = applyPreset(session, c.get("preset"))
		if pd is not None:
			st.update({"def": pd, "step": 4})
	if c.get("step") in (1, 2, 3, 4) and st["def"] is not None and st["ctx"]["use"]:
		st["step"] = int(c.get("step"))
	return st


def _rangeRule(d):
	"""Time range rule of a definition: 'Last 7 Days', or the dates of a custom range."""
	p = d["time"]["preset"]
	return _windowLabel(d, True) if p == "custom" else dict(TIME_PRESETS).get(p, p)


def _lastRuns(session):
	"""{(source, title): newest download time} of the session user."""
	out = {}
	try:
		for r in system.dataset.toPyDataSet(_nq("Runs/LastByTitle", {"username": username(session)})):
			out[(r["source"], r["title"])] = system.date.format(r["last_run"], "MM/dd HH:mm")
	except (Exception, Throwable) as e:
		LOG.warn("last runs failed: %s" % e)
	return out


def _runList(session):
	"""Recent Runs rows (own, or every user's with ManageTemplates)."""
	if not allowed(session, "Use"):
		return []
	me = username(session)
	labels = dict((s["id"], s["label"]) for s in clientCatalog(session)["sources"])
	out = []
	try:
		for r in system.dataset.toPyDataSet(_nq("Runs/List", {"username": me, "viewAll": allowed(session, "ManageTemplates")})):
			if r["source"] not in labels:
				continue
			rule = "--"
			try:
				rule = _rangeRule(normalize(_json.loads(r["definition"])))
			except (Exception, Throwable):
				pass
			out.append({"id": r["id"], "name": r["title"], "sourceId": r["source"], "source": labels[r["source"]],
				"range": rule, "format": r["format"], "runBy": r["username"], "mine": r["username"] == me,
				"runAt": system.date.format(r["run_at"], "yyyy-MM-dd HH:mm")})
	except (Exception, Throwable) as e:
		LOG.warn("run list failed: %s" % e)
	return out


def savedModel(session, tab="mine", sourceId="", owner="", search="", refresh=0):
	"""Saved Reports page: {rows, owners, sources, counts, tab}. Tabs: mine (own templates), shared (every shared
	template), runs (Recent Runs). Owner visibility is enforced in the SQL (own + shared only)."""
	empty = {"rows": [], "owners": [], "sources": [], "total": 0, "counts": {"mine": 0, "shared": 0, "runs": 0}, "tab": tab}
	if not allowed(session, "Use"):
		return empty
	me = username(session)
	share = allowed(session, "ShareTemplates")
	manage = allowed(session, "ManageTemplates")
	tpl = templates(session)
	runs = _runList(session)
	mine = [t for t in tpl if t["ownerUser"] == me]
	shared = [t for t in tpl if t["shared"]]
	counts = {"mine": len(mine), "shared": len(shared), "runs": len(runs)}
	isRuns = tab == "runs"
	base = runs if isRuns else (shared if tab == "shared" else mine)
	last = _lastRuns(session)
	q_ = unicode(search or "").strip().lower()
	rows, owners, srcs = [], set(), {}
	for t in base:
		sid = t["sourceId"] if isRuns else t["source"]
		slabel = t["source"] if isRuns else t["sourceLabel"]
		who = t["runBy"] if isRuns else t["owner"]
		owners.add(who)
		srcs[sid] = slabel
		if sourceId and sid != sourceId:
			continue
		if owner and who != owner:
			continue
		if q_ and q_ not in (t["name"] + " " + slabel).lower():
			continue
		if isRuns:
			rows.append(dict(t))
		else:
			own = t["ownerUser"] == me
			rows.append({"id": t["id"], "name": t["name"], "sourceId": sid, "source": slabel, "range": t["range"],
				"owner": who, "lastRun": last.get((sid, t["title"]), "--"), "shared": "Yes" if t["shared"] else "No",
				"isShared": t["shared"], "canEdit": t["canEdit"],
				"canShare": bool((own and (share or t["shared"])) or (manage and t["shared"]))})
	return {"rows": rows, "tab": tab, "counts": counts, "total": len(base),
		"owners": [{"value": o, "label": o} for o in sorted(owners) if o],
		"sources": [{"value": k, "label": v} for k, v in sorted(srcs.items(), key=lambda kv: kv[1])]}


def renameTemplate(session, templateId, name):
	t = loadTemplate(session, templateId)
	if t is None:
		return {"ok": False, "message": "Report Not Available"}
	if not t["canEdit"]:
		return {"ok": False, "message": "Only The Owner Can Rename This Report"}
	return saveTemplate(session, templateId, name, t["definition"], t["shared"])


def setTemplateShared(session, templateId, flag):
	t = loadTemplate(session, templateId)
	if t is None:
		return {"ok": False, "message": "Report Not Available"}
	if not t["canEdit"]:
		return {"ok": False, "message": "Only The Owner Can Change Sharing"}
	r = saveTemplate(session, templateId, t["name"], t["definition"], bool(flag))
	if r["ok"]:
		r["message"] = "'%s' Is Now %s" % (t["name"], "Shared" if flag else "Personal")
	return r


def runFromRun(session, runId, fmt=""):
	"""Recent Runs: download that run's report again (own runs only)."""
	r = loadSaved(session, "run", runId)
	if r is None:
		return "Report Not Available"
	d = r["definition"]
	if fmt in ("PDF", "Excel", "CSV"):
		d["format"] = fmt
	return download(session, d)


def startModel(session):
	"""Report Builder page: source cards + quick reports (same shapes as the builder's Step 1)."""
	cc = clientCatalog(session)
	cards = [{"item": {"id": s["id"], "label": s["label"], "description": s.get("description") or "",
		"meta": s.get("meta") or "", "icon": s.get("icon") or "material/assessment", "selected": False}}
		for s in cc["sources"]]
	quick = [_tile(p["id"], p["label"], p.get("detail") or "", False, "preset") for p in cc.get("presets") or []]
	return {"sources": cards, "quick": quick, "denied": len(cards) == 0}


def templateRows(session, sourceId=""):
	"""Reports page table rows."""
	return [{"id": t["id"], "name": t["name"], "source": t["sourceLabel"], "kind": t["kind"], "owner": t["owner"],
		"updated": t["updated"], "canEdit": t["canEdit"]} for t in templates(session, sourceId)]


def runTemplate(session, templateId, fmt=""):
	"""Reports page: download a saved template's report (format override optional). Returns a status message."""
	t = loadTemplate(session, templateId)
	if t is None:
		return "Template Not Available"
	d = t["definition"]
	if fmt in ("PDF", "Excel", "CSV"):
		d["format"] = fmt
	return download(session, d)


# ------------------------------------------------------------------------------------------------ open
POPUP_MAX = (1440, 880)    # design sizes: laptop 1366 x 768 -> 1318 x 720, 1536 x 864 -> 1440 x 816, 1920 -> 1440 x 880
POPUP_MIN = (960, 560)
POPUP_MARGIN = 24          # px kept free around the popup on every side


def _callerPage():
	"""The Perspective page of the calling component / view script (self.page up the stack), else None."""
	try:
		import sys
		f = sys._getframe(1)
		depth = 0
		while f is not None and depth < 30:
			me = f.f_locals.get("self")
			if me is not None:
				try:
					pg = me.page
					if pg is not None:
						return pg
				except (Exception, Throwable):
					pass
			f = f.f_back
			depth += 1
	except (Exception, Throwable):
		pass
	return None


def popupPosition(page=None):
	"""Popup box centred in the browser viewport and never larger than it (minus POPUP_MARGIN on each side).
	Perspective otherwise sizes a popup from the view's defaultSize and centres it in the popups pane beside the docked
	nav, which pushed the old 1500 x 900 builder off centre and past the right edge on a 1366 x 768 laptop."""
	vw, vh = 1366, 768
	try:
		dims = page.props.dimensions.viewport
		vw = int(dims.width or vw)
		vh = int(dims.height or vh)
	except (Exception, Throwable):
		pass
	w = int(max(min(POPUP_MIN[0], vw), min(POPUP_MAX[0], vw - 2 * POPUP_MARGIN)))
	h = int(max(min(POPUP_MIN[1], vh), min(POPUP_MAX[1], vh - 2 * POPUP_MARGIN)))
	return {"left": max(0, (vw - w) // 2), "top": max(0, (vh - h) // 2), "width": w, "height": h}


def centerBox(page, w, h):
	"""A w x h popup position centred in the browser viewport (small dialogs; the builder uses popupPosition)."""
	vw, vh = 1366, 768
	try:
		dims = page.props.dimensions.viewport
		vw = int(dims.width or vw)
		vh = int(dims.height or vh)
	except (Exception, Throwable):
		pass
	w, h = min(w, vw - 2 * POPUP_MARGIN), min(h, vh - 2 * POPUP_MARGIN)
	return {"left": max(0, (vw - w) // 2), "top": max(0, (vh - h) // 2), "width": w, "height": h}


def _evNum(event, key):
	for getter in (lambda: getattr(event, key), lambda: event[key]):
		try:
			v = getter()
			if v is not None:
				return float(v)
		except (Exception, Throwable):
			pass
	return None


def menuBox(page, event, w, h):
	"""A w x h small-menu position at the click (clientX / clientY), kept inside the browser viewport."""
	vw, vh = 1366, 768
	try:
		dims = page.props.dimensions.viewport
		vw = int(dims.width or vw)
		vh = int(dims.height or vh)
	except (Exception, Throwable):
		pass
	x = _evNum(event, "clientX")
	y = _evNum(event, "clientY")
	if x is None or y is None:
		x, y = _evNum(event, "pageX") or 200.0, _evNum(event, "pageY") or 200.0
	left, top = int(x) - w + 16, int(y) + 12
	left = max(4, min(left, vw - w - 4))
	top = max(4, min(top, vh - h - 4))
	return {"left": left, "top": top, "width": w, "height": h}


def open(sourceId=None, context=None, session=None, templateId=0, page=None):
	"""Open the report builder popup (any page): shared.Reports.open('alarms', {'areas': [...], 'origin': '...'}).
	The context pre-selects the source (and areas / scope / shift / day); the popup is sized to the caller's viewport."""
	s = session if session is not None else shared.Security._currentSession()
	if s is not None and not allowed(s, "Use"):
		shared.Security.require("Reports", "Use", "open report builder", s)
		shared.Alerts.showAlert(state="warning", title="Access Denied",
			message="The Report Builder Needs The Reports / Use Permission (Maintenance And Above).")
		return False
	pos = popupPosition(page if page is not None else _callerPage())
	try:
		system.perspective.closePopup(POPUP_ID)       # a builder left open gets a fresh start (new context / source)
	except (Exception, Throwable):
		pass
	system.perspective.openPopup(id=POPUP_ID, view=POPUP_VIEW,
		params={"sourceId": sourceId or "", "context": _py(context) or {}, "templateId": int(templateId or 0)},
		position=pos, modal=True, draggable=False, resizable=False, showCloseIcon=False, overlayDismiss=False,
		viewportBound=True)
	return True


def close():
	system.perspective.closePopup(POPUP_ID)
