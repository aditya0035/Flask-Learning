from flask import render_template,redirect,url_for,Blueprint
puppy_blueprint=Blueprint("Puppy",__name__,template_folder="templates/puppy",url_prefix='/puppy')
@puppy_blueprint.route("/")
def index():
    return redirect(url_for("Puppy.home"))
@puppy_blueprint.route("/home")
def home():
    return render_template("home.html")
