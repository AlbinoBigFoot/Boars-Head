# Operations Forms (Operations > Forms): Daily Rounds Log, NH3 Shift Log, Annual P&ID Verification, Form History.
# Written by .cursor/tasks/operations-forms/build.py (source: forms_library.py there) - edit the builder, not this copy.
# Design: docs/operations-forms.md.
#
# Every entry point takes the Perspective session and decides on the gateway: Forms/Use to fill / save anything,
# Forms/ViewAll to see other users' submissions (otherwise only rows submitted_by = the session username). The
# username always comes from session.props.auth.user (never from a view parameter). Named queries: OpsForms/*.
# PDF output: Reporting module resources OpsForms/* (script data source -> reportData below); email can be added as
# another sink next to downloadPdf (pdfBytes returns the bytes after the same permission check).

import json as _json
from java.lang import Throwable
from java.text import SimpleDateFormat
from java.util import Date, Locale

LOG = system.util.getLogger("shared.Forms")
PROJECT = "BH"
NQ = "OpsForms/"
CFG = "[default]_Config/Forms/"
USER_SOURCE = "default"
SCHEMA = _json.loads(r'''{"DailyRounds": {"bools": ["prv_rd_visuals", "continuous_fan"], "computed": {"avg_probe": ["evap_a1_temp", "evap_a2_temp", "evap_b1_temp", "evap_b2_temp", "evap_c1_temp", "evap_d1_temp", "evap_e1_temp", "evap_e2_temp", "evap_e3_temp", "evap_e4_temp", "evap_f1_temp", "evap_f2_temp", "evap_f3_temp", "evap_f4_temp", "evap_g1_temp", "evap_g2_temp", "evap_g3_temp", "evap_g4_temp", "evap_g5_temp"], "avg_therm": ["t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10", "t11"]}, "dates": ["date"], "file": "DailyRoundsLog", "keys": ["comp1_suction", "comp1_discharge", "comp1_fla", "comp1_hours", "comp1_slide", "comp1_ratio", "comp1_oil", "comp4_suction", "comp4_discharge", "comp4_fla", "comp4_hours", "comp4_slide", "comp4_ratio", "comp4_oil", "comp5_suction", "comp5_discharge", "comp5_fla", "comp5_hours", "comp5_slide", "comp5_ratio", "comp5_oil", "comp6_suction", "comp6_discharge", "comp6_fla", "comp6_hours", "comp6_slide", "comp6_ratio", "comp6_oil", "comp7_suction", "comp7_discharge", "comp7_fla", "comp7_hours", "comp7_slide", "comp7_ratio", "comp7_oil", "purger_psig", "purger_purges", "prv_rd_visuals", "continuous_fan", "htr_level", "htr_psi", "htr_pump", "htr_pumphrs", "ltr_level", "ltr_psi", "ltr_pump", "ltr_pumphrs", "hpr_level", "hpr_psi", "hpr_pump", "csv_level", "csv_psi", "csv_pump", "filter_dp", "pond_west", "pond_east", "csvpump1_status", "csvpump1_hrs", "csvpump2_status", "csvpump2_hrs", "csvpump3_status", "csvpump3_hrs", "cond1_fana", "cond1_fan1hrs", "cond1_fanb", "cond1_fan2hrs", "cond2_fana", "cond2_fan1hrs", "cond2_fanb", "cond2_fan2hrs", "cond_webmaster", "cond_handheld", "evap_a1_temp", "evap_a1_suction", "evap_a1_status", "evap_a1_hrs", "evap_a1_coil", "evap_a2_temp", "evap_a2_suction", "evap_a2_status", "evap_a2_hrs", "evap_a2_coil", "evap_b1_temp", "evap_b1_suction", "evap_b1_status", "evap_b1_hrs", "evap_b1_coil", "evap_b2_temp", "evap_b2_suction", "evap_b2_status", "evap_b2_hrs", "evap_b2_coil", "evap_c1_temp", "evap_c1_suction", "evap_c1_status", "evap_c1_hrs", "evap_c1_coil", "evap_d1_temp", "evap_d1_suction", "evap_d1_status", "evap_d1_hrs", "evap_d1_coil", "evap_e1_temp", "evap_e1_suction", "evap_e1_status", "evap_e1_hrs", "evap_e1_coil", "evap_e2_temp", "evap_e2_suction", "evap_e2_status", "evap_e2_hrs", "evap_e2_coil", "evap_e3_temp", "evap_e3_suction", "evap_e3_status", "evap_e3_hrs", "evap_e3_coil", "evap_e4_temp", "evap_e4_suction", "evap_e4_status", "evap_e4_hrs", "evap_e4_coil", "evap_f1_temp", "evap_f1_suction", "evap_f1_status", "evap_f1_hrs", "evap_f1_coil", "evap_f2_temp", "evap_f2_suction", "evap_f2_status", "evap_f2_hrs", "evap_f2_coil", "evap_f3_temp", "evap_f3_suction", "evap_f3_status", "evap_f3_hrs", "evap_f3_coil", "evap_f4_temp", "evap_f4_suction", "evap_f4_status", "evap_f4_hrs", "evap_f4_coil", "evap_g1_temp", "evap_g1_suction", "evap_g1_status", "evap_g1_hrs", "evap_g1_coil", "evap_g2_temp", "evap_g2_suction", "evap_g2_status", "evap_g2_hrs", "evap_g2_coil", "evap_g3_temp", "evap_g3_suction", "evap_g3_status", "evap_g3_hrs", "evap_g3_coil", "evap_g4_temp", "evap_g4_suction", "evap_g4_status", "evap_g4_hrs", "evap_g4_coil", "evap_g5_temp", "evap_g5_suction", "evap_g5_status", "evap_g5_hrs", "evap_g5_coil", "t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10", "t11", "control_room_temp", "outside_ambient_temp", "name", "date"], "labels": {"comp1_discharge": "COMP 1 Discharge", "comp1_fla": "COMP 1 FLA %", "comp1_hours": "COMP 1 Hours", "comp1_oil": "COMP 1 Oil Level", "comp1_ratio": "COMP 1 Ratio", "comp1_slide": "COMP 1 Slide Valve %", "comp1_suction": "COMP 1 Suction", "comp4_discharge": "COMP 4 Discharge", "comp4_fla": "COMP 4 FLA %", "comp4_hours": "COMP 4 Hours", "comp4_oil": "COMP 4 Oil Level", "comp4_ratio": "COMP 4 Ratio", "comp4_slide": "COMP 4 Slide Valve %", "comp4_suction": "COMP 4 Suction", "comp5_discharge": "COMP 5 Discharge", "comp5_fla": "COMP 5 FLA %", "comp5_hours": "COMP 5 Hours", "comp5_oil": "COMP 5 Oil Level", "comp5_ratio": "COMP 5 Ratio", "comp5_slide": "COMP 5 Slide Valve %", "comp5_suction": "COMP 5 Suction", "comp6_discharge": "COMP 6 Discharge", "comp6_fla": "COMP 6 FLA %", "comp6_hours": "COMP 6 Hours", "comp6_oil": "COMP 6 Oil Level", "comp6_ratio": "COMP 6 Ratio", "comp6_slide": "COMP 6 Slide Valve %", "comp6_suction": "COMP 6 Suction", "comp7_discharge": "COMP 7 Discharge", "comp7_fla": "COMP 7 FLA %", "comp7_hours": "COMP 7 Hours", "comp7_oil": "COMP 7 Oil Level", "comp7_ratio": "COMP 7 Ratio", "comp7_slide": "COMP 7 Slide Valve %", "comp7_suction": "COMP 7 Suction", "cond1_fan1hrs": "Condenser 1 Fan 1 Hours", "cond1_fan2hrs": "Condenser 1 Fan 2 Hours", "cond1_fana": "Condenser 1 Fan A Status", "cond1_fanb": "Condenser 1 Fan B Status", "cond2_fan1hrs": "Condenser 2 Fan 1 Hours", "cond2_fan2hrs": "Condenser 2 Fan 2 Hours", "cond2_fana": "Condenser 2 Fan A Status", "cond2_fanb": "Condenser 2 Fan B Status", "cond_handheld": "Conductivity Hand Held Tester Reading", "cond_webmaster": "Conductivity Web Master Reading", "continuous_fan": "Continuous Fan", "control_room_temp": "Control Room Temp", "csv_level": "CSV Level", "csv_psi": "CSV PSI", "csv_pump": "CSV Pump", "csvpump1_hrs": "CSV Pump #1 Hrs", "csvpump1_status": "CSV Pump #1 Status", "csvpump2_hrs": "CSV Pump #2 Hrs", "csvpump2_status": "CSV Pump #2 Status", "csvpump3_hrs": "CSV Pump #3 Hrs", "csvpump3_status": "CSV Pump #3 Status", "date": "Date", "evap_a1_coil": "A1 Coil Condition", "evap_a1_hrs": "A1 Unit Hrs", "evap_a1_status": "A1 Status", "evap_a1_suction": "A1 Suction PSIG", "evap_a1_temp": "A1 Temp", "evap_a2_coil": "A2 Coil Condition", "evap_a2_hrs": "A2 Unit Hrs", "evap_a2_status": "A2 Status", "evap_a2_suction": "A2 Suction PSIG", "evap_a2_temp": "A2 Temp", "evap_b1_coil": "B1 Coil Condition", "evap_b1_hrs": "B1 Unit Hrs", "evap_b1_status": "B1 Status", "evap_b1_suction": "B1 Suction PSIG", "evap_b1_temp": "B1 Temp", "evap_b2_coil": "B2 Coil Condition", "evap_b2_hrs": "B2 Unit Hrs", "evap_b2_status": "B2 Status", "evap_b2_suction": "B2 Suction PSIG", "evap_b2_temp": "B2 Temp", "evap_c1_coil": "C1 Coil Condition", "evap_c1_hrs": "C1 Unit Hrs", "evap_c1_status": "C1 Status", "evap_c1_suction": "C1 Suction PSIG", "evap_c1_temp": "C1 Temp", "evap_d1_coil": "D1 Coil Condition", "evap_d1_hrs": "D1 Unit Hrs", "evap_d1_status": "D1 Status", "evap_d1_suction": "D1 Suction PSIG", "evap_d1_temp": "D1 Temp", "evap_e1_coil": "E1 Coil Condition", "evap_e1_hrs": "E1 Unit Hrs", "evap_e1_status": "E1 Status", "evap_e1_suction": "E1 Suction PSIG", "evap_e1_temp": "E1 Temp", "evap_e2_coil": "E2 Coil Condition", "evap_e2_hrs": "E2 Unit Hrs", "evap_e2_status": "E2 Status", "evap_e2_suction": "E2 Suction PSIG", "evap_e2_temp": "E2 Temp", "evap_e3_coil": "E3 Coil Condition", "evap_e3_hrs": "E3 Unit Hrs", "evap_e3_status": "E3 Status", "evap_e3_suction": "E3 Suction PSIG", "evap_e3_temp": "E3 Temp", "evap_e4_coil": "E4 Coil Condition", "evap_e4_hrs": "E4 Unit Hrs", "evap_e4_status": "E4 Status", "evap_e4_suction": "E4 Suction PSIG", "evap_e4_temp": "E4 Temp", "evap_f1_coil": "F1 Coil Condition", "evap_f1_hrs": "F1 Unit Hrs", "evap_f1_status": "F1 Status", "evap_f1_suction": "F1 Suction PSIG", "evap_f1_temp": "F1 Temp", "evap_f2_coil": "F2 Coil Condition", "evap_f2_hrs": "F2 Unit Hrs", "evap_f2_status": "F2 Status", "evap_f2_suction": "F2 Suction PSIG", "evap_f2_temp": "F2 Temp", "evap_f3_coil": "F3 Coil Condition", "evap_f3_hrs": "F3 Unit Hrs", "evap_f3_status": "F3 Status", "evap_f3_suction": "F3 Suction PSIG", "evap_f3_temp": "F3 Temp", "evap_f4_coil": "F4 Coil Condition", "evap_f4_hrs": "F4 Unit Hrs", "evap_f4_status": "F4 Status", "evap_f4_suction": "F4 Suction PSIG", "evap_f4_temp": "F4 Temp", "evap_g1_coil": "G1 Coil Condition", "evap_g1_hrs": "G1 Unit Hrs", "evap_g1_status": "G1 Status", "evap_g1_suction": "G1 Suction PSIG", "evap_g1_temp": "G1 Temp", "evap_g2_coil": "G2 Coil Condition", "evap_g2_hrs": "G2 Unit Hrs", "evap_g2_status": "G2 Status", "evap_g2_suction": "G2 Suction PSIG", "evap_g2_temp": "G2 Temp", "evap_g3_coil": "G3 Coil Condition", "evap_g3_hrs": "G3 Unit Hrs", "evap_g3_status": "G3 Status", "evap_g3_suction": "G3 Suction PSIG", "evap_g3_temp": "G3 Temp", "evap_g4_coil": "G4 Coil Condition", "evap_g4_hrs": "G4 Unit Hrs", "evap_g4_status": "G4 Status", "evap_g4_suction": "G4 Suction PSIG", "evap_g4_temp": "G4 Temp", "evap_g5_coil": "G5 Coil Condition", "evap_g5_hrs": "G5 Unit Hrs", "evap_g5_status": "G5 Status", "evap_g5_suction": "G5 Suction PSIG", "evap_g5_temp": "G5 Temp", "filter_dp": "Filter Delta P", "hpr_level": "HPR Level", "hpr_psi": "HPR PSI", "hpr_pump": "HPR Pump", "htr_level": "HTR Level", "htr_psi": "HTR PSI", "htr_pump": "HTR Pump", "htr_pumphrs": "HTR Pump Hours", "ltr_level": "LTR Level", "ltr_psi": "LTR PSI", "ltr_pump": "LTR Pump", "ltr_pumphrs": "LTR Pump Hours", "name": "Name", "outside_ambient_temp": "Outside Ambient Temp", "pond_east": "Retention Pond East", "pond_west": "Retention Pond West", "prv_rd_visuals": "PRV & RD PSI Visuals", "purger_psig": "Purger PSIG", "purger_purges": "Purger Purges", "t1": "T 1-E2", "t10": "T 10-B1&A2", "t11": "T 11-B2", "t2": "T 2-F2", "t3": "T 3-F1&2", "t4": "T 4-F-1", "t5": "T 5-F4&G5", "t6": "T 6-G4&3", "t7": "T 7-E4&G3", "t8": "T 8-E3", "t9": "T 9-D1&A1"}, "report": "OpsForms/DailyRoundsLog", "required": [["name", "Name"], ["date", "Date"]], "rules": [], "title": "Daily Rounds Log"}, "ShiftLog": {"bools": [], "computed": {}, "dates": ["date", "sign_date"], "file": "NH3ShiftLog", "keys": ["date", "op1", "op1_time", "op2", "op2_time", "shift_status", "out_op", "out_time", "in_op", "in_time", "in_reviewed", "key_items", "alarm1_time", "alarm1_equip", "alarm1_desc", "alarm1_action", "alarm1_resolved", "alarm1_initials", "alarm2_time", "alarm2_equip", "alarm2_desc", "alarm2_action", "alarm2_resolved", "alarm2_initials", "alarm3_time", "alarm3_equip", "alarm3_desc", "alarm3_action", "alarm3_resolved", "alarm3_initials", "alarm4_time", "alarm4_equip", "alarm4_desc", "alarm4_action", "alarm4_resolved", "alarm4_initials", "alarm5_time", "alarm5_equip", "alarm5_desc", "alarm5_action", "alarm5_resolved", "alarm5_initials", "alarm6_time", "alarm6_equip", "alarm6_desc", "alarm6_action", "alarm6_resolved", "alarm6_initials", "alarm7_time", "alarm7_equip", "alarm7_desc", "alarm7_action", "alarm7_resolved", "alarm7_initials", "alarm8_time", "alarm8_equip", "alarm8_desc", "alarm8_action", "alarm8_resolved", "alarm8_initials", "rel1_time", "rel1_location", "rel1_desc", "rel1_detection", "rel1_reportable", "rel1_notified", "rel1_initials", "rel2_time", "rel2_location", "rel2_desc", "rel2_detection", "rel2_reportable", "rel2_notified", "rel2_initials", "rel3_time", "rel3_location", "rel3_desc", "rel3_detection", "rel3_reportable", "rel3_notified", "rel3_initials", "rel4_time", "rel4_location", "rel4_desc", "rel4_detection", "rel4_reportable", "rel4_notified", "rel4_initials", "wo_completed", "permits_active", "open_items", "comments", "summary", "name", "sign_date"], "labels": {"alarm1_action": "Alarm Row 1 Action Taken", "alarm1_desc": "Alarm Row 1 Alarm / Condition Description", "alarm1_equip": "Alarm Row 1 Equipment / Area", "alarm1_initials": "Alarm Row 1 Initials", "alarm1_resolved": "Alarm Row 1 Resolved?", "alarm1_time": "Alarm Row 1 Time", "alarm2_action": "Alarm Row 2 Action Taken", "alarm2_desc": "Alarm Row 2 Alarm / Condition Description", "alarm2_equip": "Alarm Row 2 Equipment / Area", "alarm2_initials": "Alarm Row 2 Initials", "alarm2_resolved": "Alarm Row 2 Resolved?", "alarm2_time": "Alarm Row 2 Time", "alarm3_action": "Alarm Row 3 Action Taken", "alarm3_desc": "Alarm Row 3 Alarm / Condition Description", "alarm3_equip": "Alarm Row 3 Equipment / Area", "alarm3_initials": "Alarm Row 3 Initials", "alarm3_resolved": "Alarm Row 3 Resolved?", "alarm3_time": "Alarm Row 3 Time", "alarm4_action": "Alarm Row 4 Action Taken", "alarm4_desc": "Alarm Row 4 Alarm / Condition Description", "alarm4_equip": "Alarm Row 4 Equipment / Area", "alarm4_initials": "Alarm Row 4 Initials", "alarm4_resolved": "Alarm Row 4 Resolved?", "alarm4_time": "Alarm Row 4 Time", "alarm5_action": "Alarm Row 5 Action Taken", "alarm5_desc": "Alarm Row 5 Alarm / Condition Description", "alarm5_equip": "Alarm Row 5 Equipment / Area", "alarm5_initials": "Alarm Row 5 Initials", "alarm5_resolved": "Alarm Row 5 Resolved?", "alarm5_time": "Alarm Row 5 Time", "alarm6_action": "Alarm Row 6 Action Taken", "alarm6_desc": "Alarm Row 6 Alarm / Condition Description", "alarm6_equip": "Alarm Row 6 Equipment / Area", "alarm6_initials": "Alarm Row 6 Initials", "alarm6_resolved": "Alarm Row 6 Resolved?", "alarm6_time": "Alarm Row 6 Time", "alarm7_action": "Alarm Row 7 Action Taken", "alarm7_desc": "Alarm Row 7 Alarm / Condition Description", "alarm7_equip": "Alarm Row 7 Equipment / Area", "alarm7_initials": "Alarm Row 7 Initials", "alarm7_resolved": "Alarm Row 7 Resolved?", "alarm7_time": "Alarm Row 7 Time", "alarm8_action": "Alarm Row 8 Action Taken", "alarm8_desc": "Alarm Row 8 Alarm / Condition Description", "alarm8_equip": "Alarm Row 8 Equipment / Area", "alarm8_initials": "Alarm Row 8 Initials", "alarm8_resolved": "Alarm Row 8 Resolved?", "alarm8_time": "Alarm Row 8 Time", "comments": "Comments", "date": "Date", "in_op": "Incoming Operator", "in_reviewed": "Incoming Op. Reviewed?", "in_time": "Incoming Time", "key_items": "Key Items For Next Shift", "name": "Name", "op1": "Operator 1", "op1_time": "Operator 1 Time In / Out", "op2": "Operator 2", "op2_time": "Operator 2 Time In / Out", "open_items": "Any Open Items?", "out_op": "Outgoing Operator", "out_time": "Outgoing Time", "permits_active": "Permits / MOC Active This Shift", "rel1_desc": "Release Row 1 Description (Incl. Est. Quantity / Duration)", "rel1_detection": "Release Row 1 Detection Method", "rel1_initials": "Release Row 1 Initials", "rel1_location": "Release Row 1 Location", "rel1_notified": "Release Row 1 Notified", "rel1_reportable": "Release Row 1 Reportable (>= 100 Lbs)?", "rel1_time": "Release Row 1 Time", "rel2_desc": "Release Row 2 Description (Incl. Est. Quantity / Duration)", "rel2_detection": "Release Row 2 Detection Method", "rel2_initials": "Release Row 2 Initials", "rel2_location": "Release Row 2 Location", "rel2_notified": "Release Row 2 Notified", "rel2_reportable": "Release Row 2 Reportable (>= 100 Lbs)?", "rel2_time": "Release Row 2 Time", "rel3_desc": "Release Row 3 Description (Incl. Est. Quantity / Duration)", "rel3_detection": "Release Row 3 Detection Method", "rel3_initials": "Release Row 3 Initials", "rel3_location": "Release Row 3 Location", "rel3_notified": "Release Row 3 Notified", "rel3_reportable": "Release Row 3 Reportable (>= 100 Lbs)?", "rel3_time": "Release Row 3 Time", "rel4_desc": "Release Row 4 Description (Incl. Est. Quantity / Duration)", "rel4_detection": "Release Row 4 Detection Method", "rel4_initials": "Release Row 4 Initials", "rel4_location": "Release Row 4 Location", "rel4_notified": "Release Row 4 Notified", "rel4_reportable": "Release Row 4 Reportable (>= 100 Lbs)?", "rel4_time": "Release Row 4 Time", "shift_status": "Shift Status", "sign_date": "Sign-Off Date", "summary": "General Shift Summary / Notes", "wo_completed": "Work Orders / PMs Completed"}, "report": "OpsForms/NH3ShiftLog", "required": [["date", "Date"], ["op1", "Operator 1"], ["shift_status", "Shift Status"], ["name", "Name"], ["sign_date", "Sign-Off Date"]], "rules": [{"label": "General Shift Summary / Notes (Abnormal Shift)", "need": ["summary"], "when": {"eq": ["shift_status", "Abnormal - See Notes"]}}, {"label": "Incoming Op. Reviewed?", "need": ["in_reviewed"], "when": {"any": ["in_op"]}}, {"label": "Comments (Open Items)", "need": ["comments"], "when": {"eq": ["open_items", "Yes - See Comments"]}}, {"label": "Alarm Row 1 Time And Description", "need": ["alarm1_time", "alarm1_desc"], "when": {"any": ["alarm1_time", "alarm1_equip", "alarm1_desc", "alarm1_action", "alarm1_resolved", "alarm1_initials"]}}, {"label": "Alarm Row 2 Time And Description", "need": ["alarm2_time", "alarm2_desc"], "when": {"any": ["alarm2_time", "alarm2_equip", "alarm2_desc", "alarm2_action", "alarm2_resolved", "alarm2_initials"]}}, {"label": "Alarm Row 3 Time And Description", "need": ["alarm3_time", "alarm3_desc"], "when": {"any": ["alarm3_time", "alarm3_equip", "alarm3_desc", "alarm3_action", "alarm3_resolved", "alarm3_initials"]}}, {"label": "Alarm Row 4 Time And Description", "need": ["alarm4_time", "alarm4_desc"], "when": {"any": ["alarm4_time", "alarm4_equip", "alarm4_desc", "alarm4_action", "alarm4_resolved", "alarm4_initials"]}}, {"label": "Alarm Row 5 Time And Description", "need": ["alarm5_time", "alarm5_desc"], "when": {"any": ["alarm5_time", "alarm5_equip", "alarm5_desc", "alarm5_action", "alarm5_resolved", "alarm5_initials"]}}, {"label": "Alarm Row 6 Time And Description", "need": ["alarm6_time", "alarm6_desc"], "when": {"any": ["alarm6_time", "alarm6_equip", "alarm6_desc", "alarm6_action", "alarm6_resolved", "alarm6_initials"]}}, {"label": "Alarm Row 7 Time And Description", "need": ["alarm7_time", "alarm7_desc"], "when": {"any": ["alarm7_time", "alarm7_equip", "alarm7_desc", "alarm7_action", "alarm7_resolved", "alarm7_initials"]}}, {"label": "Alarm Row 8 Time And Description", "need": ["alarm8_time", "alarm8_desc"], "when": {"any": ["alarm8_time", "alarm8_equip", "alarm8_desc", "alarm8_action", "alarm8_resolved", "alarm8_initials"]}}, {"label": "Release Row 1 Time, Location, Description And Reportable", "need": ["rel1_time", "rel1_location", "rel1_desc", "rel1_reportable"], "when": {"any": ["rel1_time", "rel1_location", "rel1_desc", "rel1_detection", "rel1_reportable", "rel1_notified", "rel1_initials"]}}, {"label": "Release Row 2 Time, Location, Description And Reportable", "need": ["rel2_time", "rel2_location", "rel2_desc", "rel2_reportable"], "when": {"any": ["rel2_time", "rel2_location", "rel2_desc", "rel2_detection", "rel2_reportable", "rel2_notified", "rel2_initials"]}}, {"label": "Release Row 3 Time, Location, Description And Reportable", "need": ["rel3_time", "rel3_location", "rel3_desc", "rel3_reportable"], "when": {"any": ["rel3_time", "rel3_location", "rel3_desc", "rel3_detection", "rel3_reportable", "rel3_notified", "rel3_initials"]}}, {"label": "Release Row 4 Time, Location, Description And Reportable", "need": ["rel4_time", "rel4_location", "rel4_desc", "rel4_reportable"], "when": {"any": ["rel4_time", "rel4_location", "rel4_desc", "rel4_detection", "rel4_reportable", "rel4_notified", "rel4_initials"]}}], "title": "NH3 Shift Log"}, "evapStatusMap": {"1": "Cool", "2": "Defrost", "5": "Idle", "6": "Defrost", "7": "Defrost", "8": "Defrost", "9": "Defrost"}, "live": {"comp1_discharge": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 1/Comp/DisP"}, "comp1_fla": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 1/Comp/FLA"}, "comp1_hours": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 1/Comp/TotalRuntime"}, "comp1_slide": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 1/Comp/SVP"}, "comp1_suction": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 1/Comp/SucP"}, "comp4_discharge": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 4/Comp/DisP"}, "comp4_fla": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 4/Comp/FLA"}, "comp4_hours": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 4/Comp/TotalRuntime"}, "comp4_slide": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 4/Comp/SVP"}, "comp4_suction": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 4/Comp/SucP"}, "comp5_discharge": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 5/Comp/DisP"}, "comp5_fla": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 5/Comp/FLA"}, "comp5_hours": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 5/Comp/TotalRuntime"}, "comp5_slide": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 5/Comp/SVP"}, "comp5_suction": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 5/Comp/SucP"}, "comp6_discharge": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 6/Comp/DisP"}, "comp6_fla": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 6/Comp/FLA"}, "comp6_hours": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 6/Comp/TotalRuntime"}, "comp6_slide": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 6/Comp/SVP"}, "comp6_suction": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 6/Comp/SucP"}, "comp7_discharge": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 7/Comp/DisP"}, "comp7_fla": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 7/Comp/FLA"}, "comp7_hours": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 7/Comp/TotalRuntime"}, "comp7_slide": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 7/Comp/SVP"}, "comp7_suction": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Compressors/COMP 7/Comp/SucP"}, "cond1_fan1hrs": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 1/RunTime/Val_TotRunHrs"}, "cond1_fan2hrs": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 2/RunTime/Val_TotRunHrs"}, "cond1_fana": {"kind": "motorStatus", "running": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 1/Motor/Sts_Running"}, "cond1_fanb": {"kind": "motorStatus", "running": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1A/Fan 2/Motor/Sts_Running"}, "cond2_fan1hrs": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1B/Fan 1/RunTime/Val_TotRunHrs"}, "cond2_fan2hrs": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1B/Fan 2/RunTime/Val_TotRunHrs"}, "cond2_fana": {"kind": "motorStatus", "running": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1B/Fan 1/Motor/Sts_Running"}, "cond2_fanb": {"kind": "motorStatus", "running": "[default]Boars_Head/GrovePort/Condensers/Condensers/EC-1B/Fan 2/Motor/Sts_Running"}, "csv_level": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Tanks/CSV/LvlAIn/Val"}, "csv_psi": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Tanks/CSV/PressAIn/Val"}, "csvpump1_hrs": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 1/RunTime/Val_TotRunHrs"}, "csvpump1_status": {"enabled": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 1.Enabled", "kind": "motorStatus", "oos": "Out of Service", "running": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 1/Motor/Sts_Running"}, "csvpump2_hrs": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 2/RunTime/Val_TotRunHrs"}, "csvpump2_status": {"enabled": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 2.Enabled", "kind": "motorStatus", "oos": "Out of Service", "running": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 2/Motor/Sts_Running"}, "csvpump3_hrs": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 3/RunTime/Val_TotRunHrs"}, "csvpump3_status": {"enabled": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 3.Enabled", "kind": "motorStatus", "oos": "Out of Service", "running": "[default]Boars_Head/GrovePort/Condensers/Pumps/Sump Pump 3/Motor/Sts_Running"}, "evap_a1_status": {"enabled": "[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/HmiStatus"}, "evap_a1_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Freezer/Utility/CG-A1/ZAT/Val"}, "evap_a2_status": {"enabled": "[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/HmiStatus"}, "evap_a2_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Freezer/Utility/CG-A2/ZAT/Val"}, "evap_b1_status": {"enabled": "[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/HmiStatus"}, "evap_b1_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B1/ZAT/Val"}, "evap_b2_status": {"enabled": "[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/HmiStatus"}, "evap_b2_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/SuperChill/Utility/CG-B2/ZAT/Val"}, "evap_c1_status": {"enabled": "[default]Boars_Head/GrovePort/Club/Utility/CG-C1.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Club/Utility/CG-C1/HmiStatus"}, "evap_c1_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Club/Utility/CG-C1/ZAT/Val"}, "evap_d1_status": {"enabled": "[default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/HmiStatus"}, "evap_d1_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Palletizing/Utility/CG-D1/ZAT/Val"}, "evap_e1_status": {"enabled": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E1.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E1/HmiStatus"}, "evap_e1_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E1/ZAT/Val"}, "evap_e2_status": {"enabled": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E2.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E2/HmiStatus"}, "evap_e2_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E2/ZAT/Val"}, "evap_e3_status": {"enabled": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E3.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E3/HmiStatus"}, "evap_e3_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E3/ZAT/Val"}, "evap_e4_status": {"enabled": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E4.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E4/HmiStatus"}, "evap_e4_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/East PH/Utility/CG-E4/ZAT/Val"}, "evap_f1_status": {"enabled": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F1.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F1/HmiStatus"}, "evap_f1_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F1/ZAT/Val"}, "evap_f2_status": {"enabled": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F2.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F2/HmiStatus"}, "evap_f2_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F2/ZAT/Val"}, "evap_f3_status": {"enabled": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F3.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F3/HmiStatus"}, "evap_f3_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F3/ZAT/Val"}, "evap_f4_status": {"enabled": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F4.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F4/HmiStatus"}, "evap_f4_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/West PH/Utility/CG-F4/ZAT/Val"}, "evap_g1_status": {"enabled": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G1.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G1/HmiStatus"}, "evap_g1_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G1/ZAT/Val"}, "evap_g2_status": {"enabled": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G2.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G2/HmiStatus"}, "evap_g2_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G2/ZAT/Val"}, "evap_g3_status": {"enabled": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G3.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G3/HmiStatus"}, "evap_g3_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G3/ZAT/Val"}, "evap_g4_status": {"enabled": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G4.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G4/HmiStatus"}, "evap_g4_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G4/ZAT/Val"}, "evap_g5_status": {"enabled": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G5.Enabled", "kind": "evapStatus", "status": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G5/HmiStatus"}, "evap_g5_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Dock/Utility/CG-G5/ZAT/Val"}, "hpr_level": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HPR/LvlAIn/Val"}, "hpr_psi": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HPR/PressAIn/Val"}, "htr_level": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR/LvlAIn/Val"}, "htr_psi": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR/PressAIn/Val"}, "htr_pump": {"fmt": "lead", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR/LeadPump"}, "htr_pumphrs": {"fmt": "#0.0", "kind": "leadHours", "lead": "[default]Boars_Head/GrovePort/Machine Room/Tanks/HTR/LeadPump", "paths": ["[default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 1/RunTime/Val_TotRunHrs", "[default]Boars_Head/GrovePort/Machine Room/Pumps/HTLR-Pump 2/RunTime/Val_TotRunHrs"]}, "ltr_level": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/LTR/LvlAIn/Val"}, "ltr_psi": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/LTR/PressAIn/Val"}, "ltr_pump": {"fmt": "lead", "path": "[default]Boars_Head/GrovePort/Machine Room/Tanks/LTR/LeadPump"}, "ltr_pumphrs": {"fmt": "#0.0", "kind": "leadHours", "lead": "[default]Boars_Head/GrovePort/Machine Room/Tanks/LTR/LeadPump", "paths": ["[default]Boars_Head/GrovePort/Machine Room/Pumps/LTLR-Pump 1/RunTime/Val_TotRunHrs", "[default]Boars_Head/GrovePort/Machine Room/Pumps/LTLR-Pump 2/RunTime/Val_TotRunHrs"]}, "outside_ambient_temp": {"fmt": "#0.0", "path": "[default]Boars_Head/GrovePort/Condensers/Sensors/Outside Air Temp/AIn/Val"}}}''')
PID_CATEGORIES = ['Compressors', 'Recirculators & Pumps', 'Receivers & Vessels', 'Evaporative Condensers', 'Truck Dock & Pallet Air Units', 'System & Misc']
PID_REPORT = "OpsForms/PidVerificationCycle"


# ------------------------------------------------------------------------------------------------ session / access
def username(session):
	try:
		return str(session.props.auth.user.userName or "")
	except (Exception, Throwable):
		return ""


def allowed(session, action="Use"):
	"""Forms/<action> for the session (Roles & Permissions matrix via shared.Security)."""
	try:
		return bool(shared.Security.allowed(session, "Forms", action)) and username(session) != ""
	except (Exception, Throwable) as e:
		LOG.warn("Forms permission check failed: %s" % e)
		return False


def displayName(session):
	"""'First Last' of the session user (internal user source), else the username."""
	u = username(session)
	try:
		usr = system.user.getUser(USER_SOURCE, u)
		if usr is not None:
			full = ("%s %s" % (usr.get("firstname") or "", usr.get("lastname") or "")).strip()
			if full:
				return full
	except (Exception, Throwable):
		pass
	return u


def context(session):
	return {"user": username(session), "name": displayName(session), "use": allowed(session, "Use"),
		"viewAll": allowed(session, "ViewAll")}


def operators(session=None):
	"""Operator names from [default]_Config/Forms/Operators (comma-separated) plus the session user's own name."""
	names = []
	try:
		qv = system.tag.readBlocking([CFG + "Operators"])[0]
		names = [n.strip() for n in str(qv.value or "").split(",") if n.strip()]
	except (Exception, Throwable):
		pass
	if session is not None:
		me = displayName(session)
		if me and me.lower() not in [n.lower() for n in names]:
			names.append(me)
	return names


def operatorOptions(session):
	return [{"value": n, "label": n} for n in operators(session)]


# ------------------------------------------------------------------------------------------------ helpers
def _nq(path, params, getKey=False):
	return system.db.runNamedQuery(project=PROJECT, path=NQ + path, parameters=params, getKey=getKey)


def _py(obj):
	"""Perspective / Java structures -> plain Python (dates become epoch millis)."""
	if obj is None:
		return None
	try:
		return system.util.jsonDecode(system.util.jsonEncode(obj))
	except (Exception, Throwable):
		return obj


def _rows(ds):
	out = []
	if ds is None:
		return out
	pds = system.dataset.toPyDataSet(ds)
	cols = list(ds.getColumnNames())
	for r in pds:
		out.append(dict((c, r[c]) for c in cols))
	return out


def _str(v):
	if v is None:
		return ""
	if isinstance(v, bool):
		return "Yes" if v else ""
	return unicode(v).strip()


def _blank(v):
	return v is None or (isinstance(v, basestring) and v.strip() == "")


def _dateOf(v):
	"""Date / epoch millis / 'yyyy-MM-dd' / java Date.toString() text -> java Date (None when empty / unparseable)."""
	if v is None or v == "":
		return None
	if isinstance(v, Date):
		return v
	try:
		if isinstance(v, (int, long, float)):
			return system.date.fromMillis(long(v))
		s = unicode(v).strip()
		if len(s) >= 10 and s[4] == "-" and s[7] == "-":
			return SimpleDateFormat("yyyy-MM-dd").parse(s[:10])
		return SimpleDateFormat("EEE MMM dd HH:mm:ss zzz yyyy", Locale.US).parse(s)
	except (Exception, Throwable):
		return None


def _dateStr(v):
	"""Any date form -> 'yyyy-MM-dd' ('' when empty)."""
	d = _dateOf(v)
	return system.date.format(d, "yyyy-MM-dd") if d is not None else ""


def _toDate(s):
	return _dateOf(s)


def _get(obj, k):
	"""Item of a dict / Perspective object wrapper (None when missing)."""
	try:
		return obj[k]
	except (Exception, Throwable):
		try:
			return getattr(obj, k)
		except (Exception, Throwable):
			return None


def _today():
	return system.date.format(system.date.now(), "yyyy-MM-dd")


def _num(v):
	try:
		s = unicode(v).strip()
		return float(s) if s != "" else None
	except (Exception, Throwable):
		return None


def computed(formType, data):
	"""Averages (Excel AVERAGE over the non-blank numeric cells), '' when none."""
	out = {}
	for key, src in (SCHEMA[formType].get("computed") or {}).items():
		vals = [x for x in [_num(data.get(k)) for k in src] if x is not None]
		out[key] = ("%.1f" % (sum(vals) / len(vals))) if vals else ""
	return out


def normalize(formType, raw):
	"""View data -> stored JSON shape: every schema key, strings trimmed, dates 'yyyy-MM-dd', bools True/False."""
	s = SCHEMA[formType]
	src = raw
	raw = _py(raw) or {}
	data = {}
	for k in s["keys"]:
		v = raw.get(k)
		if k in s["bools"]:
			data[k] = bool(v)
		elif k in s["dates"]:
			data[k] = _dateStr(_get(src, k))
		else:
			data[k] = _str(v)
	data.update(computed(formType, data))
	return data


def missing(formType, data):
	"""Labels of required fields that are blank (same rules as the page's Required line)."""
	s = SCHEMA[formType]
	out = [label for key, label in s["required"] if _blank(data.get(key))]
	for rule in s.get("rules") or []:
		when = rule["when"]
		hit = False
		if "eq" in when:
			hit = _str(data.get(when["eq"][0])) == when["eq"][1]
		elif "any" in when:
			hit = any(not _blank(_str(data.get(k))) for k in when["any"])
		if hit and any(_blank(_str(data.get(k))) for k in rule["need"]):
			out.append(rule["label"])
	return out


# ------------------------------------------------------------------------------------------------ form data
def blankData(formType):
	s = SCHEMA[formType]
	d = {}
	for k in s["keys"]:
		d[k] = False if k in s["bools"] else ("" if k not in s["dates"] else None)
	return d


def newData(session, formType):
	"""Defaults for a new form: Name (and Operator 1) = the logged-in user, dates = today (Date values)."""
	d = blankData(formType)
	me = displayName(session)
	today = system.date.now()
	for k in SCHEMA[formType]["dates"]:
		d[k] = today
	d["name"] = me
	if formType == "ShiftLog":
		d["op1"] = me
	return d


def forView(formType, data):
	"""Stored JSON -> view.custom.f (date keys back to Date objects for the date inputs)."""
	d = blankData(formType)
	for k, v in (data or {}).items():
		d[k] = v
	for k in SCHEMA[formType]["dates"]:
		d[k] = _toDate(d.get(k))
	return d


def merged(formType, current, updates):
	"""view.custom.f with updates applied (date keys stay Date values)."""
	d = _py(current) or {}
	for k in SCHEMA[formType]["dates"]:
		d[k] = _dateOf(_get(current, k))
	for k, v in (updates or {}).items():
		d[k] = v
	return d


def _fmt(v, fmt):
	if v is None:
		return ""
	if fmt == "lead":
		try:
			n = int(round(float(v)))
			return str(n) if n in (1, 2) else ""
		except (Exception, Throwable):
			return ""
	try:
		return ("%.1f" % float(v)) if fmt == "#0.0" else unicode(v)
	except (Exception, Throwable):
		return unicode(v)


def liveValues(session):
	"""Daily Rounds 'Fill From Live Values': {field: text} for every field mapped to a tag (one batched read)."""
	if not allowed(session, "Use"):
		return {}
	live = SCHEMA["live"]
	paths = []
	for spec in live.values():
		for k in ("path", "lead", "running", "enabled", "status"):
			if spec.get(k) and spec[k] not in paths:
				paths.append(spec[k])
		for p in spec.get("paths") or []:
			if p not in paths:
				paths.append(p)
	vals = {}
	try:
		paxCache = {}
		qvs = system.tag.readBlocking([shared.Pax.livePath(p, paxCache) for p in paths])  # pax-bindings: mapped devices read their PAX members
		for p, qv in zip(paths, qvs):
			vals[p] = qv.value if qv.quality.isGood() else None
	except (Exception, Throwable) as e:
		LOG.warn("liveValues read failed: %s" % e)
		return {}
	out = {}
	smap = SCHEMA["evapStatusMap"]
	for key, spec in live.items():
		kind = spec.get("kind") or "value"
		v = ""
		if kind == "value":
			v = _fmt(vals.get(spec["path"]), spec.get("fmt"))
		elif kind == "leadHours":
			lead = _fmt(vals.get(spec["lead"]), "lead")
			if lead:
				v = _fmt(vals.get(spec["paths"][int(lead) - 1]), spec.get("fmt"))
		elif kind == "motorStatus":
			if spec.get("enabled") and vals.get(spec["enabled"]) is False:
				v = spec.get("oos") or ""
			elif vals.get(spec["running"]) is not None:
				v = "Running" if bool(vals.get(spec["running"])) else "Idle"
		elif kind == "evapStatus":
			if vals.get(spec["enabled"]) is False:
				v = "Out of Service"
			elif vals.get(spec["status"]) is not None:
				try:
					v = smap.get(str(int(vals.get(spec["status"]))), "")
				except (Exception, Throwable):
					v = ""
		if v != "":
			out[key] = v
	return out


def _summary(formType, data):
	"""History table summary + flags."""
	if formType == "DailyRounds":
		oos = 0
		for k, v in data.items():
			if k.endswith("_status") and v == "Out of Service":
				oos += 1
		parts = []
		if data.get("avg_probe"):
			parts.append("Avg Temp Probe %s" % data["avg_probe"])
		if data.get("avg_therm"):
			parts.append("Avg Therm %s" % data["avg_therm"])
		if data.get("control_room_temp"):
			parts.append("Control Room %s" % data["control_room_temp"])
		if data.get("outside_ambient_temp"):
			parts.append("Ambient %s" % data["outside_ambient_temp"])
		parts.append("%d Out Of Service" % oos)
		return {"shift_status": None, "abnormal": oos > 0, "release": False, "open": False,
			"summary": " | ".join(parts)[:400]}
	alarms = len([i for i in range(1, 9) if data.get("alarm%d_desc" % i)])
	unresolved = len([i for i in range(1, 9) if data.get("alarm%d_desc" % i) and data.get("alarm%d_resolved" % i) != "Yes"])
	rel = len([i for i in range(1, 5) if data.get("rel%d_desc" % i) or data.get("rel%d_location" % i)])
	status = data.get("shift_status") or ""
	parts = [status or "No Status", "%d Alarm(s)" % alarms]
	if unresolved:
		parts.append("%d Unresolved" % unresolved)
	parts.append("%d Release Entr%s" % (rel, "y" if rel == 1 else "ies"))
	if data.get("open_items") == "Yes - See Comments":
		parts.append("Open Items")
	return {"shift_status": status, "abnormal": status.startswith("Abnormal"), "release": rel > 0,
		"open": data.get("open_items") == "Yes - See Comments", "summary": " | ".join(parts)[:400]}


def submit(session, formType, raw):
	"""Validate on the gateway and insert. Returns {ok, id, message, missing}."""
	if formType not in ("DailyRounds", "ShiftLog"):
		return {"ok": False, "id": 0, "message": "Unknown form.", "missing": []}
	if not allowed(session, "Use"):
		shared.Security.require("Forms", "Use", "submit " + formType, session)
		return {"ok": False, "id": 0, "message": "You do not have permission to submit forms.", "missing": []}
	data = normalize(formType, raw)
	miss = missing(formType, data)
	if miss:
		return {"ok": False, "id": 0, "message": "Required: " + ", ".join(miss), "missing": miss}
	date = data.get("date") or _today()
	sm = _summary(formType, data)
	params = {"formType": formType, "formDate": date, "submittedBy": username(session),
		"submittedName": data.get("name") or displayName(session), "submittedAt": system.date.now(),
		"shiftStatus": sm["shift_status"], "isAbnormal": sm["abnormal"], "releaseLogged": sm["release"],
		"openItems": sm["open"], "summary": sm["summary"], "data": _json.dumps(data, sort_keys=True)}
	try:
		newId = _nq("Submission/Insert", params, getKey=True)
	except (Exception, Throwable) as e:
		LOG.error("Form submit failed (%s, %s): %s" % (formType, username(session), e))
		return {"ok": False, "id": 0, "message": "Save failed: %s" % e, "missing": []}
	LOG.info("%s #%s submitted by %s for %s" % (formType, newId, username(session), date))
	return {"ok": True, "id": int(newId), "message": "%s #%s Saved For %s" % (SCHEMA[formType]["title"], newId, date),
		"missing": [], "formType": formType, "date": date}


def getSubmission(session, submissionId):
	"""One submission (dict with data) when the session may see it (own, or Forms/ViewAll); else None."""
	if not allowed(session, "Use"):
		return None
	try:
		ds = _nq("Submission/Get", {"id": int(submissionId), "viewAll": allowed(session, "ViewAll"),
			"username": username(session)})
	except (Exception, Throwable) as e:
		LOG.warn("getSubmission %s: %s" % (submissionId, e))
		return None
	rows = _rows(ds)
	if not rows:
		return None
	r = rows[0]
	try:
		r["data"] = _json.loads(r.get("data") or "{}")
	except (Exception, Throwable):
		r["data"] = {}
	return r


def loadForView(session, submissionId):
	"""{formType, data (view shape), meta} for a read-only render, or None."""
	r = getSubmission(session, submissionId)
	if r is None:
		return None
	return {"formType": r["form_type"], "data": forView(r["form_type"], r["data"]),
		"meta": "#%s | Submitted By %s (%s) | %s" % (r["id"], r.get("submitted_name") or "", r["submitted_by"],
			system.date.format(r["submitted_at"], "yyyy-MM-dd HH:mm"))}


def history(session, formType="", start=None, end=None, userFilter=""):
	"""Submissions for the History table. Without Forms/ViewAll only the session user's own rows (enforced in SQL)."""
	if not allowed(session, "Use"):
		return []
	viewAll = allowed(session, "ViewAll")
	if start is None:
		start = system.date.addDays(system.date.now(), -30)
	if end is None:
		end = system.date.now()
	try:
		ds = _nq("Submission/List", {"formType": formType or "", "startDate": _dateStr(start), "endDate": _dateStr(end),
			"viewAll": viewAll, "username": username(session), "userFilter": (userFilter or "") if viewAll else ""})
	except (Exception, Throwable) as e:
		LOG.warn("history: %s" % e)
		return []
	out = []
	for r in _rows(ds):
		out.append({"id": r["id"], "form_date": _dateStr(r["form_date"]), "form_type": r["form_type"],
			"form": SCHEMA[r["form_type"]]["title"] if r["form_type"] in SCHEMA else r["form_type"],
			"submitted": "%s (%s)" % (r.get("submitted_name") or "", r["submitted_by"]),
			"submitted_at": r["submitted_at"], "summary": r.get("summary") or "",
			"actions": "%s:%s" % (r["form_type"], r["id"])})
	return out


def historyUsers(session):
	"""Submitter options for the History user filter (Forms/ViewAll only)."""
	if not allowed(session, "ViewAll"):
		return []
	try:
		rows = _rows(_nq("Submission/Users", {"viewAll": True}))
	except (Exception, Throwable):
		return []
	return [{"value": "", "label": "All Users"}] + [{"value": r["submitted_by"],
		"label": "%s (%s)" % (r.get("submitted_name") or r["submitted_by"], r["submitted_by"])} for r in rows]


# ------------------------------------------------------------------------------------------------ PDF (Reporting)
def _reportFor(kind):
	if kind == "PidCycle":
		return PID_REPORT
	return SCHEMA[kind]["report"]


def pdfBytes(session, kind, recordId):
	"""Report PDF bytes after the same visibility check as the History page (None when refused / failed)."""
	recordId = int(recordId or 0)
	if kind == "PidCycle":
		if not pidCanView(session, recordId):
			shared.Security.require("Forms", "ViewAll", "P&ID cycle %s PDF" % recordId, session)
			return None, None
		cyc = _pidCycle(recordId) or {}
		name = "PIDVerification_%s_%s.pdf" % (cyc.get("cycle_year") or "", (cyc.get("status") or "").replace(" ", ""))
	else:
		rec = getSubmission(session, recordId)
		if rec is None:
			shared.Security.require("Forms", "ViewAll", "%s %s PDF" % (kind, recordId), session)
			return None, None
		kind = rec["form_type"]
		name = "%s_%s_%s.pdf" % (SCHEMA[kind]["file"], _dateStr(rec["form_date"]), rec["submitted_by"])
	try:
		data = system.report.executeReport(path=_reportFor(kind), project=PROJECT,
			parameters={"recordId": recordId}, fileType="pdf")
	except (Exception, Throwable) as e:
		LOG.error("Report %s %s failed: %s" % (kind, recordId, e))
		return None, None
	return data, name


def downloadPdf(session, kind, recordId):
	"""Print / Download PDF: browser download of the Reporting PDF. Returns a status message."""
	data, name = pdfBytes(session, kind, recordId)
	if data is None:
		return "PDF Not Available"
	system.perspective.download(name, data, "application/pdf")
	return "Downloaded " + name


def reportData(kind, recordId, data):
	"""Script data source of the OpsForms reports (gateway, no session - pdfBytes checked access first)."""
	recordId = int(recordId or 0)
	if kind == "PidCycle":
		return _pidReportData(recordId, data)
	rows = _rows(_nq("Submission/Get", {"id": recordId, "viewAll": True, "username": ""}))
	if not rows:
		data["notFound"] = "Submission %s Not Found" % recordId
		return
	r = rows[0]
	try:
		d = _json.loads(r.get("data") or "{}")
	except (Exception, Throwable):
		d = {}
	for k in SCHEMA[r["form_type"]]["keys"]:
		v = d.get(k)
		if k in SCHEMA[r["form_type"]]["bools"]:
			data[k] = u"√" if v else ""
		else:
			data[k] = _str(v)
	for k, v in computed(r["form_type"], d).items():
		data[k] = v
	for op in ("op1", "op2"):
		# one Time In / Out field since 2026-10-23; records saved before that stored Time In + Time Out
		if not data.get(op + "_time"):
			times = [t for t in (_str(d.get(op + "_in")), _str(d.get(op + "_out"))) if t]
			data[op + "_time"] = " / ".join(times)
	for dk in SCHEMA[r["form_type"]]["dates"]:
		s = _str(d.get(dk))
		data[dk] = ("%s/%s/%s" % (s[5:7], s[8:10], s[:4])) if len(s) >= 10 else s
	data["notFound"] = ""
	data["recordNo"] = "#%s" % r["id"]
	data["submittedBy"] = "%s (%s)" % (r.get("submitted_name") or "", r["submitted_by"])
	data["submittedAt"] = system.date.format(r["submitted_at"], "yyyy-MM-dd HH:mm")
	data["printedAt"] = system.date.format(system.date.now(), "yyyy-MM-dd HH:mm")


# ------------------------------------------------------------------------------------------------ P&ID verification
def _pidCycle(cycleId):
	rows = _rows(_nq("Pid/CycleById", {"id": int(cycleId or 0)}))
	return rows[0] if rows else None


CYCLE_BLANK = {"id": 0, "allowed": True, "cycle_year": "", "drawing_revision": "", "performed_by": "",
	"reviewed_by": "", "status": "", "created": "", "suggestYear": 0}
SEL_BLANK = {"valve_pk": 0, "pid": "", "unit_id": "", "unit_desc": "", "valve_id": "", "size": "", "valve_type": "",
	"position": "", "function_service": "", "verified": False, "verified_by": "", "verified_date": None, "notes": "",
	"updated": ""}


def pidBlankSel():
	return dict(SEL_BLANK)


def pidOpenCycle(session):
	"""The open cycle, always the full CYCLE_BLANK shape (id 0 = none open)."""
	c = dict(CYCLE_BLANK, suggestYear=system.date.getYear(system.date.now()))
	if not allowed(session, "Use"):
		c["allowed"] = False
		return c
	rows = _rows(_nq("Pid/OpenCycle", {}))
	if not rows:
		return c
	r = rows[0]
	c.update({"id": r["id"], "cycle_year": r["cycle_year"], "drawing_revision": r.get("drawing_revision") or "",
		"performed_by": r.get("performed_by") or "", "reviewed_by": r.get("reviewed_by") or "", "status": r["status"],
		"created": "%s, %s" % (r.get("created_by") or "", system.date.format(r["created_at"], "yyyy-MM-dd"))})
	return c


def pidStartCycle(session, year, revision, performedBy, reviewedBy):
	if not allowed(session, "Use"):
		return {"ok": False, "message": "You do not have permission to start a cycle."}
	if _rows(_nq("Pid/OpenCycle", {})):
		return {"ok": False, "message": "A cycle is already open - complete it first."}
	try:
		year = int(year)
	except (Exception, Throwable):
		return {"ok": False, "message": "Enter the cycle year."}
	newId = _nq("Pid/CreateCycle", {"year": year, "revision": _str(revision), "performedBy": _str(performedBy),
		"reviewedBy": _str(reviewedBy), "user": username(session), "now": system.date.now()}, getKey=True)
	LOG.info("P&ID cycle %s (%s) started by %s" % (newId, year, username(session)))
	return {"ok": True, "id": int(newId), "message": "Cycle %s Started" % year}


def pidSaveHeader(session, cycleId, revision, performedBy, reviewedBy):
	if not allowed(session, "Use"):
		return {"ok": False, "message": "You do not have permission to edit the cycle."}
	n = _nq("Pid/UpdateCycleHeader", {"id": int(cycleId), "revision": _str(revision), "performedBy": _str(performedBy),
		"reviewedBy": _str(reviewedBy)})
	return {"ok": n > 0, "message": "Header Saved" if n > 0 else "Cycle is not open."}


def pidComplete(session, cycleId):
	if not allowed(session, "Use"):
		return {"ok": False, "message": "You do not have permission to complete the cycle."}
	n = _nq("Pid/CompleteCycle", {"id": int(cycleId), "user": username(session), "now": system.date.now()})
	if n > 0:
		LOG.info("P&ID cycle %s completed by %s" % (cycleId, username(session)))
	return {"ok": n > 0, "id": int(cycleId), "message": "Cycle Completed" if n > 0 else "Cycle is not open."}


def pidSummary(session, cycleId, category=""):
	"""Dashboard (per category + overall) and the unit options of the selected category."""
	empty = {"total": 0, "verified": 0, "remaining": 0, "pct": 0.0, "pctText": "0%", "disc": 0, "incomplete": 0}
	out = {"all": dict(empty), "units": [{"value": "", "label": "All Units"}]}
	for i, cat in enumerate(PID_CATEGORIES):
		out["c%d" % i] = dict(empty, name=cat)
	if not allowed(session, "Use"):
		return out
	rows = _rows(_nq("Pid/Summary", {"cycleId": int(cycleId or 0)}))
	tot = dict(empty)
	for r in rows:
		if r["category"] not in PID_CATEGORIES:
			continue
		c = out["c%d" % PID_CATEGORIES.index(r["category"])]
		for k in ("total", "verified", "disc", "incomplete"):
			c[k] = int(r[k] or 0)
			tot[k] += int(r[k] or 0)
	for c in [out["c%d" % i] for i in range(len(PID_CATEGORIES))] + [tot]:
		c["remaining"] = c["total"] - c["verified"]
		c["pct"] = round(100.0 * c["verified"] / c["total"], 1) if c["total"] else 0.0
		c["pctText"] = "%.0f%%" % c["pct"]
	out["all"] = tot
	units = _rows(_nq("Pid/Units", {"category": category or ""}))
	out["units"] += [{"value": u["unit_id"], "label": "%s - %s (%s)" % (u["unit_id"], u.get("unit_desc") or "", u["n"])}
		for u in units]
	return out


FLAG_STYLE = {"backgroundColor": "var(--alarm-critical)", "color": "#ffffff"}


def pidRows(session, cycleId, category="", unit="", search="", show="All"):
	"""Valve table rows for the cycle; Verified By / Date cells flagged red when verified without an operator."""
	if not allowed(session, "Use"):
		return []
	rows = _rows(_nq("Pid/Rows", {"cycleId": int(cycleId or 0), "category": category or "", "unit": unit or "",
		"search": (search or "").strip(), "show": show or "All"}))
	out = []
	for r in rows:
		verified = bool(r["verified"])
		incomplete = verified and _blank(r.get("verified_by"))
		row = {"valve_pk": r["valve_pk"], "pid": r["pid"] or "", "unit_id": r["unit_id"], "valve_id": r["valve_id"],
			"size": r["size"] or "", "valve_type": r["valve_type"] or "", "position": r["position"] or "",
			"function_service": r["function_service"] or "", "verified": verified,
			"verified_by": r.get("verified_by") or "", "verified_date": _dateStr(r.get("verified_date")),
			"notes": r.get("notes") or "", "category": r["category"], "unit_desc": r.get("unit_desc") or "",
			"updated": ("%s %s" % (r.get("updated_by") or "", system.date.format(r["updated_at"], "yyyy-MM-dd HH:mm"))
				if r.get("updated_at") else "")}
		if incomplete:
			row["verified_by"] = {"value": "Missing Operator", "style": FLAG_STYLE}
			row["verified_date"] = {"value": row["verified_date"] or "-", "style": FLAG_STYLE}
		out.append(row)
	return out


def pidSaveCheck(session, cycleId, valvePk, verified, verifiedBy, verifiedDate, notes, quick=False):
	"""Save one valve check immediately (upsert + audit log row). quick=True (table checkbox): Verified By defaults
	to the session user's name and Date to today when blank; unticking clears neither (the record stays visible)."""
	if not allowed(session, "Use"):
		shared.Security.require("Forms", "Use", "P&ID check", session)
		return {"ok": False, "message": "You do not have permission to record checks."}
	cyc = _pidCycle(cycleId)
	if not cyc or cyc.get("status") != "Open":
		return {"ok": False, "message": "This cycle is not open."}
	by = _str(verifiedBy)
	date = _dateStr(verifiedDate)
	if quick and verified:
		by = by or displayName(session)
		date = date or _today()
	n = _nq("Pid/SaveCheck", {"cycleId": int(cycleId), "valvePk": int(valvePk), "verified": bool(verified),
		"verifiedBy": by, "verifiedDate": date, "notes": _str(notes)[:1000], "user": username(session),
		"now": system.date.now()})
	return {"ok": True, "message": "Saved"}


def pidCheck(session, cycleId, valvePk):
	"""Selected valve for the editor panel: master data + this cycle's check (verified_date as a Date)."""
	if not allowed(session, "Use"):
		return pidBlankSel()
	rows = _rows(_nq("Pid/Check", {"cycleId": int(cycleId or 0), "valvePk": int(valvePk or 0)}))
	if not rows:
		return pidBlankSel()
	r = rows[0]
	return {"valve_pk": r["valve_pk"], "pid": r["pid"] or "", "unit_id": r["unit_id"], "unit_desc": r.get("unit_desc") or "",
		"valve_id": r["valve_id"], "size": r["size"] or "", "valve_type": r["valve_type"] or "",
		"position": r["position"] or "", "function_service": r["function_service"] or "",
		"verified": bool(r["verified"]), "verified_by": r.get("verified_by") or "",
		"verified_date": _toDate(_dateStr(r.get("verified_date"))), "notes": r.get("notes") or "",
		"updated": ("%s %s" % (r.get("updated_by") or "", system.date.format(r["updated_at"], "yyyy-MM-dd HH:mm"))
			if r.get("updated_at") else "")}


def pidSetField(session, cycleId, valvePk, column, value):
	"""Inline table edit (Verified checkbox or Notes): re-reads the stored check, changes that one field, saves."""
	cur = pidCheck(session, cycleId, valvePk)
	if not cur.get("valve_pk"):
		return {"ok": False, "message": "Valve not found or no permission."}
	if column == "verified":
		cur["verified"] = bool(value)
	elif column == "notes":
		cur["notes"] = _str(value)
	else:
		return {"ok": False, "message": "That column is not editable here."}
	return pidSaveCheck(session, cycleId, valvePk, cur["verified"], cur["verified_by"], cur["verified_date"],
		cur["notes"], quick=(column == "verified"))


def pidDefaultRevision():
	try:
		return str(system.tag.readBlocking([CFG + "PidDrawingRevision"])[0].value or "")
	except (Exception, Throwable):
		return ""


def pidCycles(session):
	"""History: open cycles for every Forms/Use user; completed cycles for Forms/ViewAll, or for cycles the user
	recorded checks in (enforced in SQL)."""
	if not allowed(session, "Use"):
		return []
	rows = _rows(_nq("Pid/Cycles", {"viewAll": allowed(session, "ViewAll"), "username": username(session)}))
	out = []
	for r in rows:
		out.append({"id": r["id"], "cycle_year": str(r["cycle_year"]), "status": r["status"],
			"drawing_revision": r.get("drawing_revision") or "",
			"performed": "%s / %s" % (r.get("performed_by") or "-", r.get("reviewed_by") or "-"),
			"progress": "%s / %s (%s Discrepancies)" % (r["verified"], r["total"], r["disc"]),
			"completed": ("%s %s" % (r.get("completed_by") or "", system.date.format(r["completed_at"], "yyyy-MM-dd HH:mm"))
				if r.get("completed_at") else ""),
			"actions": "PidCycle:%s:%s" % (r["id"], r["status"])})
	return out


def pidCanView(session, cycleId):
	if not allowed(session, "Use"):
		return False
	cyc = _pidCycle(cycleId)
	if cyc is None:
		return False
	if cyc.get("status") == "Open" or allowed(session, "ViewAll"):
		return True
	rows = _rows(_nq("Pid/UserChecks", {"cycleId": int(cycleId), "username": username(session)}))
	return bool(rows) and int(rows[0]["n"] or 0) > 0


def _pidReportData(cycleId, data):
	cyc = _pidCycle(cycleId)
	if cyc is None:
		data["notFound"] = "Cycle %s Not Found" % cycleId
		return
	data["notFound"] = ""
	data["cycleYear"] = _str(cyc["cycle_year"])
	data["status"] = _str(cyc["status"])
	data["drawingRevision"] = _str(cyc.get("drawing_revision"))
	data["performedBy"] = _str(cyc.get("performed_by"))
	data["reviewedBy"] = _str(cyc.get("reviewed_by"))
	data["createdBy"] = "%s %s" % (_str(cyc.get("created_by")), system.date.format(cyc["created_at"], "yyyy-MM-dd"))
	data["completedBy"] = ("%s %s" % (_str(cyc.get("completed_by")), system.date.format(cyc["completed_at"], "yyyy-MM-dd HH:mm"))
		if cyc.get("completed_at") else "Not Completed")
	data["printedAt"] = system.date.format(system.date.now(), "yyyy-MM-dd HH:mm")
	summ = _rows(_nq("Pid/Summary", {"cycleId": cycleId}))
	byCat = dict((r["category"], r) for r in summ)
	dash = []
	tot = [0, 0, 0]
	for cat in PID_CATEGORIES:
		r = byCat.get(cat) or {"total": 0, "verified": 0, "disc": 0}
		t, v, d = int(r["total"] or 0), int(r["verified"] or 0), int(r["disc"] or 0)
		tot = [tot[0] + t, tot[1] + v, tot[2] + d]
		dash.append([cat, t, v, t - v, ("%.0f%%" % (100.0 * v / t)) if t else "0%", d])
	dash.append(["TOTAL", tot[0], tot[1], tot[0] - tot[1], ("%.0f%%" % (100.0 * tot[1] / tot[0])) if tot[0] else "0%", tot[2]])
	data["dashboard"] = system.dataset.toDataSet(["category", "total", "verified", "remaining", "pct", "disc"], dash)
	rows = _rows(_nq("Pid/Rows", {"cycleId": cycleId, "category": "", "unit": "", "search": "", "show": "All"}))
	vals = []
	disc = []
	for r in rows:
		flag = "Missing Operator" if (r["verified"] and _blank(r.get("verified_by"))) else ""
		line = [r["category"], r["pid"] or "", r["unit_id"], r["valve_id"], r["size"] or "", r["valve_type"] or "",
			r["position"] or "", r["function_service"] or "", u"✓" if r["verified"] else "",
			r.get("verified_by") or "", _dateStr(r.get("verified_date")), r.get("notes") or "", flag]
		vals.append(line)
		if r.get("notes") or flag:
			disc.append(line)
	cols = ["category", "pid", "unit", "valve", "size", "type", "position", "function", "verified", "by", "date",
		"notes", "flag"]
	data["valves"] = system.dataset.toDataSet(cols, vals)
	data["discrepancies"] = system.dataset.toDataSet(cols, disc)
	data["discCount"] = str(len(disc))
