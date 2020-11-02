from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Item Details"),
			"items": [
				{
					"type": "doctype",
					"name": "Item Production Detail",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Apparelo Part",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Checking",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Ironing",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Packing",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Stitching",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Bleaching",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Dyeing",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Steaming",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Roll Printing",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Piece Printing",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Label Fusing",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Knitting",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Cutting",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Compacting",
					"onboard": 1,
				}
			]
		},
		{
			"label": _("Textile Processing"),
			"items": [
				{
					"type": "doctype",
					"name": "Lot Creation",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Lot Closure",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "DC",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "GRN",
					"onboard": 1,
				}				
			]
		},
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "IPD Item Mapping",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "IPD BOM Mapping",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Apparelo Dia",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Apparelo Style",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Apparelo Size",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Print Type",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Multi Process",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Process",
					"onboard": 1,
				}			
			]
		},
		{
			"label": _("Settings"),
			"items": [
				{
					"type": "doctype",
					"name": "Apparelo Settings",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Knitting Type",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Apparelo Yarn Shade",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Apparelo Colour",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Additional Parameters",
					"onboard": 1,
				}				
			]
		},
	]
