from __future__ import unicode_literals
import frappe
import json
from library_management.custom_routes import global_functions as gf

@frappe.whitelist(allow_guest=True)
def article(*args, **kwargs):

    try:
        doctype = "Article"
        if frappe.request.method not in ["POST"]:
            return gf.response(False, {}, "Request failed.", "Request method must be POST.", "")

        validation_error = gf.validate_required(kwargs, ["article_name"])
        if validation_error:
            return gf.response(False, {}, "Failed to create article", validation_error, "")

        article = frappe.db.exists({ "doctype": doctype, "article_name": kwargs.get("article_name") })
        if article:
            return gf.response(False, {}, "Failed to create article", "Article already exists", "")

        print({
            "method": frappe.request.method,
            "url": frappe.request.url,
            "payload": kwargs
        })

        images = gf.add_images(kwargs)

        print("creating document...")
        article = frappe.new_doc(doctype)

        if kwargs.get("article_name"):
            article.article_name = kwargs.get("article_name")

        if kwargs.get("author"):
            article.author = kwargs.get("author")

        if kwargs.get("status"):
            article.status = kwargs.get("status")

        if kwargs.get("isbn"):
            article.isbn = kwargs.get("isbn")

        if kwargs.get("publisher"):
            article.publisher = kwargs.get("publisher")

        if kwargs.get("published"):
            article.published = kwargs.get("published")

        if kwargs.get("route"):
            article.route = kwargs.get("route")

        if kwargs.get("description"):
            article.description = kwargs.get("description")

        article.image = images[0].file_url if len(images) > 0 else None

        article.insert()

        # article.submit()
        return gf.response(True, article, "", "Created successfully.", "")

    except Exception as e:
        return gf.response(False, {}, e, "Something went wrong", 500)


@frappe.whitelist(allow_guest=True)
def update_article(*args, **kwargs):

    try:
        doctype = "Article"
        if frappe.request.method not in ["PUT"]:
            return gf.response(False, {}, "Request failed.", "Request method must be PUT.", "")

        validation_error = gf.validate_required(kwargs, ["docname"])
        if validation_error:
            return gf.response(False, {}, "Failed to update article", validation_error, "")

        article = frappe.db.exists({ "doctype": doctype, "name": kwargs.get("docname") })
        if not article:
            return gf.response(False, {}, "Failed to update article", "Article does not exist.", "")

        images = gf.add_images(kwargs)

        print("fetching document...")        
        article = frappe.get_doc(doctype, kwargs.get("docname"))

        if kwargs.get("article_name"):
            article.article_name = kwargs.get("article_name")

        if kwargs.get("author"):
            article.author = kwargs.get("author")

        if kwargs.get("status"):
            article.status = kwargs.get("status")

        if kwargs.get("isbn"):
            article.isbn = kwargs.get("isbn")

        if kwargs.get("publisher"):
            article.publisher = kwargs.get("publisher")

        if kwargs.get("published"):
            article.published = kwargs.get("published")

        if kwargs.get("route"):
            article.route = kwargs.get("route")

        if kwargs.get("description"):
            article.description = kwargs.get("description")

        article.image = images[0].file_url if len(images) > 0 else None

        print("updating document...")
        article.save()
        
        # article.submit()
        return gf.response(True, article, "", "Updated successfully.", "")

    except Exception as e:
        return gf.response(False, {}, e, "Something went wrong", 500)



@frappe.whitelist(allow_guest=True)
def get_one(*args, **kwargs):

    try:
        required_fields = ["docname"]
        validation_error = gf.validate_required(kwargs, required_fields)
        if validation_error:
            return gf.response(False, {}, "Failed to get article", validation_error, "")

        kwargs["filters"] = { "name": kwargs.get("docname") }

        article = get_all(kwargs)
        if len(article) > 0:
            return gf.response(True, article[0], "", "", "")
        else:
            return gf.response(False, {}, "Article does not exist.", "Article not found.", 404)

    except Exception as e:
        return gf.response(False, {}, e, "Something went wrong", 500)


@frappe.whitelist(allow_guest=True)
def get_all(*args, **kwargs):
    try:
        doctype = "Article"
        if frappe.request.method != "GET":
            return gf.response(False, {}, "Request failed.", "Request method must be GET", "")
    
        if len(args) > 0:
            data = args[0]

        if len(kwargs) > 0:
            data = kwargs

        # required_data = ["article_name", "author", "status", "isbn", "publisher", "published", "route", "image", "description", "name", "creation", "modified", "modified_by", "publish_date"]
        # validation_error =  gf.validate_required(json.loads(kwargs.get("fields")), required_data)

        fields = data.get("fields")
        filters = data.get("filters")
        limit = data.get("limit")
        page = data.get("page")
        order_by = "{} {}".format("creation", "desc")

        if page:
            if int(page) > 0:
                page = (int(page)-1) * int(limit) if limit else None
            else:
                raise Exception("Page must be greater than zero.")

        if data.get("sort"):
            order_by = "{} {}".format(data.get("sort"), data.get("order") if data.get("order") else "desc")

        if data.get("docname"):
            print("get one")
            article = frappe.db.get_list(
                doctype, 
                filters=filters, 
                fields=fields,
            )
        else:
            print("get all")
            article = frappe.db.get_list(
                doctype, 
                filters= filters if filters else None, 
                fields= fields if fields else None,
                order_by= order_by,
                start=page if page else None,
                page_length= limit if limit else None,
            )

        if len(args) > 0:
            return article
        else:
            return gf.response(True, article, "", "", "")

    except Exception as e:
        if len(args) > 0:
            raise Exception(e)
        else:
            return gf.response(False, {}, e, "Something went wrong", 500)

@frappe.whitelist(allow_guest=True)
def delete_article(*args, **kwargs):
    
    required_fields = ["docname"]
    validation_error = gf.validate_required(kwargs, required_fields)
    if validation_error:
        return gf.response(False, {}, "Failed to delete article", validation_error, "")

    try:
        # frappe.delete_doc or frappe.db.delete
        # doc = frappe.get_doc("Article", kwargs.get("docname"))
        if frappe.db.delete("Article", {"name":kwargs.get("docname")}):
            return gf.response(True, article, "", "", "")
        else:
            # return frappe.get_traceback()
            return gf.response(False, {}, "Unable to delete article {}".format(kwargs.get("docname")), "Something went wrong", 500)
    except Exception as e:
        return gf.response(False, {}, e, "Something went wrong", 500)

def call_a(args, kwargs):
    return { "m": "from call_a", 'args': args, 'kwargs': kwargs }