---
title: "WebDev Resources Reference"
sidebar_label: "WebDev Resources"
sidebar_position: 6
description: "WebDev (HTTP endpoint) resources in the BH project."
generated: true
custom_edit_url: null
---

:::note

:::

WebDev resources are HTTP endpoints served at `/system/webdev/BH/<path>` (Designer: **Project Browser > Web Dev**). Files: `gateways/standard/data/projects/BH/com.inductiveautomation.webdev/resources`.

| Resource | Type | Enabled methods | Auth required |
|---|---|---|---|
| `globe/map` | `python-resource` | `doGet` | none |
| `globe/mapMarkers` | `python-resource` | `doGet`, `doPost`, `doPut` | none |
| `rack3d/lib` | `python-resource` | `doGet` | none |
| `rack3d/state` | `python-resource` | `doGet` | none |
| `rack3d/view` | `python-resource` | `doGet` | none |
| `relay3d/lib` | `python-resource` | `doGet` | none |
| `relay3d/state` | `python-resource` | `doGet` | none |
| `relay3d/view` | `python-resource` | `doGet` | none |

## globe/map

URL: `/system/webdev/BH/globe/map`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# Globe page (iframe on the enterprise landing page): only for a logged-in BH Perspective session in this
	# browser (shared.WebAuth). The HTML lives in shared.GlobePage. docs/security-access.md
	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	shared.WebAuth.noStore(request)
	return {'html': shared.GlobePage.html()}
```

## globe/mapMarkers

URL: `/system/webdev/BH/globe/mapMarkers`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# Marker GeoJSON for the globe iframe: a logged-in BH Perspective session in this browser (shared.WebAuth), or an
	# HMI admin login (HTTP Basic, shared.Globe.adminWriter) for tools. docs/security-access.md
	if not shared.WebAuth.perspectiveUser(request):
		if not shared.WebAuth.hasBasicHeader(request):
			return shared.WebAuth.deny(request)
		status, user = shared.Globe.adminWriter(request)
		if status != 200:
			return shared.WebAuth.deny(request, status)
	shared.WebAuth.noStore(request)
	# Read GeoJson from the MapMarkerGeoJson Tag
	geoJSON = system.tag.readBlocking(["[default]_Config/MapMarkerGeoJson"])[0].value
	if geoJSON is not None:
		geoJSON = system.util.jsonEncode(geoJSON.toDict(),5)
		return {'json': geoJSON}
	else:
		return shared.WebAuth.deny(request, 404, "no markers")
```

`doPost` (require-auth `False`, roles `-`):

```python
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
```

`doPut` (require-auth `False`, roles `-`):

```python
def doPut(request, session):
	# Gateway-wide marker write: admin login first (shared.Globe.adminWriter, docs/globe-hover.md#security).
	status, user = shared.Globe.adminWriter(request)
	if status != 200:
		try:
			request['servletResponse'].setStatus(status)
		except:
			pass
		return {'json': {'ok': False, 'reason': 'login required' if status == 401 else 'admin role required'}}
	data = request['data']
	system.tag.writeBlocking(['[default]_Config/MapMarkerGeoJson'], [data])
	return {'json': {'ok': True}}
```

## rack3d/lib

URL: `/system/webdev/BH/rack3d/lib`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# PLC Rack 3D static files (whitelist in shared.Rack3d.FILES): three.js r170 (MIT), rack3d.js / .css, demo state.

	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	name = str(request.get("remainingPath") or "").strip("/")
	r = shared.Rack3d.serveFile(request, name)
	if r is None:
		return shared.WebAuth.deny(request, 404, "not found")
	try:
		request["servletResponse"].setHeader("Cache-Control", "private, max-age=300")
	except:
		pass
	return r
```

## rack3d/state

URL: `/system/webdev/BH/rack3d/state`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# PLC Rack 3D live state, READ ONLY (system.tag.readBlocking; no writes, no secrets). Logged-in BH Perspective session

	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	shared.WebAuth.noStore(request)
	return {"json": shared.Rack3d.state(request)}
```

## rack3d/view

URL: `/system/webdev/BH/rack3d/view`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# PLC Rack 3D page (iframe on /operations/plcs/:plc/3d): only for a logged-in BH Perspective session in this browser

	if not shared.WebAuth.perspectiveUser(request):
		try:
			request["servletResponse"].setStatus(401)
			request["servletResponse"].setHeader("Cache-Control", "no-store")
		except:
			pass
		return {"html": "<!doctype html><meta charset=utf-8><title>Login Required</title><body style='font:14px sans-serif;"
		                "padding:24px'>Login Required. Open this page from the BH Perspective client.</body>"}
	shared.WebAuth.noStore(request)
	r = shared.Rack3d.serveFile(request, "view.html")
	if r is None:
		return shared.WebAuth.deny(request, 404, "not found")
	return r
```

## relay3d/lib

URL: `/system/webdev/BH/relay3d/lib`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# HLCO Safety Relay 3D static files (whitelist in shared.Relay3d.FILES). three.js is served by rack3d/lib.

	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	name = str(request.get("remainingPath") or "").strip("/")
	r = shared.Relay3d.serveFile(request, name)
	if r is None:
		return shared.WebAuth.deny(request, 404, "not found")
	try:
		request["servletResponse"].setHeader("Cache-Control", "private, max-age=300")
	except:
		pass
	return r
```

## relay3d/state

URL: `/system/webdev/BH/relay3d/state`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# HLCO Safety Relay 3D live state, READ ONLY (system.tag.readBlocking; no writes, no secrets). Logged-in BH Perspective

	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	shared.WebAuth.noStore(request)
	return {"json": shared.Relay3d.state(request)}
```

## relay3d/view

URL: `/system/webdev/BH/relay3d/view`

`doGet` (require-auth `False`, roles `-`):

```python
def doGet(request, session):
	# HLCO Safety Relay 3D page (iframe on /safety-relay/3d): only for a logged-in BH Perspective session in this browser

	if not shared.WebAuth.perspectiveUser(request):
		try:
			request["servletResponse"].setStatus(401)
			request["servletResponse"].setHeader("Cache-Control", "no-store")
		except:
			pass
		return {"html": "<!doctype html><meta charset=utf-8><title>Login Required</title><body style='font:14px sans-serif;"
		                "padding:24px'>Login Required. Open this page from the BH Perspective client.</body>"}
	shared.WebAuth.noStore(request)
	r = shared.Relay3d.serveFile(request, "view.html")
	if r is None:
		return shared.WebAuth.deny(request, 404, "not found")
	return r
```
