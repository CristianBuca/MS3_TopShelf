import os
from flask import (
    Flask, flash, render_template, abort,
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


'''
DATABASE READ ROUTES
'''


# Landing/ get_items route
@app.route('/')
@app.route('/get_items')
def get_items() -> object:
    '''
    Get_items function queries the database for all items,
    Sorts them by most recent entry,
    Stores results in items variable to be passed on template render
    :return render_template items.html
    '''
    items = mongo.db.items.find().sort('_id', -1)
    return render_template('items.html', items=items)


# My shelf Route
@app.route('/my_shelf', methods=['GET', 'POST'])
def my_shelf() -> object:
    '''
    My_shelf function pulls the current user name from session cookies,
    Queries the database for entries made by user,
    Stores result in my_shelf variable to be passe on template render
    :return render_template my_shelf.html
    '''
    user = session['user']
    my_shelf = mongo.db.items.find({'owned_by': user})
    return render_template(
        'my_shelf.html', title='My Shelf', my_shelf=my_shelf
    )


# Superuser Route
@app.route('/superuser', methods=['GET', 'POST'])
def superuser() -> object:
    '''
    Superuser function checks that user is logged in,
    Queries the database for user and checks if it has superuser status,
    Queries the database for users and items collection,
    Stores results in items and users variables to be passed on template render
    :return render_template superuser.html
    '''
    if session.get('user') is not None:
        user = mongo.db.users.find_one({'username': session['user']})
        if user['superuser']:
            items = mongo.db.items.find()
            users = mongo.db.users.find()
            return render_template(
                'superuser.html', title='Admin', users=users, items=items
            )
        else:
            flash(
                f'You do not meet the requirements to access this feature',
                'deep-orange darken-4 yellow-text text-lighten-5'
            )
            return redirect(url_for('my_shelf'))


'''
USER AUTHENTICATION ROUTES
'''


# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register() -> object:
    '''
    Register function uses the RegistrationForm from forms.py,
    Checks username and email against the DB for duplicate,
    Checks if all inputs are valid,
    Adds user to the database
    :return render_template of register.html
    '''
    form = RegistrationForm()
    if request.method == 'POST':
        user_exists = mongo.db.users.find_one({
            'username': form.username.data.lower()
        })
        email_exists = mongo.db.users.find_one({'email': form.email.data})
        if user_exists:
            flash(
                'Username already taken',
                'deep-orange darken-4 yellow-text text-lighten-5'
            )
            return redirect(url_for('register'))
        elif email_exists:
            flash(
                'Email already in use!',
                'deep-orange darken-4 yellow-text text-lighten-5'
            )
        elif form.validate_on_submit():
            register = {
                'username': form.username.data.lower(),
                # Password is hashed with werkzeug.security before adding to DB
                'password': generate_password_hash(form.password.data),
                'email': form.email.data,
                # User is assigned default avatar
                'avatar': '/static/images/avatar_default.jpg',
                # Superuser status set false by default
                'superuser': False
            }
            # If form passes validation then new data is inserted in the DB
            mongo.db.users.insert_one(register)
            # User is added to session cookies and redirected to landing page
            session['user'] = form.username.data.lower()
            flash(
                f'Account created {form.username.data}. Welcome aboard!',
                'light-green darken-3 yellow-text text-lighten-5'
            )
            return redirect(url_for('get_items'))
    return render_template('register.html', title='Register', form=form)


# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login() -> object:
    '''
    Login function uses LoginForm from forms.py,
    Checks if user exists in DB and password is correct,
    Stores user in session cookies
    :return render_template of login.html
    '''
    form = LoginForm()
    if request.method == 'POST':
        user_exists = mongo.db.users.find_one({
            "username": form.username.data.lower()
        })
        # Use check_password_hash from werkzeug.security to check password
        if user_exists and check_password_hash(
                user_exists['password'], form.password.data):
            # Add user to session cookies
            session['user'] = form.username.data.lower()
            flash(
                f'Welcome {form.username.data}. This is your Shelf',
                'light-green darken-3 yellow-text text-lighten-5'
            )
            return redirect(url_for('my_shelf', username=session['user']))
        else:
            flash(
                f'Login Unsuccessful. Check your username and password!',
                'deep-orange darken-4 yellow-text text-lighten-5'
            )
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)


# Logout Route
@app.route('/logout')
def logout() -> object:
    '''
    Logout function removes user from session cookies,
    Displays flash message to confirm logout,
    :return redirect to login
    '''
    flash(
        f'You have been logged out',
        'light-green darken-3 yellow-text text-lighten-5'
    )
    session.pop('user')
    return redirect(url_for('login'))


'''
DATABASE SEARCH ROUTES
'''


# Search Route for items in DB
@app.route('/search_items', methods=['GET', 'POST'])
def search_items() -> object:
    '''
    Search_items function checks the items collection index for a match
    with the search input from user
    :return render_template of items.html
    '''
    search_items = request.form.get('search_items')
    items = mongo.db.items.find({'$text': {'$search': search_items}})
    return render_template('items.html', title='Search Results', items=items)


# Super Search Route for users and items in DB
@app.route('/super_search', methods=['GET', 'POST'])
def super_search() -> object:
    '''
    Super_search is available only to superusers,
    Function checks the items and users collection indexes for a match
    :return render_template of superuser.html
    '''
    super_search = request.form.get('super_search')
    users = mongo.db.users.find({'$text': {'$search': super_search}})
    items = mongo.db.items.find({'$text': {'$search': super_search}})
    return render_template(
        'superuser.html', Title='Search Results', users=users, items=items
    )


# Add Stock Route
@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock() -> object:
    '''
    Add_stock function uses AddStock form from forms.py,
    Stores user inputs and validates them,
    Inserts new item in items collection in DB
    :return render_template for add_stock.html for GET method
    '''
    form = AddStock()
    if request.method == 'POST':
        share = True if request.form.get("share") else False
        # Check input validations
        if form.validate_on_submit():
            # Store form data in stock dictionary
            stock = {
                'item_name': form.name.data,
                'region_name': form.region.data,
                'age': form.age.data,
                'distillery': form.distillery.data,
                'notes': form.notes.data,
                'image': form.image.data,
                'share': share,
                'owned_by': session['user'].lower()
            }
            # Insert stock dictionary in DB
            mongo.db.items.insert_one(stock)
            flash(
                f'New item was added to your shelf',
                'light-green darken-3 yellow-text text-lighten-5'
            )
            return redirect(url_for('get_items'))
    return render_template('add_stock.html', title='Add Stock', form=form)


'''
DATABASE UPDATE/DELETE ROUTES
'''


# User profile route
@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username: object) -> object:
    '''
    Profile function uses the RegistrationForm from forms.py,
    Matches the user in session cookies and pulls it's information from DB
    Populates the form with username and e-mail and let's the user
    change password and link to avatar
    :param username: username in session cookies
    :return render template profile.html
    '''
    if session.get('user') is not None:
        user = mongo.db.users.find_one({'username': session['user']})
        user_id = user['_id']
        form = RegistrationForm()
        if request.method == 'GET':
            form.username.data = user['username']
            form.email.data = user['email']
        if request.method == 'POST':
            if form.validate_on_submit():
                # Store user input in update dictionary
                update = {
                    'username': request.form.get('username'),
                    'email': request.form.get('email'),
                    'password': generate_password_hash(form.password.data),
                    'avatar': request.form.get('avatar'),
                    'superuser': user['superuser']
                }
                # replace user data based on user_id
                mongo.db.users.replace_one({'_id': ObjectId(user_id)}, update)
                flash(
                    f'Profile successfully updated',
                    'light-green darken-3 yellow-text text-lighten-5'
                )
                return render_template(
                    'profile.html', title='Profile', user=user, form=form
                )
        return render_template(
            'profile.html', title='Profile', user=user, form=form
        )


# Change stock route
@app.route('/change_stock/<item_id>', methods=['GET', 'POST'])
def change_stock(item_id: object) -> object:
    '''
    Change_stock function uses AddStock form from forms.py,
    Matches the item selected by user to be updated based on _id,
    Checks if user in session is the same as the one that created the item,
    :param _id: user id from DB
    :return render_template of change_stock.html
    '''
    item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
    if item['owned_by'] != session['user']:
        abort(403)
    form = AddStock()
    if request.method == 'POST':
        share = True if request.form.get("share") else False
        if form.validate_on_submit():
            # Store new form data in stock dictionary
            stock = {
                'item_name': form.name.data,
                'region_name': form.region.data,
                'age': form.age.data,
                'distillery': form.distillery.data,
                'notes': form.notes.data,
                'image': form.image.data,
                'share': share,
                'owned_by': session['user'].lower()
            }
            # replace item data in DB with data from stock dictionary
            mongo.db.items.replace_one({'_id': ObjectId(item_id)}, stock)
            flash(
                f'Your Shelf has been updated',
                'light-green darken-3 yellow-text text-lighten-5'
            )
            return redirect(url_for('my_shelf'))
    elif request.method == 'GET':
        form.name.data = item['item_name']
        form.age.data = item['age']
        form.distillery.data = item['distillery']
        form.region.data = item['region_name']
        form.notes.data = item['notes']
        form.image.data = item['image']
    return render_template(
        'change_stock.html', title='Change Stock', item=item, form=form
    )


# Remove Stock route
@app.route('/remove_stock/<item_id>')
def remove_stock(item_id: object) -> object:
    '''
    Function remove_stock deletes the item from the database,
    :param item_id: the id of the item in the DB
    :return redirect to my_shelf
    '''
    mongo.db.items.delete_one({'_id': ObjectId(item_id)})
    flash(
        f'Item Removed from Shelf',
        'light-green darken-3 yellow-text text-lighten-5'
    )
    return redirect(url_for('my_shelf'))


# Remove User route
@app.route('/remove_user/<user_id>')
def remove_user(user_id: object) -> object:
    '''
    Function remove_user delete the user from the database,
    Only accessible by superusers.
    :param: user_id: the id of the user in the DB
    :return redirect to superuser
    '''
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    flash(
        f'User removed from database',
        'light-green darken-3 yellow-text text-lighten-5'
    )
    return redirect(url_for('superuser'))


'''
ERROR HANDLING
'''


# Error 400
@app.errorhandler(400)
def bad_request(e: object) -> object:
    '''
    When error 400 occurs render template for respective page,
    :param e: the error that occurs
    :return render_template of error_400.html
    '''
    return render_template(
        'errors/error_400.html', title='400 Error', error=e), 400


# Error 401
@app.errorhandler(401)
def unauthorized(e: object) -> object:
    '''
    When error 401 occurs render template for respective page,
    :param e: the error that occurs
    :return render_template of error_401.html
    '''
    return render_template(
        'errors/error_401.html', title='401 Error', error=e), 401


# Error 404
@app.errorhandler(404)
def page_not_found(e: object) -> object:
    '''
    When error 404 occurs render template for respective page,
    :param e: the error that occurs
    :return render_template of error_404.html
    '''
    return render_template(
        'errors/error_404.html', title='404 Error', error=e), 404


# Error 405
@app.errorhandler(405)
def method_not_allowed(e: object) -> object:
    '''
    When error 405 occurs render template for respective page,
    :param e: the error that occurs
    :return render_template of error_405.html
    '''
    return render_template(
        'errors/error_405.html', title='405 Error', error=e), 405


# Error 500
@app.errorhandler(500)
def internal_server_error(e: object) -> object:
    '''
    When error 500 occurs render template for respective page,
    :param e: the error that occurs
    :return render_template of error_500.html
    '''
    return render_template(
        'errors/error_500.html', title='500 Error', error=e), 500

# Initialize app using environment variables
if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
