import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

basepath=os.path.abspath(os.path.dirname(__name__))
app=Flask(__name__)
dbinstance=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basepath,"migrate.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
Migrate(app,dbinstance)
class Puppy(dbinstance.Model):
    __tablename__="puppies"
    id=dbinstance.Column(dbinstance.Integer,primary_key=True)
    name=dbinstance.Column(dbinstance.Text)
    age=dbinstance.Column(dbinstance.Integer)
    def __init__(self,name):
        self.name=name
