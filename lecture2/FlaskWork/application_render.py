from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # headline variable that is plugged in html 
    headline = "I love Girls"
    return render_template("index.html", headline=headline)

@app.route("/osama")
def osama():
    # headline variable for another plug in html
    headline = "Girls don't love Osama"
    return render_template("index.html", headline=headline)

