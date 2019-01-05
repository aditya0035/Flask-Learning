from flask import Flask,render_template
app=Flask(__name__)
is_logged_in=False
@app.route("/")
def index():
    return render_template("home11.html",is_logged_in=is_logged_in)

@app.route("/Login") #it must be define in order to use url_for
def logged_in():
    is_logged_in=True
    return render_template("home11.html",is_logged_in=is_logged_in)

if __name__=="__main__":
    app.run(debug=True)


"""
for use of url_for if pass to an route the use route method names_list
and if need to load a file then use url_for("folder with respect to flask app name",filename="filename")
"""
