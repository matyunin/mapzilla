from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Hddelloe World!"

@app.route("/gift/")
def gift():
    return render_template('gift.html')

if __name__ == "__main__":
    app.run()

