from flask import Flask,flash,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

app=Flask(__name__)
app.config["SECRET_KEY"]="mysecretkey"

class InfoForm(FlaskForm):
    submit=SubmitField("Submit")

@app.route("/",methods=["GET","POST"])
def Index():
    form=InfoForm()
    if form.validate_on_submit():
        print("submit")
        flash("You Have Clicked The button")
        return redirect(url_for("Index"))
    return render_template("Index16.html",form=form)


if __name__=="__main__":
    app.run(debug=True)
