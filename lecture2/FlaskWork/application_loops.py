from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Saad", "Jafri", "Usman", "Osama"]
    return render_template("loop.html", names=names)