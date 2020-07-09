// Copyright (c) 2020, Akram Mutaher and contributors
// For license information, please see license.txt

frappe.ui.form.on('Indicator Tool', {
	refresh: function(frm) {
		frm.disable_save();
	},
	create_indicator: function (frm) {
		return frappe.call({
			doc: frm.doc,
			method: 'create_indicator',
			callback: function(r) {
			}
		})
	}

});
