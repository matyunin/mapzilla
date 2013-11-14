from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hddelloe World!"

@app.route("/gift/")
def gift():
    return render_template('gift.html')

if __name__ == "__main__":
    app.run()

