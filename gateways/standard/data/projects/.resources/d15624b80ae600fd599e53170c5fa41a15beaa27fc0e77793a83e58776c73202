def openFaceplate(id, tagPath, view, modal=False, title=None, width=560, height=640, params=None):
	"""Open a device faceplate popup (Scout Navigation.Faceplate pattern, BH geometry).

	params may include tagPath plus unified Faceplate fields:
	  deviceType, webGuiUrl, showControls, showConfiguration,
	  showTrend, showAlarmConfiguration, showAlarms
	"""
	popup_params = {'tagPath': tagPath}
	if params:
		try:
			for k, v in params.items():
				popup_params[k] = v
		except Exception:
			pass
	if 'tagPath' not in popup_params or not popup_params.get('tagPath'):
		popup_params['tagPath'] = tagPath
	if not title:
		title = tagPath.split('/')[-1] if tagPath else 'Faceplate'
	system.perspective.openPopup(
		id, view,
		params=popup_params,
		title=title,
		showCloseIcon=True,
		draggable=True,
		resizable=True,
		modal=modal,
		viewportBound=True,
		position={'width': width, 'height': height}
	)
