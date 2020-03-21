from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# route for POST method that posts the value from form to the hello.html
@app.route("/hello", methods=["GET", "POST"])
def hello():
    if (request.method == "GET"):
        return "Please Submit the Form"
    else:
        number = request.form.get("number")
        number = str(int(number) * 2)
        return render_template("hello.html", number=number)