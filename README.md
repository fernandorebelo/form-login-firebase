# Login page with authentication using firebase

## Login with an existing account

In the login form page there are two inputs to email and password.

When the submit button is pressed the backend verifies if the account already exists. If not exist, shows an error message and tell to create a new one.

If the account exists and the login is successfull you are sent to a sucess page.

![image](https://github.com/fernandorebelo/form-login-firebase/assets/94297628/57cf7cb6-5267-47db-82f8-e0ec5fa468ed)

![image](https://github.com/fernandorebelo/form-login-firebase/assets/94297628/19e44643-f33a-4f6f-b4a5-c9f97d9cd784)

## Register a new account

Using the register button you are directed to a new page to create a new account with email and password.

When the "Create account" button is pressed the backend verifies if the email is already registered. If not, it create a new account.

If the email already exists, shows an error message telling the email is already used.

![image](https://github.com/fernandorebelo/form-login-firebase/assets/94297628/d35171f1-4c82-483d-acc1-f470151cb00e)

## Password recovery key

If you forgot the password we can send a link to your email to create a new password.

![image](https://github.com/fernandorebelo/form-login-firebase/assets/94297628/eaabab00-a711-4539-b015-3433265e4e46)

## Firebase admin

To authenticate the login and create new account we are using firebase admin SDK.

## Installation

Clone the project in your machine:

```bash
  $ git clone https://github.com/fernandorebelo/form-login-firebase.git
  $ cd form-login-firebase
```

Create a new virtual environment:

```bash
  $ py -3 -m venv .venv
  $ .venv\Scripts\activate
```

Install the requirements

```bash
  $ pip install -r requirements.txt
```

Run the project:

```bash
  $ flask run --debug
```

Use your browser to access the swagger documentation:

```bash
  http:localhost/
```
