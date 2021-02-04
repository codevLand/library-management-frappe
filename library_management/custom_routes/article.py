from __future__ import unicode_literals
import frappe
import json

def validate_required(kwargs, fields):
    for rfield in fields:
        if rfield not in kwargs:
            return "Missing required field {}".format(rfield)

@frappe.whitelist(allow_guest=True)
def add_article(*args, **kwargs):

    try:
        doctype = "Article"
        if frappe.request.method not in ["POST", "PUT"]:
            return response(False, {}, "Invalid request method.", "Request method must be POST or PUT.", "")

        required = validate_required(kwargs, ["article_name"])
        if required:
            return response(False, {}, "Invalid request method.", required, "")

        article = frappe.db.exists({ "doctype": doctype, "article_name": kwargs.get("article_name") })

        # if article:
        #     return { "success": False, "message": "Article already exists" }

        # uploaded = frappe.handler.upload_file()
        add_images(kwargs)
        
        # return { "data": article[0][0], "filenames": filenames, "file": files }
        
        
        # doc = frappe.new_doc(doctype)
        # doc.article_name = kwargs.get("article_name")
        # doc.author = kwargs.get("author")
        # doc.status = kwargs.get("status")
        # doc.isbn = kwargs.get("isbn")
        # doc.publisher = kwargs.get("publisher")
        # doc.published = kwargs.get("published")
        # doc.route = kwargs.get("route")
        # doc.description = kwargs.get("description")
        # article = doc.insert()

        return response(True, article, "", "Created successfully.", "")

    except Exception as e:
        return response(False, {}, e, "Something went wrong", "")

@frappe.whitelist(allow_guest=True)
def add_images(*args, **kwargs):

    if frappe.request.method not in ["POST", "PUT"]:
        return response(False, {}, "Invalid request method.", "Request method must be POST or PUT.", "")
    
    # call inside a function
    if len(args) > 0:
        images = save_images(args[0])
        return images
    
    # call from rest api
    if len(kwargs) > 0:
        try:
            images = save_images(kwargs)
            return response(True, images, "", "Upload successful", "")
            
        except Exception as e:
            return response(False, {}, e, "Something went wrong", "")

def save_images(args):

    files = frappe.local.request.files
    files = files.to_dict(flat=False)
    
    try:
        file_docs = []
        for file in files.get(args.get("image_identifier")):        
            
            # create file and save to folder
            new_file = make_file(args, file.filename, file.stream.read())
            new_file.save(ignore_permissions=1)

            file_docs.append(new_file)
            
            # add file url to doctype
            frappe.db.set_value(args.get("doctype"), args.get("docname"), args.get("image_identifier"), new_file.file_url)

        return file_docs

    except Exception as e:
        raise e

def make_file(args, filename, content):

    folder = args.get("folder") or "Home"
    return frappe.get_doc({
        "doctype": "File",
        "attached_to_doctype": args.get("doctype"),
        "attached_to_name": args.get("docname"),
        "folder": folder,
        "file_name": filename,
        "is_private": 0,
        "content": content
    })

def response(success, data, error, message, code):
    frappe.local.response.success = success
    frappe.local.response.message = message
    if success:
        frappe.local.response.data = data
    else:
        if code:
            frappe.local.response['http_status_code'] = code

        err = error.message if hasattr(error, 'message') else str(error)
        if err:
            frappe.local.response.error = err


# @frappe.whitelist(allow_guest=True)
# def upload_image(*args, **kwargs):

    # form = frappe.local.request.form.to_dict()
    # files = frappe.local.request.filesdef extract_files(files):
    # valid_files = ["profile_pic", "valid_id"]    filemap = {}
    # for k, v in files.items():
    #     if k not in valid_files: continue
    #     filemap[k] = v
    # return filemap

    # return {
    #     "user": frappe.session.user,
    #     "req": frappe.request,
    #     "headers": frappe.request.headers,
    #     "url": frappe.request.url,
    #     # "uri": frappe.request.uri,
    #     # "params": frappe.request.params,
    #     # "query": frappe.request.query,
    #     "method": frappe.request.method,
    #     # "data": frappe.request.data,
    #     "args": args,
    #     "kwargs": kwargs
    # }
    # return json.loads(frappe.request.data)

    # frappe.log_error(
    #     "Failed to validate checkout code.\n{}\n{}\n{}".format(
    #         str(e),
    #         frappe.get_traceback(),
    #         kwargs), 
    #     "WooERPNext Error - Validate Checkout code")