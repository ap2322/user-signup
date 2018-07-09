from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route('/confirmation', methods = ['GET', 'POST'])
def username_verification():
    username = request.form['username']
    if username == '':
        error = "Please enter a username that is greater than 3 and less than 20 characters and does not contain spaces."
        return render_template('/userinfo.html', error = error)
    # if '\s' in username:
    #     return error
    if len(username) < 3 or len(username) >20:
        error = "Please enter a username that is greater than 3 and less than 20 characters and does not contain spaces."
        return render_template('/userinfo?error', error = error)
    
    return render_template('/confirmation.html', username = username)



@app.route("/", methods = ['GET', 'POST'])
def index():   
    encoded_error = request.args.get("error")
    return render_template('userinfo.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

# TODO: make a verification function for each field: username, password, verify password
# email
# TODO: Each verification function shcould check for blanks, contains a space, is <3 or >20
#   characters
# TODO: password and verify password must match
# TODO: email cannot be empty; has a single @; has a single '.' after the @; 

def password_verification():
    password = request.args.get("password")

    if password is '':
        error = "Please enter a password that is greater than 3 and less than 20 characters and does not contain spaces."
        return redirect("/?error=", error= error)
    if " " in password:
        error = "Please enter a password that is greater than 3 and less than 20 characters and does not contain spaces."
        return redirect("/?error=" + error)
    if len(password) < 3 or len(password) >20:
        error = "Please enter a password that is greater than 3 and less than 20 characters and does not contain spaces."
        return redirect("/?error=" + error)
    else:
        return render_template('/confirmation.html')

@app.route('/confirmation', methods = ['POST'])
def confirm_user():
    username = request.form['username']
    return render_template("/confirmation.html", username = username)


@app.route("/add", methods=['POST'])
def add_user():
    # look inside the request to figure out what the user typed
    new_movie = request.form['new-movie']

    # if the user typed nothing at all, redirect and tell them the error
    if (not new_movie) or (new_movie.strip() == ""):
        error = "Please specify the movie you want to add."
        return redirect("/?error=" + error)

    # if the user wants to add a terrible movie, redirect and tell them the error
    if new_movie in terrible_movies:
        error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie)
        return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    # using templates with jinja2 automatically escapes user input
    # new_movie_escaped = cgi.escape(new_movie, quote=True)

    # Create a template called add-confirmation.html inside your /templates directory
    # Use that template to render the confirmation message instead of this temporary message below

    return render_template(
        'add-confirmation.html', 
        new_movie = new_movie,   
    )

app.run()