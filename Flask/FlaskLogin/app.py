from MyProject import app,db
from flask import Flask,render_template,session,flash,abort,redirect,url_for,request
from flask_login import login_required,logout_user,login_user
from MyProject.models import User
from MyProject.forms import LoginForm,RegistrationForm

@app.route("/",methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/welcome")
@login_required
def Welcome():
    return render_template("welcome.html")

@app.route("/logout")
@login_required
def Logout():
    logout_user()
    flash("Your have been logout")
    return redirect(url_for("home"))

@app.route("/login",methods=["GET","POST"])
def LoginVw():
        loginform=LoginForm()
        if loginform.validate_on_submit():
            user=User.query.filter_by(Email=loginform.email.data)
            if user is not None and user.Check_Password(loginform.password.data):
                login_user(user)
                flash("login sucessfully")
                next=request.arg.get("next")
                if next is None or not next[0]=="/":
                    next=url_for("welcome.html")
                return redirect(next)
        return render_template("login.html",form=loginform)

@app.route("/Register",methods=["GET","POST"])
def Registration():
    registrationform=RegistrationForm()
    if registrationform.validate_on_submit():
        user=User(registrationform.email.data,registrationform.username.data,registrationform.password.data)
        db.session.add(user)
        db.session.commit()
        flash("thanks for registration")
        return redirect(url_for("LoginVw"))
    return render_template("register.html",form=registrationform)

if __name__=="__main__":
    app.run(debug=True)
