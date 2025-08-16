# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class arscustomer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		account_manager: DF.Link | None
		customer_details: DF.Text | None
		customer_group: DF.Literal["group 1", "group 2", "group 3"]
		customer_name: DF.Data
		customer_pos_id: DF.Data | None
		customer_type: DF.Literal["Company", "Individual", "Partnership"]
		gender: DF.Link | None
		image: DF.AttachImage | None
		industry: DF.Link | None
		language: DF.Link | None
		market_segment: DF.Link | None
		monthly_billing: DF.Float
		naming_series: DF.Literal["CUST-.YYYY.-"]
		p_address: DF.Data | None
		p_email_id: DF.Data | None
		p_first_name: DF.Data | None
		p_last_name: DF.Data | None
		p_mobile_no: DF.Data | None
		s_address: DF.Data | None
		s_email_id: DF.Data | None
		s_first_name: DF.Data | None
		s_last_name: DF.Data | None
		s_mobile_no: DF.Data | None
		salutation: DF.Link | None
		t_address: DF.Data | None
		t_email_id: DF.Data | None
		t_first_name: DF.Data | None
		t_last_name: DF.Data | None
		t_mobile_no: DF.Data | None
		tax_category: DF.Link | None
		tax_id: DF.Data | None
		tax_withholding_category: DF.Link | None
		territory: DF.Literal["Japan", "Rest of the world"]
		total_billing: DF.Float
		website: DF.Data | None
	# end: auto-generated types

	pass
