""" Alert Popup Script

This script allows for easy interaction with the alert popup view.  It
allows to repeatable control of the popup

The following functions are available
    * showAlert - Opens the alert popup
    * showAdhocTrend - Opens the AdhocTrend faceplate popup (in-page trending)
    * showAdhocTrendConfig - Opens Trend Configuration beside the AdhocTrend faceplate
    * showFaceplate - Opens the shared tabbed Faceplate shell (deviceType + tabs)

"""
POPUP_ADHOC_TREND = "AdhocTrend"
VIEW_ADHOC_TREND = "01_Popups/00_Faceplates/AdhocTrend"
POPUP_ADHOC_TREND_CONFIG = "AdhocTrendConfig"
VIEW_ADHOC_TREND_CONFIG = "01_Popups/00_Faceplates/AdhocTrendConfig"

# Faceplate geometry — config sits immediately left of AdhocTrend (bottom-right).
ADHOC_TREND_WIDTH = 960
ADHOC_TREND_HEIGHT = 780
ADHOC_TREND_CONFIG_WIDTH = 340
ADHOC_TREND_CONFIG_HEIGHT = 520
ADHOC_TREND_GAP = 12

def confirmApplyWrite(label, tagPath, newValue, oldValue=None, title="Apply configuration",
		extraPayload=None, btnTextApply="Apply"):
	"""Confirm before writing a config value. Cancel does not write.

	No dialog (and no write) if newValue equals oldValue.
	"""
	try:
		if oldValue is not None and shared.Audit.valuesEqual(newValue, oldValue):
			return
	except Exception:
		if oldValue is not None and newValue == oldValue:
			return
	lbl = label if label not in (None, "") else (str(tagPath or "").split("/")[-1] or "Parameter")
	old_s = "—" if oldValue is None else str(oldValue)
	new_s = str(newValue)
	msg = (
		"Apply this configuration change?<br><br>"
		"<b>%s</b><br>Old: %s<br>New: %s"
	) % (lbl, old_s, new_s)
	payload = {
		"tagPath": tagPath,
		"value": newValue,
		"label": lbl,
		"oldValue": oldValue,
		"viewName": "",
	}
	if extraPayload:
		try:
			payload.update(dict(extraPayload))
		except Exception:
			pass
	showAlert(
		state="info",
		title=title,
		message=msg,
		showCloseBtn=False,
		btnTextPrimary=btnTextApply or "Apply",
		btnTextSecondary="Cancel",
		btnActionPrimary="writeValue",
		btnActionSecondary="cancel",
		payload=payload,
		overlayDismiss=False,
	)


def promptConfigWrite(component, propPath, tagPath, label, newValue, oldValue):
	"""Snap the widget back to oldValue, then confirm. Tag writes only on Apply."""
	try:
		if str(propPath).endswith("selected"):
			component.props.selected = bool(oldValue)
		elif str(propPath).endswith("value"):
			component.props.value = oldValue
		elif str(propPath).endswith("text"):
			component.props.text = oldValue if oldValue is not None else ""
	except Exception:
		pass
	try:
		component.refreshBinding(propPath)
	except Exception:
		pass
	confirmApplyWrite(
		label=label,
		tagPath=tagPath,
		newValue=newValue,
		oldValue=oldValue,
		extraPayload={"viewName": ""},
	)


def showAlert(state="info", title="", message="", showCloseBtn=True, btnTextPrimary="", btnTextSecondary="", btnIconPrimary="", btnIconSecondary="", btnIconAlignment="right", btnActionPrimary=None, btnActionSecondary=None, payload={}, overlayDismiss=True):
	"""Opens the alert popup
	
	Parameters
	----------
	state : str
	    Affects styling of the popup.  Options are info, warning, error, success
	title : str
	    The title to display for the popup.
	message : str
	    The message to display in the body of the popup
	showCloseBtn : bool
	    Controls visibility of the close button in the top right corner of the popup
	btnTextPrimary : str
	    The text to display on the primary button
	btnTextSecondary : str
	    The text to display on the secondary button
	btnIconPrimary : str
		The icon path to display on the primary button
	btnIconSecondary : str
		The icon path to display on the secondary button
	btnActionPrimary : str
		The message handler to invoke when the primary button is clicked
	btnActionSecondary : str
		The message handler to invoke when the secondary button is clicked
	btnIconAlignment : str
	    The icon alignment inside the primary and secondary buttons
	"""
	
	params = {
		"state":state, 
		"title":title, 
		"message":message, 
		"showCloseBtn":showCloseBtn, 
		"btnTextPrimary":btnTextPrimary, 
		"btnTextSecondary":btnTextSecondary, 
		"btnIconPrimary":btnIconPrimary, 
		"btnIconSecondary":btnIconSecondary, 
		"btnIconAlignment":btnIconAlignment, 
		"btnActionPrimary":btnActionPrimary, 
		"btnActionSecondary":btnActionSecondary, 
		"payload":payload
	}

	# Compact confirm: count <br> lines; avoid 520px empty body / inner scrollbars.
	msg = message if message is not None else ""
	try:
		msg_s = str(msg)
		msg_len = len(msg_s)
		line_count = msg_s.count("\n") + msg_s.lower().count("<br") + 1
	except:
		msg_len = 0
		line_count = 1
	height = int(min(300, max(168, 72 + line_count * 18 + (26 if title else 0) + 44)))
	width = 400 if msg_len > 48 else 320

	system.perspective.openPopup(
		id="alertDialog", 
		view="01_Popups/00_Faceplates/Alerts/Alert", 
		params=params, 
		size={"width": width, "height": height},
		draggable=True,
		showCloseIcon=False,
		modal=False,
		overlayDismiss=overlayDismiss
	)

def showAdhocTrend():
	"""Open (or refocus) the Adhoc trending faceplate on the current page.

	Bottom-right placement matches Ticket Logger / contextMenuTicketLog.
	Faceplate embeds Trend in faceplateMode (no tag browser tree); pens come
	from ContextMenu Add to trend / session.custom.AdhocTrend.
	"""
	system.perspective.openPopup(
		id=POPUP_ADHOC_TREND,
		view=VIEW_ADHOC_TREND,
		position={
			"bottom": 10,
			"right": 10,
			"width": ADHOC_TREND_WIDTH,
			"height": ADHOC_TREND_HEIGHT
		},
		draggable=True,
		resizable=True,
		showCloseIcon=False,
		modal=False,
		overlayDismiss=True,
		viewportBound=True
	)

def showAdhocTrendConfig():
	"""Open Trend Configuration as a floating companion to the AdhocTrend faceplate.

	Non-modal (no viewport dim). Placed immediately left of AdhocTrend using the
	same bottom offset. Binds to session.custom.AdhocTrend — closing config does
	not close the trend faceplate.
	"""
	system.perspective.openPopup(
		id=POPUP_ADHOC_TREND_CONFIG,
		view=VIEW_ADHOC_TREND_CONFIG,
		position={
			"bottom": 10,
			"right": 10 + ADHOC_TREND_WIDTH + ADHOC_TREND_GAP,
			"width": ADHOC_TREND_CONFIG_WIDTH,
			"height": ADHOC_TREND_CONFIG_HEIGHT
		},
		draggable=True,
		resizable=False,
		showCloseIcon=False,
		modal=False,
		overlayDismiss=True,
		viewportBound=True
	)

def closeAdhocTrendConfig():
	"""Close the companion Trend Configuration popup if open."""
	try:
		system.perspective.closePopup(POPUP_ADHOC_TREND_CONFIG)
	except:
		pass
	try:
		system.perspective.closePopup("AdhocTrendToolBar")
	except:
		pass

def contextMenuTicketLog(tagPath="", viewName=None):
	
	params = {
		'tagPath':tagPath,
		'viewName':viewName
	}
	system.perspective.openPopup(
		id="ticketLog" + tagPath, 
		view="98_Configuration/TicketLogger", 
		params=params,
		position={'bottom':10,'right':10},
		draggable = True,
		showCloseIcon=False,
		modal=False,
		overlayDismiss=True
	)

def showFaceplate(tagPath="", deviceType="Compressor", webGuiUrl="", title=None,
		showControls=True, showConfiguration=True, showInterlocks=True, showTrend=True,
		showAlarmConfiguration=True, showAlarms=True, width=560, height=656,
		hiddenFromConfiguration="", hiddenFromTrend="",
		hiddenFromAlarmConfiguration="", hiddenFromAlarms=""):
	"""Open the shared tabbed Faceplate shell (Scout-style).

	Caller show* flags are hints ANDed with Faceplate tagFlags (empty tabs hide).
	deviceType selects Controls embeds under 01_Popups/00_Faceplates/_Assets/...
	hiddenFrom* are comma-separated paths; entries ending with / match a folder prefix.
	"""
	# Device-type curation defaults (caller can override / extend).
	dt = deviceType or "Compressor"
	if dt == "Valve":
		# Curate Configuration to Cfg_* + TravelTime; hide ops / ready / alarms.
		if not hiddenFromConfiguration:
			hiddenFromConfiguration = (
				"OPER/,PROG/,MAINT/,Cmd/,Cmd_Open/,Cmd_Close/,Cmd_Reset/,Cmd_Position/,Cmd_Bypass/,"
				"Cmd_Enable/,Cmd_Disable/,Cmd_ResetAckAll/,valveType/,OpenLS/,ClosedLS/,Failed/,Comm/,"
				"Status/,Interlock/,Alm_/,Ack_/,PermOK/,Rdy_/,Nrdy_/,Disabled/,Ovrd/,_Alarms/"
			)
		if not hiddenFromTrend:
			hiddenFromTrend = "Status/,Interlock/,Nrdy_/,Rdy_/,Cfg_/,Ack_/"
		if not hiddenFromAlarmConfiguration:
			hiddenFromAlarmConfiguration = "Cfg_/,Nrdy_/,Rdy_/,Cmd_/,OPER/,PROG/,MAINT/"
		if not hiddenFromAlarms:
			hiddenFromAlarms = "Cfg_/,Nrdy_/,Rdy_/"
	params = {
		"tagPath": tagPath,
		"deviceType": dt,
		"webGuiUrl": webGuiUrl or "",
		"showControls": bool(showControls),
		"showConfiguration": bool(showConfiguration),
		"showInterlocks": bool(showInterlocks),
		"showTrend": bool(showTrend),
		"showAlarmConfiguration": bool(showAlarmConfiguration),
		"showAlarms": bool(showAlarms),
		"hiddenFromConfiguration": hiddenFromConfiguration or "",
		"hiddenFromTrend": hiddenFromTrend or "",
		"hiddenFromAlarmConfiguration": hiddenFromAlarmConfiguration or "",
		"hiddenFromAlarms": hiddenFromAlarms or "",
	}
	if not title:
		title = tagPath.split("/")[-1] if tagPath else "Faceplate"
	popupId = "comp-fp-%s" % (tagPath or title)
	params["popupId"] = popupId
	Navigation.Faceplate.openFaceplate(
		popupId,
		tagPath,
		"01_Popups/00_Faceplates/Faceplate",
		False,
		title,
		width,
		height,
		params
	)
