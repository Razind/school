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
    name = StringField('Name', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])    

class EditPageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

class SectionForm(FlaskForm):
    name = StringField('Section Name', validators=[DataRequired(), Length(max=255)])
    order = IntegerField('Order', validators=[DataRequired()])
    submit = SubmitField('Save')

class ElementForm(FlaskForm):
    element_type = SelectField(
        'Element Type',
        choices=[('text', 'Text'), ('image', 'Image'), ('video', 'Video'), ('link', 'Link')],
        validators=[DataRequired()]
    )
    content = TextAreaField('Content', validators=[DataRequired()])
    extra_data = TextAreaField('Extra Data (Optional)')
    order = IntegerField('Order', validators=[DataRequired()])
    submit = SubmitField('Save')