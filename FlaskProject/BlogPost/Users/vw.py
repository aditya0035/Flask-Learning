from flask import Blueprint,render_template,request,flash,redirect,url_for
from .Forms.Login import LoginForm
from .Forms.Register import RegistrationForm
from BlogPost.DataBase.DTO.Users import User,SaveUser
from flask_login import login_user,login_required,logout_user
from wtforms.validators import ValidationError
user_blueprint=Blueprint("user",__name__,template_folder="templates/Users")

@user_blueprint.route("/login",methods=["GET","POST"])
def Login():
    loginform=LoginForm()
    if loginform.validate_on_submit():
        print(loginform.Email.data)
        user=User.query.filter_by(Email=loginform.Email.data).first()
        print(f"User is {user}")
        if User is not None and user.check_password_hash(loginform.Password.data):
            login_user(user)
            next=request.args.get('next',default=None)
            print(next)
            if  next is None or next=="/" or next[0]=="/Home":
                next=url_for("post.AllPost",page=1,pageSize=5)
            return redirect(next)
        else:
            flash("Invalid username or password")
    return render_template("login.html",form=loginform)


@user_blueprint.route("/register",methods=["GET","POST"])
def Register():
    registrationForm=RegistrationForm()
    validationError=registrationForm.validate()
    if registrationForm.validate_on_submit():
        try:
            user=User.query.filter_by(Email=registrationForm.Email.data).first()
            print(user)
            if user is not None:
                print("User eamil error")
                validationError=True
                flash("Email-Id already exists")
            user=User.query.filter_by(Username=registrationForm.UserName.data).first()
            if user is not None:
                validationError=False
                flash("UserName already exists")
            if not validationError:
                raise ValidationError
        except ValidationError as ex:
            return redirect(url_for("user.Register"))
        else:
            user=User(registrationForm.Email.data,registrationForm.UserName.data,registrationForm.Password.data)
            SaveUser(user)
            print("User Saved")
            login_user(user)
            return redirect(url_for("Index"))
    return render_template("register.html",form=registrationForm,validationError=validationError)

@login_required
@user_blueprint.route("/logout")
def Logout():
    logout_user()
    return redirect(url_for("Index"))
