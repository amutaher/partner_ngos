# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.model.document import Document

class LogicalFramework(Document):
	def on_update(self):
		frappe.msgprint("on_update")
	def validate(self):
		if self.outcomes:
			for oc in self.outcomes:
				master = frappe.get_doc("Outcomes", oc.outcome_id)
				master.logical_framework=self.name
				master.save()
				#master.db_set("logical_framework", self.name)
		self.reload()
		#self.save()
		#oc_list=[d.outcome_id for d in self.outcomes]
		##oc_list=frappe.db.sql_list("""select outcome_id from `tabOutcomes Table` where parentfield='outcomes' and parent=%s """,self.name)
		##frappe.msgprint(lfw_list)
		#if oc_list:
		#	frappe.db.sql("""update `tabOutcomes` set logical_framework= %(lfw)s where name IN %(oc)s""", {"lfw":self.name,"oc":tuple(oc_list)})

	#def sort_details(self):
		#for i, item in enumerate(sorted(self.work_plan_details, key=lambda item: item.activity_no), start=1):
			#item.idx = i # define the new index to the object based on the sorted ordem
