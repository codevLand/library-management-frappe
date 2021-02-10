import frappe

#  TODO sanitize req input

def put_update( doctype,args,kwargs ):

	if not this_exists (doctype,args,kwargs) :
		return "does not exist"
	
	else :

		tbl_id = kwargs.get('name')
		kwargs.pop('cmd', None)
		kwargs.pop('name', None)

		updated = frappe.db.update (
			doctype, 
			tbl_id,
			kwargs )

		frappe.db.commit()
		return kwargs

def this_exists (doctype,args,kwargs) :
	return frappe.db.exists (
		doctype,
		kwargs.get('name'))