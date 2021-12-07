from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = StringField('Name of the pet', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    content = TextAreaField('Description, personality, etc.', validators=[DataRequired()])
    pictures = FileField('Upload pictures', validators=[FileAllowed(['jpg', 'png'])])
    adoption_info = TextAreaField('How can people contact you? Email, phone number?', validators=[DataRequired()])
    submit = SubmitField('Done')
