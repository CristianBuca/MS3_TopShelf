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


@app.route('/')
@app.route('/get_items')
def get_items():
    items = mongo.db.items.find()
    return render_template('items.html', items=items)


@app.route('/search_items', methods=['GET', 'POST'])
def search_items():
    search_items = request.form.get('search_items')
    items = mongo.db.items.find({'$text': {'$search': search_items}})
    return render_template('items.html', Title='Search Results', items=items)


@app.route('/super_search', methods=['GET', 'POST'])
def super_search():
    super_search = request.form.get('super_search')
    users = mongo.db.users.find({'$text': {'$search': super_search}})
    items = mongo.db.items.find({'$text': {'$search': super_search}})
    return render_template('superuser.html', Title='Search Results', users=users, items=items)


'''
User Routes
'''

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Register function uses the RegistrationForm from forms.py,
    Checks username and email against the DB for duplicate,
    Checks if all inputs are valid,
    Redirects user accordingly based on form validation outcome
    If valid
    :return redirect to get_items
    If invalid
    :return render_template of register
    '''
    form = RegistrationForm()
    if request.method == 'POST':
        user_exists = mongo.db.users.find_one({'username': form.username.data.lower()})
        email_exists = mongo.db.users.find_one({'email': form.email.data})
        if user_exists:
            flash('Username already taken', 'deep-orange darken-4 yellow-text text-lighten-5')
            return redirect(url_for('register'))
        elif email_exists:
            flash('Email already in use!', 'deep-orange darken-4 yellow-text text-lighten-5')
        elif form.validate_on_submit():
            register = {
                'username': form.username.data.lower(),
                # Password is hashed using werkzeug.security before being added to DB
                'password': generate_password_hash(form.password.data),
                'email': form.email.data,
                # User is assigned default avatar that he can later change from profile page
                'avatar': '/static/images/avatar_default.jpg',
                # Superuser status set false by default. Only DB admin can promote users
                'superuser': False
            }
            # If form passes field validation then new account data is inserted in the DB
            mongo.db.users.insert_one(register)
            # User is added to session cookies and redirected to landing page
            session['user'] = form.username.data.lower()
            flash(f'Account created {form.username.data}. Welcome aboard!', 'light-green darken-3 yellow-text text-lighten-5')
            return redirect(url_for('get_items'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user_exists = mongo.db.users.find_one({"username": form.username.data.lower()})
        if user_exists and check_password_hash(user_exists['password'], form.password.data):
            session['user'] = form.username.data.lower()
            flash(f'Welcome {form.username.data}. This is what your shelf looks like',  'light-green darken-3 yellow-text text-lighten-5')
            return redirect(url_for('my_shelf', username=session['user']))
        else:
            flash(f'Login Unsuccessful. Double check your username and password!', 'deep-orange darken-4 yellow-text text-lighten-5')
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    flash(f'You have been logged out', 'light-green darken-3 yellow-text text-lighten-5')
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    form = AddStock()
    if request.method == 'POST':
        share = True if request.form.get("share") else False
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
            flash(f'New item was added to your shelf', 'light-green darken-3 yellow-text text-lighten-5')
            return redirect(url_for('get_items'))
    return render_template('add_stock.html', title='Add Stock', form=form)


@app.route('/change_stock/<item_id>', methods=['GET', 'POST'])
def change_stock(item_id):
    item = mongo.db.items.find_one({'_id': ObjectId(item_id)})
    if item['owned_by'] != session['user']:
        abort(403)
    form = AddStock()
    if request.method == 'POST':
        share = True if request.form.get("share") else False
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
            mongo.db.items.replace_one({'_id': ObjectId(item_id)}, stock)
            flash(f'Your Shelf has been updated', 'light-green darken-3 yellow-text text-lighten-5')
            return redirect(url_for('my_shelf'))
    elif request.method == 'GET':
        form.name.data = item['item_name']
        form.age.data = item['age']
        form.distillery.data = item['distillery']
        form.region.data = item['region_name']
        form.notes.data = item['notes']
        form.image.data = item['image']
    return render_template('change_stock.html', title='Change Stock', item=item, form=form)


@app.route('/remove_stock/<item_id>')
def remove_stock(item_id):
    mongo.db.items.delete_one({'_id': ObjectId(item_id)})
    flash(f'Item Removed from Shelf', 'light-green darken-3 yellow-text text-lighten-5')
    return  redirect(url_for('my_shelf'))


@app.route('/remove_user/<user_id>')
def remove_user(user_id):
    mongo.db.users.delete_one({'_id': ObjectId(user_id)})
    flash(f'User removed from database', 'light-green darken-3 yellow-text text-lighten-5')
    return redirect(url_for('superuser'))
    

@app.route('/my_shelf', methods=['GET', 'POST'])
def my_shelf():
    user = session['user']
    my_shelf = mongo.db.items.find({'owned_by': user})
    return render_template('my_shelf.html', title='My Shelf', my_shelf=my_shelf)


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    if session.get('user') is not None:
        user = mongo.db.users.find_one({'username': session['user']})
        user_id = user['_id']
        form = RegistrationForm()
        if request.method == 'GET':
            form.username.data = user['username']
            form.email.data = user['email']
        if request.method == 'POST':
            if form.validate_on_submit():
                update = {
                    'username': request.form.get('username'),
                    'email': request.form.get('email'),
                    'password': generate_password_hash(form.password.data),
                    'avatar': request.form.get('avatar'),
                    'superuser': user['superuser']
                }
                mongo.db.users.replace_one({'_id': ObjectId(user_id)}, update)
                flash(f'Profile successfully updated', 'light-green darken-3 yellow-text text-lighten-5')
                return render_template('profile.html', title='Profile', user=user, form=form)
        return render_template('profile.html', title='Profile', user=user, form=form)


@app.route('/superuser', methods=['GET', 'POST'])
def superuser():
    if session.get('user') is not None:
        user = mongo.db.users.find_one({'username': session['user']})
        if user['superuser']:
            items = mongo.db.items.find()
            users = mongo.db.users.find()
            return render_template('superuser.html', title='Admin', users=users, items=items)
        else:
            flash(f'You do not have the required permission to access this feature', 'deep-orange darken-4 yellow-text text-lighten-5')
            return redirect(url_for('my_shelf'))


'''
ERROR HANDLING
'''

# Error 400
@app.errorhandler(400)
def bad_request(e: object) -> object:
    return render_template('errors/error_400.html', title='400 Error', error=e), 400


# Error 401
@app.errorhandler(401)
def unauthorized(e: object) -> object:
    return render_template('errors/error_401.html', title='401 Error', error=e), 401


# Error 404
@app.errorhandler(404)
def page_not_found(e: object) -> object:
    return render_template('errors/error_404.html', title='404 Error', error=e), 404




if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

