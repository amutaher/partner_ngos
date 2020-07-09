# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.model.document import Document
from frappe.utils import (cstr)

class Outcomes(Document):
	def on_update(self):
		frappe.msgprint("on_update Outcomes")

	def validate(self):
		self.validate_naming()

	def validate_naming(self):
		if not self.outcome_no and self.logical_framework:
			lfw = frappe.get_doc("Logical Framework", self.logical_framework)
			if not lfw.last_outcome_no: lfw.last_outcome_no=0
			self.outcome_no="[Outcome : "+cstr(lfw.last_outcome_no+1)+" ]"
			lfw.db_set("last_outcome_no", lfw.last_outcome_no+1)
			lfw.notify_update()
