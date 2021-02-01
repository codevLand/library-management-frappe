async function borrowArticle(name, user) {
    console.log(name, user);
    if (user === "Guest") {
        alert("You are not logged in.")
    } else {
        // request(data)
        checkMembership({name, user})
    }
}

function checkMembership(data) {
    alert(data.user, data.name)
    console.log(data);
    // checkUserRole(data.user)
}

function checkUserRole(user) {
    let getData = {
        method: 'frappe.client.get_value',
        args: {
            doctype: 'User',
            filters: {
                email: user,
            },
            fields: ["status", "first_name", "last_name", "role_permission_name"]
        },
        callback: function(r) {
            console.log(r);
            document.getElementById(`span${name}`).className = "badge badge-primary";
            document.getElementById(`span${name}`).innerText = "Issued";
            document.getElementById(name).hidden = true;
        },
        error: function(r) {
            console.log("update error", r);
            // put alert???
        },
    }
}

function request(name, user) {
    let updateData = {
        method: 'frappe.client.set_value',
        args: {
            doctype: 'Article',
            "name": name,
            "fieldname": "status",
            "value": "Issued"
        },
        callback: function(r) {
            console.log(r);
            document.getElementById(`span${name}`).className = "badge badge-primary";
            document.getElementById(`span${name}`).innerText = "Issued";
            document.getElementById(name).hidden = true;
            
        },
        error: function(r) {
            console.log("update error", r);
            // put alert???
        },
    }

    let getData = {
        method: 'frappe.client.get_value',
        args: {
            doctype: 'Article',
            filters: {
                name,
            },
            fieldname: "status"
        },
        callback: function(r) {
            console.log(r);
            if (r.message && r.message.status == "Available") {
                frappeCall(updateData)
            } else {
                document.getElementById(`span${name}`).className = "badge badge-primary";
                document.getElementById(`span${name}`).innerText = "Issued";
                document.getElementById(name).hidden = true;
                alert("Sorry!\nArticle is no longer available.")
            }
        },
        error: function(r) {
            console.log("get error", r);
            // put alert???
        },
    }
    frappeCall(getData)
}

function frappeCall(data) {
    frappe.call({
        method: data.method,
        args: data.args,
        callback: data.callback,
        error: data.error
    });
}