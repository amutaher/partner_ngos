frappe.provide("frappe.treeview_settings");

frappe.treeview_settings['Budget Line'] = {
	get_tree_nodes: "partner_ngos.fund_management.doctype.budget_line.budget_line.get_children",
	add_tree_node:  "partner_ngos.fund_management.doctype.budget_line.budget_line.add_node",
	filters: [
		{
			fieldname: "logical_framework",
			fieldtype:"Link",
			options: "Logical Framework",
			label: __("Logical Framework"),
		},
		{
			fieldname: "budget_line",
			fieldtype:"Link",
			options: "Budget Line",
			label: __("Budget Line"),
			get_query: function() {
				var me = frappe.treeview_settings['Budget Line'];
				var logical_framework = me.page.fields_dict.logical_framework.get_value();
				var args = [["Budget Line", 'is_group', '=', 1]];
				if(logical_framework){
					args.push(["Budget Line", 'logical_framework', "=", logical_framework]);
				}
				return {
					filters: args
				};
			}
		}
	],
	breadcrumb: "Projects",
	get_tree_root: false,
	root_label: "All Budget Line",
	ignore_fields: ["parent_budget_line"],
	onload: function(me) {
		frappe.treeview_settings['Budget Line'].page = {};
		$.extend(frappe.treeview_settings['Budget Line'].page, me.page);
		me.make_tree();
	},
	toolbar: [
		{
			label:__("Add Multiple"),
			condition: function(node) {
				return node.expandable;
			},
			click: function(node) {
				this.data = [];
				const dialog = new frappe.ui.Dialog({
					title: __("Add Multiple Budget Line"),
					fields: [
						{
							fieldname: "multiple_budget_line", fieldtype: "Table",
							in_place_edit: true, data: this.data,
							get_data: () => {
								return this.data;
							},
							fields: [{
								fieldtype:'Data',
								fieldname:"budget_line_description",
								in_list_view: 1,
								reqd: 1,
								label: __("Budget Line Description")
							}]
						},
					],
					primary_action: function() {
						dialog.hide();
						return frappe.call({
							method: "partner_ngos.fund_management.doctype.budget_line.budget_line.add_multiple_budget_line",
							args: {
								data: dialog.get_values()["multiple_budget_line"],
								parent: node.data.value
							},
							callback: function() { }
						});
					},
					primary_action_label: __('Create')
				});
				dialog.show();
			}
		}
	],
	extend_toolbar: true
};