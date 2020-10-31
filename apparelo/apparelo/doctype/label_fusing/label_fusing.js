// Copyright (c) 2019, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt
{% include 'apparelo/apparelo/common_fields.js' %};
frappe.ui.form.on('Label Fusing', {
	get_piece_color:function(frm){
		const set_fields_color =['item','piece_colour','part_colour'];
		frappe.call({
			method: "apparelo.apparelo.doctype.stitching.stitching.get_additional_item_piece_colour",
			freeze: true,
			args: {doc: frm.doc},
			callback: function(r) {
				if(r.message) {
					frm.set_value('additional_parts_colour', []);
					$.each(r.message, function(i, d) {
						var item = frm.add_child('additional_parts_colour');
						for (let key in d) {
							if (d[key] && in_list(set_fields_color, key)) {
								item[key] = d[key];
							}
						}
					});
				}
				refresh_field('additional_parts_colour');
			}
		});
	},
	get_piece_size:function(frm){
		const set_fields_size =['item','piece_size','part_size'];
		frappe.call({
			method: "apparelo.apparelo.doctype.stitching.stitching.get_additional_item_size",
			freeze: true,
			args: {doc: frm.doc},
			callback: function(r) {
				if(r.message) {
					frm.set_value('additional_parts_size', []);
					$.each(r.message, function(i, d) {
						var item = frm.add_child('additional_parts_size');
						for (let key in d) {
							if (d[key] && in_list(set_fields_size, key)) {
								item[key] = d[key];
							}
						}
					});
				}
				refresh_field('additional_parts_size');
			}
		});
	}
	
});

