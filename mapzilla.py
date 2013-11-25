from flask import Flask, render_template
from flask.ext.pymongo import PyMongo
from flask.ext.sqlalchemy import SQLAlchemy

# Setup application
app = Flask(__name__)

app.debug = True
app.config.from_pyfile('config/app.py')

# Postgresql
db = SQLAlchemy(app)

# MongoDB
mongo = PyMongo(app, config_prefix='MONGO')

@app.route("/")
def hello():
    collections = ', '.join(mongo.db.collection_names())
    return render_template('index.html', dde=collections)
    # return render_template('index.html')

if __name__ == '__main__':
    app.run()