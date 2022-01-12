import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
if os.path.exists("env.py"):
    import env

# Credit for app initialization to Code Institute Mini Project Lessons
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_items")
def get_items():
    items = mongo.db.items.find()
    return render_template("items.html", items=items)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        user_exists = mongo.db.users.find_one({'username': form.username.data})
        email_exists = mongo.db.users.find_one({'email': form.email.data})
        if user_exists:
            flash('Username already taken', 'light-green accent-4')
            return redirect(url_for('register'))
        elif email_exists:
            flash('Email already in use!', 'light-green accent-4')
        elif form.validate_on_submit():
            register = {
                "username": form.username.data,
                "password": generate_password_hash(form.password.data),
                "email": form.email.data,
            }
            mongo.db.users.insert_one(register)
            flash(f'Account created {form.username.data}. Welcome aboard!', 'light-green accent-4')
            return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':       
            flash(f'Welcome {form.username.data}. This is your Top Shelf',  'light-green accent-4')
            return redirect(url_for('get_items'))
        else:
            flash(f'Login Unsuccessful', 'red accent-4')
    # if request.method == "POST":
    #     user_exists = mongo.db.users.find_one(
    #         {"username": request.form.get("username").lower()})

    #     if user_exists:
    #         if check_password_hash(
    #             user_exists["password"], request.form.get("password")):
    #             session["user"] = request.form.get("username").lower()
    #         else:
    #             return redirect(url_for("login"))

    #     else:
    #         return redirect(url_for("get_items"))
    return render_template("login.html", title='Login', form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
