import os
from .Configuration import Configuration
from .Logger import Logger
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

def SetupMigration(app,database):
    Migrate(app,database)

def SetupDatabase(app):
    return SQLAlchemy(app)

def ConfigureAppConfig(app,configuration):
    try:
        app.config["SECRET_KEY"]=configuration.GetSecretKey()
        app.config["SQLALCHEMY_DATABASE_URI"]=configuration.GetConnectionString()
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    except Exception as ex:
        Logger.write("exception occured while configuring app")
        Logger.write(f"exception details:{ex}")
        raise

def SetupLoginManager(app):
    login_manger=LoginManager()
    login_manger.init_app(app)
    login_manger.login_view="user.Login"
    return login_manger

def GetConfiguration(configuration):
    if configuration==None:
        return Configuration("mysecretkey","BlogDataBase","Blog.sqlite")
    else:
        return configuration

application=Flask(__name__,template_folder='templates')
ConfigureAppConfig(application,GetConfiguration(None))
dataBase=SetupDatabase(application)
SetupMigration(application,dataBase)
login_manager=SetupLoginManager(application)
Logger.write("application Ended")
