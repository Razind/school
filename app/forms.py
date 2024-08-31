from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class NewsForm(FlaskForm):
    title = StringField('Заголовок (макс. 250 символов)', validators=[DataRequired(), Length(min=10, max=250)])
    content = TextAreaField('Текст новости (макс. 1000 символов)', validators=[DataRequired(), Length(min=50, max=5000)])
    image = FileField('Изображение', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Добавить')