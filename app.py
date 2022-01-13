import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, AddStock
if os.path.exists("env.py"):
    import env

# Credit for app initialization to Code Institute Mini Project Lessons
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_items')
def get_items():
    items = mongo.db.items.find()
    return render_template("items.html", items=items)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        user_exists = mongo.db.users.find_one({'username': form.username.data.lower()})
        email_exists = mongo.db.users.find_one({'email': form.email.data})
        if user_exists:
            flash('Username already taken', 'light-green accent-4')
            return redirect(url_for('register'))
        elif email_exists:
            flash('Email already in use!', 'light-green accent-4')
        elif form.validate_on_submit():
            register = {
                'username': form.username.data,
                'password': generate_password_hash(form.password.data),
                'email': form.email.data,
            }
            mongo.db.users.insert_one(register)
            session['user'] = form.username.data.lower()
            flash(f'Account created {form.username.data}. Welcome aboard!', 'light-green accent-4')
            return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user_exists = mongo.db.users.find_one({"username": form.username.data.lower()})
        if user_exists and check_password_hash(user_exists['password'], form.password.data):
            session['user'] = form.username.data.lower()
            flash(f'Welcome {form.username.data}. This is your Profile Page',  'light-green accent-4')
            return redirect(url_for('profile', username=session['user']))
        else:
            flash(f'Login Unsuccessful', 'red accent-4')
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    form = AddStock()
    if request.method == "POST":
        share = "True" if request.form.get("share") else "False"
    if form.validate_on_submit():
        stock = {
            'item_name' : form.name.data,
            'region_name' : form.region.data,
            'age' : form.age.data,
            'distillery' : form.distillery.data,
            'notes' : form.notes.data,
            'image' : form.image.data,
            'share' : share,
            'owned_by': session['user'].lower()
        }
        mongo.db.items.insert_one(stock)
        flash(f'New item was added to your shelf', 'light-green accent-4')
        return redirect(url_for('get_items'))
    return render_template('add_stock.html', title='Add Stock', form=form)


@app.route('/my_shelf', methods=['GET', 'POST'])
def my_shelf():
    user = session['user']
    my_shelf = list(mongo.db.items.find({'owned_by': user}))
    return render_template('/my_shelf.html', title='My Shelf', my_shelf=my_shelf)

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    if session.get('user') is not None:
        username = mongo.db.users.find_one(
            {'username': session['user']})['username']
        return render_template('profile.html', title='Profile', username=username)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
