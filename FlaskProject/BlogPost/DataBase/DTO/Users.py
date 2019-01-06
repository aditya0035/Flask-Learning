from BlogPost import dataBase,login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash
@login_manager.user_loader
def UserLoader(user_id):
    return User.query.get(user_id)

class User(dataBase.Model,UserMixin):
    __tablename='Users'
    Id=dataBase.Column(dataBase.Integer,primary_key=True)
    Username=dataBase.Column(dataBase.Text,unique=True)
    Email=dataBase.Column(dataBase.Text,unique=True)
    PasswordHash=dataBase.Column(dataBase.Text)
    ProfilePic=dataBase.Column(dataBase.BLOB)
    Posts = dataBase.relationship('Posts', backref='User', lazy=True)
    def get_id(self):
        return self.Id
    def __init__(self,Username,Email,Password):
        self.Username=Username
        self.PasswordHash=generate_password_hash(Password)
        self.Email=Email
    def check_password_hash(self,Password):
        return check_password_hash(self.PasswordHash,Password)

    def __repr__(self):
        return f"<clas user>id={self.Id},Email={self.Email},PasswordHash={self.PasswordHash},UserName={self.Username}"

def SaveUser(User):
    dataBase.session.add(User)
    dataBase.session.commit()

def SaveAllUser(*Users):
    dataBase.session.add(Users)
    dataBase.session.commit()
