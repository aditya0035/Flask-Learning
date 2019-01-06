from BlogPost import application
from BlogPost.Logger import Logger
from flask import render_template
from BlogPost.Users.vw import user_blueprint
from BlogPost.Posts.vw import post_blueprint
from BlogPost.Filters.Characters import CharacterLimit
application.register_blueprint(user_blueprint,url_prefix="/user")
application.register_blueprint(post_blueprint,url_prefix="/post")
application.jinja_env.filters['CharacterLimit'] = CharacterLimit
application.config['TESTING'] = False
application.config['LOGIN_DISABLED']=False
'''print(__name__)'''
@application.route("/")
@application.route("/Home")
def Index():
    return render_template("index.html")

if __name__=="__main__":
    Logger.write("application started")
    Logger.write(application.config.get("SQLALCHEMY_DATABASE_URI","Connection String Not Setted"))
    application.run(debug=True)
