import os
from  flask import Flask
from flask_sqlalchemy import SQLAlchemy

dbPath=os.path.abspath(os.path.dirname(__file__))
dbfile=os.path.join(dbPath,"data.sqlite")
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+dbfile
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
dbInstance=SQLAlchemy(app)

class Puppy(dbInstance.Model):
    __tablename__="puppies"
    id=dbInstance.Column(dbInstance.Integer,primary_key=True)
    name=dbInstance.Column(dbInstance.Text)
    age=dbInstance.Column(dbInstance.Integer)
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f'Puppy {self.name} is {self.age} years old'
