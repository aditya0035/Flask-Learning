from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
class LoginForm(FlaskForm):
    Email=StringField("Email",validators=[DataRequired(message="Plase provide email")])
    Password=PasswordField("Password",validators=[DataRequired("Please provide password")])
    RememberMe=BooleanField("Remember Me")
    Submit=SubmitField("Login")
