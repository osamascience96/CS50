from flask import Flask, render_template

app = Flask(__name__)

# route to first_page on default route
@app.route("/")
def index():
    return render_template("first_page.html")


# route to nextpage that routes to secondpage
@app.route("/more")
def more():
    return render_template("second_page.html")