def openFaceplate(id, tagPath, view, modal=False, title=None, width=420, height=520):
	"""Open a device faceplate popup (Scout Navigation.Faceplate pattern, BH geometry)."""
	params = {'tagPath': tagPath}
	if not title:
		title = tagPath.split('/')[-1] if tagPath else 'Faceplate'
	system.perspective.openPopup(
		id, view,
		params=params,
		title=title,
		showCloseIcon=True,
		draggable=True,
		resizable=True,
		modal=modal,
		viewportBound=True,
		position={'width': width, 'height': height}
	)
