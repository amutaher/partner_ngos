# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.model.document import Document
from frappe.utils import (cstr)

class Outputs(Document):
	def validate(self):
		self.validate_naming()

	def validate_naming(self):
		if not self.output_no and self.outcome:
			oc = frappe.get_doc("Outcomes", self.outcome)
			if not oc.last_output_no: oc.last_output_no=0
			self.output_no="[Output : "+oc.outcome_no.split(' ')[-2]+"."+cstr(oc.last_output_no+1)+" ]"
			oc.db_set("last_output_no", oc.last_output_no+1)
			oc.notify_update()
