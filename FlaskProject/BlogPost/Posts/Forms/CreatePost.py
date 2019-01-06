from flask_wtf import FlaskForm
from wtforms import TextField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    Title=TextField("Provide title",validators=[DataRequired("Please provide title")])
    Text=TextAreaField("Provide a short Description",validators=[DataRequired(("Please provide description"))])
    Submit=SubmitField("Create Post")
