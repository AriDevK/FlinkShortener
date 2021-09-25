from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import URLField


class UrlForm(FlaskForm):
    url = URLField('URL', validators=[DataRequired()])
    submit = SubmitField('Shorten')
