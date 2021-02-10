import frappe

from library_management.custom_routes.api import fetch as read
from library_management.custom_routes.api import create as create
from library_management.custom_routes.api import modify as update
from library_management.custom_routes.api import remove as delete

# API USAGE:
# if 403 send request from login.http
# see test/api/{doctype.method.http}

# TODO create a custom excemption handler

@frappe.whitelist()
def article (*args,**kwargs) :
	
	try:
		req = frappe.request.method
		
		if req == "POST":
			return create.post_new ('Article', args, kwargs)

		elif req == "GET":
			return read.get_list ('Article', args, kwargs)

		elif req == "PUT":
			return update.put_update ('Article', args, kwargs)
		
		elif req == "DELETE":
			return delete.remove_this ('Article', args, kwargs)
		
		else: 
			return { req }

	except Exception as e:
		return { 
			'success': False,
			'message': 'article: ' +
			str(e) 
		}