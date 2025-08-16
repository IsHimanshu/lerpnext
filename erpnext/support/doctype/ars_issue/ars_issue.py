# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class arsissue(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		agreement_status: DF.Literal["First Response Due", "Resolution Due", "Fulfilled", "Failed"]
		attachment: DF.Attach | None
		avg_response_time: DF.Duration | None
		case_origin: DF.Literal["None", "\u96fb\u8a71", "Chatwork", "Backlog", "Slack", "\u30b9\u30d7\u30ec\u30c3\u30c9\u30b7\u30fc\u30c8", "\u8907\u6570\u306e\u624b\u6bb5"]
		category: DF.Literal["None", "\u64cd\u4f5c\u8aac\u660e", "\u4f5c\u696d\u4f9d\u983c", "\u6a5f\u80fd\u8981\u671b", "\u4e0d\u5177\u5408", "\u969c\u5bb3", "\u8acb\u6c42\u66f8\u3001\u5408\u610f\u66f8", "\u305d\u306e\u4ed6"]
		client_name: DF.Data | None
		company: DF.Link | None
		contact: DF.Link | None
		content_type: DF.Data | None
		customer: DF.Link | None
		customer_name: DF.Data | None
		customization: DF.Literal["\u5bfe\u8c61", "\u5bfe\u8c61\u5916"]
		description: DF.TextEditor | None
		development_representative: DF.Literal[None]
		email_account: DF.Link | None
		email_address1: DF.Data | None
		file1: DF.Attach | None
		file2: DF.Attach | None
		file3: DF.Attach | None
		first_responded_on: DF.Datetime | None
		first_response_time: DF.Duration | None
		image1: DF.AttachImage | None
		inquiry_handler: DF.Literal[None]
		issue_split_from: DF.Link | None
		issue_type: DF.Link | None
		lead: DF.Link | None
		naming_series: DF.Literal["ISS-.YYYY.-"]
		on_hold_since: DF.Datetime | None
		opening_date: DF.Date | None
		opening_time: DF.Time | None
		phone_number: DF.Data | None
		priority: DF.Literal["None", "\u9ad8", "\u4e2d", "\u4f4e", "\u5b8c\u4e86", "\u672a\u78ba\u5b9a"]
		product_name: DF.Literal["None", "\u901a\u8ca9Ace", "\u901a\u8ca9\u30d7\u30ed"]
		project: DF.Link | None
		question_level: DF.Literal["None", "\u672a\u5206\u985e", "\u6613 - \u55b6\u696d\u3042\u3066 \u5c0e\u5165\u524d\u306a\u3069\u306e\u8cea\u554f", "\u666e - CS\u3042\u3066 AI\u5b66\u7fd2\u3055\u305b\u308b\u8cea\u554f", "\u96e3 - CS\u3042\u3066 AI\u5b66\u7fd2\u3055\u305b\u306a\u3044\u8cea\u554f", "\u7279 - \u30ab\u30b9\u30bf\u30de\u30a4\u30ba"]
		raised_by: DF.Data | None
		resolution_details: DF.TextEditor | None
		resolution_time: DF.Duration | None
		response_by: DF.Datetime | None
		service_level_agreement: DF.Link | None
		service_level_agreement_creation: DF.Datetime | None
		sla_resolution_by: DF.Datetime | None
		sla_resolution_date: DF.Datetime | None
		stakeholder: DF.Data | None
		status: DF.Literal["None", "\u5bfe\u5fdc\u4e2d - CS\u5bfe\u5fdc\u4e2d", "\u5bfe\u5fdc\u4e2d - PG\u5bfe\u5fdc\u4e2d", "\u5bfe\u5fdc\u4e2d - \u304a\u5ba2\u69d8\u78ba\u8a8d\u5f85\u3061", "\u672a\u5bfe\u5fdc", "\u4fdd\u7559", "\u6a5f\u80fd\u8981\u671b", "\u5b8c\u4e86"]
		subject: DF.Data
		total_hold_time: DF.Duration | None
		user_resolution_time: DF.Duration | None
		via_customer_portal: DF.Check
	# end: auto-generated types

	pass
