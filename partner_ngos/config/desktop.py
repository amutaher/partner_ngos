# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Fund Management",
			"color": "grey",
			"icon": "fa fa-university",
			"type": "module",
			"label": _("Fund Management")
		},
                {
			"module_name": "Programs Management",
			"color": "grey",
			"icon": "fa fa-product-hunt",
			"type": "module",
			"label": _("Program Management")
		},
                {
			"module_name": "MEAL",
			"color": "grey",
			"icon": "fa fa-bar-chart",
			"type": "module",
			"label": _("MEAL")
		}


	]
