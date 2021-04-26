import os
from flask import (
    Flask, render_template,
    request, flash,
    redirect, url_for,
    abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    SubmitField, SelectField,
    IntegerField, TextAreaField)
from wtforms.validators import (
    DataRequired, Email, EqualTo, Length, ValidationError)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_user,
    login_required,
    logout_user)
if os.path.exists('env.py'):
    import env


app = Flask(__name__)
# app config
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')
# initializing mono
mongo = PyMongo(app)
db = mongo.db
# initializing login mananger
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# user loader for flask-login
@login_manager.user_loader
def load_user(username):
    user = mongo.db.users.find_one({'username': username})
    if not user:
        return None
    return User(user['username'], user['email'], user['_id'])


# user class
class User(UserMixin):
    def __init__(self, username, email, _id):
        self.username = username
        self.email = email
        self._id = _id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)


# registration form so the user can sign up on the webiste
class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=6, max=20)],
        render_kw={'placeholder': 'Username'})
    email = StringField(
        'E-mail',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'E-mail'})
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8, max=16)],
        render_kw={'placeholder': 'Password'})
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Confirm Password'})
    submit = SubmitField('Register')

    # check if username exist
    def validate_username(self, username):
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if user:
            raise ValidationError(
                """This username already exists.
                Please choose a different one.""")

    # check if email exist
    def validate_email(self, email):
        user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if user:
            raise ValidationError(
                """This email already exists.
                Please choose a different one.""")


# login form so user can sing in on the website
class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Username'})
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password'})
    submit = SubmitField('Log in')


# form to add sandwich 
class AddSandwichForm(FlaskForm):
    # sandwich_category = SelectField(
    #     'Sandwich Category', choices=[
    #         (None, 'Select an Option'),
    #         ('Gluten Free', 'Gluten Free'),
    #         ('Vegetarian', 'Vegetarian')])
    sandwich_name = StringField(
        'Sandwich Name',
        validators=[DataRequired(),
                    Length(min=3, max=20)],
        render_kw={'placeholder': 'sandwich name'})
    sandwich_description = TextAreaField(
        'Sandwich Description',
        validators=[DataRequired()],
        render_kw={'placeholder': 'sandwich description'})
    image_Url = StringField('Image Url',
                            validators=[DataRequired()],
                            render_kw={
                                'placeholder':
                                'pase the image address here'})
    ingredients = StringField('Ingredients',
                              validators=[DataRequired()],
                              render_kw={
                                  'placeholder':
                                  'Write ingredients separeted by a coma'})
    portion = IntegerField(
        'Portion',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Add portion of sandwiches (only numbers)'})
    duration = IntegerField(
        'Duration', validators=[DataRequired()],
        render_kw={'placeholder': 'Duration of sandwich'})
    submit = SubmitField('Add')


# form to edit sandwiches
class EditSandwich(FlaskForm):
    sandwich_name = StringField(
        'Sandwich Name', validators=[DataRequired(), Length(min=3, max=20)])
    sandwich_description = TextAreaField(
        'Sandwich Description', validators=[DataRequired()])
    image_Url = StringField('Image Url', validators=[DataRequired()])
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    portion = IntegerField('Portion', validators=[DataRequired()])
    duration = IntegerField(
        'Duration', validators=[DataRequired()],
        render_kw={'placeholder': 'Duration of sandwich'})
    submit = SubmitField('Update')


@app.route('/')
@app.route('/index')
def index():
    '''
        Index page will be available to all users signed
        in or not
        will display sandwiches
        that other users added with a limit of 8 sandwiches
    '''
    # sandwiches that will be display on the carousel
    sandwich_carousel = list(
        mongo.db.sandwiches.find().limit(3).sort('snadwich_name', 1))
    # sandwiches that will be display on cards
    sandwiches = list(mongo.db.sandwiches.find().limit(8))
    return render_template('index.html',
                           sandwiches=sandwiches,
                           sandwich_carousel=sandwich_carousel)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        mongo.db.users.insert_one({
            'username': form.username.data,
            'email': form.email.data,
            'password': hashed_password
        })
        flash('Registration successfully. You are able to login.',
              category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.users.find_one({'username': form.username.data})
        if user and User.check_password(user['password'], form.password.data):
            user_obj = User(user['username'], user['email'], user['_id'])
            login_user(user_obj)
            flash('Logged in Successfully', category='success')
            next = request.args.get('next')
            return redirect(next or url_for('index'))
        else:
            flash('Username or Email are incorrect', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/add_sandwich', methods=['GET', 'POST'])
@login_required
def add_sandwich():
    # categories variable will be used for selectfield on the template
    categories = mongo.db.categories.find()
    sandwiches = mongo.db.sandwiches.find()
    form = AddSandwichForm()
    if form.validate_on_submit():
        sandwich = {
            'sandwich_category': request.form.get('sandwich_category'),
            'sandwich_name': form.sandwich_name.data,
            'sandwich_description': form.sandwich_description.data,
            'imageUrl': form.image_Url.data,
            'ingredients': form.ingredients.data,
            'portion': form.portion.data,
            'duration': form.duration.data,
            'difficulty': request.form.get('difficulty'),
            'created_by': current_user.username,
        }
        mongo.db.sandwiches.insert_one(sandwich)
        flash('Sandwich Added.', category='success')
        return redirect(url_for('index'))
    return render_template(
            'add_sandwich.html',
            form=form,
            categories=categories,
            sandwiches=sandwiches)


@app.route('/sandwich/<sandwich_id>')
@login_required
def sandwich(sandwich_id):
    sandwich = mongo.db.sandwiches.find_one(
        {'_id': ObjectId(sandwich_id)})
    return render_template('sandwich.html', sandwich=sandwich)


@app.route('/edit_sandwich/<sandwich_id>', methods=['GET', 'POST'])
@login_required
def edit_sandwich(sandwich_id):
    categories = mongo.db.categories.find()
    sandwiches = mongo.db.sandwiches.find()
    form = EditSandwich()
    sandwich = mongo.db.sandwiches.find_one({'_id': ObjectId(sandwich_id)})
    if sandwich['created_by'] != current_user:
        abort(403)
    if request.method == 'POST':
        submit = {
            'sandwich_category': request.form.get('sandwich_category'),
            'sandwich_name': form.sandwich_name.data,
            'sandwich_description': form.sandwich_description.data,
            'imageUrl': form.image_Url.data,
            'ingredients': form.ingredients.data,
            'portion': form.portion.data,
            'duration': form.duration.data,
            'created_by': current_user.username
        }
        mongo.db.sandwiches.update({'_id': ObjectId(sandwich_id)}, submit)
        flash('Sandwich Updated', category='success')
        return redirect(url_for('sandwich', sandwich_id=sandwich_id))
    if request.method == 'GET':
        form.sandwich_name.data = sandwich['sandwich_name']
        form.sandwich_description.data = sandwich['sandwich_description']
        form.image_Url.data = sandwich['imageUrl']
        form.ingredients.data = sandwich['ingredients']
        form.portion.data = sandwich['portion']
        form.duration.data = sandwich['duration']
    return render_template('edit_sandwich.html',
                           form=form, sandwich=sandwich,
                           categories=categories,
                           sandwiches=sandwiches)


@app.route('/delete_sandwich/<sandwich_id>', methods=['GET', 'POST'])
def delete_sandwich(sandwich_id):
    sandwich = mongo.db.sandwiches.find_one({'_id': ObjectId(sandwich_id)})
    if sandwich['created_by'] != current_user:
        abort(403)
    mongo.db.sandwiches.remove({'_id': ObjectId(sandwich_id)})
    flash('Sandwich Deleted', 'success')
    return redirect(url_for('index'))


@app.route('/all_sandwich')
@login_required
def all_sandwich():
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page'
    )
    # per_page = 8
    # offset = page * per_page

    total = mongo.db.sandwiches.find().count()

    sandwiches = mongo.db.sandwiches.find()

    sandwich_pagination = sandwiches[offset: offset + per_page]
    print(sandwich_pagination)

    pagination = Pagination(page=page,
                            per_page=per_page,
                            total=total,
                            css_framework='bootstrap4')

    return render_template('all_sandwich.html',
                           sandwiches=sandwiches,
                           page=page,
                           per_page=per_page,
                           sandwich_pagination=sandwich_pagination,
                           pagination=pagination)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query')
    sandwiches = list(mongo.db.sandwiches.find({'$text': {'$search': query}}))
    return render_template('index.html',
                           sandwiches=sandwiches)


# Errors

@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html')


@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html')


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
