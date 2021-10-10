from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField, BooleanField
from wtforms.validators import DataRequired, Email, Length, InputRequired, NumberRange


class SettingsForm(FlaskForm):
    name = StringField("Ваше имя: ", validators=[DataRequired()])
    height = DecimalField("Высота поля: ",
                          validators=[NumberRange(min=5, max=30, message="Введите число от 5 до 30"),
                                      DataRequired()])
    width = DecimalField("Ширина поля: ",
                         validators=[NumberRange(min=5, max=30, message="Введите число от 5 до 30"),
                                     DataRequired()])
    field_is_infinity = BooleanField("Поле бесконечно")
    submit = SubmitField("Начать игру")
