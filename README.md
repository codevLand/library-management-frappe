## Library Management

Library Management System

#### Installation Guide

1. Install frappe and its prerequisites [here]('https://frappeframework.com/docs/user/en/installation')
2. Clone this repo using: `bench get-app https://github.com/codevLand/library-management-frappe.git`
3. Install site: `bench new-site library.test`
4. Link library app to library.test site: `bench --site library.test install-app library_management`
  ** (Optional) install ERPNext if you needed to add more functionality to your setup **
5. Run `nano /etc/hosts/` and add `127.0.0.0 1  library.test` at the end
6. Run library management: `bench start`
7. Go to `library.test:8000` and login using:
    `Email Address:` Administrator
    `Password`: [the password you used to setup mysql/frappe]

#### License

MIT
