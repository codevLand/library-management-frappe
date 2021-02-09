import frappe

def validate_required(kwargs, fields):
    for rfield in fields:
        if rfield not in kwargs:
            return "Missing required field {}".format(rfield)


@frappe.whitelist(allow_guest=True)
def add_images(*args, **kwargs):

    if frappe.request.method not in ["POST", "PUT"]:
        return response(False, {}, "Invalid request method.", "Request method must be POST or PUT.", "")
    
    # call inside a function
    if len(args) > 0:
        print("uploading image")
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
    
    file_docs = []
    if len(files) > 0:
        for file in files.get(args.get("image_identifier")):           
            try:
                # create file and save to folder
                new_file = make_file(args, file.filename, file.stream.read())
                new_file.save(ignore_permissions=1)

                file_docs.append(new_file)

                # add file url to doctype
                frappe.db.set_value(args.get("doctype"), args.get("docname"), args.get("image_identifier"), new_file.file_url)

            except Exception as e:
                raise e

    return file_docs



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

def log_event():
    # frappe.utils.logger.set_log_level("DEBUG")
    # logger = frappe.logger("api", allow_site=True, file_count=50)
    # user = frappe.session.user
    # logger.info(f"{user} accessed counter_app.update with value={value}")

    # current_value = frappe.get_single_value("Value", "counter")
    # updated_value = current_value + value
    # logger.debug(f"{current_value} + {value} = {updated_value}")
    # frappe.db.set_value("Value", "Value", "counter", updated_value)
    # logger.info(f"{user} updated value to {value}")

    frappe.logger(frappe.request.headers.get("User-agent")).debug({
        "site": "frappeframework.com",
        "remote_addr": "192.148.1.7",
        "base_url": "https://frappeframework.com/docs/user/en/api/logging",
        "full_path": "/docs/user/en/api/logging",
        "method": "POST",
        "scheme": "https",
        "http_status_code": 200
    })


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