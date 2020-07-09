# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class WorkPlan(Document):
	def validate(self):
		self.sort_details()

	def get_existing_activity_list(self):
		"""
			Returns list of active employees based on selected criteria
			and for which salary structure exists
		"""
		return frappe.db.sql_list("""select activity as activity from `tabWork Plan Details` 
		where parentfield='work_plan_details' and parent=%s order by activity_no ASC""",self.name)

	def get_activity_list(self):
		"""
			Returns list of active employees based on selected criteria
			and for which salary structure exists
		"""
		return frappe.db.sql("""select ac.name as activity from `tabActivity` ac
		INNER JOIN `tabOutputs` op ON op.name = ac.output
		INNER JOIN `tabOutcomes` oc ON oc.name = op.outcome
		INNER JOIN `tabLogical Framework` lfw ON lfw.name = oc.logical_framework 
		where lfw.name=%s order by ac.activity_no ASC""",self.logical_framework, as_dict=True)

	def fill_activity(self):			
		#self.set('work_plan_details', [])
		activities = self.get_activity_list()
		if not activities:
			frappe.throw(_("No employees for the mentioned criteria"))
		existing_activities=self.get_existing_activity_list()
		for d in activities:
			if d.activity not in existing_activities:
				self.append('work_plan_details', d)
		self.sort_details()

	def sort_details(self):
		#enumerate # built-in function that return a list of (index, item) of a given list of objects), `start` is a parameter to define the first value of the index
		#sorted # built-in function that sort a list, if the list is a list of objects, do you need pass the `key` to get the value to be used in the sort comparization.
		for i, item in enumerate(sorted(self.work_plan_details, key=lambda item: item.activity_no), start=1):
			item.idx = i # define the new index to the object based on the sorted ordem



