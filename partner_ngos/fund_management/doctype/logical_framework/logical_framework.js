// Copyright (c) 2020, Akram Mutaher and contributors
// For license information, please see license.txt

frappe.ui.form.on('Logical Framework', {
	refresh: function(frm) {
		frappe.route_options = {"logical_framework": frm.doc.logical_framework}
	}
});
