# -*- coding: utf-8 -*-
# Copyright (c) 2020, Akram Mutaher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _, throw
from frappe.model.document import Document
from frappe.utils import (flt, getdate, get_last_day)

class ProjectIndicatorLog(Document):
	def validate(self):
		self.total_=self.men_+self.women_+self.boys_+self.girls_+self.unclassified_
		self.validate_duplicate()
		self.validate_dates()

	def validate_duplicate(self):
		conditions = " where docstatus<2 and project_indicator = '%s'" % self.project_indicator
		conditions += " and month = '%s'" % self.month
		if frappe.db.exists(self.doctype, self.name):
			conditions += " and name <> '%s'" % self.name
		sum_name = frappe.db.sql("""select count(name) from `tabProject Indicator Log` %s"""% conditions)[0][0]
		if sum_name > 0:
			frappe.throw(_("Already exists with same Project Indicator, and Month"))

	def validate_dates(self):
		months = {
			"Jan": '01',
			"Feb": '02',
			"Mar": '03',
			"Apr": '04',
			"May": '05',
			"Jun": '06',
			"Jul": '07',
			"Aug": '08',
			"Sep": '09',
			"Oct": '10',
			"Nov": '11',
			"Dec": '12'
		}
		if self.month and self.fiscal_year and (not self.start_date or not self.last_date):
			self.start_date=getdate(self.fiscal_year+'-'+months[self.month]+'-01')
			self.last_date=get_last_day(self.start_date)

	def on_submit(self):
		self.update_master(True)
		# create the BSC Ledger Entry #
		#


	def on_cancel(self):
		self.update_master(False)

	def update_master(self, increase = True):
		master = frappe.get_doc("Project Indicator", self.project_indicator)
		master.db_set("men_", (master.men_+ self.men_) if increase == True else (master.men_- self.men_) )
		master.db_set("women_", (master.women_+ self.women_) if increase == True else (master.women_- self.women_) )
		master.db_set("boys_", (master.boys_+ self.boys_) if increase == True else (master.boys_- self.boys_) )
		master.db_set("girls_", (master.girls_+ self.girls_) if increase == True else (master.girls_- self.girls_) )
		master.db_set("unclassified_", (master.unclassified_+ self.unclassified_) if increase == True else (master.unclassified_- self.unclassified_) )
		master.db_set("total_", (master.total_+ self.total_) if increase == True else (master.total_- self.total_) )
		master.db_set("percent", ( flt(master.men_+ self.total_) / flt(master.total) * 100.0 ) if increase == True else  ( flt(master.men_- self.total_) / flt(master.total) * 100.0 ))




