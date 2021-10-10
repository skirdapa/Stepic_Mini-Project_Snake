from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from config import Config
from project.forms import SettingsForm

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)



@app.route("/")
def index():
    return render_template("index.html", title="Настройки", form=SettingsForm())


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)


