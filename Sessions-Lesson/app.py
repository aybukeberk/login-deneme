from flask import Flask, render_template, request, redirect, session, url_for, flash
import model

app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"

model.connect_to_db()

@app.route("/")
def index():
    if session.get("username"):
        return "User %s is logged in!" %session["username"]
    else:
        return render_template("index.html")

@app.route("/", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")

    legit_username = model.authenticate(username, password)
    print legit_username
    if legit_username != None:
        flash("User authenticated!")
        session["username"] = legit_username
    else:
        flash("Password incorrect. There may be a ferret stampede in progress!")

    return redirect(url_for("view_user", username = legit_username))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/user/<username>")
# orange 'username' is from 'legit_username' rtn from process_login
def view_user(username):
    user_id = model.get_user_by_name(username)
    wall_posts = model.get_wall_posts_by_user_id(user_id)
    return render_template("wall.html", 
                            # orange 'wallpost' gets fed to HTML 
                            wallpost = wall_posts)

# @app.route("/user/<username>", methods=["POST"])
# def post_to_wall(person_whos_wall_it_is):
#     wall_owner_user_id = model.get_user_by_name(person_whos_wall_it_is)
#     author_id_logged_in = me(logged_in)
    

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug = True)
