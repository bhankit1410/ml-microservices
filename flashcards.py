from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def welcome():
    return "welcome"

@app.route("/date")
def date():
    return "The time is " + str(datetime.now())

