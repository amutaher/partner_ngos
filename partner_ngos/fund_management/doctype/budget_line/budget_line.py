# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from frappe import _, throw
from frappe.utils import add_days, cstr, date_diff, get_link_to_form, getdate
from frappe.utils.nestedset import NestedSet
from frappe.desk.form.assign_to import close_all_assignments, clear
from frappe.utils import (cstr,date_diff)

#class CircularReferenceError(frappe.ValidationError): pass
#class EndDateCannotBeGreaterThanProjectEndDateError(frappe.ValidationError): pass

class BudgetLine(NestedSet):
	def validate(self):
		self.validate_naming()

	def validate_naming(self):
		if not self.budget_no and self.logical_framework:
			if self.parent_budget_line:
				bgl = frappe.get_doc("Budget Line", self.parent_budget_line)
				if not bgl.last_no: bgl.last_no=0
				self.budget_no=bgl.budget_no+"."+cstr(bgl.last_no+1)
				bgl.db_set("last_no", bgl.last_no+1)
				bgl.notify_update()
			else:				
				lfw = frappe.get_doc("Logical Framework", self.logical_framework)
				if not lfw.last_budget_no: lfw.last_budget_no=0
				self.budget_no=cstr(lfw.last_budget_no+1)
				lfw.db_set("last_budget_no", lfw.last_budget_no+1)
				lfw.notify_update()

	nsm_parent_field = 'parent_budget_line'

def populate_depends_on(self):
		if self.parent_budget_line:
			parent = frappe.get_doc('Budget Line', self.parent_budget_line)
			if not self.name in [row.budget_line for row in parent.depends_on]:
				parent.append("depends_on", {
					"doctype": "Budget Line Depends On",
					"budget_line": self.name,
					"subject": self.budget_line_description
				})
				parent.save()

@frappe.whitelist()
def check_if_child_exists(name):
	child_tasks = frappe.get_all("Budget Line", filters={"parent_budget_line": name})
	child_tasks = [get_link_to_form("Budget Line", budget_line.name) for budget_line in child_tasks]
	return child_tasks


 
@frappe.whitelist()
def get_children(doctype, parent, budget_line=None, logical_framework=None, is_root=False):

	filters = [['docstatus', '<', '2']]

	if budget_line:
		filters.append(['parent_budget_line', '=', budget_line])
	elif parent and not is_root:
		# via expand child
		filters.append(['parent_budget_line', '=', parent])
	else:
		filters.append(['ifnull(`parent_budget_line`, "")', '=', ''])

	if logical_framework:
		filters.append(['logical_framework', '=', logical_framework])

	budgets = frappe.get_list(doctype, fields=[
		'name as value',
		'budget_line_description as title',
		'is_group as expandable'
	], filters=filters, order_by='name')

	# return budgets
	return budgets

@frappe.whitelist()
def add_node():
	from frappe.desk.treeview import make_tree_args
	args = frappe.form_dict
	args.update({
		"name_field": "budget_line_description"
	})
	args = make_tree_args(**args)

	if args.parent_budget_line == 'All Budget Line' or args.parent_budget_line == args.logical_framework:
		args.parent_budget_line = None

	frappe.get_doc(args).insert()

@frappe.whitelist()
def add_multiple_budget_line(data, parent):
	data = json.loads(data)
	new_doc = {'doctype': 'Budget Line', 'parent_budget_line': parent if parent!="All Budget Line" else ""}
	new_doc['logical_framework'] = frappe.db.get_value('Budget Line', {"name": parent}, 'logical_framework') or ""

	for d in data:
		if not d.get("budget_line"): continue
		new_doc['budget_line_description'] = d.get("budget_line_description")
		new_budget_line = frappe.get_doc(new_doc)
		new_budget_line.insert()


