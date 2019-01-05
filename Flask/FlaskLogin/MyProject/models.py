from MyProject import db,login_manger
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

@login_manger.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    __tablename__="Users"
    Id=db.Column(db.Integer,primary_key=True)
    Email=db.Column(db.String(64),unique=True,index=True)
    Username=db.Column(db.String(64),unique=True,index=True)
    PasswordHash=db.Column(db.String(128))
    def __init__(self,email,username,pwd):
        self.Email=email
        self.Username=username
        self.PasswordHash=generate_password_hash(pwd)
    def Check_Password(self,pwd):
        return check_password_hash(self.PasswordHash,pwd)
