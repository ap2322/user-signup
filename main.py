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
    username_error = "Please enter a username greater than 3 and less than 20 characters without spaces."

    password = request.form['password']
    password_error = "Your password sucks"

    password_verification = request.form['password-verification']
    password_verification_error = "It doesn't match!"

    email = request.form['email']
    email_error = 'Please enter a valid email'

# Username testing
    if username == '':
        return render_template('/userinfo.html', username_error = username_error)
    if ' ' in username:
        return render_template('/userinfo.html', username_error = username_error)
    if len(username) < 3 or len(username) >20:
        return render_template('/userinfo.html', username_error = username_error)

# Password testing
    if password == '':
        return render_template('/userinfo.html', password_error = password_error)
    if ' ' in password:
        return render_template('/userinfo.html', password_error = password_error)
    if len(password) <3 or len(password) >20:
        return render_template('/userinfo.html', password_error = password_error)
    if password != password_verification:
        return render_template('/userinfo.html', password_verification_error = password_verification_error)

# Email Testing
    email_substring1, email_substring2 = email.split('@')

    if email == '':
        return render_template('/userinfo.html', email_error = email_error)
    if len(email)<3 or len(email)>20:
        return render_template('/userinfo.html', email_error = email_error)
    if '@' not in email:
        return render_template('/userinfo.html', email_error = email_error)
    if '.' not in email_substring2:
        return render_template('/userinfo.html', email_error = email_error)


    return render_template('/confirmation.html', username = username, username_error = '', password_error = '')

# TODO: make a verification function for each field: username, password, verify password
# email

# TODO: Each verification function shcould check for blanks, contains a space, is <3 or >20
#   characters

# TODO: password and verify password must match

# TODO: email cannot be empty; has a single @; has a single '.' after the @; 


@app.route('/userinfo', methods = ['POST'])
def confirm_user():
    username = request.form['username']
    return render_template("/confirmation.html", username = username)




app.run()