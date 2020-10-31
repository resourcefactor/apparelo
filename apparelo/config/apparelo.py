from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Textile"),
			"items": [
				{
					"type": "doctype",
					"name": "Checking",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Set Item Mapping",
					"onboard": 1,
				}
			]
		}
	]
