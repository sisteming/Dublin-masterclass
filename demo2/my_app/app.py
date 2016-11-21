from flask import Flask, request, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_HOST'] = '172.20.0.3'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'flask_demo'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route('/users')
def home_page():
    online_users = mongo.db.users.find({})
    return render_template('index.html',
        online_users=online_users)
