def doGet(request, session):
	# Globe page (iframe on the enterprise landing page): only for a logged-in BH Perspective session in this
	# browser (shared.WebAuth). The HTML lives in shared.GlobePage. docs/security-access.md
	if not shared.WebAuth.perspectiveUser(request):
		return shared.WebAuth.deny(request)
	shared.WebAuth.noStore(request)
	return {'html': shared.GlobePage.html()}
