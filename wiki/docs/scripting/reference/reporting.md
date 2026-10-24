---
title: "Reporting Resources Reference"
sidebar_label: "Reporting Resources"
sidebar_position: 7
description: "Reporting module resources (PDF layouts) in the BH project."
generated: true
custom_edit_url: null
---

:::note

:::

Reports live in `gateways/standard/data/projects/BH/com.inductiveautomation.reporting/reports` (Designer: **Project Browser > Reports**). Each `data.bin` is the Ignition XML serialization of the report (parameters, data sources, layout).

| Report | Parameters | Data sources | Format |
|---|---|---|---|
| `OpsForms/DailyRoundsLog` | `recordId` | `formData` | XML |
| `OpsForms/NH3ShiftLog` | `recordId` | `formData` | XML |
| `OpsForms/PidVerificationCycle` | `recordId` | `formData` | XML |
| `Reports/CustomReport` | `payload` | `reportData` | XML |

## OpsForms/DailyRoundsLog

Refrigeration Daily Rounds (Operations &gt; Forms). Parameter recordId = ops\_form\_submission.id.

| Parameter | Type | Default |
|---|---|---|
| `recordId` | `Integer` | `0` |

Data source `formData` (ScriptReportDataObject):

```python
	# Operations Forms: fills the @keys@ from the stored record (access is checked by shared.Forms.pdfBytes)
	shared.Forms.reportData('DailyRounds', data['recordId'], data)
```

## OpsForms/NH3ShiftLog

NH3 Refrigeration Shift Log (Operations &gt; Forms). Parameter recordId = ops\_form\_submission.id.

| Parameter | Type | Default |
|---|---|---|
| `recordId` | `Integer` | `0` |

Data source `formData` (ScriptReportDataObject):

```python
	# Operations Forms: fills the @keys@ from the stored record (access is checked by shared.Forms.pdfBytes)
	shared.Forms.reportData('ShiftLog', data['recordId'], data)
```

## OpsForms/PidVerificationCycle

Annual P&ID Verification cycle record (Operations &gt; Forms). Parameter recordId = ops\_pid\_cycle.id.

| Parameter | Type | Default |
|---|---|---|
| `recordId` | `Integer` | `0` |

Data source `formData` (ScriptReportDataObject):

```python
	# Operations Forms: fills the @keys@ from the stored record (access is checked by shared.Forms.pdfBytes)
	shared.Forms.reportData('PidCycle', data['recordId'], data)
```

## Reports/CustomReport

Generic custom report (Production KPIs, Alarms, any source in the shared.Reports catalog).

| Parameter | Type | Default |
|---|---|---|
| `payload` | `String` | `{}` |

Data source `reportData` (ScriptReportDataObject):

```python
	# Custom report (shared.Reports): the run result arrives as JSON in the 'payload' parameter, already
	# permission-checked by shared.Reports.output; this turns it into nested QueryResults for the layout.
	shared.Reports.reportData(data)
```
