# -*- coding: utf-8 -*-
# Copyright (c) 2021, Jomar Furiscal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class Article(WebsiteGenerator):
	@frappe.whitelist()
	def issued_article_status(self):
		# set article status to issued
		update = frappe.db.set_value('Article', self.name, 'status', 'Issued')

		return update

