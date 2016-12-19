from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    username = TextField("Username", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    remember = BooleanField("Remember Me", default=False)


class InputForm(FlaskForm):
    text = TextAreaField("Post", validators=[Required()])
    fb = BooleanField("Facebook", default=True)
    twitter = BooleanField("Twitter", default=True)
