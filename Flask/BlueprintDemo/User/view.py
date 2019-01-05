from flask import render_template,Blueprint
user_blueprints=Blueprint("User",__name__,template_folder="templates/User",url_prefix='/user')
@user_blueprints.route("/")
def owner():
    return render_template("owner.html")
