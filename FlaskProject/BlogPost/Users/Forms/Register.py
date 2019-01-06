from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SelectField,RadioField,SubmitField,BooleanField
from wtforms.validators import DataRequired,EqualTo

class RegistrationForm(FlaskForm):
    Email=StringField("Email",validators=[DataRequired(message="Please provide email")])
    UserName=StringField("UserName",validators=[DataRequired(message="Please provide email")])
    Password=PasswordField("Password",validators=[DataRequired(message="Please provide email"),EqualTo("ConfirmPassword",message="Password do not match")])
    ConfirmPassword=PasswordField("Confirm Password",validators=[DataRequired(message="Please provide email")])
    Gender=RadioField(label="Gender",choices=[("male","Male"),("female","Female"),("other","Not Specified")])
    Skills=SelectField(label="Prferred Skills",choices=[("write","Writing"),("read","reading")])
    Feeds=BooleanField("Interested in Feeds")
    Picture = FileField('Update Profile Picture')
    Submit=SubmitField("Register")
