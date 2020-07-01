from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class Upload(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    file = FileField('text file', validators=[FileRequired(),FileAllowed(['txt'], 'text files only!')])
    submit = SubmitField('Send')