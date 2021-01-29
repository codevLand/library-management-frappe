## Library Management

Library Management System

#### Installation Guide

1. Install frappe and its prerequisites [here]('https://frappeframework.com/docs/user/en/installation')
2. Clone this repo using: `bench get-app https://github.com/codevLand/library-management-frappe.git`
3. Install site: `bench --site library.test --force reinstall`
4. Link library app to library.test site: `bench --site library.test install-app library_management`
5. Run library management: `bench start`

#### License

MIT
