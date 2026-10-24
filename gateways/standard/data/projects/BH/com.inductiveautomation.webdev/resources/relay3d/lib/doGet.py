def doGet(request, session):
	# HLCO Safety Relay 3D static files (whitelist in shared.Relay3d.FILES). three.js is served by rack3d/lib.
	# Logged-in BH Perspective session only (shared.WebAuth). .cursor/tasks/safety-relay-3d/build.py - docs/safety-relay-3d.md
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
