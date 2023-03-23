from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length, DataRequired


class PostForm(FlaskForm):
    title = StringField('title', validators=[Length(min=3, max=50, message='title should be 3 to 50 characters')])
    content = StringField('content', validators=[DataRequired()])
