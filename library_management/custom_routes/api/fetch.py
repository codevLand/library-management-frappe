# API USAGE:
# see test/api/article.get.http

#  TODO sanitize req input

import frappe

def get_list (doctype,args,kwargs) :

    return frappe.db.get_list (
        doctype,
        filters     = filtered(args,kwargs),
		fields      = kwargs.get('fields'),
		order_by    = kwargs.get('order_by'),
		start       = kwargs.get('start'),
		page_length = kwargs.get('pg_len'),
		as_list     = False
    )

def filtered (args,kwargs) :
    return kwargs.get('filter') or None