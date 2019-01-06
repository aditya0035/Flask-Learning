from BlogPost import dataBase
from datetime import datetime,timezone
from .Users import User

class Posts(dataBase.Model):
    __tablename="Posts"
    Id=dataBase.Column(dataBase.Integer,primary_key=True)
    Title=dataBase.Column(dataBase.Text)
    Description=dataBase.Column(dataBase.Text)
    CreatedDate=dataBase.Column(dataBase.Text)
    ModifiedDate=dataBase.Column(dataBase.Text)
    CreatorId = dataBase.Column(dataBase.Integer, dataBase.ForeignKey(User.Id),
        nullable=False)
    def __init__(self,Title,Description,CreatorId):
        self.CreatorId=CreatorId
        self.Description=Description
        self.Title=Title
        self.CreatedDate=datetime.now(timezone.utc)
        self.ModifiedDate=datetime.now(timezone.utc)
    def __repr__(self):
        return f"<class Posts>Id={self.Id},Title={self.Title},Description={self.Description},CreatedDate={self.CreatedDate},Createdby={self.User.Username}"

def SavePost(title,Description,CreatorId):
    post=Posts(title,Description,CreatorId)
    dataBase.session.add(post)
    dataBase.session.commit()

def GetAllPost(page=0,pageSize=5):
    query = dataBase.session.query(Posts).order_by(Posts.ModifiedDate.desc())
    if pageSize:
        query = query.limit(pageSize)
    if page:
        query = query.offset((page-1)*pageSize)
        print(query)
    return query.all()
def GetPost(postId):
    query =dataBase.session.query(Posts).get(postId)
    return query

def GetTotalPostCount():
    return dataBase.session.query(Posts).count()

def saveEditedPost(postobj,form):
    postobj.Title=form.Title.data
    postobj.Description=form.Text.data
    postobj.ModifiedDate=datetime.now(timezone.utc)
    dataBase.session.add(postobj)
    dataBase.session.commit()
