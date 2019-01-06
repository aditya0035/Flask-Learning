from BlogPost import application,dataBase
from BlogPost.DataBase.DTO.Users import User,SaveUser

user=User("test","test","test")
SaveUser(user)
print(User.query.all())
