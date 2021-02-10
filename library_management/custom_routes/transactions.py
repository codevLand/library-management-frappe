# from __future__ import unicode_literals
import frappe
# from frappe.website.website_generator import WebsiteGenerator


@frappe.whitelist()
def get_all_book_issued_to_member():
    return frappe.db.sql(
        "SELECT * from `tabLibrary Transaction`",
        as_dict=True)