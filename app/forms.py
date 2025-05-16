from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, SelectField, TextAreaField, FileField
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

class PageForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    slug = StringField('Уникальное название', validators=[DataRequired()])    

class EditPageForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    slug = StringField('Уникальное название', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменение')

class SectionForm(FlaskForm):
    name = StringField('Название раздела', validators=[DataRequired(), Length(max=255)])
    order = IntegerField('Порядок расположения', validators=[DataRequired()])
    submit = SubmitField('Сохранить изменение')

class ElementForm(FlaskForm):
    element_type = SelectField(
        'Тип элемента',
        choices=[('text', 'Текст'), ('image', 'Картинка'), ('video', 'Видео'), ('link', 'Обычная ссылка'), ('links_doc', 'Ссылка на документ(картинка документа)'), ('links_site', 'Ссылка на какую-либо интернет страницу(картинка сети)')],
        validators=[DataRequired()]
    )
    content = TextAreaField('Содержание', validators=[DataRequired()])
    extra_data = TextAreaField('Дополнительные данные (необязательно)')
    order = IntegerField('Порядок расположения', validators=[DataRequired()])
    submit = SubmitField('Сохранить')