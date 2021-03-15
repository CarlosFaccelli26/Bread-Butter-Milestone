import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
if os.path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    sandwiches = mongo.db.sandwiches.find()
    return render_template('index.html', sandwiches=sandwiches)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
