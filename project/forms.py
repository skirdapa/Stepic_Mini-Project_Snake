from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DecimalField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length, InputRequired, NumberRange, ValidationError


def validate_word_15(form, field):
    excluded_number = '15'
    print("начинаем проверку")
    if excluded_number in field.data:
        print("нашли ошибку")
        raise ValidationError("Нельзя число 15 писать в этой форме!!!")
    else:
        print("всё норм")


class SettingsForm(FlaskForm):
    name = StringField("Ваше имя: ",
                       validators=[validate_word_15, DataRequired(message="Введите своё имя"),
                                   Length(min=2, message="Имя должно быть длиннее 2х символов")],
                       description="Имя игрока",
                       default="Безымянный герой")
    height = DecimalField("Высота поля: ",
                          validators=[NumberRange(min=5, max=30, message="Введите число от 5 до 30"),
                                      DataRequired("Введите высоту поля")],
                          description="Размеры поля должны быть в пределах от 5 до 30 клеток",
                          default=15,
                          places=0)
    width = DecimalField("Ширина поля: ",
                         validators=[NumberRange(min=5, max=30, message="Введите число от 5 до 30"),
                                     DataRequired("Введите ширину поля")],
                         description="Размеры поля должны быть в пределах от 5 до 30 клеток",
                         default=20,
                         places=0)
    field_is_infinity = BooleanField("Поле бесконечно")
    submit = SubmitField("Начать игру")


class TestForm(FlaskForm):
    word = StringField("Строка: ", [validate_word_15, Length(min=5)])
    email = EmailField("Почта: ", [Email()])
    submit = SubmitField("Submit")
