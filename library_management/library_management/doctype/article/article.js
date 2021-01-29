// Copyright (c) 2021, Jomar Furiscal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article', {
    onload:function(frm) {
        print("asdasdasdsadsadsadsadsadsd asdasdad")
    }
    // borrowArticle(name) {
    //     print("klasjhdakshdl khklahdklsahdklashdkajshdjk")
    //     frappe.call({
    //         method: 'frappe.client.set_value',
    //         args: {
    //             doctype: 'Article',
    //             "name": name,
    //             "fieldname": "status",
    //             "value": "Issued"
    //         },
    //         callback: function(r) {
    //             console.log(r);
    //             document.getElementById(name).className = "btn btn-primary disabled";
    //         }
    //     });
    // },
    // event2() {
    //     // handle event 2
    // }
});



// update doctype = name,
// doctype.status = issued
