import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Get the current date and time
    now = datetime.datetime.now()
    # init the date for the rabi-ul-awal
    new_rabiulawal = now.date == 1 and now.month == 11 and now.year == 2020
    return render_template("Rabiulawal.html", new_rabiulawal=new_rabiulawal)
