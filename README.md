## Library Management

Library Management System

#### Installation Guide

1. Install frappe and its prerequisites [here]('https://frappeframework.com/docs/user/en/installation')
2. Clone this repo using: `bench get-app https://github.com/codevLand/library-management-frappe.git`
3. Install site: `bench new-site library.test`
4. Run library management: `bench start`
> (Optional) install ERPNext if you needed to add more functionality to your setup
5. Go to `localhost:8000` (port 8000 is used by default, use the port you setup if 8000 is not used)
6. Web setup:
    6.1. Login using:
      > `Email Address:` Administrator
      > `Password`: [the password you used to setup mysql/frappe]
    6.2 Follow frappe setup on browser
7. Link library app to library.test site: `bench --site library.test install-app library_management`
8. Run `nano /etc/hosts/` and add `127.0.0.0 1  library.test` at the end
9. Browse `library.test:8000` 

#### License

MIT
