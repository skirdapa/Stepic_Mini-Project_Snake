from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class SettingsForm(FlaskForm):
    name = StringField("Ваше имя: ",
                       validators=[DataRequired(message="Введите своё имя"),
                                   Length(min=2, message="Имя должно быть длиннее 2х символов")],
                       description="Имя игрока",
                       default="Безымянный герой")
    height = IntegerField("Высота поля: ",
                          validators=[NumberRange(min=5, max=30, message="Введите число от 5 до 30"),
                                      DataRequired("Введите высоту поля: число от 5 до 30")],
                          description="Размеры поля должны быть в пределах от 5 до 30 клеток",
                          default=15)
    width = IntegerField("Ширина поля: ",
                         validators=[NumberRange(min=5, max=30, message="Введите число от 5 до 30"),
                                     DataRequired("Введите ширину поля: число от 5 до 30")],
                         description="Размеры поля должны быть в пределах от 5 до 30 клеток",
                         default=20)
    field_is_infinity = BooleanField("Поле бесконечно")
    # TODO: Доделать режим реального времени
    # type_of_game = SelectField("Тип игры: ", choices=[
    #     ("time", "В реальном времени"),
    #     ("step", "В пошаговом режиме")])
    submit = SubmitField("Начать игру")


class TestForm(FlaskForm):
    word = StringField("Строка: ", [Length(min=5)])
    email = EmailField("Почта: ", [Email()])
    submit = SubmitField("Submit")


class DirectionForm(FlaskForm):
    direction = SelectField("Направление движения: ", choices=[
        ("up", "Вверх"),
        ("down", "Вниз"),
        ("left", "Влево"),
        ("right", "Вправо")])
    submit = SubmitField("Двинуться")
