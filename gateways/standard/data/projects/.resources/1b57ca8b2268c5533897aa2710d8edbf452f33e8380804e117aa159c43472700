def doPost(request, session):
	data = request['data']
	# GeoJSON FeatureCollection updates markers; otherwise navigation payload.
	try:
		isGeo = data is not None and data['type'] == 'FeatureCollection'
	except:
		isGeo = False
	if isGeo:
		system.tag.writeBlocking(['[default]_Config/MapMarkerGeoJson'], [data])
	else:
		system.tag.writeBlocking(['[default]_Config/MapMarkerNavigation'], [data])
