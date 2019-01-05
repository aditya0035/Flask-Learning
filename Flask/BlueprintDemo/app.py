from flask import Flask,render_template
from Puppy.view import puppy_blueprint
from User.view import user_blueprints

application=Flask(__name__)
application.register_blueprint(user_blueprints)
application.register_blueprint(puppy_blueprint)

for rule in application.url_map.iter_rules():
    print(rule.endpoint)

@application.route("/")
def index():
    return render_template("index.html")
'''
@application.errorhandler(404)
def NotFound(e):
    return render_template("NotFound.html"),404
'''

if __name__=="__main__":
    application.run(debug=True)
