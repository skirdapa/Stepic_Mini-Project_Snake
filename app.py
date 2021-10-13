import random

import flask
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

from config import Config
from project.forms import SettingsForm, TestForm

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)


@app.route("/", methods=["post", "get"])
def index():
    form = SettingsForm()
    if request.method == "POST" and form.validate_on_submit():
        type_of_field = 'infinity' if request.form.get("field_is_infinity") else 'ending'
        name = request.form.get("name")
        width = request.form.get("width")
        height = request.form.get("height")
        type_of_game = request.form.get("type_of_game")
        url = f"/game/{type_of_field}/{type_of_game}/{name}/{height}/{width}"
        return flask.redirect(url)
    return render_template("index.html", title="Настройки", form=form)


@app.route("/game/")
def base_game():
    if request.method == "GET":
        type_of_field = random.choice(["infinity", "ending"])
        name = 'random_name'
        height = random.randint(10, 30)
        width = random.randint(10, 30)
        type_of_game = random.choice(["time", "step"])
        url = f"/game/{type_of_field}/{type_of_game}/{name}/{height}/{width}"
        return flask.redirect(url)
    else:
        return flask.abort(404, 'Неверный метод запроса')


@app.route("/game/<type_of_field>/<type_of_game>/<name>/<int:height>/<int:width>", methods=["get", "post"])
def tuned_game(type_of_field, type_of_game, name, height, width):
    return render_template("game.html",
                           type_of_field=type_of_field, type_of_game=type_of_game, name=name,
                           height=height, width=width)


@app.route("/test", methods=["get", "post"])
def test_form():
    form = TestForm()
    setting_form = SettingsForm()
    form.validate_on_submit()
    setting_form.validate_on_submit()
    return render_template("test.html", form=form, setting_form=setting_form)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)


