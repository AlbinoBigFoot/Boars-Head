def openFaceplate(id, tagPath, view, modal=False, title=None, width=560, height=656, params=None):
	"""Open a device faceplate popup (Scout Navigation.Faceplate pattern, BH geometry).

	params may include tagPath plus unified Faceplate fields:
	  deviceType, webGuiUrl, showControls, showConfiguration,
	  showTrend, showAlarmConfiguration, showAlarms
	"""
	# security-tiers: Faceplates/Open in Roles & Permissions (Read Only sessions get no faceplates)
	if not shared.Security.require('Faceplates', 'Open', tagPath or view):
		return False
	popup_params = {'tagPath': tagPath}
	if params:
		try:
			for k, v in params.items():
				popup_params[k] = v
		except Exception:
			pass
	if 'tagPath' not in popup_params or not popup_params.get('tagPath'):
		popup_params['tagPath'] = tagPath
	# So the in-view Close X can close this exact popup (drag strip sits above the view).
	popup_params['popupId'] = id
	if not title:
		title = tagPath.split('/')[-1] if tagPath else 'Faceplate'
	# Native chrome header is CSS-hidden (see stylesheet .ia_popup__header).
	# In-view Faceplate header supplies title + Close X; drag uses .popup-drag.
	system.perspective.openPopup(
		id, view,
		params=popup_params,
		title=title,
		showCloseIcon=False,
		draggable=True,
		resizable=True,
		modal=modal,
		viewportBound=True,
		position={'width': width, 'height': height}
	)
	return True


# Faceplate per device UDT (Devices/<Type>), the same ones the device components open on the Machine Room page.
# Popups with their own view: (popup id prefix, view, width, height). Everything else opens the tabbed Faceplate
# shell with deviceType (Devices/Valve -> 'Valve' etc.).
DEVICE_POPUPS = {
	'Tank': ('tankov-fp-', '01_Popups/00_Faceplates/TankOverview', 1100, 760),
	'DiscreteInput': ('din-fp-', '01_Popups/00_Faceplates/DiscreteInput', 600, 600),
	'SuctionSequence': ('seq-fp-', '01_Popups/00_Faceplates/SuctionSequence', 820, 700),
	'DischargeSequence': ('seq-fp-', '01_Popups/00_Faceplates/DischargeSequence', 1180, 740),
}
NO_INTERLOCKS = ('Sensor',)   # P_AIn has no interlocks: no Interlocks tab
SHELL_TYPES = ('Pump', 'Compressor', 'Valve', 'Sensor', 'ExhaustFan', 'Evaporator', 'CoolingTower')


def openDevice(tagPath, title=None):
	"""Open the device's faceplate from its tag path alone (nav tree leaves, device tables). Returns False when the
	path is not a device with a faceplate (folders, LTU, PLC stand-ins)."""
	tagPath = str(tagPath or '').strip()
	if not tagPath:
		return False
	try:
		typeId = str(system.tag.getConfiguration(tagPath, False)[0].get('typeId') or '')
	except Exception:
		typeId = ''
	if not typeId.startswith('Devices/'):
		return False
	if not shared.Security.can('Faceplates', 'Open'):
		return False
	kind = typeId.split('/')[-1]
	if not title:
		title = tagPath.rstrip('/').split('/')[-1]
	if kind in DEVICE_POPUPS:
		prefix, view, width, height = DEVICE_POPUPS[kind]
		return openFaceplate(prefix + tagPath, tagPath, view, False, title, width, height, {'title': title}) is not False
	if kind not in SHELL_TYPES:
		return False
	webGuiUrl = ''
	if kind == 'Compressor':
		try:
			webGuiUrl = str(system.tag.readBlocking([tagPath + '/Cfg_WebGuiUrl/Value'])[0].value or '').strip()
		except Exception:
			webGuiUrl = ''
	shared.Alerts.showFaceplate(tagPath=tagPath, deviceType=kind, title=title, webGuiUrl=webGuiUrl,
		showInterlocks=kind not in NO_INTERLOCKS,
		width=560, height=656 if kind == 'Valve' else 640)   # same sizes as the device components
	return True
