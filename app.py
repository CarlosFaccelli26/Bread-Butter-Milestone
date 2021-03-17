import os
from flask import (
    Flask, render_template,
    request, flash, session,
    redirect, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)
db = mongo.db
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(id):
    return User.get(User, id)


class User(UserMixin):
    def __ini__(self, username, id):
        self.id = id
        self.username = username
        self.email = None
        self.hashed_password = None

    def register(self, username, password):
        return

    # login function
    def login(self):
        username = request.args['username']
        hashed_password = generate_password_hash(request.args['password'])
        user = db.users.find_one(
            {'username': username, 'hashed_password': hashed_password})
        if user is None:
            return redirect(url_for('register'))
        return redirect(url_for('index'))

    # setting password
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    # checking if password matches
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def get(self, id):
        user = db.users.find_one({'_id': ObjectId(id)})
        return User(user['username'], user['_id'])

    def find(self, username):
        return db.users.find_one({'username': username})

    # get user from db
    def get_user(self, username, password):
        user_obj = mongo.db.users.find_one({
            'username': username
        })
        if user_obj is None or not check_password_hash(
                user_obj.get('hashed_password'), password):
            return None
        return User(username, str(user_obj['_id']))


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField(
        'E-mail', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

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


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class AddSandwichForm(FlaskForm):
    sandwich_category = SelectField(
        'Sandwich Category', choices=[
            ('Vegetarian'), ('Gluten Free'), ('Hot')])
    sandwich_name = StringField(
        'Sandwich Name', validators=[DataRequired(), Length(min=3, max=20)])
    sandwich_description = TextAreaField(
        'Sandwich Description', validators=[DataRequired()])
    image_Url = StringField('Image Url', validators=[DataRequired()])
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    portion = IntegerField('Portion', validators=[DataRequired()])
    submit = SubmitField('Add Sandwich')


class EditSandwich(FlaskForm):
    sandwich_category = SelectField(
        'Sandwich Category', choices=[
            ('Vegetarian'), ('Gluten Free'), ('Hot')])
    sandwich_name = StringField(
        'Sandwich Name', validators=[DataRequired(), Length(min=3, max=20)])
    sandwich_description = TextAreaField(
        'Sandwich Description', validators=[DataRequired()])
    image_Url = StringField('Image Url', validators=[DataRequired()])
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    portion = IntegerField('Portion', validators=[DataRequired()])
    submit = SubmitField('Add Sandwich')


@app.route('/')
@app.route('/index')
def index():
    sandwiches = mongo.db.sandwiches.find()
    return render_template('index.html', sandwiches=sandwiches)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        register = {
            'username': form.username.data,
            'email': form.email.data,
            'password': form.password.data
        }
        mongo.db.users.insert_one(register)
        flash('Registration Complete. You are able to login',
              category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        print(username)
        password = form.password.data
        print(password)
        user = User.get_user(None, password, username)
        print(user)
        if user is None:
            flash('Password or Email are incorrect. Please try again.',
                  category='danger')
            return redirect(url_for('login'))

        login_user(user)
        flash('Log in Successfull', category='success')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/add_sandwich', methods=['GET', 'POST'])
@login_required
def add_sandwich():
    form = AddSandwichForm()
    return render_template(
            'add_sandwich.html',
            form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
