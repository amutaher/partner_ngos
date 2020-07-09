from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Programs"),
			"items": [
				{
					"type": "doctype",
					"name": "Programs",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Project Indicator",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Project Indicator Log",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Indicator Tool",
					"onboard": 1,
				},
				
			]
		},
                		
	]
