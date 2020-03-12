from flask import Flask

app = Flask(__name__)


# default rotue
@app.route("/")
def index():
    return "Osama Ahmed"

# another route
@app.route("/osama")
def osama():
    return "Hello, Osama!"

# dynamic route
@app.route("/<string:name>")
def hello(name):
    # capitalize the first char of the name
    name = name.capitalize()
    return f"<h1>Hello, {name}</h1>"