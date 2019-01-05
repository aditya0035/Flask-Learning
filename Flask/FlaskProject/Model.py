import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__name__))
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
Migrate(app,db)
class Puppy(db.Model):
    """docstring for Puppy."""
    __tablename__="puppies"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    toys=db.relationship('Toys',backref='Puppy',lazy='dynamic')
    owner=db.relationship('Owner',backref='Puppy',uselist=False)
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        if(self.owner==None):
            return f'Puppy Name:{self.name},has no owner'
        else:
            return f'Puppy Name:{self.name},Owner{self.owner.name}'
    def Report_Toys(self):
        return f'{self.toys.all()}'

class Toys(db.Model):
    __tablename__="toys"
    Id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppyId=db.Column(db.Integer,db.ForeignKey('puppies.id'))
    def __init__(self,name,puppyid):
        self.name=name
        self.puppyId=puppyid
    def __repr__(self):
        return f"Toy Name:{self.name}"
class Owner(db.Model):
    __tablename__="owner"
    Id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppyId=db.Column(db.Integer,db.ForeignKey('puppies.id'))
    def __init__(self,name,puppyId):
        self.name=name
        self.puppyId=puppyId
