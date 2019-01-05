from flask import render_template,Flask
app=Flask(__name__)

#This is the real world example to use template control flow
@app.route("/")
def UserLogIn():
    is_user_logged_in=False
    return render_template("basic8.html",is_user_logged_in=is_user_logged_in)

if __name__=="__main__":
    app.run(debug=True)
