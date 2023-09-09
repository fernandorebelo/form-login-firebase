import pyrebase
#import firebase_admin
#from firebase_admin import credentials, auth
from flask import Flask, request, render_template, redirect, url_for, session
from config.settings import *

config = {
  "apiKey": APIKEY,
  "authDomain": AUTHDOMAIN,
  "databaseURL": DATABASEURL,
  "storageBucket": STORAGEBUCKET,
  "serviceAccount": SERVICEACCOUNT
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

#cred = credentials.Certificate("firebase-sdk.json")
#firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if request.form.get('login'):
            login_failed = 'Login failed. Check your credentials.'
            login_success = 'Welcome!'
            try:
                user = auth.sign_in_with_email_and_password(email=email, password=password)
                print(user)
                return render_template('success.html', message=login_success)
            except:
                return render_template('login-form.html', message=login_failed)
    return render_template('login-form.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if request.form.get('create_account'):
            login_success = 'Welcome!'
            login_failed = 'Account already exists. Try again.'
            try:
                user = auth.create_user_with_email_and_password(email=email, password=password)
                print(user)
                return render_template('success.html', message=login_success)
            except:
                return render_template('register-form.html', message=login_failed)
    return render_template('register-form.html')

@app.route('/forgot-password', methods=['POST', 'GET'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        if request.form.get('forgot_password'):
            email_valid = 'An email has been sent to your email. Verify your check mail box.'
            email_invalid = 'Email does not exist. Try again.'
            try:
                user = auth.send_password_reset_email(email=email)
                return render_template('forgot-password-form.html', message=email_valid)
            except:
                return render_template('forgot-password-form.html', message=email_invalid)
    return render_template('forgot-password-form.html')

if __name__ == '__main__':
    app.run(debug=True)