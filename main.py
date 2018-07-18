from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/", methods = ['GET', 'POST'])
def index():   
#    encoded_error = request.args.get("error")
    username_error = request.args.get("username_error")
    password_error = request.args.get("password_error")
    password_verification_error = request.args.get("password-verification_error")
    return render_template('userinfo.html', 
#        error=encoded_error and cgi.escape(encoded_error, quote=True), 
        username_error=username_error and cgi.escape(username_error, quote=True),
        password_error=password_error and cgi.escape(password_error, quote=True),
        password_verification_error=password_verification_error and cgi.escape(password_verification_error, quote=True)
        )

@app.route('/userinfo', methods = ['GET', 'POST'])
def verification():
    username = request.form['username']
    password = request.form['password']
    password_verification = request.form['password-verification']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_verification_error = ''
    email_error = ''  

# Username testing
    if username == '':
        username_error = "Please enter a username greater than 3 and less than 20 characters without spaces."
    if ' ' in username:
        username_error = "Please enter a username greater than 3 and less than 20 characters without spaces."
    if len(username) < 3 or len(username) >20:
        username_error = "Please enter a username greater than 3 and less than 20 characters without spaces."

# Password testing
    if password == '':
        password_error = "Your password sucks"
    if ' ' in password:
        password_error = "Your password sucks"
    if len(password) <3 or len(password) >20:
        password_error = "Your password sucks"
    if password != password_verification:
        password_verification_error = "It doesn't match!"
    
# Email Testing
    email_substring = email.split('@')

    if email == '':
        email_error = 'Please enter a valid email'
    if len(email)<3 or len(email)>20:
        email_error = 'Please enter a valid email'
    if '@' not in email:
        email_error = 'Please enter a valid email'
    elif '.' not in email_substring[1]:
        email_error = 'Please enter a valid email'


    if username_error or password_error or password_verification_error or email_error:
        return render_template('/userinfo.html', 
            email_error = email_error,
            username_error = username_error,
            password_error = password_error,
            password_verification_error = password_verification_error,
            )


    return render_template('/confirmation.html', username = username)


@app.route('/userinfo', methods = ['POST'])
def confirm_user():
    username = request.form['username']
    return render_template("/confirmation.html", username = username)




app.run()