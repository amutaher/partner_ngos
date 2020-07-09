from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Monitoring"),
			"items": [
				{
					"type": "doctype",
					"name": "Monitoring Plan",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Monitoring Timeline",
					"description": _("Monitoring Timeline."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Monitor Type",
					"description": _("Monitor Type."),
					
				},
				{
					"type": "doctype",
					"name": "Stakeholder Assessment",
					"description": _("Stakeholder Assessment."),
					
				},
				{
					"type": "doctype",
					"name": "Complain Mechanism",
					"description": _("Complain Mechanism."),
					
				},
				{
					"type": "doctype",
					"name": "Visits Monitoring",
					"description": _("Visits Monitoring."),
					
				}
			]
		},
                {
			"label": _("Logs"),
			"items": [
				{
					"type": "doctype",
					"name": "Task Log",
					"description": _("Task Log."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Issue Log",
					"description": _("Issue Log."),
				},
				{
					"type": "doctype",
					"name": "Activity Logs",
					"description": _("Activity Logs."),
				},
				{
					"type": "doctype",
					"name": "Indicator log",
					"description": _("Indicator log."),
				},
				{
					"type": "doctype",
					"name": "Risk Register",
					"description": _("Risk Register."),
				}


			]
		},
                {
			"label": _("Reports"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "report",
					"name": "Budget Variance Report",
					"doctype": "Cost Center",
					"is_query_report": True,
									},
				{
					"type": "report",
					"name": "Work Plan Tracking",
					"doctype": "Work Plan",
					
				},
							]
		}
                		
	]
