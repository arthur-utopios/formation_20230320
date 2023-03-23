from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=1, max=50,
                                                                          message='should be between 1 and 50 '
                                                                                  'characters')])
    password = PasswordField('password', validators=[DataRequired(message='password is required')])
