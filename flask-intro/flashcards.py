from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

from model import db, save_file

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
        return db[index]
    except IndexError:
        abort(404)


@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        card = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(card)
        save_file()
        return redirect(url_for('card_view', index=len(db) - 1))
    else:
        return render_template('add_card.html')


@app.route('/delete_card/<int:index>', methods=['GET', 'POST'])
def delete_card(index):
    try:
        if request.method == 'GET':
            return render_template('delete_card.html', card=db[index])
        else:
            del db[index]
            save_file()
            return redirect(url_for('welcome'))
    except IndexError:
        abort(404)
