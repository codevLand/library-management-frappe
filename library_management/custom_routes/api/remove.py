import frappe

def remove_this (doctype,args,kwargs) :

	kwargs.pop('cmd', None)

	removed = frappe.db.delete (
		doctype,
		kwargs
	)
	return frappe.db.commit()