from datetime import datetime

from flask import Flask

app = Flask(__name__)

count_view = 0


@app.route("/")
def welcome():
    return "welcome"


@app.route("/date")
def date():
    return "The time is " + str(datetime.now())


@app.route("/count_views")
def count_views():
    global count_view
    count_view += 1
    return f"Welcome for the {count_view}th time"
