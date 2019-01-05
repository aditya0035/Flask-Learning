from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app=Flask(__name__)
app.config["SECRET_KEY"]="abcdreeeassaassa"
class InfoForm(FlaskForm):
    breed=StringField("Please enter a breed")
    submit=SubmitField("Submit")

@app.route("/",methods=['GET','POST'])
def Index():
    breed=False
    form=InfoForm()
    if form.validate_on_submit():
        breed=form.breed.data
        form.breed.data=''
    return render_template("Index14.html",form=form,breed=breed)


if __name__=='__main__':
    app.run(debug=True)
