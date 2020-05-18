from flask import Flask, render_template, abort, jsonify

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html",
                           cards=db)


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index, max_index=len(db) - 1)
    except IndexError:
        abort(404)


@app.route('/api/card')
def card():
    return jsonify(db)


@app.route("/api/card/<int:index>")
def card_view_api(index):
    try:
        card = db[index]
        return card
    except IndexError:
        abort(404)
