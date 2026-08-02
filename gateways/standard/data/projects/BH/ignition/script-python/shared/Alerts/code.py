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

def showAlert(state="info", title="", message="", showCloseBtn=True, btnTextPrimary="", btnTextSecondary="", btnIconPrimary="", btnIconSecondary="", btnIconAlignment="right", btnActionPrimary=None, btnActionSecondary=None, payload={}):
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

	# Size popup to message content (Perspective locks size at open); keep within viewport.
	msg = message if message is not None else ""
	try:
		msg_len = len(str(msg))
		line_count = str(msg).count("\n") + 1
	except:
		msg_len = 0
		line_count = 1
	height = int(min(520, max(200, 160 + msg_len * 0.55 + line_count * 14)))
	width = 520 if msg_len > 48 else 320

	system.perspective.openPopup(
		id="alertDialog", 
		view="01_Popups/00_Faceplates/Alerts/Alert", 
		params=params, 
		size={"width": width, "height": height},
		draggable=True,
		showCloseIcon=False,
		modal=False,
		overlayDismiss=True
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
		showAlarmConfiguration=True, showAlarms=True, width=560, height=640,
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
		# TravelTime (Cfg_TransitStallT) on Configuration — backs TransitStall alarm. Hide ops/status.
		if not hiddenFromConfiguration:
			hiddenFromConfiguration = (
				"OPER/,PROG/,MAINT/,Cmd/,Cmd_Open/,Cmd_Close/,Cmd_Reset/,Cmd_Position/,"
				"valveType/,OpenLS/,ClosedLS/,Failed/,Comm/,Status/,Interlock/,Alm_/,_Alarms/"
			)
		if not hiddenFromTrend:
			hiddenFromTrend = "Status/,Interlock/"
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
	Navigation.Faceplate.openFaceplate(
		"comp-fp-%s" % (tagPath or title),
		tagPath,
		"01_Popups/00_Faceplates/Faceplate",
		False,
		title,
		width,
		height,
		params
	)
