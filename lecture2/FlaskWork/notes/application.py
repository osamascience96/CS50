from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "abc"
Session(app)

# notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    # One way of doing this 
    # session["notes"] = notes OR

    # we could apply the condition 
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    
    return render_template("index.html", notes=session["notes"])