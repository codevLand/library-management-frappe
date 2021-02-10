import frappe

#  TODO sanitize req input

def post_new (doctype,args,kwargs) :

	kwargs.pop('cmd', None)

	if this_exists (doctype,args,kwargs) :
		return "already exists"
	
	else :
		doc = frappe.new_doc(doctype)
		doc.update(kwargs)
		
		doc.insert()
		frappe.db.commit()
		return doc

def this_exists (doctype,args,kwargs) :
	return frappe.db.exists (
		doctype,
		kwargs.get('name'))