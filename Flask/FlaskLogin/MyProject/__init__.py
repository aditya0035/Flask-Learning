import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager

app=Flask(__name__)
basepath=os.path.abspath(os.path.dirname(__file__))
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basepath,"database.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="mysecretKey"
Migrate(app,db)

login_manger=LoginManager()
login_manger.init_app(app)
login_manger.LoginVw="LoginVw"
