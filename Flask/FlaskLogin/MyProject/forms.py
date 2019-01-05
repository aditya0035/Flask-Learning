from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from MyProject.models  import User

class RegistrationForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired,Email])
    username=StringField("username",validators=[DataRequired(message="Mandatory")])
    password=PasswordField("Password",validators=[DataRequired,EqualTo("passwordConfirm",message="Password Do not Match")])
    passwordConfirm=PasswordField("Confrim Password",validators=[DataRequired])
    submit=SubmitField("Register")
    def check_email(self,field):
        if User.query.filter_by(Email=field.data).first():
            raise ValidationError("Your Email Has been already Registerd")
    def Check_UserName(self,field):
        if User.query.filter_by(Username=field.data).first():
            raise ValidationError("UserName Is taken")

class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired,Email])
    password=PasswordField("Password",validators=[DataRequired])
    submit=SubmitField("Login")
