from operator import itemgetter

def getAlarmTags():
	alarmTags = []
	results = system.tag.browse('').getResults()
	for result in results:
		if result["name"] not in ["_types_", "System"]:
			provider = str(result['name'])
			query = {
			  "condition": {
			    "tagType": "AtomicTag",
			    "attributes": {
			      "values": [
			        "alarm"
			      ]
			    }
			  }
			}
			results = system.tag.query(provider, query)
			results = sorted(results, key=itemgetter('fullPath'))
			for result in results:
				alarmTags.append(str(result['fullPath']).rsplit('/',1)[0])
	
	return alarmTags
	
def getHistoricalTags():
	historicalTags = []
	results = system.tag.browse('').getResults()
	for result in results:
		if result["name"] not in ["_types_", "System"]:
			provider = str(result['name'])
			query = {
			  "options": {
			    "includeUdtMembers": True,
			    "includeUdtDefinitions": False
			  },
			  "condition": {
			    "path": "*",
			    "attributes": {
			      "values": [
			        "history"
			      ],
			      "requireAll": True
			    },
			    "properties": {
			      "op": "Or",
			      "conditions": [
			        {
			          "op": "And",
			          "conditions": [
			            {
			              "prop": "name",
			              "comp": "Equal",
			              "value": "Value"
			            },
			            {
			              "prop": "enabled",
			              "comp": "Equal",
			              "value": True
			            }
			          ]
			        }
			      ]
			    }
			  },
			  "returnProperties": [
			    "tagType",
			    "quality"
			  ]
			}
			results = system.tag.query(provider, query)
			results = sorted(results, key=itemgetter('fullPath'))
			for result in results:
				fp = str(result["fullPath"])
				if "_Config" not in fp and "_SiteInfo" not in fp and "_Sim_" not in fp:
					historicalTags.append(fp.rsplit('/',1)[0])
	
	return historicalTags
	
def createTree(paths):
	tree = []
	for path in paths:
		components = path.replace('[','').replace(']', '/').split('/')
		current = tree
		hasChildren = True
		for idx, component in enumerate(components):
			if component == '':
				continue
			found = False
			if component == components[-1]:
				hasChildren = False
				
			for item in current:
				if item['label'] == component:
					current = item['items']
					found = True
					break
				
			if not found:
				# Lightspeed default: all folders start collapsed
				new_item = {'label': component, 'expanded': False, 'data': {'tagPath': path, 'hasChildren': hasChildren}, 'items': []}
				current.append(new_item)
				current = new_item['items']
	return tree
