from flask import (Flask,render_template,request,session,url_for,redirect)
from flask_wtf import FlaskForm
from wtforms import (StringField,TextAreaField,SelectField,RadioField,
BooleanField,DateTimeField,SubmitField)
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SECRET_KEY']="mySecretKey"

class InfomationForm(FlaskForm):
    breed=StringField("Your Breed",validators=[DataRequired()])
    neatued=BooleanField("Neauted")
    mood=RadioField("Your Mood",choices=[("mood-one","Happy"),("mood-two","Exited")])
    food=SelectField("What would you like",choices=[("chi","Chicken"),("bef","beef"),("fish","Fish")])
    feedBack=TextAreaField()
    submit=SubmitField("Submit")


@app.route("/",methods=["GET","POST"])
def Index():
    form=InfomationForm()
    if form.validate_on_submit():
        session["breed"]=form.breed.data
        session["neatued"]=form.neatued.data
        session["mood"]=form.mood.data
        session["food"]=form.food.data
        session["feedBack"]=form.feedBack.data
        return redirect(url_for("ThankYou"))
    return render_template("Index15.html",form=form)

@app.route("/ThankYou",methods=["GET"])
def ThankYou():
    return render_template("Thanks15.html")

if __name__=="__main__":
    app.run(debug=True)
