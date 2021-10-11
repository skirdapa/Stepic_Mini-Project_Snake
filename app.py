import random

import flask
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

from config import Config
from project.forms import SettingsForm

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html", title="Настройки", form=SettingsForm())


@app.route("/game/", methods=["get", "post"])
def base_game():
    if request.method == "GET":
        type_of_field = random.choice(["infinity", "ending"])
        name = 'random_name'
        height = random.randint(10, 30)
        width = random.randint(10, 30)
        url = f"/game/{type_of_field}/{name}/{height}/{width}"
        return flask.redirect(url)
    elif request.method == "POST":
        type_of_field = 'infinity' if request.form.get("type_of_field") else 'ending'
        name = request.form.get("name")
        width = request.form.get("width")
        height = request.form.get("height")
        url = f"/game/{type_of_field}/{name}/{height}/{width}"
        return flask.redirect(url)
    else:
        return flask.abort(404, 'Неверный метод запроса')


@app.route("/game/<type_of_field>/<name>/<int:height>/<int:width>", methods=["get", "post"])
def tuned_game(type_of_field, name, height, width):
    return render_template("game.html", type_of_field=type_of_field, name=name, height=height, width=width)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)


