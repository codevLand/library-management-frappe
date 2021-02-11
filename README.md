## Library Management

Library Management System with custom routes and custom handlers extended from frappe's library management tutorial

#### Installation Guide

1. Install frappe and its prerequisites [here]('https://frappeframework.com/docs/user/en/installation')
> *Optional*: install ERPNext if you needed to add more functionality to your setup
2. Open terminal and go inside frappe-bench folder
3. Clone this repo: 
```sh
bench get-app https://github.com/codevLand/library-management-frappe.git
```
4. Install site: 
```sh
bench new-site library.test
```
5. Edit `/etc/hosts/` and add this line ath the end: 
```
127.0.0.1 library.test
```
5. Link library app to library.test site: 
```sh
bench --site library.test install-app library_management
```
6. Run library management: 
```sh
bench start
```
7. Go to `localhost:8000` and start the frappe new website setup wizard
> **NOTE:** *port 8000 is used by default, use the port you setup if 8000 is not used*
8. Login to view admin/librarian portal
    > `Email Address:` Administrator
    > `Password`: [the password you used to setup mysql/frappe]
9. Browse to `library.test:8000` to view the library website


### API Testing

Use API testing tool (e.g. postman, cUrl)
> You can optionally install `REST Client` on VSCode

# Authentication:

- Using session ID:
Simply generate session ID by sending a `POST` request 

```json
POST http://localhost:8000/api/method/login HTTP/1.1
Content-Type: application/json
{
   "usr":"Administrator",
   "pwd":"0000"
}
```

- Using token:
   1. Login to admin portal
   2. Go to `User and Permissions`
   3. Click `User`
   4. Create a new user (librarian) and fill out the form
   > :warning:*IMPORTANT*: once you saved the new user a prompt will popup with the user's secret key, once the prompt is closed, the secret will not be recoverable. It is recommended that you copy the secret key to a safe staorage.:warning:
   5. Click Settings on the top nav and click reload
   6. Follow steps 2 & 3
   7. Select the newly created user
   8. Browse down to roles and check `librarian` role
   9. Browse down to API Access and copy the `API key`

# Handling GET Requests
*See tests/api/article.get.http*

# Handling POST Requests
*See tests/api/article.post.http*

# Handling PUT Requests
*See tests/api/article.put.http*

# Handling DELETE Requests
*See tests/api/article.delete.http*


#### License

MIT
