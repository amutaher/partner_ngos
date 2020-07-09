# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class IndicatorTool(Document):
	def get_conditions(self):
		conditions = []
		if self.project_proposal: conditions.append("pp.name = '%s'"%self.project_proposal)
		if self.logical_framework: conditions.append("lfw.name = '%s'"%self.logical_framework)
		if self.outcomes: conditions.append("oc.name = '%s'"%self.outcomes)
		if self.outputs: conditions.append("op.name = '%s'"%self.outputs)
		return " where {}".format(" and ".join(conditions)) if conditions else ""

	def get_indicator(self):
		"""
		"""
		return frappe.db.sql("""select distinct ide.name as indicator from `tabIndicator Detail` ide
		INNER JOIN `tabIndicators` ind ON ind.name = ide.parent
		INNER JOIN `tabOutputs` op ON op.name = ind.output
		INNER JOIN `tabOutcomes` oc ON oc.name = op.outcome
		INNER JOIN `tabLogical Framework` lfw ON lfw.name = oc.logical_framework 
		INNER JOIN `tabProject Proposal` pp ON pp.name = lfw.project_proposal
		{conditions} order by ind.indicator_no ASC
		""".format(conditions=self.get_conditions()),{}, as_dict=True)

	def get_existing_indicator(self):
		"""
		"""
		return frappe.db.sql_list("""select indicator_detail from `tabProject Indicator`
		where docstatus<2 and project=%s """,self.project)

	def create_indicator(self):
		if not self.project or (not self.project_proposal and not self.logical_framework and not self.outcomes and not self.outputs):
			frappe.throw(_("Missing data"))
		indicators = self.get_indicator()
		if not indicators:
			frappe.throw(_("No Indicators"))
		existing_indicators=self.get_existing_indicator()
		count=0
		for d in indicators:
			if d.indicator not in existing_indicators:
				pi = frappe.get_doc(frappe._dict({
					"project": self.project,
					"indicator_detail": d.indicator,
					"doctype": "Project Indicator"
				}))
				pi.check_permission('write')
				pi.insert()
				count+=1
		frappe.msgprint(_("Done with {0}").format(count))








