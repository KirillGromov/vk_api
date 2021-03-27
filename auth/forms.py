from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import InputRequired, Length, Regexp
import re


class RegForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Regexp("^[A-Za-z0-9_-]*$") ,Length(min=3, max=30, message="Lenght username incorrect ")])
    password = PasswordField('Password', validators=[InputRequired(), Regexp("^[A-Za-z0-9_-]*$") ,Length(min=3, max=30, message="Lenght password incorrect")])
    c_password = PasswordField('Confim password', validators=[InputRequired(), Regexp("^[A-Za-z0-9_-]*$") ,Length(min=3, max=30, message="Lenght password incorrect")])

class LogForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(),Regexp("^[A-Za-z0-9_-]*$") ,Length(min=3, max=30, message="Lenght username incorrect")])
    password = PasswordField('Password', validators=[InputRequired(),Regexp("^[A-Za-z0-9_-]*$") ,Length(min=3, max=30, message="Lenght password incorrect")])
    token = PasswordField('Token')