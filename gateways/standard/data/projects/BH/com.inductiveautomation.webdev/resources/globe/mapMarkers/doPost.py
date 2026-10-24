def doPost(request, session):
	data = request['data']

	# Globe marker hover / click -> ONLY the Perspective page that hosts the iframe (docs/globe-hover.md).
	# {"__globe": "hover"|"navigate", "sessionId", "pageId", "token", "page", "seq"?}
	try:
		isGlobe = data is not None and data.get('__globe') is not None
	except:
		isGlobe = False
	if isGlobe:
		# the iframe's own browser must hold a logged-in BH session (shared.WebAuth), then the HMAC token
		if not shared.WebAuth.perspectiveUser(request):
			return shared.WebAuth.deny(request)
		status, reason = shared.Globe.relay(data)
		if status != 200:
			try:
				request['servletResponse'].setStatus(status)
			except:
				pass
		return {'json': {'ok': status == 200, 'reason': reason}}

	# Every other body is a gateway-wide config write: admin login (HTTP Basic, AdminRoles) checked BEFORE the
	# body is inspected (shared.Globe.adminWriter, docs/globe-hover.md#security).
	status, user = shared.Globe.adminWriter(request)
	if status != 200:
		try:
			request['servletResponse'].setStatus(status)
		except:
			pass
		return {'json': {'ok': False, 'reason': 'login required' if status == 401 else 'admin role required'}}

	# GeoJSON FeatureCollection updates markers.
	try:
		isGeo = data is not None and data['type'] == 'FeatureCollection'
	except:
		isGeo = False
	if isGeo:
		system.tag.writeBlocking(['[default]_Config/MapMarkerGeoJson'], [data])
		return

	# Navigation document write: {"__nav": true, "items": [...]}
	try:
		isNav = data is not None and data.get('__nav') == True and data.get('items') is not None
	except:
		isNav = False
	if isNav:
		system.tag.writeBlocking(['[default]_Config/Navigation'], [{'items': data['items']}])
		try:
			Navigation.Nav.flushCache()
		except:
			pass
		return

	# Legacy gateway-wide hover / click bodies (_Config/MapMarkerHover / MapMarkerNavigation) are no longer
	# accepted: they reached every open session.
	try:
		request['servletResponse'].setStatus(400)
	except:
		pass
	return {'json': {'ok': False, 'reason': 'unsupported body'}}
