# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.model.document import Document
from frappe.utils import (cstr)

class Indicators(Document):
	def validate(self):
		self.validate_naming()

	def validate_naming(self):
		if not self.indicator_no and self.output:
			ind = frappe.get_doc("Outputs", self.output)
			if not ind.last_indicator_no: ind.last_indicator_no=0
			self.indicator_no=ind.output_no.split(' ')[-2]+"."+cstr(ind.last_indicator_no+1)
			ind.db_set("last_indicator_no", ind.last_indicator_no+1)
			ind.notify_update()
