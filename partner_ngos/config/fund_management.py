from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Pipeline"),
			"items": [
				{
					"type": "doctype",
					"name": "Concept Note",
					
				},
				{
					"type": "doctype",
					"name": "Location",
					
				},
				{
					"type": "doctype",
					"name": "Programs",
					
				},

				
			]
		},
                {
			"label": _("Proposals"),
			"items": [
				{
					"type": "doctype",
					"name": "Project Proposal",
					"description": _("Project Proposal."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Logical Framework",
					"description": _("Logical Framework."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Outcomes and Outputs",
					"description": _("Outcomes and Outputs."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Activity",
					"description": _("Activity."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Indicators",
					"description": _("Indicators."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Budget Line",
					"description": _("Budget Line."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Work Plan",
					"description": _("Work Plan."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Proposal Documents",
					"description": _("Proposal Documents."),
					"onboard": 1,
				}
			]
		},
                {
			"label": _("Agreement"),
			"items": [
				{
					"type": "doctype",
					"name": "Donor Contract",
					"description": _("Donor Contract."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Payment Term",
					"description": _("Payment Term."),
				},
				{
					"type": "doctype",
					"name": "Payment Request",
					"description": _("Payment Request."),
				},
				{
					"type": "doctype",
					"name": "Cash Tracking",
					"description": _("Cash Tracking."),
				}


			]
		},

                {
			"label": _("Volunteer"),
			"items": [
				{
					"type": "doctype",
					"name": "Volunteer",
					"description": _("Volunteer information."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Volunteer Type",
					"description": _("Volunteer Type information."),
				}
			]
		},
		{
			"label": _("Donor"),
			"items": [
				{
					"type": "doctype",
					"name": "Donor",
					"description": _("Donor information."),
				},
				{
					"type": "doctype",
					"name": "Donor Type",
					"description": _("Donor Type information."),
				}
			]
		},

		
	]
