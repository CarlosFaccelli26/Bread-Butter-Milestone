import os
from flask import (
    Flask, render_template,
    request, flash,
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
def load_user(username):
    user = mongo.db.users.find_one({'username': username})
    if not user:
        return None
    return User(user['username'], user['email'], user['_id'])


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
    submit = SubmitField('Add')


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
    submit = SubmitField('Update')


@app.route('/')
@app.route('/index')
def index():
    sandwiches = list(mongo.db.sandwiches.find())
    return render_template('index.html', sandwiches=sandwiches)


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
    form = AddSandwichForm()
    if form.validate_on_submit():
        sandwich = {
            'sandwich_category': form.sandwich_category.data,
            'sandwich_name': form.sandwich_name.data,
            'sandwich_description': form.sandwich_description.data,
            'imageUrl': form.image_Url.data,
            'ingredients': form.ingredients.data,
            'portion': form.portion.data,
            'created_by': current_user.username
        }
        mongo.db.sandwiches.insert_one(sandwich)
        flash('Sandwich Added.', category='success')
        return redirect(url_for('index'))
    return render_template(
            'add_sandwich.html',
            form=form)


@app.route('/sandwich/<sandwich_id>')
@login_required
def sandwich(sandwich_id):
    sandwich = mongo.db.sandwiches.find_one(
        {'_id': ObjectId(sandwich_id)})
    return render_template('sandwich.html', sandwich=sandwich)


@app.route('/edit_sandwich/<sandwich_id>', methods=['GET', 'POST'])
@login_required
def edit_sandwich(sandwich_id):
    form = EditSandwich()
    sandwich = mongo.db.sandwiches.find_one({'_id': ObjectId(sandwich_id)})
    if request.method == 'POST':
        submit = {
            'sandwich_category': form.sandwich_category.data,
            'sandwich_name': form.sandwich_name.data,
            'sandwich_description': form.sandwich_description.data,
            'imageUrl': form.image_Url.data,
            'ingredients': form.ingredients.data,
            'portion': form.portion.data,
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
    return render_template('edit_sandwich.html', form=form, sandwich=sandwich)


@app.route('/delete_sandwich/<sandwich_id>', methods=['GET', 'POST'])
def delete_sandwich(sandwich_id):
    mongo.db.sandwiches.remove({'_id': ObjectId(sandwich_id)})
    flash('Sandwich Deleted', 'success')
    return redirect(url_for('index'))


@app.route('/all_sandwich')
@login_required
def all_sandwich():
    sandwiches = list(mongo.db.sandwiches.find())
    return render_template('all_sandwich.html', sandwiches=sandwiches)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
